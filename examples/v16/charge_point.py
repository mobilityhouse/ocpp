import asyncio
import logging
import websockets

from ocpp.v16 import ChargePoint as cp
from ocpp.v16 import call
from ocpp.v16.enums import RegistrationStatus, AuthorizationStatus

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

async def main():
    async with websockets.connect(
            "ws://localhost:9000/CP_1", subprotocols=["ocpp1.6"]
    ) as ws:
        cp = ChargePoint("CP_1", ws)
        await asyncio.gather(
            cp.start(),
            cp.send_boot_notification(),
            cp.send_authorization("car_1"),
            cp.send_authorization("car_2"))

if __name__ == "__main__":
    # asyncio.run() is used when running this example with Python >= 3.7v
    asyncio.run(main())