# server.py
import asyncio
import websockets
from datetime import datetime, timezone

from ocpp.routing import on
from ocpp.v16 import ChargePoint as cp
from ocpp.v16 import call_result
from ocpp.v16.enums import Action, RegistrationStatus


class MyChargePoint(cp):
    @on(Action.boot_notification)
    async def on_boot_notification(
        self, charge_point_vendor, charge_point_model, **kwargs
    ):
        return call_result.BootNotification(
            current_time=datetime.now(tz=timezone.utc).isoformat(),
            interval=10,
            status=RegistrationStatus.accepted,
        )


async def on_connect(connection: websockets.ServerConnection):
    """
    For every new connection, create a new ChargePoint instance,
    and start listening for messages.
    """
    charge_point_id = connection.request.path.split("/")[-1]
    charge_point = MyChargePoint(charge_point_id, connection)

    await charge_point.start()


async def main():
    server = await websockets.serve(
        on_connect,
        '0.0.0.0',
        9000,
        subprotocols=['ocpp1.6'],
    )
    await server.wait_closed()

if __name__ == '__main__':
    asyncio.run(main())