from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from ocpp.v21 import enums
from ocpp.v21.enums import (
    APNAuthentication,
    Attribute,
    AuthorizationStatus,
    ChargingLimitSource,
    ChargingProfileKind,
    ChargingProfilePurpose,
    ChargingRateUnit,
    ChargingState,
    ClearMonitoringStatus,
    ControlMode,
    CostKind,
    Data,
    EnergyTransferMode,
    EventNotification,
    EventTrigger,
    GetCertificateIdUse,
    GetVariableStatus,
    HashAlgorithm,
    Location,
    Measurand,
    MessageFormat,
    MessagePriority,
    MessageState,
    MobilityNeedsMode,
    Monitor,
    Mutability,
    OCPPTransport,
    OCPPVersion,
    OperationMode,
    Phase,
    Pricing,
    ReadingContext,
    Reason,
    RecurrencyKind,
    SetMonitoringStatus,
    SetVariableStatus,
)


@dataclass
class ACChargingParameters:
    energy_amount: float
    ev_max_current: float
    ev_max_voltage: float
    ev_min_current: float
    custom_data: Optional[CustomData] = None


@dataclass
class APN:
    apn: str
    apn_authentication: APNAuthentication
    apn_password: Optional[str] = None
    apn_user_name: Optional[str] = None
    custom_data: Optional[CustomData] = None
    preferred_network: Optional[str] = None
    sim_pin: Optional[int] = None
    use_only_preferred_network: bool = False


@dataclass
class AbsolutePriceSchedule:
    currency: str
    language: str
    price_algorithm: str
    price_rule_stacks: List[PriceRuleStack]
    price_schedule_id: int
    time_anchor: str
    additional_selected_services: Optional[List[AdditionalSelectedServices]] = None
    custom_data: Optional[CustomData] = None
    maximum_cost: Optional[RationalNumber] = None
    minimum_cost: Optional[RationalNumber] = None
    overstay_rule_list: Optional[OverstayRuleList] = None
    price_schedule_description: Optional[str] = None
    tax_rules: Optional[List[TaxRule]] = None


@dataclass
class AdditionalInfo:
    additional_id_token: str
    type: str
    custom_data: Optional[CustomData] = None


@dataclass
class AdditionalSelectedServices:
    service_fee: RationalNumber
    service_name: str
    custom_data: Optional[CustomData] = None


@dataclass
class AuthorizationData:
    id_token: IdToken
    custom_data: Optional[CustomData] = None
    id_token_info: Optional[IdTokenInfo] = None


@dataclass
class CertificateHashData:
    hash_algorithm: HashAlgorithm
    issuer_key_hash: str
    issuer_name_hash: str
    serial_number: str
    custom_data: Optional[CustomData] = None


@dataclass
class CertificateHashDataChain:
    certificate_hash_data: CertificateHashData
    certificate_type: GetCertificateIdUse
    child_certificate_hash_data: Optional[List[CertificateHashData]] = None
    custom_data: Optional[CustomData] = None


@dataclass
class ChargingLimit:
    charging_limit_source: ChargingLimitSource
    custom_data: Optional[CustomData] = None
    is_grid_critical: Optional[bool] = None
    is_local_generation: Optional[bool] = None


@dataclass
class ChargingNeeds:
    requested_energy_transfer: EnergyTransferMode
    ac_charging_parameters: Optional[ACChargingParameters] = None
    available_energy_transfer: Optional[List[EnergyTransferMode]] = None
    control_mode: Optional[ControlMode] = None
    custom_data: Optional[CustomData] = None
    dc_charging_parameters: Optional[DCChargingParameters] = None
    departure_time: Optional[str] = None
    ev_energy_offer: Optional[EVEnergyOffer] = None
    mobility_needs_mode: Optional[MobilityNeedsMode] = None
    pricing: Optional[Pricing] = None
    v2x_charging_parameters: Optional[V2XChargingParameters] = None


@dataclass
class ChargingProfile:
    charging_profile_kind: ChargingProfileKind
    charging_profile_purpose: ChargingProfilePurpose
    charging_schedule: List[ChargingSchedule]
    id: int
    stack_level: int
    custom_data: Optional[CustomData] = None
    max_offline_duration: Optional[int] = None
    price_schedule_signature: Optional[str] = None
    recurrency_kind: Optional[RecurrencyKind] = None
    transaction_id: Optional[str] = None
    update_interval: Optional[int] = None
    valid_from: Optional[str] = None
    valid_to: Optional[str] = None


@dataclass
class ChargingProfileCriterion:
    charging_limit_source: Optional[List[ChargingLimitSource]] = None
    charging_profile_id: Optional[List[int]] = None
    charging_profile_purpose: Optional[ChargingProfilePurpose] = None
    custom_data: Optional[CustomData] = None
    stack_level: Optional[int] = None


@dataclass
class ChargingSchedule:
    charging_rate_unit: ChargingRateUnit
    charging_schedule_period: List[ChargingSchedulePeriod]
    id: int
    absolute_price_schedule: Optional[AbsolutePriceSchedule] = None
    custom_data: Optional[CustomData] = None
    digest_value: Optional[str] = None
    duration: Optional[int] = None
    limit_beyond_soc: Optional[LimitBeyondSoC] = None
    min_charging_rate: Optional[float] = None
    power_tolerance: Optional[float] = None
    price_level_schedule: Optional[PriceLevelSchedule] = None
    sales_tariff: Optional[SalesTariff] = None
    signature_id: Optional[int] = None
    start_schedule: Optional[str] = None


@dataclass
class ChargingSchedulePeriod:
    start_period: int
    custom_data: Optional[CustomData] = None
    discharge_limit: Optional[float] = None
    discharge_limit_l2: Optional[float] = None
    discharge_limit_l3: Optional[float] = None
    dyn_update_time: Optional[str] = None
    limit: Optional[float] = None
    limit_l2: Optional[float] = None
    limit_l3: Optional[float] = None
    number_phases: Optional[int] = None
    operation_mode: Optional[OperationMode] = None
    phase_to_use: Optional[int] = None
    preconditioning_request: Optional[bool] = None
    set_point_reactive: Optional[float] = None
    set_point_reactive_l2: Optional[float] = None
    set_point_reactive_l3: Optional[float] = None
    setpoint: Optional[float] = None
    setpoint_l2: Optional[float] = None
    setpoint_l3: Optional[float] = None
    v2x_baseline: Optional[float] = None
    v2x_freq_watt_curve: Optional[List[V2XFreqWattEntry]] = None
    v2x_signal_watt_curve: Optional[List[V2XSignalWattEntry]] = None


@dataclass
class ChargingStation:
    model: str
    vendor_name: str
    custom_data: Optional[CustomData] = None
    firmware_version: Optional[str] = None
    modem: Optional[Modem] = None
    serial_number: Optional[str] = None


@dataclass
class ClearChargingProfile:
    charging_profile_purpose: Optional[ChargingProfilePurpose] = None
    custom_data: Optional[CustomData] = None
    evse_id: Optional[int] = None
    stack_level: Optional[int] = None


@dataclass
class Component:
    name: str
    custom_data: Optional[CustomData] = None
    evse: Optional[EVSE] = None
    instance: Optional[str] = None


@dataclass
class ComponentVariable:
    component: Component
    custom_data: Optional[CustomData] = None
    variable: Optional[Variable] = None


@dataclass
class CompositeSchedule:
    charging_rate_unit: ChargingRateUnit
    charging_schedule_period: List[ChargingSchedulePeriod]
    duration: int
    evse_id: int
    schedule_start: str
    custom_data: Optional[CustomData] = None


@dataclass
class ConsumptionCost:
    cost: List[Cost]
    start_value: float
    custom_data: Optional[CustomData] = None


@dataclass
class Cost:
    amount: int
    cost_kind: CostKind
    amount_multiplier: Optional[int] = None
    custom_data: Optional[CustomData] = None


@dataclass
class CustomData:
    vendor_id: str


@dataclass
class DCChargingParameters:
    ev_max_current: float
    ev_max_voltage: float
    bulk_soc: Optional[int] = None
    custom_data: Optional[CustomData] = None
    energy_amount: Optional[float] = None
    ev_energy_capacity: Optional[float] = None
    ev_max_power: Optional[float] = None
    full_soc: Optional[int] = None
    state_of_charge: Optional[int] = None


@dataclass
class EVAbsolutePriceSchedule:
    currency: str
    ev_absolute_price_schedule_entries: List[EVAbsolutePriceScheduleEntry]
    price_algorithm: str
    time_anchor: str
    custom_data: Optional[CustomData] = None


@dataclass
class EVAbsolutePriceScheduleEntry:
    duration: int
    ev_price_rule: List[EVPriceRule]
    custom_data: Optional[CustomData] = None


@dataclass
class EVEnergyOffer:
    ev_power_schedule: EVPowerSchedule
    custom_data: Optional[CustomData] = None
    ev_absolute_price_schedule: Optional[EVAbsolutePriceSchedule] = None


@dataclass
class EVPowerSchedule:
    ev_power_schedule_entries: List[EVPowerScheduleEntry]
    time_anchor: str
    custom_data: Optional[CustomData] = None


@dataclass
class EVPowerScheduleEntry:
    duration: int
    power: float
    custom_data: Optional[CustomData] = None


@dataclass
class EVPriceRule:
    energy_fee: float
    power_range_start: float
    custom_data: Optional[CustomData] = None


@dataclass
class EVSE:
    id: int
    connector_id: Optional[int] = None
    custom_data: Optional[CustomData] = None


@dataclass
class EventData:
    actual_value: str
    component: Component
    event_id: int
    event_notification_type: EventNotification
    timestamp: str
    trigger: EventTrigger
    variable: Variable
    cause: Optional[int] = None
    cleared: Optional[bool] = None
    custom_data: Optional[CustomData] = None
    tech_code: Optional[str] = None
    tech_info: Optional[str] = None
    transaction_id: Optional[str] = None
    variable_monitoring_id: Optional[int] = None


@dataclass
class Firmware:
    location: str
    retrieve_date_time: str
    custom_data: Optional[CustomData] = None
    install_date_time: Optional[str] = None
    signature: Optional[str] = None
    signing_certificate: Optional[str] = None


@dataclass
class GetVariableData:
    component: Component
    variable: Variable
    attribute_type: Attribute = Attribute.actual
    custom_data: Optional[CustomData] = None


@dataclass
class GetVariableResult:
    attribute_status: GetVariableStatus
    component: Component
    variable: Variable
    attribute_status_info: Optional[StatusInfo] = None
    attribute_type: Attribute = Attribute.actual
    attribute_value: Optional[str] = None
    custom_data: Optional[CustomData] = None


@dataclass
class IdToken:
    id_token: str
    type: enums.IdToken
    additional_info: Optional[List[AdditionalInfo]] = None
    custom_data: Optional[CustomData] = None


@dataclass
class IdTokenInfo:
    status: AuthorizationStatus
    cache_expiry_date_time: Optional[str] = None
    charging_priority: Optional[int] = None
    custom_data: Optional[CustomData] = None
    evse_id: Optional[List[int]] = None
    group_id_token: Optional[IdToken] = None
    language1: Optional[str] = None
    language2: Optional[str] = None
    personal_message: Optional[MessageContent] = None


@dataclass
class LimitBeyondSoC:
    limit: float
    soc: int
    custom_data: Optional[CustomData] = None


@dataclass
class LogParameters:
    remote_location: str
    custom_data: Optional[CustomData] = None
    latest_timestamp: Optional[str] = None
    oldest_timestamp: Optional[str] = None


@dataclass
class MessageContent:
    content: str
    format: MessageFormat
    custom_data: Optional[CustomData] = None
    language: Optional[str] = None


@dataclass
class MessageInfo:
    id: int
    message: MessageContent
    priority: MessagePriority
    custom_data: Optional[CustomData] = None
    display: Optional[Component] = None
    end_date_time: Optional[str] = None
    start_date_time: Optional[str] = None
    state: Optional[MessageState] = None
    transaction_id: Optional[str] = None


@dataclass
class MeterValue:
    sampled_value: List[SampledValue]
    timestamp: str
    custom_data: Optional[CustomData] = None


@dataclass
class Modem:
    custom_data: Optional[CustomData] = None
    iccid: Optional[str] = None
    imsi: Optional[str] = None


@dataclass
class MonitoringData:
    component: Component
    variable: Variable
    variable_monitoring: List[VariableMonitoring]
    custom_data: Optional[CustomData] = None


@dataclass
class NetworkConnectionProfile:
    message_timeout: int
    ocpp_csms_url: str
    ocpp_interface: OCPPTransport
    ocpp_transport: OCPPTransport
    ocpp_version: OCPPVersion
    security_profile: int
    apn: Optional[APN] = None
    custom_data: Optional[CustomData] = None
    vpn: Optional[VPN] = None


@dataclass
class OCSPRequestData:
    hash_algorithm: HashAlgorithm
    issuer_key_hash: str
    issuer_name_hash: str
    responder_url: str
    serial_number: str
    custom_data: Optional[CustomData] = None


@dataclass
class OverstayRuleList:
    custom_data: Optional[CustomData] = None
    overstay_power_threshold: Optional[RationalNumber] = None
    overstay_time_threshold: Optional[int] = None


@dataclass
class PriceLevelSchedule:
    number_of_price_levels: int
    price_level_schedule_entries: List[PriceLevelScheduleEntry]
    price_schedule_id: int
    time_anchor: str
    custom_data: Optional[CustomData] = None
    price_schedule_description: Optional[str] = None


@dataclass
class PriceLevelScheduleEntry:
    duration: int
    price_level: int
    custom_data: Optional[CustomData] = None


@dataclass
class PriceRule:
    energy_fee: RationalNumber
    power_range_start: RationalNumber
    carbon_dioxide_emission: Optional[int] = None
    custom_data: Optional[CustomData] = None
    parking_fee: Optional[RationalNumber] = None
    parking_fee_period: Optional[int] = None
    renewable_generation_percentage: Optional[int] = None


@dataclass
class PriceRuleStack:
    duration: int
    price_rule: List[PriceRule]
    custom_data: Optional[CustomData] = None


@dataclass
class RationalNumber:
    exponent: int
    value: int
    custom_data: Optional[CustomData] = None


@dataclass
class RelativeTimeInterval:
    start: int
    custom_data: Optional[CustomData] = None
    duration: Optional[int] = None


@dataclass
class ReportData:
    component: Component
    variable: Variable
    variable_attribute: List[VariableAttribute]
    custom_data: Optional[CustomData] = None
    variable_characteristics: Optional[VariableCharacteristics] = None


@dataclass
class ResponseClearMonitoringResult:
    id: int
    status: ClearMonitoringStatus
    custom_data: Optional[CustomData] = None
    status_info: Optional[StatusInfo] = None


@dataclass
class SalesTariff:
    id: int
    sales_tariff_entry: List[SalesTariffEntry]
    custom_data: Optional[CustomData] = None
    num_e_price_levels: Optional[int] = None
    sales_tariff_description: Optional[str] = None


@dataclass
class SalesTariffEntry:
    relative_time_interval: RelativeTimeInterval
    consumption_cost: Optional[List[ConsumptionCost]] = None
    custom_data: Optional[CustomData] = None
    e_price_level: Optional[int] = None


@dataclass
class SampledValue:
    value: float
    context: ReadingContext = ReadingContext.sample_periodic
    custom_data: Optional[CustomData] = None
    location: Location = Location.outlet
    measurand: Measurand = Measurand.energy_active_import_register
    phase: Optional[Phase] = None
    signed_meter_value: Optional[SignedMeterValue] = None
    unit_of_measure: Optional[UnitOfMeasure] = None


@dataclass
class SetMonitoringData:
    component: Component
    severity: int
    type: Monitor
    value: float
    variable: Variable
    custom_data: Optional[CustomData] = None
    id: Optional[int] = None
    transaction: bool = False


@dataclass
class SetMonitoringResult:
    component: Component
    severity: int
    status: SetMonitoringStatus
    type: Monitor
    variable: Variable
    custom_data: Optional[CustomData] = None
    id: Optional[int] = None
    status_info: Optional[StatusInfo] = None


@dataclass
class SetVariableData:
    attribute_value: str
    component: Component
    variable: Variable
    attribute_type: Attribute = Attribute.actual
    custom_data: Optional[CustomData] = None


@dataclass
class SetVariableResult:
    attribute_status: SetVariableStatus
    component: Component
    variable: Variable
    attribute_status_info: Optional[StatusInfo] = None
    attribute_type: Attribute = Attribute.actual
    custom_data: Optional[CustomData] = None


@dataclass
class SignedMeterValue:
    encoding_method: str
    public_key: str
    signed_meter_data: str
    signing_method: str
    custom_data: Optional[CustomData] = None


@dataclass
class StatusInfo:
    reason_code: str
    additional_info: Optional[str] = None
    custom_data: Optional[CustomData] = None


@dataclass
class TaxRule:
    applies_to_energy_fee: bool
    applies_to_minimum_maximum_cost: bool
    applies_to_overstay_fee: bool
    applies_to_parking_fee: bool
    tax_rate: RationalNumber
    tax_rule_id: int
    custom_data: Optional[CustomData] = None
    tax_included_in_price: Optional[bool] = None
    tax_rule_name: Optional[str] = None


@dataclass
class Transaction:
    transaction_id: str
    charging_state: Optional[ChargingState] = None
    custom_data: Optional[CustomData] = None
    operation_mode: Optional[OperationMode] = None
    remote_start_id: Optional[int] = None
    stopped_reason: Optional[Reason] = None
    time_spent_charging: Optional[int] = None


@dataclass
class UnitOfMeasure:
    custom_data: Optional[CustomData] = None
    multiplier: int = 0
    unit: str = "Wh"


@dataclass
class V2XChargingParameters:
    custom_data: Optional[CustomData] = None
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
class V2XFreqWattEntry:
    frequency: float
    power: float
    custom_data: Optional[CustomData] = None


@dataclass
class V2XSignalWattEntry:
    power: float
    signal: int
    custom_data: Optional[CustomData] = None


@dataclass
class VPN:
    key: str
    password: str
    server: str
    type: enums.VPN
    user: str
    custom_data: Optional[CustomData] = None
    group: Optional[str] = None


@dataclass
class Variable:
    name: str
    custom_data: Optional[CustomData] = None
    instance: Optional[str] = None


@dataclass
class VariableAttribute:
    constant: bool = False
    custom_data: Optional[CustomData] = None
    mutability: Mutability = Mutability.read_write
    persistent: bool = False
    type: Attribute = Attribute.actual
    value: Optional[str] = None


@dataclass
class VariableCharacteristics:
    data_type: Data
    supports_monitoring: bool
    custom_data: Optional[CustomData] = None
    max_limit: Optional[float] = None
    min_limit: Optional[float] = None
    unit: Optional[str] = None
    values_list: Optional[str] = None


@dataclass
class VariableMonitoring:
    id: int
    severity: int
    transaction: bool
    type: Monitor
    value: float
    custom_data: Optional[CustomData] = None
