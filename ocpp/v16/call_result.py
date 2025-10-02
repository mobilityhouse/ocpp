from dataclasses import dataclass
from typing import Dict, List, Optional

from ocpp.v16 import datatypes, enums

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
class Authorize:
    id_tag_info: datatypes.IdTagInfo


@dataclass
class BootNotification:
    current_time: str
    interval: int
    status: enums.RegistrationStatus


@dataclass
class DiagnosticsStatusNotification:
    pass


@dataclass
class FirmwareStatusNotification:
    pass


@dataclass
class Heartbeat:
    current_time: str


@dataclass
class LogStatusNotification:
    pass


@dataclass
class SecurityEventNotification:
    pass


@dataclass
class SignCertificate:
    status: enums.GenericStatus


@dataclass
class MeterValues:
    pass


@dataclass
class StartTransaction:
    transaction_id: int
    id_tag_info: datatypes.IdTagInfo


@dataclass
class StatusNotification:
    pass


@dataclass
class StopTransaction:
    id_tag_info: Optional[datatypes.IdTagInfo] = None


# The CALLRESULT messages that flow from Charge Point to Central System are
# listed in the bottom part of this module.


@dataclass
class CancelReservation:
    status: enums.CancelReservationStatus


@dataclass
class CertificateSigned:
    status: enums.CertificateSignedStatus


@dataclass
class ChangeAvailability:
    status: enums.AvailabilityStatus


@dataclass
class ChangeConfiguration:
    status: enums.ConfigurationStatus


@dataclass
class ClearCache:
    status: enums.ClearCacheStatus


@dataclass
class ClearChargingProfile:
    status: enums.ClearChargingProfileStatus


@dataclass
class DeleteCertificate:
    status: enums.DeleteCertificateStatus


@dataclass
class ExtendedTriggerMessage:
    status: enums.TriggerMessageStatus


@dataclass
class GetInstalledCertificateIds:
    status: enums.GetInstalledCertificateStatus
    certificate_hash_data: Optional[List] = None


@dataclass
class GetCompositeSchedule:
    status: enums.GetCompositeScheduleStatus
    connector_id: Optional[int] = None
    schedule_start: Optional[str] = None
    charging_schedule: Optional[Dict] = None


@dataclass
class GetConfiguration:
    configuration_key: Optional[List] = None
    unknown_key: Optional[List] = None


@dataclass
class GetDiagnostics:
    file_name: Optional[str] = None


@dataclass
class GetLocalListVersion:
    list_version: int


@dataclass
class GetLog:
    status: enums.LogStatus
    filename: Optional[str] = None


@dataclass
class InstallCertificate:
    status: enums.CertificateStatus


@dataclass
class RemoteStartTransaction:
    status: enums.RemoteStartStopStatus


@dataclass
class RemoteStopTransaction:
    status: enums.RemoteStartStopStatus


@dataclass
class ReserveNow:
    status: enums.ReservationStatus


@dataclass
class Reset:
    status: enums.ResetStatus


@dataclass
class SendLocalList:
    status: enums.UpdateStatus


@dataclass
class SetChargingProfile:
    status: enums.ChargingProfileStatus


@dataclass
class SignedFirmwareStatusNotification:
    pass


@dataclass
class SignedUpdateFirmware:
    status: enums.UpdateFirmwareStatus


@dataclass
class TriggerMessage:
    status: enums.TriggerMessageStatus


@dataclass
class UnlockConnector:
    status: enums.UnlockStatus


@dataclass
class UpdateFirmware:
    pass


# The DataTransfer CALLRESULT can be send both from Central System as well as
# from a Charge Point.


@dataclass
class DataTransfer:
    status: enums.DataTransferStatus
    data: Optional[str] = None
