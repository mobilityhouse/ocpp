import warnings
from dataclasses import dataclass
from typing import Any, Dict, List, Optional

from ocpp.v201 import datatypes, enums


@dataclass
class Authorize:
    id_token: datatypes.IdTokenType
    certificate: Optional[str] = None
    iso15118_certificate_hash_data: Optional[List[datatypes.OCSPRequestDataType]] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class BootNotification:
    charging_station: datatypes.ChargingStationType
    reason: enums.BootReasonEnumType
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class CancelReservation:
    reservation_id: int
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class CertificateSigned:
    certificate_chain: str
    certificate_type: Optional[enums.CertificateSigningUseEnumType] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class ChangeAvailability:
    operational_status: enums.OperationalStatusEnumType
    evse: Optional[datatypes.EVSEType] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class ClearCache:
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class ClearChargingProfile:
    charging_profile_id: Optional[int] = None
    charging_profile_criteria: Optional[datatypes.ClearChargingProfileType] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class ClearDisplayMessage:
    id: int
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class ClearVariableMonitoring:
    id: List[int]
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class ClearedChargingLimit:
    charging_limit_source: enums.ChargingLimitSourceEnumType
    evse_id: Optional[int] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class CostUpdated:
    total_cost: float
    transaction_id: str
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class CustomerInformation:
    request_id: int
    report: bool
    clear: bool
    customer_certificate: Optional[datatypes.CertificateHashDataType] = None
    id_token: Optional[datatypes.IdTokenType] = None
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
    certificate_hash_data: datatypes.CertificateHashDataType
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class FirmwareStatusNotification:
    status: enums.FirmwareStatusEnumType
    request_id: Optional[int] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class Get15118EVCertificate:
    iso15118_schema_version: str
    action: enums.CertificateActionEnumType
    exi_request: str
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class GetBaseReport:
    request_id: int
    report_base: enums.ReportBaseEnumType
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class GetCertificateStatus:
    ocsp_request_data: datatypes.OCSPRequestDataType
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class GetChargingProfiles:
    request_id: int
    charging_profile: datatypes.ChargingProfileCriterionType
    evse_id: Optional[int] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class GetCompositeSchedule:
    duration: int
    evse_id: int
    charging_rate_unit: Optional[enums.ChargingRateUnitEnumType] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class GetDisplayMessages:
    request_id: int
    id: Optional[List[int]] = None
    priority: Optional[enums.MessagePriorityEnumType] = None
    state: Optional[enums.MessageStateEnumType] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class GetInstalledCertificateIds:
    certificate_type: Optional[List[enums.GetCertificateIdUseEnumType]] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class GetLocalListVersion:
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class GetLog:
    log: datatypes.LogParametersType
    log_type: enums.LogEnumType
    request_id: int
    retries: Optional[int] = None
    retry_interval: Optional[int] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class GetMonitoringReport:
    request_id: int
    component_variable: Optional[List[datatypes.ComponentVariableType]] = None
    monitoring_criteria: Optional[List[enums.MonitoringCriterionEnumType]] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class GetReport:
    request_id: int
    component_variable: Optional[List[datatypes.ComponentVariableType]] = None
    component_criteria: Optional[List[enums.ComponentCriterionEnumType]] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class GetTransactionStatus:
    transaction_id: Optional[str] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class GetVariables:
    get_variable_data: List[datatypes.GetVariableDataType]
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class Heartbeat:
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class InstallCertificate:
    certificate_type: enums.InstallCertificateUseEnumType
    certificate: str
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class LogStatusNotification:
    status: enums.UploadLogStatusEnumType
    request_id: Optional[int] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class MeterValues:
    evse_id: int
    meter_value: List[datatypes.MeterValueType]
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class NotifyChargingLimit:
    charging_limit: datatypes.ChargingLimitType
    charging_schedule: Optional[List[datatypes.ChargingScheduleType]] = None
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
    message_info: Optional[List[datatypes.MessageInfoType]] = None
    tbc: Optional[bool] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class NotifyEVChargingNeeds:
    charging_needs: datatypes.ChargingNeedsType
    evse_id: int
    max_schedule_tuples: Optional[int] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class NotifyEVChargingSchedule:
    time_base: str
    charging_schedule: datatypes.ChargingScheduleType
    evse_id: int
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class NotifyEvent:
    generated_at: str
    seq_no: int
    event_data: List[datatypes.EventDataType]
    tbc: Optional[bool] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class NotifyMonitoringReport:
    request_id: int
    seq_no: int
    generated_at: str
    monitor: Optional[List[datatypes.MonitoringDataType]] = None
    tbc: Optional[bool] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class NotifyReport:
    request_id: int
    generated_at: str
    seq_no: int
    report_data: Optional[List[datatypes.ReportDataType]] = None
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
    status: enums.PublishFirmwareStatusEnumType
    location: Optional[List[str]] = None
    request_id: Optional[int] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class ReportChargingProfiles:
    request_id: int
    charging_limit_source: enums.ChargingLimitSourceEnumType
    charging_profile: List[datatypes.ChargingProfileType]
    evse_id: int
    tbc: Optional[bool] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class RequestStartTransaction:
    id_token: datatypes.IdTokenType
    remote_start_id: int
    evse_id: Optional[int] = None
    group_id_token: Optional[datatypes.IdTokenType] = None
    charging_profile: Optional[datatypes.ChargingProfileType] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class RequestStopTransaction:
    transaction_id: str
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class ReservationStatusUpdate:
    reservation_id: int
    reservation_update_status: enums.ReservationUpdateStatusEnumType
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class ReserveNow:
    id: int
    expiry_date_time: str
    id_token: datatypes.IdTokenType
    connector_type: Optional[enums.ConnectorEnumType] = None
    evse_id: Optional[int] = None
    group_id_token: Optional[datatypes.IdTokenType] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class Reset:
    type: enums.ResetEnumType
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
    update_type: enums.UpdateEnumType
    local_authorization_list: Optional[List[datatypes.AuthorizationData]] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class SetChargingProfile:
    evse_id: int
    charging_profile: datatypes.ChargingProfileType
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class SetDisplayMessage:
    message: datatypes.MessageInfoType
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class SetMonitoringBase:
    monitoring_base: enums.MonitorBaseEnumType
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class SetMonitoringLevel:
    severity: int
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class SetNetworkProfile:
    configuration_slot: int
    connection_data: datatypes.NetworkConnectionProfileType
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class SetVariableMonitoring:
    set_monitoring_data: List[datatypes.SetMonitoringDataType]
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class SetVariables:
    set_variable_data: List[datatypes.SetVariableDataType]
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class SignCertificate:
    csr: str
    certificate_type: Optional[enums.CertificateSigningUseEnumType] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class StatusNotification:
    timestamp: str
    connector_status: enums.ConnectorStatusEnumType
    evse_id: int
    connector_id: int
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class TransactionEvent:
    event_type: enums.TransactionEventEnumType
    timestamp: str
    trigger_reason: enums.TriggerReasonEnumType
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
class TriggerMessage:
    requested_message: enums.MessageTriggerEnumType
    evse: Optional[datatypes.EVSEType] = None
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
    firmware: datatypes.FirmwareType
    retries: Optional[int] = None
    retry_interval: Optional[int] = None
    custom_data: Optional[Dict[str, Any]] = None


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class AuthorizePayload(Authorize):
    def __post_init__(self):
        warnings.warn(
            (
                __class__.__name__
                + " is deprecated, use instead "
                + __class__.__mro__[1].__name__
            )
        )


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class BootNotificationPayload(BootNotification):
    def __post_init__(self):
        warnings.warn(
            (
                __class__.__name__
                + " is deprecated, use instead "
                + __class__.__mro__[1].__name__
            )
        )


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class CancelReservationPayload(CancelReservation):
    def __post_init__(self):
        warnings.warn(
            (
                __class__.__name__
                + " is deprecated, use instead "
                + __class__.__mro__[1].__name__
            )
        )


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class CertificateSignedPayload(CertificateSigned):
    def __post_init__(self):
        warnings.warn(
            (
                __class__.__name__
                + " is deprecated, use instead "
                + __class__.__mro__[1].__name__
            )
        )


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class ChangeAvailabilityPayload(ChangeAvailability):
    def __post_init__(self):
        warnings.warn(
            (
                __class__.__name__
                + " is deprecated, use instead "
                + __class__.__mro__[1].__name__
            )
        )


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class ClearCachePayload(ClearCache):
    def __post_init__(self):
        warnings.warn(
            (
                __class__.__name__
                + " is deprecated, use instead "
                + __class__.__mro__[1].__name__
            )
        )


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class ClearChargingProfilePayload(ClearChargingProfile):
    def __post_init__(self):
        warnings.warn(
            (
                __class__.__name__
                + " is deprecated, use instead "
                + __class__.__mro__[1].__name__
            )
        )


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class ClearDisplayMessagePayload(ClearDisplayMessage):
    def __post_init__(self):
        warnings.warn(
            (
                __class__.__name__
                + " is deprecated, use instead "
                + __class__.__mro__[1].__name__
            )
        )


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class ClearVariableMonitoringPayload(ClearVariableMonitoring):
    def __post_init__(self):
        warnings.warn(
            (
                __class__.__name__
                + " is deprecated, use instead "
                + __class__.__mro__[1].__name__
            )
        )


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class ClearedChargingLimitPayload(ClearedChargingLimit):
    def __post_init__(self):
        warnings.warn(
            (
                __class__.__name__
                + " is deprecated, use instead "
                + __class__.__mro__[1].__name__
            )
        )


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class CostUpdatedPayload(CostUpdated):
    def __post_init__(self):
        warnings.warn(
            (
                __class__.__name__
                + " is deprecated, use instead "
                + __class__.__mro__[1].__name__
            )
        )


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class CustomerInformationPayload(CustomerInformation):
    def __post_init__(self):
        warnings.warn(
            (
                __class__.__name__
                + " is deprecated, use instead "
                + __class__.__mro__[1].__name__
            )
        )


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class DataTransferPayload(DataTransfer):
    def __post_init__(self):
        warnings.warn(
            (
                __class__.__name__
                + " is deprecated, use instead "
                + __class__.__mro__[1].__name__
            )
        )


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class DeleteCertificatePayload(DeleteCertificate):
    def __post_init__(self):
        warnings.warn(
            (
                __class__.__name__
                + " is deprecated, use instead "
                + __class__.__mro__[1].__name__
            )
        )


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class FirmwareStatusNotificationPayload(FirmwareStatusNotification):
    def __post_init__(self):
        warnings.warn(
            (
                __class__.__name__
                + " is deprecated, use instead "
                + __class__.__mro__[1].__name__
            )
        )


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class Get15118EVCertificatePayload(Get15118EVCertificate):
    def __post_init__(self):
        warnings.warn(
            (
                __class__.__name__
                + " is deprecated, use instead "
                + __class__.__mro__[1].__name__
            )
        )


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class GetBaseReportPayload(GetBaseReport):
    def __post_init__(self):
        warnings.warn(
            (
                __class__.__name__
                + " is deprecated, use instead "
                + __class__.__mro__[1].__name__
            )
        )


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class GetCertificateStatusPayload(GetCertificateStatus):
    def __post_init__(self):
        warnings.warn(
            (
                __class__.__name__
                + " is deprecated, use instead "
                + __class__.__mro__[1].__name__
            )
        )


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class GetChargingProfilesPayload(GetChargingProfiles):
    def __post_init__(self):
        warnings.warn(
            (
                __class__.__name__
                + " is deprecated, use instead "
                + __class__.__mro__[1].__name__
            )
        )


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class GetCompositeSchedulePayload(GetCompositeSchedule):
    def __post_init__(self):
        warnings.warn(
            (
                __class__.__name__
                + " is deprecated, use instead "
                + __class__.__mro__[1].__name__
            )
        )


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class GetDisplayMessagesPayload(GetDisplayMessages):
    def __post_init__(self):
        warnings.warn(
            (
                __class__.__name__
                + " is deprecated, use instead "
                + __class__.__mro__[1].__name__
            )
        )


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class GetInstalledCertificateIdsPayload(GetInstalledCertificateIds):
    def __post_init__(self):
        warnings.warn(
            (
                __class__.__name__
                + " is deprecated, use instead "
                + __class__.__mro__[1].__name__
            )
        )


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class GetLocalListVersionPayload(GetLocalListVersion):
    def __post_init__(self):
        warnings.warn(
            (
                __class__.__name__
                + " is deprecated, use instead "
                + __class__.__mro__[1].__name__
            )
        )


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class GetLogPayload(GetLog):
    def __post_init__(self):
        warnings.warn(
            (
                __class__.__name__
                + " is deprecated, use instead "
                + __class__.__mro__[1].__name__
            )
        )


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class GetMonitoringReportPayload(GetMonitoringReport):
    def __post_init__(self):
        warnings.warn(
            (
                __class__.__name__
                + " is deprecated, use instead "
                + __class__.__mro__[1].__name__
            )
        )


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class GetReportPayload(GetReport):
    def __post_init__(self):
        warnings.warn(
            (
                __class__.__name__
                + " is deprecated, use instead "
                + __class__.__mro__[1].__name__
            )
        )


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class GetTransactionStatusPayload(GetTransactionStatus):
    def __post_init__(self):
        warnings.warn(
            (
                __class__.__name__
                + " is deprecated, use instead "
                + __class__.__mro__[1].__name__
            )
        )


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class GetVariablesPayload(GetVariables):
    def __post_init__(self):
        warnings.warn(
            (
                __class__.__name__
                + " is deprecated, use instead "
                + __class__.__mro__[1].__name__
            )
        )


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class HeartbeatPayload(Heartbeat):
    def __post_init__(self):
        warnings.warn(
            (
                __class__.__name__
                + " is deprecated, use instead "
                + __class__.__mro__[1].__name__
            )
        )


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class InstallCertificatePayload(InstallCertificate):
    def __post_init__(self):
        warnings.warn(
            (
                __class__.__name__
                + " is deprecated, use instead "
                + __class__.__mro__[1].__name__
            )
        )


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class LogStatusNotificationPayload(LogStatusNotification):
    def __post_init__(self):
        warnings.warn(
            (
                __class__.__name__
                + " is deprecated, use instead "
                + __class__.__mro__[1].__name__
            )
        )


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class MeterValuesPayload(MeterValues):
    def __post_init__(self):
        warnings.warn(
            (
                __class__.__name__
                + " is deprecated, use instead "
                + __class__.__mro__[1].__name__
            )
        )


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class NotifyChargingLimitPayload(NotifyChargingLimit):
    def __post_init__(self):
        warnings.warn(
            (
                __class__.__name__
                + " is deprecated, use instead "
                + __class__.__mro__[1].__name__
            )
        )


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class NotifyCustomerInformationPayload(NotifyCustomerInformation):
    def __post_init__(self):
        warnings.warn(
            (
                __class__.__name__
                + " is deprecated, use instead "
                + __class__.__mro__[1].__name__
            )
        )


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class NotifyDisplayMessagesPayload(NotifyDisplayMessages):
    def __post_init__(self):
        warnings.warn(
            (
                __class__.__name__
                + " is deprecated, use instead "
                + __class__.__mro__[1].__name__
            )
        )


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class NotifyEVChargingNeedsPayload(NotifyEVChargingNeeds):
    def __post_init__(self):
        warnings.warn(
            (
                __class__.__name__
                + " is deprecated, use instead "
                + __class__.__mro__[1].__name__
            )
        )


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class NotifyEVChargingSchedulePayload(NotifyEVChargingSchedule):
    def __post_init__(self):
        warnings.warn(
            (
                __class__.__name__
                + " is deprecated, use instead "
                + __class__.__mro__[1].__name__
            )
        )


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class NotifyEventPayload(NotifyEvent):
    def __post_init__(self):
        warnings.warn(
            (
                __class__.__name__
                + " is deprecated, use instead "
                + __class__.__mro__[1].__name__
            )
        )


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class NotifyMonitoringReportPayload(NotifyMonitoringReport):
    def __post_init__(self):
        warnings.warn(
            (
                __class__.__name__
                + " is deprecated, use instead "
                + __class__.__mro__[1].__name__
            )
        )


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class NotifyReportPayload(NotifyReport):
    def __post_init__(self):
        warnings.warn(
            (
                __class__.__name__
                + " is deprecated, use instead "
                + __class__.__mro__[1].__name__
            )
        )


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class PublishFirmwarePayload(PublishFirmware):
    def __post_init__(self):
        warnings.warn(
            (
                __class__.__name__
                + " is deprecated, use instead "
                + __class__.__mro__[1].__name__
            )
        )


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class PublishFirmwareStatusNotificationPayload(PublishFirmwareStatusNotification):
    def __post_init__(self):
        warnings.warn(
            (
                __class__.__name__
                + " is deprecated, use instead "
                + __class__.__mro__[1].__name__
            )
        )


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class ReportChargingProfilesPayload(ReportChargingProfiles):
    def __post_init__(self):
        warnings.warn(
            (
                __class__.__name__
                + " is deprecated, use instead "
                + __class__.__mro__[1].__name__
            )
        )


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class RequestStartTransactionPayload(RequestStartTransaction):
    def __post_init__(self):
        warnings.warn(
            (
                __class__.__name__
                + " is deprecated, use instead "
                + __class__.__mro__[1].__name__
            )
        )


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class RequestStopTransactionPayload(RequestStopTransaction):
    def __post_init__(self):
        warnings.warn(
            (
                __class__.__name__
                + " is deprecated, use instead "
                + __class__.__mro__[1].__name__
            )
        )


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class ReservationStatusUpdatePayload(ReservationStatusUpdate):
    def __post_init__(self):
        warnings.warn(
            (
                __class__.__name__
                + " is deprecated, use instead "
                + __class__.__mro__[1].__name__
            )
        )


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class ReserveNowPayload(ReserveNow):
    def __post_init__(self):
        warnings.warn(
            (
                __class__.__name__
                + " is deprecated, use instead "
                + __class__.__mro__[1].__name__
            )
        )


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class ResetPayload(Reset):
    def __post_init__(self):
        warnings.warn(
            (
                __class__.__name__
                + " is deprecated, use instead "
                + __class__.__mro__[1].__name__
            )
        )


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class SecurityEventNotificationPayload(SecurityEventNotification):
    def __post_init__(self):
        warnings.warn(
            (
                __class__.__name__
                + " is deprecated, use instead "
                + __class__.__mro__[1].__name__
            )
        )


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class SendLocalListPayload(SendLocalList):
    def __post_init__(self):
        warnings.warn(
            (
                __class__.__name__
                + " is deprecated, use instead "
                + __class__.__mro__[1].__name__
            )
        )


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class SetChargingProfilePayload(SetChargingProfile):
    def __post_init__(self):
        warnings.warn(
            (
                __class__.__name__
                + " is deprecated, use instead "
                + __class__.__mro__[1].__name__
            )
        )


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class SetDisplayMessagePayload(SetDisplayMessage):
    def __post_init__(self):
        warnings.warn(
            (
                __class__.__name__
                + " is deprecated, use instead "
                + __class__.__mro__[1].__name__
            )
        )


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class SetMonitoringBasePayload(SetMonitoringBase):
    def __post_init__(self):
        warnings.warn(
            (
                __class__.__name__
                + " is deprecated, use instead "
                + __class__.__mro__[1].__name__
            )
        )


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class SetMonitoringLevelPayload(SetMonitoringLevel):
    def __post_init__(self):
        warnings.warn(
            (
                __class__.__name__
                + " is deprecated, use instead "
                + __class__.__mro__[1].__name__
            )
        )


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class SetNetworkProfilePayload(SetNetworkProfile):
    def __post_init__(self):
        warnings.warn(
            (
                __class__.__name__
                + " is deprecated, use instead "
                + __class__.__mro__[1].__name__
            )
        )


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class SetVariableMonitoringPayload(SetVariableMonitoring):
    def __post_init__(self):
        warnings.warn(
            (
                __class__.__name__
                + " is deprecated, use instead "
                + __class__.__mro__[1].__name__
            )
        )


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class SetVariablesPayload(SetVariables):
    def __post_init__(self):
        warnings.warn(
            (
                __class__.__name__
                + " is deprecated, use instead "
                + __class__.__mro__[1].__name__
            )
        )


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class SignCertificatePayload(SignCertificate):
    def __post_init__(self):
        warnings.warn(
            (
                __class__.__name__
                + " is deprecated, use instead "
                + __class__.__mro__[1].__name__
            )
        )


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class StatusNotificationPayload(StatusNotification):
    def __post_init__(self):
        warnings.warn(
            (
                __class__.__name__
                + " is deprecated, use instead "
                + __class__.__mro__[1].__name__
            )
        )


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class TransactionEventPayload(TransactionEvent):
    def __post_init__(self):
        warnings.warn(
            (
                __class__.__name__
                + " is deprecated, use instead "
                + __class__.__mro__[1].__name__
            )
        )


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class TriggerMessagePayload(TriggerMessage):
    def __post_init__(self):
        warnings.warn(
            (
                __class__.__name__
                + " is deprecated, use instead "
                + __class__.__mro__[1].__name__
            )
        )


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class UnlockConnectorPayload(UnlockConnector):
    def __post_init__(self):
        warnings.warn(
            (
                __class__.__name__
                + " is deprecated, use instead "
                + __class__.__mro__[1].__name__
            )
        )


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class UnpublishFirmwarePayload(UnpublishFirmware):
    def __post_init__(self):
        warnings.warn(
            (
                __class__.__name__
                + " is deprecated, use instead "
                + __class__.__mro__[1].__name__
            )
        )


# Dataclass soon to be deprecated use equal class name without the suffix 'Payload'
@dataclass
class UpdateFirmwarePayload(UpdateFirmware):
    def __post_init__(self):
        warnings.warn(
            (
                __class__.__name__
                + " is deprecated, use instead "
                + __class__.__mro__[1].__name__
            )
        )
