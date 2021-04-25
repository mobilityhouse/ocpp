from enum import Enum


class Action:
    """ An Action is a required part of a Call message. """
    Authorize = "Authorize"
    BootNotification = "BootNotification"
    CancelReservation = "CancelReservation"
    ChangeAvailability = "ChangeAvailability"
    ChangeConfiguration = "ChangeConfiguration"
    ClearCache = "ClearCache"
    ClearChargingProfile = "ClearChargingProfile"
    DataTransfer = "DataTransfer"
    DiagnosticStatusNotification = "DiagnosticStatusNotification"
    FirmwareStatusNotification = "FirmwareStatusNotification"
    GetCompositeSchedule = "GetCompositeSchedule"
    GetConfiguration = "GetConfiguration"
    ClearChargingProfile = "ClearChargingProfile"
    GetDiagnostics = "GetDiagnostics"
    GetLocalListVersion = "GetLocalListVersion"
    Heartbeat = "Heartbeat"
    MeterValues = "MeterValues"
    RemoteStartTransaction = "RemoteStartTransaction"
    RemoteStopTransacton = "RemoteStopTransaction"
    ReserveNow = "ReserveNow"
    Reset = "Reset"
    SendLocalList = "SendLocalList"
    SetChargingProfile = "SetChargingProfile"
    StartTransaction = "StartTransaction"
    StatusNotification = "StatusNotification"
    StopTransaction = "StopTransaction"
    TransactionEvent = "TransactionEvent"
    TriggerMessage = "TriggerMessage"
    UnlockConnector = "UnlockConnector"
    UpdateFirmware = "UpdateFirmware"
    LogStatusNotification = "LogStatusNotification"
    NotifyChargingLimit = "NotifyChargingLimit"
    ClearedChargingLimit = "ClearedChargingLimit"
    NotifyEVChargingNeeds = "NotifyEVChargingNeeds"
    NotifyEVChargingSchedule = "NotifyEVChargingSchedule"
    FirmwareStatusNotification = "FirmwareStatusNotification"
    Update15118EVCertificate = "Update15118EVCertificate"
    Get15118EVCertificate = "Get15118EVCertificate"


class MessageType:
    Call = 2
    CallResult = 3
    CallError = 4


class NotifyEVChargingNeedsStatusEnumType(Enum):
    """
    Accepted: a SASchedule will be provided momentarily.
    Rejected: Servoce is Not Available
    Processing: The CSMS is gathering information to provide an SASchedule.
    """
    accepted = "Accepted"
    rejected = "Rejected"
    processing = "Processing"


class GenericStatusEnumType(Enum):
    accepted = "Accepted"
    rejected = "Rejected"


class LogEnumType(Enum):
    diagnosticsLog = "DiagnosticsLog"
    securityLog = "SecurityLog"


class AttributeType(Enum):
    actual = "Actual"
    target = "Target"
    min_set = "MinSet"
    max_set = "MaxSet"


class AuthorizationStatusEnumType(Enum):
    """
    Elements that constitute an entry of a Local Authorization List update.
    """

    accepted = "Accepted"
    blocked = "Blocked"
    expired = "Expired"
    invalid = "Invalid"
    concurrenttx = "ConcurrentTx"
    # Identifier is valid, but EV Driver doesn’t have enough credit to start
    # charging. Not allowed for charging.
    no_credit = "NoCredit"
    # Identifier is valid, but not allowed to charge in this type of EVSE.
    not_allowed_type_evse = "NotAllowedTypeEVSE"


class AvailabilityStatus(Enum):
    """
    Status returned in response to ChangeAvailability.req.
    """

    accepted = "Accepted"
    rejected = "Rejected"
    scheduled = "Scheduled"


class AvailabilityType(Enum):
    """
    Requested availability change in ChangeAvailability.req.
    """

    inoperative = "Inoperative"
    operative = "Operative"


class CancelReservationStatus(Enum):
    """
    Status in CancelReservation.conf.
    """

    accepted = "Accepted"
    rejected = "Rejected"


class ChargePointErrorCode(Enum):
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


class ConnectorStatus(Enum):
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


class ChargingProfileKindType(Enum):
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


class ChargingProfilePurposeType(Enum):
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

    chargepointmaxprofile = "ChargingStationMaxProfile"
    txdefaultprofile = "TxDefaultProfile"
    txprofile = "TxProfile"
    csexternalconstraints = "ChargingStationExternalConstraints"


class ChargingProfileStatus(Enum):
    """
    Status returned in response to SetChargingProfile.req.
    """

    accepted = "Accepted"
    rejected = "Rejected"
    notSupported = "NotSupported"


class ChargingRateUnitType(Enum):
    """
    Unit in which a charging schedule is defined, as used in:
    GetCompositeSchedule.req and ChargingSchedule
    """

    watts = "W"
    amps = "A"


class ClearCacheStatus(Enum):
    """
    Status returned in response to ClearCache.req.
    """

    accepted = "Accepted"
    rejected = "Rejected"


class ClearChargingProfileStatus(Enum):
    """
    Status returned in response to ClearChargingProfile.req.
    """

    accepted = "Accepted"
    unknown = "Unknown"


class ConfigurationStatus(Enum):
    """
    Status in ChangeConfiguration.conf.
    """

    accepted = "Accepted"
    rejected = "Rejected"
    rebootRequired = "RebootRequired"
    notSupported = "NotSupported"


class DataTransferStatus(Enum):
    """
    Status in DataTransfer.conf.
    """
    accepted = "Accepted"
    rejected = "Rejected"
    unknownMessageId = "UnknownMessageId"
    unknownVendorId = "UnknownVendorId"


class DiagnosticsStatus(Enum):
    """
    Status in DiagnosticsStatusNotification.req.
    """

    idle = "Idle"
    uploaded = "Uploaded"
    uploadFailed = "UploadFailed"
    uploading = "Uploading"


class FirmwareStatus(Enum):
    """
    Status of a firmware download as reported in FirmwareStatusNotification.req
    """

    downloaded = "Downloaded"
    downloadFailed = "DownloadFailed"
    downloading = "Downloading"
    idle = "Idle"
    installationFailed = "InstallationFailed"
    installing = "Installing"
    installed = "Installed"


class GetCompositeScheduleStatus(Enum):
    """
    Status returned in response to GetCompositeSchedule.req
    """

    accepted = "Accepted"
    rejected = "Rejected"


class Location(Enum):
    """
    Allowable values of the optional "location" field of a value element in
    SampledValue.
    """

    inlet = "Inlet"
    outlet = "Outlet"
    body = "Body"
    cable = "Cable"
    ev = "EV"


class Measurand(Enum):
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
    frequency = "Frequency"
    powerActiveExport = "Power.Active.Export"
    powerActiveImport = "Power.Active.Import"
    powerFactor = "Power.Factor"
    powerOffered = "Power.Offered"
    powerReactiveExport = "Power.Reactive.Export"
    powerReactiveImport = "Power.Reactive.Import"
    rpm = "RPM"
    soc = "SoC"
    temperature = "Temperature"
    voltage = "Voltage"


class MessageTriggerEnumType(Enum):
    """
    Type of request to be triggered in a TriggerMessage.req
    """

    bootNotification = "BootNotification"
    logStatusNotification = "LogStatusNotification"
    firmwareStatusNotification = "FirmwareStatusNotification"
    heartbeat = "Heartbeat"
    meterValues = "MeterValues"
    statusNotification = "StatusNotification"
    transactionEvent = "TransactionEvent"
    # Triggers a SignCertificate with typeOfCertificate:
    # ChargingStationCertificate.
    signChargingStationCertificate = "SignChargingStationCertificate"
    # Triggers a SignCertificate with typeOfCertificate: V2GCertificate
    signV2GCertificate = "SignV2GCertificate"


class Phase(Enum):
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


class ReadingContext(Enum):
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


class Reason(Enum):
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


class RecurrencyKind(Enum):
    """
    "Daily": The schedule restarts at the beginning of the next day.
    "Weekly": The schedule restarts at the beginning of the next week
              (defined as Monday morning)
    """

    daily = "Daily"
    weekly = "Weekly"


class RegistrationStatus(Enum):
    """
    Result of registration in response to BootNotification.req.
    """

    accepted = "Accepted"
    pending = "Pending"
    rejected = "Rejected"


class RemoteStartStopStatus(Enum):
    """
    The result of a RemoteStartTransaction.req or RemoteStopTransaction.req
    request.
    """
    accepted = "Accepted"
    rejected = "Rejected"


class ReservationStatus(Enum):
    """
    Status in ReserveNow.conf.
    """

    accepted = "Accepted"
    faulted = "Faulted"
    occupied = "Occupied"
    rejected = "Rejected"
    unavailable = "Unavailable"


class ResetStatus(Enum):
    """
    Result of Reset.req
    """

    accepted = "Accepted"
    rejected = "Rejected"


class ResetType(Enum):
    """
    Type of reset requested by Reset.req
    """

    hard = "Hard"
    soft = "Soft"


class TriggerMessageStatus(Enum):
    """
    Status in TriggerMessage.conf.
    """

    accepted = "Accepted"
    rejected = "Rejected"
    notImplemented = "NotImplemented"


class UnitOfMeasure(Enum):
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


class UnlockStatus(Enum):
    """
    Status in response to UnlockConnector.req.
    """

    unlocked = "Unlocked"
    unlockFailed = "UnlockFailed"
    notSupported = "NotSupported"


class UpdateStatus(Enum):
    """
    Type of update for a SendLocalList.req.
    """

    accepted = "Accepted"
    failed = "Failed"
    notSupported = "NotSupported"
    versionMismatch = "VersionMismatch"


class UpdateType(Enum):
    """
    Type of update for a SendLocalList.req.
    """

    differential = "Differential"
    full = "Full"


class ValueFormat(Enum):
    """
    Format that specifies how the value element in SampledValue is to be
    interpreted.
    """

    raw = "Raw"
    signedData = "SignedData"


class _15118EVCertificateStatusEnumType(Enum):
    """
    Status of the processing of a 15118 Certificate and that if an exiResponse
    is included
    """
    accepted = "Accepted"
    failed = "Failed"
