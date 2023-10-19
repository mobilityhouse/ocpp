from dataclasses import dataclass
from typing import List, Optional

from ocpp.v16.enums import (
    AuthorizationStatus,
    ChargingProfileKindType,
    ChargingProfilePurposeType,
    ChargingRateUnitType,
    CiStringType,
    Location,
    Measurand,
    Phase,
    ReadingContext,
    RecurrencyKind,
    UnitOfMeasure,
    ValueFormat,
)


@dataclass
class IdTagInfo:
    """
    Contains status information about an identifier. It is returned in
    Authorize, Start Transaction and Stop Transaction responses.

    If expiryDate is not given, the status has no end date.
    """

    status: AuthorizationStatus
    parent_id_tag: Optional[str] = None
    expiry_date: Optional[str] = None


@dataclass
class AuthorizationData:
    """
    Elements that constitute an entry of a Local Authorization List update.
    """

    id_tag: str
    id_tag_info: Optional[IdTagInfo] = None


@dataclass
class ChargingSchedulePeriod:
    start_period: int
    limit: float
    number_phases: Optional[int] = None


@dataclass
class ChargingSchedule:
    charging_rate_unit: ChargingRateUnitType
    charging_schedule_period: List[ChargingSchedulePeriod]
    duration: Optional[int] = None
    start_schedule: Optional[str] = None
    min_charging_rate: Optional[float] = None


@dataclass
class ChargingProfile:
    """
    A ChargingProfile consists of a ChargingSchedule, describing the
    amount of power or current that can be delivered per time interval.
    """

    charging_profile_id: int
    stack_level: int
    charging_profile_purpose: ChargingProfilePurposeType
    charging_profile_kind: ChargingProfileKindType
    charging_schedule: ChargingSchedule
    transaction_id: Optional[int] = None
    recurrency_kind: Optional[RecurrencyKind] = None
    valid_from: Optional[str] = None
    valid_to: Optional[str] = None


@dataclass
class KeyValue:
    """
    Contains information about a specific configuration key.
    It is returned in GetConfiguration.conf.
    """

    key: str
    readonly: bool
    value: Optional[str] = None

    def __post_init__(self):
        if len(self.key) > CiStringType.ci_string_50:
            msg = "Field key is longer than 50 characters"
            raise ValueError(msg)

        if self.value and len(self.value) > CiStringType.ci_string_500:
            msg = "Field key is longer than 500 characters"
            raise ValueError(msg)


@dataclass
class SampledValue:
    """
    Single sampled value in MeterValues. Each value can be accompanied by
    optional fields.
    """

    value: str
    context: Optional[ReadingContext] = None
    format: Optional[ValueFormat] = None
    measurand: Optional[Measurand] = None
    phase: Optional[Phase] = None
    location: Optional[Location] = None
    unit: Optional[UnitOfMeasure] = None


@dataclass
class MeterValue:
    """
    Collection of one or more sampled values in MeterValues.req.
    All sampled values in a MeterValue are sampled at the same point in time.
    """

    timestamp: str
    sampled_value: List[SampledValue]
