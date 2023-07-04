from dataclasses import dataclass
from typing import Any, List, Optional

from datatypes import (
    CustomData,
)

from enums import (
    GetCertificateIdUse,
)


@dataclass
class GetInstalledCertificateIds:
    certificate_type: Optional[List[GetCertificateIdUse]] = None
    custom_data: Optional[CustomData] = None
