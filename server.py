
# server.py
import asyncio
import logging
import websockets
from datetime import datetime, timezone

from ocpp.routing import on
from ocpp.v16 import ChargePoint as cp
from ocpp.v16 import call_result
from ocpp.v16.enums import Action, RegistrationStatus

# -------------------------
# Logging Configuration
# -------------------------
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
)

logging.getLogger("root").setLevel(logging.INFO)
logging.getLogger("websockets.server").setLevel(logging.WARNING)
logging.getLogger("ocpp").setLevel(logging.DEBUG)



# -------------------------
# Wrapper for raw message logging
# -------------------------
class LoggingWebSocket:
    def __init__(self, ws, tag):
        self.ws = ws
        self.tag = tag

    async def recv(self):
        msg = await self.ws.recv()
        logging.info(f"[RAW RECV] <- {self.tag}: {msg}")
        return msg

    async def send(self, msg):
        logging.info(f"[RAW SEND] -> {self.tag}: {msg}")
        return await self.ws.send(msg)

    def __getattr__(self, name):
        return getattr(self.ws, name)


# -------------------------
# OCPP ChargePoint Implementation
# -------------------------
class MyChargePoint(cp):
    @on(Action.boot_notification)
    async def on_boot_notification(
        self, charge_point_vendor, charge_point_model, **kwargs
    ):
        logging.info(
            f"[OCPP RECV] BootNotification vendor={charge_point_vendor}, model={charge_point_model}, extras={kwargs}"
        )

        response = call_result.BootNotification(
            current_time=datetime.now(tz=timezone.utc).isoformat(),
            interval=10,
            status=RegistrationStatus.accepted,
        )

        logging.info(f"[OCPP SEND] BootNotificationResponse: {response}")
        return response


# -------------------------
# Connection Handler
# -------------------------
async def on_connect(connection: websockets.WebSocketServerProtocol):
    charge_point_id = connection.request.path.split("/")[-1]
    logging.info(f"[CONNECT] ChargePoint ID={charge_point_id}, subprotocol={connection.subprotocol}")

    # Wrap the websocket for raw logging
    wrapped_ws = LoggingWebSocket(connection, charge_point_id)

    charge_point = MyChargePoint(charge_point_id, wrapped_ws)

    try:
        await charge_point.start()
    except Exception as e:
        logging.exception(f"[ERROR] {charge_point_id}: {e}")
    finally:
        logging.info(f"[DISCONNECT] {charge_point_id}")


# -------------------------
# Main Server
# -------------------------
async def main():
    server = await websockets.serve(
        on_connect,
        "0.0.0.0",
        9000,
        subprotocols=["ocpp1.6"],
    )
    logging.info("[SERVER] Listening on 0.0.0.0:9000 (OCPP 1.6)")
    await server.wait_closed()


if __name__ == "__main__":
    asyncio.run(main())
