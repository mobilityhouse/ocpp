import asyncio
import logging

import websockets
from ocpp.routing import on, after
from ocpp.v16 import ChargePoint as cp
from ocpp.v16 import call, call_result
from ocpp.v16.enums import *
from datetime import datetime

logging.basicConfig(level=logging.INFO)

"""
This Class is defining the virtual Charge Point.
All of the functions are hard coded.
The proper tests are done on proper Charge Point Hardware.
This is only used to test the OCPP implementation and message routing between HTTP, CSMS and Charge Point.
"""

class ChargePoint(cp):

    async def send_authorize(self, id_tag):
        request = call.AuthorizePayload(
            id_tag=id_tag
        )
        response = await self.call(request)

        if response.id_tag_info['status'] == AuthorizationStatus.accepted:
            print("User Authorized")

        elif response.id_tag_info['status'] == AuthorizationStatus.invalid:
            print("User Invalid")

        else:
            print("User Rejected")


    async def send_boot_notification(self):
        request = call.BootNotificationPayload(
            charge_point_model="Garo",
            charge_point_vendor="Drifter"
        )

        response = await self.call(request)

        if response.status == RegistrationStatus.accepted:
            print("Connected to central system.")
            await self.send_heartbeat(response.interval)

    async def send_heartbeat(self, interval):
        request = call.HeartbeatPayload()
        while True:
            await self.call(request)
            await asyncio.sleep(interval)

    @on(Action.ChangeConfiguration)
    def on_change_config(self, key, value):
        return call_result.ChangeConfigurationPayload(
            status=ConfigurationStatus.accepted
        )

    @on(Action.GetConfiguration)
    def on_get_config(self, key):
        return call_result.GetConfigurationPayload(
            #configuration_key=key,
            #unknown_key=List
        )

    @on(Action.ChangeAvailability)
    def on_change_availability(self, connector_id, type):
        return call_result.ChangeAvailabilityPayload(
            status=AvailabilityStatus.accepted
        )

    @on(Action.RemoteStartTransaction)
    def on_start_remote(self, id_tag, connector_id):
        return call_result.RemoteStartTransactionPayload(
            status=RemoteStartStopStatus.accepted
        )

    @on(Action.RemoteStopTransaction)
    def on_stop_remote(self, transaction_id):
        return call_result.RemoteStopTransactionPayload(
            status=RemoteStartStopStatus.accepted
        )

    @on(Action.ReserveNow)
    def on_reserve_now(self, connector_id, expiry_date, id_tag, parent_id_tag, reservation_id):
        return call_result.ReserveNowPayload(
            status=ReservationStatus.accepted
        )

    @on(Action.CancelReservation)
    def on_cancel_reservation(self, reservation_id):
        return call_result.CancelReservationPayload(
            status=CancelReservationStatus.accepted
        )

    @on(Action.GetCompositeSchedule)
    def on_get_schedule(self, connector_id, duration, charging_rate_unit):
        return call_result.GetCompositeSchedulePayload(
            status=GetCompositeScheduleStatus.accepted,
            connector_id=connector_id,
            schedule_start=None,
            charging_schedule=None
        )

    @on(Action.GetLocalListVersion)
    def on_get_local_list(self):
        return call_result.GetLocalListVersionPayload(
            list_version=1
        )

    @on(Action.SendLocalList)
    def on_send_local_list(self, list_version, local_authorization_list, update_type):
        return call_result.SendLocalListPayload(
            status=UpdateStatus.accepted
        )

    @on(Action.ClearChargingProfile)
    def on_clear_charging_profile(self, connector_id, charging_profile_purpose, stack_level):
        return call_result.ClearChargingProfilePayload(
            status=ClearChargingProfileStatus.accepted
        )


    @on(Action.ClearCache)
    def on_clear_cache(self):
        return call_result.ClearCachePayload(
            status=ClearCacheStatus.accepted
        )

    async def send_data_transfer(self, vendor_id, message_id, data):
        request = call.DataTransferPayload(
            id_tag=vendor_id,
            message_id=message_id,
            data=data
        )
        response = await self.call(request)

        if response.status == DataTransferStatus.accepted:
            print("Transfer Accepted")

        elif response.status == DataTransferStatus.rejected:
            print("Transfer Rejected")

        else:
            print("User Rejected")    

    async def send_meter_values(self, connector_id, *args, **kwargs):
        time_meter = datetime.utcnow().isoformat()
        return await self.call(call.MeterValuesPayload(
            connector_id=connector_id,
            meter_value= [{'timestamp': time_meter, 'sampledValue': [{'value': '200', 'measurand': 'Voltage'}]}]
        ))

    async def send_status_notification(self, connector_id, **kwargs):
        return await self.call(call.StatusNotificationPayload(
            connector_id=connector_id,
            error_code=ChargePointErrorCode.no_error,
            status=ChargePointStatus.available
        ))
        

    @on(Action.Reset)
    def on_reset(self, type):
        return call_result.ResetPayload(
            status=ResetStatus.accepted
        )

    async def send_start_transaction(self, connector_id, id_tag, meter_start, time_stamp, reservation_id):
        request = call.StartTransactionPayload(
            connector_id=0,
            id_tag="123abc",
            meter_start=0,
            timestamp=datetime.utcnow().isoformat(),
            reservation_id=None
        )
        response = await self.call(request)
    
    async def send_stop_transaction(self, transaction_id, timestamp, meter_stop, **kwargs):
        request = call.StopTransactionPayload(
            meter_stop=0,
            timestamp=datetime.utcnow().isoformat(),
            transaction_id=0,
            reason = None,
            id_tag= "123abc",
            transaction_list = None
        )
        response = await self.call(request)

    async def send_diagnostics(self, *args, **kwargs):
        return await self.call(call.DiagnosticsStatusNotificationPayload(
            status=DiagnosticsStatus.idle
        ))

    async def send_firmware_status(self, *args, **kwargs):
        return await self.call(call.FirmwareStatusNotificationPayload(
            status=FirmwareStatus.idle
        ))


    @on(Action.TriggerMessage)
    async def send_trigger(self, requested_message, connector_id):
        return call_result.TriggerMessagePayload(
        status=TriggerMessageStatus.accepted
        )
    @after(Action.TriggerMessage)
    async def after_trigger(self, requested_message, connector_id, *args, **kwargs):
        if requested_message == "StatusNotification":
            await self.send_status_notification(connector_id)
        if requested_message == "MeterValues":
            await self.send_meter_values(connector_id)
        if requested_message == "DiagnosticsStatusNotification":
            await self.send_diagnostics(connector_id)
        if requested_message == "FirmwareStatusNotification":
            await self.send_firmware_status(connector_id)    
        return

    @on(Action.UnlockConnector)
    def unlock_connector(self, connector_id):
        return call_result.UnlockConnectorPayload(
            status = UnlockStatus.unlocked
        )


async def main():
    async with websockets.connect(
        'ws://localhost:8000/CP', 
        subprotocols=["ocpp1.6"]
    ) as ws:

        cp = ChargePoint('CP', ws)

        await asyncio.gather(cp.start(), cp.send_boot_notification())

if __name__ == '__main__':
    try:
        # asyncio.run() is used when
        #  running this example with Python 3.7 and
        # higher.
        asyncio.run(main())
    except AttributeError:
        # For Python 3.6 a bit more code is required to run the main() task on
        # an event loop.
        loop = asyncio.get_event_loop()
        loop.run_until_complete(main())
        loop.close()
