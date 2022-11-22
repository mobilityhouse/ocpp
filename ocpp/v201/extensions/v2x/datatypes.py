from dataclasses import dataclass
from typing import List, Optional

from ocpp.v201 import enums as v201_enums
from ocpp.v201.datatypes import (
    ACChargingParametersType,
    DCChargingParametersType,
    MessageContentType,
    SalesTariffType,
)
from ocpp.v201.extensions.v2x import enums as v2x_enums


@dataclass
class AdditionalInfoType:
    """
    Contains a case insensitive identifier to use for the authorization and the
    type of authorization to support multiple forms of identifiers.
    AdditionalInfoType is used by: IdTokenType
    """

    additional_id_token: str
    type: str


@dataclass
class IdTokenType:
    """
    Contains a case insensitive identifier to use for the authorization and the
    type of authorization to support multiple forms of identifiers.
    IdTokenType is used by: AuthorizationData, Common:IdTokenInfoType,
    RequestStartTransactionRequest, AuthorizeRequest, TransactionEventRequest,
    ReserveNowRequest, CustomerInformationRequest
    """

    id_token: str
    type: v2x_enums.IdTokenType
    additional_info: Optional[AdditionalInfoType] = None


@dataclass
class IdTokenInfoType:
    """
    Contains status information about an identifier. It is advised to not stop
    charging for a token that expires during charging, as ExpiryDate is only
    used for caching purposes. If ExpiryDate is not given, the status has no
    end date.
    IdTokenInfoType is used by: AuthorizationData, AuthorizeResponse,
    TransactionEventResponse
    """

    status: v201_enums.AuthorizationStatusType
    cache_expiry_date_time: Optional[str] = None
    charging_priority: Optional[int] = None
    language_1: Optional[str] = None
    evse_id: Optional[int] = None
    language_2: Optional[str] = None
    group_id_token: Optional[IdTokenType] = None
    personal_message: Optional[MessageContentType] = None


@dataclass
class V2XChargingParametersType:
    min_charge_power: Optional[float] = None
    min_charge_power_l2: Optional[float] = None
    min_charge_power_l3: Optional[float] = None
    max_charge_power: Optional[float] = None
    max_charge_power_l2: Optional[float] = None
    max_charge_power_l3: Optional[float] = None
    min_discharge_power: Optional[float] = None
    min_discharge_power_l2: Optional[float] = None
    min_discharge_power_l3: Optional[float] = None
    max_discharge_power: Optional[float] = None
    max_discharge_power_l2: Optional[float] = None
    max_discharge_power_l3: Optional[float] = None
    min_charge_current: Optional[float] = None
    max_charge_current: Optional[float] = None
    min_discharge_current: Optional[float] = None
    max_discharge_current: Optional[float] = None
    min_voltage: Optional[float] = None
    max_voltage: Optional[float] = None
    ev_target_energy_request: Optional[float] = None
    ev_min_energy_request: Optional[float] = None
    ev_max_energy_request: Optional[float] = None
    ev_min_v2x_energy_request: Optional[float] = None
    ev_max_v2x_energy_request: Optional[float] = None
    target_soc: Optional[int] = None


@dataclass
class EVPowerScheduleEntryType:
    duration: int
    power: float


@dataclass
class EVPowerScheduleType:
    time_anchor: str
    ev_power_schedule_entries: EVPowerScheduleEntryType


@dataclass
class EVPriceRuleType:
    energy_fee: float
    power_range_start: float


@dataclass
class EVAbsolutePriceScheduleEntryType:
    duration: int
    ev_price_rules: EVPriceRuleType


@dataclass
class EVAbsolutePriceScheduleType:
    time_anchor: str
    currency: str
    price_algorithm: str
    ev_absolute_price_schedule_entries: EVAbsolutePriceScheduleEntryType


@dataclass
class EVEnergyOfferType:
    ev_power_schedule: EVPowerScheduleType
    ev_absolute_price_schedule: EVAbsolutePriceScheduleType


@dataclass
class ChargingNeedsType:
    """
    ChargingNeedsType is used by: NotifyEVChargingNeedsRequest
    """

    request_energy_transfer: v2x_enums.EnergyTransferModeType
    departure_time: Optional[str] = None
    ac_charging_parameters: Optional[ACChargingParametersType] = None
    dc_charging_parameters: Optional[DCChargingParametersType] = None
    # V2X added
    available_energy_transfer: Optional[v2x_enums.EnergyTransferModeType] = None
    control_mode: Optional[v2x_enums.ControlModeType] = None
    mobility_needs_mode: Optional[int] = None
    v2x_charging_parameters: Optional[V2XChargingParametersType] = None
    ev_energy_offer: Optional[EVEnergyOfferType] = None


@dataclass
class V2XPowerFrequencyEntryType:
    frequency: float
    power: float


@dataclass
class V2XVoltagePfEntryType:
    voltage: float
    pf: float


@dataclass
class ChargingSchedulePeriodType:
    """
    Charging schedule period structure defines a time period in a charging
    schedule.
    ChargingSchedulePeriodType is used by: ChargingScheduleType,
    CompositeScheduleType
    """

    start_period: int
    limit: Optional[float] = None
    limit_l2: Optional[float] = None
    limit_l3: Optional[float] = None
    number_phases: Optional[int] = None
    phase_to_use: Optional[int] = None
    discharge_limit: Optional[float] = None
    discharge_limit_l2: Optional[float] = None
    discharge_limit_l3: Optional[float] = None
    setpoint: Optional[float] = None
    setpoint_l2: Optional[float] = None
    setpoint_l3: Optional[float] = None
    setpoint_reactive: Optional[float] = None
    setpoint_reactive_l2: Optional[float] = None
    setpoint_reactive_l3: Optional[float] = None
    preconditioning_request: Optional[bool] = None
    v2x_operation_mode: Optional[v2x_enums.V2XOperationModeType] = None
    v2x_power_frequency_table: Optional[V2XPowerFrequencyEntryType] = None
    v2x_voltage_pf_table: Optional[V2XVoltagePfEntryType] = None


@dataclass
class AbsolutePriceScheduleType:
    time_anchor: str
    price_schedule_id: str
    price_schedule_description: str
    currency: str
    language: str
    price_algorithm: str


@dataclass
class ChargingScheduleType:
    """
    Charging schedule structure defines a list of charging periods, as used in:
    GetCompositeSchedule.conf and ChargingProfile.
    ChargingScheduleType is used by: ChargingProfileType,
    NotifyChargingLimitRequest, NotifyEVChargingScheduleRequest
    """

    id: int
    charging_rate_unit: v201_enums.ChargingRateUnitType
    charging_schedule_period: ChargingSchedulePeriodType
    start_schedule: Optional[str] = None
    duration: Optional[int] = None
    min_charging_rate: Optional[float] = None
    sales_tariff: Optional[SalesTariffType] = None
    absolute_price_schedule: Optional[AbsolutePriceScheduleType] = None


@dataclass
class ChargingProfileType:
    """
    A ChargingProfile consists of ChargingSchedule, describing the amount of
    power or current that can be delivered per time interval.
    ChargingProfileType is used by: RequestStartTransactionRequest,
    SetChargingProfileRequest, ReportChargingProfilesRequest
    """

    id: int
    stack_level: int
    charging_profile_purpose: v2x_enums.ChargingProfilePurposeType
    charging_profile_kind: v2x_enums.ChargingProfileKindType
    charging_schedule: ChargingScheduleType
    valid_from: Optional[str] = None
    valid_to: Optional[str] = None
    transaction_id: Optional[str] = None


@dataclass
class ChargingProfileUpdateType:
    valid_to: Optional[str] = None
    max_offline_duration: Optional[int] = None
    update_interval: Optional[int] = None


@dataclass
class ChargingScheduleUpdateType:
    id: int
    start_schedule: Optional[str] = None
    duration: Optional[int] = None
    charging_schedule_period: Optional[List[ChargingSchedulePeriodType]] = None
