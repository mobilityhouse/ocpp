from enum import Enum

# V2X Modified Enums


class Action(str, Enum):
    """An Action is a required part of a Call message."""

    Authorize = "Authorize"
    NotifyEVChargingNeeds = "NotifyEVChargingNeeds"
    NotifyEVChargingSchedule = "NotifyEVChargingSchedule"
    SetChargingProfile = "SetChargingProfile"
    TransactionEvent = "TransactionEvent"
    # V2X added actions
    ModifyChargingProfile = "ModifyChargingProfile"
    NotifyAllowedEnergyTransfer = "NotifyAllowedEnergyTransfer"
    NotifyPriorityCharging = "NotifyPriorityCharging"
    PullChargingProfileUpdate = "PullChargingProfileUpdate"
    UsePriorityCharging = "UsePriorityCharging"


class ChargingProfileKindType(str, Enum):
    """
    "Absolute" Schedule periods are relative to a fixed point in time defined
                in the schedule.
    "Recurring" Schedule restarts periodically at the first schedule period.
    "Relative" Schedule periods are relative to a situation- specific start
                point(such as the start of a session)
    "Dynamic" The schedule consists of only one charging schedule period,
                which is updated dynamically by CSMS.
    """

    absolute = "Absolute"
    recurring = "Recurring"
    relative = "Relative"
    # V2X
    dynamic = "Dynamic"


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

    charging_station_external_constraints = "ChargingStationExternalConstraints"
    charging_station_max_profile = "ChargingStationMaxProfile"
    tx_default_profile = "TxDefaultProfile"
    tx_profile = "TxProfile"
    # V2X added
    priority_charging = "PriorityCharging"


class EnergyTransferModeType(str, Enum):
    """
    Enumeration of energy transfer modes.
    """

    dc = "DC"
    ac_single_phase = "AC_single_phase"
    ac_two_phase = "AC_two_phase"
    ac_three_phase = "AC_three_phase"
    # V2X added
    dc_acdp = "DC_ACDP"
    wpt = "WPT"
    ac_single_phase_bpt = "AC_single_phase_BPT"
    ac_two_phase_bpt = "AC_two_phase_BPT"
    ac_three_phase_bpt = "AC_three_phase_BPT"
    dc_bpt = "DC_BPT"
    dc_acdp_bpt = "DC_ACDP_BPT"


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
    evccid = "EVCCID"


class LogType(str, Enum):
    """
    LogEnumType is used by getLogGetLogRequest
    """

    diagnostics_log = "DiagnosticsLog"
    security_log = "SecurityLog"
    # V2X added
    data_collector_log = "DataCollectorLog"


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
    # V2X added
    current_import_offered = "Current.Import.Offered"
    current_import_minimum = "Current.Import.Minimum"
    current_export_offered = "Current.Export.Offered"
    current_export_minimum = "Current.Export.Minimum"
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
    energy_active_setpoint_interval = "Energy.Active.Setpoint.Interval"
    energy_request_target = "EnergyRequest.Target"
    energy_request_minimum = "EnergyRequest.Minimum"
    energy_request_maximum = "EnergyRequest.Maximum"
    energy_request_minimum_v2x = "EnergyRequest.Minimum.V2X"
    energy_request_maximum_v2x = "EnergyRequest.Maximum.V2X"
    energy_request_bulk = "EnergyRequest.Bulk"
    power_active_setpoint = "Power.Active.Setpoint"
    power_active_residual = "Power.Active.Residual"
    power_import_offered = "Power.Import.Offered"
    power_import_minimum = "Power.Import.Minimum"
    power_export_offered = "Power.Export.Offered"
    power_export_minimum = "Power.Export.Minimum"
    voltage_minimum = "Voltage.Minimum"
    voltage_maximum = "Voltage.Maximum"


class NotifyEVChargingNeedsStatusType(str, Enum):
    """
    Accepted a SASchedule will be provided momentarily.
    Rejected Servoce is Not Available
    Processing The CSMS is gathering information to provide an SASchedule.
    NoChargingProfile CSMS will not provide a charging profile
    """

    accepted = "Accepted"
    rejected = "Rejected"
    processing = "Processing"
    # V2X added
    no_charging_profile = "NoChargingProfile"


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
    sign_v2g_certificate = "SignV2GCertificate"
    status_notification = "StatusNotification"
    transaction_event = "TransactionEvent"
    sign_combined_certificate = "SignCombinedCertificate"
    publish_firmware_status_notification = "PublishFirmwareStatusNotification"
    # V2X added
    v2x_operation_mode_changed = "V2XOperationModeChanged"


# V2X New Enums


class ControlModeType(str, Enum):
    """
    "Dynamic" Dynamic mode, EVSE executes a single schedule by sending
                setpoints to EV at every interval.
    "Scheduled" Scheduled mode, EVSE provides up to three schedules for EV to
                  choose from. EV follows the selected schedule.
    """

    dynamic = "Dynamic"
    scheduled = "Scheduled"


class NotifyAllowedEnergyTransferStatusType(str, Enum):
    accepted = "Accepted"
    rejected = "Rejected"


class PreconditioningStatusType(str, Enum):
    unknown = "Unknown"
    ready = "Ready"
    preconditioning = "Preconditioning"
    not_ready = "NotReady"


class PriorityChargingStatusType(str, Enum):
    accepted = "Accepted"
    rejected = "Rejected"
    no_profile = "NoProfile"


class V2XOperationModeType(str, Enum):
    idle = "Idle"
    charging_only = "ChargingOnly"
    central_setpoint = "CentralSetpoint"
    external_setpoint = "ExternalSetpoint"
    external_limits = "ExternalLimits"
    central_frequency = "CentralFrequency"
    local_frequency = "LocalFrequency"
    local_voltage = "LocalVoltage"
    local_load_balancing = "LocalLoadBalancing"
