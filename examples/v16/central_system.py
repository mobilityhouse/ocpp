import asyncio
import logging
from datetime import datetime
from typing import List

import websockets

from ocpp.routing import on
from ocpp.v16 import ChargePoint as cp
from ocpp.v16 import call_result
from ocpp.v16.enums import Action, RegistrationStatus, AuthorizationStatus, RemoteStartStopStatus

logging.basicConfig(level=logging.INFO)

class ChargePoint(cp):
    @on(Action.BootNotification)
    def on_boot_notification(self, charge_point_vendor: str, charge_point_model: str, **kwargs):
        return call_result.BootNotificationPayload(
            current_time=datetime.utcnow().isoformat(),
            interval=10,
            status=RegistrationStatus.accepted,
        )

    @on(Action.Authorize)
    def on_authorize(self, id_tag: str):
        return call_result.AuthorizePayload(
            id_tag_info=call_result.IdTagInfo(
                status=AuthorizationStatus.accepted,
                parent_id_tag=id_tag,
                expiry_date="2025/01/01"
            )
        )

    @on(Action.RemoteStartTransaction)
    def on_remote_start_transaction(self, id_tag: str, **kwargs):
        return call_result.RemoteStartTransactionPayload(
            status=RemoteStartStopStatus.accepted
        )

    @on(Action.RemoteStopTransaction)
    def on_remote_end_transaction(self, transaction_id: int):
        return call_result.RemoteStopTransactionPayload(
            status=RemoteStartStopStatus.accepted
        )

    @on(Action.MeterValues)
    def on_meter_values(self, connector_id: int, meter_value: List, **kwargs):
        for meter_value_entry in meter_value:
            print(f'Timestamp {meter_value_entry["timestamp"]}')
            for sampled_value_entry in meter_value_entry["sampled_value"]:
                print(sampled_value_entry)
        return call_result.MeterValuesPayload()

async def on_connect(websocket, path):
    """For every new charge point that connects, create a ChargePoint
    instance and start listening for messages.
    """
    try:
        requested_protocols = websocket.request_headers["Sec-WebSocket-Protocol"]
    except KeyError:
        logging.error("Client hasn't requested any Subprotocol. Closing Connection")
        return await websocket.close()
    if websocket.subprotocol:
        logging.info("Protocols Matched: %s", websocket.subprotocol)
    else:
        # In the websockets lib if no subprotocols are supported by the
        # client and the server, it proceeds without a subprotocol,
        # so we have to manually close the connection.
        logging.warning(
            "Protocols Mismatched | Expected Subprotocols: %s,"
            " but client supports  %s | Closing connection",
            websocket.available_subprotocols,
            requested_protocols,
        )
        return await websocket.close()

    charge_point_id = path.strip("/")
    cp = ChargePoint(charge_point_id, websocket)

    await cp.start()

async def main():
    server = await websockets.serve(
        on_connect, "0.0.0.0", 9000, subprotocols=["ocpp1.6"]
    )
    logging.info("Server Started listening to new connections...")
    await server.wait_closed()

if __name__ == "__main__":
    # asyncio.run() is used when running this example with Python >= 3.7v
    asyncio.run(main())