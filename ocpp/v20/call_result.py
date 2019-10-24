from dataclasses import dataclass
from typing import Any, Dict, List


@dataclass
class AuthorizeResponsePayload:
    id_token_info: Dict
    certificate_status: str = None
    evse_id: List = None


@dataclass
class BootNotificationResponsePayload:
    current_time: str
    interval: int
    status: str


@dataclass
class CancelReservationResponsePayload:
    status: str


@dataclass
class CertificateSignedResponsePayload:
    status: str


@dataclass
class ChangeAvailabilityResponsePayload:
    status: str


@dataclass
class ClearCacheResponsePayload:
    status: str


@dataclass
class ClearChargingProfileResponsePayload:
    status: str


@dataclass
class ClearDisplayMessageResponsePayload:
    status: str


@dataclass
class ClearVariableMonitoringResponsePayload:
    clear_monitoring_result: List


@dataclass
class ClearedChargingLimitResponsePayload:
    pass


@dataclass
class CostUpdatedResponsePayload:
    pass


@dataclass
class CustomerInformationResponsePayload:
    status: str


@dataclass
class DataTransferResponsePayload:
    status: str
    data: Any = None


@dataclass
class DeleteCertificateResponsePayload:
    status: str


@dataclass
class FirmwareStatusNotificationResponsePayload:
    pass


@dataclass
class Get15118EVCertificateResponsePayload:
    status: str
    sa_provisioning_certificate_chain: Dict
    contract_signature_certificate_chain: Dict
    exi_response: str


@dataclass
class GetBaseReportResponsePayload:
    status: str


@dataclass
class GetCertificateStatusResponsePayload:
    status: str
    ocsp_result: str = None


@dataclass
class GetChargingProfilesResponsePayload:
    status: str


@dataclass
class GetCompositeScheduleResponsePayload:
    status: str
    evse_id: int
    schedule: Dict = None


@dataclass
class GetDisplayMessagesResponsePayload:
    status: str


@dataclass
class GetInstalledCertificateIdsResponsePayload:
    status: str
    certificate_hash_data: List = None


@dataclass
class GetLocalListVersionResponsePayload:
    version_number: int


@dataclass
class GetLogResponsePayload:
    status: str
    filename: str = None


@dataclass
class GetMonitoringReportResponsePayload:
    status: str


@dataclass
class GetReportResponsePayload:
    status: str


@dataclass
class GetTransactionStatusResponsePayload:
    messages_in_queue: bool
    ongoing_indicator: bool = None


@dataclass
class GetVariablesResponsePayload:
    get_variable_result: List


@dataclass
class HeartbeatResponsePayload:
    current_time: str


@dataclass
class InstallCertificateResponsePayload:
    status: str


@dataclass
class LogStatusNotificationResponsePayload:
    pass


@dataclass
class MeterValuesResponsePayload:
    pass


@dataclass
class NotifyCentralChargingNeedsResponsePayload:
    status: str


@dataclass
class NotifyChargingLimitResponsePayload:
    pass


@dataclass
class NotifyCustomerInformationResponsePayload:
    pass


@dataclass
class NotifyDisplayMessagesResponsePayload:
    pass


@dataclass
class NotifyEVChargingNeedsResponsePayload:
    status: str


@dataclass
class NotifyEVChargingScheduleResponsePayload:
    status: str


@dataclass
class NotifyEventResponsePayload:
    pass


@dataclass
class NotifyMonitoringReportResponsePayload:
    pass


@dataclass
class NotifyReportResponsePayload:
    pass


@dataclass
class PublishFirmwareResponsePayload:
    status: str


@dataclass
class PublishFirmwareStatusNotificationResponsePayload:
    pass


@dataclass
class Renegotiate15118ScheduleResponsePayload:
    status: str


@dataclass
class ReportChargingProfilesResponsePayload:
    pass


@dataclass
class RequestStartTransactionResponsePayload:
    status: str
    transaction_id: str = None


@dataclass
class RequestStopTransactionResponsePayload:
    status: str


@dataclass
class ReservationStatusUpdateResponsePayload:
    pass


@dataclass
class ReserveNowResponsePayload:
    status: str


@dataclass
class ResetResponsePayload:
    status: str


@dataclass
class SecurityEventNotificationResponsePayload:
    pass


@dataclass
class SendLocalListResponsePayload:
    status: str


@dataclass
class SetChargingProfileResponsePayload:
    status: str


@dataclass
class SetDisplayMessageResponsePayload:
    status: str


@dataclass
class SetMonitoringBaseResponsePayload:
    status: str


@dataclass
class SetMonitoringLevelResponsePayload:
    status: str


@dataclass
class SetNetworkProfileResponsePayload:
    status: str


@dataclass
class SetVariableMonitoringResponsePayload:
    set_monitoring_result: List


@dataclass
class SetVariablesResponsePayload:
    set_variable_result: List


@dataclass
class SignCertificateResponsePayload:
    status: str


@dataclass
class StatusNotificationResponsePayload:
    pass


@dataclass
class TransactionEventResponsePayload:
    total_cost: int = None
    charging_priority: int = None
    id_token_info: Dict = None
    updated_personal_message: Dict = None


@dataclass
class TriggerMessageResponsePayload:
    status: str


@dataclass
class UnlockConnectorResponsePayload:
    status: str


@dataclass
class UnpublishFirmwareResponsePayload:
    status: str


@dataclass
class Update15118EVCertificateResponsePayload:
    status: str
    exi_response: str = None


@dataclass
class UpdateFirmwareResponsePayload:
    status: str
