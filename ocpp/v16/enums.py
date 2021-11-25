from enum import Enum


class Action(str, Enum):
    """ An Action is a required part of a Call message. """
    Authorize = "Authorize"
    BootNotification = "BootNotification"
    CancelReservation = "CancelReservation"
    CertificateSigned = "CertificateSigned"
    ChangeAvailability = "ChangeAvailability"
    ChangeConfiguration = "ChangeConfiguration"
    ClearCache = "ClearCache"
    ClearChargingProfile = "ClearChargingProfile"
    DataTransfer = "DataTransfer"
    DeleteCertificate = "DeleteCertificate"
    DiagnosticsStatusNotification = "DiagnosticsStatusNotification"
    ExtendedTriggerMessage = "ExtendedTriggerMessage"
    FirmwareStatusNotification = "FirmwareStatusNotification"
    GetCompositeSchedule = "GetCompositeSchedule"
    GetConfiguration = "GetConfiguration"
    GetDiagnostics = "GetDiagnostics"
    GetInstalledCertificateIds = "GetInstalledCertificateIds"
    GetLocalListVersion = "GetLocalListVersion"
    GetLog = "GetLog"
    Heartbeat = "Heartbeat"
    InstallCertificate = "InstallCertificate"
    LogStatusNotification = "LogStatusNotification"
    MeterValues = "MeterValues"
    RemoteStartTransaction = "RemoteStartTransaction"
    RemoteStopTransaction = "RemoteStopTransaction"
    ReserveNow = "ReserveNow"
    Reset = "Reset"
    SecurityEventNotification = "SecurityEventNotification"
    SendLocalList = "SendLocalList"
    SetChargingProfile = "SetChargingProfile"
    SignCertificate = "SignCertificate"
    SignedFirmwareStatusNotification = "SignedFirmwareStatusNotification"
    SignedUpdateFirmware = "SignedUpdateFirmware"
    StartTransaction = "StartTransaction"
    StatusNotification = "StatusNotification"
    StopTransaction = "StopTransaction"
    TriggerMessage = "TriggerMessage"
    UnlockConnector = "UnlockConnector"
    UpdateFirmware = "UpdateFirmware"


class AuthorizationStatus(str, Enum):
    """
    Elements that constitute an entry of a Local Authorization List update.
    """

    accepted = "Accepted"
    blocked = "Blocked"
    expired = "Expired"
    invalid = "Invalid"
    concurrent_tx = "ConcurrentTx"


class AvailabilityStatus(str, Enum):
    """
    Status returned in response to ChangeAvailability.req.
    """

    accepted = "Accepted"
    rejected = "Rejected"
    scheduled = "Scheduled"


class AvailabilityType(str, Enum):
    """
    Requested availability change in ChangeAvailability.req.
    """

    inoperative = "Inoperative"
    operative = "Operative"


class CancelReservationStatus(str, Enum):
    """
    Status in CancelReservation.conf.
    """

    accepted = "Accepted"
    rejected = "Rejected"


class CertificateSignedStatus(str, Enum):
    """
    CertificateSignedStatusEnumType is used by: CertificateSigned.conf
    """

    accepted = "Accepted"
    rejected = "Rejected"


class CertificateStatus(str, Enum):
    """
    CertificateStatusEnumType is used by: InstallCertificate.conf
    """

    accepted = "Accepted"
    rejected = "Rejected"
    failed = "Failed"


class CertificateUse(str, Enum):
    """
    CertificateUseEnumType is used by: GetInstalledCertificateIds.req,
    InstallCertificate.req
    """

    central_system_root_certificate = "CentralSystemRootCertificate"
    manufacturer_root_certificate = "ManufacturerRootCertificate"


class ChargePointErrorCode(str, Enum):
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

    # Soon to be deprecated enums
    connectorLockFailure = "ConnectorLockFailure"
    evCommunicationError = "EVCommunicationError"
    groundFailure = "GroundFailure"
    highTemperature = "HighTemperature"
    internalError = "InternalError"
    localListConflict = "LocalListConflict"
    noError = "NoError"
    otherError = "OtherError"
    overCurrentFailure = "OverCurrentFailure"
    overVoltage = "OverVoltage"
    powerMeterFailure = "PowerMeterFailure"
    powerSwitchFailure = "PowerSwitchFailure"
    readerFailure = "ReaderFailure"
    resetFailure = "ResetFailure"
    underVoltage = "UnderVoltage"
    weakSignal = "WeakSignal"


class ChargePointStatus(str, Enum):
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

    # Soon to be deprecated enums
    suspendedevse = "SuspendedEVSE"
    suspendedev = "SuspendedEV"


class ChargingProfileKindType(str, Enum):
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


class ChargingProfilePurposeType(str, Enum):
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

    # Soon to be deprecated enums
    chargepointmaxprofile = "ChargePointMaxProfile"
    txdefaultprofile = "TxDefaultProfile"
    txprofile = "TxProfile"


class ChargingProfileStatus(str, Enum):
    """
    Status returned in response to SetChargingProfile.req.
    """

    accepted = "Accepted"
    rejected = "Rejected"
    not_supported = "NotSupported"
    # Soon to be deprecated enums
    notSupported = "NotSupported"


class ChargingRateUnitType(str, Enum):
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


class ClearCacheStatus(str, Enum):
    """
    Status returned in response to ClearCache.req.
    """

    accepted = "Accepted"
    rejected = "Rejected"


class ClearChargingProfileStatus(str, Enum):
    """
    Status returned in response to ClearChargingProfile.req.
    """

    accepted = "Accepted"
    unknown = "Unknown"


class ConfigurationStatus(str, Enum):
    """
    Status in ChangeConfiguration.conf.
    """

    accepted = "Accepted"
    rejected = "Rejected"
    reboot_required = "RebootRequired"
    not_supported = "NotSupported"

    # Soon to be deprecated enums
    rebootRequired = "RebootRequired"
    notSupported = "NotSupported"


class DataTransferStatus(str, Enum):
    """
    Status in DataTransfer.conf.
    """
    accepted = "Accepted"
    rejected = "Rejected"
    unknown_message_id = "UnknownMessageId"
    unknown_vendor_id = "UnknownVendorId"

    # Soon to be deprecated enums
    unknownMessageId = "UnknownMessageId"
    unknownVendorId = "UnknownVendorId"


class DeleteCertificateStatus(str, Enum):
    """
    DeleteCertificateStatusEnumType is used by: DeleteCertificate.conf
    """

    accepted = "Accepted"
    failed = "Failed"
    not_found = "NotFound"


class DiagnosticsStatus(str, Enum):
    """
    Status in DiagnosticsStatusNotification.req.
    """

    idle = "Idle"
    uploaded = "Uploaded"
    upload_failed = "UploadFailed"
    uploading = "Uploading"

    # Soon to be deprecated enums
    uploadFailed = "UploadFailed"


class FirmwareStatus(str, Enum):
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

    # Soon to be deprecated enums
    downloadFailed = "DownloadFailed"
    installationFailed = "InstallationFailed"


class GenericStatus(str, Enum):
    """
    Generic message response status
    """

    accepted = "Accepted"
    rejected = "Rejected"


class GetCompositeScheduleStatus(str, Enum):
    """
    Status returned in response to GetCompositeSchedule.req
    """

    accepted = "Accepted"
    rejected = "Rejected"


class GetInstalledCertificateStatus(str, Enum):
    """
    GetInstalledCertificateStatusEnumType is used by:
    GetInstalledCertificateIds.conf
    """

    accepted = "Accepted"
    not_found = "NotFound"


class HashAlgorithm(str, Enum):
    """
    HashAlgorithmEnumType is used by: CertificateHashDataType
    """

    sha256 = "SHA256"
    sha384 = "SHA384"
    sha512 = "SHA512"


class Location(str, Enum):
    """
    Allowable values of the optional "location" field of a value element in
    SampledValue.
    """

    inlet = "Inlet"
    outlet = "Outlet"
    body = "Body"
    cable = "Cable"
    ev = "EV"


class Log(str, Enum):
    """
    LogEnumType is used by GetLog.req
    """

    diagnostics_log = "DiagnosticsLog"
    security_log = "SecurityLog"


class LogStatus(str, Enum):
    """
    LogStatusEnumType is used by: GetLog.conf
    """

    accepted = "Accepted"
    rejected = "Rejected"
    accepted_canceled = "AcceptedCanceled"


class Measurand(str, Enum):
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

    # Soon to be deprecated enums
    currentExport = "Current.Export"
    currentImport = "Current.Import"
    currentOffered = "Current.Offered"
    energyActiveExportRegister = "Energy.Active.Export.Register"
    energyActiveImportRegister = "Energy.Active.Import.Register"
    energyReactiveExportRegister = "Energy.Reactive.Export.Register"
    energyReactiveImportRegister = "Energy.Reactive.Import.Register"
    energyActiveExportInterval = "Energy.Active.Export.Interval"
    energyActiveImportInterval = "Energy.Active.Import.Interval"
    energyReactiveExportInterval = "Energy.Reactive.Export.Interval"
    energyReactiveImportInterval = "Energy.Reactive.Import.Interval"
    powerActiveExport = "Power.Active.Export"
    powerActiveImport = "Power.Active.Import"
    powerFactor = "Power.Factor"
    powerOffered = "Power.Offered"
    powerReactiveExport = "Power.Reactive.Export"
    powerReactiveImport = "Power.Reactive.Import"


class MessageTrigger(str, Enum):
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

    # Soon to be deprecated enums
    bootNotification = "BootNotification"
    diagnosticsStatusNotification = "DiagnosticsStatusNotification"
    firmwareStatusNotification = "FirmwareStatusNotification"
    meterValues = "MeterValues"
    statusNotification = "StatusNotification"


class Phase(str, Enum):
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

    # Soon to be deprecated enums
    l1n = "L1-N"
    l2n = "L2-N"
    l3n = "L3-N"
    l1l2 = "L1-L2"
    l2l3 = "L2-L3"
    l3l1 = "L3-L1"


class ReadingContext(str, Enum):
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

    # Soon to be deprecated enums
    interruptionBegin = "Interruption.Begin"
    interruptionEnd = "Interruption.End"
    sampleClock = "Sample.Clock"
    samplePeriodic = "Sample.Periodic"
    transactionBegin = "Transaction.Begin"
    transactionEnd = "Transaction.End"


class Reason(str, Enum):
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

    # Soon to be deprecated enums
    emergencyStop = "EmergencyStop"
    evDisconnected = "EVDisconnected"
    hardReset = "HardReset"
    powerLoss = "PowerLoss"
    softReset = "SoftReset"
    unlockCommand = "UnlockCommand"
    deAuthorized = "DeAuthorized"


class RecurrencyKind(str, Enum):
    """
    "Daily": The schedule restarts at the beginning of the next day.
    "Weekly": The schedule restarts at the beginning of the next week
              (defined as Monday morning)
    """

    daily = "Daily"
    weekly = "Weekly"


class RegistrationStatus(str, Enum):
    """
    Result of registration in response to BootNotification.req.
    """

    accepted = "Accepted"
    pending = "Pending"
    rejected = "Rejected"


class RemoteStartStopStatus(str, Enum):
    """
    The result of a RemoteStartTransaction.req or RemoteStopTransaction.req
    request.
    """

    accepted = "Accepted"
    rejected = "Rejected"


class ReservationStatus(str, Enum):
    """
    Status in ReserveNow.conf.
    """

    accepted = "Accepted"
    faulted = "Faulted"
    occupied = "Occupied"
    rejected = "Rejected"
    unavailable = "Unavailable"


class ResetStatus(str, Enum):
    """
    Result of Reset.req
    """

    accepted = "Accepted"
    rejected = "Rejected"


class ResetType(str, Enum):
    """
    Type of reset requested by Reset.req
    """

    hard = "Hard"
    soft = "Soft"


class TriggerMessageStatus(str, Enum):
    """
    Status in TriggerMessage.conf.
    """

    accepted = "Accepted"
    rejected = "Rejected"
    not_implemented = "NotImplemented"

    # Soon to be deprecated enums
    notImplemented = "NotImplemented"


class UnitOfMeasure(str, Enum):
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
    hertz = "Hertz"


class UnlockStatus(str, Enum):
    """
    Status in response to UnlockConnector.req.
    """

    unlocked = "Unlocked"
    unlock_failed = "UnlockFailed"
    not_supported = "NotSupported"

    # Soon to be deprecated enums
    unlockFailed = "UnlockFailed"
    notSupported = "NotSupported"


class UpdateFirmwareStatus(str, Enum):
    """
    UpdateFirmwareStatusEnumType is used by: SignedUpdateFirmware.conf
    """

    accepted = "Accepted"
    rejected = "Rejected"
    accepted_canceled = "AcceptedCanceled"
    invalid_certificate = "InvalidCertificate"
    revoked_certificate = "RevokedCertificate"


class UploadLogStatus(str, Enum):
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


class UpdateStatus(str, Enum):
    """
    Type of update for a SendLocalList.req.
    """

    accepted = "Accepted"
    failed = "Failed"
    not_supported = "NotSupported"
    version_mismatch = "VersionMismatch"

    # Soon to be deprecated enums
    notSupported = "NotSupported"
    versionMismatch = "VersionMismatch"


class UpdateType(str, Enum):
    """
    Type of update for a SendLocalList.req.
    """

    differential = "Differential"
    full = "Full"


class ValueFormat(str, Enum):
    """
    Format that specifies how the value element in SampledValue is to be
    interpreted.
    """

    raw = "Raw"
    signed_data = "SignedData"

    # Soon to be deprecated enums
    signedData = "SignedData"
