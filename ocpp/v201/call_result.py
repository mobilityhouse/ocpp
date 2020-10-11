from typing import Any, Dict, List
from dataclasses import dataclass, field

@dataclass
class AuthorizeResponsePayload:
    id_token_info: Dict
    custom_data: Dict = None
    certificate_status: str = None


@dataclass
class BootNotificationResponsePayload:
    current_time: str
    interval: int
    status: str
    custom_data: Dict = None
    status_info: Dict = None


@dataclass
class CancelReservationResponsePayload:
    status: str
    custom_data: Dict = None
    status_info: Dict = None


@dataclass
class CertificateSignedResponsePayload:
    status: str
    custom_data: Dict = None
    status_info: Dict = None


@dataclass
class ChangeAvailabilityResponsePayload:
    status: str
    custom_data: Dict = None
    status_info: Dict = None


@dataclass
class ClearCacheResponsePayload:
    status: str
    custom_data: Dict = None
    status_info: Dict = None


@dataclass
class ClearChargingProfileResponsePayload:
    status: str
    custom_data: Dict = None
    status_info: Dict = None


@dataclass
class ClearDisplayMessageResponsePayload:
    status: str
    custom_data: Dict = None
    status_info: Dict = None


@dataclass
class ClearVariableMonitoringResponsePayload:
    clear_monitoring_result: List
    custom_data: Dict = None


@dataclass
class ClearedChargingLimitResponsePayload:
    custom_data: Dict = None


@dataclass
class CostUpdatedResponsePayload:
    custom_data: Dict = None


@dataclass
class CustomerInformationResponsePayload:
    status: str
    custom_data: Dict = None
    status_info: Dict = None


@dataclass
class DataTransferResponsePayload:
    status: str
    custom_data: Dict = None
    status_info: Dict = None
    data: Dict = None


@dataclass
class DeleteCertificateResponsePayload:
    status: str
    custom_data: Dict = None
    status_info: Dict = None


@dataclass
class FirmwareStatusNotificationResponsePayload:
    custom_data: Dict = None


@dataclass
class Get15118EVCertificateResponsePayload:
    status: str
    exi_response: str
    custom_data: Dict = None
    status_info: Dict = None


@dataclass
class GetBaseReportResponsePayload:
    status: str
    custom_data: Dict = None
    status_info: Dict = None


@dataclass
class GetCertificateStatusResponsePayload:
    status: str
    custom_data: Dict = None
    status_info: Dict = None
    ocsp_result: str = None


@dataclass
class GetChargingProfilesResponsePayload:
    status: str
    custom_data: Dict = None
    status_info: Dict = None


@dataclass
class GetCompositeScheduleResponsePayload:
    status: str
    custom_data: Dict = None
    status_info: Dict = None
    schedule: Dict = None


@dataclass
class GetDisplayMessagesResponsePayload:
    status: str
    custom_data: Dict = None
    status_info: Dict = None


@dataclass
class GetInstalledCertificateIdsResponsePayload:
    status: str
    custom_data: Dict = None
    status_info: Dict = None
    certificate_hash_data_chain: List = None


@dataclass
class GetLocalListVersionResponsePayload:
    version_number: int
    custom_data: Dict = None


@dataclass
class GetLogResponsePayload:
    status: str
    custom_data: Dict = None
    status_info: Dict = None
    filename: str = None


@dataclass
class GetMonitoringReportResponsePayload:
    status: str
    custom_data: Dict = None
    status_info: Dict = None


@dataclass
class GetReportResponsePayload:
    status: str
    custom_data: Dict = None
    status_info: Dict = None


@dataclass
class GetTransactionStatusResponsePayload:
    messages_in_queue: bool
    custom_data: Dict = None
    ongoing_indicator: bool = None


@dataclass
class GetVariablesResponsePayload:
    get_variable_result: List
    custom_data: Dict = None


@dataclass
class HeartbeatResponsePayload:
    current_time: str
    custom_data: Dict = None


@dataclass
class InstallCertificateResponsePayload:
    status: str
    custom_data: Dict = None
    status_info: Dict = None


@dataclass
class LogStatusNotificationResponsePayload:
    custom_data: Dict = None


@dataclass
class MeterValuesResponsePayload:
    custom_data: Dict = None


@dataclass
class NotifyChargingLimitResponsePayload:
    custom_data: Dict = None


@dataclass
class NotifyCustomerInformationResponsePayload:
    custom_data: Dict = None


@dataclass
class NotifyDisplayMessagesResponsePayload:
    custom_data: Dict = None


@dataclass
class NotifyEVChargingNeedsResponsePayload:
    status: str
    custom_data: Dict = None
    status_info: Dict = None


@dataclass
class NotifyEVChargingScheduleResponsePayload:
    status: str
    custom_data: Dict = None
    status_info: Dict = None


@dataclass
class NotifyEventResponsePayload:
    custom_data: Dict = None


@dataclass
class NotifyMonitoringReportResponsePayload:
    custom_data: Dict = None


@dataclass
class NotifyReportResponsePayload:
    custom_data: Dict = None


@dataclass
class PublishFirmwareResponsePayload:
    status: str
    custom_data: Dict = None
    status_info: Dict = None


@dataclass
class PublishFirmwareStatusNotificationResponsePayload:
    custom_data: Dict = None


@dataclass
class ReportChargingProfilesResponsePayload:
    custom_data: Dict = None


@dataclass
class RequestStartTransactionResponsePayload:
    status: str
    custom_data: Dict = None
    status_info: Dict = None
    transaction_id: str = None


@dataclass
class RequestStopTransactionResponsePayload:
    status: str
    custom_data: Dict = None
    status_info: Dict = None


@dataclass
class ReservationStatusUpdateResponsePayload:
    custom_data: Dict = None


@dataclass
class ReserveNowResponsePayload:
    status: str
    custom_data: Dict = None
    status_info: Dict = None


@dataclass
class ResetResponsePayload:
    status: str
    custom_data: Dict = None
    status_info: Dict = None


@dataclass
class SecurityEventNotificationResponsePayload:
    custom_data: Dict = None


@dataclass
class SendLocalListResponsePayload:
    status: str
    custom_data: Dict = None
    status_info: Dict = None


@dataclass
class SetChargingProfileResponsePayload:
    status: str
    custom_data: Dict = None
    status_info: Dict = None


@dataclass
class SetDisplayMessageResponsePayload:
    status: str
    custom_data: Dict = None
    status_info: Dict = None


@dataclass
class SetMonitoringBaseResponsePayload:
    status: str
    custom_data: Dict = None
    status_info: Dict = None


@dataclass
class SetMonitoringLevelResponsePayload:
    status: str
    custom_data: Dict = None
    status_info: Dict = None


@dataclass
class SetNetworkProfileResponsePayload:
    status: str
    custom_data: Dict = None
    status_info: Dict = None


@dataclass
class SetVariableMonitoringResponsePayload:
    set_monitoring_result: List
    custom_data: Dict = None


@dataclass
class SetVariablesResponsePayload:
    set_variable_result: List
    custom_data: Dict = None


@dataclass
class SignCertificateResponsePayload:
    status: str
    custom_data: Dict = None
    status_info: Dict = None


@dataclass
class StatusNotificationResponsePayload:
    custom_data: Dict = None


@dataclass
class TransactionEventResponsePayload:
    custom_data: Dict = None
    total_cost: int = None
    charging_priority: int = None
    id_token_info: Dict = None
    updated_personal_message: Dict = None


@dataclass
class TriggerMessageResponsePayload:
    status: str
    custom_data: Dict = None
    status_info: Dict = None


@dataclass
class UnlockConnectorResponsePayload:
    status: str
    custom_data: Dict = None
    status_info: Dict = None


@dataclass
class UnpublishFirmwareResponsePayload:
    status: str
    custom_data: Dict = None


@dataclass
class UpdateFirmwareResponsePayload:
    status: str
    custom_data: Dict = None
    status_info: Dict = None
