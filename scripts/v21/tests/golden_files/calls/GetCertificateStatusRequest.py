from dataclasses import dataclass
from typing import Any, List, Optional

from ocpp.v21.datatypes import (
    CustomData,
    OCSPRequestData,
)


@dataclass
class GetCertificateStatus:
    ocsp_request_data: OCSPRequestData
    custom_data: Optional[CustomData] = None
