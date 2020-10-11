from typing import Dict, List
from dataclasses import dataclass


@dataclass
class AuthorizeRequestPayload:
    id_token: Dict
    custom_data: Dict = None
    certificate: str = None
    iso15118_certificate_hash_data: List = None


@dataclass
class BootNotificationRequestPayload:
    charging_station: Dict
    reason: str
    custom_data: Dict = None


@dataclass
class CancelReservationRequestPayload:
    reservation_id: int
    custom_data: Dict = None


@dataclass
class CertificateSignedRequestPayload:
    certificate_chain: str
    custom_data: Dict = None
    certificate_type: str = None


@dataclass
class ChangeAvailabilityRequestPayload:
    operational_status: str
    custom_data: Dict = None
    evse: Dict = None


@dataclass
class ClearCacheRequestPayload:
    custom_data: Dict = None


@dataclass
class ClearChargingProfileRequestPayload:
    custom_data: Dict = None
    charging_profile_id: int = None
    charging_profile_criteria: Dict = None


@dataclass
class ClearDisplayMessageRequestPayload:
    id: int
    custom_data: Dict = None


@dataclass
class ClearVariableMonitoringRequestPayload:
    id: List
    custom_data: Dict = None


@dataclass
class ClearedChargingLimitRequestPayload:
    charging_limit_source: str
    custom_data: Dict = None
    evse_id: int = None


@dataclass
class CostUpdatedRequestPayload:
    total_cost: int
    transaction_id: str
    custom_data: Dict = None


@dataclass
class CustomerInformationRequestPayload:
    request_id: int
    report: bool
    clear: bool
    custom_data: Dict = None
    customer_certificate: Dict = None
    id_token: Dict = None
    customer_identifier: str = None


@dataclass
class DataTransferRequestPayload:
    vendor_id: str
    custom_data: Dict = None
    message_id: str = None
    data: str = None


@dataclass
class DeleteCertificateRequestPayload:
    certificate_hash_data: Dict
    custom_data: Dict = None


@dataclass
class FirmwareStatusNotificationRequestPayload:
    status: str
    custom_data: Dict = None
    request_id: int = None


@dataclass
class Get15118EVCertificateRequestPayload:
    iso15118_schema_version: str
    action: str
    exi_request: str
    custom_data: Dict = None


@dataclass
class GetBaseReportRequestPayload:
    request_id: int
    report_base: str
    custom_data: Dict = None


@dataclass
class GetCertificateStatusRequestPayload:
    ocsp_request_data: Dict
    custom_data: Dict = None


@dataclass
class GetChargingProfilesRequestPayload:
    request_id: int
    charging_profile: Dict
    custom_data: Dict = None
    evse_id: int = None


@dataclass
class GetCompositeScheduleRequestPayload:
    duration: int
    evse_id: int
    custom_data: Dict = None
    charging_rate_unit: str = None


@dataclass
class GetDisplayMessagesRequestPayload:
    request_id: int
    custom_data: Dict = None
    id: List = None
    priority: str = None
    state: str = None


@dataclass
class GetInstalledCertificateIdsRequestPayload:
    custom_data: Dict = None
    certificate_type: List = None


@dataclass
class GetLocalListVersionRequestPayload:
    custom_data: Dict = None


@dataclass
class GetLogRequestPayload:
    log: Dict
    log_type: str
    request_id: int
    custom_data: Dict = None
    retries: int = None
    retry_interval: int = None


@dataclass
class GetMonitoringReportRequestPayload:
    request_id: int
    custom_data: Dict = None
    component_variable: List = None
    monitoring_criteria: List = None


@dataclass
class GetReportRequestPayload:
    request_id: int
    custom_data: Dict = None
    component_variable: List = None
    component_criteria: List = None


@dataclass
class GetTransactionStatusRequestPayload:
    custom_data: Dict = None
    transaction_id: str = None


@dataclass
class GetVariablesRequestPayload:
    get_variable_data: List
    custom_data: Dict = None


@dataclass
class HeartbeatRequestPayload:
    custom_data: Dict = None


@dataclass
class InstallCertificateRequestPayload:
    certificate_type: str
    certificate: str
    custom_data: Dict = None


@dataclass
class LogStatusNotificationRequestPayload:
    status: str
    custom_data: Dict = None
    request_id: int = None


@dataclass
class MeterValuesRequestPayload:
    evse_id: int
    meter_value: List
    custom_data: Dict = None


@dataclass
class NotifyChargingLimitRequestPayload:
    charging_limit: Dict
    custom_data: Dict = None
    charging_schedule: List = None
    evse_id: int = None


@dataclass
class NotifyCustomerInformationRequestPayload:
    data: str
    seq_no: int
    generated_at: str
    request_id: int
    custom_data: Dict = None
    tbc: bool = None


@dataclass
class NotifyDisplayMessagesRequestPayload:
    request_id: int
    custom_data: Dict = None
    message_info: List = None
    tbc: bool = None


@dataclass
class NotifyEVChargingNeedsRequestPayload:
    charging_needs: Dict
    evse_id: int
    custom_data: Dict = None
    max_schedule_tuples: int = None


@dataclass
class NotifyEVChargingScheduleRequestPayload:
    time_base: str
    charging_schedule: Dict
    evse_id: int
    custom_data: Dict = None


@dataclass
class NotifyEventRequestPayload:
    generated_at: str
    seq_no: int
    event_data: List
    custom_data: Dict = None
    tbc: bool = None


@dataclass
class NotifyMonitoringReportRequestPayload:
    request_id: int
    seq_no: int
    generated_at: str
    custom_data: Dict = None
    monitor: List = None
    tbc: bool = None


@dataclass
class NotifyReportRequestPayload:
    request_id: int
    generated_at: str
    seq_no: int
    custom_data: Dict = None
    report_data: List = None
    tbc: bool = None


@dataclass
class PublishFirmwareRequestPayload:
    location: str
    checksum: str
    request_id: int
    custom_data: Dict = None
    retries: int = None
    retry_interval: int = None


@dataclass
class PublishFirmwareStatusNotificationRequestPayload:
    status: str
    custom_data: Dict = None
    location: List = None
    request_id: int = None


@dataclass
class ReportChargingProfilesRequestPayload:
    request_id: int
    charging_limit_source: str
    charging_profile: List
    evse_id: int
    custom_data: Dict = None
    tbc: bool = None


@dataclass
class RequestStartTransactionRequestPayload:
    id_token: Dict
    remote_start_id: int
    custom_data: Dict = None
    evse_id: int = None
    group_id_token: Dict = None
    charging_profile: Dict = None


@dataclass
class RequestStopTransactionRequestPayload:
    transaction_id: str
    custom_data: Dict = None


@dataclass
class ReservationStatusUpdateRequestPayload:
    reservation_id: int
    reservation_update_status: str
    custom_data: Dict = None


@dataclass
class ReserveNowRequestPayload:
    id: int
    expiry_date_time: str
    id_token: Dict
    custom_data: Dict = None
    connector_type: str = None
    evse_id: int = None
    group_id_token: Dict = None


@dataclass
class ResetRequestPayload:
    type: str
    custom_data: Dict = None
    evse_id: int = None


@dataclass
class SecurityEventNotificationRequestPayload:
    type: str
    timestamp: str
    custom_data: Dict = None
    tech_info: str = None


@dataclass
class SendLocalListRequestPayload:
    version_number: int
    update_type: str
    custom_data: Dict = None
    local_authorization_list: List = None


@dataclass
class SetChargingProfileRequestPayload:
    evse_id: int
    charging_profile: Dict
    custom_data: Dict = None


@dataclass
class SetDisplayMessageRequestPayload:
    message: Dict
    custom_data: Dict = None


@dataclass
class SetMonitoringBaseRequestPayload:
    monitoring_base: str
    custom_data: Dict = None


@dataclass
class SetMonitoringLevelRequestPayload:
    severity: int
    custom_data: Dict = None


@dataclass
class SetNetworkProfileRequestPayload:
    configuration_slot: int
    connection_data: Dict
    custom_data: Dict = None


@dataclass
class SetVariableMonitoringRequestPayload:
    set_monitoring_data: List
    custom_data: Dict = None


@dataclass
class SetVariablesRequestPayload:
    set_variable_data: List
    custom_data: Dict = None


@dataclass
class SignCertificateRequestPayload:
    csr: str
    custom_data: Dict = None
    certificate_type: str = None


@dataclass
class StatusNotificationRequestPayload:
    timestamp: str
    connector_status: str
    evse_id: int
    connector_id: int
    custom_data: Dict = None


@dataclass
class TransactionEventRequestPayload:
    event_type: str
    timestamp: str
    trigger_reason: str
    seq_no: int
    transaction_info: Dict
    custom_data: Dict = None
    meter_value: List = None
    offline: bool = None
    number_of_phases_used: int = None
    cable_max_current: int = None
    reservation_id: int = None
    evse: Dict = None
    id_token: Dict = None


@dataclass
class TriggerMessageRequestPayload:
    requested_message: str
    custom_data: Dict = None
    evse: Dict = None


@dataclass
class UnlockConnectorRequestPayload:
    evse_id: int
    connector_id: int
    custom_data: Dict = None


@dataclass
class UnpublishFirmwareRequestPayload:
    checksum: str
    custom_data: Dict = None


@dataclass
class UpdateFirmwareRequestPayload:
    request_id: int
    firmware: Dict
    custom_data: Dict = None
    retries: int = None
    retry_interval: int = None
