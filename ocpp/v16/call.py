from typing import Any, Dict, List
from dataclasses import dataclass, field

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
    type: str


@dataclass
class ChangeConfigurationPayload:
    key: str
    value: Any


@dataclass
class ClearCachePayload:
    pass


@dataclass
class ClearChargingProfilePayload:
    id: int = None
    connector_id: str = None
    charger_profile_purpose: str = None
    stack_level: int = None


@dataclass
class GetCompositeSchedulePayload:
    connector_id: int
    duration: int
    charging_rate_unit: str = None


@dataclass
class GetConfigurationPayload:
    key: str = None


@dataclass
class GetDiagnosticsPayload:
    location: str
    retries: int = None
    retry_interval: int = None
    start_time: str = None
    stop_time: str = None


@dataclass
class GetLocalListVersionPayload:
    pass


@dataclass
class RemoteStartTransactionPayload:
    id_tag: int
    connector_id: int = None
    charging_profile: Dict = None


@dataclass
class RemoteStopTransactionPayload:
    transaction_id: int


@dataclass
class ReserveNowPayload:
    connector_id: int
    expiry_date: str
    id_tag: str
    reservation_id: int
    parent_id_tag: str


@dataclass
class ResetPayload:
    type: str


@dataclass
class SendLocalListPayload:
    list_version: int
    update_type: str
    local_authorization_list: List = field(default_factory=list)


@dataclass
class SetChargingProfilePayload:
    connector_id: int
    cs_charging_profiles: Dict


@dataclass
class TriggerMessagePayload:
    requested_message: str
    connector_id: int = None


@dataclass
class UnlockConnectorPayload:
    connector_id: int


@dataclass
class UpdateFirmwarePayload:
    location: str
    retrieve_date: str
    retries: int = None
    retry_interval: int = None


# The CALL messages that flow from Charge Point to Central System are listed
# in the bottom part of this module.

@dataclass
class AuthorizePayload:
    id_tag: str


@dataclass
class BootNotificationPayload:
    charge_point_model: str
    charge_point_vendor: str
    charge_box_serial_number: str = None
    charge_point_serial_number: str = None
    firmware_version: str = None
    iccid: str = None
    imsi: str = None
    meter_serial_number: str = None
    meter_type: str = None


@dataclass
class DiagnosticStatusNotificationPayload:
    status: str


@dataclass
class FirmwareStatusNotificationPayload:
    status: str


@dataclass
class HeartbeatPayload:
    pass


@dataclass
class MeterValuesPayload:
    connector_id: str
    meter_value: Dict = field(default_factory=dict)
    transaction_id: str = None


@dataclass
class StartTransactionPayload:
    connector_id: int
    id_tag: str
    meter_start: int
    timestamp: str
    reservation_id: int = None


@dataclass
class StopTransactionPayload:
    meter_stop: int
    timestamp: str
    transaction_id: int
    reason: str = None
    id_tag: str = None
    transaction_data: Dict = None


@dataclass
class StatusNotificationPayload:
    connector_id: int
    error_code: str
    status: str
    timestamp: str = None
    info: str = None
    vendor_id: str = None
    vendor_error_code: str = None


# The DataTransfer CALL can be send both from Central System as well as from a
# Charge Point.


@dataclass
class DataTransferPayload:
    vendor_id: str
    message_id: str = None
    data: Any = None
