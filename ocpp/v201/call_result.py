import warnings
from dataclasses import dataclass
from typing import Any, Dict, List, Optional

from ocpp.v201 import enums
from ocpp.v201 import datatypes

@dataclass
class Authorize:
    id_token_info: datatypes.IdTokenInfoType
    certificate_status: Optional[enums.AuthorizeCertificateStatusType] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class BootNotification:
    current_time: str
    interval: int
    status: enums.RegistrationStatusType
    status_info: Optional[datatypes.StatusInfoType] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class CancelReservation:
    status: enums.CancelReservationStatusType
    status_info: Optional[datatypes.StatusInfoType] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class CertificateSigned:
    status: enums.CertificateSignedStatusType
    status_info: Optional[datatypes.StatusInfoType] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class ChangeAvailability:
    status: enums.ChangeAvailabilityStatusType
    status_info: Optional[datatypes.StatusInfoType] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class ClearCache:
    status: enums.ClearCacheStatusType
    status_info: Optional[datatypes.StatusInfoType] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class ClearChargingProfile:
    status: enums.ClearChargingProfileStatusType
    status_info: Optional[datatypes.StatusInfoType] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class ClearDisplayMessage:
    status: enums.ClearMessageStatusType
    status_info: Optional[datatypes.StatusInfoType] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class ClearVariableMonitoring:
    clear_monitoring_result: List[enums.ClearMonitoringStatusType]
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class ClearedChargingLimit:
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class CostUpdated:
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class CustomerInformation:
    status: enums.CustomerInformationStatusType
    status_info: Optional[datatypes.StatusInfoType] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class DataTransfer:
    status: enums.DataTransferStatusType
    status_info: Optional[datatypes.StatusInfoType] = None
    data: Optional[Any] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class DeleteCertificate:
    status: enums.DeleteCertificateStatusType
    status_info: Optional[datatypes.StatusInfoType] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class FirmwareStatusNotification:
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class Get15118EVCertificate:
    status: enums.Iso15118EVCertificateStatusType
    exi_response: str
    status_info: Optional[datatypes.StatusInfoType] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class GetBaseReport:
    status: enums.GenericDeviceModelStatusType
    status_info: Optional[datatypes.StatusInfoType] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class GetCertificateStatus:
    status: enums.GetCertificateStatusType
    status_info: Optional[datatypes.StatusInfoType] = None
    ocsp_result: Optional[str] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class GetChargingProfiles:
    status: enums.GetChargingProfileStatusType
    status_info: Optional[datatypes.StatusInfoType] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class GetCompositeSchedule:
    status: enums.GenericStatusType
    status_info: Optional[datatypes.StatusInfoType] = None
    schedule: Optional[datatypes.CompositeScheduleType] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class GetDisplayMessages:
    status: enums.GetDisplayMessagesStatusType
    status_info: Optional[datatypes.StatusInfoType] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class GetInstalledCertificateIds:
    status: enums.GetInstalledCertificateStatusType
    status_info: Optional[datatypes.StatusInfoType] = None
    certificate_hash_data_chain: Optional[List[datatypes.CertificateHashDataChainType]] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class GetLocalListVersion:
    version_number: int
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class GetLog:
    status: enums.LogStatusType
    status_info: Optional[datatypes.StatusInfoType] = None
    filename: Optional[str] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class GetMonitoringReport:
    status: enums.GenericDeviceModelStatusType
    status_info: Optional[datatypes.StatusInfoType] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class GetReport:
    status: enums.GenericDeviceModelStatusType
    status_info: Optional[datatypes.StatusInfoType] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class GetTransactionStatus:
    messages_in_queue: bool
    ongoing_indicator: Optional[bool] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class GetVariables:
    get_variable_result: List[datatypes.GetVariableResultType]
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class Heartbeat:
    current_time: str
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class InstallCertificate:
    status: enums.InstallCertificateStatusType
    status_info: Optional[datatypes.StatusInfoType] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class LogStatusNotification:
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class MeterValues:
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class NotifyChargingLimit:
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class NotifyCustomerInformation:
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class NotifyDisplayMessages:
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class NotifyEVChargingNeeds:
    status: enums.NotifyEVChargingNeedsStatusType
    status_info: Optional[datatypes.StatusInfoType] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class NotifyEVChargingSchedule:
    status: enums.GenericStatusType
    status_info: Optional[datatypes.StatusInfoType] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class NotifyEvent:
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class NotifyMonitoringReport:
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class NotifyReport:
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class PublishFirmware:
    status: enums.PublishFirmwareStatusType
    status_info: Optional[datatypes.StatusInfoType] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class PublishFirmwareStatusNotification:
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class ReportChargingProfiles:
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class RequestStartTransaction:
    status: enums.RequestStartStopStatusType
    status_info: Optional[datatypes.StatusInfoType] = None
    transaction_id: Optional[str] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class RequestStopTransaction:
    status: enums.RequestStartStopStatusType
    status_info: Optional[datatypes.StatusInfoType] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class ReservationStatusUpdate:
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class ReserveNow:
    status: enums.ReserveNowStatusType
    status_info: Optional[datatypes.StatusInfoType] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class Reset:
    status: enums.ResetStatusType
    status_info: Optional[datatypes.StatusInfoType] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class SecurityEventNotification:
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class SendLocalList:
    status: enums.SendLocalListStatusType
    status_info: Optional[datatypes.StatusInfoType] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class SetChargingProfile:
    status: enums.ChargingProfileStatus
    status_info: Optional[datatypes.StatusInfoType] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class SetDisplayMessage:
    status: enums.DisplayMessageStatusType
    status_info: Optional[datatypes.StatusInfoType] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class SetMonitoringBase:
    status: enums.GenericStatusType
    status_info: Optional[datatypes.StatusInfoType] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class SetMonitoringLevel:
    status: enums.GenericStatusType
    status_info: Optional[datatypes.StatusInfoType] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class SetNetworkProfile:
    status: enums.SetNetworkProfileStatusType
    status_info: Optional[datatypes.StatusInfoType] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class SetVariableMonitoring:
    set_monitoring_result: List[datatypes.SetMonitoringResultType]
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class SetVariables:
    set_variable_result: List[datatypes.SetVariableResultType]
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class SignCertificate:
    status: enums.GenericStatusType
    status_info: Optional[datatypes.StatusInfoType] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class StatusNotification:
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class TransactionEvent:
    total_cost: Optional[float] = None
    charging_priority: Optional[int] = None
    id_token_info: Optional[datatypes.IdTokenInfoType] = None
    updated_personal_message: Optional[datatypes.MessageContentType] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class TriggerMessage:
    status: enums.TriggerMessageStatusType
    status_info: Optional[datatypes.StatusInfoType] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class UnlockConnector:
    status: enums.UnlockStatusType
    status_info: Optional[datatypes.StatusInfoType] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class UnpublishFirmware:
    status: enums.UnpublishFirmwareStatusType
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class UpdateFirmware:
    status: enums.FirmwareStatusType
    status_info: Optional[datatypes.StatusInfoType] = None
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
