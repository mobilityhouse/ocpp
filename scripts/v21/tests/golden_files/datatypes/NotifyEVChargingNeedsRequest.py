from __future__ import annotations
from typing import List, Optional
from dataclasses import dataclass

from enums import (
    ControlMode,
    EnergyTransferMode,
    MobilityNeedsMode,
    Pricing,
)


@dataclass
class ACChargingParameters:
    energy_amount: float
    ev_max_current: float
    ev_max_voltage: float
    ev_min_current: float
    custom_data: Optional[CustomData] = None


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
