from dataclasses import dataclass
from typing import Dict, Optional

from ocpp.v201.enums import ChargingProfileStatus, GenericStatusType
from ocpp.v201.v2x.datatypes import (
    ChargingProfileUpdateType,
    ChargingScheduleUpdateType,
    IdTokenInfoType,
)
from ocpp.v201.v2x.enums import (
    EnergyTransferModeType,
    NotifyAllowedEnergyTransferStatusType,
    NotifyEVChargingNeedsStatusType,
    PriorityChargingStatusType,
)


@dataclass
class AuthorizePayload:
    id_token_info: IdTokenInfoType
    certificate_status: Optional[str] = None
    allowed_energy_transfer: Optional[EnergyTransferModeType] = None


@dataclass
class ModifyChargingProfilePayload:
    status: ChargingProfileStatus
    status_info: Optional[Dict] = None


@dataclass
class NotifyAllowedEnergyTransferPayload:
    status: NotifyAllowedEnergyTransferStatusType
    status_info: Optional[Dict] = None


@dataclass
class NotifyEVChargingNeedsPayload:
    status: NotifyEVChargingNeedsStatusType
    status_info: Optional[Dict] = None


@dataclass
class NotifyEVChargingSchedulePayload:
    status: GenericStatusType
    status_info: Optional[Dict] = None


@dataclass
class NotifyPriorityChargingPayload:
    pass


@dataclass
class PullChargingProfileUpdatePayload:
    charging_profile_update: Optional[ChargingProfileUpdateType] = None
    charging_schedule_update: Optional[ChargingScheduleUpdateType] = None


@dataclass
class SetChargingProfilePayload:
    status: ChargingProfileStatus
    status_info: Optional[Dict] = None


@dataclass
class TransactionEventPayload:
    total_cost: Optional[int] = None
    charging_priority: Optional[int] = None
    id_token_info: Optional[Dict] = None
    updated_personal_message: Optional[Dict] = None


@dataclass
class UsePriorityChargingPayload:
    status: PriorityChargingStatusType
    status_info: Optional[Dict] = None
