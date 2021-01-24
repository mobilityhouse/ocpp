from datetime import datetime

try:
    import uvicorn
    import websockets
except ModuleNotFoundError:
    print("This example relies on the 'uvicorn' and 'websockets' packages.")
    print("Please install it by running: ")
    print()
    print(" $ pip install uvicorn websockets")
    import sys

    sys.exit(1)
from ocpp.routing import on, after
from ocpp.asgi_routing import Router
from ocpp.v16.enums import Action, RegistrationStatus
from ocpp.v16 import call_result


# Stateful Router class
class ChargingStation(Router):
    @on(Action.BootNotification)
    def on_boot_notification(self, **kwargs):
        return call_result.BootNotificationPayload(
            current_time=datetime.utcnow().isoformat(),
            interval=10,
            status=RegistrationStatus.accepted,
        )

    @after(Action.BootNotification)
    async def after_boot_notification(self, **kwargs):
        pass

    @on(Action.MeterValues)
    def on_meter_values(self, **kwargs):
        return call_result.MeterValuesPayload()


# Stateful Router class acting as Central System
class CentralSystem(Router):

    charging_stations = {}

    async def on_connect(self, context):
        self.charging_stations[context.id] = ChargingStation(context=context)

    async def on_disconnect(self, context):
        del self.charging_stations[context.id]

    async def on_receive(self, message, context):
        await self.charging_stations[context.id].route_message(message)


if __name__ == "__main__":
    central_system = CentralSystem()
    headers = [("Sec-WebSocket-Protocol", "ocpp1.6")]
    uvicorn.run(central_system, host="0.0.0.0", port=9000, headers=headers)
