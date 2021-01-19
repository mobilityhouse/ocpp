from typing import Dict, List, Optional
from dataclasses import dataclass


@dataclass
class AuthorizePayload:
    id_token: Dict
    certificate: Optional[str] = None
    iso15118_certificate_hash_data: Optional[List] = None


@dataclass
class BootNotificationPayload:
    charging_station: Dict
    reason: str


@dataclass
class CancelReservationPayload:
    reservation_id: int


@dataclass
class CertificateSignedPayload:
    certificate_chain: str
    certificate_type: Optional[str] = None


@dataclass
class ChangeAvailabilityPayload:
    operational_status: str
    evse: Optional[Dict] = None


@dataclass
class ClearCachePayload:
    pass


@dataclass
class ClearChargingProfilePayload:
    charging_profile_id: Optional[int] = None
    charging_profile_criteria: Optional[Dict] = None


@dataclass
class ClearDisplayMessagePayload:
    id: int


@dataclass
class ClearVariableMonitoringPayload:
    id: List


@dataclass
class ClearedChargingLimitPayload:
    charging_limit_source: str
    evse_id: Optional[int] = None


@dataclass
class CostUpdatedPayload:
    total_cost: int
    transaction_id: str


@dataclass
class CustomerInformationPayload:
    request_id: int
    report: bool
    clear: bool
    customer_certificate: Optional[Dict] = None
    id_token: Optional[Dict] = None
    customer_identifier: Optional[str] = None


@dataclass
class DataTransferPayload:
    vendor_id: str
    message_id: Optional[str] = None
    data: Optional[str] = None


@dataclass
class DeleteCertificatePayload:
    certificate_hash_data: Dict


@dataclass
class FirmwareStatusNotificationPayload:
    status: str
    request_id: Optional[int] = None


@dataclass
class Get15118EVCertificatePayload:
    iso15118_schema_version: str
    action: str
    exi_request: str


@dataclass
class GetBaseReportPayload:
    request_id: int
    report_base: str


@dataclass
class GetCertificateStatusPayload:
    ocsp_request_data: Dict


@dataclass
class GetChargingProfilesPayload:
    request_id: int
    charging_profile: Dict
    evse_id: Optional[int] = None


@dataclass
class GetCompositeSchedulePayload:
    duration: int
    evse_id: int
    charging_rate_unit: Optional[str] = None


@dataclass
class GetDisplayMessagesPayload:
    request_id: int
    id: Optional[List] = None
    priority: Optional[str] = None
    state: Optional[str] = None


@dataclass
class GetInstalledCertificateIdsPayload:
    certificate_type: Optional[List] = None


@dataclass
class GetLocalListVersionPayload:
    pass


@dataclass
class GetLogPayload:
    log: Dict
    log_type: str
    request_id: int
    retries: Optional[int] = None
    retry_interval: Optional[int] = None


@dataclass
class GetMonitoringReportPayload:
    request_id: int
    component_variable: Optional[List] = None
    monitoring_criteria: Optional[List] = None


@dataclass
class GetReportPayload:
    request_id: int
    component_variable: Optional[List] = None
    component_criteria: Optional[List] = None


@dataclass
class GetTransactionStatusPayload:
    transaction_id: Optional[str] = None


@dataclass
class GetVariablesPayload:
    get_variable_data: List


@dataclass
class HeartbeatPayload:
    pass


@dataclass
class InstallCertificatePayload:
    certificate_type: str
    certificate: str


@dataclass
class LogStatusNotificationPayload:
    status: str
    request_id: Optional[int] = None


@dataclass
class MeterValuesPayload:
    evse_id: int
    meter_value: List


@dataclass
class NotifyChargingLimitPayload:
    charging_limit: Dict
    charging_schedule: Optional[List] = None
    evse_id: Optional[int] = None


@dataclass
class NotifyCustomerInformationPayload:
    data: str
    seq_no: int
    generated_at: str
    request_id: int
    tbc: Optional[bool] = None


@dataclass
class NotifyDisplayMessagesPayload:
    request_id: int
    message_info: Optional[List] = None
    tbc: Optional[bool] = None


@dataclass
class NotifyEVChargingNeedsPayload:
    charging_needs: Dict
    evse_id: int
    max_schedule_tuples: Optional[int] = None


@dataclass
class NotifyEVChargingSchedulePayload:
    time_base: str
    charging_schedule: Dict
    evse_id: int


@dataclass
class NotifyEventPayload:
    generated_at: str
    seq_no: int
    event_data: List
    tbc: Optional[bool] = None


@dataclass
class NotifyMonitoringReportPayload:
    request_id: int
    seq_no: int
    generated_at: str
    monitor: Optional[List] = None
    tbc: Optional[bool] = None


@dataclass
class NotifyReportPayload:
    request_id: int
    generated_at: str
    seq_no: int
    report_data: Optional[List] = None
    tbc: Optional[bool] = None


@dataclass
class PublishFirmwarePayload:
    location: str
    checksum: str
    request_id: int
    retries: Optional[int] = None
    retry_interval: Optional[int] = None


@dataclass
class PublishFirmwareStatusNotificationPayload:
    status: str
    location: Optional[List] = None
    request_id: Optional[int] = None


@dataclass
class ReportChargingProfilesPayload:
    request_id: int
    charging_limit_source: str
    charging_profile: List
    evse_id: int
    tbc: Optional[bool] = None


@dataclass
class RequestStartTransactionPayload:
    id_token: Dict
    remote_start_id: int
    evse_id: Optional[int] = None
    group_id_token: Optional[Dict] = None
    charging_profile: Optional[Dict] = None


@dataclass
class RequestStopTransactionPayload:
    transaction_id: str


@dataclass
class ReservationStatusUpdatePayload:
    reservation_id: int
    reservation_update_status: str


@dataclass
class ReserveNowPayload:
    id: int
    expiry_date_time: str
    id_token: Dict
    connector_type: Optional[str] = None
    evse_id: Optional[int] = None
    group_id_token: Optional[Dict] = None


@dataclass
class ResetPayload:
    type: str
    evse_id: Optional[int] = None


@dataclass
class SecurityEventNotificationPayload:
    type: str
    timestamp: str
    tech_info: Optional[str] = None


@dataclass
class SendLocalListPayload:
    version_number: int
    update_type: str
    local_authorization_list: Optional[List] = None


@dataclass
class SetChargingProfilePayload:
    evse_id: int
    charging_profile: Dict


@dataclass
class SetDisplayMessagePayload:
    message: Dict


@dataclass
class SetMonitoringBasePayload:
    monitoring_base: str


@dataclass
class SetMonitoringLevelPayload:
    severity: int


@dataclass
class SetNetworkProfilePayload:
    configuration_slot: int
    connection_data: Dict


@dataclass
class SetVariableMonitoringPayload:
    set_monitoring_data: List


@dataclass
class SetVariablesPayload:
    set_variable_data: List


@dataclass
class SignCertificatePayload:
    csr: str
    certificate_type: Optional[str] = None


@dataclass
class StatusNotificationPayload:
    timestamp: str
    connector_status: str
    evse_id: int
    connector_id: int


@dataclass
class TransactionEventPayload:
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


@dataclass
class TriggerMessagePayload:
    requested_message: str
    evse: Optional[Dict] = None


@dataclass
class UnlockConnectorPayload:
    evse_id: int
    connector_id: int


@dataclass
class UnpublishFirmwarePayload:
    checksum: str


@dataclass
class UpdateFirmwarePayload:
    request_id: int
    firmware: Dict
    retries: Optional[int] = None
    retry_interval: Optional[int] = None
