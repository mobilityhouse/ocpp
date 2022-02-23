import logging
from datetime import datetime

from ocpp.routing import on, after
from ocpp.v16 import ChargePoint as cp
from ocpp.v16 import call, call_result
from ocpp.v16.enums import *
import http_cpo
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
    def on_heartbeat(self):
        """Recieve a heartbeat signal from Charge Point.
        Tested"""
        print("Recieved a heartbeat from: ")
        return call_result.HeartbeatPayload(
            current_time=datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S') + "Z"
        )

    @on(Action.Authorize)
    async def on_authorize(self, id_tag):
        """Recieve authorization information.
        Tested but not working"""
        authorize = await http_cpo.CentralSystem.authorize(http_cpo.CentralSystem(), id_tag)
        if authorize:
            print(datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S') + "Z", "ID Token Accepted")
            return call_result.AuthorizePayload(
                id_tag_info={
                    # 'expiry_date': 'JAN13',
                    # 'parent_id_tag': 'parent_tag',

                    'status': AuthorizationStatus.accepted
                }
            )
        elif not authorize:
            print(datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S') + "Z", "ID Token Rejected")
            return call_result.AuthorizePayload(
                id_tag_info={
                    # 'expiry_date': 'JAN13',
                    # 'parent_id_tag': 'parent_tag',

                    'status': AuthorizationStatus.invalid
                }
            )
        else:
            print(datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S') + "Z", "ID Token Rejected")
            return call_result.AuthorizePayload(
                id_tag_info={
                    # 'expiry_date': 'JAN13',
                    # 'parent_id_tag': 'Mamma_tag',

                    'status': AuthorizationStatus.expired
                }
            )

    @after(Action.Authorize)
    async def after_authorize(self, *args, **kwargs):
        """After the on decorated function is complete.
        Not developed"""
        #await self.send_remote_start_transaction(self, *args, **kwargs)
        pass


    @on(Action.StatusNotification)
    async def on_status_notification(self, timestamp, connector_id, *args, **kwargs):
        """Recieves a status notification. Should be sent to the website.
        Tested but not fully developed."""
        print("Status Update request recieved")
        return call_result.StatusNotificationPayload()

    @on(Action.StartTransaction)
    async def on_start_transaction(self, connector_id, meter_start, timestamp, reservation_id, *args, **kwargs):
        """Charge Point has started a transaction.
        Not tested"""
        print("Starting transaction request recieved")
        await http_cpo.CentralSystem.start_transaction(connector_id, meter_start, timestamp, reservation_id)
        return call_result.StartTransactionPayload(
            transaction_id=random.randint(1, 10000),
            id_tag_info={'status': AuthorizationStatus.accepted}
        )

    @on(Action.StopTransaction)
    async def on_stop_transaction(self, transaction_id, meter_stop, timestamp, reason, id_tag, transaction_list, *args, **kwargs):
        """Charge Point has stopped the transaction.
        Not tested"""
        print("Stopping transaction request recieved")
        await http_cpo.CentralSystem.start_transaction(transaction_id, meter_stop, timestamp, reason, id_tag, transaction_list)
        return call_result.StopTransactionPayload(
            id_tag_info={'status': AuthorizationStatus.accepted}
        )

    @on(Action.MeterValues)
    async def on_meter_values(self, connector_id, transaction_id, meter_values):
        """Recieve meter values.
        Not tested"""
        print("Meter Values request recieved")
        await http_cpo.CentralSystem.meter_values(connector_id, transaction_id, meter_values)
        print(f'{self.id} recieved MeterValue')
        return call_result.MeterValuesPayload()


    async def send_remote_start_transaction(self, id_tag: str, connector_id: int):
        """Send a start transaction request.
        Not tested"""
        print("Start remote transaction request")
        return await self.call(call.RemoteStartTransactionPayload(
            id_tag=id_tag,
            connector_id=connector_id
        ))

    @on(Action.DataTransfer)
    async def on_data_transfer(self, vendor_id: str, message_id: str, data: str):
        """Recieve a Data transfer.
        Not developed"""
        pass

    async def send_get_configuration(self):
        """Sends a Get Configuration request.
        Not tested"""
        print("Get Configuration request")
        return await self.call(call.GetConfigurationPayload(
            key=str
        ))


    async def send_remote_stop_transaction(self, transaction_id: int):
        """Sends a Stop transaction request.
        Not tested"""
        print("Stop transaction request")
        return await self.call(call.RemoteStopTransactionPayload(
            transaction_id=transaction_id
        ))

    async def send_change_availability(self, connector_id: int, type: str):
        """Sends a Change availability request.
        Tested"""
        print("Changing Availability request")
        return await self.call(call.ChangeAvailabilityPayload(
            connector_id=connector_id,
            type=type
        ))

    async def send_change_configuration(self, key: str, value: str):
        """Sends a Change configuration request.
        Tested"""
        print("Changing Configuration request")
        return await self.call(call.ChangeConfigurationPayload(
            key=key,
            value=value
        ))

    async def send_get_schedule(self, connector_id, duration, charging_rate_unit):
        """Sends a Get schedule request.
        Not tested"""
        print("Get Composite Schedule request")
        return await self.call(call.GetCompositeSchedulePayload(
            connector_id=connector_id,
            duration=duration,
            charging_rate_unit=charging_rate_unit
        ))

    async def send_get_local_list(self):
        """Sends a Get local list request.
        Not Tested"""
        print("Get Local List request")
        return await self.call(call.GetLocalListVersionPayload(
        ))


    async def send_local_list(self, list_version, local_authorization_list, update_type):
        """Sends Local list request.
        Not tested"""
        print("Send Local List request")
        return await self.call(call.SendLocalListPayload(
            list_version=list_version,
            update_type=update_type,
            local_authorization_list=local_authorization_list
        ))


    async def send_get_configuration(self, key):
        """Sends a Get Configuration request.
        Tested"""
        print("Get Configuration request")
        return await self.call(call.GetConfigurationPayload(
            key=key
        ))

    async def send_clear_cache(self):
        """Sends a Clear Cache request.
        Tested"""
        print("Clearing Cache request")
        return await self.call(call.ClearCachePayload())


    async def send_reserve_now(self, connector_id, expiry_date, id_tag, parent_id_tag, reservation_id):
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

    async def send_cancel_reservation(self, reservation_id):
        """Sends a Cancel reservation request.
        Not tested"""
        print("Sending cancel reservation request")
        return await self.call(call.CancelReservationPayload(
            reservation_id=reservation_id
        ))

    async def send_clear_charging_profile(self, id, connector_id, charging_profile_purpose, stack_level):
        """Sends a Clear Charging profile request.
        Not tested"""
        print("Sending clear charging profile request")
        return await self.call(call.ClearChargingProfilePayload(
            id=id,
            connector_id=connector_id,
            charging_profile_purpose=charging_profile_purpose,
            stack_level=stack_level
        ))

    async def send_reset(self, type: str):
        """Sends a Reset request.
        Tested"""
        print("Reset Charge Point")
        return await self.call(call.ResetPayload(
            type=type
        ))


    async def send_trigger(self, requested_message, connector_id: int):
        """Sends a Trigger request.
        Not tested"""
        print("Sending Trigger Message request")
        return await self.call(call.TriggerMessagePayload(
            requested_message=requested_message,
            connector_id=connector_id
        ))


    async def send_unlock_connector(self, connector_id: int):
        """Sends a Unlock request.
        Not tested"""
        print("Unlocking Connector")
        return await self.call(call.UnlockConnectorPayload(
            connector_id=connector_id
        ))

