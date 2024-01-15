from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class AuthorizePayload:
    id_token_info: Dict
    certificate_status: Optional[str] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class BootNotificationPayload:
    current_time: str
    interval: int
    status: str
    status_info: Optional[Dict] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class CancelReservationPayload:
    status: str
    status_info: Optional[Dict] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class CertificateSignedPayload:
    status: str
    status_info: Optional[Dict] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class ChangeAvailabilityPayload:
    status: str
    status_info: Optional[Dict] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class ClearCachePayload:
    status: str
    status_info: Optional[Dict] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class ClearChargingProfilePayload:
    status: str
    status_info: Optional[Dict] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class ClearDisplayMessagePayload:
    status: str
    status_info: Optional[Dict] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class ClearVariableMonitoringPayload:
    clear_monitoring_result: List
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class ClearedChargingLimitPayload:
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class CostUpdatedPayload:
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class CustomerInformationPayload:
    status: str
    status_info: Optional[Dict] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class DataTransferPayload:
    status: str
    status_info: Optional[Dict] = None
    data: Optional[str] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class DeleteCertificatePayload:
    status: str
    status_info: Optional[Dict] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class FirmwareStatusNotificationPayload:
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class Get15118EVCertificatePayload:
    status: str
    exi_response: str
    status_info: Optional[Dict] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class GetBaseReportPayload:
    status: str
    status_info: Optional[Dict] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class GetCertificateStatusPayload:
    status: str
    status_info: Optional[Dict] = None
    ocsp_result: Optional[str] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class GetChargingProfilesPayload:
    status: str
    status_info: Optional[Dict] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class GetCompositeSchedulePayload:
    status: str
    status_info: Optional[Dict] = None
    schedule: Optional[Dict] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class GetDisplayMessagesPayload:
    status: str
    status_info: Optional[Dict] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class GetInstalledCertificateIdsPayload:
    status: str
    status_info: Optional[Dict] = None
    certificate_hash_data_chain: Optional[List] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class GetLocalListVersionPayload:
    version_number: int
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class GetLogPayload:
    status: str
    status_info: Optional[Dict] = None
    filename: Optional[str] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class GetMonitoringReportPayload:
    status: str
    status_info: Optional[Dict] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class GetReportPayload:
    status: str
    status_info: Optional[Dict] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class GetTransactionStatusPayload:
    messages_in_queue: bool
    ongoing_indicator: Optional[bool] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class GetVariablesPayload:
    get_variable_result: List
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class HeartbeatPayload:
    current_time: str
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class InstallCertificatePayload:
    status: str
    status_info: Optional[Dict] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class LogStatusNotificationPayload:
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class MeterValuesPayload:
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class NotifyChargingLimitPayload:
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class NotifyCustomerInformationPayload:
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class NotifyDisplayMessagesPayload:
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class NotifyEVChargingNeedsPayload:
    status: str
    status_info: Optional[Dict] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class NotifyEVChargingSchedulePayload:
    status: str
    status_info: Optional[Dict] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class NotifyEventPayload:
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class NotifyMonitoringReportPayload:
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class NotifyReportPayload:
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class PublishFirmwarePayload:
    status: str
    status_info: Optional[Dict] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class PublishFirmwareStatusNotificationPayload:
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class ReportChargingProfilesPayload:
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class RequestStartTransactionPayload:
    status: str
    status_info: Optional[Dict] = None
    transaction_id: Optional[str] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class RequestStopTransactionPayload:
    status: str
    status_info: Optional[Dict] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class ReservationStatusUpdatePayload:
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class ReserveNowPayload:
    status: str
    status_info: Optional[Dict] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class ResetPayload:
    status: str
    status_info: Optional[Dict] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class SecurityEventNotificationPayload:
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class SendLocalListPayload:
    status: str
    status_info: Optional[Dict] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class SetChargingProfilePayload:
    status: str
    status_info: Optional[Dict] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class SetDisplayMessagePayload:
    status: str
    status_info: Optional[Dict] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class SetMonitoringBasePayload:
    status: str
    status_info: Optional[Dict] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class SetMonitoringLevelPayload:
    status: str
    status_info: Optional[Dict] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class SetNetworkProfilePayload:
    status: str
    status_info: Optional[Dict] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class SetVariableMonitoringPayload:
    set_monitoring_result: List
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class SetVariablesPayload:
    set_variable_result: List
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class SignCertificatePayload:
    status: str
    status_info: Optional[Dict] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class StatusNotificationPayload:
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class TransactionEventPayload:
    total_cost: Optional[int] = None
    charging_priority: Optional[int] = None
    id_token_info: Optional[Dict] = None
    updated_personal_message: Optional[Dict] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class TriggerMessagePayload:
    status: str
    status_info: Optional[Dict] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class UnlockConnectorPayload:
    status: str
    status_info: Optional[Dict] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class UnpublishFirmwarePayload:
    status: str
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class UpdateFirmwarePayload:
    status: str
    status_info: Optional[Dict] = None
    custom_data: Optional[Dict[str, Any]] = None
