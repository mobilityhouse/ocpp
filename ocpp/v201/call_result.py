from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class Authorize:
    id_token_info: Dict
    certificate_status: Optional[str] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class BootNotification:
    current_time: str
    interval: int
    status: str
    status_info: Optional[Dict] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class CancelReservation:
    status: str
    status_info: Optional[Dict] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class CertificateSigned:
    status: str
    status_info: Optional[Dict] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class ChangeAvailability:
    status: str
    status_info: Optional[Dict] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class ClearCache:
    status: str
    status_info: Optional[Dict] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class ClearChargingProfile:
    status: str
    status_info: Optional[Dict] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class ClearDisplayMessage:
    status: str
    status_info: Optional[Dict] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class ClearVariableMonitoring:
    clear_monitoring_result: List
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class ClearedChargingLimit:
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class CostUpdated:
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class CustomerInformation:
    status: str
    status_info: Optional[Dict] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class DataTransfer:
    status: str
    status_info: Optional[Dict] = None
    data: Optional[Any] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class DeleteCertificate:
    status: str
    status_info: Optional[Dict] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class FirmwareStatusNotification:
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class Get15118EVCertificate:
    status: str
    exi_response: str
    status_info: Optional[Dict] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class GetBaseReport:
    status: str
    status_info: Optional[Dict] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class GetCertificateStatus:
    status: str
    status_info: Optional[Dict] = None
    ocsp_result: Optional[str] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class GetChargingProfiles:
    status: str
    status_info: Optional[Dict] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class GetCompositeSchedule:
    status: str
    status_info: Optional[Dict] = None
    schedule: Optional[Dict] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class GetDisplayMessages:
    status: str
    status_info: Optional[Dict] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class GetInstalledCertificateIds:
    status: str
    status_info: Optional[Dict] = None
    certificate_hash_data_chain: Optional[List] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class GetLocalListVersion:
    version_number: int
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class GetLog:
    status: str
    status_info: Optional[Dict] = None
    filename: Optional[str] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class GetMonitoringReport:
    status: str
    status_info: Optional[Dict] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class GetReport:
    status: str
    status_info: Optional[Dict] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class GetTransactionStatus:
    messages_in_queue: bool
    ongoing_indicator: Optional[bool] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class GetVariables:
    get_variable_result: List
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class Heartbeat:
    current_time: str
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class InstallCertificate:
    status: str
    status_info: Optional[Dict] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class LogStatusNotification:
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class MeterValues:
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class NotifyChargingLimit:
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class NotifyCustomerInformation:
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class NotifyDisplayMessages:
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class NotifyEVChargingNeeds:
    status: str
    status_info: Optional[Dict] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class NotifyEVChargingSchedule:
    status: str
    status_info: Optional[Dict] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class NotifyEvent:
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class NotifyMonitoringReport:
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class NotifyReport:
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class PublishFirmware:
    status: str
    status_info: Optional[Dict] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class PublishFirmwareStatusNotification:
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class ReportChargingProfiles:
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class RequestStartTransaction:
    status: str
    status_info: Optional[Dict] = None
    transaction_id: Optional[str] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class RequestStopTransaction:
    status: str
    status_info: Optional[Dict] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class ReservationStatusUpdate:
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class ReserveNow:
    status: str
    status_info: Optional[Dict] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class Reset:
    status: str
    status_info: Optional[Dict] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class SecurityEventNotification:
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class SendLocalList:
    status: str
    status_info: Optional[Dict] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class SetChargingProfile:
    status: str
    status_info: Optional[Dict] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class SetDisplayMessage:
    status: str
    status_info: Optional[Dict] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class SetMonitoringBase:
    status: str
    status_info: Optional[Dict] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class SetMonitoringLevel:
    status: str
    status_info: Optional[Dict] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class SetNetworkProfile:
    status: str
    status_info: Optional[Dict] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class SetVariableMonitoring:
    set_monitoring_result: List
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class SetVariables:
    set_variable_result: List
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class SignCertificate:
    status: str
    status_info: Optional[Dict] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class StatusNotification:
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class TransactionEvent:
    total_cost: Optional[int] = None
    charging_priority: Optional[int] = None
    id_token_info: Optional[Dict] = None
    updated_personal_message: Optional[Dict] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class TriggerMessage:
    status: str
    status_info: Optional[Dict] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class UnlockConnector:
    status: str
    status_info: Optional[Dict] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class UnpublishFirmware:
    status: str
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class UpdateFirmware:
    status: str
    status_info: Optional[Dict] = None
    custom_data: Optional[Dict[str, Any]] = None


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class AuthorizePayload:
    id_token_info: Dict
    certificate_status: Optional[str] = None
    custom_data: Optional[Dict[str, Any]] = None


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class BootNotificationPayload:
    current_time: str
    interval: int
    status: str
    status_info: Optional[Dict] = None
    custom_data: Optional[Dict[str, Any]] = None


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class CancelReservationPayload:
    status: str
    status_info: Optional[Dict] = None
    custom_data: Optional[Dict[str, Any]] = None


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class CertificateSignedPayload:
    status: str
    status_info: Optional[Dict] = None
    custom_data: Optional[Dict[str, Any]] = None


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class ChangeAvailabilityPayload:
    status: str
    status_info: Optional[Dict] = None
    custom_data: Optional[Dict[str, Any]] = None


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class ClearCachePayload:
    status: str
    status_info: Optional[Dict] = None
    custom_data: Optional[Dict[str, Any]] = None


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class ClearChargingProfilePayload:
    status: str
    status_info: Optional[Dict] = None
    custom_data: Optional[Dict[str, Any]] = None


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class ClearDisplayMessagePayload:
    status: str
    status_info: Optional[Dict] = None
    custom_data: Optional[Dict[str, Any]] = None


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class ClearVariableMonitoringPayload:
    clear_monitoring_result: List
    custom_data: Optional[Dict[str, Any]] = None


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class ClearedChargingLimitPayload:
    custom_data: Optional[Dict[str, Any]] = None


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class CostUpdatedPayload:
    custom_data: Optional[Dict[str, Any]] = None


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class CustomerInformationPayload:
    status: str
    status_info: Optional[Dict] = None
    custom_data: Optional[Dict[str, Any]] = None


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class DataTransferPayload:
    status: str
    status_info: Optional[Dict] = None
    data: Optional[Any] = None
    custom_data: Optional[Dict[str, Any]] = None


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class DeleteCertificatePayload:
    status: str
    status_info: Optional[Dict] = None
    custom_data: Optional[Dict[str, Any]] = None


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class FirmwareStatusNotificationPayload:
    custom_data: Optional[Dict[str, Any]] = None


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class Get15118EVCertificatePayload:
    status: str
    exi_response: str
    status_info: Optional[Dict] = None
    custom_data: Optional[Dict[str, Any]] = None


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class GetBaseReportPayload:
    status: str
    status_info: Optional[Dict] = None
    custom_data: Optional[Dict[str, Any]] = None


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class GetCertificateStatusPayload:
    status: str
    status_info: Optional[Dict] = None
    ocsp_result: Optional[str] = None
    custom_data: Optional[Dict[str, Any]] = None


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class GetChargingProfilesPayload:
    status: str
    status_info: Optional[Dict] = None
    custom_data: Optional[Dict[str, Any]] = None


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class GetCompositeSchedulePayload:
    status: str
    status_info: Optional[Dict] = None
    schedule: Optional[Dict] = None
    custom_data: Optional[Dict[str, Any]] = None


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class GetDisplayMessagesPayload:
    status: str
    status_info: Optional[Dict] = None
    custom_data: Optional[Dict[str, Any]] = None


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class GetInstalledCertificateIdsPayload:
    status: str
    status_info: Optional[Dict] = None
    certificate_hash_data_chain: Optional[List] = None
    custom_data: Optional[Dict[str, Any]] = None


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class GetLocalListVersionPayload:
    version_number: int
    custom_data: Optional[Dict[str, Any]] = None


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class GetLogPayload:
    status: str
    status_info: Optional[Dict] = None
    filename: Optional[str] = None
    custom_data: Optional[Dict[str, Any]] = None


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class GetMonitoringReportPayload:
    status: str
    status_info: Optional[Dict] = None
    custom_data: Optional[Dict[str, Any]] = None


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class GetReportPayload:
    status: str
    status_info: Optional[Dict] = None
    custom_data: Optional[Dict[str, Any]] = None


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class GetTransactionStatusPayload:
    messages_in_queue: bool
    ongoing_indicator: Optional[bool] = None
    custom_data: Optional[Dict[str, Any]] = None


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class GetVariablesPayload:
    get_variable_result: List
    custom_data: Optional[Dict[str, Any]] = None


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class HeartbeatPayload:
    current_time: str
    custom_data: Optional[Dict[str, Any]] = None


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class InstallCertificatePayload:
    status: str
    status_info: Optional[Dict] = None
    custom_data: Optional[Dict[str, Any]] = None


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class LogStatusNotificationPayload:
    custom_data: Optional[Dict[str, Any]] = None


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class MeterValuesPayload:
    custom_data: Optional[Dict[str, Any]] = None


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class NotifyChargingLimitPayload:
    custom_data: Optional[Dict[str, Any]] = None


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class NotifyCustomerInformationPayload:
    custom_data: Optional[Dict[str, Any]] = None


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class NotifyDisplayMessagesPayload:
    custom_data: Optional[Dict[str, Any]] = None


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class NotifyEVChargingNeedsPayload:
    status: str
    status_info: Optional[Dict] = None
    custom_data: Optional[Dict[str, Any]] = None


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class NotifyEVChargingSchedulePayload:
    status: str
    status_info: Optional[Dict] = None
    custom_data: Optional[Dict[str, Any]] = None


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class NotifyEventPayload:
    custom_data: Optional[Dict[str, Any]] = None


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class NotifyMonitoringReportPayload:
    custom_data: Optional[Dict[str, Any]] = None


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class NotifyReportPayload:
    custom_data: Optional[Dict[str, Any]] = None


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class PublishFirmwarePayload:
    status: str
    status_info: Optional[Dict] = None
    custom_data: Optional[Dict[str, Any]] = None


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class PublishFirmwareStatusNotificationPayload:
    custom_data: Optional[Dict[str, Any]] = None


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class ReportChargingProfilesPayload:
    custom_data: Optional[Dict[str, Any]] = None


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class RequestStartTransactionPayload:
    status: str
    status_info: Optional[Dict] = None
    transaction_id: Optional[str] = None
    custom_data: Optional[Dict[str, Any]] = None


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class RequestStopTransactionPayload:
    status: str
    status_info: Optional[Dict] = None
    custom_data: Optional[Dict[str, Any]] = None


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class ReservationStatusUpdatePayload:
    custom_data: Optional[Dict[str, Any]] = None


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class ReserveNowPayload:
    status: str
    status_info: Optional[Dict] = None
    custom_data: Optional[Dict[str, Any]] = None


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class ResetPayload:
    status: str
    status_info: Optional[Dict] = None
    custom_data: Optional[Dict[str, Any]] = None


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class SecurityEventNotificationPayload:
    custom_data: Optional[Dict[str, Any]] = None


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class SendLocalListPayload:
    status: str
    status_info: Optional[Dict] = None
    custom_data: Optional[Dict[str, Any]] = None


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class SetChargingProfilePayload:
    status: str
    status_info: Optional[Dict] = None
    custom_data: Optional[Dict[str, Any]] = None


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class SetDisplayMessagePayload:
    status: str
    status_info: Optional[Dict] = None
    custom_data: Optional[Dict[str, Any]] = None


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class SetMonitoringBasePayload:
    status: str
    status_info: Optional[Dict] = None
    custom_data: Optional[Dict[str, Any]] = None


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class SetMonitoringLevelPayload:
    status: str
    status_info: Optional[Dict] = None
    custom_data: Optional[Dict[str, Any]] = None


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class SetNetworkProfilePayload:
    status: str
    status_info: Optional[Dict] = None
    custom_data: Optional[Dict[str, Any]] = None


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class SetVariableMonitoringPayload:
    set_monitoring_result: List
    custom_data: Optional[Dict[str, Any]] = None


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class SetVariablesPayload:
    set_variable_result: List
    custom_data: Optional[Dict[str, Any]] = None


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class SignCertificatePayload:
    status: str
    status_info: Optional[Dict] = None
    custom_data: Optional[Dict[str, Any]] = None


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class StatusNotificationPayload:
    custom_data: Optional[Dict[str, Any]] = None


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class TransactionEventPayload:
    total_cost: Optional[int] = None
    charging_priority: Optional[int] = None
    id_token_info: Optional[Dict] = None
    updated_personal_message: Optional[Dict] = None
    custom_data: Optional[Dict[str, Any]] = None


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class TriggerMessagePayload:
    status: str
    status_info: Optional[Dict] = None
    custom_data: Optional[Dict[str, Any]] = None


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class UnlockConnectorPayload:
    status: str
    status_info: Optional[Dict] = None
    custom_data: Optional[Dict[str, Any]] = None


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class UnpublishFirmwarePayload:
    status: str
    custom_data: Optional[Dict[str, Any]] = None


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class UpdateFirmwarePayload:
    status: str
    status_info: Optional[Dict] = None
    custom_data: Optional[Dict[str, Any]] = None
