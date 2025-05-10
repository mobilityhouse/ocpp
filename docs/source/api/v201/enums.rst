OCPP 2.0.1 Enumerations
=====================

.. module:: ocpp.v201.enums

This module contains string enumerations used in OCPP 2.0.1 messages. OCPP 2.0.1 introduces many more enumerations compared to OCPP 1.6.

Core Enumerations
---------------

Action
^^^^^^

.. class:: Action

   Enumeration of OCPP 2.0.1 actions.
   
   Includes all available actions such as:
   
   .. attribute:: authorize
      :value: "Authorize"
   
   .. attribute:: boot_notification
      :value: "BootNotification"
   
   .. attribute:: cancel_reservation
      :value: "CancelReservation"
   
   .. attribute:: certificate_signed
      :value: "CertificateSigned"
   
   .. attribute:: change_availability
      :value: "ChangeAvailability"
   
   .. attribute:: clear_cache
      :value: "ClearCache"
   
   .. attribute:: clear_charging_profile
      :value: "ClearChargingProfile"
   
   .. attribute:: data_transfer
      :value: "DataTransfer"
   
   .. attribute:: get_15118_ev_certificate
      :value: "Get15118EVCertificate"
   
   .. attribute:: get_certificate_status
      :value: "GetCertificateStatus"
   
   .. attribute:: get_charging_profiles
      :value: "GetChargingProfiles"
   
   .. attribute:: get_composite_schedule
      :value: "GetCompositeSchedule"
   
   .. attribute:: get_local_list_version
      :value: "GetLocalListVersion"
   
   .. attribute:: heartbeat
      :value: "Heartbeat"
   
   .. attribute:: meter_values
      :value: "MeterValues"
   
   .. attribute:: request_start_transaction
      :value: "RequestStartTransaction"
   
   .. attribute:: request_stop_transaction
      :value: "RequestStopTransaction"
   
   .. attribute:: reserve_now
      :value: "ReserveNow"
   
   .. attribute:: reset
      :value: "Reset"
   
   .. attribute:: security_event_notification
      :value: "SecurityEventNotification"
   
   .. attribute:: send_local_list
      :value: "SendLocalList"
   
   .. attribute:: set_charging_profile
      :value: "SetChargingProfile"
   
   .. attribute:: set_variable_monitoring
      :value: "SetVariableMonitoring"
   
   .. attribute:: set_variables
      :value: "SetVariables"
   
   .. attribute:: sign_certificate
      :value: "SignCertificate"
   
   .. attribute:: status_notification
      :value: "StatusNotification"
   
   .. attribute:: transaction_event
      :value: "TransactionEvent"
   
   .. attribute:: trigger_message
      :value: "TriggerMessage"
   
   .. attribute:: unlock_connector
      :value: "UnlockConnector"
   
   .. attribute:: update_firmware
      :value: "UpdateFirmware"
   
   *And many more actions specific to OCPP 2.0.1*

GenericStatusEnumType
^^^^^^^^^^^^^^^^^^^

.. class:: GenericStatusEnumType

   Generic message response status.
   
   .. attribute:: accepted
      :value: "Accepted"
   
   .. attribute:: rejected
      :value: "Rejected"

Authorization & Authentication Enumerations
----------------------------------------

AuthorizationStatusEnumType
^^^^^^^^^^^^^^^^^^^^^^^^^

.. class:: AuthorizationStatusEnumType

   Status of an authorization.
   
   .. attribute:: accepted
      :value: "Accepted"
   
   .. attribute:: blocked
      :value: "Blocked"
   
   .. attribute:: concurrent_tx
      :value: "ConcurrentTx"
   
   .. attribute:: expired
      :value: "Expired"
   
   .. attribute:: invalid
      :value: "Invalid"
   
   .. attribute:: no_credit
      :value: "NoCredit"
   
   .. attribute:: not_allowed_type_evse
      :value: "NotAllowedTypeEVSE"
   
   .. attribute:: not_at_this_location
      :value: "NotAtThisLocation"
   
   .. attribute:: not_at_this_time
      :value: "NotAtThisTime"
   
   .. attribute:: unknown
      :value: "Unknown"

IdTokenEnumType
^^^^^^^^^^^^^

.. class:: IdTokenEnumType

   Types of identification tokens.
   
   .. attribute:: central
      :value: "Central"
   
   .. attribute:: e_maid
      :value: "eMAID"
   
   .. attribute:: iso14443
      :value: "ISO14443"
   
   .. attribute:: iso15693
      :value: "ISO15693"
   
   .. attribute:: key_code
      :value: "KeyCode"
   
   .. attribute:: local
      :value: "Local"
   
   .. attribute:: mac_address
      :value: "MacAddress"
   
   .. attribute:: no_authorization
      :value: "NoAuthorization"

Charging Related Enumerations
---------------------------

ChargingProfilePurposeEnumType
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. class:: ChargingProfilePurposeEnumType

   Purpose of the charging profile.
   
   .. attribute:: charging_station_external_constraints
      :value: "ChargingStationExternalConstraints"
   
   .. attribute:: charging_station_max_profile
      :value: "ChargingStationMaxProfile"
   
   .. attribute:: tx_default_profile
      :value: "TxDefaultProfile"
   
   .. attribute:: tx_profile
      :value: "TxProfile"

ChargingProfileKindEnumType
^^^^^^^^^^^^^^^^^^^^^^^^^

.. class:: ChargingProfileKindEnumType

   Kind of charging profile.
   
   .. attribute:: absolute
      :value: "Absolute"
   
   .. attribute:: recurring
      :value: "Recurring"
   
   .. attribute:: relative
      :value: "Relative"

ChargingLimitSourceEnumType
^^^^^^^^^^^^^^^^^^^^^^^^^

.. class:: ChargingLimitSourceEnumType

   Source of the charging limit.
   
   .. attribute:: ems
      :value: "EMS"
   
   .. attribute:: other
      :value: "Other"
   
   .. attribute:: so
      :value: "SO"
   
   .. attribute:: cso
      :value: "CSO"

ChargingRateUnitEnumType
^^^^^^^^^^^^^^^^^^^^^^

.. class:: ChargingRateUnitEnumType

   Unit of charging rate.
   
   .. attribute:: watts
      :value: "W"
   
   .. attribute:: amps
      :value: "A"

ChargingStateEnumType
^^^^^^^^^^^^^^^^^^^

.. class:: ChargingStateEnumType

   State of the charging process.
   
   .. attribute:: charging
      :value: "Charging"
   
   .. attribute:: ev_connected
      :value: "EVConnected"
   
   .. attribute:: suspended_ev
      :value: "SuspendedEV"
   
   .. attribute:: suspended_evse
      :value: "SuspendedEVSE"
   
   .. attribute:: idle
      :value: "Idle"

Connector and EVSE Enumerations
----------------------------

ConnectorStatusEnumType
^^^^^^^^^^^^^^^^^^^^^

.. class:: ConnectorStatusEnumType

   Status of a connector.
   
   .. attribute:: available
      :value: "Available"
   
   .. attribute:: occupied
      :value: "Occupied"
   
   .. attribute:: reserved
      :value: "Reserved"
   
   .. attribute:: unavailable
      :value: "Unavailable"
   
   .. attribute:: faulted
      :value: "Faulted"

ConnectorEnumType
^^^^^^^^^^^^^^^

.. class:: ConnectorEnumType

   Types of connectors.
   
   Includes a wide range of connector types such as:
   
   .. attribute:: c_ccs1
      :value: "cCCS1"
   
   .. attribute:: c_ccs2
      :value: "cCCS2"
   
   .. attribute:: c_chao_ji
      :value: "cChaoJi"
   
   .. attribute:: c_g105
      :value: "cG105"
   
   .. attribute:: c_tesla
      :value: "cTesla"
   
   .. attribute:: c_type1
      :value: "cType1"
   
   .. attribute:: c_type2
      :value: "cType2"
   
   .. attribute:: s_type2
      :value: "sType2"
   
   .. attribute:: s_type3
      :value: "sType3"
   
   *And many more connector types*

BootReasonEnumType
^^^^^^^^^^^^^^^^

.. class:: BootReasonEnumType

   Reason for sending boot notification.
   
   .. attribute:: application_reset
      :value: "ApplicationReset"
   
   .. attribute:: firmware_update
      :value: "FirmwareUpdate"
   
   .. attribute:: local_reset
      :value: "LocalReset"
   
   .. attribute:: power_up
      :value: "PowerUp"
   
   .. attribute:: remote_reset
      :value: "RemoteReset"
   
   .. attribute:: scheduled_reset
      :value: "ScheduledReset"
   
   .. attribute:: triggered
      :value: "Triggered"
   
   .. attribute:: unknown
      :value: "Unknown"
   
   .. attribute:: watchdog
      :value: "Watchdog"

OperationalStatusEnumType
^^^^^^^^^^^^^^^^^^^^^^^

.. class:: OperationalStatusEnumType

   Requested availability change.
   
   .. attribute:: inoperative
      :value: "Inoperative"
   
   .. attribute:: operative
      :value: "Operative"

Registration Enumerations
-----------------------

RegistrationStatusEnumType
^^^^^^^^^^^^^^^^^^^^^^^^

.. class:: RegistrationStatusEnumType

   Status of registration.
   
   .. attribute:: accepted
      :value: "Accepted"
   
   .. attribute:: pending
      :value: "Pending"
   
   .. attribute:: rejected
      :value: "Rejected"

ResetEnumType
^^^^^^^^^^^

.. class:: ResetEnumType

   Type of reset.
   
   .. attribute:: immediate
      :value: "Immediate"
   
   .. attribute:: on_idle
      :value: "OnIdle"

Transaction Enumerations
---------------------

TransactionEventEnumType
^^^^^^^^^^^^^^^^^^^^^

.. class:: TransactionEventEnumType

   Type of transaction event.
   
   .. attribute:: ended
      :value: "Ended"
   
   .. attribute:: started
      :value: "Started"
   
   .. attribute:: updated
      :value: "Updated"

TriggerReasonEnumType
^^^^^^^^^^^^^^^^^^^

.. class:: TriggerReasonEnumType

   Reason for a transaction event.
   
   .. attribute:: authorized
      :value: "Authorized"
   
   .. attribute:: cable_plugged_in
      :value: "CablePluggedIn"
   
   .. attribute:: charging_rate_changed
      :value: "ChargingRateChanged"
   
   .. attribute:: charging_state_changed
      :value: "ChargingStateChanged"
   
   .. attribute:: deauthorized
      :value: "Deauthorized"
   
   .. attribute:: energy_limit_reached
      :value: "EnergyLimitReached"
   
   .. attribute:: ev_communication_lost
      :value: "EVCommunicationLost"
   
   .. attribute:: ev_connect_timeout
      :value: "EVConnectTimeout"
   
   .. attribute:: meter_value_clock
      :value: "MeterValueClock"
   
   .. attribute:: meter_value_periodic
      :value: "MeterValuePeriodic"
   
   .. attribute:: time_limit_reached
      :value: "TimeLimitReached"
   
   .. attribute:: trigger
      :value: "Trigger"
   
   .. attribute:: unlock_command
      :value: "UnlockCommand"
   
   .. attribute:: stop_authorized
      :value: "StopAuthorized"
   
   .. attribute:: ev_departed
      :value: "EVDeparted"
   
   .. attribute:: ev_detected
      :value: "EVDetected"
   
   .. attribute:: remote_stop
      :value: "RemoteStop"
   
   .. attribute:: remote_start
      :value: "RemoteStart"
   
   *And several other trigger reasons*

ReasonEnumType
^^^^^^^^^^^^

.. class:: ReasonEnumType

   Reason for stopping a transaction.
   
   .. attribute:: de_authorized
      :value: "DeAuthorized"
   
   .. attribute:: emergency_stop
      :value: "EmergencyStop"
   
   .. attribute:: energy_limit_reached
      :value: "EnergyLimitReached"
   
   .. attribute:: ev_disconnected
      :value: "EVDisconnected"
   
   .. attribute:: ground_fault
      :value: "GroundFault"
   
   .. attribute:: immediate_reset
      :value: "ImmediateReset"
   
   .. attribute:: local
      :value: "Local"
   
   .. attribute:: local_out_of_credit
      :value: "LocalOutOfCredit"
   
   .. attribute:: master_pass
      :value: "MasterPass"
   
   .. attribute:: other
      :value: "Other"
   
   .. attribute:: overcurrent_fault
      :value: "OvercurrentFault"
   
   .. attribute:: power_loss
      :value: "PowerLoss"
   
   .. attribute:: power_quality
      :value: "PowerQuality"
   
   .. attribute:: reboot
      :value: "Reboot"
   
   .. attribute:: remote
      :value: "Remote"
   
   .. attribute:: soc_limit_reached
      :value: "SOCLimitReached"
   
   .. attribute:: stopped_by_ev
      :value: "StoppedByEV"
   
   .. attribute:: time_limit_reached
      :value: "TimeLimitReached"
   
   .. attribute:: timeout
      :value: "Timeout"

RequestStartStopStatusEnumType
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. class:: RequestStartStopStatusEnumType

   Status of a remote start/stop request.
   
   .. attribute:: accepted
      :value: "Accepted"
   
   .. attribute:: rejected
      :value: "Rejected"

Meter Value Enumerations
---------------------

MeasurandEnumType
^^^^^^^^^^^^^^^

.. class:: MeasurandEnumType

   Type of measurand in SampledValue.
   
   Includes a wide range of measurands such as:
   
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
   
   .. attribute:: energy_active_net
      :value: "Energy.Active.Net"
   
   .. attribute:: energy_reactive_export_interval
      :value: "Energy.Reactive.Export.Interval"
   
   .. attribute:: energy_reactive_import_interval
      :value: "Energy.Reactive.Import.Interval"
   
   .. attribute:: energy_reactive_net
      :value: "Energy.Reactive.Net"
   
   .. attribute:: energy_apparent_net
      :value: "Energy.Apparent.Net"
   
   .. attribute:: energy_apparent_import
      :value: "Energy.Apparent.Import"
   
   .. attribute:: energy_apparent_export
      :value: "Energy.Apparent.Export"
   
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
   
   .. attribute:: soc
      :value: "SoC"
   
   .. attribute:: voltage
      :value: "Voltage"

PhaseEnumType
^^^^^^^^^^^

.. class:: PhaseEnumType

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

ReadingContextEnumType
^^^^^^^^^^^^^^^^^^^^

.. class:: ReadingContextEnumType

   Context of a sampled value.
   
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

LocationEnumType
^^^^^^^^^^^^^^

.. class:: LocationEnumType

   Location of a sampled value.
   
   .. attribute:: body
      :value: "Body"
   
   .. attribute:: cable
      :value: "Cable"
   
   .. attribute:: ev
      :value: "EV"
   
   .. attribute:: inlet
      :value: "Inlet"
   
   .. attribute:: outlet
      :value: "Outlet"

Variable Management Enumerations
-----------------------------

AttributeEnumType
^^^^^^^^^^^^^^^

.. class:: AttributeEnumType

   Type of attribute in variable monitoring.
   
   .. attribute:: actual
      :value: "Actual"
   
   .. attribute:: target
      :value: "Target"
   
   .. attribute:: min_set
      :value: "MinSet"
   
   .. attribute:: max_set
      :value: "MaxSet"

MonitorEnumType
^^^^^^^^^^^^^

.. class:: MonitorEnumType

   Type of monitoring.
   
   .. attribute:: upper_threshold
      :value: "UpperThreshold"
   
   .. attribute:: lower_threshold
      :value: "LowerThreshold"
   
   .. attribute:: delta
      :value: "Delta"
   
   .. attribute:: periodic
      :value: "Periodic"
   
   .. attribute:: periodic_clock_aligned
      :value: "PeriodicClockAligned"

SetMonitoringStatusEnumType
^^^^^^^^^^^^^^^^^^^^^^^^^

.. class:: SetMonitoringStatusEnumType

   Status in SetVariableMonitoringResponse.
   
   .. attribute:: accepted
      :value: "Accepted"
   
   .. attribute:: unknown_component
      :value: "UnknownComponent"
   
   .. attribute:: unknown_variable
      :value: "UnknownVariable"
   
   .. attribute:: unsupported_monitor_type
      :value: "UnsupportedMonitorType"
   
   .. attribute:: rejected
      :value: "Rejected"
   
   .. attribute:: duplicate
      :value: "Duplicate"

GetVariableStatusEnumType
^^^^^^^^^^^^^^^^^^^^^^^

.. class:: GetVariableStatusEnumType

   Status in GetVariablesResponse.
   
   .. attribute:: accepted
      :value: "Accepted"
   
   .. attribute:: rejected
      :value: "Rejected"
   
   .. attribute:: unknown_component
      :value: "UnknownComponent"
   
   .. attribute:: unknown_variable
      :value: "UnknownVariable"
   
   .. attribute:: not_supported_attribute_type
      :value: "NotSupportedAttributeType"

SetVariableStatusEnumType
^^^^^^^^^^^^^^^^^^^^^^^

.. class:: SetVariableStatusEnumType

   Status in SetVariablesResponse.
   
   .. attribute:: accepted
      :value: "Accepted"
   
   .. attribute:: rejected
      :value: "Rejected"
   
   .. attribute:: unknown_component
      :value: "UnknownComponent"
   
   .. attribute:: unknown_variable
      :value: "UnknownVariable"
   
   .. attribute:: not_supported_attribute_type
      :value: "NotSupportedAttributeType"
   
   .. attribute:: reboot_required
      :value: "RebootRequired"

Firmware Management Enumerations
-----------------------------

FirmwareStatusEnumType
^^^^^^^^^^^^^^^^^^^^

.. class:: FirmwareStatusEnumType

   Status of a firmware update.
   
   .. attribute:: downloaded
      :value: "Downloaded"
   
   .. attribute:: download_failed
      :value: "DownloadFailed"
   
   .. attribute:: downloading
      :value: "Downloading"
   
   .. attribute:: download_scheduled
      :value: "DownloadScheduled"
   
   .. attribute:: download_paused
      :value: "DownloadPaused"
   
   .. attribute:: idle
      :value: "Idle"
   
   .. attribute:: installation_failed
      :value: "InstallationFailed"
   
   .. attribute:: installing
      :value: "Installing"
   
   .. attribute:: installed
      :value: "Installed"
   
   .. attribute:: install_rebooting
      :value: "InstallRebooting"
   
   .. attribute:: install_scheduled
      :value: "InstallScheduled"
   
   .. attribute:: install_verification_failed
      :value: "InstallVerificationFailed"
   
   .. attribute:: invalid_signature
      :value: "InvalidSignature"
   
   .. attribute:: signature_verified
      :value: "SignatureVerified"

Security Enumerations
------------------

HashAlgorithmEnumType
^^^^^^^^^^^^^^^^^^^

.. class:: HashAlgorithmEnumType

   Hash algorithm used.
   
   .. attribute:: sha256
      :value: "SHA256"
   
   .. attribute:: sha384
      :value: "SHA384"
   
   .. attribute:: sha512
      :value: "SHA512"

Security-Related Enum Types
^^^^^^^^^^^^^^^^^^^^^^^^^^

OCPP 2.0.1 introduces many security-related enumerations to support enhanced security features such as:

* ``AuthorizeCertificateStatusEnumType`` - Status of an EV Contract certificate
* ``CertificateSignedStatusEnumType`` - Status of certificate signing
* ``CertificateSigningUseEnumType`` - Use of certificate signing
* ``DeleteCertificateStatusEnumType`` - Status of certificate deletion
* ``GetCertificateIdUseEnumType`` - Certificate usage types
* ``GetCertificateStatusEnumType`` - Status of certificate retrieval
* ``InstallCertificateStatusEnumType`` - Status of certificate installation
* ``InstallCertificateUseEnumType`` - Usage of certificate installation

Component Variables
-----------------

OCPP 2.0.1 defines a wide range of standardized component variable names as enumerations, categorized by component type:

* ``ControllerComponentName`` - Logical controller components like "AlignedDataCtrlr", "AuthCtrlr", etc.
* ``PhysicalComponentName`` - Physical components like "ChargingStation", "Connector", "EVSE", etc.
* ``StandardizedVariableName`` - Generic variable names applicable to multiple components
* Component-specific variable enums (e.g., ``ConnectedEVVariableName``, ``ChargingStationVariableName``)

These component variables form the backbone of OCPP 2.0.1's component-variable model that enables more flexible configuration and monitoring.

Standard Units of Measure
----------------------

.. class:: StandardizedUnitsOfMeasureType

   Standardized units of measure used in meter values.
   
   Includes units like:
   
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
   
   *And many other standardized units*

Note: This document covers only the most commonly used enumerations in OCPP 2.0.1. The actual implementation includes many more specialized enumerations. See the source code for the complete list of enum values.
