from dataclasses import dataclass
from typing import Dict, List, Optional

from ocpp.v201.extensions.v2x.datatypes import (
    ChargingNeedsType,
    ChargingProfileType,
    ChargingProfileUpdateType,
    ChargingScheduleType,
    ChargingScheduleUpdateType,
    IdTokenType,
)
from ocpp.v201.extensions.v2x.enums import EnergyTransferModeType


@dataclass
class AuthorizePayload:
    id_token: IdTokenType
    certificate: Optional[str] = None
    iso15118_certificate_hash_data: Optional[List] = None


@dataclass
class ModifyChargingProfilePayload:
    charging_profile_id: int
    charging_profile_update: Optional[ChargingProfileUpdateType] = None
    charging_schedule_update: Optional[ChargingScheduleUpdateType] = None


@dataclass
class NotifyAllowedEnergyTransferPayload:
    allowed_energy_transfer: Optional[EnergyTransferModeType] = None


@dataclass
class NotifyEVChargingNeedsPayload:
    charging_needs: ChargingNeedsType
    evse_id: int
    max_schedule_tuples: Optional[int] = None


@dataclass
class NotifyEVChargingSchedulePayload:
    time_base: str
    charging_schedule: ChargingScheduleType
    evse_id: int
    power_tolerance_acceptance: Optional[bool] = None


@dataclass
class NotifyPriorityChargingPayload:
    transaction_id: str
    activated: bool


@dataclass
class PullChargingProfileUpdatePayload:
    charging_profile_id: int


class SetChargingProfilePayload:
    evse_id: int
    charging_profile: ChargingProfileType


@dataclass
class TransactionEventPayload:
    event_type: str
    timestamp: str
    trigger_reason: str
    seq_no: int
    transaction_info: Dict
    meter_value: Optional[List] = None
    offline: Optional[bool] = None
    number_of_phases_used: Optional[int] = None
    cable_max_current: Optional[int] = None
    reservation_id: Optional[int] = None
    evse: Optional[Dict] = None
    id_token: Optional[Dict] = None
    allowed_energy_transfer: Optional[EnergyTransferModeType] = None


@dataclass
class UsePriorityChargingPayload:
    transaction_id: str
    activated: bool
