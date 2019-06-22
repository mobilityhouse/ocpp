import asyncio
import logging
from uuid import uuid4
from datetime import datetime

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
from ocpp.v16 import call_result
from ocpp.v16.classes import IDTagInfo

# Set log level to INFO to display print all messages send and received by
# charge point to STDOUT.
logging.basicConfig(level=logging.INFO)


class ChargePoint(cp):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # The transaction ID of the active transaction.
        self.transaction_id = None
        self.meter_start = None

    @on(Action.Authorize)
    def on_authorize(self, id_tag):
        """ Handle Authrize CALL. Only accept ID tag '12345'. """
        id_tag_info = IDTagInfo(status="Invalid")

        if id_tag == "12345":
            id_tag_info.status = "Accepted"

        return call_result.AuthorizePayload(id_tag_info=id_tag_info)

    @on(Action.StartTransaction)
    def on_start_transaction(self, connector_id, id_tag, meter_start,
            timestamp, **kwargs):
        """ Handle StartTransaction CALL. """
        self.transaction_id = uuid4().int
        self.meter_start = meter_start

        id_tag_info = IDTagInfo(status="Invalid")

        if id_tag == "12345":
            id_tag_info.status = "Accepted"


        return call_result.StartTransactionPayload(
            id_tag_info=id_tag_info,
            transaction_id=self.transaction_id,
        )

    @on(Action.MeterValues)
    def on_meter_values(self, connector_id, meter_value, **kwargs):
        """ Handle MeterValue CALL. """
        sampled_value = meter_value[0].sampled_value[0]

        print(f'CP charging with {sampled_value.value} {sampled_value.unit}.')

        return call_result.MeterValuesPayload()

    @on(Action.StopTransaction)
    def on_stop_transaction(self, meter_stop, timestamp, transaction_id,
            **kwargs):
        """ Handle a StopTransaction CALL and print energy used during
        transaction.

        """
        amount_charged = meter_stop - self.meter_start
        print(f'Transaction {transaction_id} stopped. ' \
              f'{amount_charged} Wh charged.')

        # Reset transaction ID.
        self.transaction_id = None

        return call_result.StopTransactionPayload()

    async def set_charging_profile(self):
        # cp = ChargingProfile.for_current_transaction().limit_to(10, "A")
        cp  = ChargingProfile(
            charging_profile_id=1,
            stack_level=1,
            charging_profile_purpose="TxProfile",
            charging_profile_kind="Relative",
            transaction_id=self.transaction_id,
            charging_schedule=ChargingSchedule(
                charging_rate_unit="A",
                charging_schedule_period=[ChargingSchedulePeriod(
                    limit=10.0,
                    start_period=0
                )
            )
        )


        set_limit(10, "A").from().for_transaction(0x123)
        set_limit(10, "A").immidiatly()
        set_limit(10, "A").now()

        profile.set_limit(10, "A").starting_at("08:00").till("13:00").every_day()
        profile.set_limit(20, "A").starting_at("08:00")
        set_limit(10, "A").starting_at("08:00").till("13:00").week()
        limit_to(10, "A").starting_at("08:00").till("13:00").week()
        (10, "A").valid_from("08:00").valid_till("13:00").week()


        add_limit(10, "A").valid_from("08:00").valid_till("13:00").week()
        set_limit_to(10, "A").at(


        period_1 = set_limit_to(10, "A").at("08:00").till("13:00")
        period_2 = set_limit_to(10, "A").at("08:00").until("13:00").every("week")

        create_profile().set_limit_to(

        cp = ChargingProfile()
        cp.

        create_profile.for_transaction(1234).limit_to(10, "A").now().untill(
        ChargingProfile.set_limit_to(10, "A").now()



async def on_connect(websocket, path):
    """ For every new charge point that connects, create a ChargePoint instance
    and start listening for messages.

    """
    charge_point_id = path.strip('/')
    cp = ChargePoint(charge_point_id, websocket)

    await cp.start()


async def main():
    server = await websockets.serve(
        on_connect,
        '0.0.0.0',
        9000,
        subprotocols=['ocpp1.6']
    )

    await server.wait_closed()


if __name__ == '__main__':
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































cp = ChargingProfile.valid_from("2013-01-01T00:00Z").until(
 cp.add_limit_of(11000, "W")
cp.add_limit_of(6000, "W").after(seconds=28800)
cp.add_limit_of(11000, "W").after(hours=20).




cp.set_limit_to(6000, "W").at("08:00").until("20:00")
t cp.set_limit_to(11000, "W").at("20:00")
cp.repeat('Daily')


