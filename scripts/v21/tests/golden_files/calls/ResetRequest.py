from dataclasses import dataclass
from typing import Any, List, Optional

from ocpp.v21.datatypes import (
    CustomData,
)

from ocpp.v21 import enums


@dataclass
class Reset:
    type: enums.Reset
    custom_data: Optional[CustomData] = None
    evse_id: Optional[int] = None
