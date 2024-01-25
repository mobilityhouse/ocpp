from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class Authorize:
    id_token: Dict
    certificate: Optional[str] = None
    iso15118_certificate_hash_data: Optional[List] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class BootNotification:
    charging_station: Dict
    reason: str
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class CancelReservation:
    reservation_id: int
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class CertificateSigned:
    certificate_chain: str
    certificate_type: Optional[str] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class ChangeAvailability:
    operational_status: str
    evse: Optional[Dict] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class ClearCache:
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class ClearChargingProfile:
    charging_profile_id: Optional[int] = None
    charging_profile_criteria: Optional[Dict] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class ClearDisplayMessage:
    id: int
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class ClearVariableMonitoring:
    id: List
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class ClearedChargingLimit:
    charging_limit_source: str
    evse_id: Optional[int] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class CostUpdated:
    total_cost: int
    transaction_id: str
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class CustomerInformation:
    request_id: int
    report: bool
    clear: bool
    customer_certificate: Optional[Dict] = None
    id_token: Optional[Dict] = None
    customer_identifier: Optional[str] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class DataTransfer:
    vendor_id: str
    message_id: Optional[str] = None
    data: Optional[Any] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class DeleteCertificate:
    certificate_hash_data: Dict
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class FirmwareStatusNotification:
    status: str
    request_id: Optional[int] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class Get15118EVCertificate:
    iso15118_schema_version: str
    action: str
    exi_request: str
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class GetBaseReport:
    request_id: int
    report_base: str
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class GetCertificateStatus:
    ocsp_request_data: Dict
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class GetChargingProfiles:
    request_id: int
    charging_profile: Dict
    evse_id: Optional[int] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class GetCompositeSchedule:
    duration: int
    evse_id: int
    charging_rate_unit: Optional[str] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class GetDisplayMessages:
    request_id: int
    id: Optional[List] = None
    priority: Optional[str] = None
    state: Optional[str] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class GetInstalledCertificateIds:
    certificate_type: Optional[List] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class GetLocalListVersion:
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class GetLog:
    log: Dict
    log_type: str
    request_id: int
    retries: Optional[int] = None
    retry_interval: Optional[int] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class GetMonitoringReport:
    request_id: int
    component_variable: Optional[List] = None
    monitoring_criteria: Optional[List] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class GetReport:
    request_id: int
    component_variable: Optional[List] = None
    component_criteria: Optional[List] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class GetTransactionStatus:
    transaction_id: Optional[str] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class GetVariables:
    get_variable_data: List
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class Heartbeat:
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class InstallCertificate:
    certificate_type: str
    certificate: str
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class LogStatusNotification:
    status: str
    request_id: Optional[int] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class MeterValues:
    evse_id: int
    meter_value: List
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class NotifyChargingLimit:
    charging_limit: Dict
    charging_schedule: Optional[List] = None
    evse_id: Optional[int] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class NotifyCustomerInformation:
    data: str
    seq_no: int
    generated_at: str
    request_id: int
    tbc: Optional[bool] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class NotifyDisplayMessages:
    request_id: int
    message_info: Optional[List] = None
    tbc: Optional[bool] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class NotifyEVChargingNeeds:
    charging_needs: Dict
    evse_id: int
    max_schedule_tuples: Optional[int] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class NotifyEVChargingSchedule:
    time_base: str
    charging_schedule: Dict
    evse_id: int
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class NotifyEvent:
    generated_at: str
    seq_no: int
    event_data: List
    tbc: Optional[bool] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class NotifyMonitoringReport:
    request_id: int
    seq_no: int
    generated_at: str
    monitor: Optional[List] = None
    tbc: Optional[bool] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class NotifyReport:
    request_id: int
    generated_at: str
    seq_no: int
    report_data: Optional[List] = None
    tbc: Optional[bool] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class PublishFirmware:
    location: str
    checksum: str
    request_id: int
    retries: Optional[int] = None
    retry_interval: Optional[int] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class PublishFirmwareStatusNotification:
    status: str
    location: Optional[List] = None
    request_id: Optional[int] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class ReportChargingProfiles:
    request_id: int
    charging_limit_source: str
    charging_profile: List
    evse_id: int
    tbc: Optional[bool] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class RequestStartTransaction:
    id_token: Dict
    remote_start_id: int
    evse_id: Optional[int] = None
    group_id_token: Optional[Dict] = None
    charging_profile: Optional[Dict] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class RequestStopTransaction:
    transaction_id: str
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class ReservationStatusUpdate:
    reservation_id: int
    reservation_update_status: str
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class ReserveNow:
    id: int
    expiry_date_time: str
    id_token: Dict
    connector_type: Optional[str] = None
    evse_id: Optional[int] = None
    group_id_token: Optional[Dict] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class Reset:
    type: str
    evse_id: Optional[int] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class SecurityEventNotification:
    type: str
    timestamp: str
    tech_info: Optional[str] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class SendLocalList:
    version_number: int
    update_type: str
    local_authorization_list: Optional[List] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class SetChargingProfile:
    evse_id: int
    charging_profile: Dict
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class SetDisplayMessage:
    message: Dict
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class SetMonitoringBase:
    monitoring_base: str
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class SetMonitoringLevel:
    severity: int
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class SetNetworkProfile:
    configuration_slot: int
    connection_data: Dict
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class SetVariableMonitoring:
    set_monitoring_data: List
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class SetVariables:
    set_variable_data: List
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class SignCertificate:
    csr: str
    certificate_type: Optional[str] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class StatusNotification:
    timestamp: str
    connector_status: str
    evse_id: int
    connector_id: int
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class TransactionEvent:
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
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class TriggerMessage:
    requested_message: str
    evse: Optional[Dict] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class UnlockConnector:
    evse_id: int
    connector_id: int
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class UnpublishFirmware:
    checksum: str
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class UpdateFirmware:
    request_id: int
    firmware: Dict
    retries: Optional[int] = None
    retry_interval: Optional[int] = None
    custom_data: Optional[Dict[str, Any]] = None


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class AuthorizePayload:
    id_token: Dict
    certificate: Optional[str] = None
    iso15118_certificate_hash_data: Optional[List] = None
    custom_data: Optional[Dict[str, Any]] = None


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class BootNotificationPayload:
    charging_station: Dict
    reason: str
    custom_data: Optional[Dict[str, Any]] = None


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class CancelReservationPayload:
    reservation_id: int
    custom_data: Optional[Dict[str, Any]] = None


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class CertificateSignedPayload:
    certificate_chain: str
    certificate_type: Optional[str] = None
    custom_data: Optional[Dict[str, Any]] = None


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class ChangeAvailabilityPayload:
    operational_status: str
    evse: Optional[Dict] = None
    custom_data: Optional[Dict[str, Any]] = None


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class ClearCachePayload:
    custom_data: Optional[Dict[str, Any]] = None


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class ClearChargingProfilePayload:
    charging_profile_id: Optional[int] = None
    charging_profile_criteria: Optional[Dict] = None
    custom_data: Optional[Dict[str, Any]] = None


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class ClearDisplayMessagePayload:
    id: int
    custom_data: Optional[Dict[str, Any]] = None


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class ClearVariableMonitoringPayload:
    id: List
    custom_data: Optional[Dict[str, Any]] = None


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class ClearedChargingLimitPayload:
    charging_limit_source: str
    evse_id: Optional[int] = None
    custom_data: Optional[Dict[str, Any]] = None


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class CostUpdatedPayload:
    total_cost: int
    transaction_id: str
    custom_data: Optional[Dict[str, Any]] = None


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class CustomerInformationPayload:
    request_id: int
    report: bool
    clear: bool
    customer_certificate: Optional[Dict] = None
    id_token: Optional[Dict] = None
    customer_identifier: Optional[str] = None
    custom_data: Optional[Dict[str, Any]] = None


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class DataTransferPayload:
    vendor_id: str
    message_id: Optional[str] = None
    data: Optional[Any] = None
    custom_data: Optional[Dict[str, Any]] = None


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class DeleteCertificatePayload:
    certificate_hash_data: Dict
    custom_data: Optional[Dict[str, Any]] = None


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class FirmwareStatusNotificationPayload:
    status: str
    request_id: Optional[int] = None
    custom_data: Optional[Dict[str, Any]] = None


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class Get15118EVCertificatePayload:
    iso15118_schema_version: str
    action: str
    exi_request: str
    custom_data: Optional[Dict[str, Any]] = None


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class GetBaseReportPayload:
    request_id: int
    report_base: str
    custom_data: Optional[Dict[str, Any]] = None


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class GetCertificateStatusPayload:
    ocsp_request_data: Dict
    custom_data: Optional[Dict[str, Any]] = None


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class GetChargingProfilesPayload:
    request_id: int
    charging_profile: Dict
    evse_id: Optional[int] = None
    custom_data: Optional[Dict[str, Any]] = None


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class GetCompositeSchedulePayload:
    duration: int
    evse_id: int
    charging_rate_unit: Optional[str] = None
    custom_data: Optional[Dict[str, Any]] = None


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class GetDisplayMessagesPayload:
    request_id: int
    id: Optional[List] = None
    priority: Optional[str] = None
    state: Optional[str] = None
    custom_data: Optional[Dict[str, Any]] = None


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class GetInstalledCertificateIdsPayload:
    certificate_type: Optional[List] = None
    custom_data: Optional[Dict[str, Any]] = None


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class GetLocalListVersionPayload:
    custom_data: Optional[Dict[str, Any]] = None


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class GetLogPayload:
    log: Dict
    log_type: str
    request_id: int
    retries: Optional[int] = None
    retry_interval: Optional[int] = None
    custom_data: Optional[Dict[str, Any]] = None


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class GetMonitoringReportPayload:
    request_id: int
    component_variable: Optional[List] = None
    monitoring_criteria: Optional[List] = None
    custom_data: Optional[Dict[str, Any]] = None


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class GetReportPayload:
    request_id: int
    component_variable: Optional[List] = None
    component_criteria: Optional[List] = None
    custom_data: Optional[Dict[str, Any]] = None


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class GetTransactionStatusPayload:
    transaction_id: Optional[str] = None
    custom_data: Optional[Dict[str, Any]] = None


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class GetVariablesPayload:
    get_variable_data: List
    custom_data: Optional[Dict[str, Any]] = None


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class HeartbeatPayload:
    custom_data: Optional[Dict[str, Any]] = None


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class InstallCertificatePayload:
    certificate_type: str
    certificate: str
    custom_data: Optional[Dict[str, Any]] = None


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class LogStatusNotificationPayload:
    status: str
    request_id: Optional[int] = None
    custom_data: Optional[Dict[str, Any]] = None


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class MeterValuesPayload:
    evse_id: int
    meter_value: List
    custom_data: Optional[Dict[str, Any]] = None


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class NotifyChargingLimitPayload:
    charging_limit: Dict
    charging_schedule: Optional[List] = None
    evse_id: Optional[int] = None
    custom_data: Optional[Dict[str, Any]] = None


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class NotifyCustomerInformationPayload:
    data: str
    seq_no: int
    generated_at: str
    request_id: int
    tbc: Optional[bool] = None
    custom_data: Optional[Dict[str, Any]] = None


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class NotifyDisplayMessagesPayload:
    request_id: int
    message_info: Optional[List] = None
    tbc: Optional[bool] = None
    custom_data: Optional[Dict[str, Any]] = None


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class NotifyEVChargingNeedsPayload:
    charging_needs: Dict
    evse_id: int
    max_schedule_tuples: Optional[int] = None
    custom_data: Optional[Dict[str, Any]] = None


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class NotifyEVChargingSchedulePayload:
    time_base: str
    charging_schedule: Dict
    evse_id: int
    custom_data: Optional[Dict[str, Any]] = None


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class NotifyEventPayload:
    generated_at: str
    seq_no: int
    event_data: List
    tbc: Optional[bool] = None
    custom_data: Optional[Dict[str, Any]] = None


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class NotifyMonitoringReportPayload:
    request_id: int
    seq_no: int
    generated_at: str
    monitor: Optional[List] = None
    tbc: Optional[bool] = None
    custom_data: Optional[Dict[str, Any]] = None


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class NotifyReportPayload:
    request_id: int
    generated_at: str
    seq_no: int
    report_data: Optional[List] = None
    tbc: Optional[bool] = None
    custom_data: Optional[Dict[str, Any]] = None


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class PublishFirmwarePayload:
    location: str
    checksum: str
    request_id: int
    retries: Optional[int] = None
    retry_interval: Optional[int] = None
    custom_data: Optional[Dict[str, Any]] = None


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class PublishFirmwareStatusNotificationPayload:
    status: str
    location: Optional[List] = None
    request_id: Optional[int] = None
    custom_data: Optional[Dict[str, Any]] = None


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class ReportChargingProfilesPayload:
    request_id: int
    charging_limit_source: str
    charging_profile: List
    evse_id: int
    tbc: Optional[bool] = None
    custom_data: Optional[Dict[str, Any]] = None


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class RequestStartTransactionPayload:
    id_token: Dict
    remote_start_id: int
    evse_id: Optional[int] = None
    group_id_token: Optional[Dict] = None
    charging_profile: Optional[Dict] = None
    custom_data: Optional[Dict[str, Any]] = None


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class RequestStopTransactionPayload:
    transaction_id: str
    custom_data: Optional[Dict[str, Any]] = None


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class ReservationStatusUpdatePayload:
    reservation_id: int
    reservation_update_status: str
    custom_data: Optional[Dict[str, Any]] = None


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class ReserveNowPayload:
    id: int
    expiry_date_time: str
    id_token: Dict
    connector_type: Optional[str] = None
    evse_id: Optional[int] = None
    group_id_token: Optional[Dict] = None
    custom_data: Optional[Dict[str, Any]] = None


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class ResetPayload:
    type: str
    evse_id: Optional[int] = None
    custom_data: Optional[Dict[str, Any]] = None


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class SecurityEventNotificationPayload:
    type: str
    timestamp: str
    tech_info: Optional[str] = None
    custom_data: Optional[Dict[str, Any]] = None


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class SendLocalListPayload:
    version_number: int
    update_type: str
    local_authorization_list: Optional[List] = None
    custom_data: Optional[Dict[str, Any]] = None


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class SetChargingProfilePayload:
    evse_id: int
    charging_profile: Dict
    custom_data: Optional[Dict[str, Any]] = None


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class SetDisplayMessagePayload:
    message: Dict
    custom_data: Optional[Dict[str, Any]] = None


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class SetMonitoringBasePayload:
    monitoring_base: str
    custom_data: Optional[Dict[str, Any]] = None


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class SetMonitoringLevelPayload:
    severity: int
    custom_data: Optional[Dict[str, Any]] = None


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class SetNetworkProfilePayload:
    configuration_slot: int
    connection_data: Dict
    custom_data: Optional[Dict[str, Any]] = None


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class SetVariableMonitoringPayload:
    set_monitoring_data: List
    custom_data: Optional[Dict[str, Any]] = None


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class SetVariablesPayload:
    set_variable_data: List
    custom_data: Optional[Dict[str, Any]] = None


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class SignCertificatePayload:
    csr: str
    certificate_type: Optional[str] = None
    custom_data: Optional[Dict[str, Any]] = None


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class StatusNotificationPayload:
    timestamp: str
    connector_status: str
    evse_id: int
    connector_id: int
    custom_data: Optional[Dict[str, Any]] = None


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
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
    custom_data: Optional[Dict[str, Any]] = None


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class TriggerMessagePayload:
    requested_message: str
    evse: Optional[Dict] = None
    custom_data: Optional[Dict[str, Any]] = None


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class UnlockConnectorPayload:
    evse_id: int
    connector_id: int
    custom_data: Optional[Dict[str, Any]] = None


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class UnpublishFirmwarePayload:
    checksum: str
    custom_data: Optional[Dict[str, Any]] = None


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class UpdateFirmwarePayload:
    request_id: int
    firmware: Dict
    retries: Optional[int] = None
    retry_interval: Optional[int] = None
    custom_data: Optional[Dict[str, Any]] = None
