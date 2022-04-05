import logging
from datetime import datetime

from ocpp.routing import on, after
from ocpp.v201 import ChargePoint as cp
from ocpp.v201 import call, call_result
from ocpp.v201.enums import *
from ocpp.v201.enums import Action

logging.basicConfig(level=logging.INFO)


"""This Class is defining the message functions of the CPO.

The Class is divided into a SEND and RECIEVE functions.
The SEND functions are the ones which are defined as async functions.
The RECIEVE functions are the ones with a @on decorator.
The variables are named according to the OCPP 2.0.1 protocol.
Since this is a translated version it has not been properly tested.
"""
class ChargePoint(cp):

    @on(Action.BootNotification)
    def on_boot_notification(self, **kwargs):
        """Recieve a boot notification from a newly connected Charge Point.
        Tested"""
        print("A new connection from: ")
        return call_result.BootNotificationPayload(
            current_time=datetime.utcnow().isoformat(),
            interval=1000,
            status=RegistrationStatusType.accepted
        )


    @on(Action.Heartbeat)
    def on_heartbeat(self):
        """Recieve a heartbeat signal from Charge Point.
        Tested"""
        print("Recieved a heartbeat from: ")
        return call_result.HeartbeatPayload(
            current_time=datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S') + "Z"
        )


    @on(Action.StatusNotification)
    async def on_status_notification(self, timestamp, connector_id, *args, **kwargs):
        """Recieves a status notification. Should be sent to the website.
        Not Tested"""
        print("Status Update request recieved")
        return call_result.StatusNotificationPayload()


    @on(Action.TransactionEvent)
    def on_transaction_event(self, event_type, timestamp, trigger_reason, seq_no, transaction_info, **kwargs):
        """All transaction related messages.
        Not Tested"""
        print("Transaction Event Updated")
        return call_result.TransactionEventPayload()

    @on(Action.MeterValues)
    async def on_meter_values(self, evse_id, meter_values):
        """Recieve meter values of an ongoing transaction.
        Not tested"""
        print("Meter Values request recieved")
        return call_result.MeterValuesPayload()


    async def send_request_start_transaction(self, id_token: dict, remote_start_id: int, evse_id:int,
    group_id_token: dict = None, charging_profile: dict = None):
        """Send a start transaction request.
        Not tested"""
        print("Start remote transaction request")
        return await self.call(call.RequestStartTransactionPayload(
            id_token=id_token,
            remote_start_id=remote_start_id,
            evse_id=evse_id,
            group_id_token=group_id_token,
            charging_profile=charging_profile
        ))

    @on(Action.DataTransfer)
    async def on_data_transfer(self, vendor_id: str, message_id: str, data: str):
        """Recieve a Data transfer.
        Not developed"""
        pass

    async def send_get_variable(self, get_variable_data):
        """Sends a Get Configuration request.
        Not tested"""
        print("Get Variable request")
        return await self.call(call.GetVariablesPayload(
            get_variable_data=get_variable_data
        ))


    async def send_request_stop_transaction(self, transaction_id: str):
        """Sends a Stop transaction request.
        Not tested"""
        print("Stop transaction request")
        return await self.call(call.RequestStopTransactionPayload(
            transaction_id=transaction_id
        ))

    async def send_change_availability(self, operational_status, **kwargs):
        """Sends a Change availability request.
        Not Tested"""
        print("Changing Availability request")
        return await self.call(call.ChangeAvailabilityPayload(
            operational_status=operational_status
        ))

    async def send_set_variable(self, set_variable_data: str):
        """Sends a Change configuration request.
        Not Tested"""
        print("Set variable request")
        return await self.call(call.SetVariablesPayload(
            set_variable_data=set_variable_data
        ))

    async def send_get_schedule(self, evse_id, duration, charging_rate_unit):
        """Sends a Get schedule request.
        Not tested"""
        print("Get Composite Schedule request")
        return await self.call(call.GetCompositeSchedulePayload(
            evse_id=evse_id,
            duration=duration,
            charging_rate_unit=charging_rate_unit
        ))

    async def send_get_local_list(self):
        """Sends a Get local list request.
        Not Tested"""
        print("Get Local List request")
        return await self.call(call.GetLocalListVersionPayload(
        ))


    async def send_local_list(self, version_number, local_authorization_list, update_type):
        """Sends Local list request.
        Not tested"""
        print("Send Local List request")
        return await self.call(call.SendLocalListPayload(
            version_number=version_number,
            update_type=update_type,
            local_authorization_list=local_authorization_list
        ))


    async def send_clear_cache(self):
        """Sends a Clear Cache request.
        Tested"""
        print("Clearing Cache request")
        return await self.call(call.ClearCachePayload())


    async def send_reserve_now(self, id, expiry_date, id_token, connector_type):
        """Sends a Reservation request.
        Not tested"""
        print("Sending reservation request")
        return await self.call(call.ReserveNowPayload(
            id=id,
            expiry_date=expiry_date,
            id_token={'id_token':'123abc',
            'type':'Local'},
            connector_type=connector_type
        ))

    async def send_cancel_reservation(self, reservation_id):
        """Sends a Cancel reservation request.
        Not tested"""
        print("Sending cancel reservation request")
        return await self.call(call.CancelReservationPayload(
            reservation_id=reservation_id
        ))

    async def send_clear_charging_profile(self, charging_profile_id):
        """Sends a Clear Charging profile request.
        Not tested"""
        print("Sending clear charging profile request")
        return await self.call(call.ClearChargingProfilePayload(
            charging_profile_id=charging_profile_id
        ))

    async def send_reset(self, type: str):
        """Sends a Reset request.
        Tested"""
        print("Reset Charge Point")
        return await self.call(call.ResetPayload(
            type=type
        ))


    async def send_trigger(self, requested_message):
        """Sends a Trigger request.
        Not tested"""
        print("Sending Trigger Message request")
        return await self.call(call.TriggerMessagePayload(
            requested_message=requested_message
        ))


    async def send_unlock_connector(self, evse_id, connector_id: int):
        """Sends a Unlock request.
        Not tested"""
        print("Unlocking Connector")
        return await self.call(call.UnlockConnectorPayload(
            evse_id=evse_id,
            connector_id=connector_id
        ))

