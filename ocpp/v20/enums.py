class 15118EVCertificateStatus:
    accepted: "Accepted"
    failed: "Failed"


class APNAuthentication:
    chap: "CHAP"
    none: "NONE"
    pap: "PAP"
    auto: "AUTO"


class Attribute:
    actual: "Actual"
    target: "Target"
    min_set: "MinSet"
    max_set: "MaxSet"


class AuthorizationStatus:
    accepted: "Accepted"
    blocked: "Blocked"
    concurrent_tx: "ConcurrentTx"
    expired: "Expired"
    invalid: "Invalid"
    no_credit: "NoCredit"
    not_allowed_type_evse: "NotAllowedTypeEVSE"
    not_at_this_location: "NotAtThisLocation"
    not_at_this_time: "NotAtThisTime"
    unknown: "Unknown"


class BootReason:
    application_reset: "ApplicationReset"
    firmware_update: "FirmwareUpdate"
    local_reset: "LocalReset"
    power_up: "PowerUp"
    remote_reset: "RemoteReset"
    scheduled_reset: "ScheduledReset"
    triggered: "Triggered"
    unknown: "Unknown"
    watchdog: "Watchdog"


class CertificateStatus:
    accepted: "Accepted"
    signature_error: "SignatureError"
    certificate_expired: "CertificateExpired"
    certificate_revoked: "CertificateRevoked"
    no_certificate_available: "NoCertificateAvailable"
    cert_chain_error: "CertChainError"
    contract_cancelled: "ContractCancelled"


class ChargingLimitSource:
    ems: "EMS"
    other: "Other"
    so: "SO"
    cso: "CSO"


class ChargingProfileKind:
    absolute: "Absolute"
    recurring: "Recurring"
    relative: "Relative"


class ChargingProfilePurpose:
    charging_station_external_constraints: "ChargingStationExternalConstraints"
    charging_station_max_profile: "ChargingStationMaxProfile"
    tx_default_profile: "TxDefaultProfile"
    tx_profile: "TxProfile"


class ChargingRateUnit:
    w: "W"
    a: "A"


class ChargingState:
    charging: "Charging"
    ev_detected: "EVDetected"
    suspended_ev: "SuspendedEV"
    suspended_evse: "SuspendedEVSE"


class ClearMonitoringStatus:
    accepted: "Accepted"
    rejected: "Rejected"
    not_found: "NotFound"


class ComponentCriterion:
    active: "Active"
    available: "Available"
    enabled: "Enabled"
    problem: "Problem"


class Connector:
    c_ccs1: "cCCS1"
    c_ccs2: "cCCS2"
    c_g105: "cG105"
    c_tesla: "cTesla"
    c_type1: "cType1"
    c_type2: "cType2"
    s309_1_p_16_a: "s309-1P-16A"
    s309_1_p_32_a: "s309-1P-32A"
    s309_3_p_16_a: "s309-3P-16A"
    s309_3_p_32_a: "s309-3P-32A"
    s_bs1361: "sBS1361"
    s_cee_7_7: "sCEE-7-7"
    s_type2: "sType2"
    s_type3: "sType3"
    other1_ph_max16_a: "Other1PhMax16A"
    other1_ph_over16_a: "Other1PhOver16A"
    other3_ph: "Other3Ph"
    pan: "Pan"
    w_inductive: "wInductive"
    w_resonant: "wResonant"
    undetermined: "Undetermined"
    unknown: "Unknown"


class CostKind:
    carbon_dioxide_emission: "CarbonDioxideEmission"
    relative_price_percentage: "RelativePricePercentage"
    renewable_generation_percentage: "RenewableGenerationPercentage"


class Data:
    string: "string"
    decimal: "decimal"
    integer: "integer"
    date_time: "dateTime"
    boolean: "boolean"
    option_list: "OptionList"
    sequence_list: "SequenceList"
    member_list: "MemberList"


class EncodingMethod:
    other: "Other"
    dlms _message: "DLMS Message"
    cosem _protected _data: "COSEM Protected Data"
    edl: "EDL"


class EnergyTransferMode:
    ac_single_phase_core: "AC_single_phase_core"
    ac_three_phase_core: "AC_three_phase_core"
    dc_combo_core: "DC_combo_core"
    dc_core: "DC_core"
    dc_extended: "DC_extended"
    dc_unique: "DC_unique"


class EventTrigger:
    alerting: "Alerting"
    delta: "Delta"
    periodic: "Periodic"


class GetCompositeScheduleStatus:
    accepted: "Accepted"
    rejected: "Rejected"


class GetInstalledCertificateStatus:
    accepted: "Accepted"
    not_found: "NotFound"


class GetVariableStatus:
    accepted: "Accepted"
    rejected: "Rejected"
    unknown_component: "UnknownComponent"
    unknown_variable: "UnknownVariable"
    not_supported_attribute_type: "NotSupportedAttributeType"


class HashAlgorithm:
    sha256: "SHA256"
    sha384: "SHA384"
    sha512: "SHA512"


class IdToken:
    central: "Central"
    e_maid: "eMAID"
    iso14443: "ISO14443"
    key_code: "KeyCode"
    local: "Local"
    no_authorization: "NoAuthorization"
    iso15693: "ISO15693"


class Location:
    body: "Body"
    cable: "Cable"
    ev: "EV"
    inlet: "Inlet"
    outlet: "Outlet"


class Log:
    diagnostics_log: "DiagnosticsLog"
    security_log: "SecurityLog"


class Measurand:
    current._export: "Current.Export"
    current._import: "Current.Import"
    current._offered: "Current.Offered"
    energy._active._export._register: "Energy.Active.Export.Register"
    energy._active._import._register: "Energy.Active.Import.Register"
    energy._reactive._export._register: "Energy.Reactive.Export.Register"
    energy._reactive._import._register: "Energy.Reactive.Import.Register"
    energy._active._export._interval: "Energy.Active.Export.Interval"
    energy._active._import._interval: "Energy.Active.Import.Interval"
    energy._active._net: "Energy.Active.Net"
    energy._reactive._export._interval: "Energy.Reactive.Export.Interval"
    energy._reactive._import._interval: "Energy.Reactive.Import.Interval"
    energy._reactive._net: "Energy.Reactive.Net"
    energy._apparent._net: "Energy.Apparent.Net"
    energy._apparent._import: "Energy.Apparent.Import"
    energy._apparent._export: "Energy.Apparent.Export"
    frequency: "Frequency"
    power._active._export: "Power.Active.Export"
    power._active._import: "Power.Active.Import"
    power._factor: "Power.Factor"
    power._offered: "Power.Offered"
    power._reactive._export: "Power.Reactive.Export"
    power._reactive._import: "Power.Reactive.Import"
    so_c: "SoC"
    voltage: "Voltage"


class MessageFormat:
    ascii: "ASCII"
    html: "HTML"
    uri: "URI"
    utf8: "UTF8"


class MessagePriority:
    always_front: "AlwaysFront"
    in_front: "InFront"
    normal_cycle: "NormalCycle"


class MessageState:
    charging: "Charging"
    faulted: "Faulted"
    idle: "Idle"
    unavailable: "Unavailable"


class MessageTrigger:
    boot_notification: "BootNotification"
    log_status_notification: "LogStatusNotification"
    firmware_status_notification: "FirmwareStatusNotification"
    heartbeat: "Heartbeat"
    meter_values: "MeterValues"
    sign_charging_station_certificate: "SignChargingStationCertificate"
    sign_v2_g_certificate: "SignV2GCertificate"
    status_notification: "StatusNotification"
    transaction_event: "TransactionEvent"


class Monitor:
    upper_threshold: "UpperThreshold"
    lower_threshold: "LowerThreshold"
    delta: "Delta"
    periodic: "Periodic"
    periodic_clock_aligned: "PeriodicClockAligned"


class MonitoringCriterion:
    threshold_monitoring: "ThresholdMonitoring"
    delta_monitoring: "DeltaMonitoring"
    periodic_monitoring: "PeriodicMonitoring"


class Mutability:
    read_only: "ReadOnly"
    write_only: "WriteOnly"
    read_write: "ReadWrite"


class OCPPInterface:
    wired0: "Wired0"
    wired1: "Wired1"
    wired2: "Wired2"
    wired3: "Wired3"
    wireless0: "Wireless0"
    wireless1: "Wireless1"
    wireless2: "Wireless2"
    wireless3: "Wireless3"


class OCPPTransport:
    json: "JSON"
    soap: "SOAP"


class OCPPVersion:
    ocpp12: "OCPP12"
    ocpp15: "OCPP15"
    ocpp16: "OCPP16"
    ocpp20: "OCPP20"


class Phase:
    l1: "L1"
    l2: "L2"
    l3: "L3"
    n: "N"
    l1_n: "L1-N"
    l2_n: "L2-N"
    l3_n: "L3-N"
    l1_l2: "L1-L2"
    l2_l3: "L2-L3"
    l3_l1: "L3-L1"


class ReadingContext:
    interruption._begin: "Interruption.Begin"
    interruption._end: "Interruption.End"
    other: "Other"
    sample._clock: "Sample.Clock"
    sample._periodic: "Sample.Periodic"
    transaction._begin: "Transaction.Begin"
    transaction._end: "Transaction.End"
    trigger: "Trigger"


class Reason:
    de_authorized: "DeAuthorized"
    emergency_stop: "EmergencyStop"
    energy_limit_reached: "EnergyLimitReached"
    ev_disconnected: "EVDisconnected"
    ground_fault: "GroundFault"
    immediate_reset: "ImmediateReset"
    local: "Local"
    local_out_of_credit: "LocalOutOfCredit"
    master_pass: "MasterPass"
    other: "Other"
    overcurrent_fault: "OvercurrentFault"
    power_loss: "PowerLoss"
    power_quality: "PowerQuality"
    reboot: "Reboot"
    remote: "Remote"
    soc_limit_reached: "SOCLimitReached"
    stopped_by_ev: "StoppedByEV"
    time_limit_reached: "TimeLimitReached"
    timeout: "Timeout"
    unlock_command: "UnlockCommand"


class RecurrencyKind:
    daily: "Daily"
    weekly: "Weekly"


class SetMonitoringStatus:
    accepted: "Accepted"
    unknown_component: "UnknownComponent"
    unknown_variable: "UnknownVariable"
    unsupported_monitor_type: "UnsupportedMonitorType"
    rejected: "Rejected"
    out_of_range: "OutOfRange"
    duplicate: "Duplicate"


class SetVariableStatus:
    accepted: "Accepted"
    rejected: "Rejected"
    invalid_value: "InvalidValue"
    unknown_component: "UnknownComponent"
    unknown_variable: "UnknownVariable"
    not_supported_attribute_type: "NotSupportedAttributeType"
    out_of_range: "OutOfRange"
    reboot_required: "RebootRequired"


class SignatureMethod:
    ecdsap256_sha256: "ECDSAP256SHA256"
    ecdsap384_sha384: "ECDSAP384SHA384"
    ecdsa192_sha256: "ECDSA192SHA256"


class TransactionEvent:
    ended: "Ended"
    started: "Started"
    updated: "Updated"


class TriggerReason:
    authorized: "Authorized"
    cable_plugged_in: "CablePluggedIn"
    charging_rate_changed: "ChargingRateChanged"
    charging_state_changed: "ChargingStateChanged"
    deauthorized: "Deauthorized"
    energy_limit_reached: "EnergyLimitReached"
    ev_communication_lost: "EVCommunicationLost"
    ev_connect_timeout: "EVConnectTimeout"
    meter_value_clock: "MeterValueClock"
    meter_value_periodic: "MeterValuePeriodic"
    time_limit_reached: "TimeLimitReached"
    trigger: "Trigger"
    unlock_command: "UnlockCommand"
    stop_authorized: "StopAuthorized"
    ev_departed: "EVDeparted"
    ev_detected: "EVDetected"
    remote_stop: "RemoteStop"
    remote_start: "RemoteStart"


class Unknown:
    """CancelReservationResponse_v1p0"""
    accepted: "Accepted"
    rejected: "Rejected"


class Unknown:
    """RequestStopTransactionResponse_v1p0"""
    accepted: "Accepted"
    rejected: "Rejected"


class Unknown:
    """BootNotificationResponse_v1p0"""
    accepted: "Accepted"
    pending: "Pending"
    rejected: "Rejected"


class Unknown:
    """StatusNotificationRequest_v1p0"""
    available: "Available"
    occupied: "Occupied"
    reserved: "Reserved"
    unavailable: "Unavailable"
    faulted: "Faulted"


class Unknown:
    """InstallCertificateRequest_v1p0"""
    v2_g_root_certficate: "V2GRootCertficate"
    mo_root_certificate: "MORootCertificate"
    cso_sub_ca1: "CSOSubCA1"
    cso_sub_ca2: "CSOSubCA2"
    csms_root_certificate: "CSMSRootCertificate"
    manufacturer_root_certificate: "ManufacturerRootCertificate"


class Unknown:
    """DeleteCertificateResponse_v1p0"""
    accepted: "Accepted"
    failed: "Failed"
    not_found: "NotFound"


class Unknown:
    """SignCertificateResponse_v1p0"""
    accepted: "Accepted"
    rejected: "Rejected"


class Unknown:
    """ClearDisplayMessageResponse_v1p0"""
    accepted: "Accepted"
    unknown: "Unknown"


class Unknown:
    """ClearedChargingLimitRequest_v1p0"""
    ems: "EMS"
    other: "Other"
    so: "SO"
    cso: "CSO"


class Unknown:
    """CertificateSignedRequest_v1p0"""
    charging_station_certificate: "ChargingStationCertificate"
    v2_g_certificate: "V2GCertificate"


class Unknown:
    """GetCompositeScheduleRequest_v1p0"""
    w: "W"
    a: "A"


class Unknown:
    """GetBaseReportRequest_v1p0"""
    configuration_inventory: "ConfigurationInventory"
    full_inventory: "FullInventory"
    summary_inventory: "SummaryInventory"


class Unknown:
    """ClearCacheResponse_v1p0"""
    accepted: "Accepted"
    rejected: "Rejected"


class Unknown:
    """GetCertificateStatusResponse_v1p0"""
    accepted: "Accepted"
    rejected: "Rejected"


class Unknown:
    """UnlockConnectorResponse_v1p0"""
    unlocked: "Unlocked"
    unlock_failed: "UnlockFailed"


class Unknown:
    """SetMonitoringLevelResponse_v1p0"""
    accepted: "Accepted"
    rejected: "Rejected"


class Unknown:
    """SetNetworkProfileResponse_v1p0"""
    accepted: "Accepted"
    rejected: "Rejected"
    failed: "Failed"


class Unknown:
    """CustomerInformationResponse_v1p0"""
    accepted: "Accepted"
    rejected: "Rejected"
    invalid: "Invalid"


class Unknown:
    """NotifyEVChargingNeedsResponse_v1p0"""
    accepted: "Accepted"
    rejected: "Rejected"
    processing: "Processing"


class Unknown:
    """SetMonitoringBaseResponse_v1p0"""
    accepted: "Accepted"
    rejected: "Rejected"
    not_supported: "NotSupported"


class Unknown:
    """RequestStartTransactionResponse_v1p0"""
    accepted: "Accepted"
    rejected: "Rejected"


class Unknown:
    """ReservationStatusUpdateRequest_v1p0"""
    expired: "Expired"
    removed: "Removed"


class Unknown:
    """PublishFirmwareStatusNotificationRequest_v1p0"""
    downloaded: "Downloaded"
    download_failed: "DownloadFailed"
    downloading: "Downloading"
    download_scheduled: "DownloadScheduled"
    download_paused: "DownloadPaused"
    publish_failed: "PublishFailed"
    published: "Published"
    invalid_checksum: "InvalidChecksum"
    checksum_verified: "ChecksumVerified"


class Unknown:
    """NotifyEVChargingScheduleResponse_v1p0"""
    accepted: "Accepted"
    rejected: "Rejected"


class Unknown:
    """ResetResponse_v1p0"""
    accepted: "Accepted"
    rejected: "Rejected"
    scheduled: "Scheduled"


class Unknown:
    """GetDisplayMessagesRequest_v1p0"""
    always_front: "AlwaysFront"
    in_front: "InFront"
    normal_cycle: "NormalCycle"


class Unknown:
    """GetDisplayMessagesRequest_v1p0"""
    charging: "Charging"
    faulted: "Faulted"
    idle: "Idle"
    unavailable: "Unavailable"


class Unknown:
    """GetInstalledCertificateIdsRequest_v1p0"""
    v2_g_root_certficate: "V2GRootCertficate"
    mo_root_certificate: "MORootCertificate"
    cso_sub_ca1: "CSOSubCA1"
    cso_sub_ca2: "CSOSubCA2"
    csms_root_certificate: "CSMSRootCertificate"
    manufacturer_root_certificate: "ManufacturerRootCertificate"


class Unknown:
    """GetDisplayMessagesResponse_v1p0"""
    accepted: "Accepted"
    unknown: "Unknown"


class Unknown:
    """ReserveNowResponse_v1p0"""
    accepted: "Accepted"
    faulted: "Faulted"
    occupied: "Occupied"
    rejected: "Rejected"
    unavailable: "Unavailable"


class Unknown:
    """SignCertificateRequest_v1p0"""
    charging_station_certificate: "ChargingStationCertificate"
    v2_g_certificate: "V2GCertificate"


class Unknown:
    """InstallCertificateResponse_v1p0"""
    accepted: "Accepted"
    signature_error: "SignatureError"
    certificate_expired: "CertificateExpired"
    certificate_revoked: "CertificateRevoked"
    no_certificate_available: "NoCertificateAvailable"
    cert_chain_error: "CertChainError"
    contract_cancelled: "ContractCancelled"


class Unknown:
    """SecurityEventNotificationRequest_v1p0"""
    firmware_updated: "FirmwareUpdated"
    failed_to_authenticate_at_csms: "FailedToAuthenticateAtCsms"
    csms_failed_to_authenticate: "CsmsFailedToAuthenticate"
    setting_system_time: "SettingSystemTime"
    startup_of_the_device: "StartupOfTheDevice"
    reset_or_reboot: "ResetOrReboot"
    security_log_was_cleared: "SecurityLogWasCleared"
    reconfiguration_of_security_parameters: "ReconfigurationOfSecurityParameters"
    memory_exhaustion: "MemoryExhaustion"
    invalid_messages: "InvalidMessages"
    attempted_replay_attacks: "AttemptedReplayAttacks"
    tamper_detection_activated: "TamperDetectionActivated"
    invalid_firmware_signature: "InvalidFirmwareSignature"
    invalid_firmware_signing_certificate: "InvalidFirmwareSigningCertificate"
    invalid_csms_certificate: "InvalidCsmsCertificate"
    invalid_charging_station_certificate: "InvalidChargingStationCertificate"
    invalid_tls_version: "InvalidTLSVersion"
    invalid_tls_cipher_suite: "InvalidTLSCipherSuite"


class Unknown:
    """SetMonitoringBaseRequest_v1p0"""
    all: "All"
    factory_default: "FactoryDefault"
    none: "None"


class Unknown:
    """GetMonitoringReportResponse_v1p0"""
    accepted: "Accepted"
    rejected: "Rejected"
    not_supported: "NotSupported"


class Unknown:
    """UpdateFirmwareResponse_v1p0"""
    accepted: "Accepted"
    rejected: "Rejected"
    accepted_canceled: "AcceptedCanceled"


class Unknown:
    """GetChargingProfilesResponse_v1p0"""
    accepted: "Accepted"
    no_profiles: "NoProfiles"


class Unknown:
    """CertificateSignedResponse_v1p0"""
    accepted: "Accepted"
    rejected: "Rejected"


class Unknown:
    """DataTransferResponse_v1p0"""
    accepted: "Accepted"
    rejected: "Rejected"
    unknown_message_id: "UnknownMessageId"
    unknown_vendor_id: "UnknownVendorId"


class Unknown:
    """NotifyCentralChargingNeedsResponse_v1p0"""
    accepted: "Accepted"
    rejected: "Rejected"


class Unknown:
    """LogStatusNotificationRequest_v1p0"""
    bad_message: "BadMessage"
    idle: "Idle"
    not_supported_operation: "NotSupportedOperation"
    permission_denied: "PermissionDenied"
    uploaded: "Uploaded"
    upload_failure: "UploadFailure"
    uploading: "Uploading"


class Unknown:
    """GetBaseReportResponse_v1p0"""
    accepted: "Accepted"
    rejected: "Rejected"
    not_supported: "NotSupported"


class Unknown:
    """PublishFirmwareResponse_v1p0"""
    accepted: "Accepted"
    rejected: "Rejected"


class Unknown:
    """ChangeAvailabilityResponse_v1p0"""
    accepted: "Accepted"
    rejected: "Rejected"
    scheduled: "Scheduled"


class Unknown:
    """ResetRequest_v1p0"""
    immediate: "Immediate"
    on_idle: "OnIdle"


class Unknown:
    """SendLocalListResponse_v1p0"""
    accepted: "Accepted"
    failed: "Failed"
    version_mismatch: "VersionMismatch"


class Unknown:
    """ChangeAvailabilityRequest_v1p0"""
    inoperative: "Inoperative"
    operative: "Operative"


class Unknown:
    """TriggerMessageResponse_v1p0"""
    accepted: "Accepted"
    rejected: "Rejected"
    not_implemented: "NotImplemented"


class Unknown:
    """Update15118EVCertificateResponse_v1p0"""
    accepted: "Accepted"
    failed: "Failed"


class Unknown:
    """ClearChargingProfileResponse_v1p0"""
    accepted: "Accepted"
    unknown: "Unknown"


class Unknown:
    """GetReportResponse_v1p0"""
    accepted: "Accepted"
    rejected: "Rejected"
    not_supported: "NotSupported"


class Unknown:
    """UnpublishFirmwareResponse_v1p0"""
    download_ongoing: "DownloadOngoing"
    no_firmware: "NoFirmware"
    unpublished: "Unpublished"


class Unknown:
    """FirmwareStatusNotificationRequest_v1p0"""
    certificate_verified: "CertificateVerified"
    downloaded: "Downloaded"
    download_failed: "DownloadFailed"
    downloading: "Downloading"
    download_scheduled: "DownloadScheduled"
    download_paused: "DownloadPaused"
    idle: "Idle"
    installation_failed: "InstallationFailed"
    installing: "Installing"
    installed: "Installed"
    install_rebooting: "InstallRebooting"
    install_scheduled: "InstallScheduled"
    install_verification_failed: "InstallVerificationFailed"
    invalid_signature: "InvalidSignature"
    invalid_certificate: "InvalidCertificate"
    revoked_certificate: "RevokedCertificate"
    publish_failed: "PublishFailed"
    signature_verified: "SignatureVerified"


class Unknown:
    """GetLogResponse_v1p0"""
    accepted: "Accepted"
    rejected: "Rejected"
    accepted_canceled: "AcceptedCanceled"


class Unknown:
    """SetDisplayMessageResponse_v1p0"""
    accepted: "Accepted"
    not_supported_message_format: "NotSupportedMessageFormat"
    rejected: "Rejected"
    not_supported_priority: "NotSupportedPriority"
    not_supported_state: "NotSupportedState"
    unknown_transaction: "UnknownTransaction"


class Unknown:
    """Renegotiate15118ScheduleResponse_v1p0"""
    accepted: "Accepted"
    rejected: "Rejected"


class Unknown:
    """SetChargingProfileResponse_v1p0"""
    accepted: "Accepted"
    rejected: "Rejected"


class Update:
    differential: "Differential"
    full: "Full"


class VPN:
    ik_ev2: "IKEv2"
    ip_sec: "IPSec"
    l2_tp: "L2TP"
    pptp: "PPTP"


105
