from dataclasses import dataclass
from typing import Any, Dict, List, Optional

from ocpp.v201 import datatypes, enums


@dataclass
class Authorize:
    id_token_info: datatypes.IdTokenInfoType
    certificate_status: Optional[enums.AuthorizeCertificateStatusEnumType] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class BootNotification:
    current_time: str
    interval: int
    status: enums.RegistrationStatusEnumType
    status_info: Optional[datatypes.StatusInfoType] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class CancelReservation:
    status: enums.CancelReservationStatusEnumType
    status_info: Optional[datatypes.StatusInfoType] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class CertificateSigned:
    status: enums.CertificateSignedStatusEnumType
    status_info: Optional[datatypes.StatusInfoType] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class ChangeAvailability:
    status: enums.ChangeAvailabilityStatusEnumType
    status_info: Optional[datatypes.StatusInfoType] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class ClearCache:
    status: enums.ClearCacheStatusEnumType
    status_info: Optional[datatypes.StatusInfoType] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class ClearChargingProfile:
    status: enums.ClearChargingProfileStatusEnumType
    status_info: Optional[datatypes.StatusInfoType] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class ClearDisplayMessage:
    status: enums.ClearMessageStatusEnumType
    status_info: Optional[datatypes.StatusInfoType] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class ClearVariableMonitoring:
    clear_monitoring_result: List[enums.ClearMonitoringStatusEnumType]
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class ClearedChargingLimit:
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class CostUpdated:
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class CustomerInformation:
    status: enums.CustomerInformationStatusEnumType
    status_info: Optional[datatypes.StatusInfoType] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class DataTransfer:
    status: enums.DataTransferStatusEnumType
    status_info: Optional[datatypes.StatusInfoType] = None
    data: Optional[Any] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class DeleteCertificate:
    status: enums.DeleteCertificateStatusEnumType
    status_info: Optional[datatypes.StatusInfoType] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class FirmwareStatusNotification:
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class Get15118EVCertificate:
    status: enums.Iso15118EVCertificateStatusEnumType
    exi_response: str
    status_info: Optional[datatypes.StatusInfoType] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class GetBaseReport:
    status: enums.GenericDeviceModelStatusEnumType
    status_info: Optional[datatypes.StatusInfoType] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class GetCertificateStatus:
    status: enums.GetCertificateStatusEnumType
    status_info: Optional[datatypes.StatusInfoType] = None
    ocsp_result: Optional[str] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class GetChargingProfiles:
    status: enums.GetChargingProfileStatusEnumType
    status_info: Optional[datatypes.StatusInfoType] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class GetCompositeSchedule:
    status: enums.GenericStatusEnumType
    status_info: Optional[datatypes.StatusInfoType] = None
    schedule: Optional[datatypes.CompositeScheduleType] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class GetDisplayMessages:
    status: enums.GetDisplayMessagesStatusEnumType
    status_info: Optional[datatypes.StatusInfoType] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class GetInstalledCertificateIds:
    status: enums.GetInstalledCertificateStatusEnumType
    status_info: Optional[datatypes.StatusInfoType] = None
    certificate_hash_data_chain: Optional[
        List[datatypes.CertificateHashDataChainType]
    ] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class GetLocalListVersion:
    version_number: int
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class GetLog:
    status: enums.LogStatusEnumType
    status_info: Optional[datatypes.StatusInfoType] = None
    filename: Optional[str] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class GetMonitoringReport:
    status: enums.GenericDeviceModelStatusEnumType
    status_info: Optional[datatypes.StatusInfoType] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class GetReport:
    status: enums.GenericDeviceModelStatusEnumType
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
    status: enums.InstallCertificateStatusEnumType
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
    status: enums.NotifyEVChargingNeedsStatusEnumType
    status_info: Optional[datatypes.StatusInfoType] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class NotifyEVChargingSchedule:
    status: enums.GenericStatusEnumType
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
    status: enums.GenericStatusEnumType
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
    status: enums.RequestStartStopStatusEnumType
    status_info: Optional[datatypes.StatusInfoType] = None
    transaction_id: Optional[str] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class RequestStopTransaction:
    status: enums.RequestStartStopStatusEnumType
    status_info: Optional[datatypes.StatusInfoType] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class ReservationStatusUpdate:
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class ReserveNow:
    status: enums.ReserveNowStatusEnumType
    status_info: Optional[datatypes.StatusInfoType] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class Reset:
    status: enums.ResetStatusEnumType
    status_info: Optional[datatypes.StatusInfoType] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class SecurityEventNotification:
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class SendLocalList:
    status: enums.SendLocalListStatusEnumType
    status_info: Optional[datatypes.StatusInfoType] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class SetChargingProfile:
    status: enums.ChargingProfileStatusEnumType
    status_info: Optional[datatypes.StatusInfoType] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class SetDisplayMessage:
    status: enums.DisplayMessageStatusEnumType
    status_info: Optional[datatypes.StatusInfoType] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class SetMonitoringBase:
    status: enums.GenericDeviceModelStatusEnumType
    status_info: Optional[datatypes.StatusInfoType] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class SetMonitoringLevel:
    status: enums.GenericStatusEnumType
    status_info: Optional[datatypes.StatusInfoType] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class SetNetworkProfile:
    status: enums.SetNetworkProfileStatusEnumType
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
    status: enums.GenericStatusEnumType
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
    status: enums.TriggerMessageStatusEnumType
    status_info: Optional[datatypes.StatusInfoType] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class UnlockConnector:
    status: enums.UnlockStatusEnumType
    status_info: Optional[datatypes.StatusInfoType] = None
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class UnpublishFirmware:
    status: enums.UnpublishFirmwareStatusEnumType
    custom_data: Optional[Dict[str, Any]] = None


@dataclass
class UpdateFirmware:
    status: enums.UpdateFirmwareStatusEnumType
    status_info: Optional[datatypes.StatusInfoType] = None
    custom_data: Optional[Dict[str, Any]] = None
