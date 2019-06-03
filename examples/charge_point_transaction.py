import asyncio
import logging
from typing import Dict
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

from ocpp.v16 import call
from ocpp.v16 import ChargePoint as cp
from ocpp.v16.enums import RegistrationStatus, AuthorizationStatus
from ocpp.v16.classes import SampledValue, MeterValue

# Set log level to INFO to display print all messages send and received by
# charge point to STDOUT.
logging.basicConfig(level=logging.INFO)

# Most attributes for SampledValue are static and won't change.
# `SampledValue.prefill()` can be used to prefill the constructor of
# `SampledValue` with these static values.
#
# Later on `current_at_l1` can be used like this:
#
#   > sampled_value = current_at_l1(value="20")
#   > sampled_value
#   SampledValue(value='20', format='Raw', context='Sample.Periodic', measurand='Current.Import', phase='L1', location='Outlet', unit='A')
current_at_l1 = SampledValue.prefill(
    format="Raw",
    context="Sample.Periodic",
    measurand="Current.Import",
    phase="L1",
    location="Outlet",
    unit="A"
)


class ChargePoint(cp):
    """ A charge point that can send the following CALLs:

    * Authorize
    * StartTransaction
    * MeterValues
    * StopTransaction

    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # The transaction ID of the active transaction.
        self.transaction_id = None

    async def authorize(self):
        """ Send Authorize CALL with ID tag "12345" to central system.

        If ID tag is accepted call self.start_transaction(). Otherwise don't
        continue.

        """
        request = call.AuthorizePayload(id_tag="12345")

        response = await self.call(request)

        if response.id_tag_info.status != AuthorizationStatus.accepted:
            print("Authorization failed.")

            return

        await self.start_transaction()

    async def start_transaction(self):
        """ Start a transaction for connector 1 using ID tag "12345".

        If ID tag is accepted continue and call self.meter_values() 5 times
        before calling self.stop_transaction(). Otherwise don't continue.

        """
        request = call.StartTransactionPayload(
            connector_id=1,
            id_tag="12345",
            meter_start=0,
            timestamp=datetime.utcnow().isoformat()
        )

        response = await self.call(request)

        if response.id_tag_info.status != AuthorizationStatus.accepted:
            print("Authorization failed.")

            return

        self.transaction_id = response.transaction_id
        print(f"Transaction started with transaction ID: {self.transaction_id}.")

        for _ in range(5):
            await self.meter_values()
            await asyncio.sleep(1)

        await self.stop_transaction()

    async def meter_values(self):
        """ Send MeterValue CALL to central system. """
        sampled_value = current_at_l1(value="20")

        meter_value = MeterValue(
            timestamp=datetime.utcnow().isoformat(),
            sampled_value=[sampled_value]
        )

        request = call.MeterValuesPayload(
            connector_id=1,
            transaction_id=self.transaction_id,
            meter_value=[meter_value]
        )

        await self.call(request)

    async def stop_transaction(self):
        """ Stop an ongoing transaction. """
        request = call.StopTransactionPayload(
            meter_stop=15,
            timestamp=datetime.utcnow().isoformat(),
            transaction_id=self.transaction_id
        )

        await self.call(request)


async def main():
    async with websockets.connect(
        'ws://localhost:9000/CP_1',
         subprotocols=['ocpp1.6']
    ) as ws:

        cp = ChargePoint('CP_1', ws)

        await asyncio.gather(cp.start(), cp.authorize())


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
