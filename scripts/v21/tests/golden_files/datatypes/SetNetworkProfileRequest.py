from __future__ import annotations
from typing import List, Optional
from dataclasses import dataclass

from ocpp.v21 import enums
from ocpp.v21.enums import (
    APNAuthentication,
    OCPPTransport,
    OCPPVersion,
)


@dataclass
class APN:
    apn: str
    apn_authentication: APNAuthentication
    apn_password: Optional[str] = None
    apn_user_name: Optional[str] = None
    custom_data: Optional[CustomData] = None
    preferred_network: Optional[str] = None
    sim_pin: Optional[int] = None
    use_only_preferred_network: bool = False


@dataclass
class CustomData:
    vendor_id: str


@dataclass
class NetworkConnectionProfile:
    message_timeout: int
    ocpp_csms_url: str
    ocpp_interface: OCPPTransport
    ocpp_transport: OCPPTransport
    ocpp_version: OCPPVersion
    security_profile: int
    apn: Optional[APN] = None
    custom_data: Optional[CustomData] = None
    vpn: Optional[VPN] = None


@dataclass
class VPN:
    key: str
    password: str
    server: str
    type: enums.VPN
    user: str
    custom_data: Optional[CustomData] = None
    group: Optional[str] = None
