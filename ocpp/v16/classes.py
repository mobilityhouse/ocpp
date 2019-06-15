from functools import partial
from typing import List, Dict
from dataclasses import dataclass


@dataclass
class ChargingProfile:
    charging_profile_id: int
    stack_level: int
    charging_profile_purpose: str
    charging_profile_kind: str
    charging_schedule: ChargingSchedule
    transaction_id: int = None
    recurrency_kind: str = None
    valid_from: str = None
    valid_to str = None

    def __post_init__(self):
        if isinstance(self.charging_schedule, dict):
            self.charging_schedule = ChargingSchedule(**self.charging_schedule)

    def for_current_transaction(self, transaction_id=None):
        return ChargingProfile(
            charge_profile_id: transaction_id,
            stack_level: 99,
            charging_profile_purpose: "TxProfile",



@dataclass
class ChargingSchedule:
    charging_rate_unit: str
    charging_schedule_period = List[ChargingSchedulePeriod]
    min_charging_rate: float = None
    duration: int = None
    start_schedule: str = None

    def __post_init__(self):
        if isinstance(self.charging_schedule_period, list):
            for index, cs_period in enumerate(self.charging_schedule_period):
                if isinstance(cs_period, dict):
                    self.charging_schedule_period[index] = \
                        ChargingSchedulePeriod(**cs_period)


@dataclass
class ChargingSchedulePeriod:
    start_period: int
    limit: float
    number_of_phases: int = None


@dataclass
class IDTagInfo:
    status: str
    expiry_date: str = None
    parent_id_tag: Dict = None


@dataclass
class MeterValue:
    timestamp: str
    sampled_value: List[SampledValue]

    def __post_init__(self):
        if isinstance(self.sampled_value, list):
            for index, sampled_value in enumerate(self.sampled_value):
                if isinstance(sampled_value, dict):
                    self.sampled_value[index] = SampledValue(**sampled_value)


@dataclass
class SampledValue:
    value: str
    format: str = None
    context: str = None
    measurand: str = None
    phase: str = None
    location: str = None
    unit: str = None

    @staticmethod
    def prefill(**kwargs):
        return partial(SampledValue, **kwargs)
