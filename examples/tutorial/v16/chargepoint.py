# /// script
# requires-python = ">=3.9"
# dependencies = [
#     "ocpp==2",
#     "websockets==15",
# ]
# ///

import asyncio
import logging

from ocpp.v16 import ChargePoint as cp
from ocpp.v16 import call, enums
from websockets import connect
from websockets.exceptions import ConnectionClosedOK


class ChargePoint(cp):
    async def send_boot_notification(self):
        request = call.BootNotification(
            charge_point_model="Optimus", charge_point_vendor="The Mobility House"
        )

        response = await self.call(request)

        if response.status == enums.RegistrationStatus.accepted:
            await self.synchronize_internal_clock(response.current_time)
            await self.send_heartbeats(response.interval)
            print("Connected to central system.")

        if response.status == enums.RegistrationStatus.rejected:
            print("CSMS rejected connection")
            await self._connection.close()

        if response.status == enums.RegistrationStatus.pending:
            print("Status pending | Charge point should not initiate any new messages "
                  "until CSMS accepts registration")

    async def synchronize_internal_clock(self, time):
        print("Setting system time")

    async def send_heartbeats(self, interval):
        while True:
            await asyncio.sleep(interval)
            response = await self.call(call.Heartbeat())
            await self.synchronize_internal_clock(response.current_time)


async def main():
    async with connect("ws://localhost:8765/SOME_ID", subprotocols=["ocpp1.6"]) as connection:
        cp = ChargePoint("SOME_ID", connection)

        try:
            await asyncio.gather(cp.start(), cp.send_boot_notification())
        except ConnectionClosedOK:
            print("CSMS closed the connection")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
