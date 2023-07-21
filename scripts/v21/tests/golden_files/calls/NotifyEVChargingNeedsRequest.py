from dataclasses import dataclass
from typing import Any, List, Optional

from ocpp.v21.datatypes import (
    ChargingNeeds,
    CustomData,
)


@dataclass
class NotifyEVChargingNeeds:
    charging_needs: ChargingNeeds
    evse_id: int
    custom_data: Optional[CustomData] = None
    max_schedule_tuples: Optional[int] = None
