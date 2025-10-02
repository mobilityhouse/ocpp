import functools

routables = []
global_hooks = []


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
        @on(Action.boot_notification):
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

        @after(Action.boot_notification):
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


def before_message(func):
    """
    Function decorator to mark function as a global hook that runs before
    any message processing. The wrapped function may be async or sync.

    The hook function will receive the raw message as its first argument.
    It's recommended you use `**kwargs` in your definition to ignore any
    extra arguments that may be added in the future.

    The hook function should not return anything.

    It can be used like so:

    ```
    class MyChargePoint(cp):
        @before_message
        async def log_incoming_message(self, raw_msg, **kwargs):
            await self.db.save_message(raw_msg)
    ```
    """

    @functools.wraps(func)
    def inner(*args, **kwargs):
        return func(*args, **kwargs)

    inner._before_message = True
    if func.__name__ not in global_hooks:
        global_hooks.append(func.__name__)
    return inner


def after_message(func):
    """
    Function decorator to mark function as a global hook that runs after
    any message processing. The wrapped function may be async or sync.

    The hook function will receive the raw message as its first argument
    and the parsed message as its second argument.

    It can be used like so:

    ```
    class MyChargePoint(cp):
        @after_message
        async def log_processed_message(self, raw_msg, parsed_msg, **kwargs):
            await self.db.update_message_status(parsed_msg.unique_id, 'processed')
    ```
    """

    @functools.wraps(func)
    def inner(*args, **kwargs):
        return func(*args, **kwargs)

    inner._after_message = True
    if func.__name__ not in global_hooks:
        global_hooks.append(func.__name__)
    return inner


def create_route_map(obj):
    """
    Iterates of all attributes of the class looking for attributes which
    have been decorated by the @on() decorator It returns a dictionary where
    the action name are the keys and the decorated functions are the values.

    To illustrate this with an example, consider the following function:

        class ChargePoint:

            @on(Action.boot_notification)
            def on_boot_notification(self, *args, **kwargs):
                pass

            @after(Action.boot_notification)
            def after_boot_notification(self, *args, **kwargs):
                pass


    In this case this returns:

        {
            Action.boot_notification: {
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


def discover_message_hooks(obj):
    """
    Discovers and organizes global message hooks from decorated methods.

    Returns a dictionary with hook types as keys and lists of handlers as values.
    """
    hooks = {
        "before_message": [],
        "after_message": [],
    }

    for attr_name in global_hooks:
        try:
            attr = getattr(obj, attr_name)

            if hasattr(attr, "_before_message"):
                hooks["before_message"].append(attr)
            if hasattr(attr, "_after_message"):
                hooks["after_message"].append(attr)

        except AttributeError:
            continue

    return hooks
