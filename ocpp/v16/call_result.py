from typing import Dict
from dataclasses import dataclass

# Most types of CALLRESULT messages can originate from only 1 source, either
# from a Charge Point or Central System, but not from both.
#
# Take for example the CALLRESULT for an Authorize action. This type of
# CALLRESULT can only be send from a Central System to Charging Station, not
# the other way around.
#
# For some types of CALLRESULT messages the opposite is true; for example for
# the CALLRESULT message for a Reset action. This can only come from a Charge
# Point to a Central System.
#
# The only CALLRESULT that can originate from both a Central System and a
# Charge Point is the CALLRESULT message for a DataTransfer.

# The now following section of classes are for CALLRESULT messages that flow
# from Central System to Charge Point.


@dataclass
class AuthorizePayload:
    id_tag_info: Dict


@dataclass
class BootNotificationPayload:
    current_time: str
    interval: int
    status: str


@dataclass
class DiagnosticStatusNotificationPayload:
    pass


@dataclass
class FirmwareStatusNotificationPayload:
    pass


@dataclass
class HeartbeatPayload:
    current_time: str


@dataclass
class MeterValuesPayload:
    pass


@dataclass
class StartTransactionPayload:
    transaction_id: int
    id_tag_info: Dict


@dataclass
class StatusNotificationPayload:
    pass


@dataclass
class StopTransactionPayload:
    id_tag_info: Dict = None


# The CALLRESULT messages that flow from Charge Point to Central System are
# listed in the bottom part of this module.


@dataclass
class CancelReservationPayload:
    status: str


@dataclass
class ChangeAvailabilityPayload:
    status: str


@dataclass
class ChangeConfigurationPayload:
    status: str


@dataclass
class ClearCachePayload:
    status: str


@dataclass
class ClearChargingProfilePayload:
    status: str


@dataclass
class GetCompositeSchedulePayload:
    status: str
    connector_id: int = None
    schedule_start: str = None
    charging_schedule: Dict = None


@dataclass
class GetConfigurationPayload:
    configuration_key: Dict = None
    unknown_key: str = None


@dataclass
class GetDiagnosticsPayload:
    file_name: str = None


@dataclass
class GetLocalListVersionPayload:
    list_version: int


@dataclass
class RemoteStartTransactionPayload:
    status: str


@dataclass
class RemoteStopTransactionPayload:
    status: str


@dataclass
class ReserveNowPayload:
    status: str


@dataclass
class ResetPayload:
    status: str


@dataclass
class SendLocalListPayload:
    status: str


@dataclass
class SetChargingProfilePayload:
    status: str


@dataclass
class TriggerMessagePayload:
    status: str


@dataclass
class UnlockConnectorPayload:
    status: str


@dataclass
class UpdateFirmwarePayload:
    pass


# The DataTransfer CALLRESULT can be send both from Central System as well as
# from a Charge Point.


@dataclass
class DataTransferPayload:
    status: str
    data: Dict = None
