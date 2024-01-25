from dataclasses import dataclass
from typing import Dict, List, Optional

from ocpp.v16.datatypes import IdTagInfo
from ocpp.v16.enums import (
    AvailabilityStatus,
    CancelReservationStatus,
    CertificateSignedStatus,
    CertificateStatus,
    ChargingProfileStatus,
    ClearCacheStatus,
    ClearChargingProfileStatus,
    ConfigurationStatus,
    DataTransferStatus,
    DeleteCertificateStatus,
    GenericStatus,
    GetCompositeScheduleStatus,
    GetInstalledCertificateStatus,
    LogStatus,
    RegistrationStatus,
    RemoteStartStopStatus,
    ReservationStatus,
    ResetStatus,
    TriggerMessageStatus,
    UnlockStatus,
    UpdateFirmwareStatus,
    UpdateStatus,
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
class Authorize:
    id_tag_info: IdTagInfo


@dataclass
class BootNotification:
    current_time: str
    interval: int
    status: RegistrationStatus


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
    status: GenericStatus


@dataclass
class MeterValues:
    pass


@dataclass
class StartTransaction:
    transaction_id: int
    id_tag_info: IdTagInfo


@dataclass
class StatusNotification:
    pass


@dataclass
class StopTransaction:
    id_tag_info: Optional[IdTagInfo] = None


# The CALLRESULT messages that flow from Charge Point to Central System are
# listed in the bottom part of this module.


@dataclass
class CancelReservation:
    status: CancelReservationStatus


@dataclass
class CertificateSigned:
    status: CertificateSignedStatus


@dataclass
class ChangeAvailability:
    status: AvailabilityStatus


@dataclass
class ChangeConfiguration:
    status: ConfigurationStatus


@dataclass
class ClearCache:
    status: ClearCacheStatus


@dataclass
class ClearChargingProfile:
    status: ClearChargingProfileStatus


@dataclass
class DeleteCertificate:
    status: DeleteCertificateStatus


@dataclass
class ExtendedTriggerMessage:
    status: TriggerMessageStatus


@dataclass
class GetInstalledCertificateIds:
    status: GetInstalledCertificateStatus
    certificate_hash_data: Optional[List] = None


@dataclass
class GetCompositeSchedule:
    status: GetCompositeScheduleStatus
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
    status: LogStatus
    filename: Optional[str] = None


@dataclass
class InstallCertificate:
    status: CertificateStatus


@dataclass
class RemoteStartTransaction:
    status: RemoteStartStopStatus


@dataclass
class RemoteStopTransaction:
    status: RemoteStartStopStatus


@dataclass
class ReserveNow:
    status: ReservationStatus


@dataclass
class Reset:
    status: ResetStatus


@dataclass
class SendLocalList:
    status: UpdateStatus


@dataclass
class SetChargingProfile:
    status: ChargingProfileStatus


@dataclass
class SignedFirmwareStatusNotification:
    pass


@dataclass
class SignedUpdateFirmware:
    status: UpdateFirmwareStatus


@dataclass
class TriggerMessage:
    status: TriggerMessageStatus


@dataclass
class UnlockConnector:
    status: UnlockStatus


@dataclass
class UpdateFirmware:
    pass


# The DataTransfer CALLRESULT can be send both from Central System as well as
# from a Charge Point.


@dataclass
class DataTransfer:
    status: DataTransferStatus
    data: Optional[str] = None


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class AuthorizePayload:
    id_tag_info: IdTagInfo


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class BootNotificationPayload:
    current_time: str
    interval: int
    status: RegistrationStatus


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class DiagnosticsStatusNotificationPayload:
    pass


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class FirmwareStatusNotificationPayload:
    pass


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class HeartbeatPayload:
    current_time: str


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class LogStatusNotificationPayload:
    pass


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class SecurityEventNotificationPayload:
    pass


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class SignCertificatePayload:
    status: GenericStatus


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class MeterValuesPayload:
    pass


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class StartTransactionPayload:
    transaction_id: int
    id_tag_info: IdTagInfo


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class StatusNotificationPayload:
    pass


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class StopTransactionPayload:
    id_tag_info: Optional[IdTagInfo] = None


# The CALLRESULT messages that flow from Charge Point to Central System are
# listed in the bottom part of this module.


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class CancelReservationPayload:
    status: CancelReservationStatus


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class CertificateSignedPayload:
    status: CertificateSignedStatus


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class ChangeAvailabilityPayload:
    status: AvailabilityStatus


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class ChangeConfigurationPayload:
    status: ConfigurationStatus


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class ClearCachePayload:
    status: ClearCacheStatus


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class ClearChargingProfilePayload:
    status: ClearChargingProfileStatus


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class DeleteCertificatePayload:
    status: DeleteCertificateStatus


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class ExtendedTriggerMessagePayload:
    status: TriggerMessageStatus


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class GetInstalledCertificateIdsPayload:
    status: GetInstalledCertificateStatus
    certificate_hash_data: Optional[List] = None


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class GetCompositeSchedulePayload:
    status: GetCompositeScheduleStatus
    connector_id: Optional[int] = None
    schedule_start: Optional[str] = None
    charging_schedule: Optional[Dict] = None


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class GetConfigurationPayload:
    configuration_key: Optional[List] = None
    unknown_key: Optional[List] = None


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class GetDiagnosticsPayload:
    file_name: Optional[str] = None


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class GetLocalListVersionPayload:
    list_version: int


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class GetLogPayload:
    status: LogStatus
    filename: Optional[str] = None


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class InstallCertificatePayload:
    status: CertificateStatus


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class RemoteStartTransactionPayload:
    status: RemoteStartStopStatus


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class RemoteStopTransactionPayload:
    status: RemoteStartStopStatus


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class ReserveNowPayload:
    status: ReservationStatus


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class ResetPayload:
    status: ResetStatus


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class SendLocalListPayload:
    status: UpdateStatus


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class SetChargingProfilePayload:
    status: ChargingProfileStatus


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class SignedFirmwareStatusNotificationPayload:
    pass


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class SignedUpdateFirmwarePayload:
    status: UpdateFirmwareStatus


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class TriggerMessagePayload:
    status: TriggerMessageStatus


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class UnlockConnectorPayload:
    status: UnlockStatus


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class UpdateFirmwarePayload:
    pass


# The DataTransfer CALLRESULT can be send both from Central System as well as
# from a Charge Point.


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class DataTransferPayload:
    status: DataTransferStatus
    data: Optional[str] = None
