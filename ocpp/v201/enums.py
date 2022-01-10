from enum import Enum


class Action(str, Enum):
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
    SetMonitoringBase = "SetMonitoringBase"
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


class APNAuthenticationType(str, Enum):
    """
    APNAuthenticationEnumType is used by
    setNetworkProfileSetNetworkProfileRequest.APNType
    """
    chap = "CHAP"
    none = "NONE"
    pap = "PAP"
    auto = "AUTO"


class AttributeType(str, Enum):
    """
    AttributeEnumType is used by Common:VariableAttributeType,
    getVariables:GetVariablesRequest.GetVariableDataType ,
    getVariables:GetVariablesResponse.GetVariableResultType ,
    setVariables:SetVariablesRequest.SetVariableDataType ,
    setVariables:SetVariablesResponse.SetVariableResultType
    """
    actual = "Actual"
    target = "Target"
    minSet = "MinSet"
    maxSet = "MaxSet"


class AuthorizationStatusType(str, Enum):
    """
    Elements that constitute an entry of a Local Authorization List update.
    """

    accepted = "Accepted"
    blocked = "Blocked"
    concurrent_tx = "ConcurrentTx"
    expired = "Expired"
    invalid = "Invalid"
    # Identifier is valid, but EV Driver doesn’t have enough credit to start
    # charging. Not allowed for charging.
    no_credit = "NoCredit"
    # Identifier is valid, but not allowed to charge in this type of EVSE.
    not_allowed_type_evse = "NotAllowedTypeEVSE"
    not_at_this_location = "NotAtThisLocation"
    not_at_this_time = "NotAtThisTime"
    unknown = "Unknown"


class AuthorizeCertificateStatusType(str, Enum):
    """
    Status of the EV Contract certificate.
    """

    accepted = "Accepted"
    signature_error = "SignatureError"
    certificate_expired = "CertificateExpired"
    certificate_revoked = "CertificateRevoked"
    no_certificate_available = "NoCertificateAvailable"
    cert_chain_error = "CertChainError"
    contract_cancelled = "ContractCancelled"


class BootReasonType(str, Enum):
    """
    BootReasonEnumType is used by bootNotificationBootNotificationRequest
    """

    application_reset = "ApplicationReset"
    firmware_update = "FirmwareUpdate"
    local_reset = "LocalReset"
    power_up = "PowerUp"
    remote_reset = "RemoteReset"
    scheduled_reset = "ScheduledReset"
    triggered = "Triggered"
    unknown = "Unknown"
    watchdog = "Watchdog"


class CancelReservationStatusType(str, Enum):
    """
    Status in CancelReservationResponse.
    """

    accepted = "Accepted"
    rejected = "Rejected"


class CertificateActionType(str, Enum):
    """
    CertificateActionEnumType is used by
    get15118EVCertificateGet15118EVCertificateRequest
    """
    install = "Install"
    update = "Update"


class CertificateSignedStatusType(str, Enum):
    accepted = "Accepted"
    rejected = "Rejected"


class CertificateSigningUseType(str, Enum):
    """
    CertificateSigningUseEnumType is used by signCertificate
    SignCertificateRequest ,
    certificateSignedCertificateSignedRequest
    """
    charging_station_certificate = "ChargingStationCertificate"
    v2g_certificate = "V2GCertificate"


class ChangeAvailabilityStatusType(str, Enum):
    """
    Status returned in response to ChangeAvailability.req.
    """

    accepted = "Accepted"
    rejected = "Rejected"
    scheduled = "Scheduled"


class ChargingLimitSourceType(str, Enum):
    """
    Enumeration for indicating from which source a charging limit originates.
    """

    ems = "EMS"
    other = "Other"
    so = "SO"
    cso = "CSO"


class ChargingProfileKindType(str, Enum):
    """
    "Absolute" Schedule periods are relative to a fixed point in time defined
                in the schedule.
    "Recurring" Schedule restarts periodically at the first schedule period.
    "Relative" Schedule periods are relative to a situation- specific start
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
    discard it and return an error status in SetChargingProfileResponse.
    TxProfile SHALL only be set at Charge Point ConnectorId >0.

    It is not possible to set a ChargingProfile with purpose set to
    TxProfile without presence of an active transaction, or in advance of
    a transaction.

    In order to ensure that the updated charging profile applies only to the
    current transaction, the chargingProfilePurpose of the ChargingProfile
    MUST be set to TxProfile.
    """
    charging_station_external_constraints = "ChargingStationExternalConstraints"  # noqa: E501
    charging_station_max_profile = "ChargingStationMaxProfile"
    tx_default_profile = "TxDefaultProfile"
    tx_profile = "TxProfile"


class ChargingProfileStatus(str, Enum):
    """
    Status returned in response to SetChargingProfile.req.
    """

    accepted = "Accepted"
    rejected = "Rejected"


class ChargingRateUnitType(str, Enum):
    """
    Unit in which a charging schedule is defined, as used in
    GetCompositeSchedule.req and ChargingSchedule
    """

    watts = "W"
    amps = "A"


class ChargingStateType(str, Enum):
    """
    The state of the charging process.
    """

    charging = "Charging"
    ev_connected = "EVConnected"
    suspended_ev = "SuspendedEV"
    suspended_evse = "SuspendedEVSE"
    idle = "Idle"


class ClearCacheStatusType(str, Enum):
    """
    Status returned in response to ClearCache.req.
    """

    accepted = "Accepted"
    rejected = "Rejected"


class ClearChargingProfileStatusType(str, Enum):
    """
    Status returned in response to ClearChargingProfile.req.
    """

    accepted = "Accepted"
    unknown = "Unknown"


class ClearMessageStatusType(str, Enum):
    """
    Status returned in response to ClearDisplayMessageRequest.
    """

    accepted = "Accepted"
    unknown = "Unknown"


class ClearMonitoringStatusType(str, Enum):
    """
    ClearMonitoringStatusEnumType is used by CommonClearMonitoringResultType
    """

    accepted = "Accepted"
    rejected = "Rejected"
    not_found = "NotFound"


class ComponentCriterionType(str, Enum):
    """
    ComponentCriterionEnumType is used by getReportGetReportRequest
    """

    active = "Active"
    available = "Available"
    enabled = "Enabled"
    problem = "Problem"


class ConnectorStatusType(str, Enum):
    """
    Status reported in StatusNotification.req. A status can be reported for
    the Charge Point main controller (connectorId = 0) or for a specific
    connector. Status for the Charge Point main controller is a subset of the
    enumeration Available, Unavailable or Faulted.

    States considered Operative are Available, Preparing, Charging,
    SuspendedEVSE, SuspendedEV, Finishing, Reserved.
    States considered Inoperative are Unavailable, Faulted.
    """

    available = "Available"
    occupied = "Occupied"
    reserved = "Reserved"
    unavailable = "Unavailable"
    faulted = "Faulted"


class ConnectorType(str, Enum):
    """
    Allowed values of ConnectorCode.
    """
    # Combined Charging System 1 (captive cabled) a.k.a. Combo 1
    c_ccs1 = "cCCS1"
    # Combined Charging System 2 (captive cabled) a.k.a. Combo 2
    c_ccs2 = "cCCS2"
    # JARI G105-1993 (captive cabled) a.k.a. CHAdeMO
    c_g105 = "cG105"
    # Tesla Connector (captive cabled)
    c_tesla = "cTesla"
    # IEC62196-2 Type 1 connector (captive cabled) a.k.a. J1772
    c_type1 = "cType1"
    # IEC62196-2 Type 2 connector (captive cabled) a.k.a. Mennekes connector
    c_type2 = "cType2"
    # 16A 1 phase IEC60309 socket
    s309_1p_16a = "s309-1P-16A"
    s309_1p_32a = "s309-1P-32A"
    s309_3p_16a = "s309-3P-16A"
    s309_3p_32a = "s309-3P-32A"
    s_bs1361 = "sBS1361"
    s_cee_7_7 = "sCEE-7-7"
    s_type2 = "sType2"
    s_type3 = "sType3"
    other_1ph_max_16a = "Other1PhMax16A"
    other_1ph_over_16a = "Other1PhOver16A"
    other_3ph = "Other3Ph"
    pan = "Pan"
    w_inductive = "wInductive"
    w_resonant = "wResonant"
    undetermined = "Undetermined"
    unknown = "Unknown"


class CostKindType(str, Enum):
    """
    CostKindEnumType is used by CommonCostType
    """

    carbon_dioxide_emission = "CarbonDioxideEmission"
    relative_price_percentage = "RelativePricePercentage"
    renewable_generation_percentage = "RenewableGenerationPercentage"


class CustomerInformationStatusType(str, Enum):
    """
    Status in CustomerInformationResponse
    """

    accepted = "Accepted"
    rejected = "Rejected"
    invalid = "Invalid"


class DataTransferStatusType(str, Enum):
    """
    Status in DataTransferResponse.
    """
    accepted = "Accepted"
    rejected = "Rejected"
    unknown_message_id = "UnknownMessageId"
    unknown_vendor_id = "UnknownVendorId"


class DataType(str, Enum):
    """
    DataEnumType is used by CommonVariableCharacteristicsType
    """
    string = "string"
    decimal = "decimal"
    integer = "integer"
    date_time = "dateTime"
    boolean = "boolean"
    option_list = "OptionList"
    sequence_list = "SequenceList"
    member_list = "MemberList"


class DeleteCertificateStatusType(str, Enum):
    """
    DeleteCertificateStatusEnumType is used by
    deleteCertificateDeleteCertificateResponse
    """
    accepted = "Accepted"
    failed = "Failed"
    not_found = "NotFound"


class DisplayMessageStatusType(str, Enum):
    """
    Result for a SetDisplayMessageRequest as used in a
    SetDisplayMessageResponse.
    """
    accepted = "Accepted"
    not_supported_message_format = "NotSupportedMessageFormat"
    rejected = "Rejected"
    not_supported_priority = "NotSupportedPriority"
    not_supported_state = "NotSupportedState"
    unknown_transaction = "UnknownTransaction"


class EnergyTransferModeType(str, Enum):
    """
    Enumeration of energy transfer modes.
    """
    dc = "DC"
    ac_single_phase = "AC_single_phase"
    ac_two_phase = "AC_two_phase"
    ac_three_phase = "AC_three_phase"


class EventNotificationType(str, Enum):
    """
    Specifies the event notification type of the message.
    """
    hard_wired_notification = "HardWiredNotification"
    hard_wired_monitor = "HardWiredMonitor"
    preconfigured_monitor = "PreconfiguredMonitor"
    custom_monitor = "CustomMonitor"


class EventTriggerType(str, Enum):
    """
    EventTriggerEnumType is used by
    notifyEventNotifyEventRequest.EventDataType
    """
    alerting = "Alerting"
    delta = "Delta"
    periodic = "Periodic"


class FirmwareStatusType(str, Enum):
    """
    Status of a firmware download as reported in
    FirmwareStatusNotificationRequest
    """
    downloaded = "Downloaded"
    download_failed = "DownloadFailed"
    downloading = "Downloading"
    download_scheduled = "DownloadScheduled"
    download_paused = "DownloadPaused"
    idle = "Idle"
    installation_failed = "InstallationFailed"
    installing = "Installing"
    installed = "Installed"
    install_rebooting = "InstallRebooting"
    install_scheduled = "InstallScheduled"
    install_verification_failed = "InstallVerificationFailed"
    invalid_signature = "InvalidSignature"
    signature_verified = "SignatureVerified"


class GenericDeviceModelStatusType(str, Enum):
    """
    Status of a firmware download as reported in GetBaseReportResponse
    """
    accepted = "Accepted"
    rejected = "Rejected"
    not_supported = "NotSupported"
    empty_result_set = "EmptyResultSet"


class GenericStatusType(str, Enum):
    """
    Generic message response status
    """
    accepted = "Accepted"
    rejected = "Rejected"


class GetCertificateIdUseType(str, Enum):
    v2g_root_certificate = "V2GRootCertificate"
    mo_root_certificate = "MORootCertificate"
    csms_root_certificate = "CSMSRootCertificate"
    v2g_certificate_chain = "V2GCertificateChain"
    manufacturer_root_certificate = "ManufacturerRootCertificate"


class GetCertificateStatusType(str, Enum):
    """
    GetCertificateStatusEnumType is used by
     getCertificateStatusGetCertificateStatusResponse
    """
    accepted = "Accepted"
    failed = "Failed"


class GetChargingProfileStatusType(str, Enum):
    """
    GetChargingProfileStatusEnumType is used by
    getChargingProfilesGetChargingProfilesResponse
    """
    accepted = "Accepted"
    no_profiles = "NoProfiles"


class GetDisplayMessagesStatusType(str, Enum):
    """
    GetDisplayMessagesStatusEnumType is used by
    getDisplayMessagesGetDisplayMessagesResponse
    """
    accepted = "Accepted"
    unknown = "Unknown"


class GetInstalledCertificateStatusType(str, Enum):
    """
    GetInstalledCertificateStatusEnumType is used by
    getInstalledCertificateIdsGetInstalledCertificateIdsResponse
    """
    accepted = "Accepted"
    notFound = "NotFound"


class GetVariableStatusType(str, Enum):
    """
    GetVariableStatusEnumType is used by
    getVariablesGetVariablesResponse.GetVariableResultType
    """
    accepted = "Accepted"
    rejected = "Rejected"
    unknown_component = "UnknownComponent"
    unknown_variable = "UnknownVariable"
    not_supported_attribute_type = "NotSupportedAttributeType"


class HashAlgorithmType(str, Enum):
    """
    HashAlgorithmEnumType is used by
    CommonCertificateHashDataType , CommonOCSPRequestDataType
    """
    sha256 = "SHA256"
    sha384 = "SHA384"
    sha512 = "SHA512"


class IdTokenType(str, Enum):
    """
    Allowable values of the IdTokenType field.
    """
    central = "Central"
    e_maid = "eMAID"
    iso14443 = "ISO14443"
    iso15693 = "ISO15693"
    key_code = "KeyCode"
    local = "Local"
    mac_address = "MacAddress"
    no_authorization = "NoAuthorization"


class InstallCertificateStatusType(str, Enum):
    """
    InstallCertificateStatusEnumType is used by
    installCertificateInstallCertificateResponse
    """
    accepted = "Accepted"
    rejected = "Rejected"
    failed = "Failed"


class InstallCertificateUseType(str, Enum):
    """
    InstallCertificateUseEnumType is used by
    installCertificateInstallCertificateRequest
    """
    v2g_root_certificate = "V2GRootCertificate"
    mo_root_certificate = "MORootCertificate"
    csms_root_certificate = "CSMSRootCertificate"
    manufacturer_root_certificate = "ManufacturerRootCertificate"


class Iso15118EVCertificateStatusType(str, Enum):
    """
    Iso15118EVCertificateStatusEnumType is used by
    get15118EVCertificateGet15118EVCertificateResponse
    """
    accepted = "Accepted"
    failed = "Failed"


class LocationType(str, Enum):
    """
    Allowable values of the optional "location" field of a value element in
    SampledValue.
    """
    body = "Body"
    cable = "Cable"
    ev = "EV"
    inlet = "Inlet"
    outlet = "Outlet"


class LogType(str, Enum):
    """
    LogEnumType is used by getLogGetLogRequest
    """
    diagnostics_log = "DiagnosticsLog"
    security_log = "SecurityLog"


class LogStatusType(str, Enum):
    """
    Generic message response status
    """

    accepted = "Accepted"
    rejected = "Rejected"
    accepted_canceled = "AcceptedCanceled"


class MeasurandType(str, Enum):
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
    energy_active_net = "Energy.Active.Net"
    energy_reactive_export_interval = "Energy.Reactive.Export.Interval"
    energy_reactive_import_interval = "Energy.Reactive.Import.Interval"
    energy_reactive_net = "Energy.Reactive.Net"
    energy_apparent_net = "Energy.Apparent.Net"
    energy_apparent_import = "Energy.Apparent.Import"
    energy_apparent_export = "Energy.Apparent.Export"
    frequency = "Frequency"
    power_active_export = "Power.Active.Export"
    power_active_import = "Power.Active.Import"
    power_factor = "Power.Factor"
    power_offered = "Power.Offered"
    power_reactive_export = "Power.Reactive.Export"
    power_reactive_import = "Power.Reactive.Import"
    soc = "SoC"
    voltage = "Voltage"


class MessageFormatType(str, Enum):
    """
    Format of a message to be displayed on the display of the Charging Station.
    """
    ascii = "ASCII"
    html = "HTML"
    uri = "URI"
    utf8 = "UTF8"


class MessagePriorityType(str, Enum):
    """
    Priority with which a message should be displayed on a Charging Station.
    """
    always_front = "AlwaysFront"
    in_front = "InFront"
    normal_cycle = "NormalCycle"


class MessageStateType(str, Enum):
    """
    State of the Charging Station during which a message SHALL be displayed.
    """
    charging = "Charging"
    faulted = "Faulted"
    idle = "Idle"


class MessageTriggerType(str, Enum):
    """
    Type of request to be triggered in a TriggerMessage.req
    """

    boot_notification = "BootNotification"
    log_status_notification = "LogStatusNotification"
    firmware_status_notification = "FirmwareStatusNotification"
    heartbeat = "Heartbeat"
    meter_values = "MeterValues"
    # Triggers a SignCertificate with typeOfCertificate
    # ChargingStationCertificate.
    sign_charging_station_certificate = "SignChargingStationCertificate"
    # Triggers a SignCertificate with typeOfCertificate V2GCertificate
    sign_v2_gcertificate = "SignV2GCertificate"
    status_notification = "StatusNotification"
    transaction_event = "TransactionEvent"
    sign_combined_certificate = "SignCombinedCertificate"
    publish_firmware_status_notification = "PublishFirmwareStatusNotification"


class MonitorType(str, Enum):
    """
    MonitorEnumType is used by CommonVariableMonitoringType
    """
    upper_threshold = "UpperThreshold"
    lower_threshold = "LowerThreshold"
    delta = "Delta"
    periodic = "Periodic"
    periodic_clock_aligned = "PeriodicClockAligned"


class MonitorBaseType(str, Enum):
    """
    MonitoringBaseEnumType is used by
    setMonitoringBaseSetMonitoringBaseRequest
    """
    all = "All"
    factory_default = "FactoryDefault"
    hard_wired_only = "HardWiredOnly"


class MonitoringCriterionType(str, Enum):
    """
    MonitoringCriterionEnumType is used by
    getMonitoringReportGetMonitoringReportRequest
    """
    threshold_monitoring = "ThresholdMonitoring"
    delta_monitoring = "DeltaMonitoring"
    periodic_monitoring = "PeriodicMonitoring"


class MutabilityType(str, Enum):
    """
    MutabilityEnumType is used by CommonVariableAttributeType
    """
    read_only = "ReadOnly"
    write_only = "WriteOnly"
    read_write = "ReadWrite"


class NotifyEVChargingNeedsStatusType(str, Enum):
    """
    Accepted a SASchedule will be provided momentarily.
    Rejected Servoce is Not Available
    Processing The CSMS is gathering information to provide an SASchedule.
    """
    accepted = "Accepted"
    rejected = "Rejected"
    processing = "Processing"


class OCPPInterfaceType(str, Enum):
    """
    Enumeration of network interfaces.
    """

    wired0 = "Wired0"
    wired1 = "Wired1"
    wired2 = "Wired2"
    wired3 = "Wired3"
    wireless0 = "Wireless0"
    wireless1 = "Wireless1"
    wireless2 = "Wireless2"
    wireless3 = "Wireless3"


class OCPPTransportType(str, Enum):
    """
    Enumeration of OCPP transport mechanisms.
    SOAP is currently not a valid value for OCPP 2.0.
    """

    json = "JSON"
    soap = "SOAP"


class OCPPVersionType(str, Enum):
    """
    Enumeration of OCPP transport mechanisms.
    SOAP is currently not a valid value for OCPP 2.0.
    """

    ocpp12 = "OCPP12"
    ocpp15 = "OCPP15"
    ocpp16 = "OCPP16"
    ocpp20 = "OCPP20"


class OperationalStatusType(str, Enum):
    """
    Requested availability change in ChangeAvailability.req.
    """

    inoperative = "Inoperative"
    operative = "Operative"


class PhaseType(str, Enum):
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


class PublishFirmwareStatusType(str, Enum):
    """
    Status for when publishing a Firmware
    """

    idle = "Idle"
    download_scheduled = "DownloadScheduled"
    downloading = "Downloading"
    downloaded = "Downloaded"
    published = "Published"
    download_failed = "DownloadFailed"
    download_paused = "DownloadPaused"
    invalid_checksum = "InvalidChecksum"
    checksum_verified = "ChecksumVerified"
    publish_failed = "PublishFailed"


class ReadingContextType(str, Enum):
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


class ReasonType(str, Enum):
    """
    Reason for stopping a transaction in StopTransactionRequest
    """
    de_authorized = "DeAuthorized"
    emergency_stop = "EmergencyStop"
    energy_limit_reached = "EnergyLimitReached"
    ev_disconnected = "EVDisconnected"
    ground_fault = "GroundFault"
    immediate_reset = "ImmediateReset"
    local = "Local"
    local_out_of_credit = "LocalOutOfCredit"
    master_pass = "MasterPass"
    other = "Other"
    overcurrent_fault = "OvercurrentFault"
    power_loss = "PowerLoss"
    power_quality = "PowerQuality"
    reboot = "Reboot"
    remote = "Remote"
    soc_limit_reached = "SOCLimitReached"
    stopped_by_ev = "StoppedByEV"
    time_limit_reached = "TimeLimitReached"
    timeout = "Timeout"


class RecurrencyKindType(str, Enum):
    """
    "Daily" The schedule restarts at the beginning of the next day.
    "Weekly" The schedule restarts at the beginning of the next week
              (defined as Monday morning)
    """

    daily = "Daily"
    weekly = "Weekly"


class RegistrationStatusType(str, Enum):
    """
    Result of registration in response to BootNotification.req.
    """

    accepted = "Accepted"
    pending = "Pending"
    rejected = "Rejected"


class ReportBaseType(str, Enum):
    """
    Report Base Type required in GetBaseReportRequest
    """

    configuration_inventory = "ConfigurationInventory"
    full_inventory = "FullInventory"
    summary_inventory = "SummaryInventory"


class RequestStartStopStatusType(str, Enum):
    """
    The result of a RemoteStartTransaction.req or RemoteStopTransaction.req
    request.
    """
    accepted = "Accepted"
    rejected = "Rejected"


class ReservationUpdateStatusType(str, Enum):
    expired = "Expired"
    removed = "Removed"


class ReserveNowStatusType(str, Enum):
    """
    Status in ReserveNowResponse.
    """

    accepted = "Accepted"
    faulted = "Faulted"
    occupied = "Occupied"
    rejected = "Rejected"
    unavailable = "Unavailable"


class ResetStatusType(str, Enum):
    """
    Result of Reset.req
    """

    accepted = "Accepted"
    rejected = "Rejected"
    scheduled = "Scheduled"


class ResetType(str, Enum):
    """
    Type of reset requested by Reset.req
    """
    immediate = "Immediate"
    on_idle = "OnIdle"


class SendLocalListStatusType(str, Enum):
    """
    Type of update for a SendLocalList Request.
    """

    accepted = "Accepted"
    failed = "Failed"
    version_mismatch = "VersionMismatch"


class SetMonitoringStatusType(str, Enum):
    """
    Status in SetVariableMonitoringResponse
    """

    accepted = "Accepted"
    unknown_component = "UnknownComponent"
    unknown_variable = "UnknownVariable"
    unsupported_monitor_type = "UnsupportedMonitorType"
    rejected = "Rejected"
    duplicate = "Duplicate"


class SetNetworkProfileStatusType(str, Enum):
    """
    Status in SetNetworkProfileResponse
    """

    accepted = "Accepted"
    rejected = "Rejected"
    failed = "Failed"


class SetVariableStatusType(str, Enum):
    """
    Status in ChangeConfigurationResponse.
    """

    accepted = "Accepted"
    rejected = "Rejected"
    unknown_component = "UnknownComponent"
    unknown_variable = "UnknownVariable"
    not_supported_attribute_type = "NotSupportedAttributeType"
    reboot_required = "RebootRequired"


class TransactionEventType(str, Enum):
    """
    Type of Event in TransactionEventRequest
    """

    ended = "Ended"
    started = "Started"
    updated = "Updated"


class TriggerMessageStatusType(str, Enum):
    """
    Status in TriggerMessageResponse.
    """

    accepted = "Accepted"
    rejected = "Rejected"
    not_implemented = "NotImplemented"


class TriggerReasonType(str, Enum):
    """
    Reason that triggered a transactionEventRequest
    """

    authorized = "Authorized"
    cable_plugged_in = "CablePluggedIn"
    charging_rate_changed = "ChargingRateChanged"
    charging_state_changed = "ChargingStateChanged"
    deauthorized = "Deauthorized"
    energy_limit_reached = "EnergyLimitReached"
    ev_communication_lost = "EVCommunicationLost"
    ev_connect_timeout = "EVConnectTimeout"
    meter_value_clock = "MeterValueClock"
    meter_value_periodic = "MeterValuePeriodic"
    time_limit_reached = "TimeLimitReached"
    trigger = "Trigger"
    unlock_command = "UnlockCommand"
    stop_authorized = "StopAuthorized"
    ev_departed = "EVDeparted"
    ev_detected = "EVDetected"
    remote_stop = "RemoteStop"
    remote_start = "RemoteStart"
    abnormal_condition = "AbnormalCondition"
    signed_data_received = "SignedDataReceived"
    reset_command = "ResetCommand"


class UnlockStatusType(str, Enum):
    """
    Status in response to UnlockConnector.req.
    """

    unlocked = "Unlocked"
    unlock_failed = "UnlockFailed"
    ongoing_authorized_transaction = "OngoingAuthorizedTransaction"
    unknown_connector = "UnknownConnector"


class UnpublishFirmwareStatusType(str, Enum):
    """
    Status for when unpublishing a Firmware (used by UnpublishFirmwareResponse)
    """

    download_ongoing = "DownloadOngoing"
    no_firmware = "NoFirmware"
    unpublished = "Unpublished"


class UpdateFirmwareStatusType(str, Enum):
    """
    Generic message response status for UpdateFirmwareResponse
    """

    accepted = "Accepted"
    rejected = "Rejected"
    accepted_canceled = "AcceptedCanceled"
    invalid_certificate = "InvalidCertificate"
    revoked_certificate = "RevokedCertificate"


class UpdateType(str, Enum):
    """
    Type of update for a SendLocalList Request.
    """

    differential = "Differential"
    full = "Full"


class UploadLogStatusType(str, Enum):
    """
    Status in LogStatusNotificationRequest.
    """
    bad_message = "BadMessage"
    idle = "Idle"
    not_supported_operation = "NotSupportedOperation"
    permission_denied = "PermissionDenied"
    uploaded = "Uploaded"
    upload_failure = "UploadFailure"
    uploading = "Uploading"
    accepted_canceled = "AcceptedCanceled"


class VPNType(str, Enum):
    """
    Enumeration of VPN Types used in SetNetworkProfileRequest.VPNType
    """
    ikev2 = "IKEv2"
    ipsec = "IPSec"
    l2tp = "L2TP"
    pptp = "PPTP"


# DataTypes

class UnitOfMeasureType(str, Enum):
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
    kvah = "kVAh"
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


class StatusInfoReasonType(str, Enum):
    """Standardized reason codes for StatusInfo defined in Appendix 5."""
    cs_not_accepted = "CSNotAccepted"
    duplicate_profile = "DuplicateProfile"
    duplicate_request_id = "DuplicateRequestId"
    fixed_cable = "FixedCable"
    fw_update_in_progress = "FwUpdateInProgress"
    internal_error = "InternalError"
    invalid_certificate = "InvalidCertificate"
    invalid_csr = "InvalidCSR"
    invalid_id_token = "InvalidIdToken"
    invalid_profile = "InvalidProfile"
    invaild_schedule = "InvalidSchedule"
    invalid_stack_level = "InvalidStackLevel"
    invalid_url = "InvalidURL"
    invalid_value = "InvalidValue"
    missing_param = "MissingParam"
    no_cable = "NoCable"
    no_error = "NoError"
    not_enabled = "NotEnabled"
    not_found = "NotFound"
    out_of_memory = "OutOfMemory"
    out_of_storage = "OutOfStorage"
    read_only = "ReadOnly"
    too_large_element = "TooLargeElement"
    too_many_elements = "TooManyElements"
    tx_in_progress = "TxInProgress"
    tx_not_found = "TxNotFound"
    tx_started = "TxStarted"
    unknown_connector_id = "UnknownConnectorId"
    unknown_connector_type = "UnknownConnectorType"
    unknown_evse = "UnknownEvse"
    unknown_tx_id = "UnknownTxId"
    unspecified = "Unspecified"
    unsupported_param = "UnsupportedParam"
    unsupported_rate_unit = "UnsupportedRateUnit"
    unsupported_request = "UnsupportedRequest"
    value_out_of_range = "ValueOutOfRange"
    value_positive_only = "ValuePositiveOnly"
    value_too_hight = "ValueTooHigh"
    value_too_low = "ValueTooLow"
    value_zero_not_allowed = "ValueZeroNotAllowed"
    write_only = "WriteOnly"
