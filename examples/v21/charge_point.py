import asyncio
import logging
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

from ocpp.messages import SchemaValidator
from ocpp.v21 import ChargePoint as cp
from ocpp.v21 import call, call_result
from ocpp.v21.datatypes import ChargingStation
from ocpp.v21.enums import BootReason, RegistrationStatus

logging.basicConfig(level=logging.INFO)

schemas_dir = pathlib.Path(__file__).parent.joinpath("schemas").resolve()
validator = SchemaValidator(str(schemas_dir))


class ChargePoint(cp):
    async def send_boot_notification(self):
        request = call.BootNotification(
            reason=BootReason.power_up,
            charging_station=ChargingStation(
                model="Virtual Charge Point",
                vendor_name="y",
            ),
        )

        response: call_result.BootNotification = await self.call(request)

        if response.status == RegistrationStatus.accepted:
            print("Connected to central system.")


async def main():
    async with websockets.connect(
        "ws://localhost:9000/CP_1", subprotocols=["ocpp2.1"]
    ) as ws:
        cp = ChargePoint("CP_1", ws, validator)

        await asyncio.gather(cp.start(), cp.send_boot_notification())


if __name__ == "__main__":
    asyncio.run(main())
