from typing import Dict, List, Optional
from dataclasses import dataclass


@dataclass
class AuthorizePayload:
    id_token_info: Dict
    certificate_status: Optional[str] = None


@dataclass
class BootNotificationPayload:
    current_time: str
    interval: int
    status: str
    status_info: Optional[Dict] = None


@dataclass
class CancelReservationPayload:
    status: str
    status_info: Optional[Dict] = None


@dataclass
class CertificateSignedPayload:
    status: str
    status_info: Optional[Dict] = None


@dataclass
class ChangeAvailabilityPayload:
    status: str
    status_info: Optional[Dict] = None


@dataclass
class ClearCachePayload:
    status: str
    status_info: Optional[Dict] = None


@dataclass
class ClearChargingProfilePayload:
    status: str
    status_info: Optional[Dict] = None


@dataclass
class ClearDisplayMessagePayload:
    status: str
    status_info: Optional[Dict] = None


@dataclass
class ClearVariableMonitoringPayload:
    clear_monitoring_result: List


@dataclass
class ClearedChargingLimitPayload:
    pass


@dataclass
class CostUpdatedPayload:
    pass


@dataclass
class CustomerInformationPayload:
    status: str
    status_info: Optional[Dict] = None


@dataclass
class DataTransferPayload:
    status: str
    status_info: Optional[Dict] = None
    data: Optional[Dict] = None


@dataclass
class DeleteCertificatePayload:
    status: str
    status_info: Optional[Dict] = None


@dataclass
class FirmwareStatusNotificationPayload:
    pass


@dataclass
class Get15118EVCertificatePayload:
    status: str
    exi_response: str
    status_info: Optional[Dict] = None


@dataclass
class GetBaseReportPayload:
    status: str
    status_info: Optional[Dict] = None


@dataclass
class GetCertificateStatusPayload:
    status: str
    status_info: Optional[Dict] = None
    ocsp_result: Optional[str] = None


@dataclass
class GetChargingProfilesPayload:
    status: str
    status_info: Optional[Dict] = None


@dataclass
class GetCompositeSchedulePayload:
    status: str
    status_info: Optional[Dict] = None
    schedule: Optional[Dict] = None


@dataclass
class GetDisplayMessagesPayload:
    status: str
    status_info: Optional[Dict] = None


@dataclass
class GetInstalledCertificateIdsPayload:
    status: str
    status_info: Optional[Dict] = None
    certificate_hash_data_chain: Optional[List] = None


@dataclass
class GetLocalListVersionPayload:
    version_number: int


@dataclass
class GetLogPayload:
    status: str
    status_info: Optional[Dict] = None
    filename: Optional[str] = None


@dataclass
class GetMonitoringReportPayload:
    status: str
    status_info: Optional[Dict] = None


@dataclass
class GetReportPayload:
    status: str
    status_info: Optional[Dict] = None


@dataclass
class GetTransactionStatusPayload:
    messages_in_queue: bool
    ongoing_indicator: Optional[bool] = None


@dataclass
class GetVariablesPayload:
    get_variable_result: List


@dataclass
class HeartbeatPayload:
    current_time: str


@dataclass
class InstallCertificatePayload:
    status: str
    status_info: Optional[Dict] = None


@dataclass
class LogStatusNotificationPayload:
    pass


@dataclass
class MeterValuesPayload:
    pass


@dataclass
class NotifyChargingLimitPayload:
    pass


@dataclass
class NotifyCustomerInformationPayload:
    pass


@dataclass
class NotifyDisplayMessagesPayload:
    pass


@dataclass
class NotifyEVChargingNeedsPayload:
    status: str
    status_info: Optional[Dict] = None


@dataclass
class NotifyEVChargingSchedulePayload:
    status: str
    status_info: Optional[Dict] = None


@dataclass
class NotifyEventPayload:
    pass


@dataclass
class NotifyMonitoringReportPayload:
    pass


@dataclass
class NotifyReportPayload:
    pass


@dataclass
class PublishFirmwarePayload:
    status: str
    status_info: Optional[Dict] = None


@dataclass
class PublishFirmwareStatusNotificationPayload:
    pass


@dataclass
class ReportChargingProfilesPayload:
    pass


@dataclass
class RequestStartTransactionPayload:
    status: str
    status_info: Optional[Dict] = None
    transaction_id: Optional[str] = None


@dataclass
class RequestStopTransactionPayload:
    status: str
    status_info: Optional[Dict] = None


@dataclass
class ReservationStatusUpdatePayload:
    pass


@dataclass
class ReserveNowPayload:
    status: str
    status_info: Optional[Dict] = None


@dataclass
class ResetPayload:
    status: str
    status_info: Optional[Dict] = None


@dataclass
class SecurityEventNotificationPayload:
    pass


@dataclass
class SendLocalListPayload:
    status: str
    status_info: Optional[Dict] = None


@dataclass
class SetChargingProfilePayload:
    status: str
    status_info: Optional[Dict] = None


@dataclass
class SetDisplayMessagePayload:
    status: str
    status_info: Optional[Dict] = None


@dataclass
class SetMonitoringBasePayload:
    status: str
    status_info: Optional[Dict] = None


@dataclass
class SetMonitoringLevelPayload:
    status: str
    status_info: Optional[Dict] = None


@dataclass
class SetNetworkProfilePayload:
    status: str
    status_info: Optional[Dict] = None


@dataclass
class SetVariableMonitoringPayload:
    set_monitoring_result: List


@dataclass
class SetVariablesPayload:
    set_variable_result: List


@dataclass
class SignCertificatePayload:
    status: str
    status_info: Optional[Dict] = None


@dataclass
class StatusNotificationPayload:
    pass


@dataclass
class TransactionEventPayload:
    total_cost: Optional[int] = None
    charging_priority: Optional[int] = None
    id_token_info: Optional[Dict] = None
    updated_personal_message: Optional[Dict] = None


@dataclass
class TriggerMessagePayload:
    status: str
    status_info: Optional[Dict] = None


@dataclass
class UnlockConnectorPayload:
    status: str
    status_info: Optional[Dict] = None


@dataclass
class UnpublishFirmwarePayload:
    status: str


@dataclass
class UpdateFirmwarePayload:
    status: str
    status_info: Optional[Dict] = None
