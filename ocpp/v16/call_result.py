from typing import Dict, List, Optional
from dataclasses import dataclass

from ocpp.v16.enums import (
    AvailabilityStatus,
    CancelReservationStatus,
    ChargingProfileStatus,
    ClearCacheStatus,
    ClearChargingProfileStatus,
    ConfigurationStatus,
    DataTransferStatus,
    GetCompositeScheduleStatus,
    RegistrationStatus,
    RemoteStartStopStatus,
    ReservationStatus,
    ResetStatus,
    TriggerMessageStatus,
    UpdateStatus,
    UnlockStatus,
    CertificateSignedStatus,
    CertificateStatus,
    DeleteCertificateStatus,
    GenericStatus,
    GetInstalledCertificateStatus,
    LogStatus,
    UpdateFirmwareStatus
)

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
    status: RegistrationStatus


@dataclass
class DiagnosticsStatusNotificationPayload:
    pass


@dataclass
class FirmwareStatusNotificationPayload:
    pass


@dataclass
class HeartbeatPayload:
    current_time: str


@dataclass
class LogStatusNotificationPayload:
    pass


@dataclass
class SecurityEventNotificationPayload:
    pass


@dataclass
class SignCertificatePayload:
    status: GenericStatus


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
    id_tag_info: Optional[Dict] = None


# The CALLRESULT messages that flow from Charge Point to Central System are
# listed in the bottom part of this module.


@dataclass
class CancelReservationPayload:
    status: CancelReservationStatus


@dataclass
class CertificateSignedPayload:
    status: CertificateSignedStatus


@dataclass
class ChangeAvailabilityPayload:
    status: AvailabilityStatus


@dataclass
class ChangeConfigurationPayload:
    status: ConfigurationStatus


@dataclass
class ClearCachePayload:
    status: ClearCacheStatus


@dataclass
class ClearChargingProfilePayload:
    status: ClearChargingProfileStatus


@dataclass
class DeleteCertificatePayload:
    status: DeleteCertificateStatus


@dataclass
class ExtendedTriggerMessagePayload:
    status: TriggerMessageStatus


@dataclass
class GetInstalledCertificateIdsPayload:
    status: GetInstalledCertificateStatus
    certificate_hash_data: Optional[List] = None


@dataclass
class GetCompositeSchedulePayload:
    status: GetCompositeScheduleStatus
    connector_id: Optional[int] = None
    schedule_start: Optional[str] = None
    charging_schedule: Optional[Dict] = None


@dataclass
class GetConfigurationPayload:
    configuration_key: Optional[List] = None
    unknown_key: Optional[List] = None


@dataclass
class GetDiagnosticsPayload:
    file_name: Optional[str] = None


@dataclass
class GetLocalListVersionPayload:
    list_version: int


@dataclass
class GetLogPayload:
    status: LogStatus
    filename: Optional[str] = None


@dataclass
class InstallCertificatePayload:
    status: CertificateStatus


@dataclass
class RemoteStartTransactionPayload:
    status: RemoteStartStopStatus


@dataclass
class RemoteStopTransactionPayload:
    status: RemoteStartStopStatus


@dataclass
class ReserveNowPayload:
    status: ReservationStatus


@dataclass
class ResetPayload:
    status: ResetStatus


@dataclass
class SendLocalListPayload:
    status: UpdateStatus


@dataclass
class SetChargingProfilePayload:
    status: ChargingProfileStatus


@dataclass
class SignedFirmwareStatusNotificationPayload:
    pass


@dataclass
class SignedUpdateFirmwarePayload:
    status: UpdateFirmwareStatus


@dataclass
class TriggerMessagePayload:
    status: TriggerMessageStatus


@dataclass
class UnlockConnectorPayload:
    status: UnlockStatus


@dataclass
class UpdateFirmwarePayload:
    pass


# The DataTransfer CALLRESULT can be send both from Central System as well as
# from a Charge Point.


@dataclass
class DataTransferPayload:
    status: DataTransferStatus
    data: Optional[str] = None
