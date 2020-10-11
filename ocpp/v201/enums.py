class Action:
    """ An Action is a required part of a Call message. """
    Authorize = "Authorize"
    BootNotification = "BootNotification"
    CancelReservation = "CancelReservation"
    CertifiedSigned = "CertifiedSigned"
    ChangeAvailability = "ChangeAvailability"
    ClearCache = "ClearCache"
    ClearChargingProfile = "ClearChargingProfile"
    ClearDisplayMessage = "ClearDisplayMessage"
    ClearedChargingLimi = "ClearedChargingLimit"
    ClearVariableMonitoring = "ClearVariableMonitoring"
    CostUpdate = "CostUpdate"
    CustomerInformation = "CustomerInformation"
    DataTransfer = "DataTransfer"
    DeleteCertificate = "DeleteCertificate"
    FirmwareStatusNotification = "FirmwareStatusNotification"
    Get15118EVCertificate = "Get15118EVCertificate"
    GetBaseReport = "GetBaseReport"
    GetCertificateStatus = "GetCertificateStatus"
    GetChargingProfiles = "GetChargingProfiles"
    GetCompositeSchedule = "GetCompositeSchedule"
    GetDisplayMessages = "GetDisplayMessages"
    GetInstalledCertificateIds = "GetInstalledCertificateIds"
    GetLocalListVersion = "GetLocalListVersion"
    GetLog = "GetLog"
    GetMonitoringReport = "GetMonitoringReport"
    GetReport = "GetReport"
    GetTransactionStatus = "GetTransactionStatus"
    GetVariables = "GetVariables"
    Heartbeat = "Heartbeat"
    InstallCertificate = "InstallCertificate"
    LogStatusNotification = "LogStatusNotification"
    MeterValues = "MeterValues"
    NotifyChargingLimit = "NotifyChargingLimit"
    NotifyCustomerInformation = "NotifyCustomerInformation"
    NotifyDisplayMessages = "NotifyDisplayMessages"
    NotifyEVChargingNeeds = "NotifyEVChargingNeeds"
    NotifyEVChargingSchedule = "NotifyEVChargingSchedule"
    NotiyEvent = "NotiyEvent"
    NotifyMonitoringReport = "NotifyMonitoringReport"
    NotifyReport = "NotifyReport"
    PublishFirmware = "PublishFirmware"
    PublishFirmwareStatusNotification = "PublishFirmwareStatusNotification"
    ReportChargingProfiles = "ReportChargingProfiles"
    RequestStartTransaction = "RequestStartTransaction"
    RequestStopTransaction = "RequestStopTransaction"
    ReservationStatusUpdate = "ReservationStatusUpdate"
    ReserveNow = "ReserveNow"
    Reset = "Reset"
    SecurityEventNotification = "SecurityEventNotification"
    SendLocalList = "SendLocalList"
    SetChargingProfile = "SetChargingProfile"
    SetDisplayMessage = "SetDisplayMessage"
    SetMonitoringBase = "SetMonitorBase"
    SetMonitoringLevel = "SetMonitoringLevel"
    SetNetworkProfile = "SetNetworkProfile"
    SetVariableMonitoring = "SetVariableMonitoring"
    SetVariables = "SetVariables"
    SignCertificate = "SignCertificate"
    StatusNotification = "StatusNotification"
    TransactionEvent = "TransactionEvent"
    TriggerMessage = "TriggerMessage"
    UnlockConnector = "UnlockConnector"
    UnpublishFirmware = "UnpublishFirmware"
    UpdateFirmware = "UpdateFirmware"

class MessageType:
    Call = 2
    CallResult = 3
    CallError = 4


class NotifyEVChargingNeedsStatusType():
    """
    Accepted: a SASchedule will be provided momentarily.
    Rejected: Servoce is Not Available
    Processing: The CSMS is gathering information to provide an SASchedule.
    """
    accepted = "Accepted"
    rejected = "Rejected"
    processing = "Processing"


class GenericStatusType():
    accepted = "Accepted"
    rejected = "Rejected"


class LogType():
    diagnosticsLog = "DiagnosticsLog"
    securityLog = "SecurityLog"


class AttributeType():
    actual = "Actual"
    target = "Target"
    min_set = "MinSet"
    max_set = "MaxSet"


class AuthorizationStatusType():
    """
    Elements that constitute an entry of a Local Authorization List update.
    """

    accepted = "Accepted"
    blocked = "Blocked"
    concurrenttx = "ConcurrentTx"
    expired = "Expired"
    invalid = "Invalid"
    # Identifier is valid, but EV Driver doesn’t have enough credit to start
    # charging. Not allowed for charging.
    no_credit = "NoCredit"
    # Identifier is valid, but not allowed to charge in this type of EVSE.
    not_allowed_type_evse = "NotAllowedTypeEVSE"
    not_at_this_location = "NotAtThisLocation"
    not_at_this_time = "NotAtThisTime"
    Unknown = "Unknown"


class ChangeAvailabilityStatusType():
    """
    Status returned in response to ChangeAvailability.req.
    """

    accepted = "Accepted"
    rejected = "Rejected"
    scheduled = "Scheduled"


class OperationalStatusEnumType():
    """
    Requested availability change in ChangeAvailability.req.
    """

    inoperative = "Inoperative"
    operative = "Operative"


class ChargePointErrorCode():
    """
    Charge Point status reported in StatusNotification.req.
    """

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


class ConnectorStatus():
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
    occupied = "Occupied"
    reserved = "Reserved"
    unavailable = "Unavailable"
    faulted = "Faulted"


class ChargingProfileKindType():
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


class ChargingProfilePurposeType():
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
    csmaxprofile = "ChargingStationMaxProfile"
    txdefaultprofile = "TxDefaultProfile"
    txprofile = "TxProfile"
    csexternalconstraints = "ChargingStationExternalConstraints"


class ChargingProfileStatus():
    """
    Status returned in response to SetChargingProfile.req.
    """

    accepted = "Accepted"
    rejected = "Rejected"


class ChargingRateUnitType():
    """
    Unit in which a charging schedule is defined, as used in:
    GetCompositeSchedule.req and ChargingSchedule
    """

    watts = "W"
    amps = "A"


class ClearCacheStatusType():
    """
    Status returned in response to ClearCache.req.
    """

    accepted = "Accepted"
    rejected = "Rejected"


class ClearChargingProfileStatusType():
    """
    Status returned in response to ClearChargingProfile.req.
    """

    accepted = "Accepted"
    unknown = "Unknown"

class ClearMessageStatusType():
    """
    Status returned in response to ClearDisplayMessageRequest.
    """

    accepted = "Accepted"
    unknown = "Unknown"


class SetVariableStatusType():
    """
    Status in ChangeConfiguration.conf.
    """

    accepted = "Accepted"
    rejected = "Rejected"
    unknownComponent = "UnknownComponent"
    unknownVariable = "UnknownVariable"
    notSupportedAttributeType = "NotSupportedAttributeType"
    rebootRequired = "RebootRequired"


class DataTransferStatus():
    """
    Status in DataTransfer.conf.
    """
    accepted = "Accepted"
    rejected = "Rejected"
    unknownMessageId = "UnknownMessageId"
    unknownVendorId = "UnknownVendorId"


class UploadLogStatusType():
    """
    Status in LogStatusNotificationRequest.
    """
    badMessage = "BadMessage"
    idle = "Idle"
    notSupportedOperation = "NotSupportedOperation"
    permissionDenied = "PermissionDenied"
    uploaded = "Uploaded"
    uploadFailure = "UploadFailure"
    uploading = "Uploading"
    acceptedCanceled = "AcceptedCanceled"


class FirmwareStatusType():
    """
    Status of a firmware download as reported in FirmwareStatusNotification.req
    """

    downloaded = "Downloaded"
    downloadFailed = "DownloadFailed"
    downloading = "Downloading"
    downloadingScheduled = "DownloadingScheduled"
    downloadPaused = "DownloadPaused"
    idle = "Idle"
    installationFailed = "InstallationFailed"
    installing = "Installing"
    installed = "Installed"
    installRebooting = "InstallRebooting"
    installScheduled = "InstallScheduled"
    installVerificationFailed = "InstallVerificationFailed"
    invalidSignature = "InvalidSignature"
    signatureVerified = "SignatureVerified"


class LocationType():
    """
    Allowable values of the optional "location" field of a value element in
    SampledValue.
    """

    inlet = "Inlet"
    outlet = "Outlet"
    body = "Body"
    cable = "Cable"
    ev = "EV"


class MeasurandType():
    """
    Allowable values of the optional "measurand" field of a Value element, as
    used in MeterValues.req and StopTransaction.req messages. Default value of
    "measurand" is always "Energy.Active.Import.Register"
    """

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
    energyActiveNet = "Energy.Active.Net"
    energyReactiveNet = "Energy.Reactive.Net"
    energyApparentNet = "Energy.Apparent.Net"
    energyApparentImport = "Energy.Apparent.Import"
    energyApparentExport = "Energy.Apparent.Export"
    frequency = "Frequency"
    powerActiveExport = "Power.Active.Export"
    powerActiveImport = "Power.Active.Import"
    powerFactor = "Power.Factor"
    powerOffered = "Power.Offered"
    powerReactiveExport = "Power.Reactive.Export"
    powerReactiveImport = "Power.Reactive.Import"
    soc = "SoC"
    voltage = "Voltage"


class MessageTriggerType():
    """
    Type of request to be triggered in a TriggerMessage.req
    """

    bootNotification = "BootNotification"
    logStatusNotification = "LogStatusNotification"
    firmwareStatusNotification = "FirmwareStatusNotification"
    heartbeat = "Heartbeat"
    meterValues = "MeterValues"
    # Triggers a SignCertificate with typeOfCertificate:
    # ChargingStationCertificate.
    signChargingStationCertificate = "SignChargingStationCertificate"
    # Triggers a SignCertificate with typeOfCertificate: V2GCertificate
    signV2GCertificate = "SignV2GCertificate"
    statusNotification = "StatusNotification"
    transactionEvent = "TransactionEvent"
    signCombinedCertificate = "SignCombinedCertificate"
    publishFirmwareStatusNotification = "PublishFirmwareStatusNotification"


class PhaseType():
    """
    Phase as used in SampledValue. Phase specifies how a measured value is to
    be interpreted. Please note that not all values of Phase are applicable to
    all Measurands.
    """

    l1 = "L1"
    l2 = "L2"
    l3 = "L3"
    n = "N"
    l1n = "L1-N"
    l2n = "L2-N"
    l3n = "L3-N"
    l1l2 = "L1-L2"
    l2l3 = "L2-L3"
    l3l1 = "L3-L1"


class ReadingContextType():
    """
    Values of the context field of a value in SampledValue.
    """

    interruptionBegin = "Interruption.Begin"
    interruptionEnd = "Interruption.End"
    other = "Other"
    sampleClock = "Sample.Clock"
    samplePeriodic = "Sample.Periodic"
    transactionBegin = "Transaction.Begin"
    transactionEnd = "Transaction.End"
    trigger = "Trigger"


# TODO: Verify
class ReasonType():
    """
    Reason for stopping a transaction in StopTransaction.req.
    """

    emergencyStop = "EmergencyStop"
    evDisconnected = "EVDisconnected"
    hardReset = "HardReset"
    local = "Local"
    other = "Other"
    powerLoss = "PowerLoss"
    reboot = "Reboot"
    remote = "Remote"
    softReset = "SoftReset"
    unlockCommand = "UnlockCommand"
    deAuthorized = "DeAuthorized"


class RecurrencyKindType():
    """
    "Daily": The schedule restarts at the beginning of the next day.
    "Weekly": The schedule restarts at the beginning of the next week
              (defined as Monday morning)
    """

    daily = "Daily"
    weekly = "Weekly"


class RegistrationStatusType():
    """
    Result of registration in response to BootNotification.req.
    """

    accepted = "Accepted"
    pending = "Pending"
    rejected = "Rejected"


class RequestStartStopStatusType():
    """
    The result of a RemoteStartTransaction.req or RemoteStopTransaction.req
    request.
    """
    accepted = "Accepted"
    rejected = "Rejected"


class ReservationUpdateStatusType():
    expired = "Expired"
    removed = "Removed"


class ReserveNowStatusType():
    """
    Status in ReserveNow.conf.
    """

    accepted = "Accepted"
    faulted = "Faulted"
    occupied = "Occupied"
    rejected = "Rejected"
    unavailable = "Unavailable"


class ResetStatusType():
    """
    Result of Reset.req
    """

    accepted = "Accepted"
    rejected = "Rejected"
    scheduled = "Scheduled"


class ResetType():
    """
    Type of reset requested by Reset.req
    """

    immediate  = "Immediate"
    onIdle = "OnIdle"


class TriggerMessageStatusType():
    """
    Status in TriggerMessage.conf.
    """

    accepted = "Accepted"
    rejected = "Rejected"
    notImplemented = "NotImplemented"


class UnitOfMeasureType():
    """
    Allowable values of the optional "unit" field of a Value element, as used
    in MeterValues.req and StopTransaction.req messages. Default value of
    "unit" is always "Wh".
    """
    asu = "ASU"
    b = "Bytes"
    db = "dB"
    dbm = "dBm"
    deg = "Deg"
    hz = "Hz"
    lx = "lx"
    m = "m"
    ms2 = "ms2"
    n = "n"
    ohm = "ohm"
    kpa = "kPa"
    percent = "Percent"
    rh = "RH"
    rpm = "RPM"
    s = "s"
    va = "VA"
    kva = "kVA"
    vah = "VAh"
    kVAh = "kVAh"
    var = "var"
    kvar = "kvar"
    varh = "varh"
    kvarh = "kvarh"
    wh = "Wh"
    kwh = "kWh"
    w = "W"
    kw = "kW"
    a = "A"
    v = "V"
    celsius = "Celsius"
    fahrenheit = "Fahrenheit"
    k = "K"


class UnlockStatusType():
    """
    Status in response to UnlockConnector.req.
    """

    unlocked = "Unlocked"
    unlockFailed = "UnlockFailed"
    ongoingAuthorizedTransaction = "OngoingAuthorizedTransaction"
    unknownConnector = "UnknownConnector"


class SendLocalListStatusType():
    """
    Type of update for a SendLocalList Request.
    """

    accepted = "Accepted"
    failed = "Failed"
    notSupported = "NotSupported"
    versionMismatch = "VersionMismatch"


class UpdateType():
    """
    Type of update for a SendLocalList Request.
    """

    differential = "Differential"
    full = "Full"

