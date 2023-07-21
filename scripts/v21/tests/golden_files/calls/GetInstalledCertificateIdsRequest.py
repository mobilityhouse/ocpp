from dataclasses import dataclass
from typing import Any, List, Optional

from ocpp.v21.datatypes import (
    CustomData,
)

from ocpp.v21.enums import (
    GetCertificateIdUse,
)


@dataclass
class GetInstalledCertificateIds:
    certificate_type: Optional[List[GetCertificateIdUse]] = None
    custom_data: Optional[CustomData] = None
