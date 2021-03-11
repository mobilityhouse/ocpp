from dataclasses import dataclass
from typing import Optional, List

from ocpp.v16.enums import (
    ChargingRateUnitType,
    ChargingProfilePurposeType,
    ChargingProfileKindType,
    RecurrencyKind
)


@dataclass
class ChargingSchedulePeriod:
    """Charging schedule period structure defines a time period
     in a charging schedule, as used in: ChargingSchedule."""
    start_period: int
    limit: float
    number_phases: Optional[int] = None


@dataclass
class ChargingSchedule:
    """Charging schedule structure defines a list of charging periods,
    as used in: GetCompositeSchedule.conf and ChargingProfile."""

    charging_rate_unit: ChargingRateUnitType
    charging_schedule_period: List[ChargingSchedulePeriod]
    duration: Optional[int] = None
    start_schedule: Optional[str] = None
    min_charging_rate: Optional[float] = None


@dataclass
class ChargingProfile:
    """A ChargingProfile consists of a ChargingSchedule, describing the
    amount of power or current that can be delivered per time interval."""
    charging_profile_id: int
    stack_level: int
    charging_profile_purpose: ChargingProfilePurposeType
    charging_profile_kind: ChargingProfileKindType
    charging_schedule: ChargingSchedule
    transaction_id: Optional[int] = None
    recurrency_kind: Optional[RecurrencyKind] = None
    valid_from: Optional[str] = None
    valid_to: Optional[str] = None
