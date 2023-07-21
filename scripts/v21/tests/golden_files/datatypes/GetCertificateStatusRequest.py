from __future__ import annotations
from typing import List, Optional
from dataclasses import dataclass

from ocpp.v21.enums import (
    HashAlgorithm,
)


@dataclass
class CustomData:
    vendor_id: str


@dataclass
class OCSPRequestData:
    hash_algorithm: HashAlgorithm
    issuer_key_hash: str
    issuer_name_hash: str
    responder_url: str
    serial_number: str
    custom_data: Optional[CustomData] = None
