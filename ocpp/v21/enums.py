try:
    # breaking change introduced in python 3.11
    from enum import StrEnum
except ImportError:  # pragma: no cover
    from enum import Enum  # pragma: no cover

    class StrEnum(str, Enum):  # pragma: no cover
        pass  # pragma: no cover


class Action(StrEnum):
    """An Action is a required part of a Call message."""

    afrr_signal = "AFRRSignal"
    adjust_periodic_event_stream = "AdjustPeriodicEventStream"
    authorize = "Authorize"
    battery_swap = "BatterySwap"
    boot_notification = "BootNotification"
    cancel_reservation = "CancelReservation"
    certificate_signed = "CertificateSigned"
    change_availability = "ChangeAvailability"
    change_transaction_tariff = "ChangeTransactionTariff"
    clear_cache = "ClearCache"
    clear_charging_profile = "ClearChargingProfile"
    clear_der_control = "ClearDERControl"
    clear_display_message = "ClearDisplayMessage"
    clear_tariffs = "ClearTariffs"
    clear_variable_monitoring = "ClearVariableMonitoring"
    cleared_charging_limit = "ClearedChargingLimit"
    close_periodic_event_stream = "ClosePeriodicEventStream"
    cost_updated = "CostUpdated"
    customer_information = "CustomerInformation"
    data_transfer = "DataTransfer"
    delete_certificate = "DeleteCertificate"
    firmware_status_notification = "FirmwareStatusNotification"
    get15118_ev_certificate = "Get15118EVCertificate"
    get_base_report = "GetBaseReport"
    get_certificate_chain_status = "GetCertificateChainStatus"
    get_certificate_status = "GetCertificateStatus"
    get_charging_profiles = "GetChargingProfiles"
    get_composite_schedule = "GetCompositeSchedule"
    get_der_control = "GetDERControl"
    get_display_messages = "GetDisplayMessages"
    get_installed_certificate_ids = "GetInstalledCertificateIds"
    get_local_list_version = "GetLocalListVersion"
    get_log = "GetLog"
    get_monitoring_report = "GetMonitoringReport"
    get_periodic_event_stream = "GetPeriodicEventStream"
    get_report = "GetReport"
    get_tariffs = "GetTariffs"
    get_transaction_status = "GetTransactionStatus"
    get_variables = "GetVariables"
    heartbeat = "Heartbeat"
    install_certificate = "InstallCertificate"
    log_status_notification = "LogStatusNotification"
    meter_values = "MeterValues"
    notify_allowed_energy_transfer = "NotifyAllowedEnergyTransfer"
    notify_charging_limit = "NotifyChargingLimit"
    notify_customer_information = "NotifyCustomerInformation"
    notify_der_alarm = "NotifyDERAlarm"
    notify_der_start_stop = "NotifyDERStartStop"
    notify_display_messages = "NotifyDisplayMessages"
    notify_ev_charging_needs = "NotifyEVChargingNeeds"
    notify_ev_charging_schedule = "NotifyEVChargingSchedule"
    notify_event = "NotifyEvent"
    notify_monitoring_report = "NotifyMonitoringReport"
    notify_priority_charging = "NotifyPriorityCharging"
    notify_report = "NotifyReport"
    notify_settlement = "NotifySettlement"
    notify_web_payment_started = "NotifyWebPaymentStarted"
    open_periodic_event_stream = "OpenPeriodicEventStream"
    publish_firmware = "PublishFirmware"
    publish_firmware_status_notification = "PublishFirmwareStatusNotification"
    pull_dynamic_schedule_update = "PullDynamicScheduleUpdate"
    report_charging_profiles = "ReportChargingProfiles"
    report_der_control = "ReportDERControl"
    request_battery_swap = "RequestBatterySwap"
    request_start_transaction = "RequestStartTransaction"
    request_stop_transaction = "RequestStopTransaction"
    reservation_status_update = "ReservationStatusUpdate"
    reserve_now = "ReserveNow"
    reset = "Reset"
    security_event_notification = "SecurityEventNotification"
    send_local_list = "SendLocalList"
    set_charging_profile = "SetChargingProfile"
    set_der_control = "SetDERControl"
    set_default_tariff = "SetDefaultTariff"
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
    update_dynamic_schedule = "UpdateDynamicSchedule"
    update_firmware = "UpdateFirmware"
    use_priority_charging = "UsePriorityCharging"
    vat_number_validation = "VatNumberValidation"


class APNAuthenticationEnumType(StrEnum):
    pap = "PAP"
    chap = "CHAP"
    none = "NONE"
    auto = "AUTO"


class AttributeEnumType(StrEnum):
    actual = "Actual"
    target = "Target"
    min_set = "MinSet"
    max_set = "MaxSet"


class AuthorizationStatusEnumType(StrEnum):
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


class AuthorizeCertificateStatusEnumType(StrEnum):
    accepted = "Accepted"
    signature_error = "SignatureError"
    certificate_expired = "CertificateExpired"
    certificate_revoked = "CertificateRevoked"
    no_certificate_available = "NoCertificateAvailable"
    cert_chain_error = "CertChainError"
    contract_cancelled = "ContractCancelled"


class BatterySwapEventEnumType(StrEnum):
    battery_in = "BatteryIn"
    battery_out = "BatteryOut"
    battery_out_timeout = "BatteryOutTimeout"


class BootReasonEnumType(StrEnum):
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
    accepted = "Accepted"
    rejected = "Rejected"


class CertificateActionEnumType(StrEnum):
    install = "Install"
    update = "Update"


class CertificateSignedStatusEnumType(StrEnum):
    accepted = "Accepted"
    rejected = "Rejected"


class CertificateSigningUseEnumType(StrEnum):
    charging_station_certificate = "ChargingStationCertificate"
    v2g_certificate = "V2GCertificate"
    v2g20_certificate = "V2G20Certificate"


class CertificateStatusEnumType(StrEnum):
    good = "Good"
    revoked = "Revoked"
    unknown = "Unknown"
    failed = "Failed"


class CertificateStatusSourceEnumType(StrEnum):
    crl = "CRL"
    ocsp = "OCSP"


class ChangeAvailabilityStatusEnumType(StrEnum):
    accepted = "Accepted"
    rejected = "Rejected"
    scheduled = "Scheduled"


class ChargingProfileKindEnumType(StrEnum):
    absolute = "Absolute"
    recurring = "Recurring"
    relative = "Relative"
    dynamic = "Dynamic"


class ChargingProfilePurposeEnumType(StrEnum):
    charging_station_external_constraints = "ChargingStationExternalConstraints"
    charging_station_max_profile = "ChargingStationMaxProfile"
    tx_default_profile = "TxDefaultProfile"
    tx_profile = "TxProfile"
    priority_charging = "PriorityCharging"
    local_generation = "LocalGeneration"


class ChargingProfileStatusEnumType(StrEnum):
    accepted = "Accepted"
    rejected = "Rejected"


class ChargingRateUnitEnumType(StrEnum):
    w = "W"
    a = "A"


class ChargingStateEnumType(StrEnum):
    ev_connected = "EVConnected"
    charging = "Charging"
    suspended_ev = "SuspendedEV"
    suspended_evse = "SuspendedEVSE"
    idle = "Idle"


class ClearCacheStatusEnumType(StrEnum):
    accepted = "Accepted"
    rejected = "Rejected"


class ClearChargingProfileStatusEnumType(StrEnum):
    accepted = "Accepted"
    unknown = "Unknown"


class ClearMessageStatusEnumType(StrEnum):
    accepted = "Accepted"
    unknown = "Unknown"
    rejected = "Rejected"


class ClearMonitoringStatusEnumType(StrEnum):
    accepted = "Accepted"
    rejected = "Rejected"
    not_found = "NotFound"


class ComponentCriterionEnumType(StrEnum):
    active = "Active"
    available = "Available"
    enabled = "Enabled"
    problem = "Problem"


class ConnectorStatusEnumType(StrEnum):
    available = "Available"
    occupied = "Occupied"
    reserved = "Reserved"
    unavailable = "Unavailable"
    faulted = "Faulted"


class ControlModeEnumType(StrEnum):
    scheduled_control = "ScheduledControl"
    dynamic_control = "DynamicControl"


class CostDimensionEnumType(StrEnum):
    energy = "Energy"
    max_current = "MaxCurrent"
    min_current = "MinCurrent"
    max_power = "MaxPower"
    min_power = "MinPower"
    idle_t_ime = "IdleTIme"
    charging_time = "ChargingTime"


class CostKindEnumType(StrEnum):
    carbon_dioxide_emission = "CarbonDioxideEmission"
    relative_price_percentage = "RelativePricePercentage"
    renewable_generation_percentage = "RenewableGenerationPercentage"


class CustomerInformationStatusEnumType(StrEnum):
    accepted = "Accepted"
    rejected = "Rejected"
    invalid = "Invalid"


class DERControlEnumType(StrEnum):
    enter_service = "EnterService"
    freq_droop = "FreqDroop"
    freq_watt = "FreqWatt"
    fixed_pf_absorb = "FixedPFAbsorb"
    fixed_pf_inject = "FixedPFInject"
    fixed_var = "FixedVar"
    gradients = "Gradients"
    hf_must_trip = "HFMustTrip"
    hf_may_trip = "HFMayTrip"
    hv_must_trip = "HVMustTrip"
    hv_mom_cess = "HVMomCess"
    hv_may_trip = "HVMayTrip"
    limit_max_discharge = "LimitMaxDischarge"
    lf_must_trip = "LFMustTrip"
    lv_must_trip = "LVMustTrip"
    lv_mom_cess = "LVMomCess"
    lv_may_trip = "LVMayTrip"
    power_monitoring_must_trip = "PowerMonitoringMustTrip"
    volt_var = "VoltVar"
    volt_watt = "VoltWatt"
    watt_pf = "WattPF"
    watt_var = "WattVar"


class DERControlStatusEnumType(StrEnum):
    accepted = "Accepted"
    rejected = "Rejected"
    not_supported = "NotSupported"
    not_found = "NotFound"


class DERUnitEnumType(StrEnum):
    not__applicable = "Not_Applicable"
    pct_maxw = "PctMaxW"
    pct_max_var = "PctMaxVar"
    pct_w_avail = "PctWAvail"
    pct_var_avail = "PctVarAvail"
    pct_effectivev = "PctEffectiveV"


class DataEnumType(StrEnum):
    string = "string"
    decimal = "decimal"
    integer = "integer"
    date_time = "dateTime"
    boolean = "boolean"
    option_list = "OptionList"
    sequence_list = "SequenceList"
    member_list = "MemberList"


class DataTransferStatusEnumType(StrEnum):
    accepted = "Accepted"
    rejected = "Rejected"
    unknown_message_id = "UnknownMessageId"
    unknown_vendor_id = "UnknownVendorId"


class DayOfWeekEnumType(StrEnum):
    monday = "Monday"
    tuesday = "Tuesday"
    wednesday = "Wednesday"
    thursday = "Thursday"
    friday = "Friday"
    saturday = "Saturday"
    sunday = "Sunday"


class DeleteCertificateStatusEnumType(StrEnum):
    accepted = "Accepted"
    failed = "Failed"
    not_found = "NotFound"


class DisplayMessageStatusEnumType(StrEnum):
    accepted = "Accepted"
    not_supported_message_format = "NotSupportedMessageFormat"
    rejected = "Rejected"
    not_supported_priority = "NotSupportedPriority"
    not_supported_state = "NotSupportedState"
    unknown_transaction = "UnknownTransaction"
    language_not_supported = "LanguageNotSupported"


class EnergyTransferModeEnumType(StrEnum):
    ac_single_phase = "AC_single_phase"
    ac_two_phase = "AC_two_phase"
    ac_three_phase = "AC_three_phase"
    dc = "DC"
    ac_bpt = "AC_BPT"
    ac_bpt_der = "AC_BPT_DER"
    ac_der = "AC_DER"
    dc_bpt = "DC_BPT"
    dc_acdp = "DC_ACDP"
    dc_acdp_bpt = "DC_ACDP_BPT"
    wpt = "WPT"


class EventNotificationEnumType(StrEnum):
    hard_wired_notification = "HardWiredNotification"
    hard_wired_monitor = "HardWiredMonitor"
    preconfigured_monitor = "PreconfiguredMonitor"
    custom_monitor = "CustomMonitor"


class EventTriggerEnumType(StrEnum):
    alerting = "Alerting"
    delta = "Delta"
    periodic = "Periodic"


class EvseKindEnumType(StrEnum):
    ac = "AC"
    dc = "DC"


class FirmwareStatusEnumType(StrEnum):
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
    accepted = "Accepted"
    rejected = "Rejected"
    not_supported = "NotSupported"
    empty_result_set = "EmptyResultSet"


class GenericStatusEnumType(StrEnum):
    accepted = "Accepted"
    rejected = "Rejected"


class GetCertificateIdUseEnumType(StrEnum):
    v2g_root_certificate = "V2GRootCertificate"
    mo_root_certificate = "MORootCertificate"
    csms_root_certificate = "CSMSRootCertificate"
    v2g_certificate_chain = "V2GCertificateChain"
    manufacturer_root_certificate = "ManufacturerRootCertificate"
    oem_root_certificate = "OEMRootCertificate"


class GetCertificateStatusEnumType(StrEnum):
    accepted = "Accepted"
    failed = "Failed"


class GetChargingProfileStatusEnumType(StrEnum):
    accepted = "Accepted"
    no_profiles = "NoProfiles"


class GetDisplayMessagesStatusEnumType(StrEnum):
    accepted = "Accepted"
    unknown = "Unknown"


class GetInstalledCertificateStatusEnumType(StrEnum):
    accepted = "Accepted"
    not_found = "NotFound"


class GetVariableStatusEnumType(StrEnum):
    accepted = "Accepted"
    rejected = "Rejected"
    unknown_component = "UnknownComponent"
    unknown_variable = "UnknownVariable"
    not_supported_attribute_type = "NotSupportedAttributeType"


class GridEventFaultEnumType(StrEnum):
    current_imbalance = "CurrentImbalance"
    local_emergency = "LocalEmergency"
    low_input_power = "LowInputPower"
    over_current = "OverCurrent"
    over_frequency = "OverFrequency"
    over_voltage = "OverVoltage"
    phase_rotation = "PhaseRotation"
    remote_emergency = "RemoteEmergency"
    under_frequency = "UnderFrequency"
    under_voltage = "UnderVoltage"
    voltage_imbalance = "VoltageImbalance"


class HashAlgorithmEnumType(StrEnum):
    sha256 = "SHA256"
    sha384 = "SHA384"
    sha512 = "SHA512"


class InstallCertificateStatusEnumType(StrEnum):
    accepted = "Accepted"
    rejected = "Rejected"
    failed = "Failed"


class InstallCertificateUseEnumType(StrEnum):
    v2g_root_certificate = "V2GRootCertificate"
    mo_root_certificate = "MORootCertificate"
    manufacturer_root_certificate = "ManufacturerRootCertificate"
    csms_root_certificate = "CSMSRootCertificate"
    oem_root_certificate = "OEMRootCertificate"


class IslandingDetectionEnumType(StrEnum):
    no_anti_islanding_support = "NoAntiIslandingSupport"
    ro_cof = "RoCoF"
    uvp_ovp = "UVP_OVP"
    ufp_ofp = "UFP_OFP"
    voltage_vector_shift = "VoltageVectorShift"
    zero_crossing_detection = "ZeroCrossingDetection"
    other_passive = "OtherPassive"
    impedance_measurement = "ImpedanceMeasurement"
    impedance_at_frequency = "ImpedanceAtFrequency"
    slip_mode_frequency_shift = "SlipModeFrequencyShift"
    sandia_frequency_shift = "SandiaFrequencyShift"
    sandia_voltage_shift = "SandiaVoltageShift"
    frequency_jump = "FrequencyJump"
    rclq_factor = "RCLQFactor"
    other_active = "OtherActive"


class Iso15118EVCertificateStatusEnumType(StrEnum):
    accepted = "Accepted"
    failed = "Failed"


class LocationEnumType(StrEnum):
    body = "Body"
    cable = "Cable"
    ev = "EV"
    inlet = "Inlet"
    outlet = "Outlet"
    upstream = "Upstream"


class LogEnumType(StrEnum):
    diagnostics_log = "DiagnosticsLog"
    security_log = "SecurityLog"
    data_collector_log = "DataCollectorLog"


class LogStatusEnumType(StrEnum):
    accepted = "Accepted"
    rejected = "Rejected"
    accepted_canceled = "AcceptedCanceled"


class MeasurandEnumType(StrEnum):
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
    energy_active_import_cable_loss = "Energy.Active.Import.CableLoss"
    energy_active_import_local_generation_register = (
        "Energy.Active.Import.LocalGeneration.Register"
    )
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


class MessageFormatEnumType(StrEnum):
    ascii = "ASCII"
    html = "HTML"
    uri = "URI"
    utf8 = "UTF8"
    qrcode = "QRCODE"


class MessagePriorityEnumType(StrEnum):
    always_front = "AlwaysFront"
    in_front = "InFront"
    normal_cycle = "NormalCycle"


class MessageStateEnumType(StrEnum):
    charging = "Charging"
    faulted = "Faulted"
    idle = "Idle"
    unavailable = "Unavailable"
    suspended = "Suspended"
    discharging = "Discharging"


class MessageTriggerEnumType(StrEnum):
    boot_notification = "BootNotification"
    log_status_notification = "LogStatusNotification"
    firmware_status_notification = "FirmwareStatusNotification"
    heartbeat = "Heartbeat"
    meter_values = "MeterValues"
    sign_charging_station_certificate = "SignChargingStationCertificate"
    sign_v2g_certificate = "SignV2GCertificate"
    sign_v2g20_certificate = "SignV2G20Certificate"
    status_notification = "StatusNotification"
    transaction_event = "TransactionEvent"
    sign_combined_certificate = "SignCombinedCertificate"
    publish_firmware_status_notification = "PublishFirmwareStatusNotification"
    custom_trigger = "CustomTrigger"


class MobilityNeedsModeEnumType(StrEnum):
    evcc = "EVCC"
    evcc_secc = "EVCC_SECC"


class MonitorEnumType(StrEnum):
    upper_threshold = "UpperThreshold"
    lower_threshold = "LowerThreshold"
    delta = "Delta"
    periodic = "Periodic"
    periodic_clock_aligned = "PeriodicClockAligned"
    target_delta = "TargetDelta"
    target_delta_relative = "TargetDeltaRelative"


class MonitoringBaseEnumType(StrEnum):
    all = "All"
    factory_default = "FactoryDefault"
    hard_wired_only = "HardWiredOnly"


class MonitoringCriterionEnumType(StrEnum):
    threshold_monitoring = "ThresholdMonitoring"
    delta_monitoring = "DeltaMonitoring"
    periodic_monitoring = "PeriodicMonitoring"


class MutabilityEnumType(StrEnum):
    read_only = "ReadOnly"
    write_only = "WriteOnly"
    read_write = "ReadWrite"


class NotifyAllowedEnergyTransferStatusEnumType(StrEnum):
    accepted = "Accepted"
    rejected = "Rejected"


class NotifyEVChargingNeedsStatusEnumType(StrEnum):
    accepted = "Accepted"
    rejected = "Rejected"
    processing = "Processing"
    no_charging_profile = "NoChargingProfile"


class OCPPInterfaceEnumType(StrEnum):
    wired0 = "Wired0"
    wired1 = "Wired1"
    wired2 = "Wired2"
    wired3 = "Wired3"
    wireless0 = "Wireless0"
    wireless1 = "Wireless1"
    wireless2 = "Wireless2"
    wireless3 = "Wireless3"
    any = "Any"


class OCPPTransportEnumType(StrEnum):
    soap = "SOAP"
    json = "JSON"


class OCPPVersionEnumType(StrEnum):
    ocpp12 = "OCPP12"
    ocpp15 = "OCPP15"
    ocpp16 = "OCPP16"
    ocpp20 = "OCPP20"
    ocpp201 = "OCPP201"
    ocpp21 = "OCPP21"


class OperationModeEnumType(StrEnum):
    idle = "Idle"
    charging_only = "ChargingOnly"
    central_setpoint = "CentralSetpoint"
    external_setpoint = "ExternalSetpoint"
    external_limits = "ExternalLimits"
    central_frequency = "CentralFrequency"
    local_frequency = "LocalFrequency"
    local_load_balancing = "LocalLoadBalancing"


class OperationalStatusEnumType(StrEnum):
    inoperative = "Inoperative"
    operative = "Operative"


class PaymentStatusEnumType(StrEnum):
    settled = "Settled"
    canceled = "Canceled"
    rejected = "Rejected"
    failed = "Failed"


class PhaseEnumType(StrEnum):
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


class PowerDuringCessationEnumType(StrEnum):
    active = "Active"
    reactive = "Reactive"


class PreconditioningStatusEnumType(StrEnum):
    unknown = "Unknown"
    ready = "Ready"
    not_ready = "NotReady"
    preconditioning = "Preconditioning"


class PriorityChargingStatusEnumType(StrEnum):
    accepted = "Accepted"
    rejected = "Rejected"
    no_profile = "NoProfile"


class PublishFirmwareStatusEnumType(StrEnum):
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
    interruption_begin = "Interruption.Begin"
    interruption_end = "Interruption.End"
    other = "Other"
    sample_clock = "Sample.Clock"
    sample_periodic = "Sample.Periodic"
    transaction_begin = "Transaction.Begin"
    transaction_end = "Transaction.End"
    trigger = "Trigger"


class ReasonEnumType(StrEnum):
    de_authorized = "DeAuthorized"
    emergency_stop = "EmergencyStop"
    energy_limit_reached = "EnergyLimitReached"
    ev_disconnected = "EVDisconnected"
    ground_fault = "GroundFault"
    immediate_reset = "ImmediateReset"
    master_pass = "MasterPass"
    local = "Local"
    local_out_of_credit = "LocalOutOfCredit"
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
    req_energy_transfer_rejected = "ReqEnergyTransferRejected"


class RecurrencyKindEnumType(StrEnum):
    daily = "Daily"
    weekly = "Weekly"


class RegistrationStatusEnumType(StrEnum):
    accepted = "Accepted"
    pending = "Pending"
    rejected = "Rejected"


class ReportBaseEnumType(StrEnum):
    configuration_inventory = "ConfigurationInventory"
    full_inventory = "FullInventory"
    summary_inventory = "SummaryInventory"


class RequestStartStopStatusEnumType(StrEnum):
    accepted = "Accepted"
    rejected = "Rejected"


class ReservationUpdateStatusEnumType(StrEnum):
    expired = "Expired"
    removed = "Removed"
    no_transaction = "NoTransaction"


class ReserveNowStatusEnumType(StrEnum):
    accepted = "Accepted"
    faulted = "Faulted"
    occupied = "Occupied"
    rejected = "Rejected"
    unavailable = "Unavailable"


class ResetEnumType(StrEnum):
    immediate = "Immediate"
    on_idle = "OnIdle"
    immediate_and_resume = "ImmediateAndResume"


class ResetStatusEnumType(StrEnum):
    accepted = "Accepted"
    rejected = "Rejected"
    scheduled = "Scheduled"


class SendLocalListStatusEnumType(StrEnum):
    accepted = "Accepted"
    failed = "Failed"
    version_mismatch = "VersionMismatch"


class SetMonitoringStatusEnumType(StrEnum):
    accepted = "Accepted"
    unknown_component = "UnknownComponent"
    unknown_variable = "UnknownVariable"
    unsupported_monitor_type = "UnsupportedMonitorType"
    rejected = "Rejected"
    duplicate = "Duplicate"


class SetNetworkProfileStatusEnumType(StrEnum):
    accepted = "Accepted"
    rejected = "Rejected"
    failed = "Failed"


class SetVariableStatusEnumType(StrEnum):
    accepted = "Accepted"
    rejected = "Rejected"
    unknown_component = "UnknownComponent"
    unknown_variable = "UnknownVariable"
    not_supported_attribute_type = "NotSupportedAttributeType"
    reboot_required = "RebootRequired"


class TariffChangeStatusEnumType(StrEnum):
    accepted = "Accepted"
    rejected = "Rejected"
    too_many_elements = "TooManyElements"
    condition_not_supported = "ConditionNotSupported"
    tx_not_found = "TxNotFound"
    no_currency_change = "NoCurrencyChange"


class TariffClearStatusEnumType(StrEnum):
    accepted = "Accepted"
    rejected = "Rejected"
    no_tariff = "NoTariff"


class TariffCostEnumType(StrEnum):
    normal_cost = "NormalCost"
    min_cost = "MinCost"
    max_cost = "MaxCost"


class TariffGetStatusEnumType(StrEnum):
    accepted = "Accepted"
    rejected = "Rejected"
    no_tariff = "NoTariff"


class TariffKindEnumType(StrEnum):
    default_tariff = "DefaultTariff"
    driver_tariff = "DriverTariff"


class TariffSetStatusEnumType(StrEnum):
    accepted = "Accepted"
    rejected = "Rejected"
    too_many_elements = "TooManyElements"
    condition_not_supported = "ConditionNotSupported"
    duplicate_tariff_id = "DuplicateTariffId"


class TransactionEventEnumType(StrEnum):
    ended = "Ended"
    started = "Started"
    updated = "Updated"


class TriggerMessageStatusEnumType(StrEnum):
    accepted = "Accepted"
    rejected = "Rejected"
    not_implemented = "NotImplemented"


class TriggerReasonEnumType(StrEnum):
    abnormal_condition = "AbnormalCondition"
    authorized = "Authorized"
    cable_plugged_in = "CablePluggedIn"
    charging_rate_changed = "ChargingRateChanged"
    charging_state_changed = "ChargingStateChanged"
    cost_limit_reached = "CostLimitReached"
    deauthorized = "Deauthorized"
    energy_limit_reached = "EnergyLimitReached"
    ev_communication_lost = "EVCommunicationLost"
    ev_connect_timeout = "EVConnectTimeout"
    ev_departed = "EVDeparted"
    ev_detected = "EVDetected"
    limit_set = "LimitSet"
    meter_value_clock = "MeterValueClock"
    meter_value_periodic = "MeterValuePeriodic"
    operation_mode_changed = "OperationModeChanged"
    remote_start = "RemoteStart"
    remote_stop = "RemoteStop"
    reset_command = "ResetCommand"
    running_cost = "RunningCost"
    signed_data_received = "SignedDataReceived"
    so_c_limit_reached = "SoCLimitReached"
    stop_authorized = "StopAuthorized"
    tariff_changed = "TariffChanged"
    tariff_not_accepted = "TariffNotAccepted"
    time_limit_reached = "TimeLimitReached"
    trigger = "Trigger"
    tx_resumed = "TxResumed"
    unlock_command = "UnlockCommand"


class UnlockStatusEnumType(StrEnum):
    unlocked = "Unlocked"
    unlock_failed = "UnlockFailed"
    ongoing_authorized_transaction = "OngoingAuthorizedTransaction"
    unknown_connector = "UnknownConnector"


class UnpublishFirmwareStatusEnumType(StrEnum):
    download_ongoing = "DownloadOngoing"
    no_firmware = "NoFirmware"
    unpublished = "Unpublished"


class UpdateEnumType(StrEnum):
    differential = "Differential"
    full = "Full"


class UpdateFirmwareStatusEnumType(StrEnum):
    accepted = "Accepted"
    rejected = "Rejected"
    accepted_canceled = "AcceptedCanceled"
    invalid_certificate = "InvalidCertificate"
    revoked_certificate = "RevokedCertificate"


class UploadLogStatusEnumType(StrEnum):
    bad_message = "BadMessage"
    idle = "Idle"
    not_supported_operation = "NotSupportedOperation"
    permission_denied = "PermissionDenied"
    uploaded = "Uploaded"
    upload_failure = "UploadFailure"
    uploading = "Uploading"
    accepted_canceled = "AcceptedCanceled"


class VPNEnumType(StrEnum):
    ik_ev2 = "IKEv2"
    ip_sec = "IPSec"
    l2_tp = "L2TP"
    pptp = "PPTP"
