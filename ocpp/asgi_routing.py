# ASGIRouter can also be excluded from ocpp-library

from enum import Enum

from ocpp.routing import Router as RouterBase, Context, Connection, OCPPAdapter
from ocpp.v201 import call_result as v201_call_result, call as v201_call
from ocpp.v20 import call_result as v20_call_result, call as v20_call
from ocpp.v16 import call_result as v16_call_result, call as v16_call

from typing import MutableMapping, Any, Callable, Awaitable

Scope = MutableMapping[str, Any]
Message = MutableMapping[str, Any]

Receive = Callable[[], Awaitable[Message]]
Send = Callable[[Message], Awaitable[None]]

ASGIApp = Callable[[Scope, Receive, Send], Awaitable[None]]


class Subprotocols(str, Enum):
    ocpp16 = "ocpp1.6"
    ocpp20 = "ocpp2.0"
    ocpp201 = "ocpp2.0.1"


ocpp_adapters = {
    Subprotocols.ocpp201: OCPPAdapter(
        call=v201_call, call_result=v201_call_result, ocpp_version="2.0.1"
    ),
    Subprotocols.ocpp20: OCPPAdapter(
        call=v20_call, call_result=v20_call_result, ocpp_version="2.0"
    ),
    Subprotocols.ocpp16: OCPPAdapter(
        call=v16_call, call_result=v16_call_result, ocpp_version="1.6"
    ),
}


class ASGIConnection(Connection):
    """Connection for sending and receiving messages."""

    def __init__(self, send: Send, receive: Receive):
        self._send = send
        # self._receive is not set as receive happens via ASGI interface

    async def send(self, message: str):
        await self._send({"type": "websocket.send", "text": message})

    async def recv(self) -> str:
        raise NotImplementedError


def websocket_context(scope: Scope, receive: Receive, send: Send) -> Context:
    id = scope["path"].strip("/")
    subprotocols = scope["subprotocols"][0]
    # Pick the highest matching subprotocol
    if Subprotocols.ocpp201 in subprotocols:
        ocpp_adapter = ocpp_adapters[Subprotocols.ocpp201]
    elif Subprotocols.ocpp20 in subprotocols:
        ocpp_adapter = ocpp_adapters[Subprotocols.ocpp201]
    elif Subprotocols.ocpp16 in subprotocols:
        ocpp_adapter = ocpp_adapters[Subprotocols.ocpp16]
    else:
        raise ValueError
    context = Context(
        connection=ASGIConnection(send, receive),
        id=id,
        ocpp_adapter=ocpp_adapter,
    )
    return context


class Router(RouterBase):
    """ASGI compatible router."""

    async def __call__(
        self, scope: Scope, receive: Receive, send: Send
    ) -> None:
        """ASGI signature handler.

        Args:
            scope (Scope): ASGI scope
            receive (Receive): ASGI handle for receiving messages
            send (Send): ASGI handle for sending messages
        """
        if scope["type"] == "lifespan":
            await self._lifecycle_handler(scope, receive, send)
        elif scope["type"] == "websocket":
            await self._websocket_handler(scope, receive, send)
        elif scope["type"] == "http":
            await self._http_handler(scope, receive, send)
        else:
            raise ValueError(f'Unsupported ASGI scope type: {scope["type"]}')

    async def _lifecycle_handler(self, scope, receive, send):
        event = await receive()
        if event["type"] == "lifespan.startup":
            await send({"type": "lifespan.startup.complete"})
        elif event["type"] == "lifespan.shutdown":
            await send({"type": "lifespan.shutdown.complete"})

    async def _websocket_handler(self, scope, receive, send):
        while True:
            event = await receive()
            context = websocket_context(scope, receive, send)
            if event["type"] == "websocket.receive":
                if "text" not in event:
                    # OCPP-J message is never binary.
                    raise ValueError
                message = event["text"]
                await self.on_receive(message, context=context)
            elif event["type"] == "websocket.connect":
                await self.on_connect(context)
                await send({"type": "websocket.accept"})
            elif event["type"] == "websocket.disconnect":
                await self.on_disconnect(context)
                await send({"type": "websocket.close"})

    async def _http_handler(self, scope, receive, send):
        # ASGI http.request event type handling can be extended in subclasses
        # as interface between "Service" and "ASGI server" depends about
        # the used service (e.g. AWS).
        pass

    async def on_connect(self, context):
        if not self._stateless:
            # Actual implementation for stateful router missing
            raise NotImplementedError

    async def on_disconnect(self, context):
        if not self._stateless:
            # Actual implementation for stateful router missing
            raise NotImplementedError

    async def on_receive(self, message, context):
        if self._stateless:
            await self.route_message(message, context=context)
        else:
            # Actual implementation for stateful router missing
            raise NotImplementedError
