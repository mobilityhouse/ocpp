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
