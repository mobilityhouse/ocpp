from typing import Any, Dict, List
from dataclasses import dataclass, field

@dataclass
class AuthorizeResponsePayload:
    id_token_info: Dict
    certificate_status: str = None


@dataclass
class BootNotificationResponsePayload:
    current_time: str
    interval: int
    status: str
    status_info: Dict = None


@dataclass
class CancelReservationResponsePayload:
    status: str
    status_info: Dict = None


@dataclass
class CertificateSignedResponsePayload:
    status: str
    status_info: Dict = None


@dataclass
class ChangeAvailabilityResponsePayload:
    status: str
    status_info: Dict = None


@dataclass
class ClearCacheResponsePayload:
    status: str
    status_info: Dict = None


@dataclass
class ClearChargingProfileResponsePayload:
    status: str
    status_info: Dict = None


@dataclass
class ClearDisplayMessageResponsePayload:
    status: str
    status_info: Dict = None


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
    status_info: Dict = None


@dataclass
class DataTransferResponsePayload:
    status: str
    status_info: Dict = None
    data: Dict = None


@dataclass
class DeleteCertificateResponsePayload:
    status: str
    status_info: Dict = None


@dataclass
class FirmwareStatusNotificationResponsePayload:
    pass

@dataclass
class Get15118EVCertificateResponsePayload:
    status: str
    exi_response: str
    status_info: Dict = None


@dataclass
class GetBaseReportResponsePayload:
    status: str
    status_info: Dict = None


@dataclass
class GetCertificateStatusResponsePayload:
    status: str
    status_info: Dict = None
    ocsp_result: str = None


@dataclass
class GetChargingProfilesResponsePayload:
    status: str
    status_info: Dict = None


@dataclass
class GetCompositeScheduleResponsePayload:
    status: str
    status_info: Dict = None
    schedule: Dict = None


@dataclass
class GetDisplayMessagesResponsePayload:
    status: str
    status_info: Dict = None


@dataclass
class GetInstalledCertificateIdsResponsePayload:
    status: str
    status_info: Dict = None
    certificate_hash_data_chain: List = None


@dataclass
class GetLocalListVersionResponsePayload:
    version_number: int


@dataclass
class GetLogResponsePayload:
    status: str
    status_info: Dict = None
    filename: str = None


@dataclass
class GetMonitoringReportResponsePayload:
    status: str
    status_info: Dict = None


@dataclass
class GetReportResponsePayload:
    status: str
    status_info: Dict = None


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
    status_info: Dict = None


@dataclass
class LogStatusNotificationResponsePayload:
    pass


@dataclass
class MeterValuesResponsePayload:
    pass


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
    status_info: Dict = None


@dataclass
class NotifyEVChargingScheduleResponsePayload:
    status: str
    status_info: Dict = None


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
    status_info: Dict = None


@dataclass
class PublishFirmwareStatusNotificationResponsePayload:
    pass

@dataclass
class ReportChargingProfilesResponsePayload:
    pass


@dataclass
class RequestStartTransactionResponsePayload:
    status: str
    status_info: Dict = None
    transaction_id: str = None


@dataclass
class RequestStopTransactionResponsePayload:
    status: str
    status_info: Dict = None


@dataclass
class ReservationStatusUpdateResponsePayload:
    pass

@dataclass
class ReserveNowResponsePayload:
    status: str
    status_info: Dict = None


@dataclass
class ResetResponsePayload:
    status: str
    status_info: Dict = None


@dataclass
class SecurityEventNotificationResponsePayload:
    pass

@dataclass
class SendLocalListResponsePayload:
    status: str
    status_info: Dict = None


@dataclass
class SetChargingProfileResponsePayload:
    status: str
    status_info: Dict = None


@dataclass
class SetDisplayMessageResponsePayload:
    status: str
    status_info: Dict = None


@dataclass
class SetMonitoringBaseResponsePayload:
    status: str
    status_info: Dict = None


@dataclass
class SetMonitoringLevelResponsePayload:
    status: str
    status_info: Dict = None


@dataclass
class SetNetworkProfileResponsePayload:
    status: str
    status_info: Dict = None


@dataclass
class SetVariableMonitoringResponsePayload:
    set_monitoring_result: List


@dataclass
class SetVariablesResponsePayload:
    set_variable_result: List


@dataclass
class SignCertificateResponsePayload:
    status: str
    status_info: Dict = None


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
    status_info: Dict = None


@dataclass
class UnlockConnectorResponsePayload:
    status: str
    status_info: Dict = None


@dataclass
class UnpublishFirmwareResponsePayload:
    status: str


@dataclass
class UpdateFirmwareResponsePayload:
    status: str
    status_info: Dict = None
