from functools import partial
from typing import List, Dict
from dataclasses import dataclass


@dataclass
class IDTagInfo:
    status: str
    expiry_date: str = None
    parent_id_tag: Dict = None


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


@dataclass
class MeterValue:
    timestamp: str
    sampled_value: List[SampledValue]

    def __post_init__(self):
        if isinstance(self.sampled_value, list):
            for index, sampled_value in enumerate(self.sampled_value):
                if isinstance(sampled_value, dict):
                    self.sampled_value[index] = SampledValue(**sampled_value)
