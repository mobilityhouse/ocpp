# /// script
# requires-python = ">=3.9"
# dependencies = [
#     "ocpp==2",
#     "websockets==15",
# ]
# ///

import asyncio
from datetime import datetime, timezone
import logging
import signal

from ocpp.routing import after, on
from ocpp.v16 import ChargePoint as cp
from ocpp.v16 import call, call_result, enums
from ocpp.v16.datatypes import ChargingProfile, ChargingSchedule, ChargingSchedulePeriod
from websockets import serve
from websockets.exceptions import ConnectionClosedOK


async def slow_db_call(data):
    print("Registering data in the database")
    await asyncio.sleep(5)


class ChargePoint(cp):
    @on(enums.Action.boot_notification)
    def on_boot_notification(self, **kwargs):
        time = datetime.now(timezone.utc).isoformat()
        response = call_result.BootNotification(
            current_time=time,
            interval=3600,
            status=enums.RegistrationStatus.accepted
        )
        return response

    @after(enums.Action.boot_notification)
    async def after_boot_notification(self, **kwargs):
        await slow_db_call(kwargs)

    async def remote_start_transaction(self):
        period = ChargingSchedulePeriod(
            start_period=0,
            limit=16
        )
        schedule = ChargingSchedule(
            charging_rate_unit=enums.ChargingRateUnitType.amps,
            charging_schedule_period=[period]
        )
        profile = ChargingProfile(
            charging_profile_id=1,
            stack_level=1,
            charging_profile_purpose=enums.ChargingProfilePurposeType.tx_default_profile,
            charging_profile_kind=enums.ChargingProfileKindType.absolute,
            charging_schedule=schedule
        )
        payload = call.RemoteStartTransaction(id_tag="SOME_ID", charging_profile=profile)

        call_result = await self.call(payload)


async def on_connect(connection):
    charge_point_id = connection.request.path.strip("/")
    cp = ChargePoint(charge_point_id, connection)

    try:
        await cp.start()
    except ConnectionClosedOK:
        logging.info(f"Charge point <{charge_point_id}> closed the connection")


async def main():
    async with serve(on_connect, "localhost", 8765, subprotocols=["ocpp1.6"]) as server:
        loop = asyncio.get_running_loop()
        loop.add_signal_handler(signal.SIGINT, server.close)
        loop.add_signal_handler(signal.SIGTERM, server.close)
        await server.wait_closed()


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
