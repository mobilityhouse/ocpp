from dataclasses import dataclass
from typing import Any, Dict, List


@dataclass
class AuthorizePayload:
    id_token_info: Dict
    certificate_status: str = None
    evse_id: List = None


@dataclass
class BootNotificationPayload:
    current_time: str
    interval: int
    status: str


@dataclass
class CancelReservationPayload:
    status: str


@dataclass
class CertificateSignedPayload:
    status: str


@dataclass
class ChangeAvailabilityPayload:
    status: str


@dataclass
class ClearCachePayload:
    status: str


@dataclass
class ClearChargingProfilePayload:
    status: str


@dataclass
class ClearDisplayMessagePayload:
    status: str


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


@dataclass
class DataTransferPayload:
    status: str
    data: Any = None


@dataclass
class DeleteCertificatePayload:
    status: str


@dataclass
class FirmwareStatusNotificationPayload:
    pass


@dataclass
class Get15118EVCertificatePayload:
    status: str
    sa_provisioning_certificate_chain: Dict
    contract_signature_certificate_chain: Dict
    exi_response: str


@dataclass
class GetBaseReportPayload:
    status: str


@dataclass
class GetCertificateStatusPayload:
    status: str
    ocsp_result: str = None


@dataclass
class GetChargingProfilesPayload:
    status: str


@dataclass
class GetCompositeSchedulePayload:
    status: str
    evse_id: int
    schedule: Dict = None


@dataclass
class GetDisplayMessagesPayload:
    status: str


@dataclass
class GetInstalledCertificateIdsPayload:
    status: str
    certificate_hash_data: List = None


@dataclass
class GetLocalListVersionPayload:
    version_number: int


@dataclass
class GetLogPayload:
    status: str
    filename: str = None


@dataclass
class GetMonitoringReportPayload:
    status: str


@dataclass
class GetReportPayload:
    status: str


@dataclass
class GetTransactionStatusPayload:
    messages_in_queue: bool
    ongoing_indicator: bool = None


@dataclass
class GetVariablesPayload:
    get_variable_result: List


@dataclass
class HeartbeatPayload:
    current_time: str


@dataclass
class InstallCertificatePayload:
    status: str


@dataclass
class LogStatusNotificationPayload:
    pass


@dataclass
class MeterValuesPayload:
    pass


@dataclass
class NotifyCentralChargingNeedsPayload:
    status: str


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


@dataclass
class NotifyEVChargingSchedulePayload:
    status: str


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


@dataclass
class PublishFirmwareStatusNotificationPayload:
    pass


@dataclass
class Renegotiate15118SchedulePayload:
    status: str


@dataclass
class ReportChargingProfilesPayload:
    pass


@dataclass
class RequestStartTransactionPayload:
    status: str
    transaction_id: str = None


@dataclass
class RequestStopTransactionPayload:
    status: str


@dataclass
class ReservationStatusUpdatePayload:
    pass


@dataclass
class ReserveNowPayload:
    status: str


@dataclass
class ResetPayload:
    status: str


@dataclass
class SecurityEventNotificationPayload:
    pass


@dataclass
class SendLocalListPayload:
    status: str


@dataclass
class SetChargingProfilePayload:
    status: str


@dataclass
class SetDisplayMessagePayload:
    status: str


@dataclass
class SetMonitoringBasePayload:
    status: str


@dataclass
class SetMonitoringLevelPayload:
    status: str


@dataclass
class SetNetworkProfilePayload:
    status: str


@dataclass
class SetVariableMonitoringPayload:
    set_monitoring_result: List


@dataclass
class SetVariablesPayload:
    set_variable_result: List


@dataclass
class SignCertificatePayload:
    status: str


@dataclass
class StatusNotificationPayload:
    pass


@dataclass
class TransactionEventPayload:
    total_cost: int = None
    charging_priority: int = None
    id_token_info: Dict = None
    updated_personal_message: Dict = None


@dataclass
class TriggerMessagePayload:
    status: str


@dataclass
class UnlockConnectorPayload:
    status: str


@dataclass
class UnpublishFirmwarePayload:
    status: str


@dataclass
class Update15118EVCertificatePayload:
    status: str
    exi_response: str = None


@dataclass
class UpdateFirmwarePayload:
    status: str
