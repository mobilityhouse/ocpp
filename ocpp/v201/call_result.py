from dataclasses import dataclass
from typing import Any, Dict, List, Optional

from ocpp.v201 import enums
from ocpp.v201 import datatypes

@dataclass
class AuthorizePayload:
    id_token_info: datatypes.IdTokenInfoType
    certificate_status: Optional[enums.AuthorizeCertificateStatusType] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class BootNotificationPayload:
    current_time: str
    interval: int
    status: enums.RegistrationStatusType
    status_info: Optional[datatypes.StatusInfoType] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class CancelReservationPayload:
    status: enums.CancelReservationStatusType
    status_info: Optional[datatypes.StatusInfoType] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class CertificateSignedPayload:
    status: enums.CertificateSignedStatusType
    status_info: Optional[datatypes.StatusInfoType] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class ChangeAvailabilityPayload:
    status: enums.ChangeAvailabilityStatusType
    status_info: Optional[datatypes.StatusInfoType] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class ClearCachePayload:
    status: enums.ClearCacheStatusType
    status_info: Optional[datatypes.StatusInfoType] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class ClearChargingProfilePayload:
    status: enums.ClearChargingProfileStatusType
    status_info: Optional[datatypes.StatusInfoType] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class ClearDisplayMessagePayload:
    status: enums.ClearMessageStatusType
    status_info: Optional[datatypes.StatusInfoType] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class ClearVariableMonitoringPayload:
    clear_monitoring_result: List[enums.ClearMonitoringStatusType]
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class ClearedChargingLimitPayload:
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class CostUpdatedPayload:
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class CustomerInformationPayload:
    status: enums.CustomerInformationStatusType
    status_info: Optional[datatypes.StatusInfoType] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class DataTransferPayload:
    status: enums.DataTransferStatusType
    status_info: Optional[datatypes.StatusInfoType] = None
    data: Optional[Any] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class DeleteCertificatePayload:
    status: enums.DeleteCertificateStatusType
    status_info: Optional[datatypes.StatusInfoType] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class FirmwareStatusNotificationPayload:
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class Get15118EVCertificatePayload:
    status: enums.Iso15118EVCertificateStatusType
    exi_response: str
    status_info: Optional[datatypes.StatusInfoType] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class GetBaseReportPayload:
    status: enums.GenericDeviceModelStatusType
    status_info: Optional[datatypes.StatusInfoType] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class GetCertificateStatusPayload:
    status: enums.GetCertificateStatusType
    status_info: Optional[datatypes.StatusInfoType] = None
    ocsp_result: Optional[str] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class GetChargingProfilesPayload:
    status: enums.GetChargingProfileStatusType
    status_info: Optional[datatypes.StatusInfoType] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class GetCompositeSchedulePayload:
    status: enums.GenericStatusType
    status_info: Optional[datatypes.StatusInfoType] = None
    schedule: Optional[datatypes.CompositeScheduleType] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class GetDisplayMessagesPayload:
    status: enums.GetDisplayMessagesStatusType
    status_info: Optional[datatypes.StatusInfoType] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class GetInstalledCertificateIdsPayload:
    status: enums.GetInstalledCertificateStatusType
    status_info: Optional[datatypes.StatusInfoType] = None
    certificate_hash_data_chain: Optional[List[datatypes.CertificateHashDataChainType]] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class GetLocalListVersionPayload:
    version_number: int
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class GetLogPayload:
    status: enums.LogStatusType
    status_info: Optional[datatypes.StatusInfoType] = None
    filename: Optional[str] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class GetMonitoringReportPayload:
    status: enums.GenericDeviceModelStatusType
    status_info: Optional[datatypes.StatusInfoType] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class GetReportPayload:
    status: enums.GenericDeviceModelStatusType
    status_info: Optional[datatypes.StatusInfoType] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class GetTransactionStatusPayload:
    messages_in_queue: bool
    ongoing_indicator: Optional[bool] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class GetVariablesPayload:
    get_variable_result: List[datatypes.GetVariableResultType]
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class HeartbeatPayload:
    current_time: str
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class InstallCertificatePayload:
    status: enums.InstallCertificateStatusType
    status_info: Optional[datatypes.StatusInfoType] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class LogStatusNotificationPayload:
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class MeterValuesPayload:
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class NotifyChargingLimitPayload:
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class NotifyCustomerInformationPayload:
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class NotifyDisplayMessagesPayload:
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class NotifyEVChargingNeedsPayload:
    status: enums.NotifyEVChargingNeedsStatusType
    status_info: Optional[datatypes.StatusInfoType] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class NotifyEVChargingSchedulePayload:
    status: enums.GenericStatusType
    status_info: Optional[datatypes.StatusInfoType] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class NotifyEventPayload:
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class NotifyMonitoringReportPayload:
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class NotifyReportPayload:
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class PublishFirmwarePayload:
    status: enums.PublishFirmwareStatusType
    status_info: Optional[datatypes.StatusInfoType] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class PublishFirmwareStatusNotificationPayload:
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class ReportChargingProfilesPayload:
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class RequestStartTransactionPayload:
    status: enums.RequestStartStopStatusType
    status_info: Optional[datatypes.StatusInfoType] = None
    transaction_id: Optional[str] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class RequestStopTransactionPayload:
    status: enums.RequestStartStopStatusType
    status_info: Optional[datatypes.StatusInfoType] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class ReservationStatusUpdatePayload:
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class ReserveNowPayload:
    status: enums.ReserveNowStatusType
    status_info: Optional[datatypes.StatusInfoType] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class ResetPayload:
    status: enums.ResetStatusType
    status_info: Optional[datatypes.StatusInfoType] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class SecurityEventNotificationPayload:
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class SendLocalListPayload:
    status: enums.SendLocalListStatusType
    status_info: Optional[datatypes.StatusInfoType] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class SetChargingProfilePayload:
    status: enums.ChargingProfileStatus
    status_info: Optional[datatypes.StatusInfoType] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class SetDisplayMessagePayload:
    status: enums.DisplayMessageStatusType
    status_info: Optional[datatypes.StatusInfoType] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class SetMonitoringBasePayload:
    status: enums.GenericStatusType
    status_info: Optional[datatypes.StatusInfoType] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class SetMonitoringLevelPayload:
    status: enums.GenericStatusType
    status_info: Optional[datatypes.StatusInfoType] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class SetNetworkProfilePayload:
    status: enums.SetNetworkProfileStatusType
    status_info: Optional[datatypes.StatusInfoType] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class SetVariableMonitoringPayload:
    set_monitoring_result: List[datatypes.SetMonitoringResultType]
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class SetVariablesPayload:
    set_variable_result: List[datatypes.SetVariableResultType]
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class SignCertificatePayload:
    status: enums.GenericStatusType
    status_info: Optional[datatypes.StatusInfoType] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class StatusNotificationPayload:
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class TransactionEventPayload:
    total_cost: Optional[int] = None
    charging_priority: Optional[int] = None
    id_token_info: Optional[datatypes.IdTokenInfoType] = None
    updated_personal_message: Optional[datatypes.MessageContentType] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class TriggerMessagePayload:
    status: enums.TriggerMessageStatusType
    status_info: Optional[datatypes.StatusInfoType] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class UnlockConnectorPayload:
    status: enums.UnlockStatusType
    status_info: Optional[datatypes.StatusInfoType] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class UnpublishFirmwarePayload:
    status: enums.UnpublishFirmwareStatusType
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class UpdateFirmwarePayload:
    status: enums.FirmwareStatusType
    status_info: Optional[datatypes.StatusInfoType] = None
    custom_data: Optional[Dict[str, Any]] = None
