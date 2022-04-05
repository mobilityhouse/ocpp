import logging
from datetime import datetime
from typing import Dict, List

from ocpp.routing import on
from ocpp.v16 import ChargePoint as cp
from ocpp.v16 import call, call_result
from ocpp.v16.enums import *
import random



logging.basicConfig(level=logging.INFO)


"""This Class is defining the message functions of the CPO.

The Class is divided into a SEND and RECIEVE functions.
The SEND functions are the ones which are defined as async functions.
The RECIEVE functions are the ones with a @on decorator.
The variables are named according to the OCPP 1.6 protocol.
"""
class ChargePoint(cp):

    @on(Action.BootNotification)
    def on_boot_notification(self, charge_point_vendor: str, charge_point_model: str, **kwargs):
        """Recieve a boot notification from a newly connected Charge Point.
        Tested"""
        print("A new connection from: ")
        return call_result.BootNotificationPayload(
            current_time=datetime.utcnow().isoformat(),
            interval=10,
            status=RegistrationStatus.accepted
        )


    @on(Action.Heartbeat)
    def on_heartbeat(self, **kwargs):
        """Recieve a heartbeat signal from Charge Point.
        Tested"""
        print("Recieved a heartbeat from: ")
        return call_result.HeartbeatPayload(
            current_time=datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S') + "Z"
        )

    @on(Action.Authorize)
    def on_authorize(self, id_tag: str, **kwargs):
        """Recieve authorization information.
        Tested but not working"""
        print(datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S') + "Z", "ID Token Accepted")
        return call_result.AuthorizePayload(
            id_tag_info={
                # 'expiry_date': 'JAN13',
                # 'parent_id_tag': 'parent_tag',

                "status": AuthorizationStatus.accepted
            }
        )

    @on(Action.StatusNotification)
    def on_status_notification(self, timestamp, connector_id, *args, **kwargs):
        """Recieves a status notification. Should be sent to the website.
        Tested but not fully developed."""
        print("Status Update request recieved")
        return call_result.StatusNotificationPayload()

    @on(Action.StartTransaction)
    def on_start_transaction(self, connector_id: int, id_tag: str, meter_start: int, timestamp: str, reservation_id: int, **kwargs):
        """Charge Point has started a transaction.
        Not tested"""
        print("Starting transaction request recieved")

        return call_result.StartTransactionPayload(
            transaction_id=random.randint(1, 10000),
            id_tag_info={"status": AuthorizationStatus.accepted}
        )

    @on(Action.StopTransaction)
    def on_stop_transaction(self, transaction_id: int, meter_stop: int, timestamp: str, reason: str, id_tag: Dict, transaction_list: List, **kwargs):
        """Charge Point has stopped the transaction.
        Not tested"""
        print("Stopping transaction request recieved")
        return call_result.StopTransactionPayload(
            id_tag_info={'status': AuthorizationStatus.accepted}
        )

    @on(Action.MeterValues)
    def on_meter_values(self, connector_id: int, transaction_id: int, meter_values, **kwargs):
        """Recieve meter values.
        Not tested"""
        print("Meter Values request recieved")
        print(f'{self.id} recieved MeterValue')
        return call_result.MeterValuesPayload()

    @on(Action.DiagnosticsStatusNotification)
    def on_diagnostics_status(self):
        return call_result.DiagnosticsStatusNotificationPayload()
    
    @on(Action.FirmwareStatusNotification)
    def on_firmware_status(self, **kwargs):
        return call_result.FirmwareStatusNotificationPayload()

    async def send_data_transfer(self, vendor_id: str, message_id: str, data: str, **kwargs):
        """Recieve a Data transfer.
        Not developed"""
        return await self.call(call.DataTransferPayload(
            vendor_id=vendor_id,
            message_id=message_id,
            data=data
            ))

    async def send_get_configuration(self, key: List, **kwargs):
        """Sends a Get Configuration request.
        Not tested"""
        print("Get Configuration request")
        return await self.call(call.GetConfigurationPayload(
            key=key
        ))

    async def send_remote_start_transaction(self, id_tag: str, connector_id: int, charging_profile: Dict, **kwargs):
        """Send a start transaction request.
        Not tested"""
        print("Start remote transaction request")
        return await self.call(call.RemoteStartTransactionPayload(
            id_tag=id_tag,
            connector_id=connector_id,
            charging_profile=charging_profile
        ))

    async def send_remote_stop_transaction(self, transaction_id: int, **kwargs):
        """Sends a Stop transaction request.
        Not tested"""
        print("Stop transaction request")
        return await self.call(call.RemoteStopTransactionPayload(
            transaction_id=transaction_id
        ))

    async def send_change_availability(self, connector_id: int, type: AvailabilityType, **kwargs):
        """Sends a Change availability request.
        Tested"""
        print("Changing Availability request")
        return await self.call(call.ChangeAvailabilityPayload(
            connector_id=connector_id,
            type=type
        ))

    async def send_change_configuration(self, key: str, value: str, **kwargs):
        """Sends a Change configuration request.
        Tested"""
        print("Changing Configuration request")
        return await self.call(call.ChangeConfigurationPayload(
            key=key,
            value=value
        ))

    async def send_get_schedule(self, connector_id: int, duration: int, charging_rate_unit: ChargingRateUnitType, **kwargs):
        """Sends a Get schedule request.
        Not tested"""
        print("Get Composite Schedule request")
        return await self.call(call.GetCompositeSchedulePayload(
            connector_id=connector_id,
            duration=duration,
            charging_rate_unit=charging_rate_unit
        ))

    async def send_get_local_list(self, **kwargs):
        """Sends a Get local list request.
        Not Tested"""
        print("Get Local List request")
        return await self.call(call.GetLocalListVersionPayload(
        ))


    async def send_local_list(self, list_version: int, local_authorization_list: List, update_type: UpdateType, **kwargs):
        """Sends Local list request.
        Not tested"""
        print("Send Local List request")
        return await self.call(call.SendLocalListPayload(
            list_version=list_version,
            update_type=update_type,
            local_authorization_list=local_authorization_list
        ))


    async def send_get_configuration(self, key: List, **kwargs):
        """Sends a Get Configuration request.
        Tested"""
        print("Get Configuration request")
        return await self.call(call.GetConfigurationPayload(
            key=key
        ))

    async def send_clear_cache(self, **kwargs):
        """Sends a Clear Cache request.
        Tested"""
        print("Clearing Cache request")
        return await self.call(call.ClearCachePayload())


    async def send_reserve_now(self, connector_id: int, expiry_date:str, id_tag:str, parent_id_tag:str, reservation_id:int, **kwargs):
        """Sends a Reservation request.
        Not tested"""
        print("Sending reservation request")
        return await self.call(call.ReserveNowPayload(
            connector_id=connector_id,
            expiry_date=expiry_date,
            id_tag=id_tag,
            parent_id_tag=parent_id_tag,
            reservation_id=reservation_id
        ))

    async def send_cancel_reservation(self, reservation_id: int, **kwargs):
        """Sends a Cancel reservation request.
        Not tested"""
        print("Sending cancel reservation request")
        return await self.call(call.CancelReservationPayload(
            reservation_id=reservation_id
        ))

    async def send_reset(self, type: ResetType):
        """Sends a Reset request.
        Tested"""
        print("Reset Charge Point")
        return await self.call(call.ResetPayload(
            type=type
        ))


    async def send_trigger(self, requested_message: MessageTrigger, connector_id: int, **kwargs):
        """Sends a Trigger request.
        Not tested"""
        print("Sending Trigger Message request")
        return await self.call(call.TriggerMessagePayload(
            requested_message=requested_message,
            connector_id=connector_id
        ))


    async def send_unlock_connector(self, connector_id: int, **kwargs):
        """Sends a Unlock request.
        Not tested"""
        print("Unlocking Connector")
        return await self.call(call.UnlockConnectorPayload(
            connector_id=connector_id
        ))

    async def send_charging_profile(self, connector_id: int, cs_charging_profiles: Dict, **kwargs):
        """Sends a Charging Profile to Charge Point
        Not tested"""
        return await self.call(call.SetChargingProfilePayload(
            connector_id=connector_id,
            cs_charging_profiles={
                "chargingProfileId": 1111,
                "stackLevel": 1,
                "chargingProfilePurpose": "ChargePointMaxProfile",
                "chargingProfileKind": "Relative",
                "chargingSchedule": {
                    "chargingRateUnit": "A",
                    "chargingSchedulePeriod": [{"startPeriod": 0, "limit": 0.0}],
                },
            },
        ))

    async def send_clear_charging_profile(self, id: str, connector_id: int, charging_profile_purpose: ChargingProfilePurposeType, stack_level: int, **kwargs):
        """Sends a Clear Charging profile request.
        Not tested"""
        print("Sending clear charging profile request")
        return await self.call(call.ClearChargingProfilePayload(
        id=id,
        connector_id=connector_id,
        charging_profile_purpose=charging_profile_purpose,
        stack_level=stack_level
        ))

    async def send_get_diagnostics(self, location:str, retries: int, retry_interval: int, start_time:str, stop_time:str, **kwargs):
        """Sends a request to get diagnostics of Charge Point
        Not tested"""
        return await self.call(call.GetDiagnosticsPayload(
            location=location,
            retries=retries,
            retry_interval=retry_interval,
            start_time=start_time,
            stop_time=stop_time
        ))

    async def send_update_firmware(self, location: str, retries: int, retry_interval: int, **kwargs):
        """Sends a firmware update to Charge Point
        Not tested"""
        t = datetime.utcnow().isoformat()
        return await self.call(call.UpdateFirmwarePayload(
            location=location,
            retrieve_date= t + "Z",
            retries=retries,
            retry_interval=retry_interval
        ))
