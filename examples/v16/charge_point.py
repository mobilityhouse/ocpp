import asyncio
import logging
import websockets

from ocpp.v16 import ChargePoint as cp
from ocpp.v16 import call
from ocpp.v16.datatypes import SampledValue, MeterValue
from ocpp.v16.enums import RegistrationStatus, AuthorizationStatus, RemoteStartStopStatus

logging.basicConfig(level=logging.INFO)

class ChargePoint(cp):
    async def send_boot_notification(self):
        request = call.BootNotificationPayload(charge_point_model="Optimus", charge_point_vendor="The Mobility House")
        response = await self.call(request)
        if response.status == RegistrationStatus.accepted:
            print("Connected to central system.")

    async def send_authorization(self, id_tag):
        request = call.AuthorizePayload(id_tag=id_tag)
        response = await self.call(request)
        if response.id_tag_info["status"] == AuthorizationStatus.accepted:
            print(f'Authorized {id_tag} for charging, '
                  f'parent_id_tag is {response.id_tag_info["parent_id_tag"]} and expiring date is {response.id_tag_info["expiry_date"]}')

    async def send_remote_start_transaction(self, id_tag):
        request = call.RemoteStartTransactionPayload(id_tag=id_tag)
        response = await self.call(request)
        if response.status == RemoteStartStopStatus.accepted:
            print(f'Accepted {id_tag} to start charging')

    async def send_remote_end_transaction(self, id_tag, transaction_id):
        request = call.RemoteStopTransactionPayload(transaction_id=transaction_id)
        response = await self.call(request)
        if response.status == RemoteStartStopStatus.accepted:
            print(f'Accepted {id_tag} to end charging on transaction_id {transaction_id}')

    async def send_meter_values(self, connector_id):
        request = call.MeterValuesPayload(connector_id=connector_id, meter_value=[
            MeterValue(timestamp="0100", sampled_value=[
                SampledValue("10"),
                SampledValue("11"),
                SampledValue("12")
            ]),
            MeterValue(timestamp="0200", sampled_value=[
                SampledValue("20"),
                SampledValue("21"),
                SampledValue("22")
            ])
        ])
        response = await self.call(request)
        print("Forwarded meter values to central system")

async def main():
    async with websockets.connect(
            "ws://localhost:9000/CP_1", subprotocols=["ocpp1.6"]
    ) as ws:
        cp = ChargePoint("CP_1", ws)
        await asyncio.gather(
            cp.start(),
            cp.send_boot_notification(),
            cp.send_authorization("car_1"),
            cp.send_remote_start_transaction("car_1"),
            cp.send_remote_end_transaction("car_1", 12345),
            cp.send_meter_values(67890)
        )


if __name__ == "__main__":
    # asyncio.run() is used when running this example with Python >= 3.7v
    asyncio.run(main())