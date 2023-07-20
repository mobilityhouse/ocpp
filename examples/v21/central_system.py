import asyncio
import logging
import pathlib
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

from ocpp.messages import SchemaValidator
from ocpp.routing import on
from ocpp.v21 import ChargePoint as cp
from ocpp.v21 import call_result
from ocpp.v21.enums import RegistrationStatus

logging.basicConfig(level=logging.INFO)

# The ocpp package doesn't come with the JSON schemas for OCPP 2.1.
# See https://github.com/mobilityhouse/ocpp/issues/458 for more details.
schemas_dir = str(pathlib.Path(__file__).parent.joinpath("schemas").resolve())
validator = SchemaValidator(schemas_dir)


class ChargePoint(cp):
    @on("BootNotification")
    def on_boot_notification(self, reason: str, charging_station: str, **kwargs):
        return call_result.BootNotification(
            current_time=datetime.now(timezone.utc).isoformat(),
            interval=10,
            status=RegistrationStatus.accepted,
        )


async def on_connect(websocket, path):
    charge_point_id = path.strip("/")
    cp = ChargePoint(charge_point_id, websocket, validator)

    await cp.start()


async def main():
    server = await websockets.serve(
        on_connect, "0.0.0.0", 9000, subprotocols=["ocpp2.1"]
    )

    logging.info("Server Started listening to new connections...")
    await server.wait_closed()


if __name__ == "__main__":
    asyncio.run(main())
