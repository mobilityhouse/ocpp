from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from ocpp.v21.enums import (
    APNAuthenticationEnumType,
    AttributeEnumType,
    AuthorizationStatusEnumType,
    CertificateStatusEnumType,
    CertificateStatusSourceEnumType,
    ChargingProfileKindEnumType,
    ChargingProfilePurposeEnumType,
    ChargingRateUnitEnumType,
    ChargingStateEnumType,
    ClearMonitoringStatusEnumType,
    ControlModeEnumType,
    CostDimensionEnumType,
    CostKindEnumType,
    DataEnumType,
    DayOfWeekEnumType,
    DERControlEnumType,
    DERUnitEnumType,
    EnergyTransferModeEnumType,
    EventNotificationEnumType,
    EventTriggerEnumType,
    EvseKindEnumType,
    GetCertificateIdUseEnumType,
    GetVariableStatusEnumType,
    HashAlgorithmEnumType,
    IslandingDetectionEnumType,
    LocationEnumType,
    MeasurandEnumType,
    MessageFormatEnumType,
    MessagePriorityEnumType,
    MessageStateEnumType,
    MobilityNeedsModeEnumType,
    MonitorEnumType,
    MutabilityEnumType,
    OCPPInterfaceEnumType,
    OCPPTransportEnumType,
    OCPPVersionEnumType,
    OperationModeEnumType,
    PhaseEnumType,
    PowerDuringCessationEnumType,
    ReadingContextEnumType,
    ReasonEnumType,
    RecurrencyKindEnumType,
    SetMonitoringStatusEnumType,
    SetVariableStatusEnumType,
    TariffClearStatusEnumType,
    TariffCostEnumType,
    TariffKindEnumType,
    VPNEnumType,
)


@dataclass
class ACChargingParametersType:
    energy_amount: float
    ev_max_current: float
    ev_max_voltage: float
    ev_min_current: float
    custom_data: Optional[CustomDataType] = None


@dataclass
class APNType:
    apn: str
    apn_authentication: APNAuthenticationEnumType
    apn_password: Optional[str] = None
    apn_user_name: Optional[str] = None
    custom_data: Optional[CustomDataType] = None
    preferred_network: Optional[str] = None
    sim_pin: Optional[int] = None
    use_only_preferred_network: bool = False


@dataclass
class AbsolutePriceScheduleType:
    currency: str
    language: str
    price_algorithm: str
    price_rule_stacks: List[PriceRuleStackType]
    price_schedule_id: int
    time_anchor: str
    additional_selected_services: Optional[List[AdditionalSelectedServicesType]] = None
    custom_data: Optional[CustomDataType] = None
    maximum_cost: Optional[RationalNumberType] = None
    minimum_cost: Optional[RationalNumberType] = None
    overstay_rule_list: Optional[OverstayRuleListType] = None
    price_schedule_description: Optional[str] = None
    tax_rules: Optional[List[TaxRuleType]] = None


@dataclass
class AdditionalInfoType:
    additional_id_token: str
    type: str
    custom_data: Optional[CustomDataType] = None


@dataclass
class AdditionalSelectedServicesType:
    service_fee: RationalNumberType
    service_name: str
    custom_data: Optional[CustomDataType] = None


@dataclass
class AddressType:
    address1: str
    city: str
    country: str
    name: str
    address2: Optional[str] = None
    custom_data: Optional[CustomDataType] = None
    postal_code: Optional[str] = None


@dataclass
class AuthorizationData:
    id_token: IdTokenType
    custom_data: Optional[CustomDataType] = None
    id_token_info: Optional[IdTokenInfoType] = None


@dataclass
class BatteryDataType:
    evse_id: int
    serial_number: str
    soc: float
    soh: float
    custom_data: Optional[CustomDataType] = None
    production_date: Optional[str] = None
    vendor_info: Optional[str] = None


@dataclass
class CertificateHashDataChainType:
    certificate_hash_data: CertificateHashDataType
    certificate_type: GetCertificateIdUseEnumType
    child_certificate_hash_data: Optional[List[CertificateHashDataType]] = None
    custom_data: Optional[CustomDataType] = None


@dataclass
class CertificateHashDataType:
    hash_algorithm: HashAlgorithmEnumType
    issuer_key_hash: str
    issuer_name_hash: str
    serial_number: str
    custom_data: Optional[CustomDataType] = None


@dataclass
class CertificateStatusRequestInfoType:
    certificate_hash_data: CertificateHashDataType
    source: CertificateStatusSourceEnumType
    urls: List[str]
    custom_data: Optional[CustomDataType] = None


@dataclass
class CertificateStatusType:
    certificate_hash_data: CertificateHashDataType
    next_update: str
    source: CertificateStatusSourceEnumType
    status: CertificateStatusEnumType
    custom_data: Optional[CustomDataType] = None


@dataclass
class ChargingLimitType:
    charging_limit_source: str
    custom_data: Optional[CustomDataType] = None
    is_grid_critical: Optional[bool] = None
    is_local_generation: Optional[bool] = None


@dataclass
class ChargingNeedsType:
    requested_energy_transfer: EnergyTransferModeEnumType
    ac_charging_parameters: Optional[ACChargingParametersType] = None
    available_energy_transfer: Optional[List[EnergyTransferModeEnumType]] = None
    control_mode: Optional[ControlModeEnumType] = None
    custom_data: Optional[CustomDataType] = None
    dc_charging_parameters: Optional[DCChargingParametersType] = None
    departure_time: Optional[str] = None
    der_charging_parameters: Optional[DERChargingParametersType] = None
    ev_energy_offer: Optional[EVEnergyOfferType] = None
    mobility_needs_mode: Optional[MobilityNeedsModeEnumType] = None
    v2x_charging_parameters: Optional[V2XChargingParametersType] = None


@dataclass
class ChargingPeriodType:
    start_period: str
    custom_data: Optional[CustomDataType] = None
    dimensions: Optional[List[CostDimensionType]] = None
    tariff_id: Optional[str] = None


@dataclass
class ChargingProfileCriterionType:
    charging_limit_source: Optional[List[str]] = None
    charging_profile_id: Optional[List[int]] = None
    charging_profile_purpose: Optional[ChargingProfilePurposeEnumType] = None
    custom_data: Optional[CustomDataType] = None
    stack_level: Optional[int] = None


@dataclass
class ChargingProfileType:
    charging_profile_kind: ChargingProfileKindEnumType
    charging_profile_purpose: ChargingProfilePurposeEnumType
    charging_schedule: List[ChargingScheduleType]
    id: int
    stack_level: int
    custom_data: Optional[CustomDataType] = None
    dyn_update_interval: Optional[int] = None
    dyn_update_time: Optional[str] = None
    invalid_after_offline_duration: Optional[bool] = None
    max_offline_duration: Optional[int] = None
    price_schedule_signature: Optional[str] = None
    recurrency_kind: Optional[RecurrencyKindEnumType] = None
    transaction_id: Optional[str] = None
    valid_from: Optional[str] = None
    valid_to: Optional[str] = None


@dataclass
class ChargingSchedulePeriodType:
    start_period: int
    custom_data: Optional[CustomDataType] = None
    discharge_limit: Optional[float] = None
    discharge_limit_l2: Optional[float] = None
    discharge_limit_l3: Optional[float] = None
    evse_sleep: Optional[bool] = None
    limit: Optional[float] = None
    limit_l2: Optional[float] = None
    limit_l3: Optional[float] = None
    number_phases: Optional[int] = None
    operation_mode: Optional[OperationModeEnumType] = None
    phase_to_use: Optional[int] = None
    preconditioning_request: Optional[bool] = None
    setpoint: Optional[float] = None
    setpoint_l2: Optional[float] = None
    setpoint_l3: Optional[float] = None
    setpoint_reactive: Optional[float] = None
    setpoint_reactive_l2: Optional[float] = None
    setpoint_reactive_l3: Optional[float] = None
    v2x_baseline: Optional[float] = None
    v2x_freq_watt_curve: Optional[List[V2XFreqWattPointType]] = None
    v2x_signal_watt_curve: Optional[List[V2XSignalWattPointType]] = None


@dataclass
class ChargingScheduleType:
    charging_rate_unit: ChargingRateUnitEnumType
    charging_schedule_period: List[ChargingSchedulePeriodType]
    id: int
    absolute_price_schedule: Optional[AbsolutePriceScheduleType] = None
    custom_data: Optional[CustomDataType] = None
    digest_value: Optional[str] = None
    duration: Optional[int] = None
    limit_at_soc: Optional[LimitAtSoCType] = None
    min_charging_rate: Optional[float] = None
    power_tolerance: Optional[float] = None
    price_level_schedule: Optional[PriceLevelScheduleType] = None
    randomized_delay: Optional[int] = None
    sales_tariff: Optional[SalesTariffType] = None
    signature_id: Optional[int] = None
    start_schedule: Optional[str] = None
    use_local_time: Optional[bool] = None


@dataclass
class ChargingScheduleUpdateType:
    custom_data: Optional[CustomDataType] = None
    discharge_limit: Optional[float] = None
    discharge_limit_l2: Optional[float] = None
    discharge_limit_l3: Optional[float] = None
    limit: Optional[float] = None
    limit_l2: Optional[float] = None
    limit_l3: Optional[float] = None
    setpoint: Optional[float] = None
    setpoint_l2: Optional[float] = None
    setpoint_l3: Optional[float] = None
    setpoint_reactive: Optional[float] = None
    setpoint_reactive_l2: Optional[float] = None
    setpoint_reactive_l3: Optional[float] = None


@dataclass
class ChargingStationType:
    model: str
    vendor_name: str
    custom_data: Optional[CustomDataType] = None
    firmware_version: Optional[str] = None
    modem: Optional[ModemType] = None
    serial_number: Optional[str] = None


@dataclass
class ClearChargingProfileType:
    charging_profile_purpose: Optional[ChargingProfilePurposeEnumType] = None
    custom_data: Optional[CustomDataType] = None
    evse_id: Optional[int] = None
    stack_level: Optional[int] = None


@dataclass
class ClearMonitoringResultType:
    id: int
    status: ClearMonitoringStatusEnumType
    custom_data: Optional[CustomDataType] = None
    status_info: Optional[StatusInfoType] = None


@dataclass
class ClearTariffsResultType:
    status: TariffClearStatusEnumType
    custom_data: Optional[CustomDataType] = None
    status_info: Optional[StatusInfoType] = None
    tariff_id: Optional[str] = None


@dataclass
class ComponentType:
    name: str
    custom_data: Optional[CustomDataType] = None
    evse: Optional[EVSEType] = None
    instance: Optional[str] = None


@dataclass
class ComponentVariableType:
    component: ComponentType
    custom_data: Optional[CustomDataType] = None
    variable: Optional[VariableType] = None


@dataclass
class CompositeScheduleType:
    charging_rate_unit: ChargingRateUnitEnumType
    charging_schedule_period: List[ChargingSchedulePeriodType]
    duration: int
    evse_id: int
    schedule_start: str
    custom_data: Optional[CustomDataType] = None


@dataclass
class ConstantStreamDataType:
    id: int
    params: PeriodicEventStreamParamsType
    variable_monitoring_id: int
    custom_data: Optional[CustomDataType] = None


@dataclass
class ConsumptionCostType:
    cost: List[CostType]
    start_value: float
    custom_data: Optional[CustomDataType] = None


@dataclass
class CostDetailsType:
    total_cost: TotalCostType
    total_usage: TotalUsageType
    charging_periods: Optional[List[ChargingPeriodType]] = None
    custom_data: Optional[CustomDataType] = None
    failure_reason: Optional[str] = None
    failure_to_calculate: Optional[bool] = None


@dataclass
class CostDimensionType:
    type: CostDimensionEnumType
    volume: float
    custom_data: Optional[CustomDataType] = None


@dataclass
class CostType:
    amount: int
    cost_kind: CostKindEnumType
    amount_multiplier: Optional[int] = None
    custom_data: Optional[CustomDataType] = None


@dataclass
class CustomDataType:
    vendor_id: str


@dataclass
class DCChargingParametersType:
    ev_max_current: float
    ev_max_voltage: float
    bulk_soc: Optional[int] = None
    custom_data: Optional[CustomDataType] = None
    energy_amount: Optional[float] = None
    ev_energy_capacity: Optional[float] = None
    ev_max_power: Optional[float] = None
    full_soc: Optional[int] = None
    state_of_charge: Optional[int] = None


@dataclass
class DERChargingParametersType:
    custom_data: Optional[CustomDataType] = None
    ev_duration_level1_dc_injection: Optional[float] = None
    ev_duration_level2_dc_injection: Optional[float] = None
    ev_inverter_hw_version: Optional[str] = None
    ev_inverter_manufacturer: Optional[str] = None
    ev_inverter_model: Optional[str] = None
    ev_inverter_serial_number: Optional[str] = None
    ev_inverter_sw_version: Optional[str] = None
    ev_islanding_detection_method: Optional[List[IslandingDetectionEnumType]] = None
    ev_islanding_trip_time: Optional[float] = None
    ev_maximum_level1_dc_injection: Optional[float] = None
    ev_maximum_level2_dc_injection: Optional[float] = None
    ev_over_excited_max_discharge_power: Optional[float] = None
    ev_over_excited_power_factor: Optional[float] = None
    ev_reactive_susceptance: Optional[float] = None
    ev_session_total_discharge_energy_available: Optional[float] = None
    ev_supported_der_control: Optional[List[DERControlEnumType]] = None
    ev_under_excited_max_discharge_power: Optional[float] = None
    ev_under_excited_power_factor: Optional[float] = None
    max_apparent_power: Optional[float] = None
    max_charge_apparent_power: Optional[float] = None
    max_charge_apparent_power_l2: Optional[float] = None
    max_charge_apparent_power_l3: Optional[float] = None
    max_charge_reactive_power: Optional[float] = None
    max_charge_reactive_power_l2: Optional[float] = None
    max_charge_reactive_power_l3: Optional[float] = None
    max_discharge_apparent_power: Optional[float] = None
    max_discharge_apparent_power_l2: Optional[float] = None
    max_discharge_apparent_power_l3: Optional[float] = None
    max_discharge_reactive_power: Optional[float] = None
    max_discharge_reactive_power_l2: Optional[float] = None
    max_discharge_reactive_power_l3: Optional[float] = None
    max_nominal_voltage: Optional[float] = None
    min_charge_reactive_power: Optional[float] = None
    min_charge_reactive_power_l2: Optional[float] = None
    min_charge_reactive_power_l3: Optional[float] = None
    min_discharge_reactive_power: Optional[float] = None
    min_discharge_reactive_power_l2: Optional[float] = None
    min_discharge_reactive_power_l3: Optional[float] = None
    min_nominal_voltage: Optional[float] = None
    nominal_voltage: Optional[float] = None
    nominal_voltage_offset: Optional[float] = None


@dataclass
class DERCurveGetType:
    curve: DERCurveType
    curve_type: DERControlEnumType
    id: str
    is_default: bool
    is_superseded: bool
    custom_data: Optional[CustomDataType] = None


@dataclass
class DERCurvePointsType:
    x: float
    y: float
    custom_data: Optional[CustomDataType] = None


@dataclass
class DERCurveType:
    curve_data: List[DERCurvePointsType]
    priority: int
    y_unit: DERUnitEnumType
    custom_data: Optional[CustomDataType] = None
    duration: Optional[float] = None
    hysteresis: Optional[HysteresisType] = None
    reactive_power_params: Optional[ReactivePowerParamsType] = None
    response_time: Optional[float] = None
    start_time: Optional[str] = None
    voltage_params: Optional[VoltageParamsType] = None


@dataclass
class EVAbsolutePriceScheduleEntryType:
    duration: int
    ev_price_rule: List[EVPriceRuleType]
    custom_data: Optional[CustomDataType] = None


@dataclass
class EVAbsolutePriceScheduleType:
    currency: str
    ev_absolute_price_schedule_entries: List[EVAbsolutePriceScheduleEntryType]
    price_algorithm: str
    time_anchor: str
    custom_data: Optional[CustomDataType] = None


@dataclass
class EVEnergyOfferType:
    ev_power_schedule: EVPowerScheduleType
    custom_data: Optional[CustomDataType] = None
    ev_absolute_price_schedule: Optional[EVAbsolutePriceScheduleType] = None


@dataclass
class EVPowerScheduleEntryType:
    duration: int
    power: float
    custom_data: Optional[CustomDataType] = None


@dataclass
class EVPowerScheduleType:
    ev_power_schedule_entries: List[EVPowerScheduleEntryType]
    time_anchor: str
    custom_data: Optional[CustomDataType] = None


@dataclass
class EVPriceRuleType:
    energy_fee: float
    power_range_start: float
    custom_data: Optional[CustomDataType] = None


@dataclass
class EVSEType:
    id: int
    connector_id: Optional[int] = None
    custom_data: Optional[CustomDataType] = None


@dataclass
class EnterServiceGetType:
    enter_service: EnterServiceType
    id: str
    custom_data: Optional[CustomDataType] = None


@dataclass
class EnterServiceType:
    high_freq: float
    high_voltage: float
    low_freq: float
    low_voltage: float
    priority: int
    custom_data: Optional[CustomDataType] = None
    delay: Optional[float] = None
    ramp_rate: Optional[float] = None
    random_delay: Optional[float] = None


@dataclass
class EventDataType:
    actual_value: str
    component: ComponentType
    event_id: int
    event_notification_type: EventNotificationEnumType
    timestamp: str
    trigger: EventTriggerEnumType
    variable: VariableType
    cause: Optional[int] = None
    cleared: Optional[bool] = None
    custom_data: Optional[CustomDataType] = None
    severity: Optional[int] = None
    tech_code: Optional[str] = None
    tech_info: Optional[str] = None
    transaction_id: Optional[str] = None
    variable_monitoring_id: Optional[int] = None


@dataclass
class FirmwareType:
    location: str
    retrieve_date_time: str
    custom_data: Optional[CustomDataType] = None
    install_date_time: Optional[str] = None
    signature: Optional[str] = None
    signing_certificate: Optional[str] = None


@dataclass
class FixedPFGetType:
    fixed_pf: FixedPFType
    id: str
    is_default: bool
    is_superseded: bool
    custom_data: Optional[CustomDataType] = None


@dataclass
class FixedPFType:
    displacement: float
    excitation: bool
    priority: int
    custom_data: Optional[CustomDataType] = None
    duration: Optional[float] = None
    start_time: Optional[str] = None


@dataclass
class FixedVarGetType:
    fixed_var: FixedVarType
    id: str
    is_default: bool
    is_superseded: bool
    custom_data: Optional[CustomDataType] = None


@dataclass
class FixedVarType:
    priority: int
    setpoint: float
    unit: DERUnitEnumType
    custom_data: Optional[CustomDataType] = None
    duration: Optional[float] = None
    start_time: Optional[str] = None


@dataclass
class FreqDroopGetType:
    freq_droop: FreqDroopType
    id: str
    is_default: bool
    is_superseded: bool
    custom_data: Optional[CustomDataType] = None


@dataclass
class FreqDroopType:
    over_droop: float
    over_freq: float
    priority: int
    response_time: float
    under_droop: float
    under_freq: float
    custom_data: Optional[CustomDataType] = None
    duration: Optional[float] = None
    start_time: Optional[str] = None


@dataclass
class GetVariableDataType:
    component: ComponentType
    variable: VariableType
    attribute_type: AttributeEnumType = AttributeEnumType.actual
    custom_data: Optional[CustomDataType] = None


@dataclass
class GetVariableResultType:
    attribute_status: GetVariableStatusEnumType
    component: ComponentType
    variable: VariableType
    attribute_status_info: Optional[StatusInfoType] = None
    attribute_type: AttributeEnumType = AttributeEnumType.actual
    attribute_value: Optional[str] = None
    custom_data: Optional[CustomDataType] = None


@dataclass
class GradientGetType:
    gradient: GradientType
    id: str
    custom_data: Optional[CustomDataType] = None


@dataclass
class GradientType:
    gradient: float
    priority: int
    soft_gradient: float
    custom_data: Optional[CustomDataType] = None


@dataclass
class HysteresisType:
    custom_data: Optional[CustomDataType] = None
    hysteresis_delay: Optional[float] = None
    hysteresis_gradient: Optional[float] = None
    hysteresis_high: Optional[float] = None
    hysteresis_low: Optional[float] = None


@dataclass
class IdTokenInfoType:
    status: AuthorizationStatusEnumType
    cache_expiry_date_time: Optional[str] = None
    charging_priority: Optional[int] = None
    custom_data: Optional[CustomDataType] = None
    evse_id: Optional[List[int]] = None
    group_id_token: Optional[IdTokenType] = None
    language1: Optional[str] = None
    language2: Optional[str] = None
    personal_message: Optional[MessageContentType] = None


@dataclass
class IdTokenType:
    id_token: str
    type: str
    additional_info: Optional[List[AdditionalInfoType]] = None
    custom_data: Optional[CustomDataType] = None


@dataclass
class LimitAtSoCType:
    limit: float
    soc: int
    custom_data: Optional[CustomDataType] = None


@dataclass
class LimitMaxDischargeGetType:
    id: str
    is_default: bool
    is_superseded: bool
    limit_max_discharge: LimitMaxDischargeType
    custom_data: Optional[CustomDataType] = None


@dataclass
class LimitMaxDischargeType:
    priority: int
    custom_data: Optional[CustomDataType] = None
    duration: Optional[float] = None
    pct_max_discharge_power: Optional[float] = None
    power_monitoring_must_trip: Optional[DERCurveType] = None
    start_time: Optional[str] = None


@dataclass
class LogParametersType:
    remote_location: str
    custom_data: Optional[CustomDataType] = None
    latest_timestamp: Optional[str] = None
    oldest_timestamp: Optional[str] = None


@dataclass
class MessageContentType:
    content: str
    format: MessageFormatEnumType
    custom_data: Optional[CustomDataType] = None
    language: Optional[str] = None


@dataclass
class MessageInfoType:
    id: int
    message: MessageContentType
    priority: MessagePriorityEnumType
    custom_data: Optional[CustomDataType] = None
    display: Optional[ComponentType] = None
    end_date_time: Optional[str] = None
    message_extra: Optional[List[MessageContentType]] = None
    start_date_time: Optional[str] = None
    state: Optional[MessageStateEnumType] = None
    transaction_id: Optional[str] = None


@dataclass
class MeterValueType:
    sampled_value: List[SampledValueType]
    timestamp: str
    custom_data: Optional[CustomDataType] = None


@dataclass
class ModemType:
    custom_data: Optional[CustomDataType] = None
    iccid: Optional[str] = None
    imsi: Optional[str] = None


@dataclass
class MonitoringDataType:
    component: ComponentType
    variable: VariableType
    variable_monitoring: List[VariableMonitoringType]
    custom_data: Optional[CustomDataType] = None


@dataclass
class NetworkConnectionProfileType:
    message_timeout: int
    ocpp_csms_url: str
    ocpp_interface: OCPPInterfaceEnumType
    ocpp_transport: OCPPTransportEnumType
    security_profile: int
    apn: Optional[APNType] = None
    basic_auth_password: Optional[str] = None
    custom_data: Optional[CustomDataType] = None
    identity: Optional[str] = None
    ocpp_version: Optional[OCPPVersionEnumType] = None
    vpn: Optional[VPNType] = None


@dataclass
class OCSPRequestDataType:
    hash_algorithm: HashAlgorithmEnumType
    issuer_key_hash: str
    issuer_name_hash: str
    responder_url: str
    serial_number: str
    custom_data: Optional[CustomDataType] = None


@dataclass
class OverstayRuleListType:
    overstay_rule: List[OverstayRuleType]
    custom_data: Optional[CustomDataType] = None
    overstay_power_threshold: Optional[RationalNumberType] = None
    overstay_time_threshold: Optional[int] = None


@dataclass
class OverstayRuleType:
    overstay_fee: RationalNumberType
    overstay_fee_period: int
    start_time: int
    custom_data: Optional[CustomDataType] = None
    overstay_rule_description: Optional[str] = None


@dataclass
class PeriodicEventStreamParamsType:
    custom_data: Optional[CustomDataType] = None
    interval: Optional[int] = None
    values: Optional[int] = None


@dataclass
class PriceLevelScheduleEntryType:
    duration: int
    price_level: int
    custom_data: Optional[CustomDataType] = None


@dataclass
class PriceLevelScheduleType:
    number_of_price_levels: int
    price_level_schedule_entries: List[PriceLevelScheduleEntryType]
    price_schedule_id: int
    time_anchor: str
    custom_data: Optional[CustomDataType] = None
    price_schedule_description: Optional[str] = None


@dataclass
class PriceRuleStackType:
    duration: int
    price_rule: List[PriceRuleType]
    custom_data: Optional[CustomDataType] = None


@dataclass
class PriceRuleType:
    energy_fee: RationalNumberType
    power_range_start: RationalNumberType
    carbon_dioxide_emission: Optional[int] = None
    custom_data: Optional[CustomDataType] = None
    parking_fee: Optional[RationalNumberType] = None
    parking_fee_period: Optional[int] = None
    renewable_generation_percentage: Optional[int] = None


@dataclass
class PriceType:
    custom_data: Optional[CustomDataType] = None
    excl_tax: Optional[float] = None
    incl_tax: Optional[float] = None
    tax_rates: Optional[List[TaxRateType]] = None


@dataclass
class RationalNumberType:
    exponent: int
    value: int
    custom_data: Optional[CustomDataType] = None


@dataclass
class ReactivePowerParamsType:
    autonomous_v_ref_enable: Optional[bool] = None
    autonomous_v_ref_time_constant: Optional[float] = None
    custom_data: Optional[CustomDataType] = None
    v_ref: Optional[float] = None


@dataclass
class RelativeTimeIntervalType:
    start: int
    custom_data: Optional[CustomDataType] = None
    duration: Optional[int] = None


@dataclass
class ReportDataType:
    component: ComponentType
    variable: VariableType
    variable_attribute: List[VariableAttributeType]
    custom_data: Optional[CustomDataType] = None
    variable_characteristics: Optional[VariableCharacteristicsType] = None


@dataclass
class SalesTariffEntryType:
    relative_time_interval: RelativeTimeIntervalType
    consumption_cost: Optional[List[ConsumptionCostType]] = None
    custom_data: Optional[CustomDataType] = None
    e_price_level: Optional[int] = None


@dataclass
class SalesTariffType:
    id: int
    sales_tariff_entry: List[SalesTariffEntryType]
    custom_data: Optional[CustomDataType] = None
    num_e_price_levels: Optional[int] = None
    sales_tariff_description: Optional[str] = None


@dataclass
class SampledValueType:
    value: float
    context: ReadingContextEnumType = ReadingContextEnumType.sample_periodic
    custom_data: Optional[CustomDataType] = None
    location: LocationEnumType = LocationEnumType.outlet
    measurand: MeasurandEnumType = MeasurandEnumType.energy_active_import_register
    phase: Optional[PhaseEnumType] = None
    signed_meter_value: Optional[SignedMeterValueType] = None
    unit_of_measure: Optional[UnitOfMeasureType] = None


@dataclass
class SetMonitoringDataType:
    component: ComponentType
    severity: int
    type: MonitorEnumType
    value: float
    variable: VariableType
    custom_data: Optional[CustomDataType] = None
    id: Optional[int] = None
    periodic_event_stream: Optional[PeriodicEventStreamParamsType] = None
    transaction: bool = False


@dataclass
class SetMonitoringResultType:
    component: ComponentType
    severity: int
    status: SetMonitoringStatusEnumType
    type: MonitorEnumType
    variable: VariableType
    custom_data: Optional[CustomDataType] = None
    id: Optional[int] = None
    status_info: Optional[StatusInfoType] = None


@dataclass
class SetVariableDataType:
    attribute_value: str
    component: ComponentType
    variable: VariableType
    attribute_type: AttributeEnumType = AttributeEnumType.actual
    custom_data: Optional[CustomDataType] = None


@dataclass
class SetVariableResultType:
    attribute_status: SetVariableStatusEnumType
    component: ComponentType
    variable: VariableType
    attribute_status_info: Optional[StatusInfoType] = None
    attribute_type: AttributeEnumType = AttributeEnumType.actual
    custom_data: Optional[CustomDataType] = None


@dataclass
class SignedMeterValueType:
    encoding_method: str
    signed_meter_data: str
    custom_data: Optional[CustomDataType] = None
    public_key: Optional[str] = None
    signing_method: Optional[str] = None


@dataclass
class StatusInfoType:
    reason_code: str
    additional_info: Optional[str] = None
    custom_data: Optional[CustomDataType] = None


@dataclass
class TariffAssignmentType:
    tariff_id: str
    tariff_kind: TariffKindEnumType
    custom_data: Optional[CustomDataType] = None
    evse_ids: Optional[List[int]] = None
    id_tokens: Optional[List[str]] = None
    valid_from: Optional[str] = None


@dataclass
class TariffConditionsFixedType:
    custom_data: Optional[CustomDataType] = None
    day_of_week: Optional[List[DayOfWeekEnumType]] = None
    end_time_of_day: Optional[str] = None
    evse_kind: Optional[EvseKindEnumType] = None
    payment_brand: Optional[str] = None
    payment_recognition: Optional[str] = None
    start_time_of_day: Optional[str] = None
    valid_from_date: Optional[str] = None
    valid_to_date: Optional[str] = None


@dataclass
class TariffConditionsType:
    custom_data: Optional[CustomDataType] = None
    day_of_week: Optional[List[DayOfWeekEnumType]] = None
    end_time_of_day: Optional[str] = None
    evse_kind: Optional[EvseKindEnumType] = None
    max_charging_time: Optional[int] = None
    max_current: Optional[float] = None
    max_energy: Optional[float] = None
    max_idle_time: Optional[int] = None
    max_power: Optional[float] = None
    max_time: Optional[int] = None
    min_charging_time: Optional[int] = None
    min_current: Optional[float] = None
    min_energy: Optional[float] = None
    min_idle_time: Optional[int] = None
    min_power: Optional[float] = None
    min_time: Optional[int] = None
    start_time_of_day: Optional[str] = None
    valid_from_date: Optional[str] = None
    valid_to_date: Optional[str] = None


@dataclass
class TariffEnergyPriceType:
    price_kwh: float
    conditions: Optional[TariffConditionsType] = None
    custom_data: Optional[CustomDataType] = None


@dataclass
class TariffEnergyType:
    prices: List[TariffEnergyPriceType]
    custom_data: Optional[CustomDataType] = None
    tax_rates: Optional[List[TaxRateType]] = None


@dataclass
class TariffFixedPriceType:
    price_fixed: float
    conditions: Optional[TariffConditionsFixedType] = None
    custom_data: Optional[CustomDataType] = None


@dataclass
class TariffFixedType:
    prices: List[TariffFixedPriceType]
    custom_data: Optional[CustomDataType] = None
    tax_rates: Optional[List[TaxRateType]] = None


@dataclass
class TariffTimePriceType:
    price_minute: float
    conditions: Optional[TariffConditionsType] = None
    custom_data: Optional[CustomDataType] = None


@dataclass
class TariffTimeType:
    prices: List[TariffTimePriceType]
    custom_data: Optional[CustomDataType] = None
    tax_rates: Optional[List[TaxRateType]] = None


@dataclass
class TariffType:
    currency: str
    tariff_id: str
    charging_time: Optional[TariffTimeType] = None
    custom_data: Optional[CustomDataType] = None
    description: Optional[List[MessageContentType]] = None
    energy: Optional[TariffEnergyType] = None
    fixed_fee: Optional[TariffFixedType] = None
    idle_time: Optional[TariffTimeType] = None
    max_cost: Optional[PriceType] = None
    min_cost: Optional[PriceType] = None
    reservation_fixed: Optional[TariffFixedType] = None
    reservation_time: Optional[TariffTimeType] = None
    valid_from: Optional[str] = None


@dataclass
class TaxRateType:
    tax: float
    type: str
    custom_data: Optional[CustomDataType] = None
    stack: Optional[int] = None


@dataclass
class TaxRuleType:
    applies_to_energy_fee: bool
    applies_to_minimum_maximum_cost: bool
    applies_to_overstay_fee: bool
    applies_to_parking_fee: bool
    tax_rate: RationalNumberType
    tax_rule_id: int
    custom_data: Optional[CustomDataType] = None
    tax_included_in_price: Optional[bool] = None
    tax_rule_name: Optional[str] = None


@dataclass
class TotalCostType:
    currency: str
    total: TotalPriceType
    type_of_cost: TariffCostEnumType
    charging_time: Optional[PriceType] = None
    custom_data: Optional[CustomDataType] = None
    energy: Optional[PriceType] = None
    fixed: Optional[PriceType] = None
    idle_time: Optional[PriceType] = None
    reservation_fixed: Optional[PriceType] = None
    reservation_time: Optional[PriceType] = None


@dataclass
class TotalPriceType:
    custom_data: Optional[CustomDataType] = None
    excl_tax: Optional[float] = None
    incl_tax: Optional[float] = None


@dataclass
class TotalUsageType:
    charging_time: int
    energy: float
    idle_time: int
    custom_data: Optional[CustomDataType] = None
    reservation_time: Optional[int] = None


@dataclass
class TransactionLimitType:
    custom_data: Optional[CustomDataType] = None
    max_cost: Optional[float] = None
    max_energy: Optional[float] = None
    max_soc: Optional[int] = None
    max_time: Optional[int] = None


@dataclass
class TransactionType:
    transaction_id: str
    charging_state: Optional[ChargingStateEnumType] = None
    custom_data: Optional[CustomDataType] = None
    operation_mode: Optional[OperationModeEnumType] = None
    remote_start_id: Optional[int] = None
    stopped_reason: Optional[ReasonEnumType] = None
    tariff_id: Optional[str] = None
    time_spent_charging: Optional[int] = None
    transaction_limit: Optional[TransactionLimitType] = None


@dataclass
class UnitOfMeasureType:
    custom_data: Optional[CustomDataType] = None
    multiplier: int = 0
    unit: str = "Wh"


@dataclass
class V2XChargingParametersType:
    custom_data: Optional[CustomDataType] = None
    ev_max_energy_request: Optional[float] = None
    ev_max_v2x_energy_request: Optional[float] = None
    ev_min_energy_request: Optional[float] = None
    ev_min_v2x_energy_request: Optional[float] = None
    ev_target_energy_request: Optional[float] = None
    max_charge_current: Optional[float] = None
    max_charge_power: Optional[float] = None
    max_charge_power_l2: Optional[float] = None
    max_charge_power_l3: Optional[float] = None
    max_discharge_current: Optional[float] = None
    max_discharge_power: Optional[float] = None
    max_discharge_power_l2: Optional[float] = None
    max_discharge_power_l3: Optional[float] = None
    max_voltage: Optional[float] = None
    min_charge_current: Optional[float] = None
    min_charge_power: Optional[float] = None
    min_charge_power_l2: Optional[float] = None
    min_charge_power_l3: Optional[float] = None
    min_discharge_current: Optional[float] = None
    min_discharge_power: Optional[float] = None
    min_discharge_power_l2: Optional[float] = None
    min_discharge_power_l3: Optional[float] = None
    min_voltage: Optional[float] = None
    target_soc: Optional[int] = None


@dataclass
class V2XFreqWattPointType:
    frequency: float
    power: float
    custom_data: Optional[CustomDataType] = None


@dataclass
class V2XSignalWattPointType:
    power: float
    signal: int
    custom_data: Optional[CustomDataType] = None


@dataclass
class VPNType:
    key: str
    password: str
    server: str
    type: VPNEnumType
    user: str
    custom_data: Optional[CustomDataType] = None
    group: Optional[str] = None


@dataclass
class VariableAttributeType:
    constant: bool = False
    custom_data: Optional[CustomDataType] = None
    mutability: MutabilityEnumType = MutabilityEnumType.read_write
    persistent: bool = False
    type: AttributeEnumType = AttributeEnumType.actual
    value: Optional[str] = None


@dataclass
class VariableCharacteristicsType:
    data_type: DataEnumType
    supports_monitoring: bool
    custom_data: Optional[CustomDataType] = None
    max_elements: Optional[int] = None
    max_limit: Optional[float] = None
    min_limit: Optional[float] = None
    unit: Optional[str] = None
    values_list: Optional[str] = None


@dataclass
class VariableMonitoringType:
    event_notification_type: EventNotificationEnumType
    id: int
    severity: int
    transaction: bool
    type: MonitorEnumType
    value: float
    custom_data: Optional[CustomDataType] = None


@dataclass
class VariableType:
    name: str
    custom_data: Optional[CustomDataType] = None
    instance: Optional[str] = None


@dataclass
class VoltageParamsType:
    custom_data: Optional[CustomDataType] = None
    hv10_min_mean_trip_delay: Optional[float] = None
    hv10_min_mean_value: Optional[float] = None
    power_during_cessation: Optional[PowerDuringCessationEnumType] = None
