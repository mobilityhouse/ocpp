from dataclasses import dataclass
from typing import Any, List, Optional

from datatypes import (
    CustomData,
    ReportData,
)


@dataclass
class NotifyReport:
    generated_at: str
    request_id: int
    seq_no: int
    custom_data: Optional[CustomData] = None
    report_data: Optional[List[ReportData]] = None
    tbc: bool = False
