import asyncio
import logging
from urllib import response

import websockets
from ocpp.routing import on
from ocpp.v201 import ChargePoint as cp
from ocpp.v201 import call, call_result
from ocpp.v201.enums import *
import datetime

logging.basicConfig(level=logging.INFO)

"""
This Class is defining the virtual Charge Point.
All of the functions are hard coded.
The proper tests are done on proper Charge Point Hardware.
This is only used to test the OCPP implementation and message routing between HTTP, CSMS and Charge Point.
Since this is a translated version it has not been properly tested.
"""

class ChargePoint(cp):

    async def send_authorize(self, id_tag):
        request = call.AuthorizePayload(
            id_tag=id_tag
        )
        response = await self.call(request)

        if response.id_tag_info['status'] == AuthorizationStatusType.accepted:
            print("User Authorized")

        elif response.id_tag_info['status'] == AuthorizationStatusType.invalid:
            print("User Invalid")

        else:
            print("User Rejected")


    async def send_boot_notification(self):
        request = call.BootNotificationPayload(
            charging_station={'model':"Drifter",
            'vendor_name':'Drifter'},
            reason="PowerUp"
        )

        response = await self.call(request)

        if response.status == RegistrationStatusType.accepted:
            print("Connected to central system.")
            await self.send_heartbeat(response.interval)

    async def send_heartbeat(self, interval):
        request = call.HeartbeatPayload()
        while True:
            await self.call(request)
            await asyncio.sleep(interval)

    @on(Action.SetVariables)
    def on_change_config(self, set_variable_data):
        return call_result.SetVariablesPayload(
            set_variable_result=None
        )

    @on(Action.GetVariables)
    def on_get_config(self, get_variable_data):
        return call_result.GetVariablesPayload(
            get_variable_result=None
        )

    @on(Action.ChangeAvailability)
    def on_change_availability(self, operational_status):
        return call_result.ChangeAvailabilityPayload(
            status=ChangeAvailabilityStatusType.accepted
        )

    @on(Action.RequestStartTransaction)
    def on_start_remote(self, id_token, remote_start_id, evse_id):
        return call_result.RequestStartTransactionPayload(
            status=RequestStartStopStatusType.accepted,
            transaction_id="ABC123"
        )

    @on(Action.RequestStopTransaction)
    def on_stop_remote(self, transaction_id):
        return call_result.RequestStopTransactionPayload(
            status=RequestStartStopStatusType.accepted
        )

    @on(Action.ReserveNow)
    def on_reserve_now(self, id, expiry_date, id_token, connector_type):
        return call_result.ReserveNowPayload(
            status=ReserveNowStatusType.accepted
        )

    @on(Action.CancelReservation)
    def on_cancel_reservation(self, reservation_id):
        return call_result.CancelReservationPayload(
            status=CancelReservationStatusType.accepted
        )

    @on(Action.GetCompositeSchedule)
    def on_cancel_reservation(self, connector_id, duration, charging_rate_unit):
        return call_result.GetCompositeSchedulePayload(
            status=GenericStatusType.accepted
        )

    @on(Action.GetLocalListVersion)
    def on_get_local_list(self):
        return call_result.GetLocalListVersionPayload(
            version_number=1
        )

    @on(Action.SendLocalList)
    def on_send_local_list(self, list_version, local_authorization_list, update_type):
        return call_result.SendLocalListPayload(
            status=SendLocalListStatusType.accepted
        )

    @on(Action.ClearChargingProfile)
    def on_clear_charging_profile(self, charging_profile_id):
        return call_result.ClearChargingProfilePayload(
            status=ClearChargingProfileStatusType.accepted
        )


    @on(Action.ClearCache)
    def on_clear_cache(self):
        return call_result.ClearCachePayload(
            status=ClearCacheStatusType.accepted
        )

    async def send_data_transfer(self, vendor_id, message_id, data):
        request = call.DataTransferPayload(
            vendor_id=vendor_id,
            message_id=message_id,
            data=data
        )
        response = await self.call(request)

        if response.status == DataTransferStatusType.accepted:
            print("Transfer Accepted")

        elif response.status == DataTransferStatusType.rejected:
            print("Transfer Rejected")

        else:
            print("User Rejected")    

    async def send_meter_values(self, evse_id, meter_value):
        request = call.MeterValuesPayload(
            evse_id=evse_id,
            meter_value=meter_value
        )
        response = await self.call(request) 

    async def send_status_notification(self, timestamp: datetime, connector_status: str, evse_id:int, connector_id:int):
        request = call.StatusNotificationPayload(
            timestamp=datetime.utcnow().isoformat(),
            connector_status="Occupied",
            evse_id=1,
            connector_id=1
        )
        response = await self.call(request)

    @on(Action.Reset)
    def on_reset(self, type):
        return call_result.ResetPayload(
            status=ResetStatusType.accepted
        )
    
    async def transaction_event(self, event_type, timestamp, trigger_reason, seq_no, transaction_id, charge_state, evse, id_token, **kwargs):
        request = call.TransactionEventPayload(
            event_type="Started",
            timestamp=datetime.utcnow().isoformat(),
            trigger_reason="CablePlugedIn",
            seq_no=1,
            
            transaction_info=
                {"transaction_id":"ABC123",
                "charging_state":"EVConnected"},
            evse=
                {"id": 1,
                "connectorId": 1},
            id_token={
                'id_token':"ABC123",
                'type': "Local"}
        )
        response = await self.call(request)


    @on(Action.TriggerMessage)
    def unlock_connector(self, requested_message):
        return call_result.TriggerMessagePayload(
            status = TriggerMessageStatusType.accepted
        )


    @on(Action.UnlockConnector)
    def unlock_connector(self, evse_id, connector_id):
        return call_result.UnlockConnectorPayload(
            status = UnlockStatusType.unlocked
        )


async def main():
    async with websockets.connect(
        'ws://localhost:8000/v201/api/v201/CP',
        subprotocols=["ocpp2.0.1"]
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
