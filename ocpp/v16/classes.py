from functools import partial
from typing import List, Dict
from dataclasses import dataclass


@dataclass
class ChargingSchedulePeriod:
    """ ChargingSchedule

    :param start_period: Start of the periond in seconds, relative to the start
        of the schedule.
    :param limit: Power limit during this schedule period.
    :param number_of_phases: Optional. The number of phases that can be used for
        charging.

    """
    start_period: int
    limit: float
    number_of_phases: int = None


@dataclass
class ChargingSchedule:
    """

    :param charging_rate_unit: The unit of measure the charge limit is
        expresses in, "A" or "W".
    :param charging_schedule_period: List of :class:`ChargingSchedulePeriod` .
    :param min_charging_rate: Optional. Minimum charging rate supported by the
        vehicle.
    :param start_schedule: Optional. Starting point of an absolute schedule.
    :param duration: Optional. Duration of the charging schedule in seconds.

    """
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
class ChargingProfile:
    """ A ChargingProfile is used to limit the charge rate of a charging
    station over time.

    :param charging_profile_id: Unique identifier for a profile.
    :param stack_level: Number determining level in hierarchy of profiles.
    :param charging_profile_purpose: Defines the purpose of the schedule.
    :param charging_profile_kind: Defines the kind of schedule.
    :param charging_schedule: :class:`ChargingSchedule` containing the charge
        limits.
    :param transaction_id: Optional. Number that may be used to match profile
        to specific transaction.
    :param recurrency_kind: Optional. If schedule is recurring, it defines if
        schedule recurs either "Daily" or "Weekly".
    :param valid_from: Optional. Point in time at which the profile starts to
        be valid.
    :param valid_to: Optional. Point in time at which the profiles stops to be
        valid.
    """
    charging_profile_id: int
    stack_level: int
    charging_profile_purpose: str
    charging_profile_kind: str
    charging_schedule: ChargingSchedule
    transaction_id: int = None
    recurrency_kind: str = None
    valid_from: str = None
    valid_to: str = None

    def __post_init__(self):
        if isinstance(self.charging_schedule, dict):
            self.charging_schedule = ChargingSchedule(**self.charging_schedule)


@dataclass
class SampledValue:
    """

    :param value: The measured value.
    :param format: Optional. String defining the format, either "Raw" or
        "Signed".
    :param context: Optional. Type of detail value.
    :param measurand: Optional. Type of measurand.
    :param phase: Optional. Indicates how the measured value is to be
        interpreted.
    :param location: Optional. Location of the measurement.
    :param unit: Optional. The unit of the value.
    """
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



@dataclass
class IDTagInfo:
    """

    :param status: Contains whether the tag has been accepted by the central
        system or not.
    :param expiry_date: Optional. The date at which the tag should be removed
        from the Authorization Cache.
    :param parent_id_tag: Optional. This contains the parent identifier
    """
    status: str
    expiry_date: str = None
    parent_id_tag: Dict = None


@dataclass
class MeterValue:
    """

    :param timestamp: Timestamp for the measured values.
    :param sampled_value: List of :class:`SampledValue` s.

    """
    timestamp: str
    sampled_value: List[SampledValue]

    def __post_init__(self):
        if isinstance(self.sampled_value, list):
            for index, sampled_value in enumerate(self.sampled_value):
                if isinstance(sampled_value, dict):
                    self.sampled_value[index] = SampledValue(**sampled_value)
