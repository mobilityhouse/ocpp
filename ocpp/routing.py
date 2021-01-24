from __future__ import annotations
import functools
from abc import ABC, abstractmethod
from typing import Callable, Optional

import asyncio
import inspect
import logging
import re
import time
import uuid
from dataclasses import asdict, dataclass

from ocpp.messages import Call, unpack, validate_payload, MessageType
from ocpp.exceptions import OCPPError, NotImplementedError

routables = []

LOGGER = logging.getLogger("ocpp")


def camel_to_snake_case(data):
    """
    Convert all keys of all dictionaries inside the given argument from
    camelCase to snake_case.

    Inspired by: https://stackoverflow.com/a/1176023/1073222

    """
    if isinstance(data, dict):
        snake_case_dict = {}
        for key, value in data.items():
            s1 = re.sub("(.)([A-Z][a-z]+)", r"\1_\2", key)
            key = re.sub("([a-z0-9])([A-Z])", r"\1_\2", s1).lower()

            snake_case_dict[key] = camel_to_snake_case(value)

        return snake_case_dict

    if isinstance(data, list):
        snake_case_list = []
        for value in data:
            snake_case_list.append(camel_to_snake_case(value))

        return snake_case_list

    return data


def snake_to_camel_case(data):
    """
    Convert all keys of a all dictionaries inside given argument from
    snake_case to camelCase.

    Inspired by: https://stackoverflow.com/a/19053800/1073222
    """
    if isinstance(data, dict):
        camel_case_dict = {}
        for key, value in data.items():
            components = key.split("_")
            key = components[0] + "".join(x.title() for x in components[1:])
            camel_case_dict[key] = snake_to_camel_case(value)

        return camel_case_dict

    if isinstance(data, list):
        camel_case_list = []
        for value in data:
            camel_case_list.append(snake_to_camel_case(value))

        return camel_case_list

    return data


def remove_nones(dict_to_scan):
    dict_to_scan = {k: v for k, v in dict_to_scan.items() if v is not None}
    return dict_to_scan


def on(action, *, skip_schema_validation=False):
    """
    Function decorator to mark function as handler for specific action. The
    wrapped function may be async or sync.

    The handler function will receive keyword arguments derived from the
    payload of the specific action. It's recommended you use `**kwargs` in your
    definition to ignore any extra arguments that may be added in the future.

    The handler function should return a relevant payload to be returned to the
    Charge Point.

    It can be used like so:

    ```
    class MyChargePoint(cp):
        @on(Action.BootNotification):
        async def on_boot_notification(
            self,
            charge_point_model,
            charge_point_vendor,
            **kwargs,
        ):
            print(f'{charge_point_model} from {charge_point_vendor} booted.')

            now = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S') + "Z"
            return call_result.BootNotificationPayload(
                current_time=now,
                interval=30,
                status="Accepted",
            )
    ```

    The decorator takes an optional argument `skip_schema_validation` which
    defaults to False. Setting this argument to `True` will disable schema
    validation of the request and the response of the specific route.

    """

    def decorator(func):
        @functools.wraps(func)
        def inner(*args, **kwargs):
            return func(*args, **kwargs)

        inner._on_action = action
        inner._skip_schema_validation = skip_schema_validation
        if func.__name__ not in routables:
            routables.append(func.__name__)
        return inner

    return decorator


def after(action):
    """Function decorator to mark function as hook to post-request hook.

    This hook's arguments are the data that is in the payload for the specific
    action.

    It can be used like so:

        @after(Action.BootNotification):
        def after_boot_notification():
            pass

    """

    def decorator(func):
        @functools.wraps(func)
        def inner(*args, **kwargs):
            return func(*args, **kwargs)

        inner._after_action = action
        if func.__name__ not in routables:
            routables.append(func.__name__)
        return inner

    return decorator


def create_route_map(obj) -> dict:
    """
    Iterates of all attributes of the class looking for attributes which
    have been decorated by the @on() decorator It returns a dictionary where
    the action name are the keys and the decorated functions are the values.

    To illustrate this with an example, consider the following function:

        class ChargePoint:

            @on(Action.BootNotification)
            def on_boot_notification(self, *args, **kwargs):
                pass

            @after(Action.BootNotification)
            def after_boot_notification(self, *args, **kwargs):
                pass


    In this case this returns:

        {
            Action.BootNotification: {
                '_on_action': <reference to 'on_boot_notification'>,
                '_after_action': <reference to 'after_boot_notification'>,
                '_skip_schema_validation': False,
            },
        }

    """
    routes = {}
    for attr_name in routables:
        for option in ["_on_action", "_after_action"]:
            try:
                attr = getattr(obj, attr_name)
                action = getattr(attr, option)

                if action not in routes:
                    routes[action] = {}

                # Routes decorated with the `@on()` decorator can be configured
                # to skip validation of the input and output. For more info see
                # the docstring of `on()`.
                if option == "_on_action":
                    routes[action]["_skip_schema_validation"] = getattr(
                        attr, "_skip_schema_validation", False
                    )

                routes[action][option] = attr

            except AttributeError:
                continue

    return routes


class Queue(ABC):
    """Queue interface for routing incoming CallResult/CallError."""

    @abstractmethod
    async def get(self) -> str:
        pass

    @abstractmethod
    def put_nowait(self, msg):
        pass


class Connection(ABC):
    """Connection for sending and receiving messages."""

    @abstractmethod
    async def send(self, message: str):
        pass

    @abstractmethod
    async def recv(self) -> str:
        pass


@dataclass
class OCPPAdapter:
    ocpp_version: str
    call: Callable
    call_result: Callable


@dataclass
class Context:
    """Context class allows to inject implementation specific dependencies."""

    connection: Connection
    id: str
    ocpp_adapter: Optional[OCPPAdapter] = None
    response_queue: Optional[Queue] = asyncio.Queue()


class Router:
    """Router base class."""

    def __init__(
        self,
        *,
        context: Optional[Context] = None,
        stateless: Optional[bool] = False,
        response_timeout: Optional[int] = 30,
        create_task: Optional[bool] = True,
    ):
        """Initialize Router instance.

        Args:
            context (Context): Context object this router identity end env.
            stateless (bool): Stateful Router instance's (stateless == False)
                action handlers can use and store data to instance's variables
                (e.g. id) and receive ocpp message attributes as kwargs.
                Stateless Router instance only contains route map of action
                handlers. Action handlers will receive ocpp message in event
                argument and Context object as an additional argument.
            response_timeout (int): When no response on a request is received
                within this interval, a asyncio.TimeoutError is raised.
            create_task (bool): Create asyncio.Task for executing
                "after"-handler. Does not affect "on-handler".
        """
        self.id = context.id if context else None

        # The maximum time in seconds it may take for a CP to respond to a
        # CALL. An asyncio.TimeoutError will be raised if this limit has been
        # exceeded.
        self._response_timeout = response_timeout

        # A connection to the client. Currently this is an instance of gh
        self._connection = context.connection if context else None

        # A dictionary that hooks for Actions. So if the CS receives a it will
        # look up the Action into this map and execute the corresponding hooks
        # if exists.
        self.route_map = {}
        self.include_router(self)

        self._call_lock = asyncio.Lock()

        # A queue used to pass CallResults and CallErrors from
        # the self.serve() task to the self.call() task.
        self._response_queue = asyncio.Queue()

        # Function used to generate unique ids for CALLs. By default
        # uuid.uuid4() is used, but it can be changed. This is meant primarily
        # for testing purposes to have predictable unique ids.
        self._unique_id_generator = uuid.uuid4

        # Use asyncio.create_task for "after"-handler.
        self._create_task = create_task

        # Router operating mode
        self._stateless = stateless

        if not self._stateless and context and context.ocpp_adapter:
            self._ocpp_version = context.ocpp_adapter.ocpp_version
            self._call = context.ocpp_adapter.call
            self._call_result = context.ocpp_adapter.call_result

    def include_router(self, router: Router):
        """Include routes from router to routemap

        Args:
            router (Router): [description]
        """
        routes = create_route_map(router)
        self.route_map.update(routes)

    async def route_message(self, raw_msg, *, context: Context = None):
        """
        Route a message received from a CP.

        If the message is a of type Call the corresponding hooks are executed.
        If the message is of type CallResult or CallError the message is passed
        to the call() function via the response_queue.
        """
        try:
            msg = unpack(raw_msg)
        except OCPPError as e:
            LOGGER.exception(
                "Unable to parse message: '%s', it doesn't seem "
                "to be valid OCPP: %s",
                raw_msg,
                e,
            )
            return

        if msg.message_type_id == MessageType.Call:
            await self._handle_call(msg, context=context)

        elif msg.message_type_id in [
            MessageType.CallResult,
            MessageType.CallError,
        ]:
            response_queue: Queue = (
                context.queue if context else self._response_queue
            )
            response_queue.put_nowait(msg)

    async def _handle_call(self, msg, *, context: Context = None):
        """
        Execute all hooks installed for based on the Action of the message.

        First the '_on_action' hook is executed and its response is returned to
        the client. If there is no '_on_action' hook for Action in the message
        a CallError with a NotImplemtendError is returned.

        Next the '_after_action' hook is executed.

        """
        ocpp_version = (
            context.ocpp_adapter.ocpp_version
            if context
            else self._ocpp_version
        )

        try:
            handlers = self.route_map[msg.action]
        except KeyError:
            raise NotImplementedError(
                f"No handler for '{msg.action}' " "registered."
            )

        if not handlers.get("_skip_schema_validation", False):
            validate_payload(msg, ocpp_version)

        # OCPP uses camelCase for the keys in the payload. It's more pythonic
        # to use snake_case for keyword arguments. Therefore the keys must be
        # 'translated'. Some examples:
        #
        # * chargePointVendor becomes charge_point_vendor
        # * firmwareVersion becomes firmwareVersion
        snake_case_payload = camel_to_snake_case(msg.payload)

        try:
            handler = handlers["_on_action"]
        except KeyError:
            raise NotImplementedError(
                f"No handler for '{msg.action}' " "registered."
            )

        try:
            # NOTE!!! This brakes backward compatibility if stateless way is
            # used. Event based router should not contain other that route map
            # (i.e route map should not be build again for every invocation).
            # This means that router can't have information that's currently
            # defined in ChargePoint e.g. id, ocpp_version, call etc...
            # TODO: Maybe use inspect.signature to maintain compatibility?
            if self._stateless:
                response = handler(event=snake_case_payload, context=context)
            else:
                response = handler(**snake_case_payload)
            if inspect.isawaitable(response):
                response = await response
        except Exception as e:
            LOGGER.exception("Error while handling request '%s'", msg)
            response = msg.create_call_error(e).to_json()
            await self._send(response)

        temp_response_payload = asdict(response)

        # Remove nones ensures that we strip out optional arguments
        # which were not set and have a default value of None
        response_payload = remove_nones(temp_response_payload)

        # The response payload must be 'translated' from snake_case to
        # camelCase. So:
        #
        # * charge_point_vendor becomes chargePointVendor
        # * firmware_version becomes firmwareVersion
        camel_case_payload = snake_to_camel_case(response_payload)

        response = msg.create_call_result(camel_case_payload)

        if not handlers.get("_skip_schema_validation", False):
            validate_payload(response, ocpp_version)

        await self._send(response.to_json(), context=context)

        try:
            handler = handlers["_after_action"]
            # NOTE!!! Braking change as is "on"-handler
            if self._stateless:
                response = handler(event=snake_case_payload, context=context)
            else:
                response = handler(**snake_case_payload)
            if inspect.isawaitable(response):
                if self._create_task:
                    # Create task to avoid blocking when making a call
                    # inside the after handler
                    asyncio.ensure_future(response)
                else:
                    await response
        except KeyError:
            # '_on_after' hooks are not required. Therefore ignore exception
            # when no '_on_after' hook is installed.
            pass

    async def call(self, payload, suppress=True, *, context: Context = None):
        """
        Send Call message to client and return payload of response.

        The given payload is transformed into a Call object by looking at the
        type of the payload. A payload of type BootNotificationPayload will
        turn in a Call with Action BootNotification, a HeartbeatPayload will
        result in a Call with Action Heartbeat etc.

        A timeout is raised when no response has arrived before expiring of
        the configured timeout.

        When waiting for a response no other Call message can be send. So this
        function will wait before response arrives or response timeout has
        expired. This is in line the OCPP specification

        Suppress is used to maintain backwards compatibility. When set to True,
        if response is a CallError, then this call will be suppressed. When
        set to False, an exception will be raised for users to handle this
        CallError.

        """
        ocpp_version = (
            context.ocpp_adapter.ocpp_version
            if context
            else self._ocpp_version
        )

        camel_case_payload = snake_to_camel_case(asdict(payload))

        call = Call(
            unique_id=str(self._unique_id_generator()),
            action=payload.__class__.__name__[:-7],
            payload=remove_nones(camel_case_payload),
        )

        validate_payload(call, ocpp_version)

        # Use a lock to prevent make sure that only 1 message can be send at a
        # a time.
        async with self._call_lock:
            await self._send(call.to_json(), context=context)
            response = await self._get_specific_response(
                call.unique_id, self._response_timeout, context=context
            )

        if response.message_type_id == MessageType.CallError:
            LOGGER.warning("Received a CALLError: %s'", response)
            if suppress:
                return
            raise response.to_exception()
        else:
            response.action = call.action
            validate_payload(response, ocpp_version)

        snake_case_payload = camel_to_snake_case(response.payload)
        # Create the correct Payload instance based on the received payload. If
        # this method is called with a call.BootNotificationPayload, then it
        # will create a call_result.BootNotificationPayload. If this method is
        # called with a call.HeartbeatPayload, then it will create a
        # call_result.HeartbeatPayload etc.
        call_result = (
            context.ocpp_adapter.call_result if context else self._call_result
        )
        cls = getattr(call_result, payload.__class__.__name__)  # noqa
        return cls(**snake_case_payload)

    async def _get_specific_response(
        self, unique_id, timeout, *, context: Context = None
    ):
        """
        Return response with given unique ID or raise an asyncio.TimeoutError.
        """
        wait_until = time.time() + timeout
        try:
            # Wait for response of the Call message.
            response_queue = context.queue if context else self._response_queue
            response = await asyncio.wait_for(response_queue.get(), timeout)
        except asyncio.TimeoutError:
            raise

        if response.unique_id == unique_id:
            return response

        LOGGER.error("Ignoring response with unknown unique id: %s", response)
        timeout_left = wait_until - time.time()

        if timeout_left < 0:
            raise asyncio.TimeoutError

        return await self._get_specific_response(
            unique_id, timeout_left, context=context
        )

    async def _send(self, message, *, context: Context = None):
        LOGGER.info("%s: send %s", self.id, message)
        connection = context.connection if context else self._connection
        await connection.send(message)
