class _15118EVCertificateStatus:
    accepted = "Accepted"
    failed = "Failed"


class APNAuthentication:
    chap = "CHAP"
    none = "NONE"
    pap = "PAP"
    auto = "AUTO"


class Attribute:
    actual = "Actual"
    target = "Target"
    min_set = "MinSet"
    max_set = "MaxSet"


class AuthorizationStatus:
    accepted = "Accepted"
    blocked = "Blocked"
    concurrent_tx = "ConcurrentTx"
    expired = "Expired"
    invalid = "Invalid"
    no_credit = "NoCredit"
    not_allowed_type_evse = "NotAllowedTypeEVSE"
    not_at_this_location = "NotAtThisLocation"
    not_at_this_time = "NotAtThisTime"
    unknown = "Unknown"


class BootReason:
    application_reset = "ApplicationReset"
    firmware_update = "FirmwareUpdate"
    local_reset = "LocalReset"
    power_up = "PowerUp"
    remote_reset = "RemoteReset"
    scheduled_reset = "ScheduledReset"
    triggered = "Triggered"
    unknown = "Unknown"
    watchdog = "Watchdog"


class CertificateStatus:
    accepted = "Accepted"
    signature_error = "SignatureError"
    certificate_expired = "CertificateExpired"
    certificate_revoked = "CertificateRevoked"
    no_certificate_available = "NoCertificateAvailable"
    cert_chain_error = "CertChainError"
    contract_cancelled = "ContractCancelled"


class ChargingLimitSource:
    ems = "EMS"
    other = "Other"
    so = "SO"
    cso = "CSO"


class ChargingProfileKind:
    absolute = "Absolute"
    recurring = "Recurring"
    relative = "Relative"


class ChargingProfilePurpose:
    charging_station_external_constraints =\
        "ChargingStationExternalConstraints"
    charging_station_max_profile = "ChargingStationMaxProfile"
    tx_default_profile = "TxDefaultProfile"
    tx_profile = "TxProfile"


class ChargingRateUnit:
    w = "W"
    a = "A"


class ChargingState:
    charging = "Charging"
    ev_detected = "EVDetected"
    suspended_ev = "SuspendedEV"
    suspended_evse = "SuspendedEVSE"


class ClearMonitoringStatus:
    accepted = "Accepted"
    rejected = "Rejected"
    not_found = "NotFound"


class ComponentCriterion:
    active = "Active"
    available = "Available"
    enabled = "Enabled"
    problem = "Problem"


class Connector:
    c_ccs1 = "cCCS1"
    c_ccs2 = "cCCS2"
    c_g105 = "cG105"
    c_tesla = "cTesla"
    c_type1 = "cType1"
    c_type2 = "cType2"
    s309_1p_16a = "s309-1P-16A"
    s309_1p_32a = "s309-1P-32A"
    s309_3p_16a = "s309-3P-16A"
    s309_3p_32a = "s309-3P-32A"
    s_bs1361 = "sBS1361"
    s_cee_7_7 = "sCEE-7-7"
    s_type_2 = "sType2"
    s_type_3 = "sType3"
    other1_ph_max_16a = "Other1PhMax16A"
    other1_ph_over_16a = "Other1PhOver16A"
    other3_ph = "Other3Ph"
    pan = "Pan"
    w_inductive = "wInductive"
    w_resonant = "wResonant"
    undetermined = "Undetermined"
    unknown = "Unknown"


class CostKind:
    carbon_dioxide_emission = "CarbonDioxideEmission"
    relative_price_percentage = "RelativePricePercentage"
    renewable_generation_percentage = "RenewableGenerationPercentage"


class Data:
    string = "string"
    decimal = "decimal"
    integer = "integer"
    date_time = "dateTime"
    boolean = "boolean"
    option_list = "OptionList"
    sequence_list = "SequenceList"
    member_list = "MemberList"


class EncodingMethod:
    other = "Other"
    dlms_message = "DLMS Message"
    cosem_protected_data = "COSEM Protected Data"
    edl = "EDL"


class EnergyTransferMode:
    ac_single_phase_core = "AC_single_phase_core"
    ac_three_phase_core = "AC_three_phase_core"
    dc_combo_core = "DC_combo_core"
    dc_core = "DC_core"
    dc_extended = "DC_extended"
    dc_unique = "DC_unique"


class EventTrigger:
    alerting = "Alerting"
    delta = "Delta"
    periodic = "Periodic"


class GetCompositeScheduleStatus:
    accepted = "Accepted"
    rejected = "Rejected"


class GetInstalledCertificateStatus:
    accepted = "Accepted"
    not_found = "NotFound"


class GetVariableStatus:
    accepted = "Accepted"
    rejected = "Rejected"
    unknown_component = "UnknownComponent"
    unknown_variable = "UnknownVariable"
    not_supported_attribute_type = "NotSupportedAttributeType"


class HashAlgorithm:
    sha256 = "SHA256"
    sha384 = "SHA384"
    sha512 = "SHA512"


class IdToken:
    central = "Central"
    e_maid = "eMAID"
    iso14443 = "ISO14443"
    key_code = "KeyCode"
    local = "Local"
    no_authorization = "NoAuthorization"
    iso15693 = "ISO15693"


class Location:
    body = "Body"
    cable = "Cable"
    ev = "EV"
    inlet = "Inlet"
    outlet = "Outlet"


class Log:
    diagnostics_log = "DiagnosticsLog"
    security_log = "SecurityLog"


class Measurand:
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


class MessageFormat:
    ascii = "ASCII"
    html = "HTML"
    uri = "URI"
    utf8 = "UTF8"


class MessagePriority:
    always_front = "AlwaysFront"
    in_front = "InFront"
    normal_cycle = "NormalCycle"


class MessageState:
    charging = "Charging"
    faulted = "Faulted"
    idle = "Idle"
    unavailable = "Unavailable"


class MessageTrigger:
    boot_notification = "BootNotification"
    log_status_notification = "LogStatusNotification"
    firmware_status_notification = "FirmwareStatusNotification"
    heartbeat = "Heartbeat"
    meter_values = "MeterValues"
    sign_charging_station_certificate = "SignChargingStationCertificate"
    sign_v2g_certificate = "SignV2GCertificate"
    status_notification = "StatusNotification"
    transaction_event = "TransactionEvent"


class Monitor:
    upper_threshold = "UpperThreshold"
    lower_threshold = "LowerThreshold"
    delta = "Delta"
    periodic = "Periodic"
    periodic_clock_aligned = "PeriodicClockAligned"


class MonitoringCriterion:
    threshold_monitoring = "ThresholdMonitoring"
    delta_monitoring = "DeltaMonitoring"
    periodic_monitoring = "PeriodicMonitoring"


class Mutability:
    read_only = "ReadOnly"
    write_only = "WriteOnly"
    read_write = "ReadWrite"


class OCPPInterface:
    wired_0 = "Wired0"
    wired_1 = "Wired1"
    wired_2 = "Wired2"
    wired_3 = "Wired3"
    wireless_0 = "Wireless0"
    wireless_1 = "Wireless1"
    wireless_2 = "Wireless2"
    wireless_3 = "Wireless3"


class OCPPTransport:
    json = "JSON"
    soap = "SOAP"


class OCPPVersion:
    ocpp12 = "OCPP12"
    ocpp15 = "OCPP15"
    ocpp16 = "OCPP16"
    ocpp20 = "OCPP20"


class Phase:
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


class ReadingContext:
    interruption_begin = "Interruption.Begin"
    interruption_end = "Interruption.End"
    other = "Other"
    sample_clock = "Sample.Clock"
    sample_periodic = "Sample.Periodic"
    transaction_begin = "Transaction.Begin"
    transaction_end = "Transaction.End"
    trigger = "Trigger"


class Reason:
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
    unlock_command = "UnlockCommand"


class RecurrencyKind:
    daily = "Daily"
    weekly = "Weekly"


class SetMonitoringStatus:
    accepted = "Accepted"
    unknown_component = "UnknownComponent"
    unknown_variable = "UnknownVariable"
    unsupported_monitor_type = "UnsupportedMonitorType"
    rejected = "Rejected"
    out_of_range = "OutOfRange"
    duplicate = "Duplicate"


class SetVariableStatus:
    accepted = "Accepted"
    rejected = "Rejected"
    invalid_value = "InvalidValue"
    unknown_component = "UnknownComponent"
    unknown_variable = "UnknownVariable"
    not_supported_attribute_type = "NotSupportedAttributeType"
    out_of_range = "OutOfRange"
    reboot_required = "RebootRequired"


class SignatureMethod:
    ecdsap256_sha256 = "ECDSAP256SHA256"
    ecdsap384_sha384 = "ECDSAP384SHA384"
    ecdsa192_sha256 = "ECDSA192SHA256"


class TransactionEvent:
    ended = "Ended"
    started = "Started"
    updated = "Updated"


class TriggerReason:
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


class CancelReservationStatus:
    accepted = "Accepted"
    rejected = "Rejected"


class RequestStartStopStatus:
    accepted = "Accepted"
    rejected = "Rejected"


class RegistrationStatus:
    accepted = "Accepted"
    pending = "Pending"
    rejected = "Rejected"


class ConnectorStatus:
    available = "Available"
    occupied = "Occupied"
    reserved = "Reserved"
    unavailable = "Unavailable"
    faulted = "Faulted"


class CertificateUse:
    v2g_root_certficate = "V2GRootCertficate"
    mo_root_certificate = "MORootCertificate"
    cso_sub_ca1 = "CSOSubCA1"
    cso_sub_ca2 = "CSOSubCA2"
    csms_root_certificate = "CSMSRootCertificate"
    manufacturer_root_certificate = "ManufacturerRootCertificate"


class DeleteCertificateStatus:
    accepted = "Accepted"
    failed = "Failed"
    not_found = "NotFound"


class GenericStatus:
    accepted = "Accepted"
    rejected = "Rejected"


class ClearMessageStatus:
    ccepted = "Accepted"
    unknown = "Unknown"


class CertificateSigningUse:
    charging_station_certificate = "ChargingStationCertificate"
    v2g_certificate = "V2GCertificate"


class ReportBase:
    configuration_inventory = "ConfigurationInventory"
    full_inventory = "FullInventory"
    summary_inventory = "SummaryInventory"


class ClearCacheStatus:
    accepted = "Accepted"
    rejected = "Rejected"


class UnlockStatus:
    unlocked = "Unlocked"
    unlock_failed = "UnlockFailed"


class SetNetworkProfileStatus:
    accepted = "Accepted"
    rejected = "Rejected"
    failed = "Failed"


class CustomerInformationStatus:
    accepted = "Accepted"
    rejected = "Rejected"
    invalid = "Invalid"


class NotifyEVChargingNeedsStatus:
    accepted = "Accepted"
    rejected = "Rejected"
    processing = "Processing"


class ReservationUpdateStatus:
    expired = "Expired"
    removed = "Removed"


class PublishFirmwareStatus:
    downloaded = "Downloaded"
    download_failed = "DownloadFailed"
    downloading = "Downloading"
    download_scheduled = "DownloadScheduled"
    download_paused = "DownloadPaused"
    publish_failed = "PublishFailed"
    published = "Published"
    invalid_checksum = "InvalidChecksum"
    checksum_verified = "ChecksumVerified"


class ResetStatus:
    accepted = "Accepted"
    rejected = "Rejected"
    scheduled = "Scheduled"


class GetDisplayMessageStatus:
    """GetDisplayMessagesResponse_v1p0"""
    accepted = "Accepted"
    unknown = "Unknown"


class ReserveNowStatus:
    accepted = "Accepted"
    faulted = "Faulted"
    occupied = "Occupied"
    rejected = "Rejected"
    unavailable = "Unavailable"


class SecurityEvent:
    firmware_updated = "FirmwareUpdated"
    failed_to_authenticate_at_csms = "FailedToAuthenticateAtCsms"
    csms_failed_to_authenticate = "CsmsFailedToAuthenticate"
    setting_system_time = "SettingSystemTime"
    startup_of_the_device = "StartupOfTheDevice"
    reset_or_reboot = "ResetOrReboot"
    security_log_was_cleared = "SecurityLogWasCleared"
    reconfiguration_of_security_parameters =\
        "ReconfigurationOfSecurityParameters"
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


class MonitoringBase:
    all = "All"
    factory_default = "FactoryDefault"
    none = "None"


class GenericDeviceModelStatus:
    accepted = "Accepted"
    rejected = "Rejected"
    not_supported = "NotSupported"


class UpdateFirmwareStatus:
    accepted = "Accepted"
    rejected = "Rejected"
    accepted_canceled = "AcceptedCanceled"


class GetChargingProfileStatus:
    accepted = "Accepted"
    no_profiles = "NoProfiles"


class CertificateSignedStatus:
    accepted = "Accepted"
    rejected = "Rejected"


class DataTranserStatus:
    accepted = "Accepted"
    rejected = "Rejected"
    unknown_message_id = "UnknownMessageId"
    unknown_vendor_id = "UnknownVendorId"


class UploadLogStatus:
    bad_message = "BadMessage"
    idle = "Idle"
    not_supported_operation = "NotSupportedOperation"
    permission_denied = "PermissionDenied"
    uploaded = "Uploaded"
    upload_failure = "UploadFailure"
    uploading = "Uploading"


class ChangeAvailabilityStatus:
    accepted = "Accepted"
    rejected = "Rejected"
    scheduled = "Scheduled"


class Reset:
    immediate = "Immediate"
    on_idle = "OnIdle"


class UpdateStatus:
    accepted = "Accepted"
    failed = "Failed"
    version_mismatch = "VersionMismatch"


class OperationalStatus:
    inoperative = "Inoperative"
    operative = "Operative"


class TriggerMessageStatus:
    accepted = "Accepted"
    rejected = "Rejected"
    not_implemented = "NotImplemented"


class UnpublishFirmwareStatus:
    download_ongoing = "DownloadOngoing"
    no_firmware = "NoFirmware"
    unpublished = "Unpublished"


class FirmwareStatus:
    certificate_verified = "CertificateVerified"
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
    invalid_certificate = "InvalidCertificate"
    revoked_certificate = "RevokedCertificate"
    publish_failed = "PublishFailed"
    signature_verified = "SignatureVerified"


class LogStatus:
    accepted = "Accepted"
    rejected = "Rejected"
    accepted_canceled = "AcceptedCanceled"


class DisplayMessageStatus:
    accepted = "Accepted"
    not_supported_message_format = "NotSupportedMessageFormat"
    rejected = "Rejected"
    not_supported_priority = "NotSupportedPriority"
    not_supported_state = "NotSupportedState"
    unknown_transaction = "UnknownTransaction"


class ChargingProfileStatus:
    accepted = "Accepted"
    rejected = "Rejected"


class Update:
    differential = "Differential"
    full = "Full"


class VPN:
    ik_ev2 = "IKEv2"
    ip_sec = "IPSec"
    l2_tp = "L2TP"
    pptp = "PPTP"
