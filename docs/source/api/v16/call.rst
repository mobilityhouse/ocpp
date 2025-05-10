OCPP 1.6 Call Messages
=====================

.. module:: ocpp.v16.call

This module contains dataclasses for OCPP 1.6 Call messages that can be sent by both Charge Points and Central Systems.

Charge Point to Central System Messages
--------------------------------------

These dataclasses represent messages that flow from Charge Point to Central System:

.. py:class:: Authorize

   Request to authorize an identifier.
   
   :param id_tag: The identifier that needs to be authorized
   :type id_tag: str

.. py:class:: BootNotification

   Sent by the Charge Point to the Central System when starting up.
   
   :param charge_point_model: Charge Point model
   :type charge_point_model: str
   :param charge_point_vendor: Charge Point vendor
   :type charge_point_vendor: str
   :param charge_box_serial_number: Charge Box serial number (optional)
   :type charge_box_serial_number: str, optional
   :param charge_point_serial_number: Charge Point serial number (optional)
   :type charge_point_serial_number: str, optional
   :param firmware_version: Firmware version (optional)
   :type firmware_version: str, optional
   :param iccid: ICCID of the SIM card (optional)
   :type iccid: str, optional
   :param imsi: IMSI of the SIM card (optional)
   :type imsi: str, optional
   :param meter_serial_number: Meter serial number (optional)
   :type meter_serial_number: str, optional
   :param meter_type: Meter type (optional)
   :type meter_type: str, optional

.. py:class:: DiagnosticsStatusNotification

   Sent by the Charge Point to the Central System to report diagnostics status.
   
   :param status: Status of the diagnostics (from enums.DiagnosticsStatus)
   :type status: enums.DiagnosticsStatus

.. py:class:: FirmwareStatusNotification

   Sent by the Charge Point to the Central System to report firmware status.
   
   :param status: Status of the firmware (from enums.FirmwareStatus)
   :type status: enums.FirmwareStatus

.. py:class:: Heartbeat

   Sent by the Charge Point to the Central System to indicate it is still alive.

.. py:class:: MeterValues

   Sent by the Charge Point to the Central System to report meter readings.
   
   :param connector_id: Connector ID
   :type connector_id: int
   :param meter_value: List of meter values
   :type meter_value: list
   :param transaction_id: Transaction ID (optional)
   :type transaction_id: int, optional

.. py:class:: StartTransaction

   Sent by the Charge Point to the Central System to start a transaction.
   
   :param connector_id: Connector ID
   :type connector_id: int
   :param id_tag: The identifier that started the transaction
   :type id_tag: str
   :param meter_start: Meter reading at start of transaction
   :type meter_start: int
   :param timestamp: Timestamp of the start
   :type timestamp: str
   :param reservation_id: Reservation ID (optional)
   :type reservation_id: int, optional

.. py:class:: StatusNotification

   Sent by the Charge Point to the Central System to report status changes.
   
   :param connector_id: Connector ID
   :type connector_id: int
   :param error_code: Error code (from enums.ChargePointErrorCode)
   :type error_code: enums.ChargePointErrorCode
   :param status: Status (from enums.ChargePointStatus)
   :type status: enums.ChargePointStatus
   :param timestamp: Timestamp of the status notification (optional)
   :type timestamp: str, optional
   :param info: Additional info (optional)
   :type info: str, optional
   :param vendor_id: Vendor ID (optional)
   :type vendor_id: str, optional
   :param vendor_error_code: Vendor error code (optional)
   :type vendor_error_code: str, optional

.. py:class:: StopTransaction

   Sent by the Charge Point to the Central System to stop a transaction.
   
   :param meter_stop: Meter reading at end of transaction
   :type meter_stop: int
   :param timestamp: Timestamp of the stop
   :type timestamp: str
   :param transaction_id: Transaction ID
   :type transaction_id: int
   :param reason: Reason for stopping (from enums.Reason, optional)
   :type reason: enums.Reason, optional
   :param id_tag: The identifier that stopped the transaction (optional)
   :type id_tag: str, optional
   :param transaction_data: List of transaction data (optional)
   :type transaction_data: list, optional

Central System to Charge Point Messages
--------------------------------------

These dataclasses represent messages that flow from Central System to Charge Point:

.. py:class:: CancelReservation

   Request to cancel a reservation.
   
   :param reservation_id: Reservation ID
   :type reservation_id: int

.. py:class:: ChangeAvailability

   Request to change the availability of a connector.
   
   :param connector_id: Connector ID
   :type connector_id: int
   :param type: Availability type (from enums.AvailabilityType)
   :type type: enums.AvailabilityType

.. py:class:: ChangeConfiguration

   Request to change a configuration parameter.
   
   :param key: Configuration key
   :type key: str
   :param value: Configuration value
   :type value: str

.. py:class:: ClearCache

   Request to clear the authorization cache.

.. py:class:: ClearChargingProfile

   Request to clear a charging profile.
   
   :param id: Charging profile ID (optional)
   :type id: int, optional
   :param connector_id: Connector ID (optional)
   :type connector_id: int, optional
   :param charging_profile_purpose: Charging profile purpose (optional)
   :type charging_profile_purpose: enums.ChargingProfilePurposeType, optional
   :param stack_level: Stack level (optional)
   :type stack_level: int, optional

.. py:class:: GetCompositeSchedule

   Request to get the composite schedule.
   
   :param connector_id: Connector ID
   :type connector_id: int
   :param duration: Duration in seconds
   :type duration: int
   :param charging_rate_unit: Charging rate unit (optional)
   :type charging_rate_unit: enums.ChargingRateUnitType, optional

.. py:class:: GetConfiguration

   Request to get configuration parameters.
   
   :param key: List of configuration keys (optional)
   :type key: list, optional

.. py:class:: GetDiagnostics

   Request to get diagnostics information.
   
   :param location: Location where to upload the diagnostics
   :type location: str
   :param retries: Number of retries (optional)
   :type retries: int, optional
   :param retry_interval: Retry interval in seconds (optional)
   :type retry_interval: int, optional
   :param start_time: Start time (optional)
   :type start_time: str, optional
   :param stop_time: Stop time (optional)
   :type stop_time: str, optional

.. py:class:: RemoteStartTransaction

   Request to start a transaction remotely.
   
   :param id_tag: The identifier to start the transaction with
   :type id_tag: str
   :param connector_id: Connector ID (optional)
   :type connector_id: int, optional
   :param charging_profile: Charging profile (optional)
   :type charging_profile: dict or datatypes.ChargingProfile, optional

.. py:class:: RemoteStopTransaction

   Request to stop a transaction remotely.
   
   :param transaction_id: Transaction ID
   :type transaction_id: int

.. py:class:: Reset

   Request to reset the Charge Point.
   
   :param type: Reset type (from enums.ResetType)
   :type type: enums.ResetType

.. py:class:: SetChargingProfile

   Request to set a charging profile.
   
   :param connector_id: Connector ID
   :type connector_id: int
   :param cs_charging_profiles: Charging profile
   :type cs_charging_profiles: datatypes.ChargingProfile or dict

Bidirectional Messages
--------------------

These dataclasses represent messages that can flow in both directions:

.. py:class:: DataTransfer

   Message to transfer data between Central System and Charge Point.
   
   :param vendor_id: Vendor ID
   :type vendor_id: str
   :param message_id: Message ID (optional)
   :type message_id: str, optional
   :param data: Data to transfer (optional)
   :type data: str, optional
