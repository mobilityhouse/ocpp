try:
    # breaking change introduced in python 3.11
    from enum import StrEnum
except ImportError:  # pragma: no cover
    from enum import Enum  # pragma: no cover

    class StrEnum(str, Enum):  # pragma: no cover
        pass  # pragma: no cover


class Action(StrEnum):
    """An Action is a required part of a Call message."""

    authorize = "Authorize"
    boot_notification = "BootNotification"
    cancel_reservation = "CancelReservation"
    certificate_signed = "CertificateSigned"
    change_availability = "ChangeAvailability"
    change_configuration = "ChangeConfiguration"
    clear_cache = "ClearCache"
    clear_charging_profile = "ClearChargingProfile"
    data_transfer = "DataTransfer"
    delete_certificate = "DeleteCertificate"
    diagnostics_status_notification = "DiagnosticsStatusNotification"
    extended_trigger_message = "ExtendedTriggerMessage"
    firmware_status_notification = "FirmwareStatusNotification"
    get_composite_schedule = "GetCompositeSchedule"
    get_configuration = "GetConfiguration"
    get_diagnostics = "GetDiagnostics"
    get_installed_certificate_ids = "GetInstalledCertificateIds"
    get_local_list_version = "GetLocalListVersion"
    get_log = "GetLog"
    heartbeat = "Heartbeat"
    install_certificate = "InstallCertificate"
    log_status_notification = "LogStatusNotification"
    meter_values = "MeterValues"
    remote_start_transaction = "RemoteStartTransaction"
    remote_stop_transaction = "RemoteStopTransaction"
    reserve_now = "ReserveNow"
    reset = "Reset"
    security_event_notification = "SecurityEventNotification"
    send_local_list = "SendLocalList"
    set_charging_profile = "SetChargingProfile"
    sign_certificate = "SignCertificate"
    signed_firmware_status_notification = "SignedFirmwareStatusNotification"
    signed_update_firmware = "SignedUpdateFirmware"
    start_transaction = "StartTransaction"
    status_notification = "StatusNotification"
    stop_transaction = "StopTransaction"
    trigger_message = "TriggerMessage"
    unlock_connector = "UnlockConnector"
    update_firmware = "UpdateFirmware"


class AuthorizationStatus(StrEnum):
    """
    Elements that constitute an entry of a Local Authorization List update.
    """

    accepted = "Accepted"
    blocked = "Blocked"
    expired = "Expired"
    invalid = "Invalid"
    concurrent_tx = "ConcurrentTx"


class AvailabilityStatus(StrEnum):
    """
    Status returned in response to ChangeAvailability.req.
    """

    accepted = "Accepted"
    rejected = "Rejected"
    scheduled = "Scheduled"


class AvailabilityType(StrEnum):
    """
    Requested availability change in ChangeAvailability.req.
    """

    inoperative = "Inoperative"
    operative = "Operative"


class CancelReservationStatus(StrEnum):
    """
    Status in CancelReservation.conf.
    """

    accepted = "Accepted"
    rejected = "Rejected"


class CertificateSignedStatus(StrEnum):
    """
    CertificateSignedStatusEnumType is used by: CertificateSigned.conf
    """

    accepted = "Accepted"
    rejected = "Rejected"


class CertificateStatus(StrEnum):
    """
    CertificateStatusEnumType is used by: InstallCertificate.conf
    """

    accepted = "Accepted"
    rejected = "Rejected"
    failed = "Failed"


class CertificateUse(StrEnum):
    """
    CertificateUseEnumType is used by: GetInstalledCertificateIds.req,
    InstallCertificate.req
    """

    central_system_root_certificate = "CentralSystemRootCertificate"
    manufacturer_root_certificate = "ManufacturerRootCertificate"


class ChargePointErrorCode(StrEnum):
    """
    Charge Point status reported in StatusNotification.req.
    """

    connector_lock_failure = "ConnectorLockFailure"
    ev_communication_error = "EVCommunicationError"
    ground_failure = "GroundFailure"
    high_temperature = "HighTemperature"
    internal_error = "InternalError"
    local_list_conflict = "LocalListConflict"
    no_error = "NoError"
    other_error = "OtherError"
    over_current_failure = "OverCurrentFailure"
    over_voltage = "OverVoltage"
    power_meter_failure = "PowerMeterFailure"
    power_switch_failure = "PowerSwitchFailure"
    reader_failure = "ReaderFailure"
    reset_failure = "ResetFailure"
    under_voltage = "UnderVoltage"
    weak_signal = "WeakSignal"


class ChargePointStatus(StrEnum):
    """
    Status reported in StatusNotification.req. A status can be reported for
    the Charge Point main controller (connectorId = 0) or for a specific
    connector. Status for the Charge Point main controller is a subset of the
    enumeration: Available, Unavailable or Faulted.

    States considered Operative are: Available, Preparing, Charging,
    SuspendedEVSE, SuspendedEV, Finishing, Reserved.
    States considered Inoperative are: Unavailable, Faulted.
    """

    available = "Available"
    preparing = "Preparing"
    charging = "Charging"
    suspended_evse = "SuspendedEVSE"
    suspended_ev = "SuspendedEV"
    finishing = "Finishing"
    reserved = "Reserved"
    unavailable = "Unavailable"
    faulted = "Faulted"


class ChargingProfileKindType(StrEnum):
    """
    "Absolute": Schedule periods are relative to a fixed point in time defined
                in the schedule.
    "Recurring": Schedule restarts periodically at the first schedule period.
    "Relative": Schedule periods are relative to a situation- specific start
                point(such as the start of a session)
    """

    absolute = "Absolute"
    recurring = "Recurring"
    relative = "Relative"


class ChargingProfilePurposeType(StrEnum):
    """
    In load balancing scenarios, the Charge Point has one or more local
    charging profiles that limit the power or current to be shared by all
    connectors of the Charge Point. The Central System SHALL configure such
    a profile with ChargingProfilePurpose set to “ChargePointMaxProfile”.
    ChargePointMaxProfile can only be set at Charge Point ConnectorId 0.

    Default schedules for new transactions MAY be used to impose charging
    policies. An example could be a policy that prevents charging during
    the day. For schedules of this purpose, ChargingProfilePurpose SHALL
    be set to TxDefaultProfile. If TxDefaultProfile is set to ConnectorId 0,
    the TxDefaultProfile is applicable to all Connectors. If ConnectorId is
    set >0, it only applies to that specific connector. In the event a
    TxDefaultProfile for connector 0 is installed, and the Central
    System sends a new profile with ConnectorId >0, the TxDefaultProfile
    SHALL be replaced only for that specific connector.

    If a transaction-specific profile with purpose TxProfile is present,
    it SHALL overrule the default charging profile with purpose
    TxDefaultProfile for the duration of the current transaction only.
    After the transaction is stopped, the profile SHOULD be deleted.
    If there is no transaction active on the connector specified in a
    charging profile of type TxProfile, then the Charge Point SHALL
    discard it and return an error status in SetChargingProfile.conf.
    TxProfile SHALL only be set at Charge Point ConnectorId >0.

    It is not possible to set a ChargingProfile with purpose set to
    TxProfile without presence of an active transaction, or in advance of
    a transaction.

    In order to ensure that the updated charging profile applies only to the
    current transaction, the chargingProfilePurpose of the ChargingProfile
    MUST be set to TxProfile.
    """

    charge_point_max_profile = "ChargePointMaxProfile"
    tx_default_profile = "TxDefaultProfile"
    tx_profile = "TxProfile"


class ChargingProfileStatus(StrEnum):
    """
    Status returned in response to SetChargingProfile.req.
    """

    accepted = "Accepted"
    rejected = "Rejected"
    not_supported = "NotSupported"


class ChargingRateUnitType(StrEnum):
    """
    Unit in which a charging schedule is defined, as used in:
    GetCompositeSchedule.req and ChargingSchedule
    """

    watts = "W"
    amps = "A"


class CiStringType(int):
    """
    Generic used case insensitive string of X characters
    """

    ci_string_20 = 20
    ci_string_25 = 25
    ci_string_50 = 50
    ci_string_255 = 255
    ci_string_500 = 500


class ClearCacheStatus(StrEnum):
    """
    Status returned in response to ClearCache.req.
    """

    accepted = "Accepted"
    rejected = "Rejected"


class ClearChargingProfileStatus(StrEnum):
    """
    Status returned in response to ClearChargingProfile.req.
    """

    accepted = "Accepted"
    unknown = "Unknown"


class ConfigurationStatus(StrEnum):
    """
    Status in ChangeConfiguration.conf.
    """

    accepted = "Accepted"
    rejected = "Rejected"
    reboot_required = "RebootRequired"
    not_supported = "NotSupported"


class ConfigurationKey(StrEnum):
    """
    Configuration Key Names.
    """

    # 9.1 Core Profile
    allow_offline_tx_for_unknown_id = "AllowOfflineTxForUnknownId"
    authorization_cache_enabled = "AuthorizationCacheEnabled"
    authorize_remote_tx_requests = "AuthorizeRemoteTxRequests"
    blink_repeat = "BlinkRepeat"
    clock_aligned_data_interval = "ClockAlignedDataInterval"
    connection_time_out = "ConnectionTimeOut"
    connector_phase_rotation = "ConnectorPhaseRotation"
    connector_phase_rotation_max_length = "ConnectorPhaseRotationMaxLength"
    get_configuration_max_keys = "GetConfigurationMaxKeys"
    heartbeat_interval = "HeartbeatInterval"
    light_intensity = "LightIntensity"
    local_authorize_offline = "LocalAuthorizeOffline"
    local_pre_authorize = "LocalPreAuthorize"
    max_energy_on_invalid_id = "MaxEnergyOnInvalidId"
    meter_values_aligned_data = "MeterValuesAlignedData"
    meter_values_aligned_data_max_length = "MeterValuesAlignedDataMaxLength"
    meter_values_sampled_data = "MeterValuesSampledData"
    meter_values_sampled_data_max_length = "MeterValuesSampledDataMaxLength"
    meter_value_sample_interval = "MeterValueSampleInterval"
    minimum_status_duration = "MinimumStatusDuration"
    number_of_connectors = "NumberOfConnectors"
    reset_retries = "ResetRetries"
    stop_transaction_on_ev_side_disconnect = "StopTransactionOnEVSideDisconnect"
    stop_transaction_on_invalid_id = "StopTransactionOnInvalidId"
    stop_txn_aligned_data = "StopTxnAlignedData"
    stop_txn_aligned_data_max_length = "StopTxnAlignedDataMaxLength"
    stop_txn_sampled_data = "StopTxnSampledData"
    stop_txn_sampled_data_max_length = "StopTxnSampledDataMaxLength"
    supported_feature_profiles = "SupportedFeatureProfiles"
    supported_feature_profiles_max_length = "SupportedFeatureProfilesMaxLength"
    transaction_message_attempts = "TransactionMessageAttempts"
    transaction_message_retry_interval = "TransactionMessageRetryInterval"
    unlock_connector_on_ev_side_disconnect = "UnlockConnectorOnEVSideDisconnect"
    web_socket_ping_interval = "WebSocketPingInterval"

    # 9.2 Local Auth List Management Profile
    local_auth_list_enabled = "LocalAuthListEnabled"
    local_auth_list_max_length = "LocalAuthListMaxLength"
    send_local_list_max_length = "SendLocalListMaxLength"

    # 9.3 Reservation Profile
    reserve_connector_zero_supported = "ReserveConnectorZeroSupported"

    # 9.4 Smart Charging Profile
    charge_profile_max_stack_level = "ChargeProfileMaxStackLevel"
    charging_schedule_allowed_charging_rate_unit = (
        "ChargingScheduleAllowedChargingRateUnit"
    )
    charging_schedule_max_periods = "ChargingScheduleMaxPeriods"
    connector_switch_3to1_phase_supported = "ConnectorSwitch3to1PhaseSupported"
    max_charging_profiles_installed = "MaxChargingProfilesInstalled"

    # OCPP 1.6 ISO 15118 v10 added configuration keys
    central_contract_validation_allowed = "CentralContractValidationAllowed"
    certificate_signed_max_chain_size = "CertificateSignedMaxChainSize"
    cert_signing_wait_minimum = "CertSigningWaitMinimum"
    cert_signing_repeat_times = "CertSigningRepeatTimes"
    certificate_store_max_length = "CertificateStoreMaxLength"
    contract_validation_offline = "ContractValidationOffline"
    iso_15118_pnc_enabled = "ISO15118PnCEnabled"

    # OCPP security whitepaper added configuration keys
    additional_root_certificate_check = "AdditionalRootCertificateCheck"
    authorization_key = "AuthorizationKey"
    cpo_name = "CpoName"
    security_profile = "SecurityProfile"


class DataTransferStatus(StrEnum):
    """
    Status in DataTransfer.conf.
    """

    accepted = "Accepted"
    rejected = "Rejected"
    unknown_message_id = "UnknownMessageId"
    unknown_vendor_id = "UnknownVendorId"


class DeleteCertificateStatus(StrEnum):
    """
    DeleteCertificateStatusEnumType is used by: DeleteCertificate.conf
    """

    accepted = "Accepted"
    failed = "Failed"
    not_found = "NotFound"


class DiagnosticsStatus(StrEnum):
    """
    Status in DiagnosticsStatusNotification.req.
    """

    idle = "Idle"
    uploaded = "Uploaded"
    upload_failed = "UploadFailed"
    uploading = "Uploading"


class FirmwareStatus(StrEnum):
    """
    Status of a firmware download as reported in FirmwareStatusNotification.req
    """

    # Common for:
    # FirmwareStatusNotification.req and SignedFirmwareStatusNotification.req
    downloaded = "Downloaded"
    download_failed = "DownloadFailed"
    downloading = "Downloading"
    idle = "Idle"
    installation_failed = "InstallationFailed"
    installing = "Installing"
    installed = "Installed"

    # Only for SignedFirmwareStatusNotification.reg
    download_scheduled = "DownloadScheduled"
    download_paused = "DownloadPaused"
    install_rebooting = "InstallRebooting"
    install_scheduled = "InstallScheduled"
    install_verification_failed = "InstallVerificationFailed"
    invalid_signature = "InvalidSignature"
    signature_verified = "SignatureVerified"


class GenericStatus(StrEnum):
    """
    Generic message response status
    """

    accepted = "Accepted"
    rejected = "Rejected"


class GetCompositeScheduleStatus(StrEnum):
    """
    Status returned in response to GetCompositeSchedule.req
    """

    accepted = "Accepted"
    rejected = "Rejected"


class GetInstalledCertificateStatus(StrEnum):
    """
    GetInstalledCertificateStatusEnumType is used by:
    GetInstalledCertificateIds.conf
    """

    accepted = "Accepted"
    not_found = "NotFound"


class HashAlgorithm(StrEnum):
    """
    HashAlgorithmEnumType is used by: CertificateHashDataType
    """

    sha256 = "SHA256"
    sha384 = "SHA384"
    sha512 = "SHA512"


class Location(StrEnum):
    """
    Allowable values of the optional "location" field of a value element in
    SampledValue.
    """

    inlet = "Inlet"
    outlet = "Outlet"
    body = "Body"
    cable = "Cable"
    ev = "EV"


class Log(StrEnum):
    """
    LogEnumType is used by GetLog.req
    """

    diagnostics_log = "DiagnosticsLog"
    security_log = "SecurityLog"


class LogStatus(StrEnum):
    """
    LogStatusEnumType is used by: GetLog.conf
    """

    accepted = "Accepted"
    rejected = "Rejected"
    accepted_canceled = "AcceptedCanceled"


class Measurand(StrEnum):
    """
    Allowable values of the optional "measurand" field of a Value element, as
    used in MeterValues.req and StopTransaction.req messages. Default value of
    "measurand" is always "Energy.Active.Import.Register"
    """

    current_export = "Current.Export"
    current_import = "Current.Import"
    current_offered = "Current.Offered"
    energy_active_export_register = "Energy.Active.Export.Register"
    energy_active_import_register = "Energy.Active.Import.Register"
    energy_reactive_export_register = "Energy.Reactive.Export.Register"
    energy_reactive_import_register = "Energy.Reactive.Import.Register"
    energy_active_export_interval = "Energy.Active.Export.Interval"
    energy_active_import_interval = "Energy.Active.Import.Interval"
    energy_reactive_export_interval = "Energy.Reactive.Export.Interval"
    energy_reactive_import_interval = "Energy.Reactive.Import.Interval"
    frequency = "Frequency"
    power_active_export = "Power.Active.Export"
    power_active_import = "Power.Active.Import"
    power_factor = "Power.Factor"
    power_offered = "Power.Offered"
    power_reactive_export = "Power.Reactive.Export"
    power_reactive_import = "Power.Reactive.Import"
    rpm = "RPM"
    soc = "SoC"
    temperature = "Temperature"
    voltage = "Voltage"


class MessageTrigger(StrEnum):
    """
    Type of request to be triggered in a TriggerMessage.req
    """

    # Common for TriggerMessage.req and ExtendedTriggerMessage.req
    boot_notification = "BootNotification"
    firmware_status_notification = "FirmwareStatusNotification"
    heartbeat = "Heartbeat"
    meter_values = "MeterValues"
    status_notification = "StatusNotification"

    # Only for TriggerMessage.req
    diagnostics_status_notification = "DiagnosticsStatusNotification"

    # Only for ExtendedTriggerMessage.req
    log_status_notification = "LogStatusNotification"
    sign_charge_point_certificate = "SignChargePointCertificate"


class Phase(StrEnum):
    """
    Phase as used in SampledValue. Phase specifies how a measured value is to
    be interpreted. Please note that not all values of Phase are applicable to
    all Measurands.
    """

    l1 = "L1"
    l2 = "L2"
    l3 = "L3"
    n = "N"
    l1_n = "L1-N"
    l2_n = "L2-N"
    l3_n = "L3-N"
    l1_l2 = "L1-L2"
    l2_l3 = "L2-L3"
    l3_l1 = "L3-L1"


class ReadingContext(StrEnum):
    """
    Values of the context field of a value in SampledValue.
    """

    interruption_begin = "Interruption.Begin"
    interruption_end = "Interruption.End"
    other = "Other"
    sample_clock = "Sample.Clock"
    sample_periodic = "Sample.Periodic"
    transaction_begin = "Transaction.Begin"
    transaction_end = "Transaction.End"
    trigger = "Trigger"


class Reason(StrEnum):
    """
    Reason for stopping a transaction in StopTransaction.req.
    """

    emergency_stop = "EmergencyStop"
    ev_disconnected = "EVDisconnected"
    hard_reset = "HardReset"
    local = "Local"
    other = "Other"
    power_loss = "PowerLoss"
    reboot = "Reboot"
    remote = "Remote"
    soft_reset = "SoftReset"
    unlock_command = "UnlockCommand"
    de_authorized = "DeAuthorized"


class RecurrencyKind(StrEnum):
    """
    "Daily": The schedule restarts at the beginning of the next day.
    "Weekly": The schedule restarts at the beginning of the next week
              (defined as Monday morning)
    """

    daily = "Daily"
    weekly = "Weekly"


class RegistrationStatus(StrEnum):
    """
    Result of registration in response to BootNotification.req.
    """

    accepted = "Accepted"
    pending = "Pending"
    rejected = "Rejected"


class RemoteStartStopStatus(StrEnum):
    """
    The result of a RemoteStartTransaction.req or RemoteStopTransaction.req
    request.
    """

    accepted = "Accepted"
    rejected = "Rejected"


class ReservationStatus(StrEnum):
    """
    Status in ReserveNow.conf.
    """

    accepted = "Accepted"
    faulted = "Faulted"
    occupied = "Occupied"
    rejected = "Rejected"
    unavailable = "Unavailable"


class ResetStatus(StrEnum):
    """
    Result of Reset.req
    """

    accepted = "Accepted"
    rejected = "Rejected"


class ResetType(StrEnum):
    """
    Type of reset requested by Reset.req
    """

    hard = "Hard"
    soft = "Soft"


class TriggerMessageStatus(StrEnum):
    """
    Status in TriggerMessage.conf.
    """

    accepted = "Accepted"
    rejected = "Rejected"
    not_implemented = "NotImplemented"


class UnitOfMeasure(StrEnum):
    """
    Allowable values of the optional "unit" field of a Value element, as used
    in MeterValues.req and StopTransaction.req messages. Default value of
    "unit" is always "Wh".
    """

    wh = "Wh"
    kwh = "kWh"
    varh = "varh"
    kvarh = "kvarh"
    w = "W"
    kw = "kW"
    va = "VA"
    kva = "kVA"
    var = "var"
    kvar = "kvar"
    a = "A"
    v = "V"
    celsius = "Celsius"
    fahrenheit = "Fahrenheit"
    k = "K"
    percent = "Percent"


class UnlockStatus(StrEnum):
    """
    Status in response to UnlockConnector.req.
    """

    unlocked = "Unlocked"
    unlock_failed = "UnlockFailed"
    not_supported = "NotSupported"


class UpdateFirmwareStatus(StrEnum):
    """
    UpdateFirmwareStatusEnumType is used by: SignedUpdateFirmware.conf
    """

    accepted = "Accepted"
    rejected = "Rejected"
    accepted_canceled = "AcceptedCanceled"
    invalid_certificate = "InvalidCertificate"
    revoked_certificate = "RevokedCertificate"


class UploadLogStatus(StrEnum):
    """
    UploadLogStatusEnumType is used by: LogStatusNotification.req
    """

    bad_message = "BadMessage"
    idle = "Idle"
    not_supported_operation = "NotSupportedOperation"
    permission_denied = "PermissionDenied"
    uploaded = "Uploaded"
    upload_failure = "UploadFailure"
    uploading = "Uploading"


class UpdateStatus(StrEnum):
    """
    Type of update for a SendLocalList.req.
    """

    accepted = "Accepted"
    failed = "Failed"
    not_supported = "NotSupported"
    version_mismatch = "VersionMismatch"


class UpdateType(StrEnum):
    """
    Type of update for a SendLocalList.req.
    """

    differential = "Differential"
    full = "Full"


class ValueFormat(StrEnum):
    """
    Format that specifies how the value element in SampledValue is to be
    interpreted.
    """

    raw = "Raw"
    signed_data = "SignedData"
