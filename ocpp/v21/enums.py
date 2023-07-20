try:
    # breaking change introduced in python 3.11
    from enum import StrEnum
except ImportError:  # pragma: no cover
    from enum import Enum  # pragma: no cover

    class StrEnum(str, Enum):  # pragma: no cover
        pass  # pragma: no cover


class APNAuthentication(StrEnum):
    pap = "PAP"
    chap = "CHAP"
    none = "NONE"
    auto = "AUTO"


class Attribute(StrEnum):
    actual = "Actual"
    target = "Target"
    min_set = "MinSet"
    max_set = "MaxSet"


class AuthorizationStatus(StrEnum):
    accepted = "Accepted"
    blocked = "Blocked"
    expired = "Expired"
    invalid = "Invalid"
    no_credit = "NoCredit"
    not_allowed_type_evse = "NotAllowedTypeEVSE"
    not_at_this_location = "NotAtThisLocation"
    not_at_this_time = "NotAtThisTime"
    concurrent_tx = "ConcurrentTx"
    unknown = "Unknown"


class AuthorizeCertificateStatus(StrEnum):
    accepted = "Accepted"
    signature_error = "SignatureError"
    certificate_expired = "CertificateExpired"
    certificate_revoked = "CertificateRevoked"
    no_certificate_available = "NoCertificateAvailable"
    cert_chain_error = "CertChainError"
    contract_cancelled = "ContractCancelled"


class BootReason(StrEnum):
    application_reset = "ApplicationReset"
    firmware_update = "FirmwareUpdate"
    local_reset = "LocalReset"
    power_up = "PowerUp"
    remote_reset = "RemoteReset"
    scheduled_reset = "ScheduledReset"
    triggered = "Triggered"
    unknown = "Unknown"
    watchdog = "Watchdog"


class CancelReservationStatus(StrEnum):
    accepted = "Accepted"
    rejected = "Rejected"


class CertificateAction(StrEnum):
    install = "Install"
    update = "Update"


class CertificateSignedStatus(StrEnum):
    accepted = "Accepted"
    rejected = "Rejected"


class CertificateSigningUse(StrEnum):
    charging_station_certificate = "ChargingStationCertificate"
    v2g_certificate = "V2GCertificate"


class ChangeAvailabilityStatus(StrEnum):
    accepted = "Accepted"
    rejected = "Rejected"
    scheduled = "Scheduled"


class ChargingLimitSource(StrEnum):
    cso = "CSO"
    ems = "EMS"
    other = "Other"
    so = "SO"


class ChargingProfileKind(StrEnum):
    absolute = "Absolute"
    recurring = "Recurring"
    relative = "Relative"
    dynamic = "Dynamic"


class ChargingProfilePurpose(StrEnum):
    charging_station_external_constraints = "ChargingStationExternalConstraints"
    charging_station_max_profile = "ChargingStationMaxProfile"
    tx_default_profile = "TxDefaultProfile"
    tx_profile = "TxProfile"
    priority_charging = "PriorityCharging"
    local_generation = "LocalGeneration"


class ChargingProfileStatus(StrEnum):
    accepted = "Accepted"
    rejected = "Rejected"


class ChargingRateUnit(StrEnum):
    w = "W"
    a = "A"


class ChargingState(StrEnum):
    ev_connected = "EVConnected"
    charging = "Charging"
    suspended_ev = "SuspendedEV"
    suspended_evse = "SuspendedEVSE"
    idle = "Idle"


class ClearCacheStatus(StrEnum):
    accepted = "Accepted"
    rejected = "Rejected"


class ClearChargingProfileStatus(StrEnum):
    accepted = "Accepted"
    unknown = "Unknown"


class ClearMessageStatus(StrEnum):
    accepted = "Accepted"
    unknown = "Unknown"


class ClearMonitoringStatus(StrEnum):
    accepted = "Accepted"
    rejected = "Rejected"
    not_found = "NotFound"


class ComponentCriterion(StrEnum):
    active = "Active"
    available = "Available"
    enabled = "Enabled"
    problem = "Problem"


class Connector(StrEnum):
    c_ccs1 = "cCCS1"
    c_ccs2 = "cCCS2"
    c_g105 = "cG105"
    c_tesla = "cTesla"
    c_type1 = "cType1"
    c_type2 = "cType2"
    s309_1_p_16a = "s309-1P-16A"
    s309_1_p_32a = "s309-1P-32A"
    s309_3_p_16a = "s309-3P-16A"
    s309_3_p_32a = "s309-3P-32A"
    s_bs1361 = "sBS1361"
    s_cee_7_7 = "sCEE-7-7"
    s_type2 = "sType2"
    s_type3 = "sType3"
    other1_ph_max16a = "Other1PhMax16A"
    other1_ph_over16a = "Other1PhOver16A"
    other3_ph = "Other3Ph"
    pan = "Pan"
    w_inductive = "wInductive"
    w_resonant = "wResonant"
    undetermined = "Undetermined"
    unknown = "Unknown"


class ConnectorStatus(StrEnum):
    available = "Available"
    occupied = "Occupied"
    reserved = "Reserved"
    unavailable = "Unavailable"
    faulted = "Faulted"


class ControlMode(StrEnum):
    scheduled = "Scheduled"
    dynamic = "Dynamic"


class CostKind(StrEnum):
    carbon_dioxide_emission = "CarbonDioxideEmission"
    relative_price_percentage = "RelativePricePercentage"
    renewable_generation_percentage = "RenewableGenerationPercentage"


class CustomerInformationStatus(StrEnum):
    accepted = "Accepted"
    rejected = "Rejected"
    invalid = "Invalid"


class Data(StrEnum):
    string = "string"
    decimal = "decimal"
    integer = "integer"
    date_time = "dateTime"
    boolean = "boolean"
    option_list = "OptionList"
    sequence_list = "SequenceList"
    member_list = "MemberList"


class DataTransferStatus(StrEnum):
    accepted = "Accepted"
    rejected = "Rejected"
    unknown_message_id = "UnknownMessageId"
    unknown_vendor_id = "UnknownVendorId"


class DeleteCertificateStatus(StrEnum):
    accepted = "Accepted"
    failed = "Failed"
    not_found = "NotFound"


class DisplayMessageStatus(StrEnum):
    accepted = "Accepted"
    not_supported_message_format = "NotSupportedMessageFormat"
    rejected = "Rejected"
    not_supported_priority = "NotSupportedPriority"
    not_supported_state = "NotSupportedState"
    unknown_transaction = "UnknownTransaction"


class EnergyTransferMode(StrEnum):
    ac_single_phase = "AC_single_phase"
    ac_two_phase = "AC_two_phase"
    ac_three_phase = "AC_three_phase"
    dc = "DC"
    ac_single_phase_bpt = "AC_single_phase_BPT"
    ac_two_phase_bpt = "AC_two_phase_BPT"
    ac_three_phase_bpt = "AC_three_phase_BPT"
    dc_bpt = "DC_BPT"
    dc_acdp = "DC_ACDP"
    dc_acdp_bpt = "DC_ACDP_BPT"
    wpt = "WPT"


class EventNotification(StrEnum):
    hard_wired_notification = "HardWiredNotification"
    hard_wired_monitor = "HardWiredMonitor"
    preconfigured_monitor = "PreconfiguredMonitor"
    custom_monitor = "CustomMonitor"


class EventTrigger(StrEnum):
    alerting = "Alerting"
    delta = "Delta"
    periodic = "Periodic"


class FirmwareStatus(StrEnum):
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


class GenericDeviceModelStatus(StrEnum):
    accepted = "Accepted"
    rejected = "Rejected"
    not_supported = "NotSupported"
    empty_result_set = "EmptyResultSet"


class GenericStatus(StrEnum):
    accepted = "Accepted"
    rejected = "Rejected"


class GetCertificateIdUse(StrEnum):
    v2g_root_certificate = "V2GRootCertificate"
    mo_root_certificate = "MORootCertificate"
    csms_root_certificate = "CSMSRootCertificate"
    v2g_certificate_chain = "V2GCertificateChain"
    manufacturer_root_certificate = "ManufacturerRootCertificate"
    oem_root_certificate = "OEMRootCertificate"


class GetCertificateStatus(StrEnum):
    accepted = "Accepted"
    failed = "Failed"


class GetChargingProfileStatus(StrEnum):
    accepted = "Accepted"
    no_profiles = "NoProfiles"


class GetDisplayMessagesStatus(StrEnum):
    accepted = "Accepted"
    unknown = "Unknown"


class GetInstalledCertificateStatus(StrEnum):
    accepted = "Accepted"
    not_found = "NotFound"


class GetVariableStatus(StrEnum):
    accepted = "Accepted"
    rejected = "Rejected"
    unknown_component = "UnknownComponent"
    unknown_variable = "UnknownVariable"
    not_supported_attribute_type = "NotSupportedAttributeType"


class HashAlgorithm(StrEnum):
    sha256 = "SHA256"
    sha384 = "SHA384"
    sha512 = "SHA512"


class IdToken(StrEnum):
    central = "Central"
    e_maid = "eMAID"
    iso14443 = "ISO14443"
    iso15693 = "ISO15693"
    key_code = "KeyCode"
    local = "Local"
    mac_address = "MacAddress"
    no_authorization = "NoAuthorization"
    evccid = "EVCCID"
    nema = "NEMA"


class InstallCertificateStatus(StrEnum):
    accepted = "Accepted"
    rejected = "Rejected"
    failed = "Failed"


class InstallCertificateUse(StrEnum):
    v2g_root_certificate = "V2GRootCertificate"
    mo_root_certificate = "MORootCertificate"
    csms_root_certificate = "CSMSRootCertificate"
    oem_root_certificate = "OEMRootCertificate"
    manufacturer_root_certificate = "ManufacturerRootCertificate"


class Iso15118EVCertificateStatus(StrEnum):
    accepted = "Accepted"
    failed = "Failed"


class Location(StrEnum):
    body = "Body"
    cable = "Cable"
    ev = "EV"
    inlet = "Inlet"
    outlet = "Outlet"
    local_grid = "LocalGrid"


class Log(StrEnum):
    diagnostics_log = "DiagnosticsLog"
    security_log = "SecurityLog"
    data_collector_log = "DataCollectorLog"


class LogStatus(StrEnum):
    accepted = "Accepted"
    rejected = "Rejected"
    accepted_canceled = "AcceptedCanceled"


class Measurand(StrEnum):
    current_export = "Current.Export"
    current_export_offered = "Current.Export.Offered"
    current_export_minimum = "Current.Export.Minimum"
    current_import = "Current.Import"
    current_import_offered = "Current.Import.Offered"
    current_import_minimum = "Current.Import.Minimum"
    current_offered = "Current.Offered"
    display_present_soc = "Display.PresentSOC"
    display_minimum_soc = "Display.MinimumSOC"
    display_target_soc = "Display.TargetSOC"
    display_maximum_soc = "Display.MaximumSOC"
    display_remaining_time_to_minimum_soc = "Display.RemainingTimeToMinimumSOC"
    display_remaining_time_to_target_soc = "Display.RemainingTimeToTargetSOC"
    display_remaining_time_to_maximum_soc = "Display.RemainingTimeToMaximumSOC"
    display_charging_complete = "Display.ChargingComplete"
    display_battery_energy_capacity = "Display.BatteryEnergyCapacity"
    display_inlet_hot = "Display.InletHot"
    energy_active_export_interval = "Energy.Active.Export.Interval"
    energy_active_export_register = "Energy.Active.Export.Register"
    energy_active_import_interval = "Energy.Active.Import.Interval"
    energy_active_import_register = "Energy.Active.Import.Register"
    energy_active_net = "Energy.Active.Net"
    energy_active_setpoint_interval = "Energy.Active.Setpoint.Interval"
    energy_apparent_export = "Energy.Apparent.Export"
    energy_apparent_import = "Energy.Apparent.Import"
    energy_apparent_net = "Energy.Apparent.Net"
    energy_reactive_export_interval = "Energy.Reactive.Export.Interval"
    energy_reactive_export_register = "Energy.Reactive.Export.Register"
    energy_reactive_import_interval = "Energy.Reactive.Import.Interval"
    energy_reactive_import_register = "Energy.Reactive.Import.Register"
    energy_reactive_net = "Energy.Reactive.Net"
    energy_request_target = "EnergyRequest.Target"
    energy_request_minimum = "EnergyRequest.Minimum"
    energy_request_maximum = "EnergyRequest.Maximum"
    energy_request_minimum_v2x = "EnergyRequest.Minimum.V2X"
    energy_request_maximum_v2x = "EnergyRequest.Maximum.V2X"
    energy_request_bulk = "EnergyRequest.Bulk"
    frequency = "Frequency"
    power_active_export = "Power.Active.Export"
    power_active_import = "Power.Active.Import"
    power_active_setpoint = "Power.Active.Setpoint"
    power_active_residual = "Power.Active.Residual"
    power_export_minimum = "Power.Export.Minimum"
    power_export_offered = "Power.Export.Offered"
    power_factor = "Power.Factor"
    power_import_offered = "Power.Import.Offered"
    power_import_minimum = "Power.Import.Minimum"
    power_offered = "Power.Offered"
    power_reactive_export = "Power.Reactive.Export"
    power_reactive_import = "Power.Reactive.Import"
    soc = "SoC"
    voltage = "Voltage"
    voltage_minimum = "Voltage.Minimum"
    voltage_maximum = "Voltage.Maximum"


class MessageFormat(StrEnum):
    ascii = "ASCII"
    html = "HTML"
    uri = "URI"
    utf8 = "UTF8"


class MessagePriority(StrEnum):
    always_front = "AlwaysFront"
    in_front = "InFront"
    normal_cycle = "NormalCycle"


class MessageState(StrEnum):
    charging = "Charging"
    faulted = "Faulted"
    idle = "Idle"
    unavailable = "Unavailable"


class MessageTrigger(StrEnum):
    boot_notification = "BootNotification"
    log_status_notification = "LogStatusNotification"
    firmware_status_notification = "FirmwareStatusNotification"
    heartbeat = "Heartbeat"
    meter_values = "MeterValues"
    sign_charging_station_certificate = "SignChargingStationCertificate"
    sign_v2g_certificate = "SignV2GCertificate"
    status_notification = "StatusNotification"
    transaction_event = "TransactionEvent"
    sign_combined_certificate = "SignCombinedCertificate"
    publish_firmware_status_notification = "PublishFirmwareStatusNotification"


class MobilityNeedsMode(StrEnum):
    evcc = "EVCC"
    evcc_secc = "EVCC_SECC"


class Monitor(StrEnum):
    upper_threshold = "UpperThreshold"
    lower_threshold = "LowerThreshold"
    delta = "Delta"
    periodic = "Periodic"
    periodic_clock_aligned = "PeriodicClockAligned"


class MonitoringBase(StrEnum):
    all = "All"
    factory_default = "FactoryDefault"
    hard_wired_only = "HardWiredOnly"


class MonitoringCriterion(StrEnum):
    threshold_monitoring = "ThresholdMonitoring"
    delta_monitoring = "DeltaMonitoring"
    periodic_monitoring = "PeriodicMonitoring"


class Mutability(StrEnum):
    read_only = "ReadOnly"
    write_only = "WriteOnly"
    read_write = "ReadWrite"


class NotifyAllowedEnergyTransferStatus(StrEnum):
    accepted = "Accepted"
    rejected = "Rejected"


class NotifyCRLStatus(StrEnum):
    available = "Available"
    unavailable = "Unavailable"


class NotifyEVChargingNeedsStatus(StrEnum):
    accepted = "Accepted"
    rejected = "Rejected"
    processing = "Processing"
    no_charging_profile = "NoChargingProfile"


class OCPPTransport(StrEnum):
    soap = "SOAP"
    json = "JSON"


class OCPPVersion(StrEnum):
    ocpp12 = "OCPP12"
    ocpp15 = "OCPP15"
    ocpp16 = "OCPP16"
    ocpp20 = "OCPP20"


class OperationMode(StrEnum):
    idle = "Idle"
    charging_only = "ChargingOnly"
    central_setpoint = "CentralSetpoint"
    external_setpoint = "ExternalSetpoint"
    external_limits = "ExternalLimits"
    central_frequency = "CentralFrequency"
    local_frequency = "LocalFrequency"
    local_load_balancing = "LocalLoadBalancing"


class OperationalStatus(StrEnum):
    inoperative = "Inoperative"
    operative = "Operative"


class Phase(StrEnum):
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


class PreconditioningStatus(StrEnum):
    unknown = "Unknown"
    ready = "Ready"
    not_ready = "NotReady"
    preconditioning = "Preconditioning"


class Pricing(StrEnum):
    no_pricing = "NoPricing"
    absolute_pricing = "AbsolutePricing"
    price_levels = "PriceLevels"


class PriorityChargingStatus(StrEnum):
    accepted = "Accepted"
    rejected = "Rejected"
    no_profile = "NoProfile"


class PublishFirmwareStatus(StrEnum):
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


class ReadingContext(StrEnum):
    interruption_begin = "Interruption.Begin"
    interruption_end = "Interruption.End"
    other = "Other"
    sample_clock = "Sample.Clock"
    sample_periodic = "Sample.Periodic"
    transaction_begin = "Transaction.Begin"
    transaction_end = "Transaction.End"
    trigger = "Trigger"


class Reason(StrEnum):
    de_authorized = "DeAuthorized"
    emergency_stop = "EmergencyStop"
    energy_limit_reached = "EnergyLimitReached"
    ev_disconnected = "EVDisconnected"
    ground_fault = "GroundFault"
    immediate_reset = "ImmediateReset"
    master_pass = "MasterPass"
    local = "Local"
    out_of_credit = "OutOfCredit"
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
    charging_needs_not_accepted = "ChargingNeedsNotAccepted"


class RecurrencyKind(StrEnum):
    daily = "Daily"
    weekly = "Weekly"


class RegistrationStatus(StrEnum):
    accepted = "Accepted"
    pending = "Pending"
    rejected = "Rejected"


class ReportBase(StrEnum):
    configuration_inventory = "ConfigurationInventory"
    full_inventory = "FullInventory"
    summary_inventory = "SummaryInventory"


class RequestStartStopStatus(StrEnum):
    accepted = "Accepted"
    rejected = "Rejected"


class ReservationUpdateStatus(StrEnum):
    expired = "Expired"
    removed = "Removed"


class ReserveNowStatus(StrEnum):
    accepted = "Accepted"
    faulted = "Faulted"
    occupied = "Occupied"
    rejected = "Rejected"
    unavailable = "Unavailable"


class Reset(StrEnum):
    immediate = "Immediate"
    on_idle = "OnIdle"


class ResetStatus(StrEnum):
    accepted = "Accepted"
    rejected = "Rejected"
    scheduled = "Scheduled"


class SendLocalListStatus(StrEnum):
    accepted = "Accepted"
    failed = "Failed"
    version_mismatch = "VersionMismatch"


class SetMonitoringStatus(StrEnum):
    accepted = "Accepted"
    unknown_component = "UnknownComponent"
    unknown_variable = "UnknownVariable"
    unsupported_monitor_type = "UnsupportedMonitorType"
    rejected = "Rejected"
    duplicate = "Duplicate"


class SetNetworkProfileStatus(StrEnum):
    accepted = "Accepted"
    rejected = "Rejected"
    failed = "Failed"


class SetVariableStatus(StrEnum):
    accepted = "Accepted"
    rejected = "Rejected"
    unknown_component = "UnknownComponent"
    unknown_variable = "UnknownVariable"
    not_supported_attribute_type = "NotSupportedAttributeType"
    reboot_required = "RebootRequired"


class TransactionEvent(StrEnum):
    ended = "Ended"
    started = "Started"
    updated = "Updated"


class TriggerMessageStatus(StrEnum):
    accepted = "Accepted"
    rejected = "Rejected"
    not_implemented = "NotImplemented"


class TriggerReason(StrEnum):
    abnormal_condition = "AbnormalCondition"
    authorized = "Authorized"
    cable_plugged_in = "CablePluggedIn"
    charging_rate_changed = "ChargingRateChanged"
    charging_state_changed = "ChargingStateChanged"
    deauthorized = "Deauthorized"
    energy_limit_reached = "EnergyLimitReached"
    ev_communication_lost = "EVCommunicationLost"
    ev_connect_timeout = "EVConnectTimeout"
    ev_departed = "EVDeparted"
    ev_detected = "EVDetected"
    meter_value_clock = "MeterValueClock"
    meter_value_periodic = "MeterValuePeriodic"
    remote_start = "RemoteStart"
    remote_stop = "RemoteStop"
    reset_command = "ResetCommand"
    signed_data_received = "SignedDataReceived"
    stop_authorized = "StopAuthorized"
    time_limit_reached = "TimeLimitReached"
    trigger = "Trigger"
    unlock_command = "UnlockCommand"
    operation_mode_changed = "OperationModeChanged"


class UnlockStatus(StrEnum):
    unlocked = "Unlocked"
    unlock_failed = "UnlockFailed"
    ongoing_authorized_transaction = "OngoingAuthorizedTransaction"
    unknown_connector = "UnknownConnector"


class UnpublishFirmwareStatus(StrEnum):
    download_ongoing = "DownloadOngoing"
    no_firmware = "NoFirmware"
    unpublished = "Unpublished"


class Update(StrEnum):
    differential = "Differential"
    full = "Full"


class UpdateFirmwareStatus(StrEnum):
    accepted = "Accepted"
    rejected = "Rejected"
    accepted_canceled = "AcceptedCanceled"
    invalid_certificate = "InvalidCertificate"
    revoked_certificate = "RevokedCertificate"


class UploadLogStatus(StrEnum):
    bad_message = "BadMessage"
    idle = "Idle"
    not_supported_operation = "NotSupportedOperation"
    permission_denied = "PermissionDenied"
    uploaded = "Uploaded"
    upload_failure = "UploadFailure"
    uploading = "Uploading"
    accepted_canceled = "AcceptedCanceled"


class VPN(StrEnum):
    ik_ev2 = "IKEv2"
    ip_sec = "IPSec"
    l2_tp = "L2TP"
    pptp = "PPTP"
