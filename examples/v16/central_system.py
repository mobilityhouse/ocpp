import asyncio
import aioconsole
import logging
from datetime import datetime
import ssl
import pathlib

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
from ocpp.v16 import ChargePoint as cp
from ocpp.v16.enums import Action, RegistrationStatus
from ocpp.v16 import call_result, call

logging.basicConfig(level=logging.INFO)


class ChargePoint(cp):
    #########################################################################
    # The messages below during regular idle operation of the charger
    #########################################################################

    @on(Action.BootNotification)
    def on_boot_notification(
        self, charge_point_vendor: str, charge_point_model: str, **kwargs
    ):
        t = datetime.utcnow().isoformat()
        return call_result.BootNotificationPayload(
            current_time=t + "Z", interval=10, status=RegistrationStatus.accepted
        )

    @on(Action.StatusNotification)
    def on_status_notification(self, connector_id: int, **kwargs):
        return call_result.StatusNotificationPayload()

    @on(Action.Heartbeat)
    def on_heartbeat(self, **kwargs):
        t = datetime.utcnow().isoformat()
        return call_result.HeartbeatPayload(current_time=t + "Z")

    @on(Action.FirmwareStatusNotification)
    def on_firmware_status(self, **kwargs):
        return call_result.FirmwareStatusNotificationPayload()

    @on(Action.MeterValues)
    def on_meter_values(self, **kwargs):
        return call_result.MeterValuesPayload()

    #########################################################################
    # The messages below occur asynchronously with user action
    #########################################################################

    @on(Action.Authorize)
    def on_authorize(self, id_tag: str, **kwargs):
        return call_result.AuthorizePayload(id_tag_info={"status": "Accepted"})

    @on(Action.StartTransaction)
    def on_start_transaction(
        self, connector_id: int, id_tag: str, meter_start: int, timestamp: str, **kwargs
    ):
        return call_result.StartTransactionPayload(
            transaction_id=1234, id_tag_info={"status": "Accepted"}
        )

    @on(Action.StopTransaction)
    def on_stop_transaction(self, **kwargs):
        return call_result.StopTransactionPayload(id_tag_info={"status": "Accepted"})


#########################################################################
# Helper functions for CLI commands below
#########################################################################


async def send_remote_start(cp):
    # await asyncio.sleep(1)

    # Send a remote start
    msg = call.RemoteStartTransactionPayload(id_tag="DEADBEEF")
    await cp.call(msg)


async def send_remote_stop(cp):
    # await asyncio.sleep(1)

    # Send a remote stop
    msg = call.RemoteStopTransactionPayload(transaction_id=1234)
    await cp.call(msg)


async def send_update_firmware(cp):
    # await asyncio.sleep(1)

    # Send update firmware
    t = datetime.utcnow().isoformat()
    msg = call.UpdateFirmwarePayload(
        location="sftp://username:password@my.ftphost.com/update.tgz",
        retrieve_date=t + "Z",
    )
    await cp.call(msg)


async def send_clear_cache(cp):
    # Send clear cache
    msg = call.ClearCachePayload()
    await cp.call(msg)


async def send_tx_profile(cp):
    # Send tx profile
    msg = call.SetChargingProfilePayload(
        connector_id=0,
        cs_charging_profiles={
            "chargingProfileId": 1111,
            "stackLevel": 1,
            "chargingProfilePurpose": "ChargePointMaxProfile",
            "chargingProfileKind": "Relative",
            "chargingSchedule": {
                "chargingRateUnit": "A",
                "chargingSchedulePeriod": [{"startPeriod": 0, "limit": 0.0}],
            },
        },
    )
    await cp.call(msg)


async def clear_tx_profile(cp):
    # Clear tx profile
    msg = call.ClearChargingProfilePayload(id=1111, connector_id=0)
    await cp.call(msg)


async def send_change_config(cp):
    # Send change config
    msg = call.ChangeConfigurationPayload(key="SmartChargingEnabled", value="true")
    await cp.call(msg)


async def send_trigger(cp):
    # Send trigger req
    msg = call.TriggerMessagePayload(requested_message="StatusNotification")
    await cp.call(msg)


async def send_data_transfer(cp):
    # Send data transfer req
    msg = call.DataTransferPayload(
        vendor_id="INVALID-VENDOR"  # Triggers a Rejected response
    )
    await cp.call(msg)


async def send_soft_reset(cp):
    # Send soft reset req
    msg = call.ResetPayload(type="Soft")
    await cp.call(msg)


async def send_hard_reset(cp):
    # Send hard reset req
    msg = call.ResetPayload(type="Hard")
    await cp.call(msg)


#########################################################################
# A callback for charger connected
#########################################################################


async def on_connect(websocket, path):
    """ For every new charge point that connects, create a ChargePoint
    instance and start listening for messages.
    """
    try:
        requested_protocols = websocket.request_headers["Sec-WebSocket-Protocol"]
    except KeyError:
        logging.error("Client hasn't requested any Subprotocol. Closing Connection")
        return await websocket.close()

    if "Authorization" in websocket.request_headers:
        logging.info(
            "Got Authorization: {}".format(websocket.request_headers["Authorization"])
        )

    # logging.info("Got headers {}".format(websocket.request_headers))

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

    console_task = asyncio.create_task(console(cp))

    await cp.start()

    await console_task


#########################################################################
# Implements CLI, to be run in an asyncio task
#########################################################################


async def console(cp):
    try:
        logging.info("Started console")
        while True:
            line = await aioconsole.ainput(">")
            if "help" in line:
                logging.info("TODO Create help menu")
            elif "send-remote-start" in line:
                task = asyncio.create_task(send_remote_start(cp))
                await task
            elif "send-remote-stop" in line:
                task = asyncio.create_task(send_remote_stop(cp))
                await task
            elif "send-update-firmware" in line:
                task = asyncio.create_task(send_update_firmware(cp))
                await task
            elif "send-tx-profile" in line:
                task = asyncio.create_task(send_tx_profile(cp))
                await task
            elif "clear-tx-profile" in line:
                task = asyncio.create_task(clear_tx_profile(cp))
                await task
            elif "clear-cache" in line:
                task = asyncio.create_task(send_clear_cache(cp))
                await task
            elif "change-config" in line:
                task = asyncio.create_task(send_change_config(cp))
                await task
            elif "send-trigger" in line:
                task = asyncio.create_task(send_trigger(cp))
                await task
            elif "send-data-transfer" in line:
                task = asyncio.create_task(send_data_transfer(cp))
                await task
            elif "send-soft-reset" in line:
                task = asyncio.create_task(send_soft_reset(cp))
                await task
            elif "send-hard-reset" in line:
                task = asyncio.create_task(send_hard_reset(cp))
                await task
            else:
                logging.info("Unknown command: {}".format(line))
    except Exception as e:
        logging.error("Caught exception {}".format(e))


#########################################################################
# The main task
#########################################################################


async def main():
    # TODO Uncomment to use certificates
    # ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    # localhost_pem = pathlib.Path(__file__).with_name("cert.pem")
    # localhost_key = pathlib.Path(__file__).with_name("key.pem")
    # ssl_context.load_cert_chain(localhost_pem, localhost_key)

    server = await websockets.serve(
        on_connect,
        "0.0.0.0",
        9000,
        subprotocols=["ocpp1.6"],
        # ssl=ssl_context
    )

    logging.info("Server Started listening to new connections...")
    await server.wait_closed()


#########################################################################
# Entry point
#########################################################################

if __name__ == "__main__":
    try:
        # asyncio.run() is used when running this example with Python 3.7 and
        # higher.
        asyncio.run(main())
    except AttributeError:
        # For Python 3.6 a bit more code is required to run the main() task on
        # an event loop.
        loop = asyncio.get_event_loop()
        loop.run_until_complete(main())
        loop.close()
