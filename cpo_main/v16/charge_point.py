import asyncio
import logging

import websockets
from ocpp.routing import on, after
from ocpp.v16 import ChargePoint as cp
from ocpp.v16 import call, call_result
from ocpp.v16.datatypes import SampledValue, MeterValue
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
            charge_point_serial_number="1234.ADcb",
            charge_point_model="DrifterChargeBox",
            charge_point_vendor="Drifter",
            charge_box_serial_number="1234.DCba",
            iccid="aabb",
            imsi="bbaa",
            meter_serial_number="IEC",
            meter_type="IEC"
        )

        response = await self.call(request)

        if response.status == RegistrationStatus.accepted:
            await self.send_heartbeat(response.interval)

    async def send_heartbeat(self, interval: datetime):
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
    def on_get_config(self, key: str = None):
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
    async def on_start_remote(self, id_tag, connector_id):
        return call_result.RemoteStartTransactionPayload(
            status=RemoteStartStopStatus.accepted
        )
    @after(Action.RemoteStartTransaction)
    async def after_start_remote(self, id_tag, connector_id):
        await self.send_start_transaction(id_tag, connector_id)

    @on(Action.RemoteStopTransaction)
    def on_stop_remote(self, transaction_id):
        return call_result.RemoteStopTransactionPayload(
            status=RemoteStartStopStatus.accepted
        )
    
    @after(Action.RemoteStopTransaction)
    async def after_stop_remote(self, transaction_id):
        await self.send_stop_transaction(transaction_id)

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

    async def send_meter_values(self, connector_id: int,  *args, **kwargs):
        return await self.call(call.MeterValuesPayload(
            connector_id=connector_id,
            meter_value= [MeterValue(
                timestamp= datetime.now().isoformat(), 
                sampled_value = [
                    SampledValue(
                    value= '200', context= 'Trigger', format= 'SignedData', measurand= 'Current.Export', 
                        phase= 'L1', location= 'Outlet', unit= 'A'),
                    SampledValue(value= '50', context= 'Trigger', format= 'SignedData', measurand= 'Current.Import', 
                        phase= 'L1', location= 'Outlet', unit= 'A'),
                    SampledValue(value= '12', context= 'Trigger', format= 'SignedData', measurand= 'Current.Offered', 
                        phase= 'L1', location= 'Outlet', unit= 'A'),
                    SampledValue(value= '1000', context= 'Trigger', format= 'SignedData', 
                        measurand= 'Energy.Active.Export.Register', phase= 'L1', location= 'Outlet', unit= 'kWh'),
                    SampledValue(value= '305', context= 'Trigger', format= 'SignedData', 
                        measurand= 'Energy.Active.Import.Register', phase= 'L1', location= 'Outlet', unit= 'kWh'),
                    SampledValue(value= '740', context= 'Trigger', format= 'SignedData', 
                        measurand= 'Energy.Reactive.Export.Register', phase= 'L1', location= 'Outlet', unit= 'kvarh'),
                    SampledValue(value= '500', context= 'Trigger', format= 'SignedData', 
                        measurand= 'Energy.Reactive.Import.Register', phase= 'L1', location= 'Outlet', unit= 'kvarh'),
                    SampledValue(value= '1', context= 'Trigger', format= 'SignedData', 
                        measurand= 'Energy.Active.Export.Interval', phase= 'L1', location= 'Outlet', unit= 'kWh'),
                    SampledValue(value= '90', context= 'Trigger', format= 'SignedData', 
                        measurand= 'Energy.Active.Import.Interval', phase= 'L1', location= 'Outlet', unit= 'kWh'),
                    SampledValue(value= '20.1', context= 'Trigger', format= 'SignedData', 
                        measurand= 'Energy.Reactive.Export.Interval', phase= 'L1', location= 'Outlet', unit= 'kvarh'),
                    SampledValue(value= '521', context= 'Trigger', format= 'SignedData', 
                        measurand= 'Energy.Reactive.Import.Interval', phase= 'L1', location= 'Outlet', unit= 'kvarh'),
                    SampledValue(value= '888', context= 'Trigger', format= 'SignedData', 
                        measurand= 'Frequency', phase= 'L1', location= 'Outlet', unit= 'W'),
                    SampledValue(value= '222', context= 'Trigger', format= 'SignedData', measurand= 'Power.Active.Export', 
                        phase= 'L1', location= 'Outlet', unit= 'W'),
                    SampledValue(value= '333', context= 'Trigger', format= 'SignedData', 
                        measurand= 'Power.Active.Import', phase= 'L1', location= 'Outlet', unit= 'W'),
                    SampledValue(value= '621', context= 'Trigger', format= 'SignedData', measurand= 'Power.Factor', 
                        phase= 'L1', location= 'Outlet', unit= 'W'),
                    SampledValue(value= '19', context= 'Trigger', format= 'SignedData', measurand= 'Power.Offered', 
                        phase= 'L1', location= 'Outlet', unit= 'W'),
                    SampledValue(value= '4000', context= 'Trigger', format= 'SignedData', 
                        measurand= 'Power.Reactive.Export', phase= 'L1', location= 'Outlet', unit= 'kvar'),
                    SampledValue(value= '1431', context= 'Trigger', format= 'SignedData', 
                        measurand= 'Power.Reactive.Import', phase= 'L1', location= 'Outlet', unit= 'kvar'),
                    SampledValue(value= '634', context= 'Trigger', format= 'SignedData', 
                        measurand= 'RPM', phase= 'L1', location= 'Outlet', unit= 'W'),
                    SampledValue(value= '3131', context= 'Trigger', format= 'SignedData', 
                        measurand= 'SoC', phase= 'L1', location= 'Outlet', unit= 'Percent'),
                    SampledValue(value= '25689', context= 'Trigger', format= 'SignedData', measurand= 'Temperature', 
                        phase= 'L1', location= 'Outlet', unit= 'Celsius'),
                    SampledValue(value= '5', context= 'Trigger', format= 'SignedData', measurand= 'Voltage', 
                        phase= 'L1', location= 'Outlet', unit= 'V')
                    ])],
                    transaction_id=1234
        ))

    async def send_status_notification(self, connector_id: int = None, **kwargs):
        return await self.call(call.StatusNotificationPayload(
            connector_id=connector_id,
            error_code=ChargePointErrorCode.no_error,
            status=ChargePointStatus.available,
            timestamp=datetime.utcnow().isoformat(),
            info="Charge Point is available for use",
            vendor_id="Drifter",
            vendor_error_code="Operational"

        ))
        

    @on(Action.Reset)
    def on_reset(self, type):
        return call_result.ResetPayload(
            status=ResetStatus.accepted
        )

    async def send_start_transaction(self, id_tag, connector_id):
        request = call.StartTransactionPayload(
            connector_id=connector_id,
            id_tag=id_tag,
            meter_start=0,
            timestamp=datetime.now().isoformat(),
            reservation_id=None
        )
        response = await self.call(request)

        return response
    
    async def send_stop_transaction(self, transaction_id, **kwargs):
        request = call.StopTransactionPayload(
            meter_stop=1000,
            timestamp=datetime.now().isoformat(),
            transaction_id=transaction_id,
            reason = Reason.remote,
            id_tag="string",
            transaction_data=[MeterValue(
                timestamp= datetime.now().isoformat(), 
                sampled_value = [
                    SampledValue(value= '200', context= 'Transaction.End', format= 'SignedData', measurand= 'Current.Export', 
                        phase= 'L1', location= 'Outlet', unit= 'A'),
                    SampledValue(value= '50', context= 'Transaction.End', format= 'SignedData', measurand= 'Current.Import', 
                        phase= 'L1', location= 'Outlet', unit= 'A'),
                    SampledValue(value= '12', context= 'Transaction.End', format= 'SignedData', measurand= 'Current.Offered', 
                        phase= 'L1', location= 'Outlet', unit= 'A'),
                    SampledValue(value= '1000', context= 'Transaction.End', format= 'SignedData', 
                        measurand= 'Energy.Active.Export.Register', phase= 'L1', location= 'Outlet', unit= 'kWh'),
                    SampledValue(value= '305', context= 'Transaction.End', format= 'SignedData', 
                        measurand= 'Energy.Active.Import.Register', phase= 'L1', location= 'Outlet', unit= 'kWh'),
                    SampledValue(value= '740', context= 'Transaction.End', format= 'SignedData', 
                        measurand= 'Energy.Reactive.Export.Register', phase= 'L1', location= 'Outlet', unit= 'kvarh'),
                    SampledValue(value= '500', context= 'Transaction.End', format= 'SignedData', 
                        measurand= 'Energy.Reactive.Import.Register', phase= 'L1', location= 'Outlet', unit= 'kvarh'),
                    SampledValue(value= '1', context= 'Transaction.End', format= 'SignedData', 
                        measurand= 'Energy.Active.Export.Interval', phase= 'L1', location= 'Outlet', unit= 'kWh'),
                    SampledValue(value= '90', context= 'Transaction.End', format= 'SignedData', 
                        measurand= 'Energy.Active.Import.Interval', phase= 'L1', location= 'Outlet', unit= 'kWh'),
                    SampledValue(value= '20.1', context= 'Transaction.End', format= 'SignedData', 
                        measurand= 'Energy.Reactive.Export.Interval', phase= 'L1', location= 'Outlet', unit= 'kvarh'),
                    SampledValue(value= '521', context= 'Transaction.End', format= 'SignedData', 
                        measurand= 'Energy.Reactive.Import.Interval', phase= 'L1', location= 'Outlet', unit= 'kvarh'),
                    SampledValue(value= '888', context= 'Transaction.End', format= 'SignedData', 
                        measurand= 'Frequency', phase= 'L1', location= 'Outlet', unit= 'W'),
                    SampledValue(value= '222', context= 'Transaction.End', format= 'SignedData', measurand= 'Power.Active.Export', 
                        phase= 'L1', location= 'Outlet', unit= 'W'),
                    SampledValue(value= '333', context= 'Transaction.End', format= 'SignedData', 
                        measurand= 'Power.Active.Import', phase= 'L1', location= 'Outlet', unit= 'W'),
                    SampledValue(value= '621', context= 'Transaction.End', format= 'SignedData', measurand= 'Power.Factor', 
                        phase= 'L1', location= 'Outlet', unit= 'W'),
                    SampledValue(value= '19', context= 'Transaction.End', format= 'SignedData', measurand= 'Power.Offered', 
                        phase= 'L1', location= 'Outlet', unit= 'W'),
                    SampledValue(value= '4000', context= 'Transaction.End', format= 'SignedData', 
                        measurand= 'Power.Reactive.Export', phase= 'L1', location= 'Outlet', unit= 'kvar'),
                    SampledValue(value= '1431', context= 'Transaction.End', format= 'SignedData', 
                        measurand= 'Power.Reactive.Import', phase= 'L1', location= 'Outlet', unit= 'kvar'),
                    SampledValue(value= '634', context= 'Transaction.End', format= 'SignedData', 
                        measurand= 'RPM', phase= 'L1', location= 'Outlet', unit= 'W'),
                    SampledValue(value= '80', context= 'Transaction.End', format= 'SignedData', 
                        measurand= 'SoC', phase= 'L1', location= 'Outlet', unit= 'Percent'),
                    SampledValue(value= '25689', context= 'Transaction.End', format= 'SignedData', measurand= 'Temperature', 
                        phase= 'L1', location= 'Outlet', unit= 'Celsius'),
                    SampledValue(value= '5', context= 'Transaction.End', format= 'SignedData', measurand= 'Voltage', 
                        phase= 'L1', location= 'Outlet', unit= 'V')
                    ])]
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
    async def send_trigger(self, requested_message, connector_id:int = None, transaction_id: int = None):
        return call_result.TriggerMessagePayload(
        status=TriggerMessageStatus.accepted
        )
    @after(Action.TriggerMessage)
    async def after_trigger(self, requested_message, connector_id: int = None, *args, **kwargs):
        if requested_message == "StatusNotification":
            await self.send_status_notification(connector_id)
        if requested_message == "MeterValues":
            await self.send_meter_values(connector_id)
        if requested_message == "DiagnosticsStatusNotification":
            await self.send_diagnostics(connector_id)
        if requested_message == "FirmwareStatusNotification":
            await self.send_firmware_status(connector_id)
        if requested_message == "BootNotification":
            await self.send_boot_notification()  
        if requested_message == "Heartbeat":
            await self.send_heartbeat()    
        return

    @on(Action.UnlockConnector)
    def unlock_connector(self, connector_id):
        return call_result.UnlockConnectorPayload(
            status = UnlockStatus.unlocked
        )


async def main():
    async with websockets.connect(
        'ws://localhost:8000/ocpp/16/api/v16/CP', 
        subprotocols=["ocpp1.6"]
    ) as ws:

        cp = ChargePoint('CP', ws)

        await asyncio.gather(cp.start(), cp.send_boot_notification())

if __name__ == '__main__':
    try:
        # asyncio.run() is used when
        # running this example with Python 3.7 and
        # higher.
        asyncio.run(main())
    except AttributeError:
        # For Python 3.6 a bit more code is required to run the main() task on
        # an event loop.
        loop = asyncio.get_event_loop()
        loop.run_until_complete(main())
        loop.close()
