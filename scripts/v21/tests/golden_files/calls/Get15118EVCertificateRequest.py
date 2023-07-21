from dataclasses import dataclass
from typing import Any, List, Optional

from ocpp.v21.datatypes import (
    CustomData,
)

from ocpp.v21.enums import (
    CertificateAction,
)


@dataclass
class Get15118EVCertificate:
    action: CertificateAction
    exi_request: str
    iso_15118_schema_version: str
    custom_data: Optional[CustomData] = None
    maximum_contract_certificate_chains: Optional[int] = None
    prioritized_emaids: Optional[List[str]] = None
