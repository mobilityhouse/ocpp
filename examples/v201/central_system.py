import asyncio
import logging
from datetime import datetime, timezone

try:
    import websockets
except ModuleNotFoundError:
    print("This example relies on the 'websockets' package.")
    print("Please install it by running: ")
    print()
    print(" $ pip install websockets")
    import sys

    sys.exit(1)

from ocpp.routing import on
from ocpp.v201 import ChargePoint as cp
from ocpp.v201 import call_result

logging.basicConfig(level=logging.INFO)

class ChargePoint(cp):
    @on("BootNotification")
    def on_boot_notification(self, charging_station, reason, **kwargs):
        return call_result.BootNotification(
            current_time=datetime.now(timezone.utc).isoformat(), interval=10, status="Accepted"
        )

    @on("Heartbeat")
    def on_heartbeat(self):
        return call_result.Heartbeat(
            current_time=datetime.now(timezone.utc).strftime()
        )

    @on("CancelReservation")
    def on_cancel_reservation(self, reservation_id):    
        return call_result.CancelReservation(
            status="Accepted",
        )

    @on("StatusNotification")
    def on_Status_Notification(self,**kwargs):
        return call_result.StatusNotification()
    
    @on("SecurityEventNotification")
    def on_SecurityEventNotification(self, **kwargs):
        return call_result.SecurityEventNotification()

    @on("Authorize")
    def on_authorize(self, **kwargs):
        # logging.info(f"Received Authorize request with id_token: {id_token}")
        return call_result.Authorize(id_token_info={"status": "Accepted"})

    @on('MeterValues')
    def on_meter_values(self, **kwargs):
        logging.info("Received MeterValues.")
        return call_result.MeterValues()

    @on("ReportChargingProfiles")
    def on_report_charging_profiles(self, custom_data=None, **kwargs):
        logging.info(f"Received ReportChargingProfiles with custom_data: {custom_data}, kwargs: {kwargs}")
        # Process the ReportChargingProfiles request here, if needed.

        # Return the result with a status, e.g., "Accepted".
        return call_result.ReportChargingProfiles()

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
            " but client supports %s | Closing connection",
            websocket.available_subprotocols,
            requested_protocols,
        )
        return await websocket.close()

    charge_point_id = path.strip("/")
    charge_point = ChargePoint(charge_point_id, websocket)

    await charge_point.start()

async def main():
    #  deepcode ignore BindToAllNetworkInterfaces: <Example Purposes>
    server = await websockets.serve(
        on_connect, "192.168.0.102", 9000, subprotocols=["ocpp2.0.1"]
    )

    logging.info("Server Started listening to new connections...")
    await server.wait_closed()


if __name__ == "__main__":
    # asyncio.run() is used when running this example with Python >= 3.7v
    asyncio.run(main())