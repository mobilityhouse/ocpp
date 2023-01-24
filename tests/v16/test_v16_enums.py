# flake8: noqa
from ocpp.v16.enums import *


def test_authorization_status():
    assert AuthorizationStatus.accepted == "Accepted"
    assert AuthorizationStatus.blocked == "Blocked"
    assert AuthorizationStatus.expired == "Expired"
    assert AuthorizationStatus.invalid == "Invalid"
    assert AuthorizationStatus.concurrent_tx == "ConcurrentTx"


def test_availability_status():
    assert AvailabilityStatus.accepted == "Accepted"
    assert AvailabilityStatus.rejected == "Rejected"
    assert AvailabilityStatus.scheduled == "Scheduled"


def test_availability_type():
    assert AvailabilityType.inoperative == "Inoperative"
    assert AvailabilityType.operative == "Operative"


def test_cancel_reservation_status():
    assert CancelReservationStatus.accepted == "Accepted"
    assert CancelReservationStatus.rejected == "Rejected"


def test_charge_point_error_code():
    assert ChargePointErrorCode.connector_lock_failure == "ConnectorLockFailure"
    assert ChargePointErrorCode.ev_communication_error == "EVCommunicationError"
    assert ChargePointErrorCode.ground_failure == "GroundFailure"
    assert ChargePointErrorCode.high_temperature == "HighTemperature"
    assert ChargePointErrorCode.internal_error == "InternalError"
    assert ChargePointErrorCode.local_list_conflict == "LocalListConflict"
    assert ChargePointErrorCode.no_error == "NoError"
    assert ChargePointErrorCode.other_error == "OtherError"
    assert ChargePointErrorCode.over_current_failure == "OverCurrentFailure"
    assert ChargePointErrorCode.over_voltage == "OverVoltage"
    assert ChargePointErrorCode.power_meter_failure == "PowerMeterFailure"
    assert ChargePointErrorCode.power_switch_failure == "PowerSwitchFailure"
    assert ChargePointErrorCode.reader_failure == "ReaderFailure"
    assert ChargePointErrorCode.reset_failure == "ResetFailure"
    assert ChargePointErrorCode.under_voltage == "UnderVoltage"
    assert ChargePointErrorCode.weak_signal == "WeakSignal"


def test_charge_point_status():
    assert ChargePointStatus.available == "Available"
    assert ChargePointStatus.preparing == "Preparing"
    assert ChargePointStatus.charging == "Charging"
    assert ChargePointStatus.suspended_evse == "SuspendedEVSE"
    assert ChargePointStatus.suspended_ev == "SuspendedEV"
    assert ChargePointStatus.finishing == "Finishing"
    assert ChargePointStatus.reserved == "Reserved"
    assert ChargePointStatus.unavailable == "Unavailable"
    assert ChargePointStatus.faulted == "Faulted"


def test_charging_profile_kind_type():
    assert ChargingProfileKindType.absolute == "Absolute"
    assert ChargingProfileKindType.recurring == "Recurring"
    assert ChargingProfileKindType.relative == "Relative"


def test_charging_profile_purpose_type():
    assert (
        ChargingProfilePurposeType.charge_point_max_profile == "ChargePointMaxProfile"
    )
    assert ChargingProfilePurposeType.tx_default_profile == "TxDefaultProfile"
    assert ChargingProfilePurposeType.tx_profile == "TxProfile"


def test_charging_profile_status():
    assert ChargingProfileStatus.accepted == "Accepted"
    assert ChargingProfileStatus.rejected == "Rejected"
    assert ChargingProfileStatus.not_supported == "NotSupported"


def test_charging_rate_unit():
    assert ChargingRateUnitType.watts == "W"
    assert ChargingRateUnitType.amps == "A"


def test_clear_cache_status():
    assert ClearCacheStatus.accepted == "Accepted"
    assert ClearCacheStatus.rejected == "Rejected"


def test_clear_charging_profile_status():
    assert ClearChargingProfileStatus.accepted == "Accepted"
    assert ClearChargingProfileStatus.unknown == "Unknown"


def test_configuration_status():
    assert ConfigurationStatus.accepted == "Accepted"
    assert ConfigurationStatus.rejected == "Rejected"
    assert ConfigurationStatus.reboot_required == "RebootRequired"
    assert ConfigurationStatus.not_supported == "NotSupported"


def test_configuration_keys():
    assert ConfigurationKey.allow_offline_tx_for_unknown_id == "AllowOfflineTxForUnknownId"
    assert ConfigurationKey.authorization_cache_enabled == "AuthorizationCacheEnabled"
    assert ConfigurationKey.authorize_remote_tx_requests == "AuthorizeRemoteTxRequests"
    assert ConfigurationKey.blink_repeat == "BlinkRepeat"
    assert ConfigurationKey.clock_aligned_data_interval == "ClockAlignedDataInterval"
    assert ConfigurationKey.connection_time_out == "ConnectionTimeOut"
    assert ConfigurationKey.connector_phase_rotation == "ConnectorPhaseRotation"
    assert ConfigurationKey.connector_phase_rotation_max_length == "ConnectorPhaseRotationMaxLength"
    assert ConfigurationKey.get_configuration_max_keys == "GetConfigurationMaxKeys"
    assert ConfigurationKey.heartbeat_interval == "HeartbeatInterval"
    assert ConfigurationKey.light_intensity == "LightIntensity"
    assert ConfigurationKey.local_authorize_offline == "LocalAuthorizeOffline"
    assert ConfigurationKey.local_pre_authorize == "LocalPreAuthorize"
    assert ConfigurationKey.max_energy_on_invalid_id == "MaxEnergyOnInvalidId"
    assert ConfigurationKey.meter_values_aligned_data == "MeterValuesAlignedData"
    assert ConfigurationKey.meter_values_aligned_data_max_length == "MeterValuesAlignedDataMaxLength"
    assert ConfigurationKey.meter_values_sampled_data == "MeterValuesSampledData"
    assert ConfigurationKey.meter_values_sampled_data_max_length == "MeterValuesSampledDataMaxLength"
    assert ConfigurationKey.meter_value_sample_interval == "MeterValueSampleInterval"
    assert ConfigurationKey.minimum_status_duration == "MinimumStatusDuration"
    assert ConfigurationKey.number_of_connectors == "NumberOfConnectors"
    assert ConfigurationKey.reset_retries == "ResetRetries"
    assert ConfigurationKey.stop_transaction_on_ev_side_disconnect == "StopTransactionOnEVSideDisconnect"
    assert ConfigurationKey.stop_transaction_on_invalid_id == "StopTransactionOnInvalidId"
    assert ConfigurationKey.stop_txn_aligned_data == "StopTxnAlignedData"
    assert ConfigurationKey.stop_txn_aligned_data_max_length == "StopTxnAlignedDataMaxLength"
    assert ConfigurationKey.stop_txn_sampled_data == "StopTxnSampledData"
    assert ConfigurationKey.stop_txn_sampled_data_max_length == "StopTxnSampledDataMaxLength"
    assert ConfigurationKey.supported_feature_profiles == "SupportedFeatureProfiles"
    assert ConfigurationKey.supported_feature_profiles_max_length == "SupportedFeatureProfilesMaxLength"
    assert ConfigurationKey.transaction_message_attempts == "TransactionMessageAttempts"
    assert ConfigurationKey.transaction_message_retry_interval == "TransactionMessageRetryInterval"
    assert ConfigurationKey.unlock_connector_on_ev_side_disconnect == "UnlockConnectorOnEVSideDisconnect"
    assert ConfigurationKey.web_socket_ping_interval == "WebSocketPingInterval"
    assert ConfigurationKey.local_auth_list_enabled == "LocalAuthListEnabled"
    assert ConfigurationKey.local_auth_list_max_length == "LocalAuthListMaxLength"
    assert ConfigurationKey.send_local_list_max_length == "SendLocalListMaxLength"
    assert ConfigurationKey.reserve_connector_zero_supported == "ReserveConnectorZeroSupported"
    assert ConfigurationKey.charge_profile_max_stack_level == "ChargeProfileMaxStackLevel"
    assert ConfigurationKey.charging_schedule_allowed_charging_rate_unit == "ChargingScheduleAllowedChargingRateUnit"
    assert ConfigurationKey.charging_schedule_max_periods == "ChargingScheduleMaxPeriods"
    assert ConfigurationKey.connector_switch_3to1_phase_supported == "ConnectorSwitch3to1PhaseSupported"
    assert ConfigurationKey.max_charging_profiles_installed == "MaxChargingProfilesInstalled"


def test_data_transfer_status():
    assert DataTransferStatus.accepted == "Accepted"
    assert DataTransferStatus.rejected == "Rejected"
    assert DataTransferStatus.unknown_message_id == "UnknownMessageId"
    assert DataTransferStatus.unknown_vendor_id == "UnknownVendorId"


def test_diagnostics_status():
    assert DiagnosticsStatus.idle == "Idle"
    assert DiagnosticsStatus.uploaded == "Uploaded"
    assert DiagnosticsStatus.upload_failed == "UploadFailed"
    assert DiagnosticsStatus.uploading == "Uploading"


def test_firmware_status():
    assert FirmwareStatus.downloaded == "Downloaded"
    assert FirmwareStatus.download_failed == "DownloadFailed"
    assert FirmwareStatus.downloading == "Downloading"
    assert FirmwareStatus.idle == "Idle"
    assert FirmwareStatus.installation_failed == "InstallationFailed"
    assert FirmwareStatus.installing == "Installing"
    assert FirmwareStatus.installed == "Installed"


def test_get_composite_schedule_status():
    assert GetCompositeScheduleStatus.accepted == "Accepted"
    assert GetCompositeScheduleStatus.rejected == "Rejected"


def test_location():
    assert Location.inlet == "Inlet"
    assert Location.outlet == "Outlet"
    assert Location.body == "Body"
    assert Location.cable == "Cable"
    assert Location.ev == "EV"


def test_measurand():
    assert Measurand.energy_active_export_register == "Energy.Active.Export.Register"
    assert Measurand.energy_active_import_register == "Energy.Active.Import.Register"
    assert (
        Measurand.energy_reactive_export_register == "Energy.Reactive.Export.Register"
    )
    assert (
        Measurand.energy_reactive_import_register == "Energy.Reactive.Import.Register"
    )
    assert Measurand.energy_active_export_interval == "Energy.Active.Export.Interval"
    assert Measurand.energy_active_import_interval == "Energy.Active.Import.Interval"
    assert (
        Measurand.energy_reactive_export_interval == "Energy.Reactive.Export.Interval"
    )
    assert (
        Measurand.energy_reactive_import_interval == "Energy.Reactive.Import.Interval"
    )
    assert Measurand.frequency == "Frequency"
    assert Measurand.power_active_export == "Power.Active.Export"
    assert Measurand.power_active_import == "Power.Active.Import"
    assert Measurand.power_factor == "Power.Factor"
    assert Measurand.power_offered == "Power.Offered"
    assert Measurand.power_reactive_export == "Power.Reactive.Export"
    assert Measurand.power_reactive_import == "Power.Reactive.Import"
    assert Measurand.current_export == "Current.Export"
    assert Measurand.current_import == "Current.Import"
    assert Measurand.current_offered == "Current.Offered"
    assert Measurand.rpm == "RPM"
    assert Measurand.soc == "SoC"
    assert Measurand.voltage == "Voltage"
    assert Measurand.temperature == "Temperature"


def test_message_trigger():
    assert MessageTrigger.boot_notification == "BootNotification"
    assert (
        MessageTrigger.diagnostics_status_notification
        == "DiagnosticsStatusNotification"
    )
    assert MessageTrigger.firmware_status_notification == "FirmwareStatusNotification"
    assert MessageTrigger.heartbeat == "Heartbeat"
    assert MessageTrigger.meter_values == "MeterValues"
    assert MessageTrigger.status_notification == "StatusNotification"


def test_phase():
    assert Phase.l1 == "L1"
    assert Phase.l2 == "L2"
    assert Phase.l3 == "L3"
    assert Phase.n == "N"
    assert Phase.l1_n == "L1-N"
    assert Phase.l2_n == "L2-N"
    assert Phase.l3_n == "L3-N"
    assert Phase.l1_l2 == "L1-L2"
    assert Phase.l2_l3 == "L2-L3"
    assert Phase.l3_l1 == "L3-L1"


def test_reading_context():
    assert ReadingContext.interruption_begin == "Interruption.Begin"
    assert ReadingContext.interruption_end == "Interruption.End"
    assert ReadingContext.other == "Other"
    assert ReadingContext.sample_clock == "Sample.Clock"
    assert ReadingContext.sample_periodic == "Sample.Periodic"
    assert ReadingContext.transaction_begin == "Transaction.Begin"
    assert ReadingContext.transaction_end == "Transaction.End"
    assert ReadingContext.trigger == "Trigger"


def test_reason():
    assert Reason.emergency_stop == "EmergencyStop"
    assert Reason.ev_disconnected == "EVDisconnected"
    assert Reason.hard_reset == "HardReset"
    assert Reason.local == "Local"
    assert Reason.other == "Other"
    assert Reason.power_loss == "PowerLoss"
    assert Reason.reboot == "Reboot"
    assert Reason.remote == "Remote"
    assert Reason.soft_reset == "SoftReset"
    assert Reason.unlock_command == "UnlockCommand"
    assert Reason.de_authorized == "DeAuthorized"


def test_recurrency_kind():
    assert RecurrencyKind.daily == "Daily"
    assert RecurrencyKind.weekly == "Weekly"


def test_registration_status():
    assert RegistrationStatus.accepted == "Accepted"
    assert RegistrationStatus.pending == "Pending"
    assert RegistrationStatus.rejected == "Rejected"


def test_remote_start_stop_status():
    assert RemoteStartStopStatus.accepted == "Accepted"
    assert RemoteStartStopStatus.rejected == "Rejected"


def test_reservation_status():
    assert ReservationStatus.accepted == "Accepted"
    assert ReservationStatus.faulted == "Faulted"
    assert ReservationStatus.occupied == "Occupied"
    assert ReservationStatus.rejected == "Rejected"
    assert ReservationStatus.unavailable == "Unavailable"


def test_reset_status():
    assert ResetStatus.accepted == "Accepted"
    assert ResetStatus.rejected == "Rejected"


def test_reset_type():
    assert ResetType.hard == "Hard"
    assert ResetType.soft == "Soft"


def test_trigger_message_status():
    assert TriggerMessageStatus.accepted == "Accepted"
    assert TriggerMessageStatus.rejected == "Rejected"
    assert TriggerMessageStatus.not_implemented == "NotImplemented"


def test_unit_of_measure():
    assert UnitOfMeasure.wh == "Wh"
    assert UnitOfMeasure.kwh == "kWh"
    assert UnitOfMeasure.varh == "varh"
    assert UnitOfMeasure.kvarh == "kvarh"
    assert UnitOfMeasure.w == "W"
    assert UnitOfMeasure.kw == "kW"
    assert UnitOfMeasure.va == "VA"
    assert UnitOfMeasure.kva == "kVA"
    assert UnitOfMeasure.var == "var"
    assert UnitOfMeasure.kvar == "kvar"
    assert UnitOfMeasure.a == "A"
    assert UnitOfMeasure.v == "V"
    assert UnitOfMeasure.celsius == "Celsius"
    assert UnitOfMeasure.fahrenheit == "Fahrenheit"
    assert UnitOfMeasure.k == "K"
    assert UnitOfMeasure.percent == "Percent"
    assert UnitOfMeasure.hertz == "Hertz"


def test_unlock_status():
    assert UnlockStatus.unlocked == "Unlocked"
    assert UnlockStatus.unlock_failed == "UnlockFailed"
    assert UnlockStatus.not_supported == "NotSupported"


def test_update_status():
    assert UpdateStatus.accepted == "Accepted"
    assert UpdateStatus.failed == "Failed"
    assert UpdateStatus.not_supported == "NotSupported"
    assert UpdateStatus.version_mismatch == "VersionMismatch"


def test_update_type():
    assert UpdateType.differential == "Differential"
    assert UpdateType.full == "Full"


def test_value_format():
    assert ValueFormat.raw == "Raw"
    assert ValueFormat.signed_data == "SignedData"
