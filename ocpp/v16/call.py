from dataclasses import dataclass, field
from typing import Dict, List, Optional

from ocpp.v16.enums import (
    AvailabilityType,
    CertificateUse,
    ChargePointErrorCode,
    ChargePointStatus,
    ChargingProfilePurposeType,
    ChargingRateUnitType,
    DiagnosticsStatus,
    FirmwareStatus,
    Log,
    MessageTrigger,
    Reason,
    ResetType,
    UpdateType,
    UploadLogStatus,
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
class CancelReservation:
    reservation_id: int


@dataclass
class CertificateSigned:
    certificate_chain: str


@dataclass
class ChangeAvailability:
    connector_id: int
    type: AvailabilityType


@dataclass
class ChangeConfiguration:
    key: str
    value: str


@dataclass
class ClearCache:
    pass


@dataclass
class ClearChargingProfile:
    id: Optional[int] = None
    connector_id: Optional[int] = None
    charging_profile_purpose: Optional[ChargingProfilePurposeType] = None
    stack_level: Optional[int] = None


@dataclass
class DeleteCertificate:
    certificate_hash_data: Dict


@dataclass
class ExtendedTriggerMessage:
    requested_message: MessageTrigger
    connector_id: Optional[int] = None


@dataclass
class GetCompositeSchedule:
    connector_id: int
    duration: int
    charging_rate_unit: Optional[ChargingRateUnitType] = None


@dataclass
class GetConfiguration:
    key: Optional[List] = None


@dataclass
class GetDiagnostics:
    location: str
    retries: Optional[int] = None
    retry_interval: Optional[int] = None
    start_time: Optional[str] = None
    stop_time: Optional[str] = None


@dataclass
class GetInstalledCertificateIds:
    certificate_type: CertificateUse


@dataclass
class GetLocalListVersion:
    pass


@dataclass
class GetLog:
    log: Dict
    log_type: Log
    request_id: int
    retries: Optional[int] = None
    retry_interval: Optional[int] = None


@dataclass
class InstallCertificate:
    certificate_type: CertificateUse
    certificate: str


@dataclass
class RemoteStartTransaction:
    id_tag: str
    connector_id: Optional[int] = None
    charging_profile: Optional[Dict] = None


@dataclass
class RemoteStopTransaction:
    transaction_id: int


@dataclass
class ReserveNow:
    connector_id: int
    expiry_date: str
    id_tag: str
    reservation_id: int
    parent_id_tag: Optional[str] = None


@dataclass
class Reset:
    type: ResetType


@dataclass
class SendLocalList:
    list_version: int
    update_type: UpdateType
    local_authorization_list: List = field(default_factory=list)


@dataclass
class SetChargingProfile:
    connector_id: int
    cs_charging_profiles: Dict


@dataclass
class SignedUpdateFirmware:
    request_id: int
    firmware: Dict
    retries: Optional[int] = None
    retry_interval: Optional[int] = None


@dataclass
class TriggerMessage:
    requested_message: MessageTrigger
    connector_id: Optional[int] = None


@dataclass
class UnlockConnector:
    connector_id: int


@dataclass
class UpdateFirmware:
    location: str
    retrieve_date: str
    retries: Optional[int] = None
    retry_interval: Optional[int] = None


# The CALL messages that flow from Charge Point to Central System are listed
# in the bottom part of this module.


@dataclass
class Authorize:
    id_tag: str


@dataclass
class BootNotification:
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
class DiagnosticsStatusNotification:
    status: DiagnosticsStatus


@dataclass
class FirmwareStatusNotification:
    status: FirmwareStatus


@dataclass
class Heartbeat:
    pass


@dataclass
class LogStatusNotification:
    status: UploadLogStatus
    request_id: int


@dataclass
class MeterValues:
    connector_id: int
    meter_value: List = field(default_factory=list)
    transaction_id: Optional[int] = None


@dataclass
class SecurityEventNotification:
    type: str
    timestamp: str
    tech_info: Optional[str]


@dataclass
class SignCertificate:
    csr: str


@dataclass
class SignedFirmwareStatusNotification:
    status: FirmwareStatus
    request_id: int


@dataclass
class StartTransaction:
    connector_id: int
    id_tag: str
    meter_start: int
    timestamp: str
    reservation_id: Optional[int] = None


@dataclass
class StopTransaction:
    meter_stop: int
    timestamp: str
    transaction_id: int
    reason: Optional[Reason] = None
    id_tag: Optional[str] = None
    transaction_data: Optional[List] = None


@dataclass
class StatusNotification:
    connector_id: int
    error_code: ChargePointErrorCode
    status: ChargePointStatus
    timestamp: Optional[str] = None
    info: Optional[str] = None
    vendor_id: Optional[str] = None
    vendor_error_code: Optional[str] = None


# The DataTransfer CALL can be sent both from Central System as well as from a
# Charge Point.


@dataclass
class DataTransfer:
    vendor_id: str
    message_id: Optional[str] = None
    data: Optional[str] = None


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class CancelReservationPayload:
    reservation_id: int


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class CertificateSignedPayload:
    certificate_chain: str


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class ChangeAvailabilityPayload:
    connector_id: int
    type: AvailabilityType


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class ChangeConfigurationPayload:
    key: str
    value: str


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class ClearCachePayload:
    pass


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class ClearChargingProfilePayload:
    id: Optional[int] = None
    connector_id: Optional[int] = None
    charging_profile_purpose: Optional[ChargingProfilePurposeType] = None
    stack_level: Optional[int] = None


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class DeleteCertificatePayload:
    certificate_hash_data: Dict


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class ExtendedTriggerMessagePayload:
    requested_message: MessageTrigger
    connector_id: Optional[int] = None


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class GetCompositeSchedulePayload:
    connector_id: int
    duration: int
    charging_rate_unit: Optional[ChargingRateUnitType] = None


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class GetConfigurationPayload:
    key: Optional[List] = None


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class GetDiagnosticsPayload:
    location: str
    retries: Optional[int] = None
    retry_interval: Optional[int] = None
    start_time: Optional[str] = None
    stop_time: Optional[str] = None


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class GetInstalledCertificateIdsPayload:
    certificate_type: CertificateUse


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class GetLocalListVersionPayload:
    pass


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class GetLogPayload:
    log: Dict
    log_type: Log
    request_id: int
    retries: Optional[int] = None
    retry_interval: Optional[int] = None


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class InstallCertificatePayload:
    certificate_type: CertificateUse
    certificate: str


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class RemoteStartTransactionPayload:
    id_tag: str
    connector_id: Optional[int] = None
    charging_profile: Optional[Dict] = None


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class RemoteStopTransactionPayload:
    transaction_id: int


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class ReserveNowPayload:
    connector_id: int
    expiry_date: str
    id_tag: str
    reservation_id: int
    parent_id_tag: Optional[str] = None


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class ResetPayload:
    type: ResetType


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class SendLocalListPayload:
    list_version: int
    update_type: UpdateType
    local_authorization_list: List = field(default_factory=list)


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class SetChargingProfilePayload:
    connector_id: int
    cs_charging_profiles: Dict


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class SignedUpdateFirmwarePayload:
    request_id: int
    firmware: Dict
    retries: Optional[int] = None
    retry_interval: Optional[int] = None


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class TriggerMessagePayload:
    requested_message: MessageTrigger
    connector_id: Optional[int] = None


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class UnlockConnectorPayload:
    connector_id: int


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class UpdateFirmwarePayload:
    location: str
    retrieve_date: str
    retries: Optional[int] = None
    retry_interval: Optional[int] = None


# The CALL messages that flow from Charge Point to Central System are listed
# in the bottom part of this module.


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class AuthorizePayload:
    id_tag: str


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
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


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class DiagnosticsStatusNotificationPayload:
    status: DiagnosticsStatus


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class FirmwareStatusNotificationPayload:
    status: FirmwareStatus


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class HeartbeatPayload:
    pass


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class LogStatusNotificationPayload:
    status: UploadLogStatus
    request_id: int


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class MeterValuesPayload:
    connector_id: int
    meter_value: List = field(default_factory=list)
    transaction_id: Optional[int] = None


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class SecurityEventNotificationPayload:
    type: str
    timestamp: str
    tech_info: Optional[str]


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class SignCertificatePayload:
    csr: str


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class SignedFirmwareStatusNotificationPayload:
    status: FirmwareStatus
    request_id: int


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class StartTransactionPayload:
    connector_id: int
    id_tag: str
    meter_start: int
    timestamp: str
    reservation_id: Optional[int] = None


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class StopTransactionPayload:
    meter_stop: int
    timestamp: str
    transaction_id: int
    reason: Optional[Reason] = None
    id_tag: Optional[str] = None
    transaction_data: Optional[List] = None


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
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


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class DataTransferPayload:
    vendor_id: str
    message_id: Optional[str] = None
    data: Optional[str] = None
