from dataclasses import dataclass
from typing import Any, Dict, List, Optional

from ocpp.v201 import enums
from ocpp.v201 import datatypes

@dataclass
class AuthorizePayload:
    id_token: datatypes.IdTokenType
    certificate: Optional[str] = None
    iso15118_certificate_hash_data: Optional[List[datatypes.OCSPRequestDataType]] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class BootNotificationPayload:
    charging_station: datatypes.ChargingStationType
    reason: enums.BootReasonType
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class CancelReservationPayload:
    reservation_id: int
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class CertificateSignedPayload:
    certificate_chain: str
    certificate_type: Optional[enums.CertificateSigningUseType] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class ChangeAvailabilityPayload:
    operational_status: enums.OperationalStatusType
    evse: Optional[datatypes.EVSEType] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class ClearCachePayload:
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class ClearChargingProfilePayload:
    charging_profile_id: Optional[int] = None
    charging_profile_criteria: Optional[datatypes.ClearChargingProfileType] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class ClearDisplayMessagePayload:
    id: int
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class ClearVariableMonitoringPayload:
    id: List[int]
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class ClearedChargingLimitPayload:
    charging_limit_source: enums.ChargingLimitSourceType
    evse_id: Optional[int] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class CostUpdatedPayload:
    total_cost: float
    transaction_id: str
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class CustomerInformationPayload:
    request_id: int
    report: bool
    clear: bool
    customer_certificate: Optional[datatypes.CertificateHashDataType] = None
    id_token: Optional[datatypes.IdTokenType] = None
    customer_identifier: Optional[str] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class DataTransferPayload:
    vendor_id: str
    message_id: Optional[str] = None
    data: Optional[Any] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class DeleteCertificatePayload:
    certificate_hash_data: datatypes.CertificateHashDataType
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class FirmwareStatusNotificationPayload:
    status: enums.FirmwareStatusType
    request_id: Optional[int] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class Get15118EVCertificatePayload:
    iso15118_schema_version: str
    action: enums.CertificateActionType
    exi_request: str
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class GetBaseReportPayload:
    request_id: int
    report_base: enums.ReportBaseType
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class GetCertificateStatusPayload:
    ocsp_request_data: datatypes.OCSPRequestDataType
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class GetChargingProfilesPayload:
    request_id: int
    charging_profile: datatypes.ChargingProfileCriterionType
    evse_id: Optional[int] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class GetCompositeSchedulePayload:
    duration: int
    evse_id: int
    charging_rate_unit: Optional[enums.ChargingRateUnitType] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class GetDisplayMessagesPayload:
    request_id: int
    id: Optional[List[int]] = None
    priority: Optional[enums.MessagePriorityType] = None
    state: Optional[enums.MessageStateType] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class GetInstalledCertificateIdsPayload:
    certificate_type: Optional[List[enums.GetCertificateIdUseType]] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class GetLocalListVersionPayload:
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class GetLogPayload:
    log: datatypes.LogParametersType
    log_type: enums.LogType
    request_id: int
    retries: Optional[int] = None
    retry_interval: Optional[int] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class GetMonitoringReportPayload:
    request_id: int
    component_variable: Optional[List[datatypes.ComponentVariableType]] = None
    monitoring_criteria: Optional[List[enums.MonitoringCriterionType]] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class GetReportPayload:
    request_id: int
    component_variable: Optional[List[datatypes.ComponentVariableType]] = None
    component_criteria: Optional[List[enums.ComponentCriterionType]] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class GetTransactionStatusPayload:
    transaction_id: Optional[str] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class GetVariablesPayload:
    get_variable_data: List[datatypes.GetVariableDataType]
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class HeartbeatPayload:
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class InstallCertificatePayload:
    certificate_type: enums.InstallCertificateUseType
    certificate: str
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class LogStatusNotificationPayload:
    status: enums.UploadLogStatusType
    request_id: Optional[int] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class MeterValuesPayload:
    evse_id: int
    meter_value: List[datatypes.MeterValueType]
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class NotifyChargingLimitPayload:
    charging_limit: datatypes.ChargingLimitType
    charging_schedule: Optional[List[datatypes.ChargingScheduleType]] = None
    evse_id: Optional[int] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class NotifyCustomerInformationPayload:
    data: str
    seq_no: int
    generated_at: str
    request_id: int
    tbc: Optional[bool] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class NotifyDisplayMessagesPayload:
    request_id: int
    message_info: Optional[List[datatypes.MessageInfoType]] = None
    tbc: Optional[bool] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class NotifyEVChargingNeedsPayload:
    charging_needs: datatypes.ChargingNeedsType
    evse_id: int
    max_schedule_tuples: Optional[int] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class NotifyEVChargingSchedulePayload:
    time_base: str
    charging_schedule: datatypes.ChargingScheduleType
    evse_id: int
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class NotifyEventPayload:
    generated_at: str
    seq_no: int
    event_data: List[datatypes.EventDataType]
    tbc: Optional[bool] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class NotifyMonitoringReportPayload:
    request_id: int
    seq_no: int
    generated_at: str
    monitor: Optional[List[datatypes.MonitoringDataType]] = None
    tbc: Optional[bool] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class NotifyReportPayload:
    request_id: int
    generated_at: str
    seq_no: int
    report_data: Optional[List[datatypes.ReportDataType]] = None
    tbc: Optional[bool] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class PublishFirmwarePayload:
    location: str
    checksum: str
    request_id: int
    retries: Optional[int] = None
    retry_interval: Optional[int] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class PublishFirmwareStatusNotificationPayload:
    status: enums.PublishFirmwareStatusType
    location: Optional[List[str]] = None
    request_id: Optional[int] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class ReportChargingProfilesPayload:
    request_id: int
    charging_limit_source: enums.ChargingLimitSourceType
    charging_profile: List[datatypes.ChargingProfileType]
    evse_id: int
    tbc: Optional[bool] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class RequestStartTransactionPayload:
    id_token: datatypes.IdTokenType
    remote_start_id: int
    evse_id: Optional[int] = None
    group_id_token: Optional[datatypes.IdTokenType] = None
    charging_profile: Optional[datatypes.ChargingProfileType] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class RequestStopTransactionPayload:
    transaction_id: str
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class ReservationStatusUpdatePayload:
    reservation_id: int
    reservation_update_status: enums.ReservationUpdateStatusType
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class ReserveNowPayload:
    id: int
    expiry_date_time: str
    id_token: datatypes.IdTokenType
    connector_type: Optional[enums.ConnectorType] = None
    evse_id: Optional[int] = None
    group_id_token: Optional[datatypes.IdTokenType] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class ResetPayload:
    type: enums.ResetType
    evse_id: Optional[int] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class SecurityEventNotificationPayload:
    type: str
    timestamp: str
    tech_info: Optional[str] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class SendLocalListPayload:
    version_number: int
    update_type: enums.UpdateType
    local_authorization_list: Optional[List[datatypes.AuthorizationData]] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class SetChargingProfilePayload:
    evse_id: int
    charging_profile: datatypes.ChargingProfileType
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class SetDisplayMessagePayload:
    message: datatypes.MessageInfoType
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class SetMonitoringBasePayload:
    monitoring_base: enums.MonitorBaseType
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class SetMonitoringLevelPayload:
    severity: int
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class SetNetworkProfilePayload:
    configuration_slot: int
    connection_data: datatypes.NetworkConnectionProfileType
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class SetVariableMonitoringPayload:
    set_monitoring_data: List[datatypes.SetMonitoringDataType]
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class SetVariablesPayload:
    set_variable_data: List[datatypes.SetVariableDataType]
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class SignCertificatePayload:
    csr: str
    certificate_type: Optional[enums.CertificateSigningUseType] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class StatusNotificationPayload:
    timestamp: str
    connector_status: enums.ConnectorStatusType
    evse_id: int
    connector_id: int
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class TransactionEventPayload:
    event_type: enums.TransactionEventType
    timestamp: str
    trigger_reason: enums.TriggerReasonType
    seq_no: int
    transaction_info: datatypes.TransactionType
    meter_value: Optional[List[datatypes.MeterValueType]] = None
    offline: Optional[bool] = None
    number_of_phases_used: Optional[int] = None
    cable_max_current: Optional[int] = None
    reservation_id: Optional[int] = None
    evse: Optional[datatypes.EVSEType] = None
    id_token: Optional[datatypes.IdTokenType] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class TriggerMessagePayload:
    requested_message: enums.MessageTriggerType
    evse: Optional[datatypes.EVSEType] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class UnlockConnectorPayload:
    evse_id: int
    connector_id: int
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class UnpublishFirmwarePayload:
    checksum: str
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class UpdateFirmwarePayload:
    request_id: int
    firmware: datatypes.FirmwareType
    retries: Optional[int] = None
    retry_interval: Optional[int] = None
    custom_data: Optional[Dict[str, Any]] = None
