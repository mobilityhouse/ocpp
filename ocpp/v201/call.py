from typing import Dict, List
from dataclasses import dataclass


@dataclass
class AuthorizeRequestPayload:
    id_token: Dict
    certificate: str = None
    iso15118_certificate_hash_data: List = None


@dataclass
class BootNotificationRequestPayload:
    charging_station: Dict
    reason: str


@dataclass
class CancelReservationRequestPayload:
    reservation_id: int


@dataclass
class CertificateSignedRequestPayload:
    certificate_chain: str
    certificate_type: str = None


@dataclass
class ChangeAvailabilityRequestPayload:
    operational_status: str
    evse: Dict = None


@dataclass
class ClearCacheRequestPayload:
    pass


@dataclass
class ClearChargingProfileRequestPayload:
    charging_profile_id: int = None
    charging_profile_criteria: Dict = None


@dataclass
class ClearDisplayMessageRequestPayload:
    id: int


@dataclass
class ClearVariableMonitoringRequestPayload:
    id: List


@dataclass
class ClearedChargingLimitRequestPayload:
    charging_limit_source: str
    evse_id: int = None


@dataclass
class CostUpdatedRequestPayload:
    total_cost: int
    transaction_id: str


@dataclass
class CustomerInformationRequestPayload:
    request_id: int
    report: bool
    clear: bool
    customer_certificate: Dict = None
    id_token: Dict = None
    customer_identifier: str = None


@dataclass
class DataTransferRequestPayload:
    vendor_id: str
    message_id: str = None
    data: str = None


@dataclass
class DeleteCertificateRequestPayload:
    certificate_hash_data: Dict


@dataclass
class FirmwareStatusNotificationRequestPayload:
    status: str
    request_id: int = None


@dataclass
class Get15118EVCertificateRequestPayload:
    iso15118_schema_version: str
    action: str
    exi_request: str


@dataclass
class GetBaseReportRequestPayload:
    request_id: int
    report_base: str


@dataclass
class GetCertificateStatusRequestPayload:
    ocsp_request_data: Dict


@dataclass
class GetChargingProfilesRequestPayload:
    request_id: int
    charging_profile: Dict
    evse_id: int = None


@dataclass
class GetCompositeScheduleRequestPayload:
    duration: int
    evse_id: int
    charging_rate_unit: str = None


@dataclass
class GetDisplayMessagesRequestPayload:
    request_id: int
    id: List = None
    priority: str = None
    state: str = None


@dataclass
class GetInstalledCertificateIdsRequestPayload:
    certificate_type: List = None


@dataclass
class GetLocalListVersionRequestPayload:
    pass


@dataclass
class GetLogRequestPayload:
    log: Dict
    log_type: str
    request_id: int
    retries: int = None
    retry_interval: int = None


@dataclass
class GetMonitoringReportRequestPayload:
    request_id: int
    component_variable: List = None
    monitoring_criteria: List = None


@dataclass
class GetReportRequestPayload:
    request_id: int
    component_variable: List = None
    component_criteria: List = None


@dataclass
class GetTransactionStatusRequestPayload:
    transaction_id: str = None


@dataclass
class GetVariablesRequestPayload:
    get_variable_data: List


@dataclass
class HeartbeatRequestPayload:
    pass


@dataclass
class InstallCertificateRequestPayload:
    certificate_type: str
    certificate: str


@dataclass
class LogStatusNotificationRequestPayload:
    status: str
    request_id: int = None


@dataclass
class MeterValuesRequestPayload:
    evse_id: int
    meter_value: List


@dataclass
class NotifyChargingLimitRequestPayload:
    charging_limit: Dict
    charging_schedule: List = None
    evse_id: int = None


@dataclass
class NotifyCustomerInformationRequestPayload:
    data: str
    seq_no: int
    generated_at: str
    request_id: int
    tbc: bool = None


@dataclass
class NotifyDisplayMessagesRequestPayload:
    request_id: int
    message_info: List = None
    tbc: bool = None


@dataclass
class NotifyEVChargingNeedsRequestPayload:
    charging_needs: Dict
    evse_id: int
    max_schedule_tuples: int = None


@dataclass
class NotifyEVChargingScheduleRequestPayload:
    time_base: str
    charging_schedule: Dict
    evse_id: int


@dataclass
class NotifyEventRequestPayload:
    generated_at: str
    seq_no: int
    event_data: List
    tbc: bool = None


@dataclass
class NotifyMonitoringReportRequestPayload:
    request_id: int
    seq_no: int
    generated_at: str
    monitor: List = None
    tbc: bool = None


@dataclass
class NotifyReportRequestPayload:
    request_id: int
    generated_at: str
    seq_no: int
    report_data: List = None
    tbc: bool = None


@dataclass
class PublishFirmwareRequestPayload:
    location: str
    checksum: str
    request_id: int
    retries: int = None
    retry_interval: int = None


@dataclass
class PublishFirmwareStatusNotificationRequestPayload:
    status: str
    location: List = None
    request_id: int = None


@dataclass
class ReportChargingProfilesRequestPayload:
    request_id: int
    charging_limit_source: str
    charging_profile: List
    evse_id: int
    tbc: bool = None


@dataclass
class RequestStartTransactionRequestPayload:
    id_token: Dict
    remote_start_id: int
    evse_id: int = None
    group_id_token: Dict = None
    charging_profile: Dict = None


@dataclass
class RequestStopTransactionRequestPayload:
    transaction_id: str


@dataclass
class ReservationStatusUpdateRequestPayload:
    reservation_id: int
    reservation_update_status: str


@dataclass
class ReserveNowRequestPayload:
    id: int
    expiry_date_time: str
    id_token: Dict
    connector_type: str = None
    evse_id: int = None
    group_id_token: Dict = None


@dataclass
class ResetRequestPayload:
    type: str
    evse_id: int = None


@dataclass
class SecurityEventNotificationRequestPayload:
    type: str
    timestamp: str
    tech_info: str = None


@dataclass
class SendLocalListRequestPayload:
    version_number: int
    update_type: str
    local_authorization_list: List = None


@dataclass
class SetChargingProfileRequestPayload:
    evse_id: int
    charging_profile: Dict


@dataclass
class SetDisplayMessageRequestPayload:
    message: Dict


@dataclass
class SetMonitoringBaseRequestPayload:
    monitoring_base: str


@dataclass
class SetMonitoringLevelRequestPayload:
    severity: int


@dataclass
class SetNetworkProfileRequestPayload:
    configuration_slot: int
    connection_data: Dict


@dataclass
class SetVariableMonitoringRequestPayload:
    set_monitoring_data: List


@dataclass
class SetVariablesRequestPayload:
    set_variable_data: List


@dataclass
class SignCertificateRequestPayload:
    csr: str
    certificate_type: str = None


@dataclass
class StatusNotificationRequestPayload:
    timestamp: str
    connector_status: str
    evse_id: int
    connector_id: int


@dataclass
class TransactionEventRequestPayload:
    event_type: str
    timestamp: str
    trigger_reason: str
    seq_no: int
    transaction_info: Dict
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
    evse: Dict = None


@dataclass
class UnlockConnectorRequestPayload:
    evse_id: int
    connector_id: int


@dataclass
class UnpublishFirmwareRequestPayload:
    checksum: str


@dataclass
class UpdateFirmwareRequestPayload:
    request_id: int
    firmware: Dict
    retries: int = None
    retry_interval: int = None
