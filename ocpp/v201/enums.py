class Action:
    """ An Action is a required part of a Call message. """
    Authorize = "Authorize"
    BootNotification = "BootNotification"
    CancelReservation = "CancelReservation"
    CertificateSigned = "CertificateSigned"
    ChangeAvailability = "ChangeAvailability"
    ClearCache = "ClearCache"
    ClearChargingProfile = "ClearChargingProfile"
    ClearDisplayMessage = "ClearDisplayMessage"
    ClearedChargingLimit = "ClearedChargingLimit"
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
    NotifyEvent = "NotifyEvent"
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

# Enums


class APNAuthenticationType:
    """
    APNAuthenticationEnumType is used by:
    setNetworkProfile:SetNetworkProfileRequest.APNType
    """
    chap = "CHAP"
    none = "NONE"
    pap = "PAP"
    auto = "AUTO"


class AttributeType:
    """
    AttributeEnumType is used by: Common:VariableAttributeType ,
    getVariables:GetVariablesRequest.GetVariableDataType ,
    getVariables:GetVariablesResponse.GetVariableResultType ,
    setVariables:SetVariablesRequest.SetVariableDataType ,
    setVariables:SetVariablesResponse.SetVariableResultType
    """
    actual = "Actual"
    target = "Target"
    minSet = "MinSet"
    maxSet = "MaxSet"


class AuthorizationStatusType:
    """
    Elements that constitute an entry of a Local Authorization List update.
    """

    accepted = "Accepted"
    blocked = "Blocked"
    concurrentTx = "ConcurrentTx"
    expired = "Expired"
    invalid = "Invalid"
    # Identifier is valid, but EV Driver doesn’t have enough credit to start
    # charging. Not allowed for charging.
    noCredit = "NoCredit"
    # Identifier is valid, but not allowed to charge in this type of EVSE.
    notAllowedTypeEVSE = "NotAllowedTypeEVSE"
    notAtThisLocation = "NotAtThisLocation"
    notAtThisTime = "NotAtThisTime"
    Unknown = "Unknown"


class AuthorizeCertificateStatusType:
    """
    Status of the EV Contract certificate.
    """

    accepted = "Accepted"
    signatureError = "SignatureError"
    certificateExpired = "CertificateExpired"
    certificateRevoked = "CertificateRevoked"
    noCertificateAvailable = "NoCertificateAvailable"
    certChainError = "CertChainError"
    contractCancelled = "ContractCancelled"


class BootReasonType:
    """
    BootReasonEnumType is used by: bootNotification:BootNotificationRequest
    """

    ApplicationReset = "ApplicationReset"
    FirmwareUpdate = "FirmwareUpdate"
    LocalReset = "LocalReset"
    PowerUp = "PowerUp"
    RemoteReset = "RemoteReset"
    ScheduledReset = "ScheduledReset"
    Triggered = "Triggered"
    Unknown = "Unknown"
    Watchdog = "Watchdog"


class CancelReservationStatusType:
    """
    Status in CancelReservationResponse.
    """

    accepted = "Accepted"
    rejected = "Rejected"


class CertificateActionType:
    """
    CertificateActionEnumType is used by:
    get15118EVCertificate:Get15118EVCertificateRequest
    """
    install = "Install"
    update = "Update"


class CertificateActionType:
    """
    CertificateSigningUseEnumType is used by: signCertificate:
    SignCertificateRequest ,
    certificateSigned:CertificateSignedRequest
    """
    chargingStationCertificate = "ChargingStationCertificate"
    v2gCertificate = "V2GCertificate"


class ChangeAvailabilityStatusType:
    """
    Status returned in response to ChangeAvailability.req.
    """

    accepted = "Accepted"
    rejected = "Rejected"
    scheduled = "Scheduled"


class ChargingLimitSourceEnumType:
    """
    Enumeration for indicating from which source a charging limit originates.
    """

    ems = "EMS"
    other = "Other"
    so = "SO"
    cso = "CSO"


class ChargingProfileKindType:
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


class ChargingProfilePurposeType:
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
    discard it and return an error status in SetChargingProfileResponse.
    TxProfile SHALL only be set at Charge Point ConnectorId >0.

    It is not possible to set a ChargingProfile with purpose set to
    TxProfile without presence of an active transaction, or in advance of
    a transaction.

    In order to ensure that the updated charging profile applies only to the
    current transaction, the chargingProfilePurpose of the ChargingProfile
    MUST be set to TxProfile.
    """
    chargingStationMaxProfile = "ChargingStationMaxProfile"
    txDefaultProfile = "TxDefaultProfile"
    txProfile = "TxProfile"
    chargingStationExternalConstraints = "ChargingStationExternalConstraints"


class ChargingProfileStatus:
    """
    Status returned in response to SetChargingProfile.req.
    """

    accepted = "Accepted"
    rejected = "Rejected"


class ChargingRateUnitType:
    """
    Unit in which a charging schedule is defined, as used in:
    GetCompositeSchedule.req and ChargingSchedule
    """

    watts = "W"
    amps = "A"


class ChargingStateType:
    """
    The state of the charging process.
    """

    charging = "Charging"
    evConnected = "EVConnected"
    suspendedEV = "SuspendedEV"
    suspendedEVSE = "SuspendedEVSE"
    idle = "Idle"


class ClearCacheStatusType:
    """
    Status returned in response to ClearCache.req.
    """

    accepted = "Accepted"
    rejected = "Rejected"


class ClearChargingProfileStatusType:
    """
    Status returned in response to ClearChargingProfile.req.
    """

    accepted = "Accepted"
    unknown = "Unknown"


class ClearMessageStatusType:
    """
    Status returned in response to ClearDisplayMessageRequest.
    """

    accepted = "Accepted"
    unknown = "Unknown"


class ClearMonitoringStatusType:
    """
    ClearMonitoringStatusEnumType is used by: Common:ClearMonitoringResultType
    """

    accepted = "Accepted"
    rejected = "Rejected"
    notFound = "NotFound"


class ComponentCriterionType:
    """
    ComponentCriterionEnumType is used by: getReport:GetReportRequest
    """

    active = "Active"
    available = "Available"
    enabled = "Enabled"
    problem = "Problem"


class ConnectorType:
    """
    Allowed values of ConnectorCode.
    """
    # Combined Charging System 1 (captive cabled) a.k.a. Combo 1
    cCCS1 = "cCCS1"
    # Combined Charging System 2 (captive cabled) a.k.a. Combo 2
    cCCS2 = "cCCS2"
    # JARI G105-1993 (captive cabled) a.k.a. CHAdeMO
    cG105 = "cG105"
    # Tesla Connector (captive cabled)
    cTesla = "cTesla"
    # IEC62196-2 Type 1 connector (captive cabled) a.k.a. J1772
    cType1 = "cType1"
    # IEC62196-2 Type 2 connector (captive cabled) a.k.a. Mennekes connector
    cType2 = "cType2"
    # 16A 1 phase IEC60309 socket
    s309_1P_16A = "s309-1P-16A"
    s309_1P_32A = "s309-1P-32A"
    s309_3P_16A = "s309-3P-16A"
    s309_3P_32A = "s309-3P-32A"
    sBS1361 = "sBS1361"
    sCEE_7_7 = "sCEE-7-7"
    sType2 = "sType2"
    sType3 = "sType3"
    other1PhMax16A = " Other1PhMax16A"
    other1PhOver16A = "Other1PhOver16A"
    Pan = "Pan"
    wInductive = "wInductive"
    wResonant = "wResonant"
    undetermined = "Undetermined"
    unknown = "Unknown"


class ConnectorStatus:
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


class CostKindType:
    """
    CostKindEnumType is used by: Common:CostType
    """

    carbonDioxideEmission = "CarbonDioxideEmission"
    relativePricePercentage = " RelativePricePercentage"
    renewableGenerationPercentage = "RenewableGenerationPercentage"


class CustomerInformationStatusType:
    """
    Status in CustomerInformationResponse
    """

    accepted = "Accepted"
    rejected = " Rejected"
    invalid = "Invalid"


class NotifyEVChargingNeedsStatusType:
    """
    Accepted: a SASchedule will be provided momentarily.
    Rejected: Servoce is Not Available
    Processing: The CSMS is gathering information to provide an SASchedule.
    """
    accepted = "Accepted"
    rejected = "Rejected"
    processing = "Processing"


class GenericStatusType:
    accepted = "Accepted"
    rejected = "Rejected"


class LogType:
    diagnosticsLog = "DiagnosticsLog"
    securityLog = "SecurityLog"


class OperationalStatusEnumType:
    """
    Requested availability change in ChangeAvailability.req.
    """

    inoperative = "Inoperative"
    operative = "Operative"


class ChargePointErrorCode:
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


class DataTransferStatus:
    """
    Status in DataTransferResponse.
    """
    accepted = "Accepted"
    rejected = "Rejected"
    unknownMessageId = "UnknownMessageId"
    unknownVendorId = "UnknownVendorId"


class FirmwareStatusType:
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


class LocationType:
    """
    Allowable values of the optional "location" field of a value element in
    SampledValue.
    """

    inlet = "Inlet"
    outlet = "Outlet"
    body = "Body"
    cable = "Cable"
    ev = "EV"


class MeasurandType:
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


class MessageTriggerType:
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


class PhaseType:
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


class ReadingContextType:
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


class ReasonType:
    """
    Reason for stopping a transaction in StopTransaction.req.
    """
    deAuthorized = "DeAuthorized"
    emergencyStop = "EmergencyStop"
    energyLimitReached = "EnergyLimitReached"
    evDisconnected = "EVDisconnected"
    groundFault = "GroundFault"
    immediateReset = "ImmediateReset"
    local = "Local"
    localOutOfCredit = "LocalOutOfCredit"
    masterPass = "MasterPass"
    other = "Other"
    overcurrentFault = "OvercurrentFault"
    powerLoss = "PowerLoss"
    powerQuality = "PowerQuality"
    reboot = "Reboot"
    remote = "Remote"
    socLimitReached = "SOCLimitReached"
    stoppedByEV = "StoppedByEV"
    timeLimitReached = "TimeLimitReached"
    timeout = "Timeout"


class RecurrencyKindType:
    """
    "Daily": The schedule restarts at the beginning of the next day.
    "Weekly": The schedule restarts at the beginning of the next week
              (defined as Monday morning)
    """

    daily = "Daily"
    weekly = "Weekly"


class RegistrationStatusType:
    """
    Result of registration in response to BootNotification.req.
    """

    accepted = "Accepted"
    pending = "Pending"
    rejected = "Rejected"


class ReportBaseType:
    """
    Report Base Type required in GetBaseReportRequest
    """

    configurationInventory = "ConfigurationInventory"
    fullInventory = "FullInventory"
    summaryInventory = "SummaryInventory"


class RequestStartStopStatusType:
    """
    The result of a RemoteStartTransaction.req or RemoteStopTransaction.req
    request.
    """
    accepted = "Accepted"
    rejected = "Rejected"


class ReservationUpdateStatusType:
    expired = "Expired"
    removed = "Removed"


class ReserveNowStatusType:
    """
    Status in ReserveNowResponse.
    """

    accepted = "Accepted"
    faulted = "Faulted"
    occupied = "Occupied"
    rejected = "Rejected"
    unavailable = "Unavailable"


class ResetType:
    """
    Type of reset requested by Reset.req
    """

    immediate = "Immediate"
    onIdle = "OnIdle"


class ResetStatusType:
    """
    Result of Reset.req
    """

    accepted = "Accepted"
    rejected = "Rejected"
    scheduled = "Scheduled"


class SendLocalListStatusType:
    """
    Type of update for a SendLocalList Request.
    """

    accepted = "Accepted"
    failed = "Failed"
    versionMismatch = "VersionMismatch"


class SetMonitoringStatusType:
    """
    Status in SetVariableMonitoringResponse
    """

    accepted = "Accepted"
    unknownComponent = "UnknownComponent"
    unknownVariable = "UnknownVariable"
    unsupportedMonitorType = " UnsupportedMonitorType"
    rejected = "Rejected"
    duplicate = "Duplicate"


class SetNetworkProfileStatusType:
    """
    Status in SetNetworkProfileResponse
    """

    accepted = "Accepted"
    rejected = "Rejected"
    failed = "Failed"


class SetVariableStatusType:
    """
    Status in ChangeConfigurationResponse.
    """

    accepted = "Accepted"
    rejected = "Rejected"
    unknownComponent = "UnknownComponent"
    unknownVariable = "UnknownVariable"
    notSupportedAttributeType = "NotSupportedAttributeType"
    rebootRequired = "RebootRequired"


class TransactionEventType:
    """
    Type of Event in TransactionEventRequest
    """

    ended = "Ended"
    started = "Started"
    updated = "Updated"


class TriggerMessageStatusType:
    """
    Status in TriggerMessageResponse.
    """

    accepted = "Accepted"
    rejected = "Rejected"
    notImplemented = "NotImplemented"


class TriggerMessageStatusType:
    """
    Reason that triggered a transactionEventRequest
    """

    authorized = "Authorized"
    cablePluggedIn = "CablePluggedIn"
    chargingRateChanged = "ChargingRateChanged"
    chargingStateChanged = " ChargingStateChanged"
    deauthorized = "Deauthorized"
    energyLimitReached = "EnergyLimitReached"
    eVCommunicationLost = "EVCommunicationLost"
    eVConnectTimeout = "EVConnectTimeout"
    meterValueClock = "MeterValueClock"
    meterValuePeriodic = "MeterValuePeriodic"
    timeLimitReached = "TimeLimitReached"
    trigger = "Trigger"
    unlockCommand = "UnlockCommand"
    stopAuthorized = "StopAuthorized"
    eVDeparted = "EVDeparted"
    eVDetected = "EVDetected"
    remoteStop = "RemoteStop"
    remoteStart = "RemoteStart"
    abnormalCondition = "AbnormalCondition"
    signedDataReceived = "SignedDataReceived"
    resetCommand = "ResetCommand"


class UnlockStatusType:
    """
    Status in response to UnlockConnector.req.
    """

    unlocked = "Unlocked"
    unlockFailed = "UnlockFailed"
    ongoingAuthorizedTransaction = "OngoingAuthorizedTransaction"
    unknownConnector = "UnknownConnector"


class UnpublishFirmwareStatusType:
    """
    Status for when unpublishing a Firmware (used by UnpublishFirmwareResponse)
    """

    downloadOngoing = "DownloadOngoing"
    noFirmware = "NoFirmware"
    unpublished = "Unpublished"


class UpdateType:
    """
    Type of update for a SendLocalList Request.
    """

    differential = "Differential"
    full = "Full"


class UpdateFirmwareStatusType:
    """
    Generic message response status for UpdateFirmwareResponse
    """

    accepted = "Accepted"
    rejected = "Rejected"
    acceptedCanceled = "AcceptedCanceled"
    invalidCertificate = "InvalidCertificate"
    revokedCertificate = "RevokedCertificate"


class UploadLogStatusType:
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


class VPNType:
    """
    Enumeration of VPN Types used in SetNetworkProfileRequest.VPNType
    """
    badMessage = "IKEv2"
    idle = "IPSec"
    notSupportedOperation = "L2TP"
    permissionDenied = "PPTP"


# DataTypes

class UnitOfMeasureType:
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

