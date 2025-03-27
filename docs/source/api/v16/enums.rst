OCPP 1.6 Enumerations
===================

.. module:: ocpp.v16.enums

This module contains string enumerations used in OCPP 1.6 messages.

Action
-----

.. class:: Action

   Enumeration of OCPP 1.6 actions.
   
   .. attribute:: authorize
      :value: "Authorize"
   
   .. attribute:: boot_notification
      :value: "BootNotification"
   
   .. attribute:: cancel_reservation
      :value: "CancelReservation"
   
   .. attribute:: change_availability
      :value: "ChangeAvailability"
   
   .. attribute:: change_configuration
      :value: "ChangeConfiguration"
   
   .. attribute:: clear_cache
      :value: "ClearCache"
   
   .. attribute:: clear_charging_profile
      :value: "ClearChargingProfile"
   
   .. attribute:: data_transfer
      :value: "DataTransfer"
   
   .. attribute:: get_composite_schedule
      :value: "GetCompositeSchedule"
   
   .. attribute:: get_configuration
      :value: "GetConfiguration"
   
   .. attribute:: get_diagnostics
      :value: "GetDiagnostics"
   
   .. attribute:: get_local_list_version
      :value: "GetLocalListVersion"
   
   .. attribute:: heartbeat
      :value: "Heartbeat"
   
   .. attribute:: meter_values
      :value: "MeterValues"
   
   .. attribute:: remote_start_transaction
      :value: "RemoteStartTransaction"
   
   .. attribute:: remote_stop_transaction
      :value: "RemoteStopTransaction"
   
   .. attribute:: reserve_now
      :value: "ReserveNow"
   
   .. attribute:: reset
      :value: "Reset"
   
   .. attribute:: send_local_list
      :value: "SendLocalList"
   
   .. attribute:: set_charging_profile
      :value: "SetChargingProfile"
   
   .. attribute:: start_transaction
      :value: "StartTransaction"
   
   .. attribute:: status_notification
      :value: "StatusNotification"
   
   .. attribute:: stop_transaction
      :value: "StopTransaction"
   
   .. attribute:: trigger_message
      :value: "TriggerMessage"
   
   .. attribute:: unlock_connector
      :value: "UnlockConnector"
   
   .. attribute:: update_firmware
      :value: "UpdateFirmware"

   .. attribute:: diagnostics_status_notification
      :value: "DiagnosticsStatusNotification"
   
   .. attribute:: firmware_status_notification
      :value: "FirmwareStatusNotification"

Authorization Enumerations
------------------------

.. class:: AuthorizationStatus

   Authorization status in IdTagInfo.
   
   .. attribute:: accepted
      :value: "Accepted"
   
   .. attribute:: blocked
      :value: "Blocked"
   
   .. attribute:: expired
      :value: "Expired"
   
   .. attribute:: invalid
      :value: "Invalid"
   
   .. attribute:: concurrent_tx
      :value: "ConcurrentTx"

Availability Enumerations
-----------------------

.. class:: AvailabilityStatus

   Status returned in response to ChangeAvailability.req.
   
   .. attribute:: accepted
      :value: "Accepted"
   
   .. attribute:: rejected
      :value: "Rejected"
   
   .. attribute:: scheduled
      :value: "Scheduled"

.. class:: AvailabilityType

   Requested availability change in ChangeAvailability.req.
   
   .. attribute:: inoperative
      :value: "Inoperative"
   
   .. attribute:: operative
      :value: "Operative"

Charging Profile Enumerations
---------------------------

.. class:: ChargingProfileKindType

   Type of charging profile.
   
   .. attribute:: absolute
      :value: "Absolute"
   
   .. attribute:: recurring
      :value: "Recurring"
   
   .. attribute:: relative
      :value: "Relative"

.. class:: ChargingProfilePurposeType

   Purpose of the charging profile.
   
   .. attribute:: charge_point_max_profile
      :value: "ChargePointMaxProfile"
   
   .. attribute:: tx_default_profile
      :value: "TxDefaultProfile"
   
   .. attribute:: tx_profile
      :value: "TxProfile"

.. class:: ChargingProfileStatus

   Status returned in response to SetChargingProfile.req.
   
   .. attribute:: accepted
      :value: "Accepted"
   
   .. attribute:: rejected
      :value: "Rejected"
   
   .. attribute:: not_supported
      :value: "NotSupported"

.. class:: ChargingRateUnitType

   Unit in which a charging schedule is defined.
   
   .. attribute:: watts
      :value: "W"
   
   .. attribute:: amps
      :value: "A"

Charge Point Status Enumerations
------------------------------

.. class:: ChargePointErrorCode

   Charge Point error codes.
   
   .. attribute:: connector_lock_failure
      :value: "ConnectorLockFailure"
   
   .. attribute:: ev_communication_error
      :value: "EVCommunicationError"
   
   .. attribute:: ground_failure
      :value: "GroundFailure"
   
   .. attribute:: high_temperature
      :value: "HighTemperature"
   
   .. attribute:: internal_error
      :value: "InternalError"
   
   .. attribute:: local_list_conflict
      :value: "LocalListConflict"
   
   .. attribute:: no_error
      :value: "NoError"
   
   .. attribute:: other_error
      :value: "OtherError"
   
   .. attribute:: over_current_failure
      :value: "OverCurrentFailure"
   
   .. attribute:: over_voltage
      :value: "OverVoltage"
   
   .. attribute:: power_meter_failure
      :value: "PowerMeterFailure"
   
   .. attribute:: power_switch_failure
      :value: "PowerSwitchFailure"
   
   .. attribute:: reader_failure
      :value: "ReaderFailure"
   
   .. attribute:: reset_failure
      :value: "ResetFailure"
   
   .. attribute:: under_voltage
      :value: "UnderVoltage"
   
   .. attribute:: weak_signal
      :value: "WeakSignal"

.. class:: ChargePointStatus

   Status reported in StatusNotification.req.
   
   .. attribute:: available
      :value: "Available"
   
   .. attribute:: preparing
      :value: "Preparing"
   
   .. attribute:: charging
      :value: "Charging"
   
   .. attribute:: suspended_evse
      :value: "SuspendedEVSE"
   
   .. attribute:: suspended_ev
      :value: "SuspendedEV"
   
   .. attribute:: finishing
      :value: "Finishing"
   
   .. attribute:: reserved
      :value: "Reserved"
   
   .. attribute:: unavailable
      :value: "Unavailable"
   
   .. attribute:: faulted
      :value: "Faulted"

Configuration Enumerations
------------------------

.. class:: ConfigurationStatus

   Status in ChangeConfiguration.conf.
   
   .. attribute:: accepted
      :value: "Accepted"
   
   .. attribute:: rejected
      :value: "Rejected"
   
   .. attribute:: reboot_required
      :value: "RebootRequired"
   
   .. attribute:: not_supported
      :value: "NotSupported"

.. class:: ConfigurationKey

   Configuration key names.
   
   This enumeration includes a large number of predefined configuration keys, organized in categories. Some key examples include:
   
   .. attribute:: allow_offline_tx_for_unknown_id
      :value: "AllowOfflineTxForUnknownId"
   
   .. attribute:: authorization_cache_enabled
      :value: "AuthorizationCacheEnabled"
   
   .. attribute:: heartbeat_interval
      :value: "HeartbeatInterval"
   
   .. attribute:: local_auth_list_enabled
      :value: "LocalAuthListEnabled"
   
   .. attribute:: meter_value_sample_interval
      :value: "MeterValueSampleInterval"
   
   .. attribute:: reset_retries
      :value: "ResetRetries"
   
   .. attribute:: transaction_message_attempts
      :value: "TransactionMessageAttempts"
   
   .. attribute:: web_socket_ping_interval
      :value: "WebSocketPingInterval"

Meter Value Enumerations
----------------------

.. class:: Location

   Location of a sampled value in SampledValue.
   
   .. attribute:: inlet
      :value: "Inlet"
   
   .. attribute:: outlet
      :value: "Outlet"
   
   .. attribute:: body
      :value: "Body"
   
   .. attribute:: cable
      :value: "Cable"
   
   .. attribute:: ev
      :value: "EV"

.. class:: Measurand

   Measurand in SampledValue.
   
   .. attribute:: current_export
      :value: "Current.Export"
   
   .. attribute:: current_import
      :value: "Current.Import"
   
   .. attribute:: current_offered
      :value: "Current.Offered"
   
   .. attribute:: energy_active_export_register
      :value: "Energy.Active.Export.Register"
   
   .. attribute:: energy_active_import_register
      :value: "Energy.Active.Import.Register"
   
   .. attribute:: energy_reactive_export_register
      :value: "Energy.Reactive.Export.Register"
   
   .. attribute:: energy_reactive_import_register
      :value: "Energy.Reactive.Import.Register"
   
   .. attribute:: energy_active_export_interval
      :value: "Energy.Active.Export.Interval"
   
   .. attribute:: energy_active_import_interval
      :value: "Energy.Active.Import.Interval"
   
   .. attribute:: energy_reactive_export_interval
      :value: "Energy.Reactive.Export.Interval"
   
   .. attribute:: energy_reactive_import_interval
      :value: "Energy.Reactive.Import.Interval"
   
   .. attribute:: frequency
      :value: "Frequency"
   
   .. attribute:: power_active_export
      :value: "Power.Active.Export"
   
   .. attribute:: power_active_import
      :value: "Power.Active.Import"
   
   .. attribute:: power_factor
      :value: "Power.Factor"
   
   .. attribute:: power_offered
      :value: "Power.Offered"
   
   .. attribute:: power_reactive_export
      :value: "Power.Reactive.Export"
   
   .. attribute:: power_reactive_import
      :value: "Power.Reactive.Import"
   
   .. attribute:: rpm
      :value: "RPM"
   
   .. attribute:: soc
      :value: "SoC"
   
   .. attribute:: temperature
      :value: "Temperature"
   
   .. attribute:: voltage
      :value: "Voltage"

.. class:: Phase

   Phase in SampledValue.
   
   .. attribute:: l1
      :value: "L1"
   
   .. attribute:: l2
      :value: "L2"
   
   .. attribute:: l3
      :value: "L3"
   
   .. attribute:: n
      :value: "N"
   
   .. attribute:: l1_n
      :value: "L1-N"
   
   .. attribute:: l2_n
      :value: "L2-N"
   
   .. attribute:: l3_n
      :value: "L3-N"
   
   .. attribute:: l1_l2
      :value: "L1-L2"
   
   .. attribute:: l2_l3
      :value: "L2-L3"
   
   .. attribute:: l3_l1
      :value: "L3-L1"

.. class:: ReadingContext

   Context of a sampled value in SampledValue.
   
   .. attribute:: interruption_begin
      :value: "Interruption.Begin"
   
   .. attribute:: interruption_end
      :value: "Interruption.End"
   
   .. attribute:: other
      :value: "Other"
   
   .. attribute:: sample_clock
      :value: "Sample.Clock"
   
   .. attribute:: sample_periodic
      :value: "Sample.Periodic"
   
   .. attribute:: transaction_begin
      :value: "Transaction.Begin"
   
   .. attribute:: transaction_end
      :value: "Transaction.End"
   
   .. attribute:: trigger
      :value: "Trigger"

.. class:: UnitOfMeasure

   Unit of a sampled value in SampledValue.
   
   .. attribute:: wh
      :value: "Wh"
   
   .. attribute:: kwh
      :value: "kWh"
   
   .. attribute:: varh
      :value: "varh"
   
   .. attribute:: kvarh
      :value: "kvarh"
   
   .. attribute:: w
      :value: "W"
   
   .. attribute:: kw
      :value: "kW"
   
   .. attribute:: va
      :value: "VA"
   
   .. attribute:: kva
      :value: "kVA"
   
   .. attribute:: var
      :value: "var"
   
   .. attribute:: kvar
      :value: "kvar"
   
   .. attribute:: a
      :value: "A"
   
   .. attribute:: v
      :value: "V"
   
   .. attribute:: celsius
      :value: "Celsius"
   
   .. attribute:: fahrenheit
      :value: "Fahrenheit"
   
   .. attribute:: k
      :value: "K"
   
   .. attribute:: percent
      :value: "Percent"

Transaction Enumerations
----------------------

.. class:: Reason

   Reason for stopping a transaction in StopTransaction.req.
   
   .. attribute:: emergency_stop
      :value: "EmergencyStop"
   
   .. attribute:: ev_disconnected
      :value: "EVDisconnected"
   
   .. attribute:: hard_reset
      :value: "HardReset"
   
   .. attribute:: local
      :value: "Local"
   
   .. attribute:: other
      :value: "Other"
   
   .. attribute:: power_loss
      :value: "PowerLoss"
   
   .. attribute:: reboot
      :value: "Reboot"
   
   .. attribute:: remote
      :value: "Remote"
   
   .. attribute:: soft_reset
      :value: "SoftReset"
   
   .. attribute:: unlock_command
      :value: "UnlockCommand"
   
   .. attribute:: de_authorized
      :value: "DeAuthorized"

.. class:: ResetType

   Type of reset requested by Reset.req.
   
   .. attribute:: hard
      :value: "Hard"
   
   .. attribute:: soft
      :value: "Soft"

Registration Enumerations
-----------------------

.. class:: RegistrationStatus

   Result of registration in response to BootNotification.req.
   
   .. attribute:: accepted
      :value: "Accepted"
   
   .. attribute:: pending
      :value: "Pending"
   
   .. attribute:: rejected
      :value: "Rejected"

.. class:: RemoteStartStopStatus

   Result of RemoteStartTransaction.req or RemoteStopTransaction.req.
   
   .. attribute:: accepted
      :value: "Accepted"
   
   .. attribute:: rejected
      :value: "Rejected"

Security Extension Enumerations
----------------------------

.. class:: HashAlgorithm

   Hash algorithm used in CertificateHashDataType.
   
   .. attribute:: sha256
      :value: "SHA256"
   
   .. attribute:: sha384
      :value: "SHA384"
   
   .. attribute:: sha512
      :value: "SHA512"
