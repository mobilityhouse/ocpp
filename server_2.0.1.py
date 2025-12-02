
# server_2.0.1.py
import asyncio
import base64
import logging
import websockets
from datetime import datetime, timezone

from ocpp.routing import on
from ocpp.v201 import ChargePoint as cp
from ocpp.v201 import call_result
from ocpp.v201.enums import Action, RegistrationStatusEnumType, AuthorizationStatusEnumType
USERNAME = "SE1T2525300231"
PASSWORD = "a49b503d0a0d4b7090fba607460c8807"

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
)
logging.getLogger("ocpp").setLevel(logging.INFO)
logging.getLogger("websockets.server").setLevel(logging.INFO)

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





class MyChargePoint(cp):
    @on(Action.boot_notification)
    async def on_boot_notification(self, charging_station, reason, **kwargs):
        logging.info(f"[OCPP RECV] BootNotification station={charging_station}, reason={reason}")
        return call_result.BootNotification(
            current_time=datetime.now(tz=timezone.utc).isoformat(),
            interval=60,  # Set heartbeat interval to 60s for production
            status=RegistrationStatusEnumType.accepted,
        )

    @on(Action.heartbeat)
    async def on_heartbeat(self, **kwargs):
        logging.info("[OCPP RECV] Heartbeat")
        return call_result.Heartbeat(
            current_time=datetime.now(tz=timezone.utc).isoformat()
        )

    @on(Action.status_notification)
    async def on_status_notification(self, timestamp, connector_id, connector_status, evse_id, **kwargs):
        logging.info(f"[OCPP RECV] StatusNotification evse_id={evse_id}, connector_id={connector_id}, status={connector_status}")
        return call_result.StatusNotification()

    @on(Action.authorize)
    async def on_authorize(self, id_token, **kwargs):
        logging.info(f"[OCPP RECV] Authorize id_token={id_token}")
        # For now, accept all tokens
        return call_result.Authorize(
            id_token_info={"status": AuthorizationStatusEnumType.accepted}
        )

    @on(Action.transaction_event)
    async def on_transaction_event(self, event_type, timestamp, transaction_info, **kwargs):
        logging.info(f"[OCPP RECV] TransactionEvent type={event_type}, transaction_info={transaction_info}")
        # Respond with empty payload (spec allows this)
        return call_result.TransactionEvent()

    @on(Action.meter_values)
    async def on_meter_values(self, evse_id, meter_value, **kwargs):
        logging.info(f"[OCPP RECV] MeterValues evse_id={evse_id}, meter_value={meter_value}")
        return call_result.MeterValues()



# websockets.WebSocketServerProtocol was deprecated; ServerConnection is used by websockets.serve
async def on_connect(connection: websockets.ServerConnection):
    auth_header = connection.request.headers.get("Authorization")
    if not auth_header or not auth_header.startswith("Basic "):
        logging.warning("[AUTH] Missing or invalid Authorization header")
        await connection.close(code=1008, reason="Unauthorized")
        return

    try:
        encoded = auth_header.split(" ", 1)[1]
        decoded = base64.b64decode(encoded).decode("utf-8")
        logging.info(f"[AUTH DEBUG] Encoded credentials: {encoded}")
        logging.info(f"[AUTH DEBUG] Decoded credentials: {decoded}")
        user_pwd = decoded.split(":", 1)
        if len(user_pwd) != 2:
            logging.warning("[AUTH] Malformed credentials format")
            await connection.close(code=1008, reason="Unauthorized")
            return
        user, pwd = user_pwd
    except Exception as e:
        logging.warning(f"[AUTH] Malformed credentials: {e}")
        await connection.close(code=1008, reason="Unauthorized")
        return

    if user != USERNAME or pwd != PASSWORD:
        logging.warning(f"[AUTH] Invalid credentials for user={user}")
        await connection.close(code=1008, reason="Unauthorized")
        return

    logging.info(f"[AUTH] Authenticated user={user}")

    charge_point_id = connection.request.path.split("/")[-1]
    logging.info(f"[CONNECT] ChargePoint ID={charge_point_id}, subprotocol={connection.subprotocol}")

    wrapped_ws = LoggingWebSocket(connection, charge_point_id)
    charge_point = MyChargePoint(charge_point_id, wrapped_ws)

    try:
        await charge_point.start()
    except Exception as e:
        logging.exception(f"[ERROR] {charge_point_id}: {e}")
    finally:
        logging.info(f"[DISCONNECT] {charge_point_id}")

async def main():
    server = await websockets.serve(
        on_connect,
        "0.0.0.0",
        9000,
        subprotocols=["ocpp2.0.1"],
    )
    logging.info("[SERVER] Listening on 0.0.0.0:9000 (OCPP 2.0.1 + Basic Auth)")
    await server.wait_closed()

if __name__ == "__main__":
    asyncio.run(main())
