from __future__ import annotations
from typing import List, Optional
from dataclasses import dataclass


@dataclass
class CustomData:
    vendor_id: str


@dataclass
class EVSE:
    id: int
    connector_id: Optional[int] = None
    custom_data: Optional[CustomData] = None
