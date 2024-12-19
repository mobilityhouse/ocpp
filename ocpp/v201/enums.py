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
    clear_cache = "ClearCache"
    clear_charging_profile = "ClearChargingProfile"
    clear_display_message = "ClearDisplayMessage"
    cleared_charging_limit = "ClearedChargingLimit"
    clear_variable_monitoring = "ClearVariableMonitoring"
    cost_updated = "CostUpdated"
    customer_information = "CustomerInformation"
    data_transfer = "DataTransfer"
    delete_certificate = "DeleteCertificate"
    firmware_status_notification = "FirmwareStatusNotification"
    get_15118_ev_certificate = "Get15118EVCertificate"
    get_base_report = "GetBaseReport"
    get_certificate_status = "GetCertificateStatus"
    get_charging_profiles = "GetChargingProfiles"
    get_composite_schedule = "GetCompositeSchedule"
    get_display_messages = "GetDisplayMessages"
    get_installed_certificate_ids = "GetInstalledCertificateIds"
    get_local_list_version = "GetLocalListVersion"
    get_log = "GetLog"
    get_monitoring_report = "GetMonitoringReport"
    get_report = "GetReport"
    get_transaction_status = "GetTransactionStatus"
    get_variables = "GetVariables"
    heartbeat = "Heartbeat"
    install_certificate = "InstallCertificate"
    log_status_notification = "LogStatusNotification"
    meter_values = "MeterValues"
    notify_charging_limit = "NotifyChargingLimit"
    notify_customer_information = "NotifyCustomerInformation"
    notify_display_messages = "NotifyDisplayMessages"
    notify_ev_charging_needs = "NotifyEVChargingNeeds"
    notify_ev_charging_schedule = "NotifyEVChargingSchedule"
    notify_event = "NotifyEvent"
    notify_monitoring_report = "NotifyMonitoringReport"
    notify_report = "NotifyReport"
    publish_firmware = "PublishFirmware"
    publish_firmware_status_notification = "PublishFirmwareStatusNotification"
    report_charging_profiles = "ReportChargingProfiles"
    request_start_transaction = "RequestStartTransaction"
    request_stop_transaction = "RequestStopTransaction"
    reservation_status_update = "ReservationStatusUpdate"
    reserve_now = "ReserveNow"
    reset = "Reset"
    security_event_notification = "SecurityEventNotification"
    send_local_list = "SendLocalList"
    set_charging_profile = "SetChargingProfile"
    set_display_message = "SetDisplayMessage"
    set_monitoring_base = "SetMonitoringBase"
    set_monitoring_level = "SetMonitoringLevel"
    set_network_profile = "SetNetworkProfile"
    set_variable_monitoring = "SetVariableMonitoring"
    set_variables = "SetVariables"
    sign_certificate = "SignCertificate"
    status_notification = "StatusNotification"
    transaction_event = "TransactionEvent"
    trigger_message = "TriggerMessage"
    unlock_connector = "UnlockConnector"
    unpublish_firmware = "UnpublishFirmware"
    update_firmware = "UpdateFirmware"


class APNAuthenticationEnumType(StrEnum):
    """
    APNAuthenticationEnumType is used by
    setNetworkProfileSetNetworkProfileRequest.APNType
    """

    chap = "CHAP"
    none = "NONE"
    pap = "PAP"
    auto = "AUTO"


class AttributeEnumType(StrEnum):
    """
    AttributeEnumType is used by Common:VariableAttributeType,
    getVariables:GetVariablesRequest.GetVariableDataType ,
    getVariables:GetVariablesResponse.GetVariableResultType ,
    setVariables:SetVariablesRequest.SetVariableDataType ,
    setVariables:SetVariablesResponse.SetVariableResultType ,
    ConnectedEV component variable AttributeType
    """

    actual = "Actual"
    target = "Target"
    min_set = "MinSet"
    max_set = "MaxSet"


class AuthorizationStatusEnumType(StrEnum):
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


class AuthorizeCertificateStatusEnumType(StrEnum):
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


class BootReasonEnumType(StrEnum):
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


class CancelReservationStatusEnumType(StrEnum):
    """
    Status in CancelReservationResponse.
    """

    accepted = "Accepted"
    rejected = "Rejected"


class CertificateActionEnumType(StrEnum):
    """
    CertificateActionEnumType is used by
    get15118EVCertificateGet15118EVCertificateRequest
    """

    install = "Install"
    update = "Update"


class CertificateSignedStatusEnumType(StrEnum):
    accepted = "Accepted"
    rejected = "Rejected"


class CertificateSigningUseEnumType(StrEnum):
    """
    CertificateSigningUseEnumType is used by signCertificate
    SignCertificateRequest ,
    certificateSignedCertificateSignedRequest
    """

    charging_station_certificate = "ChargingStationCertificate"
    v2g_certificate = "V2GCertificate"


class ChangeAvailabilityStatusEnumType(StrEnum):
    """
    Status returned in response to ChangeAvailability.req.
    """

    accepted = "Accepted"
    rejected = "Rejected"
    scheduled = "Scheduled"


class ChargingLimitSourceEnumType(StrEnum):
    """
    Enumeration for indicating from which source a charging limit originates.
    """

    ems = "EMS"
    other = "Other"
    so = "SO"
    cso = "CSO"


class ChargingProfileKindEnumType(StrEnum):
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


class ChargingProfilePurposeEnumType(StrEnum):
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

    charging_station_external_constraints = (
        "ChargingStationExternalConstraints"  # noqa: E501
    )
    charging_station_max_profile = "ChargingStationMaxProfile"
    tx_default_profile = "TxDefaultProfile"
    tx_profile = "TxProfile"


class ChargingProfileStatusEnumType(StrEnum):
    """
    Status returned in response to SetChargingProfile.req.
    """

    accepted = "Accepted"
    rejected = "Rejected"


class ChargingRateUnitEnumType(StrEnum):
    """
    Unit in which a charging schedule is defined, as used in
    GetCompositeSchedule.req and ChargingSchedule
    """

    watts = "W"
    amps = "A"


class ChargingStateEnumType(StrEnum):
    """
    The state of the charging process.
    """

    charging = "Charging"
    ev_connected = "EVConnected"
    suspended_ev = "SuspendedEV"
    suspended_evse = "SuspendedEVSE"
    idle = "Idle"


class ClearCacheStatusEnumType(StrEnum):
    """
    Status returned in response to ClearCache.req.
    """

    accepted = "Accepted"
    rejected = "Rejected"


class ClearChargingProfileStatusEnumType(StrEnum):
    """
    Status returned in response to ClearChargingProfile.req.
    """

    accepted = "Accepted"
    unknown = "Unknown"


class ClearMessageStatusEnumType(StrEnum):
    """
    Status returned in response to ClearDisplayMessageRequest.
    """

    accepted = "Accepted"
    unknown = "Unknown"


class ClearMonitoringStatusEnumType(StrEnum):
    """
    ClearMonitoringStatusEnumType is used by CommonClearMonitoringResultType
    """

    accepted = "Accepted"
    rejected = "Rejected"
    not_found = "NotFound"


class ComponentCriterionEnumType(StrEnum):
    """
    ComponentCriterionEnumType is used by getReportGetReportRequest
    """

    active = "Active"
    available = "Available"
    enabled = "Enabled"
    problem = "Problem"


class ConnectorStatusEnumType(StrEnum):
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


class ConnectorEnumType(StrEnum):
    """
    Allowed values of ConnectorCode.
    """

    # Combined Charging System 1 (captive cabled) a.k.a. Combo 1
    c_ccs1 = "cCCS1"
    # Combined Charging System 2 (captive cabled) a.k.a. Combo 2
    c_ccs2 = "cCCS2"
    # ChaoJi: New CHAdeMO connector harmonised with GB/T
    c_chao_ji = "cChaoJi"
    # JARI G105-1993 (captive cabled) a.k.a. CHAdeMO
    c_g105 = "cG105"
    # GB/T: Chinese DC charging connector
    c_gbt = "cGBT"
    # Tesla Connector (captive cabled)
    c_tesla = "cTesla"
    # IEC62196-2 Type 1 connector (captive cabled) a.k.a. J1772
    c_type1 = "cType1"
    # IEC62196-2 Type 2 connector (captive cabled) a.k.a. Mennekes connector
    c_type2 = "cType2"
    # 16A 1 phase IEC60309 socket
    s309_1p_16a = "s309-1P-16A"
    # 32A 1 phase IEC60309 socket
    s309_1p_32a = "s309-1P-32A"
    # 16A 3 phase IEC60309 socket
    s309_3p_16a = "s309-3P-16A"
    # 32A 3 phase IEC60309 socket
    s309_3p_32a = "s309-3P-32A"
    # UK domestic socket a.k.a. 13Amp
    s_bs1361 = "sBS1361"
    # CEE 7/7 16A socket. May represent 7/4 & 7/5 a.k.a Schuko
    s_cee_7_7 = "sCEE-7-7"
    # IEC62196-2 Type 2 socket a.k.a. Mennekes socket
    s_type2 = "sType2"
    # IEC62196-2 Type 3 socket a.k.a. Scame
    s_type3 = "sType3"
    # Reverse pantograph
    opp_charge = "OppCharge"
    # Other single phase (domestic) sockets not mentioned above, rated at
    # no more than 16A. CEE7/17, AS3112, NEMA 5-15, NEMA 5-20, JISC8303,
    # TIS166, SI 32, CPCS-CCC, SEV1011, etc.
    other_1ph_max_16a = "Other1PhMax16A"
    # Other single phase sockets not mentioned above (over 16A)
    other_1ph_over_16a = "Other1PhOver16A"
    # Other 3 phase sockets not mentioned above. NEMA14-30, NEMA14-50
    other_3ph = "Other3Ph"
    # Pantograph connector
    pan = "Pan"
    # Wireless inductively coupled connection (generic)
    w_inductive = "wInductive"
    # Wireless resonant coupled connection (generic)
    w_resonant = "wResonant"
    # Yet to be determined (e.g. before plugged in)
    undetermined = "Undetermined"
    # Unknown & not determinable
    unknown = "Unknown"


class CostKindEnumType(StrEnum):
    """
    CostKindEnumType is used by CommonCostType
    """

    carbon_dioxide_emission = "CarbonDioxideEmission"
    relative_price_percentage = "RelativePricePercentage"
    renewable_generation_percentage = "RenewableGenerationPercentage"


class CustomerInformationStatusEnumType(StrEnum):
    """
    Status in CustomerInformationResponse
    """

    accepted = "Accepted"
    rejected = "Rejected"
    invalid = "Invalid"


class DataTransferStatusEnumType(StrEnum):
    """
    Status in DataTransferResponse.
    """

    accepted = "Accepted"
    rejected = "Rejected"
    unknown_message_id = "UnknownMessageId"
    unknown_vendor_id = "UnknownVendorId"


class DataEnumType(StrEnum):
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
    password_string = "passwordString"


class DeleteCertificateStatusEnumType(StrEnum):
    """
    DeleteCertificateStatusEnumType is used by
    deleteCertificateDeleteCertificateResponse
    """

    accepted = "Accepted"
    failed = "Failed"
    not_found = "NotFound"


class DisplayMessageStatusEnumType(StrEnum):
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


class EnergyTransferModeEnumType(StrEnum):
    """
    Enumeration of energy transfer modes.
    """

    dc = "DC"
    ac_single_phase = "AC_single_phase"
    ac_two_phase = "AC_two_phase"
    ac_three_phase = "AC_three_phase"


class EventNotificationEnumType(StrEnum):
    """
    Specifies the event notification type of the message.
    """

    hard_wired_notification = "HardWiredNotification"
    hard_wired_monitor = "HardWiredMonitor"
    preconfigured_monitor = "PreconfiguredMonitor"
    custom_monitor = "CustomMonitor"


class EventTriggerEnumType(StrEnum):
    """
    EventTriggerEnumType is used by
    notifyEventNotifyEventRequest.EventDataType
    """

    alerting = "Alerting"
    delta = "Delta"
    periodic = "Periodic"


class FirmwareStatusEnumType(StrEnum):
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


class GenericDeviceModelStatusEnumType(StrEnum):
    """
    Status of a firmware download as reported in GetBaseReportResponse
    """

    accepted = "Accepted"
    rejected = "Rejected"
    not_supported = "NotSupported"
    empty_result_set = "EmptyResultSet"


class GenericStatusEnumType(StrEnum):
    """
    Generic message response status
    """

    accepted = "Accepted"
    rejected = "Rejected"


class GetCertificateIdUseEnumType(StrEnum):
    v2g_root_certificate = "V2GRootCertificate"
    mo_root_certificate = "MORootCertificate"
    csms_root_certificate = "CSMSRootCertificate"
    v2g_certificate_chain = "V2GCertificateChain"
    manufacturer_root_certificate = "ManufacturerRootCertificate"


class GetCertificateStatusEnumType(StrEnum):
    """
    GetCertificateStatusEnumType is used by
     getCertificateStatusGetCertificateStatusResponse
    """

    accepted = "Accepted"
    failed = "Failed"


class GetChargingProfileStatusEnumType(StrEnum):
    """
    GetChargingProfileStatusEnumType is used by
    getChargingProfilesGetChargingProfilesResponse
    """

    accepted = "Accepted"
    no_profiles = "NoProfiles"


class GetDisplayMessagesStatusEnumType(StrEnum):
    """
    GetDisplayMessagesStatusEnumType is used by
    getDisplayMessagesGetDisplayMessagesResponse
    """

    accepted = "Accepted"
    unknown = "Unknown"


class GetInstalledCertificateStatusEnumType(StrEnum):
    """
    GetInstalledCertificateStatusEnumType is used by
    getInstalledCertificateIdsGetInstalledCertificateIdsResponse
    """

    accepted = "Accepted"
    notFound = "NotFound"


class GetVariableStatusEnumType(StrEnum):
    """
    GetVariableStatusEnumType is used by
    getVariablesGetVariablesResponse.GetVariableResultType
    """

    accepted = "Accepted"
    rejected = "Rejected"
    unknown_component = "UnknownComponent"
    unknown_variable = "UnknownVariable"
    not_supported_attribute_type = "NotSupportedAttributeType"


class HashAlgorithmEnumType(StrEnum):
    """
    HashAlgorithmEnumType is used by
    CommonCertificateHashDataType , CommonOCSPRequestDataType
    """

    sha256 = "SHA256"
    sha384 = "SHA384"
    sha512 = "SHA512"


class IdTokenEnumType(StrEnum):
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


class InstallCertificateStatusEnumType(StrEnum):
    """
    InstallCertificateStatusEnumType is used by
    installCertificateInstallCertificateResponse
    """

    accepted = "Accepted"
    rejected = "Rejected"
    failed = "Failed"


class InstallCertificateUseEnumType(StrEnum):
    """
    InstallCertificateUseEnumType is used by
    installCertificateInstallCertificateRequest
    """

    v2g_root_certificate = "V2GRootCertificate"
    mo_root_certificate = "MORootCertificate"
    csms_root_certificate = "CSMSRootCertificate"
    manufacturer_root_certificate = "ManufacturerRootCertificate"


class Iso15118EVCertificateStatusEnumType(StrEnum):
    """
    Iso15118EVCertificateStatusEnumType is used by
    get15118EVCertificateGet15118EVCertificateResponse
    """

    accepted = "Accepted"
    failed = "Failed"


class LocationEnumType(StrEnum):
    """
    Allowable values of the optional "location" field of a value element in
    SampledValue.
    """

    body = "Body"
    cable = "Cable"
    ev = "EV"
    inlet = "Inlet"
    outlet = "Outlet"


class LogEnumType(StrEnum):
    """
    LogEnumType is used by getLogGetLogRequest
    """

    diagnostics_log = "DiagnosticsLog"
    security_log = "SecurityLog"


class LogStatusEnumType(StrEnum):
    """
    Generic message response status
    """

    accepted = "Accepted"
    rejected = "Rejected"
    accepted_canceled = "AcceptedCanceled"


class MeasurandEnumType(StrEnum):
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


class MessageFormatEnumType(StrEnum):
    """
    Format of a message to be displayed on the display of the Charging Station.
    """

    ascii = "ASCII"
    html = "HTML"
    uri = "URI"
    utf8 = "UTF8"


class MessagePriorityEnumType(StrEnum):
    """
    Priority with which a message should be displayed on a Charging Station.
    """

    always_front = "AlwaysFront"
    in_front = "InFront"
    normal_cycle = "NormalCycle"


class MessageStateEnumType(StrEnum):
    """
    State of the Charging Station during which a message SHALL be displayed.
    """

    charging = "Charging"
    faulted = "Faulted"
    idle = "Idle"


class MessageTriggerEnumType(StrEnum):
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
    sign_v2g_certificate = "SignV2GCertificate"
    status_notification = "StatusNotification"
    transaction_event = "TransactionEvent"
    sign_combined_certificate = "SignCombinedCertificate"
    publish_firmware_status_notification = "PublishFirmwareStatusNotification"


class MonitorEnumType(StrEnum):
    """
    MonitorEnumType is used by CommonVariableMonitoringType
    """

    upper_threshold = "UpperThreshold"
    lower_threshold = "LowerThreshold"
    delta = "Delta"
    periodic = "Periodic"
    periodic_clock_aligned = "PeriodicClockAligned"


class MonitorBaseEnumType(StrEnum):
    """
    MonitoringBaseEnumType is used by
    setMonitoringBaseSetMonitoringBaseRequest
    """

    all = "All"
    factory_default = "FactoryDefault"
    hard_wired_only = "HardWiredOnly"


class MonitoringCriterionEnumType(StrEnum):
    """
    MonitoringCriterionEnumType is used by
    getMonitoringReportGetMonitoringReportRequest
    """

    threshold_monitoring = "ThresholdMonitoring"
    delta_monitoring = "DeltaMonitoring"
    periodic_monitoring = "PeriodicMonitoring"


class MutabilityEnumType(StrEnum):
    """
    MutabilityEnumType is used by CommonVariableAttributeType
    """

    read_only = "ReadOnly"
    write_only = "WriteOnly"
    read_write = "ReadWrite"


class NotifyEVChargingNeedsStatusEnumType(StrEnum):
    """
    Accepted a SASchedule will be provided momentarily.
    Rejected Servoce is Not Available
    Processing The CSMS is gathering information to provide an SASchedule.
    """

    accepted = "Accepted"
    rejected = "Rejected"
    processing = "Processing"


class OCPPInterfaceEnumType(StrEnum):
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


class OCPPTransportEnumType(StrEnum):
    """
    Enumeration of OCPP transport mechanisms.
    SOAP is currently not a valid value for OCPP 2.0.
    """

    json = "JSON"
    soap = "SOAP"


class OCPPVersionEnumType(StrEnum):
    """
    Enumeration of OCPP transport mechanisms.
    SOAP is currently not a valid value for OCPP 2.0.
    """

    ocpp12 = "OCPP12"
    ocpp15 = "OCPP15"
    ocpp16 = "OCPP16"
    ocpp20 = "OCPP20"


class OperationalStatusEnumType(StrEnum):
    """
    Requested availability change in ChangeAvailability.req.
    """

    inoperative = "Inoperative"
    operative = "Operative"


class PhaseEnumType(StrEnum):
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


class PublishFirmwareStatusEnumType(StrEnum):
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


class ReadingContextEnumType(StrEnum):
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


class ReasonEnumType(StrEnum):
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


class RecurrencyKindEnumType(StrEnum):
    """
    "Daily" The schedule restarts at the beginning of the next day.
    "Weekly" The schedule restarts at the beginning of the next week
              (defined as Monday morning)
    """

    daily = "Daily"
    weekly = "Weekly"


class RegistrationStatusEnumType(StrEnum):
    """
    Result of registration in response to BootNotification.req.
    """

    accepted = "Accepted"
    pending = "Pending"
    rejected = "Rejected"


class ReportBaseEnumType(StrEnum):
    """
    Report Base Type required in GetBaseReportRequest
    """

    configuration_inventory = "ConfigurationInventory"
    full_inventory = "FullInventory"
    summary_inventory = "SummaryInventory"


class RequestStartStopStatusEnumType(StrEnum):
    """
    The result of a RemoteStartTransaction.req or RemoteStopTransaction.req
    request.
    """

    accepted = "Accepted"
    rejected = "Rejected"


class ReservationUpdateStatusEnumType(StrEnum):
    expired = "Expired"
    removed = "Removed"


class ReserveNowStatusEnumType(StrEnum):
    """
    Status in ReserveNowResponse.
    """

    accepted = "Accepted"
    faulted = "Faulted"
    occupied = "Occupied"
    rejected = "Rejected"
    unavailable = "Unavailable"


class ResetStatusEnumType(StrEnum):
    """
    Result of Reset.req
    """

    accepted = "Accepted"
    rejected = "Rejected"
    scheduled = "Scheduled"


class ResetEnumType(StrEnum):
    """
    Type of reset requested by Reset.req
    """

    immediate = "Immediate"
    on_idle = "OnIdle"


class SendLocalListStatusEnumType(StrEnum):
    """
    Type of update for a SendLocalList Request.
    """

    accepted = "Accepted"
    failed = "Failed"
    version_mismatch = "VersionMismatch"


class SetMonitoringStatusEnumType(StrEnum):
    """
    Status in SetVariableMonitoringResponse
    """

    accepted = "Accepted"
    unknown_component = "UnknownComponent"
    unknown_variable = "UnknownVariable"
    unsupported_monitor_type = "UnsupportedMonitorType"
    rejected = "Rejected"
    duplicate = "Duplicate"


class SetNetworkProfileStatusEnumType(StrEnum):
    """
    Status in SetNetworkProfileResponse
    """

    accepted = "Accepted"
    rejected = "Rejected"
    failed = "Failed"


class SetVariableStatusEnumType(StrEnum):
    """
    Status in ChangeConfigurationResponse.
    """

    accepted = "Accepted"
    rejected = "Rejected"
    unknown_component = "UnknownComponent"
    unknown_variable = "UnknownVariable"
    not_supported_attribute_type = "NotSupportedAttributeType"
    reboot_required = "RebootRequired"


class TransactionEventEnumType(StrEnum):
    """
    Type of Event in TransactionEventRequest
    """

    ended = "Ended"
    started = "Started"
    updated = "Updated"


class TriggerMessageStatusEnumType(StrEnum):
    """
    Status in TriggerMessageResponse.
    """

    accepted = "Accepted"
    rejected = "Rejected"
    not_implemented = "NotImplemented"


class TriggerReasonEnumType(StrEnum):
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


class TxStartStopPointEnumType(StrEnum):
    """
    The values allowed for the TxStartPoint and TxStopPoint variables.
    """

    authorized = "Authorized"
    data_signed = "DataSigned"
    energy_transfer = "EnergyTransfer"
    ev_connected = "EVConnected"
    parking_bay_occupancy = "ParkingBayOccupancy"
    power_path_closed = "PowerPathClosed"


class UnlockStatusEnumType(StrEnum):
    """
    Status in response to UnlockConnector.req.
    """

    unlocked = "Unlocked"
    unlock_failed = "UnlockFailed"
    ongoing_authorized_transaction = "OngoingAuthorizedTransaction"
    unknown_connector = "UnknownConnector"


class UnpublishFirmwareStatusEnumType(StrEnum):
    """
    Status for when unpublishing a Firmware (used by UnpublishFirmwareResponse)
    """

    download_ongoing = "DownloadOngoing"
    no_firmware = "NoFirmware"
    unpublished = "Unpublished"


class UpdateFirmwareStatusEnumType(StrEnum):
    """
    Generic message response status for UpdateFirmwareResponse
    """

    accepted = "Accepted"
    rejected = "Rejected"
    accepted_canceled = "AcceptedCanceled"
    invalid_certificate = "InvalidCertificate"
    revoked_certificate = "RevokedCertificate"


class UpdateEnumType(StrEnum):
    """
    Type of update for a SendLocalList Request.
    """

    differential = "Differential"
    full = "Full"


class UploadLogStatusEnumType(StrEnum):
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


class VPNEnumType(StrEnum):
    """
    Enumeration of VPN Types used in SetNetworkProfileRequest.VPNType
    """

    ikev2 = "IKEv2"
    ipsec = "IPSec"
    l2tp = "L2TP"
    pptp = "PPTP"


# DataTypes


class StandardizedUnitsOfMeasureType(StrEnum):
    """
    Allowable values of the optional "unit" field of a Value element, as used
    in MeterValues.req and StopTransaction.req messages. Default value of
    "unit" is always "Wh". Also used in component/variables -
    specifically the unit in variableCharacteristics.
    """

    asu = "ASU"
    b = "B"
    db = "dB"
    dbm = "dBm"
    deg = "Deg"
    hz = "Hz"
    lx = "lx"
    m = "m"
    ms2 = "ms2"
    n = "N"
    ohm = "Ohm"
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


class StatusInfoReasonType(StrEnum):
    """
    Standardized reason codes for StatusInfo defined in Appendix 5. v1.3
    """

    cs_not_accepted = "CSNotAccepted"
    duplicate_profile = "DuplicateProfile"
    duplicate_request_id = "DuplicateRequestId"
    fixed_cable = "FixedCable"
    fw_update_in_progress = "FwUpdateInProgress"
    internal_error = "InternalError"
    invalid_certificate = "InvalidCertificate"
    invalid_csr = "InvalidCSR"
    invalid_id_token = "InvalidIdToken"
    invalid_message_sequence = "InvalidMessageSeq"
    invalid_profile = "InvalidProfile"
    invalid_schedule = "InvalidSchedule"
    invalid_stack_level = "InvalidStackLevel"
    invalid_url = "InvalidURL"
    invalid_value = "InvalidValue"
    missing_device_model_info = "MissingDeviceModelInfo"
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
    value_too_high = "ValueTooHigh"
    value_too_low = "ValueTooLow"
    value_zero_not_allowed = "ValueZeroNotAllowed"
    write_only = "WriteOnly"


class SecurityEventType(StrEnum):
    """
    Security Events as listed in Appendices (Appendix 1. Security Events) v1.3
    """

    firmware_updated = "FirmwareUpdated"
    failed_to_authenticate_at_csms = "FailedToAuthenticateAtCsms"
    csms_failed_to_authenticate = "CsmsFailedToAuthenticate"
    setting_system_time = "SettingSystemTime"
    startup_of_the_device = "StartupOfTheDevice"
    reset_or_reboot = "ResetOrReboot"
    security_log_was_cleared = "SecurityLogWasCleared"
    reconfiguration_of_security_parameters = "ReconfigurationOfSecurityParameters"
    memory_exhaustion = "MemoryExhaustion"
    invalid_messages = "InvalidMessages"
    attempted_replay_attacks = "AttemptedReplayAttacks"
    tamper_detection_activated = "TamperDetectionActivated"
    invalid_firmware_signature = "InvalidFirmwareSignature"
    invalid_firmware_signing_certificate = "InvalidFirmwareSigningCertificate"
    invalid_csms_certificate = "InvalidCsmsCertificate"
    invalid_charging_station_certificate = "InvalidChargingStationCertificate"
    invalid_tls_version = "InvalidTLSVersion"
    invalid_tls_cipher_suite = "InvalidTLSCipherSuite"
    maintenance_login_accepted = "MaintenanceLoginAccepted"
    maintenance_login_failed = "MaintenanceLoginFailed"


class ControllerComponentName(StrEnum):
    """
    Referenced Controller Components (Logical Components)
    Sourced from ocpp 2.0.1 part 2 appendices 3.1 v1.3, in
    appendices_CSV_v1.3.zip dm_components_vars.csv and components.csv.
    """

    aligned_data_ctrlr = "AlignedDataCtrlr"
    auth_cache_ctrlr = "AuthCacheCtrlr"
    auth_ctrlr = "AuthCtrlr"
    chademo_ctrlr = "CHAdeMOCtrlr"
    clock_ctrlr = "ClockCtrlr"
    customization_ctrlr = "CustomizationCtrlr"
    device_data_ctrlr = "DeviceDataCtrlr"
    display_message_ctrlr = "DisplayMessageCtrlr"
    iso15118_ctrlr = "ISO15118Ctrlr"
    local_auth_list_ctrlr = "LocalAuthListCtrlr"
    monitoring_ctrlr = "MonitoringCtrlr"
    ocpp_comm_ctrlr = "OCPPCommCtrlr"
    reservation_ctrlr = "ReservationCtrlr"
    sampled_data_ctrlr = "SampledDataCtrlr"
    security_ctrlr = "SecurityCtrlr"
    smart_charging_ctrlr = "SmartChargingCtrlr"
    tariff_cost_ctrlr = "TariffCostCtrlr"
    tx_ctrlr = "TxCtrlr"


class PhysicalComponentName(StrEnum):
    """
    Referenced Physical Components - sourced from dm_components_vars.csv.
    Note: specific variables for each component are sourced from a union of
    ocpp 2.0.1 part 2 appendices 3.2 v1.3 and dm_components_vars.csv
    from appendices_CSV_v1.3.zip. That is for all Physical Components in
    section 3.2. expressed in this module as enums,
    e.g. the variables of ControllerVariableName enum
    """

    access_barrier = "AccessBarrier"
    ac_dc_converter = "AcDcConverter"
    ac_phase_selector = "AcPhaseSelector"
    actuator = "Actuator"
    air_cooling_system = "AirCoolingSystem"
    area_ventilation = "AreaVentilation"
    bay_occupancy_sensor = "BayOccupancySensor"
    beacon_lighting = "BeaconLighting"
    cable_breakaway_sensor = "CableBreakawaySensor"
    case_access_sensor = "CaseAccessSensor"
    charging_station = "ChargingStation"
    charging_status_indicator = "ChargingStatusIndicator"
    connected_ev = "ConnectedEV"
    connector = "Connector"
    connector_holster_release = "ConnectorHolsterRelease"
    connector_holster_sensor = "ConnectorHolsterSensor"
    connector_plug_retention_lock = "ConnectorPlugRetentionLock"
    connector_protection_release = "ConnectorProtectionRelease"
    controller = "Controller"
    control_metering = "ControlMetering"
    cppwm_controller = "CPPWMController"
    data_link = "DataLink"
    display = "Display"
    distribution_panel = "DistributionPanel"
    electrical_feed = "ElectricalFeed"
    elv_supply = "ELVSupply"
    emergency_stop_sensor = "EmergencyStopSensor"
    environmental_lighting = "EnvironmentalLighting"
    ev_retention_lock = "EVRetentionLock"
    evse = "EVSE"
    external_temperature_sensor = "ExternalTemperatureSensor"
    fiscal_metering = "FiscalMetering"
    flood_sensor = "FloodSensor"
    ground_isolation_protection = "GroundIsolationProtection"
    heater = "Heater"
    humidity_sensor = "HumiditySensor"
    light_sensor = "LightSensor"
    liquid_cooling_system = "LiquidCoolingSystem"
    local_availability_sensor = "LocalAvailabilitySensor"
    local_controller = "LocalController"
    local_energy_storage = "LocalEnergyStorage"
    over_current_protection = "OverCurrentProtection"
    over_current_protection_recloser = "OverCurrentProtectionRecloser"
    power_contactor = "PowerContactor"
    rcd = "RCD"
    rcd_recloser = "RCDRecloser"
    real_time_clock = "RealTimeClock"
    shock_sensor = "ShockSensor"
    spaces_count_signage = "SpacesCountSignage"
    switch = "Switch"
    temperature_sensor = "TemperatureSensor"
    tilt_sensor = "TiltSensor"
    token_reader = "TokenReader"
    ui_input = "UIInput"
    upstream_protection_trigger = "UpstreamProtectionTrigger"
    vehicle_id_sensor = "VehicleIdSensor"


class StandardizedVariableName(StrEnum):
    """
    Variable names where the component type is non-specific
    derived from a union of in appendices_CSV_v1.3.zip,
    dm_components_vars.csv (Generic) and variables.csv
    """

    ac_current = "ACCurrent"
    active = "Active"
    ac_voltage = "ACVoltage"
    allow_reset = "AllowReset"
    angle = "Angle"
    attempts = "Attempts"
    availability_state = "AvailabilityState"
    available = "Available"
    certificate = "Certificate"
    charge_protocol = "ChargeProtocol"
    charging_complete_bulk = "ChargingCompleteBulk"
    charging_complete_full = "ChargingCompleteFull"
    charging_time = "ChargingTime"
    color = "Color"
    complete = "Complete"
    connected_time = "ConnectedTime"
    connector_type = "ConnectorType"
    count = "Count"
    currency = "Currency"
    current_imbalance = "CurrentImbalance"
    data_text = "DataText"
    date_time = "DateTime"
    dc_current = "DCCurrent"
    dc_voltage = "DCVoltage"
    departure_time = "DepartureTime"
    ec_variant = "ECVariant"
    enabled = "Enabled"
    energy = "Energy"
    energy_capacity = "EnergyCapacity"
    energy_export = "EnergyExport"
    energy_export_register = "EnergyExportRegister"
    energy_import = "EnergyImport"
    energy_import_register = "EnergyImportRegister"
    entries = "Entries"
    evse_id = "EvseId"
    fallback = "Fallback"
    fan_speed = "FanSpeed"
    firmware_version = "FirmwareVersion"
    force = "Force"
    formats = "Formats"
    frequency = "Frequency"
    fuse_rating = "FuseRating"
    height = "Height"
    humidity = "Humidity"
    hysteresis = "Hysteresis"
    iccid = "ICCID"
    impedance = "Impedance"
    imsi = "IMSI"
    interval = "Interval"
    iso15118_evse_id = "ISO15118EvseId"
    length = "Length"
    light = "Light"
    manufacturer = "Manufacturer"
    message = "Message"
    minimum_status_duration = "MinimumStatusDuration"
    mode = "Mode"
    model = "Model"
    network_address = "NetworkAddress"
    operated = "Operated"
    operating_times = "OperatingTimes"
    overload = "Overload"
    percent = "Percent"
    phase_rotation = "PhaseRotation"
    post_charging_time = "PostChargingTime"
    power = "Power"
    problem = "Problem"
    protecting = "Protecting"
    remaining_time_bulk = "RemainingTimeBulk"
    remaining_time_full = "RemainingTimeFull"
    secc_id = "SeccId"
    serial_number = "SerialNumber"
    signal_strength = "SignalStrength"
    state = "State"
    state_of_charge = "StateOfCharge"
    state_of_charge_bulk = "StateOfChargeBulk"
    storage = "Storage"
    supply_phases = "SupplyPhases"
    suspending = "Suspending"
    suspension = "Suspension"
    temperature = "Temperature"
    time = "Time"
    time_offset = "TimeOffset"
    timeout = "Timeout"
    token = "Token"
    token_type = "TokenType"
    tries = "Tries"
    tripped = "Tripped"
    vehicle_id = "VehicleId"
    version_date = "VersionDate"
    version_number = "VersionNumber"
    voltage_imbalance = "VoltageImbalance"


class AlignedDataCtrlrVariableName(StrEnum):
    """
    Variable names where the component type is AlignedDataCtrlr
    See ControllerComponentName for referenced logical component
    """

    available = "Available"
    enabled = "Enabled"
    interval = "Interval"
    measurands = "Measurands"
    send_during_idle = "SendDuringIdle"
    sign_readings = "SignReadings"
    tx_ended_interval = "TxEndedInterval"
    tx_ended_measurands = "TxEndedMeasurands"


class AuthCacheCtrlrVariableName(StrEnum):
    """
    Variable names where the component type is AuthCacheCtrlr
    See ControllerComponentName for referenced logical component
    """

    available = "Available"
    enabled = "Enabled"
    life_time = "LifeTime"
    policy = "Policy"
    storage = "Storage"
    disable_post_authorize = "DisablePostAuthorize"


class AuthCtrlrVariableName(StrEnum):
    """
    Variable names where the component type is AuthCtrlr
    See ControllerComponentName for referenced logical component
    """

    additional_info_items_per_message = "AdditionalInfoItemsPerMessage"
    authorize_remote_start = "AuthorizeRemoteStart"
    enabled = "Enabled"
    local_authorize_offline = "LocalAuthorizeOffline"
    local_pre_authorize = "LocalPreAuthorize"
    master_pass_group_id = "MasterPassGroupId"
    offline_tx_for_unknown_id_enabled = "OfflineTxForUnknownIdEnabled"
    disable_remote_authorization = "DisableRemoteAuthorization"


class CHAdeMOCtrlrVariableName(StrEnum):
    """
    Variable names where the component type is CHAdeMOCtrlr
    See ControllerComponentName for referenced logical component
    """

    enabled = "Enabled"
    active = "Active"
    complete = "Complete"
    tripped = "Tripped"
    problem = "Problem"
    selftest_active = "SelftestActive"
    selftest_active_set = "SelftestActive(Set)"
    chademo_protocol_number = "CHAdeMOProtocolNumber"
    vehicle_status = "VehicleStatus"
    dynamic_control = "DynamicControl"
    high_current_control = "HighCurrentControl"
    high_voltage_control = "HighVoltageControl"
    auto_manufacturer_code = "AutoManufacturerCode"


class ClockCtrlrVariableName(StrEnum):
    """
    Variable names where the component type is ClockCtrlr
    See ControllerComponentName for referenced logical component
    """

    date_time = "DateTime"
    next_time_offset_transition_date_time = "NextTimeOffsetTransitionDateTime"
    ntp_server_uri = "NtpServerUri"
    ntp_source = "NtpSource"
    time_adjustment_reporting_threshold = "TimeAdjustmentReportingThreshold"
    time_offset = "TimeOffset"
    time_source = "TimeSource"
    time_zone = "TimeZone"


class CustomizationCtrlrVariableName(StrEnum):
    """
    Variable names where the component type is CustomizationCtrlr
    See ControllerComponentName for referenced logical component
    """

    custom_implementation_enabled = "CustomImplementationEnabled"


class DeviceDataCtrlrVariableName(StrEnum):
    """
    Variable names where the component type is DeviceDataCtrlr
    See ControllerComponentName for referenced logical component
    """

    bytes_per_message = "BytesPerMessage"
    configuration_value_size = "ConfigurationValueSize"
    items_per_message = "ItemsPerMessage"
    reporting_value_size = "ReportingValueSize"
    value_size = "ValueSize"


class DeviceDataCtrlrInstanceName(StrEnum):
    """
    Instance names where the component type is DeviceDataCtrlr
    """

    get_report = "GetReport"
    get_variables = "GetVariables"
    set_variables = "SetVariables"


class DisplayMessageCtrlrVariableName(StrEnum):
    """
    Variable names where the component type is DisplayMessageCtrlr
    See ControllerComponentName for referenced logical component
    """

    available = "Available"
    display_messages = "DisplayMessages"
    enabled = "Enabled"
    personal_message_size = "PersonalMessageSize"
    supported_formats = "SupportedFormats"
    supported_priorities = "SupportedPriorities"


class ISO15118CtrlrVariableName(StrEnum):
    """
    Variable names where the component type is ISO15118Ctrlr
    See ControllerComponentName for referenced logical component
    """

    active = "Active"
    enabled = "Enabled"
    central_contract_validation_allowed = "CentralContractValidationAllowed"
    complete = "Complete"
    contract_validation_offline = "ContractValidationOffline"
    secc_id = "SeccId"
    selftest_active = "SelftestActive"
    selftest_active_set = "SelftestActive(Set)"
    max_schedule_entries = "MaxScheduleEntries"
    requested_energy_transfer_mode = "RequestedEnergyTransferMode"
    request_metering_receipt = "RequestMeteringReceipt"
    country_name = "CountryName"
    organization_name = "OrganizationName"
    pnc_enabled = "PnCEnabled"
    problem = "Problem"
    tripped = "Tripped"
    v2g_certificate_installation_enabled = "V2GCertificateInstallationEnabled"
    contract_certificate_installation_enabled = "ContractCertificateInstallationEnabled"


class LocalAuthListCtrlrVariableName(StrEnum):
    """
    Variable names where the component type is LocalAuthListCtrlr
    See ControllerComponentName for referenced logical component
    """

    available = "Available"
    bytes_per_message = "BytesPerMessage"
    enabled = "Enabled"
    entries = "Entries"
    items_per_message = "ItemsPerMessage"
    storage = "Storage"
    disable_post_authorize = "DisablePostAuthorize"


class MonitoringCtrlrVariableName(StrEnum):
    """
    Variable names where the component type is MonitoringCtrlr
    See ControllerComponentName for referenced logical component
    """

    available = "Available"
    bytes_per_message = "BytesPerMessage"
    enabled = "Enabled"
    items_per_message = "ItemsPerMessage"
    offline_queuing_severity = "OfflineQueuingSeverity"
    monitoring_base = "MonitoringBase"
    monitoring_level = "MonitoringLevel"
    active_monitoring_base = "ActiveMonitoringBase"
    active_monitoring_level = "ActiveMonitoringLevel"


class MonitoringCtrlrInstanceName(StrEnum):
    """
    Instance names where the component type is MonitoringCtrlr
    """

    clear_variable_monitoring = "ClearVariableMonitoring"
    set_variable_monitoring = "SetVariableMonitoring"


class OCPPCommCtrlrVariableName(StrEnum):
    """
    Variable names where the component type is OCPPCommCtrlr
    See ControllerComponentName for referenced logical component
    """

    active_network_profile = "ActiveNetworkProfile"
    file_transfer_protocols = "FileTransferProtocols"
    heartbeat_interval = "HeartbeatInterval"
    message_timeout = "MessageTimeout"
    message_attempt_interval = "MessageAttemptInterval"
    message_attempts = "MessageAttempts"
    minimum_status_duration = "MinimumStatusDuration"
    network_configuration_priority = "NetworkConfigurationPriority"
    network_profile_connection_attempts = "NetworkProfileConnectionAttempts"
    offline_threshold = "OfflineThreshold"
    public_key_with_signed_meter_value = "PublicKeyWithSignedMeterValue"
    queue_all_messages = "QueueAllMessages"
    reset_retries = "ResetRetries"
    retry_back_off_random_range = "RetryBackOffRandomRange"
    retry_back_off_repeat_times = "RetryBackOffRepeatTimes"
    retry_back_off_wait_minimum = "RetryBackOffWaitMinimum"
    unlock_on_ev_side_disconnect = "UnlockOnEVSideDisconnect"
    web_socket_ping_interval = "WebSocketPingInterval"
    field_length = "FieldLength"


class OCPPCommCtrlrInstanceName(StrEnum):
    """
    Instance names where the component type is OCPPCommCtrlr
    """

    default = "Default"
    transaction_event = "TransactionEvent"


class ReservationCtrlrVariableName(StrEnum):
    """
    Variable names where the component type is ReservationCtrlr
    See ControllerComponentName for referenced logical component
    """

    available = "Available"
    enabled = "Enabled"
    non_evse_specific = "NonEvseSpecific"


class SampledDataCtrlrVariableName(StrEnum):
    """
    Variable names where the component type is SampledDataCtrlr
    See ControllerComponentName for referenced logical component
    """

    available = "Available"
    enabled = "Enabled"
    sign_readings = "SignReadings"
    tx_ended_interval = "TxEndedInterval"
    tx_ended_measurands = "TxEndedMeasurands"
    tx_started_measurands = "TxStartedMeasurands"
    tx_updated_interval = "TxUpdatedInterval"
    tx_updated_measurands = "TxUpdatedMeasurands"
    register_values_without_phases = "RegisterValuesWithoutPhases"


class SecurityCtrlrVariableName(StrEnum):
    """
    Variable names where the component type is SampledDataCtrlr
    See ControllerComponentName for referenced logical component
    """

    additional_root_certificate_check = "AdditionalRootCertificateCheck"
    basic_auth_password = "BasicAuthPassword"
    certificate_entries = "CertificateEntries"
    cert_signing_repeat_times = "CertSigningRepeatTimes"
    cert_signing_wait_minimum = "CertSigningWaitMinimum"
    identity = "Identity"
    max_certificate_chain_size = "MaxCertificateChainSize"
    organization_name = "OrganizationName"
    security_profile = "SecurityProfile"


class SmartChargingCtrlrVariableName(StrEnum):
    """
    Variable names where the component type is SmartChargingCtrlr
    See ControllerComponentName for referenced logical component
    """

    ac_phase_switching_supported = "ACPhaseSwitchingSupported"
    available = "Available"
    enabled = "Enabled"
    entries = "Entries"
    external_control_signals_enabled = "ExternalControlSignalsEnabled"
    limit_change_significance = "LimitChangeSignificance"
    notify_charging_limit_with_schedules = "NotifyChargingLimitWithSchedules"
    periods_per_schedule = "PeriodsPerSchedule"
    phases_3to1 = "Phases3to1"
    profile_stack_level = "ProfileStackLevel"
    rate_unit = "RateUnit"


class SmartChargingCtrlrInstanceName(StrEnum):
    """
    Instance names where the component type is SmartChargingCtrlr
    """

    charging_profiles = "ChargingProfiles"


class TariffCostCtrlrVariableName(StrEnum):
    """
    Variable names where the component type is TariffCostCtrlr
    See ControllerComponentName for referenced logical component
    """

    available = "Available"
    currency = "Currency"
    enabled = "Enabled"
    tariff_fallback_message = "TariffFallbackMessage"
    total_cost_fallback_message = "TotalCostFallbackMessage"


class TariffCostCtrlrInstanceName(StrEnum):
    """
    Instance names where the component type is TariffCostCtrlr
    """

    tariff = "Tariff"
    cost = "Cost"


class TxCtrlrVariableName(StrEnum):
    """
    Instance names where the component type is TxCtrlr
    See ControllerComponentName for referenced logical component
    """

    ev_connection_time_out = "EVConnectionTimeOut"
    max_energy_on_invalid_id = "MaxEnergyOnInvalidId"
    stop_tx_on_ev_side_disconnect = "StopTxOnEVSideDisconnect"
    stop_tx_on_invalid_id = "StopTxOnInvalidId"
    tx_before_accepted_enabled = "TxBeforeAcceptedEnabled"
    tx_start_point = "TxStartPoint"
    tx_stop_point = "TxStopPoint"


class AccessBarrierVariableName(StrEnum):
    """
    Variable names where the component type is AccessBarrier
    See PhysicalComponentName for referenced physical component
    """

    enabled = "Enabled"
    active = "Active"
    problem = "Problem"


class AcDcConverterVariableName(StrEnum):
    """
    Variable names where the component type is AcDcConverter
    See PhysicalComponentName for referenced physical component
    """

    dc_current = "DCCurrent"
    dc_voltage = "DCVoltage"
    enabled = "Enabled"
    fan_speed = "FanSpeed"
    overload = "Overload"
    power = "Power"
    problem = "Problem"
    temperature = "Temperature"
    tripped = "Tripped"


class AcPhaseSelectorVariableName(StrEnum):
    """
    Variable names where the component type is AcPhaseSelector
    See PhysicalComponentName for referenced physical component
    """

    active = "Active"
    enabled = "Enabled"
    phase_rotation = "PhaseRotation"
    problem = "Problem"


class ActuatorVariableName(StrEnum):
    """
    Variable names where the component type is Actuator
    See PhysicalComponentName for referenced physical component
    """

    active = "Active"
    enabled = "Enabled"
    problem = "Problem"
    state = "State"


class AirCoolingSystemVariableName(StrEnum):
    """
    Variable names where the component type is AirCoolingSystem
    See PhysicalComponentName for referenced physical component
    """

    active = "Active"
    enabled = "Enabled"
    problem = "Problem"
    fan_speed = "FanSpeed"


class AreaVentilationVariableName(StrEnum):
    """
    Variable names where the component type is AreaVentilation
    See PhysicalComponentName for referenced physical component
    """

    active = "Active"
    enabled = "Enabled"
    problem = "Problem"
    fan_speed = "FanSpeed"


class BayOccupancySensorVariableName(StrEnum):
    """
    Variable names where the component type is BayOccupancySensor
    See PhysicalComponentName for referenced physical component
    """

    active = "Active"
    enabled = "Enabled"
    percent = "Percent"


class BeaconLightingVariableName(StrEnum):
    """
    Variable names where the component type is BeaconLighting
    See PhysicalComponentName for referenced physical component
    """

    active = "Active"
    color = "Color"
    enabled = "Enabled"
    enabled_set = "Enabled(Set)"
    percent = "Percent"
    percent_set = "Percent(Set)"
    power = "Power"
    problem = "Problem"


class CableBreakawaySensorVariableName(StrEnum):
    """
    Variable names where the component type is CableBreakawaySensor
    See PhysicalComponentName for referenced physical component
    """

    active = "Active"
    enabled = "Enabled"
    tripped = "Tripped"


class CaseAccessSensorVariableName(StrEnum):
    """
    Variable names where the component type is CaseAccessSensor
    See PhysicalComponentName for referenced physical component
    """

    active = "Active"
    enabled = "Enabled"
    enabled_set = "Enabled(Set)"
    problem = "Problem"
    tripped = "Tripped"


class ChargingStationVariableName(StrEnum):
    """
    Variable names where the component type is ChargingStation
    See PhysicalComponentName for referenced physical component
    """

    ac_current = "ACCurrent"
    ac_voltage = "ACVoltage"
    ac_voltage_max_limit = "ACVoltage(MaxLimit)"
    allow_new_sessions_pending_firmware_update = "AllowNewSessionsPendingFirmwareUpdate"
    available = "Available"
    availability_state = "AvailabilityState"
    charge_protocol = "ChargeProtocol"
    current_imbalance = "CurrentImbalance"
    ec_variant = "ECVariant"
    enabled = "Enabled"
    model = "Model"
    operating_times = "OperatingTimes"
    overload = "Overload"
    phase_rotation = "PhaseRotation"
    power = "Power"
    power_max_limit = "Power(MaxLimit)"
    problem = "Problem"
    serial_number = "SerialNumber"
    supply_phases = "SupplyPhases"
    supply_phases_max_limit = "SupplyPhases(MaxLimit)"
    tripped = "Tripped"
    vendor_name = "VendorName"
    voltage_imbalance = "VoltageImbalance"


class ChargingStatusIndicatorVariableName(StrEnum):
    """
    Variable names where the component type is ChargingStatusIndicator
    See PhysicalComponentName for referenced physical component
    """

    active = "Active"
    color = "Color"


class ConnectedEVVariableName(StrEnum):
    """
    Variable names where the component type is ConnectedEV
    See PhysicalComponentName for referenced physical component
    """

    available = "Available"

    # Vehicle
    vehicle_id = "VehicleId"
    protocol_agreed = "ProtocolAgreed"
    protocol_supported_by_ev = "ProtocolSupportedByEV"

    # Voltage and current values
    ac_current_min_set = "ACCurrent.minSet"
    ac_current_max_set = "ACCurrent.maxSet"
    ac_voltage_max_set = "ACVoltage.maxSet"
    dc_current_min_set = "DCCurrent.minSet"
    dc_current_max_set = "DCCurrent.maxSet"
    dc_current_target = "DCCurrent.target"
    dc_voltage_min_set = "DCVoltage.minSet"
    dc_voltage_max_set = "DCVoltage.maxSet"
    dc_voltage_target = "DCVoltage.target"

    # Power, energy and time values
    power_max_set = "Power.maxSet"
    energy_capacity = "EnergyCapacity"
    energy_import_target = "EnergyImport.target"
    departure_time = "DepartureTime"
    remaining_time_bulk = "RemainingTimeBulk"
    remaining_time_full_max_set = "RemainingTimeFull.maxSet"
    remaining_time_full_actual = "RemainingTimeFull.actual"
    state_of_charge_bulk = "StateOfChargeBulk"
    state_of_charge_max_set = "StateOfCharge.maxSet"
    state_of_charge_actual = "StateOfCharge.actual"
    charging_complete_bulk = "ChargingCompleteBulk"
    charging_complete_full = "ChargingCompleteFull"

    # Status values
    battery_overvoltage = "BatteryOvervoltage"
    battery_undervoltage = "BatteryUndervoltage"
    charging_current_deviation = "ChargingCurrentDeviation"
    battery_temperature = "BatteryTemperature"
    voltage_deviation = "VoltageDeviation"
    charging_system_error = "ChargingSystemError"
    vehicle_shift_position = "VehicleShiftPosition"
    vehicle_charging_enabled = "VehicleChargingEnabled"
    charging_system_incompatibility = "ChargingSystemIncompatibility"
    charger_connector_lock_fault = "ChargerConnectorLockFault"


class ChargingStateVariableName(StrEnum):
    """
    Variable names where the component type is ChargingState
    """

    # Status values - ChargingState
    battery_overvoltage = "BatteryOvervoltage"
    battery_undervoltage = "BatteryUndervoltage"
    charging_current_deviation = "ChargingCurrentDeviation"
    battery_temperature = "BatteryTemperature"
    voltage_deviation = "VoltageDeviation"
    charging_system_error = "ChargingSystemError"
    vehicle_shift_position = "VehicleShiftPosition"
    vehicle_charging_enabled = "VehicleChargingEnabled"
    charging_system_incompatibility = "ChargingSystemIncompatibility"
    charger_connector_lock_fault = "ChargerConnectorLockFault"


class ConnectorVariableName(StrEnum):
    """
    Variable names where the component type is Connector
    See PhysicalComponentName for referenced physical component
    """

    availability_state = "AvailabilityState"
    available = "Available"
    charge_protocol = "ChargeProtocol"
    connector_type = "ConnectorType"
    enabled = "Enabled"
    phase_rotation = "PhaseRotation"
    problem = "Problem"
    supply_phases = "SupplyPhases"
    supply_phases_max_limit = "SupplyPhases(MaxLimit)"
    tripped = "Tripped"


class ConnectorHolsterReleaseVariableName(StrEnum):
    """
    Variable names where the component type is ConnectorHolsterRelease
    See PhysicalComponentName for referenced physical component
    """

    enabled = "Enabled"
    active = "Active"
    problem = "Problem"
    state = "State"


class ConnectorHolsterSensorVariableName(StrEnum):
    """
    Variable names where the component type is ConnectorHolsterSensor
    See PhysicalComponentName for referenced physical component
    """

    enabled = "Enabled"
    active = "Active"
    problem = "Problem"


class ConnectorPlugRetentionLockVariableName(StrEnum):
    """
    Variable names where the component type is ConnectorPlugRetentionLock
    See PhysicalComponentName for referenced physical component
    """

    enabled = "Enabled"
    active = "Active"
    problem = "Problem"
    tripped = "Tripped"
    tries = "Tries"
    tries_set_limit = "Tries(SetLimit)"
    tries_max_limit = "Tries(MaxLimit)"


class ConnectorProtectionReleaseVariableName(StrEnum):
    """
    Variable names where the component type is ConnectorProtectionRelease
    See PhysicalComponentName for referenced physical component
    """

    enabled = "Enabled"
    active = "Active"
    problem = "Problem"
    tripped = "Tripped"


class ControllerVariableName(StrEnum):
    """
    Variable names where the component type is Controller
    See PhysicalComponentName for referenced physical component
    """

    active = "Active"
    ec_variant = "ECVariant"
    firmware_version = "FirmwareVersion"
    interval_heartbeat = "Interval[Heartbeat]"
    manufacturer = "Manufacturer"
    max_msg_elements = "MaxMsgElements"
    model = "Model"
    problem = "Problem"
    selftest_active = "SelftestActive"
    selftest_active_set = "SelftestActive(Set)"
    serial_number = "SerialNumber"
    version_date = "VersionDate"
    version_number = "VersionNumber"


class ControlMeteringVariableName(StrEnum):
    """
    Variable names where the component type is ControlMetering
    See PhysicalComponentName for referenced physical component
    """

    power = "Power"
    ac_current = "ACCurrent"
    dc_current = "DCCurrent"
    dc_voltage = "DCVoltage"


class CPPWMControllerVariableName(StrEnum):
    """
    Variable names where the component type is CPPWMController
    See PhysicalComponentName for referenced physical component
    """

    active = "Active"
    dc_voltage = "DCVoltage"
    enabled = "Enabled"
    percentage = "Percentage"
    problem = "Problem"
    selftest_active = "SelftestActive"
    selftest_active_set = "SelftestActive(Set)"
    state = "State"


class DataLinkVariableName(StrEnum):
    """
    Variable names where the component type is DataLink
    See PhysicalComponentName for referenced physical component
    """

    active = "Active"
    complete = "Complete"
    enabled = "Enabled"
    fallback = "Fallback"
    iccid = "ICCID"
    imsi = "IMSI"
    network_address = "NetworkAddress"
    problem = "Problem"
    signal_strength = "SignalStrength"


class DisplayVariableName(StrEnum):
    """
    Variable names where the component type is Display
    See PhysicalComponentName for referenced physical component
    """

    color = "Color"
    count_height_in_chars = "Count[HeightInChars]"
    count_width_in_chars = "Count[WidthInChars]"
    data_text_visible = "DataText[Visible]"
    enabled = "Enabled"
    problem = "Problem"
    state = "State"


class DistributionPanelVariableName(StrEnum):
    """
    Variable names where the component type is DistributionPanel
    See PhysicalComponentName for referenced physical component
    """

    charging_station = "ChargingStation"
    distribution_panel = "DistributionPanel"
    fuse = "Fuse"
    instance_name = "InstanceName"


class ElectricalFeedVariableName(StrEnum):
    """
    Variable names where the component type is ElectricalFeed
    See PhysicalComponentName for referenced physical component
    """

    ac_voltage = "ACVoltage"
    active = "Active"
    dc_voltage = "DCVoltage"
    enabled = "Enabled"
    energy = "Energy"
    phase_rotation = "PhaseRotation"
    power = "Power"
    power_type = "PowerType"
    problem = "Problem"
    supply_phases = "SupplyPhases"


class ELVSupplyVariableName(StrEnum):
    """
    Variable names where the component type is ELVSupply
    See PhysicalComponentName for referenced physical component
    """

    energy_import_register = "EnergyImportRegister"
    fallback = "Fallback"
    fallback_max_limit = "Fallback(MaxLimit)"
    power = "Power"
    power_max_limit = "Power(MaxLimit)"
    state_of_charge = "StateOfCharge"
    time = "Time"


class EmergencyStopSensorVariableName(StrEnum):
    """
    Variable names where the component type is EmergencyStopSensor
    See PhysicalComponentName for referenced physical component
    """

    enabled = "Enabled"
    active = "Active"
    tripped = "Tripped"


class EnvironmentalLightingVariableName(StrEnum):
    """
    Variable names where the component type is EnvironmentalLighting
    See PhysicalComponentName for referenced physical component
    """

    active = "Active"
    color = "Color"
    enabled = "Enabled"
    enabled_set = "Enabled(Set)"
    percent = "Percent"
    percent_set = "Percent(Set)"
    power = "Power"
    problem = "Problem"


class EVRetentionLockVariableName(StrEnum):
    """
    Variable names where the component type is EVRetentionLock
    See PhysicalComponentName for referenced physical component
    """

    active = "Active"
    complete = "Complete"
    enabled = "Enabled"
    problem = "Problem"


class EVSEVariableName(StrEnum):
    """
    Variable names where the component type is EVSE
    See PhysicalComponentName for referenced physical component
    """

    ac_current = "ACCurrent"
    ac_voltage = "ACVoltage"
    available = "Available"
    availability_state = "AvailabilityState"
    allow_reset = "AllowReset"
    charge_protocol = "ChargeProtocol"
    charging_time = "ChargingTime"
    count_charging_profiles_max_limit = "Count[ChargingProfiles](MaxLimit)"
    count_charging_profiles = "Count[ChargingProfiles]"
    current_imbalance = "CurrentImbalance"
    dc_current = "DCCurrent"
    dc_voltage = "DCVoltage"
    enabled = "Enabled"
    evse_id = "EvseId"
    iso15118_evse_id = "ISO15118EvseId"
    overload = "Overload"
    phase_rotation = "PhaseRotation"
    post_charging_time = "PostChargingTime"
    power = "Power"
    problem = "Problem"
    supply_phases = "SupplyPhases"
    tripped = "Tripped"
    voltage_imbalance = "VoltageImbalance"


class ExternalTemperatureSensorVariableName(StrEnum):
    """
    Variable names where the component type is ExternalTemperatureSensor
    See PhysicalComponentName for referenced physical component
    """

    active = "Active"
    problem = "Problem"
    temperature = "Temperature"


class FiscalMeteringVariableName(StrEnum):
    """
    Variable names where the component type is FiscalMetering
    See PhysicalComponentName for referenced physical component
    """

    problem = "Problem"
    certificate = "Certificate"
    ec_variant = "ECVariant"
    energy_export = "EnergyExport"
    energy_export_register = "EnergyExportRegister"
    energy_import = "EnergyImport"
    energy_import_register = "EnergyImportRegister"
    manufacturer_ct = "Manufacturer[CT]"
    manufacturer_meter = "Manufacturer[Meter]"
    model_ct = "Model[CT]"
    model_meter = "Model[Meter]"
    options_set_meter_value_aligned_data = "OptionsSet[MeterValueAlignedData]"
    options_set_txn_stopped_aligned_data = "OptionsSet[TxnStoppedAlignedData]"
    serial_number_ct = "SerialNumber[CT]"
    serial_number_meter = "SerialNumber[Meter]"


class FloodSensorVariableName(StrEnum):
    """
    Variable names where the component type is FloodSensor
    See PhysicalComponentName for referenced physical component
    """

    active = "Active"
    enabled = "Enabled"
    height = "Height"
    percent = "Percent"
    tripped = "Tripped"


class GroundIsolationProtectionVariableName(StrEnum):
    """
    Variable names where the component type is GroundIsolationProtection
    See PhysicalComponentName for referenced physical component
    """

    active = "Active"
    complete = "Complete"
    enabled = "Enabled"
    impedance = "Impedance"
    problem = "Problem"


class HeaterVariableName(StrEnum):
    """
    Variable names where the component type is Heater
    See PhysicalComponentName for referenced physical component
    """

    active = "Active"
    enabled = "Enabled"
    problem = "Problem"
    tripped = "Tripped"
    power = "Power"
    power_max_limit = "Power(MaxLimit)"
    power_max_set = "Power(MaxSet)"
    temperature_min_set = "Temperature(MinSet)"
    temperature_max_set = "Temperature(MaxSet)"


class HumiditySensorVariableName(StrEnum):
    """
    Variable names where the component type is HumiditySensor
    See PhysicalComponentName for referenced physical component
    """

    enabled = "Enabled"
    humidity = "Humidity"
    problem = "Problem"


class LightSensorVariableName(StrEnum):
    """
    Variable names where the component type is LightSensor
    See PhysicalComponentName for referenced physical component
    """

    enabled = "Enabled"
    light = "Light"
    problem = "Problem"


class LiquidCoolingSystemVariableName(StrEnum):
    """
    Variable names where the component type is LiquidCoolingSystem
    See PhysicalComponentName for referenced physical component
    """

    active = "Active"
    enabled = "Enabled"
    problem = "Problem"
    temperature = "Temperature"


class LocalAvailabilitySensorVariableName(StrEnum):
    """
    Variable names where the component type is LocalAvailabilitySensor
    See PhysicalComponentName for referenced physical component
    """

    active = "Active"
    enabled = "Enabled"
    problem = "Problem"


class LocalControllerVariableName(StrEnum):
    """
    Variable names where the component type is LocalController
    See PhysicalComponentName for referenced physical component
    """

    charging_station = "ChargingStation"
    distribution_panel = "DistributionPanel"
    ec_variant = "ECVariant"
    enabled = "Enabled"
    identity = "Identity"
    manufacturer = "Manufacturer"
    model = "Model"
    problem = "Problem"
    serial_number = "SerialNumber"
    tripped = "Tripped"


class LocalEnergyStorageVariableName(StrEnum):
    """
    Variable names where the component type is LocalEnergyStorage
    See PhysicalComponentName for referenced physical component
    """

    energy_capacity = "EnergyCapacity"
    identity = "Identity"


class OverCurrentProtectionVariableName(StrEnum):
    """
    Variable names where the component type is OverCurrentProtection
    See PhysicalComponentName for referenced physical component
    """

    ac_current = "ACCurrent"
    active = "Active"
    operated = "Operated"


class OverCurrentProtectionRecloserVariableName(StrEnum):
    """
    Variable names where the component type is OverCurrentProtectionRecloser
    See PhysicalComponentName for referenced physical component
    """

    active = "Active"
    active_set = "Active(Set)"
    enabled = "Enabled"
    complete = "Complete"
    problem = "Problem"
    mode = "Mode"
    tries = "Tries"
    tries_set_limit = "Tries(SetLimit)"
    tries_max_limit = "Tries(MaxLimit)"


class PowerContactorVariableName(StrEnum):
    """
    Variable names where the component type is PowerContactor
    See PhysicalComponentName for referenced physical component
    """

    active = "Active"
    problem = "Problem"
    tripped = "Tripped"


class RCDVariableName(StrEnum):
    """
    Variable names where the component type is RCD
    See PhysicalComponentName for referenced physical component
    """

    operated = "Operated"
    tripped = "Tripped"


class RCDRecloserVariableName(StrEnum):
    """
    Variable names where the component type is RCDRecloser
    See PhysicalComponentName for referenced physical component
    """

    active = "Active"
    active_set = "Active(Set)"
    complete = "Complete"
    enabled = "Enabled"
    problem = "Problem"
    tries = "Tries"
    tries_max_limit = "Tries(MaxLimit)"
    tries_set_limit = "Tries(SetLimit)"


class RealTimeClockVariableName(StrEnum):
    """
    Variable names where the component type is RealTimeClock
    See PhysicalComponentName for referenced physical component
    """

    active = "Active"
    dc_voltage = "DCVoltage"
    fallback = "Fallback"
    fallback_max_limit = "Fallback(MaxLimit)"
    problem = "Problem"


class ShockSensorVariableName(StrEnum):
    """
    Variable names where the component type is ShockSensor
    See PhysicalComponentName for referenced physical component
    """

    active = "Active"
    enabled = "Enabled"
    force = "Force"


class SpacesCountSignageVariableName(StrEnum):
    """
    Variable names where the component type is SpacesCountSignage
    See PhysicalComponentName for referenced physical component
    """

    active = "Active"
    count = "Count"
    enabled = "Enabled"


class SwitchVariableName(StrEnum):
    """
    Variable names where the component type is Switch
    See PhysicalComponentName for referenced physical component
    """

    active = "Active"
    enabled = "Enabled"
    state = "State"


class TemperatureSensorVariableName(StrEnum):
    """
    Variable names where the component type is TemperatureSensor
    See PhysicalComponentName for referenced physical component
    """

    active = "Active"
    problem = "Problem"
    temperature = "Temperature"


class TiltSensorVariableName(StrEnum):
    """
    Variable names where the component type is TiltSensor
    See PhysicalComponentName for referenced physical component
    """

    active = "Active"
    enabled = "Enabled"
    angle = "Angle"


class TokenReaderVariableName(StrEnum):
    """
    Variable names where the component type is TokenReader
    See PhysicalComponentName for referenced physical component
    """

    enabled = "Enabled"
    enabled_set = "Enabled(Set)"
    operated = "Operated"
    problem = "Problem"
    token = "Token"
    token_type = "TokenType"


class UIInputVariableName(StrEnum):
    """
    Variable names where the component type is UIInput
    See PhysicalComponentName for referenced physical component
    """

    active = "Active"
    enabled = "Enabled"
    operated = "Operated"


class UpstreamProtectionTriggerVariableName(StrEnum):
    """
    Variable names where the component type is UpstreamProtectionTrigger
    See PhysicalComponentName for referenced physical component
    """

    active_set = "Active(Set)"
    enabled = "Enabled"
    problem = "Problem"
    tripped = "Tripped"


class VehicleIdSensorVariableName(StrEnum):
    """
    Variable names where the component type is VehicleIdSensor
    See PhysicalComponentName for referenced physical component
    """

    active = "Active"
    enabled = "Enabled"
