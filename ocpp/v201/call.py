import warnings
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class Authorize:
    id_token: Dict
    certificate: Optional[str] = None
    iso15118_certificate_hash_data: Optional[List] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class BootNotification:
    charging_station: Dict
    reason: str
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class CancelReservation:
    reservation_id: int
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class CertificateSigned:
    certificate_chain: str
    certificate_type: Optional[str] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class ChangeAvailability:
    operational_status: str
    evse: Optional[Dict] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class ClearCache:
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class ClearChargingProfile:
    charging_profile_id: Optional[int] = None
    charging_profile_criteria: Optional[Dict] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class ClearDisplayMessage:
    id: int
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class ClearVariableMonitoring:
    id: List
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class ClearedChargingLimit:
    charging_limit_source: str
    evse_id: Optional[int] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class CostUpdated:
    total_cost: int
    transaction_id: str
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class CustomerInformation:
    request_id: int
    report: bool
    clear: bool
    customer_certificate: Optional[Dict] = None
    id_token: Optional[Dict] = None
    customer_identifier: Optional[str] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class DataTransfer:
    vendor_id: str
    message_id: Optional[str] = None
    data: Optional[Any] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class DeleteCertificate:
    certificate_hash_data: Dict
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class FirmwareStatusNotification:
    status: str
    request_id: Optional[int] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class Get15118EVCertificate:
    iso15118_schema_version: str
    action: str
    exi_request: str
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class GetBaseReport:
    request_id: int
    report_base: str
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class GetCertificateStatus:
    ocsp_request_data: Dict
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class GetChargingProfiles:
    request_id: int
    charging_profile: Dict
    evse_id: Optional[int] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class GetCompositeSchedule:
    duration: int
    evse_id: int
    charging_rate_unit: Optional[str] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class GetDisplayMessages:
    request_id: int
    id: Optional[List] = None
    priority: Optional[str] = None
    state: Optional[str] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class GetInstalledCertificateIds:
    certificate_type: Optional[List] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class GetLocalListVersion:
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class GetLog:
    log: Dict
    log_type: str
    request_id: int
    retries: Optional[int] = None
    retry_interval: Optional[int] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class GetMonitoringReport:
    request_id: int
    component_variable: Optional[List] = None
    monitoring_criteria: Optional[List] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class GetReport:
    request_id: int
    component_variable: Optional[List] = None
    component_criteria: Optional[List] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class GetTransactionStatus:
    transaction_id: Optional[str] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class GetVariables:
    get_variable_data: List
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class Heartbeat:
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class InstallCertificate:
    certificate_type: str
    certificate: str
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class LogStatusNotification:
    status: str
    request_id: Optional[int] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class MeterValues:
    evse_id: int
    meter_value: List
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class NotifyChargingLimit:
    charging_limit: Dict
    charging_schedule: Optional[List] = None
    evse_id: Optional[int] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class NotifyCustomerInformation:
    data: str
    seq_no: int
    generated_at: str
    request_id: int
    tbc: Optional[bool] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class NotifyDisplayMessages:
    request_id: int
    message_info: Optional[List] = None
    tbc: Optional[bool] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class NotifyEVChargingNeeds:
    charging_needs: Dict
    evse_id: int
    max_schedule_tuples: Optional[int] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class NotifyEVChargingSchedule:
    time_base: str
    charging_schedule: Dict
    evse_id: int
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class NotifyEvent:
    generated_at: str
    seq_no: int
    event_data: List
    tbc: Optional[bool] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class NotifyMonitoringReport:
    request_id: int
    seq_no: int
    generated_at: str
    monitor: Optional[List] = None
    tbc: Optional[bool] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class NotifyReport:
    request_id: int
    generated_at: str
    seq_no: int
    report_data: Optional[List] = None
    tbc: Optional[bool] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class PublishFirmware:
    location: str
    checksum: str
    request_id: int
    retries: Optional[int] = None
    retry_interval: Optional[int] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class PublishFirmwareStatusNotification:
    status: str
    location: Optional[List] = None
    request_id: Optional[int] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class ReportChargingProfiles:
    request_id: int
    charging_limit_source: str
    charging_profile: List
    evse_id: int
    tbc: Optional[bool] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class RequestStartTransaction:
    id_token: Dict
    remote_start_id: int
    evse_id: Optional[int] = None
    group_id_token: Optional[Dict] = None
    charging_profile: Optional[Dict] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class RequestStopTransaction:
    transaction_id: str
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class ReservationStatusUpdate:
    reservation_id: int
    reservation_update_status: str
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class ReserveNow:
    id: int
    expiry_date_time: str
    id_token: Dict
    connector_type: Optional[str] = None
    evse_id: Optional[int] = None
    group_id_token: Optional[Dict] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class Reset:
    type: str
    evse_id: Optional[int] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class SecurityEventNotification:
    type: str
    timestamp: str
    tech_info: Optional[str] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class SendLocalList:
    version_number: int
    update_type: str
    local_authorization_list: Optional[List] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class SetChargingProfile:
    evse_id: int
    charging_profile: Dict
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class SetDisplayMessage:
    message: Dict
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class SetMonitoringBase:
    monitoring_base: str
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class SetMonitoringLevel:
    severity: int
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class SetNetworkProfile:
    configuration_slot: int
    connection_data: Dict
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class SetVariableMonitoring:
    set_monitoring_data: List
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class SetVariables:
    set_variable_data: List
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class SignCertificate:
    csr: str
    certificate_type: Optional[str] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class StatusNotification:
    timestamp: str
    connector_status: str
    evse_id: int
    connector_id: int
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class TransactionEvent:
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
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class TriggerMessage:
    requested_message: str
    evse: Optional[Dict] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class UnlockConnector:
    evse_id: int
    connector_id: int
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class UnpublishFirmware:
    checksum: str
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class UpdateFirmware:
    request_id: int
    firmware: Dict
    retries: Optional[int] = None
    retry_interval: Optional[int] = None
    custom_data: Optional[Dict[str, Any]] = None


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class AuthorizePayload(Authorize):
    def __post_init__(self):
        warnings.warn(
            (
                __class__.__name__
                + " is deprecated, use instead "
                + __class__.__mro__[1].__name__
            )
        )


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class BootNotificationPayload(BootNotification):
    def __post_init__(self):
        warnings.warn(
            (
                __class__.__name__
                + " is deprecated, use instead "
                + __class__.__mro__[1].__name__
            )
        )


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class CancelReservationPayload(CancelReservation):
    def __post_init__(self):
        warnings.warn(
            (
                __class__.__name__
                + " is deprecated, use instead "
                + __class__.__mro__[1].__name__
            )
        )


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class CertificateSignedPayload(CertificateSigned):
    def __post_init__(self):
        warnings.warn(
            (
                __class__.__name__
                + " is deprecated, use instead "
                + __class__.__mro__[1].__name__
            )
        )


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class ChangeAvailabilityPayload(ChangeAvailability):
    def __post_init__(self):
        warnings.warn(
            (
                __class__.__name__
                + " is deprecated, use instead "
                + __class__.__mro__[1].__name__
            )
        )


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class ClearCachePayload(ClearCache):
    def __post_init__(self):
        warnings.warn(
            (
                __class__.__name__
                + " is deprecated, use instead "
                + __class__.__mro__[1].__name__
            )
        )


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class ClearChargingProfilePayload(ClearChargingProfile):
    def __post_init__(self):
        warnings.warn(
            (
                __class__.__name__
                + " is deprecated, use instead "
                + __class__.__mro__[1].__name__
            )
        )


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class ClearDisplayMessagePayload(ClearDisplayMessage):
    def __post_init__(self):
        warnings.warn(
            (
                __class__.__name__
                + " is deprecated, use instead "
                + __class__.__mro__[1].__name__
            )
        )


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class ClearVariableMonitoringPayload(ClearVariableMonitoring):
    def __post_init__(self):
        warnings.warn(
            (
                __class__.__name__
                + " is deprecated, use instead "
                + __class__.__mro__[1].__name__
            )
        )


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class ClearedChargingLimitPayload(ClearedChargingLimit):
    def __post_init__(self):
        warnings.warn(
            (
                __class__.__name__
                + " is deprecated, use instead "
                + __class__.__mro__[1].__name__
            )
        )


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class CostUpdatedPayload(CostUpdated):
    def __post_init__(self):
        warnings.warn(
            (
                __class__.__name__
                + " is deprecated, use instead "
                + __class__.__mro__[1].__name__
            )
        )


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class CustomerInformationPayload(CustomerInformation):
    def __post_init__(self):
        warnings.warn(
            (
                __class__.__name__
                + " is deprecated, use instead "
                + __class__.__mro__[1].__name__
            )
        )


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class DataTransferPayload(DataTransfer):
    def __post_init__(self):
        warnings.warn(
            (
                __class__.__name__
                + " is deprecated, use instead "
                + __class__.__mro__[1].__name__
            )
        )


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class DeleteCertificatePayload(DeleteCertificate):
    def __post_init__(self):
        warnings.warn(
            (
                __class__.__name__
                + " is deprecated, use instead "
                + __class__.__mro__[1].__name__
            )
        )


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class FirmwareStatusNotificationPayload(FirmwareStatusNotification):
    def __post_init__(self):
        warnings.warn(
            (
                __class__.__name__
                + " is deprecated, use instead "
                + __class__.__mro__[1].__name__
            )
        )


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class Get15118EVCertificatePayload(Get15118EVCertificate):
    def __post_init__(self):
        warnings.warn(
            (
                __class__.__name__
                + " is deprecated, use instead "
                + __class__.__mro__[1].__name__
            )
        )


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class GetBaseReportPayload(GetBaseReport):
    def __post_init__(self):
        warnings.warn(
            (
                __class__.__name__
                + " is deprecated, use instead "
                + __class__.__mro__[1].__name__
            )
        )


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class GetCertificateStatusPayload(GetCertificateStatus):
    def __post_init__(self):
        warnings.warn(
            (
                __class__.__name__
                + " is deprecated, use instead "
                + __class__.__mro__[1].__name__
            )
        )


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class GetChargingProfilesPayload(GetChargingProfiles):
    def __post_init__(self):
        warnings.warn(
            (
                __class__.__name__
                + " is deprecated, use instead "
                + __class__.__mro__[1].__name__
            )
        )


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class GetCompositeSchedulePayload(GetCompositeSchedule):
    def __post_init__(self):
        warnings.warn(
            (
                __class__.__name__
                + " is deprecated, use instead "
                + __class__.__mro__[1].__name__
            )
        )


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class GetDisplayMessagesPayload(GetDisplayMessages):
    def __post_init__(self):
        warnings.warn(
            (
                __class__.__name__
                + " is deprecated, use instead "
                + __class__.__mro__[1].__name__
            )
        )


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class GetInstalledCertificateIdsPayload(GetInstalledCertificateIds):
    def __post_init__(self):
        warnings.warn(
            (
                __class__.__name__
                + " is deprecated, use instead "
                + __class__.__mro__[1].__name__
            )
        )


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class GetLocalListVersionPayload(GetLocalListVersion):
    def __post_init__(self):
        warnings.warn(
            (
                __class__.__name__
                + " is deprecated, use instead "
                + __class__.__mro__[1].__name__
            )
        )


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class GetLogPayload(GetLog):
    def __post_init__(self):
        warnings.warn(
            (
                __class__.__name__
                + " is deprecated, use instead "
                + __class__.__mro__[1].__name__
            )
        )


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class GetMonitoringReportPayload(GetMonitoringReport):
    def __post_init__(self):
        warnings.warn(
            (
                __class__.__name__
                + " is deprecated, use instead "
                + __class__.__mro__[1].__name__
            )
        )


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class GetReportPayload(GetReport):
    def __post_init__(self):
        warnings.warn(
            (
                __class__.__name__
                + " is deprecated, use instead "
                + __class__.__mro__[1].__name__
            )
        )


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class GetTransactionStatusPayload(GetTransactionStatus):
    def __post_init__(self):
        warnings.warn(
            (
                __class__.__name__
                + " is deprecated, use instead "
                + __class__.__mro__[1].__name__
            )
        )


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class GetVariablesPayload(GetVariables):
    def __post_init__(self):
        warnings.warn(
            (
                __class__.__name__
                + " is deprecated, use instead "
                + __class__.__mro__[1].__name__
            )
        )


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class HeartbeatPayload(Heartbeat):
    def __post_init__(self):
        warnings.warn(
            (
                __class__.__name__
                + " is deprecated, use instead "
                + __class__.__mro__[1].__name__
            )
        )


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class InstallCertificatePayload(InstallCertificate):
    def __post_init__(self):
        warnings.warn(
            (
                __class__.__name__
                + " is deprecated, use instead "
                + __class__.__mro__[1].__name__
            )
        )


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class LogStatusNotificationPayload(LogStatusNotification):
    def __post_init__(self):
        warnings.warn(
            (
                __class__.__name__
                + " is deprecated, use instead "
                + __class__.__mro__[1].__name__
            )
        )


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class MeterValuesPayload(MeterValues):
    def __post_init__(self):
        warnings.warn(
            (
                __class__.__name__
                + " is deprecated, use instead "
                + __class__.__mro__[1].__name__
            )
        )


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class NotifyChargingLimitPayload(NotifyChargingLimit):
    def __post_init__(self):
        warnings.warn(
            (
                __class__.__name__
                + " is deprecated, use instead "
                + __class__.__mro__[1].__name__
            )
        )


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class NotifyCustomerInformationPayload(NotifyCustomerInformation):
    def __post_init__(self):
        warnings.warn(
            (
                __class__.__name__
                + " is deprecated, use instead "
                + __class__.__mro__[1].__name__
            )
        )


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class NotifyDisplayMessagesPayload(NotifyDisplayMessages):
    def __post_init__(self):
        warnings.warn(
            (
                __class__.__name__
                + " is deprecated, use instead "
                + __class__.__mro__[1].__name__
            )
        )


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class NotifyEVChargingNeedsPayload(NotifyEVChargingNeeds):
    def __post_init__(self):
        warnings.warn(
            (
                __class__.__name__
                + " is deprecated, use instead "
                + __class__.__mro__[1].__name__
            )
        )


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class NotifyEVChargingSchedulePayload(NotifyEVChargingSchedule):
    def __post_init__(self):
        warnings.warn(
            (
                __class__.__name__
                + " is deprecated, use instead "
                + __class__.__mro__[1].__name__
            )
        )


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class NotifyEventPayload(NotifyEvent):
    def __post_init__(self):
        warnings.warn(
            (
                __class__.__name__
                + " is deprecated, use instead "
                + __class__.__mro__[1].__name__
            )
        )


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class NotifyMonitoringReportPayload(NotifyMonitoringReport):
    def __post_init__(self):
        warnings.warn(
            (
                __class__.__name__
                + " is deprecated, use instead "
                + __class__.__mro__[1].__name__
            )
        )


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class NotifyReportPayload(NotifyReport):
    def __post_init__(self):
        warnings.warn(
            (
                __class__.__name__
                + " is deprecated, use instead "
                + __class__.__mro__[1].__name__
            )
        )


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class PublishFirmwarePayload(PublishFirmware):
    def __post_init__(self):
        warnings.warn(
            (
                __class__.__name__
                + " is deprecated, use instead "
                + __class__.__mro__[1].__name__
            )
        )


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class PublishFirmwareStatusNotificationPayload(PublishFirmwareStatusNotification):
    def __post_init__(self):
        warnings.warn(
            (
                __class__.__name__
                + " is deprecated, use instead "
                + __class__.__mro__[1].__name__
            )
        )


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class ReportChargingProfilesPayload(ReportChargingProfiles):
    def __post_init__(self):
        warnings.warn(
            (
                __class__.__name__
                + " is deprecated, use instead "
                + __class__.__mro__[1].__name__
            )
        )


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class RequestStartTransactionPayload(RequestStartTransaction):
    def __post_init__(self):
        warnings.warn(
            (
                __class__.__name__
                + " is deprecated, use instead "
                + __class__.__mro__[1].__name__
            )
        )


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class RequestStopTransactionPayload(RequestStopTransaction):
    def __post_init__(self):
        warnings.warn(
            (
                __class__.__name__
                + " is deprecated, use instead "
                + __class__.__mro__[1].__name__
            )
        )


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class ReservationStatusUpdatePayload(ReservationStatusUpdate):
    def __post_init__(self):
        warnings.warn(
            (
                __class__.__name__
                + " is deprecated, use instead "
                + __class__.__mro__[1].__name__
            )
        )


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class ReserveNowPayload(ReserveNow):
    def __post_init__(self):
        warnings.warn(
            (
                __class__.__name__
                + " is deprecated, use instead "
                + __class__.__mro__[1].__name__
            )
        )


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class ResetPayload(Reset):
    def __post_init__(self):
        warnings.warn(
            (
                __class__.__name__
                + " is deprecated, use instead "
                + __class__.__mro__[1].__name__
            )
        )


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class SecurityEventNotificationPayload(SecurityEventNotification):
    def __post_init__(self):
        warnings.warn(
            (
                __class__.__name__
                + " is deprecated, use instead "
                + __class__.__mro__[1].__name__
            )
        )


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class SendLocalListPayload(SendLocalList):
    def __post_init__(self):
        warnings.warn(
            (
                __class__.__name__
                + " is deprecated, use instead "
                + __class__.__mro__[1].__name__
            )
        )


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class SetChargingProfilePayload(SetChargingProfile):
    def __post_init__(self):
        warnings.warn(
            (
                __class__.__name__
                + " is deprecated, use instead "
                + __class__.__mro__[1].__name__
            )
        )


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class SetDisplayMessagePayload(SetDisplayMessage):
    def __post_init__(self):
        warnings.warn(
            (
                __class__.__name__
                + " is deprecated, use instead "
                + __class__.__mro__[1].__name__
            )
        )


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class SetMonitoringBasePayload(SetMonitoringBase):
    def __post_init__(self):
        warnings.warn(
            (
                __class__.__name__
                + " is deprecated, use instead "
                + __class__.__mro__[1].__name__
            )
        )


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class SetMonitoringLevelPayload(SetMonitoringLevel):
    def __post_init__(self):
        warnings.warn(
            (
                __class__.__name__
                + " is deprecated, use instead "
                + __class__.__mro__[1].__name__
            )
        )


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class SetNetworkProfilePayload(SetNetworkProfile):
    def __post_init__(self):
        warnings.warn(
            (
                __class__.__name__
                + " is deprecated, use instead "
                + __class__.__mro__[1].__name__
            )
        )


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class SetVariableMonitoringPayload(SetVariableMonitoring):
    def __post_init__(self):
        warnings.warn(
            (
                __class__.__name__
                + " is deprecated, use instead "
                + __class__.__mro__[1].__name__
            )
        )


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class SetVariablesPayload(SetVariables):
    def __post_init__(self):
        warnings.warn(
            (
                __class__.__name__
                + " is deprecated, use instead "
                + __class__.__mro__[1].__name__
            )
        )


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class SignCertificatePayload(SignCertificate):
    def __post_init__(self):
        warnings.warn(
            (
                __class__.__name__
                + " is deprecated, use instead "
                + __class__.__mro__[1].__name__
            )
        )


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class StatusNotificationPayload(StatusNotification):
    def __post_init__(self):
        warnings.warn(
            (
                __class__.__name__
                + " is deprecated, use instead "
                + __class__.__mro__[1].__name__
            )
        )


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class TransactionEventPayload(TransactionEvent):
    def __post_init__(self):
        warnings.warn(
            (
                __class__.__name__
                + " is deprecated, use instead "
                + __class__.__mro__[1].__name__
            )
        )


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class TriggerMessagePayload(TriggerMessage):
    def __post_init__(self):
        warnings.warn(
            (
                __class__.__name__
                + " is deprecated, use instead "
                + __class__.__mro__[1].__name__
            )
        )


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class UnlockConnectorPayload(UnlockConnector):
    def __post_init__(self):
        warnings.warn(
            (
                __class__.__name__
                + " is deprecated, use instead "
                + __class__.__mro__[1].__name__
            )
        )


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class UnpublishFirmwarePayload(UnpublishFirmware):
    def __post_init__(self):
        warnings.warn(
            (
                __class__.__name__
                + " is deprecated, use instead "
                + __class__.__mro__[1].__name__
            )
        )


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class UpdateFirmwarePayload(UpdateFirmware):
    def __post_init__(self):
        warnings.warn(
            (
                __class__.__name__
                + " is deprecated, use instead "
                + __class__.__mro__[1].__name__
            )
        )
