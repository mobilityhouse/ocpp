from dataclasses import dataclass
from typing import Any, List, Optional

from datatypes import (
    CustomData,
)


@dataclass
class DataTransfer:
    vendor_id: str
    custom_data: Optional[CustomData] = None
    data: Any = None
    message_id: Optional[str] = None
