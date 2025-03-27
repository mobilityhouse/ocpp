OCPP 2.0.1 Call Messages
======================

.. module:: ocpp.v201.call

This module contains dataclasses for OCPP 2.0.1 Call messages. OCPP 2.0.1 introduces many new message types compared to OCPP 1.6.

Common Structure
--------------

Most OCPP 2.0.1 message types include a ``custom_data`` field which is optional and can be used to include additional, custom information.

Authentication Messages
--------------------

.. py:class:: Authorize

   Request to authorize an identifier.
   
   :param id_token: The ID token
   :type id_token: datatypes.IdTokenType
   :param certificate: Certificate in PEM format (optional)
   :type certificate: str, optional
   :param iso15118_certificate_hash_data: Certificate hash data (optional)
   :type iso15118_certificate_hash_data: list[datatypes.OCSPRequestDataType], optional
   :param custom_data: Custom data (optional)
   :type custom_data: dict, optional

Boot and Status Messages
---------------------

.. py:class:: BootNotification

   Sent by the Charging Station to the CSMS when starting up.
   
   :param charging_station: Information about the charging station
   :type charging_station: datatypes.ChargingStationType
   :param reason: Reason for sending the boot notification
   :type reason: enums.BootReasonEnumType
   :param custom_data: Custom data (optional)
   :type custom_data: dict, optional

.. py:class:: Heartbeat

   Sent by the Charging Station to the CSMS to indicate it is still alive.
   
   :param custom_data: Custom data (optional)
   :type custom_data: dict, optional

.. py:class:: StatusNotification

   Sent by the Charging Station to the CSMS to report status changes.
   
   :param timestamp: Timestamp of the status notification
   :type timestamp: str
   :param connector_status: Status of the connector
   :type connector_status: enums.ConnectorStatusEnumType
   :param evse_id: EVSE ID
   :type evse_id: int
   :param connector_id: Connector ID
   :type connector_id: int
   :param custom_data: Custom data (optional)
   :type custom_data: dict, optional

Transaction Messages
-----------------

.. py:class:: TransactionEvent

   Sent by the Charging Station to the CSMS to report transaction events.
   
   :param event_type: Type of the event
   :type event_type: enums.TransactionEventEnumType
   :param timestamp: Timestamp of the event
   :type timestamp: str
   :param trigger_reason: Reason that triggered the event
   :type trigger_reason: enums.TriggerReasonEnumType
   :param seq_no: Sequence number of the event
   :type seq_no: int
   :param transaction_info: Information about the transaction
   :type transaction_info: datatypes.TransactionType
   :param meter_value: List of meter values (optional)
   :type meter_value: list[datatypes.MeterValueType], optional
   :param offline: Whether the event occurred while offline (optional)
   :type offline: bool, optional
   :param number_of_phases_used: Number of phases used (optional)
   :type number_of_phases_used: int, optional
   :param cable_max_current: Maximum current of the cable (optional)
   :type cable_max_current: int, optional
   :param reservation_id: Reservation ID (optional)
   :type reservation_id: int, optional
   :param evse: EVSE information (optional)
   :type evse: datatypes.EVSEType, optional
   :param id_token: ID token (optional)
   :type id_token: datatypes.IdTokenType, optional
   :param custom_data: Custom data (optional)
   :type custom_data: dict, optional

.. py:class:: MeterValues

   Sent by the Charging Station to the CSMS to report meter values.
   
   :param evse_id: EVSE ID
   :type evse_id: int
   :param meter_value: List of meter values
   :type meter_value: list[datatypes.MeterValueType]
   :param custom_data: Custom data (optional)
   :type custom_data: dict, optional

Remote Control Messages
--------------------

.. py:class:: RequestStartTransaction

   Sent by the CSMS to the Charging Station to remotely start a transaction.
   
   :param id_token: ID token to use for the transaction
   :type id_token: datatypes.IdTokenType
   :param remote_start_id: ID for the remote start request
   :type remote_start_id: int
   :param evse_id: EVSE ID (optional)
   :type evse_id: int, optional
   :param group_id_token: Group ID token (optional)
   :type group_id_token: datatypes.IdTokenType, optional
   :param charging_profile: Charging profile (optional)
   :type charging_profile: datatypes.ChargingProfileType, optional
   :param custom_data: Custom data (optional)
   :type custom_data: dict, optional

.. py:class:: RequestStopTransaction

   Sent by the CSMS to the Charging Station to remotely stop a transaction.
   
   :param transaction_id: ID of the transaction to stop
   :type transaction_id: str
   :param custom_data: Custom data (optional)
   :type custom_data: dict, optional

Charging Profile Messages
----------------------

.. py:class:: SetChargingProfile

   Sent by the CSMS to the Charging Station to set a charging profile.
   
   :param evse_id: EVSE ID
   :type evse_id: int
   :param charging_profile: Charging profile
   :type charging_profile: datatypes.ChargingProfileType
   :param custom_data: Custom data (optional)
   :type custom_data: dict, optional

.. py:class:: ClearChargingProfile

   Sent by the CSMS to the Charging Station to clear a charging profile.
   
   :param charging_profile_id: Charging profile ID (optional)
   :type charging_profile_id: int, optional
   :param charging_profile_criteria: Criteria for clearing profiles (optional)
   :type charging_profile_criteria: datatypes.ClearChargingProfileType, optional
   :param custom_data: Custom data (optional)
   :type custom_data: dict, optional

.. py:class:: GetChargingProfiles

   Sent by the CSMS to the Charging Station to get charging profiles.
   
   :param request_id: ID for the request
   :type request_id: int
   :param charging_profile: Charging profile criteria
   :type charging_profile: datatypes.ChargingProfileCriterionType
   :param evse_id: EVSE ID (optional)
   :type evse_id: int, optional
   :param custom_data: Custom data (optional)
   :type custom_data: dict, optional

.. py:class:: ReportChargingProfiles

   Sent by the Charging Station to the CSMS to report charging profiles.
   
   :param request_id: ID of the request
   :type request_id: int
   :param charging_limit_source: Source of the charging limit
   :type charging_limit_source: enums.ChargingLimitSourceEnumType
   :param charging_profile: List of charging profiles
   :type charging_profile: list[datatypes.ChargingProfileType]
   :param evse_id: EVSE ID
   :type evse_id: int
   :param tbc: Whether more messages are to be expected (optional)
   :type tbc: bool, optional
   :param custom_data: Custom data (optional)
   :type custom_data: dict, optional

Reset and Availability Messages
----------------------------

.. py:class:: Reset

   Sent by the CSMS to the Charging Station to reset it.
   
   :param type: Type of reset
   :type type: enums.ResetEnumType
   :param evse_id: EVSE ID (optional)
   :type evse_id: int, optional
   :param custom_data: Custom data (optional)
   :type custom_data: dict, optional

.. py:class:: ChangeAvailability

   Sent by the CSMS to the Charging Station to change the availability.
   
   :param operational_status: Requested operational status
   :type operational_status: enums.OperationalStatusEnumType
   :param evse: EVSE information (optional)
   :type evse: datatypes.EVSEType, optional
   :param custom_data: Custom data (optional)
   :type custom_data: dict, optional

Data Transfer Message
------------------

.. py:class:: DataTransfer

   Sent by either the Charging Station or the CSMS to exchange custom data.
   
   :param vendor_id: Vendor ID
   :type vendor_id: str
   :param message_id: Message ID (optional)
   :type message_id: str, optional
   :param data: Data to transfer (optional)
   :type data: any, optional
   :param custom_data: Custom data (optional)
   :type custom_data: dict, optional

Variable and Monitoring Messages
-----------------------------

.. py:class:: GetVariables

   Sent by the CSMS to the Charging Station to get variable values.
   
   :param get_variable_data: List of variables to get
   :type get_variable_data: list[datatypes.GetVariableDataType]
   :param custom_data: Custom data (optional)
   :type custom_data: dict, optional

.. py:class:: SetVariables

   Sent by the CSMS to the Charging Station to set variable values.
   
   :param set_variable_data: List of variables to set
   :type set_variable_data: list[datatypes.SetVariableDataType]
   :param custom_data: Custom data (optional)
   :type custom_data: dict, optional

.. py:class:: SetVariableMonitoring

   Sent by the CSMS to the Charging Station to set up variable monitoring.
   
   :param set_monitoring_data: List of monitoring settings
   :type set_monitoring_data: list[datatypes.SetMonitoringDataType]
   :param custom_data: Custom data (optional)
   :type custom_data: dict, optional

.. py:class:: ClearVariableMonitoring

   Sent by the CSMS to the Charging Station to clear variable monitoring.
   
   :param id: List of monitoring IDs to clear
   :type id: list[int]
   :param custom_data: Custom data (optional)
   :type custom_data: dict, optional

Firmware Messages
--------------

.. py:class:: UpdateFirmware

   Sent by the CSMS to the Charging Station to update firmware.
   
   :param request_id: ID for the request
   :type request_id: int
   :param firmware: Firmware information
   :type firmware: datatypes.FirmwareType
   :param retries: Number of retries (optional)
   :type retries: int, optional
   :param retry_interval: Retry interval in seconds (optional)
   :type retry_interval: int, optional
   :param custom_data: Custom data (optional)
   :type custom_data: dict, optional

.. py:class:: FirmwareStatusNotification

   Sent by the Charging Station to the CSMS to report firmware status.
   
   :param status: Status of the firmware update
   :type status: enums.FirmwareStatusEnumType
   :param request_id: ID of the request (optional)
   :type request_id: int, optional
   :param custom_data: Custom data (optional)
   :type custom_data: dict, optional

Note: This list is not exhaustive; OCPP 2.0.1 defines many more message types for features like:

* Certificate management
* Local authorization list management
* Reservation
* Display messages
* Security events
* Smart charging
* Monitoring and diagnostics
* Remotely triggered messages
* Custom information for customers
