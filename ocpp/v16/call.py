from decimal import Decimal
from typing import Any, Dict, List, Optional, Union
from dataclasses import dataclass, field

from ocpp.v16.enums import (
    AvailabilityType,
    ChargePointErrorCode,
    ChargePointStatus,
    ChargingProfileKindType,
    ChargingProfilePurposeType,
    ChargingRateUnitType,
    DiagnosticsStatus,
    FirmwareStatus,
    MessageTrigger,
    Reason,
    RecurrencyKind,
    ResetType,
    UpdateType,
)

# Most types of CALL messages can originate from only 1 source, either
# from a Charge Point or Central System, but not from both.
#
# Take for example the CALL for an ChangeConfiguration action. This type of
# CALL can only be send from a Central System to Charging Station, not
# the other way around.
#
# For some types of CALL messages the opposite is true; for example for the
# CALL message for a BootNotification action. This can only come from a Charge
# Point and send to a Central System.
#
# The only CALL that can originate from both a Central System and a
# Charge Point is the CALL message for a DataTransfer.

# The now following section of classes are for CALL messages that flow
# from Central System to Charge Point.


@dataclass
class CancelReservationPayload:
    reservation_id: int


@dataclass
class ChangeAvailabilityPayload:
    connector_id: int
    type: AvailabilityType


@dataclass
class ChangeConfigurationPayload:
    key: str
    value: Any


@dataclass
class ClearCachePayload:
    pass


@dataclass
class ClearChargingProfilePayload:
    id: Optional[int] = None
    connector_id: Optional[int] = None
    charging_profile_purpose: Optional[ChargingProfilePurposeType] = None
    stack_level: Optional[int] = None


@dataclass
class GetCompositeSchedulePayload:
    connector_id: int
    duration: int
    charging_rate_unit: Optional[ChargingRateUnitType] = None


@dataclass
class GetConfigurationPayload:
    key: Optional[List] = None


@dataclass
class GetDiagnosticsPayload:
    location: str
    retries: Optional[int] = None
    retry_interval: Optional[int] = None
    start_time: Optional[str] = None
    stop_time: Optional[str] = None


@dataclass
class GetLocalListVersionPayload:
    pass


@dataclass
class RemoteStartTransactionPayload:
    id_tag: str
    connector_id: Optional[int] = None
    charging_profile: Optional[Dict] = None


@dataclass
class RemoteStopTransactionPayload:
    transaction_id: int


@dataclass
class ReserveNowPayload:
    connector_id: int
    expiry_date: str
    id_tag: str
    reservation_id: int
    parent_id_tag: Optional[str] = None


@dataclass
class ResetPayload:
    type: ResetType


@dataclass
class SendLocalListPayload:
    list_version: int
    update_type: UpdateType
    local_authorization_list: List = field(default_factory=list)


@dataclass
class ChargingSchedulePeriod:
    """Charging schedule period structure defines a time period
     in a charging schedule, as used in: ChargingSchedule."""
    start_period: int
    limit: Decimal
    number_phases: Optional[int] = None


@dataclass
class ChargingSchedule:
    """Charging schedule structure defines a list of charging periods,
    as used in: GetCompositeSchedule.conf and ChargingProfile."""

    charging_rate_unit: ChargingRateUnitType
    charging_schedule_period: List[ChargingSchedulePeriod]
    duration: Optional[int] = None
    start_schedule: Optional[str] = None
    min_charging_rate: Optional[Decimal] = None


@dataclass
class ChargingProfile:
    """A ChargingProfile consists of a ChargingSchedule, describing the
    amount of power or current that can be delivered per time interval."""
    charging_profile_id: int
    stack_level: int
    charging_profile_purpose: ChargingProfilePurposeType
    charging_profile_kind: ChargingProfileKindType
    charging_schedule: ChargingSchedule
    transaction_id: Optional[int] = None
    recurrency_kind: Optional[RecurrencyKind] = None
    valid_from: Optional[str] = None
    valid_to: Optional[str] = None


@dataclass
class SetChargingProfilePayload:
    connector_id: int
    # Accept Dict for backwards compatibility
    cs_charging_profiles: Union[ChargingProfile, Dict]


@dataclass
class TriggerMessagePayload:
    requested_message: MessageTrigger
    connector_id: Optional[int] = None


@dataclass
class UnlockConnectorPayload:
    connector_id: int


@dataclass
class UpdateFirmwarePayload:
    location: str
    retrieve_date: str
    retries: Optional[int] = None
    retry_interval: Optional[int] = None


# The CALL messages that flow from Charge Point to Central System are listed
# in the bottom part of this module.

@dataclass
class AuthorizePayload:
    id_tag: str


@dataclass
class BootNotificationPayload:
    charge_point_model: str
    charge_point_vendor: str
    charge_box_serial_number: Optional[str] = None
    charge_point_serial_number: Optional[str] = None
    firmware_version: Optional[str] = None
    iccid: Optional[str] = None
    imsi: Optional[str] = None
    meter_serial_number: Optional[str] = None
    meter_type: Optional[str] = None


@dataclass
class DiagnosticsStatusNotificationPayload:
    status: DiagnosticsStatus


@dataclass
class FirmwareStatusNotificationPayload:
    status: FirmwareStatus


@dataclass
class HeartbeatPayload:
    pass


@dataclass
class MeterValuesPayload:
    connector_id: int
    meter_value: List = field(default_factory=list)
    transaction_id: Optional[int] = None


@dataclass
class StartTransactionPayload:
    connector_id: int
    id_tag: str
    meter_start: int
    timestamp: str
    reservation_id: Optional[int] = None


@dataclass
class StopTransactionPayload:
    meter_stop: int
    timestamp: str
    transaction_id: int
    reason: Optional[Reason] = None
    id_tag: Optional[str] = None
    transaction_data: Optional[List] = None


@dataclass
class StatusNotificationPayload:
    connector_id: int
    error_code: ChargePointErrorCode
    status: ChargePointStatus
    timestamp: Optional[str] = None
    info: Optional[str] = None
    vendor_id: Optional[str] = None
    vendor_error_code: Optional[str] = None


# The DataTransfer CALL can be send both from Central System as well as from a
# Charge Point.


@dataclass
class DataTransferPayload:
    vendor_id: str
    message_id: Optional[str] = None
    data: Optional[str] = None
