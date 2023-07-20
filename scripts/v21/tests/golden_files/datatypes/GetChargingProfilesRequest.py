from __future__ import annotations
from typing import List, Optional
from dataclasses import dataclass

from enums import (
    ChargingLimitSource,
    ChargingProfilePurpose,
)


@dataclass
class ChargingProfileCriterion:
    charging_limit_source: Optional[List[ChargingLimitSource]] = None
    charging_profile_id: Optional[List[int]] = None
    charging_profile_purpose: Optional[ChargingProfilePurpose] = None
    custom_data: Optional[CustomData] = None
    stack_level: Optional[int] = None


@dataclass
class CustomData:
    vendor_id: str
