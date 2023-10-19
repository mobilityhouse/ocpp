import asyncio
import logging
import time

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
from ocpp.v16.enums import Action, RegistrationStatus, PNCMessageIDType
from ocpp.v16 import call_result, call

logging.basicConfig(level=logging.DEBUG)


class ChargePoint(cp):
    async def send_boot_notification(self):
        request = call.BootNotificationPayload(
            charge_point_model="Super_Charger_3000", charge_point_vendor="Super_Charger"
        )

        response = await self.call(request)

        if response.status == RegistrationStatus.accepted:
            print("Connected to central system.")

            # Schedule the heartbeat function to run
            asyncio.create_task(self.send_heartbeat())

    async def send_heartbeat(self):
        while True:
            request = call.HeartbeatPayload() # not payload in heartbeat request
            response = await self.call(request)
            print(response)
            await asyncio.sleep(5)

    @on(Action.DataTransfer)
    def on_data_transfer(self):
        return call_result.DataTransferPayload(
            current_time=datetime.utcnow().isoformat()
        )





async def main():
    async with websockets.connect(
        "ws://localhost:9000/CP_1", subprotocols=["ocpp1.6"]
    ) as ws:

        cp = ChargePoint("CP_1", ws)

        await asyncio.gather(cp.start(), cp.send_boot_notification())




if __name__ == "__main__":
    # asyncio.run() is used when running this example with Python >= 3.7v
    asyncio.run(main())
