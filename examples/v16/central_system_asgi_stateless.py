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
from ocpp.asgi_routing import Router, Context
from ocpp.v16.enums import Action, RegistrationStatus
from ocpp.v16 import call_result


# Stateless Router class
class ProvisioningRouter(Router):
    @on(Action.BootNotification)
    def on_boot_notification(self, event: dict, context: Context):
        id = context.id  # we can identify the charging_station by "id" in context
        return call_result.BootNotificationPayload(
            current_time=datetime.utcnow().isoformat(),
            interval=10,
            status=RegistrationStatus.accepted,
        )

    @after(Action.BootNotification)
    async def after_boot_notification(self, event: dict, context: Context):
        pass


# Stateless Router class
class MeterValuesRouter(Router):
    @on(Action.MeterValues)
    def on_meter_values(self, event: dict, context: Context):
        return call_result.MeterValuesPayload()


if __name__ == "__main__":
    router = Router(stateless=True)
    router.include_router(ProvisioningRouter())
    router.include_router(MeterValuesRouter())
    headers = [("Sec-WebSocket-Protocol", "ocpp1.6")]
    uvicorn.run(router, host="0.0.0.0", port=9000, headers=headers)
