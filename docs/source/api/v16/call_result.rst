OCPP 1.6 Call Result Messages
===========================

.. module:: ocpp.v16.call_result

This module contains dataclasses for OCPP 1.6 Call Result messages, which are responses to Call messages.

Charge Point to Central System Responses
--------------------------------------

These dataclasses represent response messages that flow from Charge Point to Central System:

.. py:class:: CancelReservation

   Response to a CancelReservation request.
   
   :param status: Status of the cancellation (from enums.CancelReservationStatus)
   :type status: enums.CancelReservationStatus

.. py:class:: ChangeAvailability

   Response to a ChangeAvailability request.
   
   :param status: Status of the availability change (from enums.AvailabilityStatus)
   :type status: enums.AvailabilityStatus

.. py:class:: ChangeConfiguration

   Response to a ChangeConfiguration request.
   
   :param status: Status of the configuration change (from enums.ConfigurationStatus)
   :type status: enums.ConfigurationStatus

.. py:class:: ClearCache

   Response to a ClearCache request.
   
   :param status: Status of the cache clearing (from enums.ClearCacheStatus)
   :type status: enums.ClearCacheStatus

.. py:class:: ClearChargingProfile

   Response to a ClearChargingProfile request.
   
   :param status: Status of the clearing (from enums.ClearChargingProfileStatus)
   :type status: enums.ClearChargingProfileStatus

.. py:class:: GetCompositeSchedule

   Response to a GetCompositeSchedule request.
   
   :param status: Status of the request (from enums.GetCompositeScheduleStatus)
   :type status: enums.GetCompositeScheduleStatus
   :param connector_id: Connector ID (optional)
   :type connector_id: int, optional
   :param schedule_start: Schedule start time (optional)
   :type schedule_start: str, optional
   :param charging_schedule: Charging schedule (optional)
   :type charging_schedule: dict, optional

.. py:class:: GetConfiguration

   Response to a GetConfiguration request.
   
   :param configuration_key: List of configuration keys and values (optional)
   :type configuration_key: list, optional
   :param unknown_key: List of unknown configuration keys (optional)
   :type unknown_key: list, optional

.. py:class:: GetDiagnostics

   Response to a GetDiagnostics request.
   
   :param file_name: Name of the diagnostics file (optional)
   :type file_name: str, optional

.. py:class:: GetLocalListVersion

   Response to a GetLocalListVersion request.
   
   :param list_version: Version number of the local list
   :type list_version: int

.. py:class:: RemoteStartTransaction

   Response to a RemoteStartTransaction request.
   
   :param status: Status of the transaction start (from enums.RemoteStartStopStatus)
   :type status: enums.RemoteStartStopStatus

.. py:class:: RemoteStopTransaction

   Response to a RemoteStopTransaction request.
   
   :param status: Status of the transaction stop (from enums.RemoteStartStopStatus)
   :type status: enums.RemoteStartStopStatus

.. py:class:: Reset

   Response to a Reset request.
   
   :param status: Status of the reset (from enums.ResetStatus)
   :type status: enums.ResetStatus

.. py:class:: SetChargingProfile

   Response to a SetChargingProfile request.
   
   :param status: Status of the profile setting (from enums.ChargingProfileStatus)
   :type status: enums.ChargingProfileStatus

Central System to Charge Point Responses
--------------------------------------

These dataclasses represent response messages that flow from Central System to Charge Point:

.. py:class:: Authorize

   Response to an Authorize request.
   
   :param id_tag_info: Information about the ID tag
   :type id_tag_info: datatypes.IdTagInfo

.. py:class:: BootNotification

   Response to a BootNotification request.
   
   :param current_time: Current time in ISO 8601 format
   :type current_time: str
   :param interval: Heartbeat interval in seconds
   :type interval: int
   :param status: Status of the registration (from enums.RegistrationStatus)
   :type status: enums.RegistrationStatus

.. py:class:: DiagnosticsStatusNotification

   Response to a DiagnosticsStatusNotification request. This is an empty class.

.. py:class:: FirmwareStatusNotification

   Response to a FirmwareStatusNotification request. This is an empty class.

.. py:class:: Heartbeat

   Response to a Heartbeat request.
   
   :param current_time: Current time in ISO 8601 format
   :type current_time: str

.. py:class:: MeterValues

   Response to a MeterValues request. This is an empty class.

.. py:class:: StartTransaction

   Response to a StartTransaction request.
   
   :param transaction_id: Transaction ID
   :type transaction_id: int
   :param id_tag_info: Information about the ID tag
   :type id_tag_info: datatypes.IdTagInfo

.. py:class:: StatusNotification

   Response to a StatusNotification request. This is an empty class.

.. py:class:: StopTransaction

   Response to a StopTransaction request.
   
   :param id_tag_info: Information about the ID tag (optional)
   :type id_tag_info: datatypes.IdTagInfo, optional

Bidirectional Responses
--------------------

These dataclasses represent response messages that can flow in both directions:

.. py:class:: DataTransfer

   Response to a DataTransfer request.
   
   :param status: Status of the data transfer (from enums.DataTransferStatus)
   :type status: enums.DataTransferStatus
   :param data: Data returned (optional)
   :type data: str, optional
