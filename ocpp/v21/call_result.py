from dataclasses import dataclass
from typing import Any, List, Optional

import enums
from datatypes import (
    CertificateHashDataChain,
    CompositeSchedule,
    CustomData,
    GetVariableResult,
    IdTokenInfo,
    MessageContent,
    ResponseClearMonitoringResult,
    SetMonitoringResult,
    SetVariableResult,
    StatusInfo,
)
from enums import (
    AuthorizeCertificateStatus,
    CancelReservationStatus,
    CertificateSignedStatus,
    ChangeAvailabilityStatus,
    ChargingProfileStatus,
    ClearCacheStatus,
    ClearChargingProfileStatus,
    ClearMessageStatus,
    CustomerInformationStatus,
    DataTransferStatus,
    DeleteCertificateStatus,
    DisplayMessageStatus,
    EnergyTransferMode,
    GenericDeviceModelStatus,
    GenericStatus,
    GetChargingProfileStatus,
    GetDisplayMessagesStatus,
    GetInstalledCertificateStatus,
    InstallCertificateStatus,
    Iso15118EVCertificateStatus,
    LogStatus,
    NotifyAllowedEnergyTransferStatus,
    NotifyEVChargingNeedsStatus,
    PriorityChargingStatus,
    RegistrationStatus,
    RequestStartStopStatus,
    ReserveNowStatus,
    ResetStatus,
    SendLocalListStatus,
    SetNetworkProfileStatus,
    TriggerMessageStatus,
    UnlockStatus,
    UnpublishFirmwareStatus,
    UpdateFirmwareStatus,
)


@dataclass
class AFRRSignal:
    status: GenericStatus
    custom_data: Optional[CustomData] = None
    status_info: Optional[StatusInfo] = None


@dataclass
class Authorize:
    id_token_info: IdTokenInfo
    allowed_energy_transfer: Optional[List[EnergyTransferMode]] = None
    certificate_status: Optional[AuthorizeCertificateStatus] = None
    custom_data: Optional[CustomData] = None


@dataclass
class BootNotification:
    current_time: str
    interval: int
    status: RegistrationStatus
    custom_data: Optional[CustomData] = None
    status_info: Optional[StatusInfo] = None


@dataclass
class CancelReservation:
    status: CancelReservationStatus
    custom_data: Optional[CustomData] = None
    status_info: Optional[StatusInfo] = None


@dataclass
class CertificateSigned:
    status: CertificateSignedStatus
    custom_data: Optional[CustomData] = None
    status_info: Optional[StatusInfo] = None


@dataclass
class ChangeAvailability:
    status: ChangeAvailabilityStatus
    custom_data: Optional[CustomData] = None
    status_info: Optional[StatusInfo] = None


@dataclass
class ClearCache:
    status: ClearCacheStatus
    custom_data: Optional[CustomData] = None
    status_info: Optional[StatusInfo] = None


@dataclass
class ClearChargingProfile:
    status: ClearChargingProfileStatus
    custom_data: Optional[CustomData] = None
    status_info: Optional[StatusInfo] = None


@dataclass
class ClearDisplayMessage:
    status: ClearMessageStatus
    custom_data: Optional[CustomData] = None
    status_info: Optional[StatusInfo] = None


@dataclass
class ClearVariableMonitoring:
    clear_monitoring_result: List[ResponseClearMonitoringResult]
    custom_data: Optional[CustomData] = None


@dataclass
class ClearedChargingLimit:
    custom_data: Optional[CustomData] = None


@dataclass
class CostUpdated:
    custom_data: Optional[CustomData] = None


@dataclass
class CustomerInformation:
    status: CustomerInformationStatus
    custom_data: Optional[CustomData] = None
    status_info: Optional[StatusInfo] = None


@dataclass
class DataTransfer:
    status: DataTransferStatus
    custom_data: Optional[CustomData] = None
    data: Any = None
    status_info: Optional[StatusInfo] = None


@dataclass
class DeleteCertificate:
    status: DeleteCertificateStatus
    custom_data: Optional[CustomData] = None
    status_info: Optional[StatusInfo] = None


@dataclass
class FirmwareStatusNotification:
    custom_data: Optional[CustomData] = None


@dataclass
class Get15118EVCertificate:
    exi_response: str
    status: Iso15118EVCertificateStatus
    custom_data: Optional[CustomData] = None
    remaining_contracts: Optional[int] = None
    status_info: Optional[StatusInfo] = None


@dataclass
class GetBaseReport:
    status: GenericDeviceModelStatus
    custom_data: Optional[CustomData] = None
    status_info: Optional[StatusInfo] = None


@dataclass
class GetCRL:
    request_id: int
    status: GenericStatus
    custom_data: Optional[CustomData] = None
    status_info: Optional[StatusInfo] = None


@dataclass
class GetCertificateStatus:
    status: enums.GetCertificateStatus
    custom_data: Optional[CustomData] = None
    ocsp_result: Optional[str] = None
    status_info: Optional[StatusInfo] = None


@dataclass
class GetChargingProfiles:
    status: GetChargingProfileStatus
    custom_data: Optional[CustomData] = None
    status_info: Optional[StatusInfo] = None


@dataclass
class GetCompositeSchedule:
    status: GenericStatus
    custom_data: Optional[CustomData] = None
    schedule: Optional[CompositeSchedule] = None
    status_info: Optional[StatusInfo] = None


@dataclass
class GetDisplayMessages:
    status: GetDisplayMessagesStatus
    custom_data: Optional[CustomData] = None
    status_info: Optional[StatusInfo] = None


@dataclass
class GetInstalledCertificateIds:
    status: GetInstalledCertificateStatus
    certificate_hash_data_chain: Optional[List[CertificateHashDataChain]] = None
    custom_data: Optional[CustomData] = None
    status_info: Optional[StatusInfo] = None


@dataclass
class GetLocalListVersion:
    version_number: int
    custom_data: Optional[CustomData] = None


@dataclass
class GetLog:
    status: LogStatus
    custom_data: Optional[CustomData] = None
    filename: Optional[str] = None
    status_info: Optional[StatusInfo] = None


@dataclass
class GetMonitoringReport:
    status: GenericDeviceModelStatus
    custom_data: Optional[CustomData] = None
    status_info: Optional[StatusInfo] = None


@dataclass
class GetReport:
    status: GenericDeviceModelStatus
    custom_data: Optional[CustomData] = None
    status_info: Optional[StatusInfo] = None


@dataclass
class GetTransactionStatus:
    messages_in_queue: bool
    custom_data: Optional[CustomData] = None
    ongoing_indicator: Optional[bool] = None


@dataclass
class GetVariables:
    get_variable_result: List[GetVariableResult]
    custom_data: Optional[CustomData] = None


@dataclass
class Heartbeat:
    current_time: str
    custom_data: Optional[CustomData] = None


@dataclass
class InstallCertificate:
    status: InstallCertificateStatus
    custom_data: Optional[CustomData] = None
    status_info: Optional[StatusInfo] = None


@dataclass
class LogStatusNotification:
    custom_data: Optional[CustomData] = None


@dataclass
class MeterValues:
    custom_data: Optional[CustomData] = None


@dataclass
class NotifyAllowedEnergyTransfer:
    status: NotifyAllowedEnergyTransferStatus
    custom_data: Optional[CustomData] = None
    status_info: Optional[StatusInfo] = None


@dataclass
class NotifyCRL:
    custom_data: Optional[CustomData] = None


@dataclass
class NotifyChargingLimit:
    custom_data: Optional[CustomData] = None


@dataclass
class NotifyCustomerInformation:
    custom_data: Optional[CustomData] = None


@dataclass
class NotifyDisplayMessages:
    custom_data: Optional[CustomData] = None


@dataclass
class NotifyEVChargingNeeds:
    status: NotifyEVChargingNeedsStatus
    custom_data: Optional[CustomData] = None
    status_info: Optional[StatusInfo] = None


@dataclass
class NotifyEVChargingSchedule:
    status: GenericStatus
    custom_data: Optional[CustomData] = None
    status_info: Optional[StatusInfo] = None


@dataclass
class NotifyEvent:
    custom_data: Optional[CustomData] = None


@dataclass
class NotifyMonitoringReport:
    custom_data: Optional[CustomData] = None


@dataclass
class NotifyPriorityCharging:
    custom_data: Optional[CustomData] = None


@dataclass
class NotifyReport:
    custom_data: Optional[CustomData] = None


@dataclass
class PublishFirmware:
    status: GenericStatus
    custom_data: Optional[CustomData] = None
    status_info: Optional[StatusInfo] = None


@dataclass
class PublishFirmwareStatusNotification:
    custom_data: Optional[CustomData] = None


@dataclass
class PullDynamicScheduleUpdate:
    custom_data: Optional[CustomData] = None
    discharge_limit: Optional[float] = None
    discharge_limit_l2: Optional[float] = None
    discharge_limit_l3: Optional[float] = None
    limit: Optional[float] = None
    limit_l2: Optional[float] = None
    limit_l3: Optional[float] = None
    setpoint: Optional[float] = None
    setpoint_l2: Optional[float] = None
    setpoint_l3: Optional[float] = None
    setpoint_reactive: Optional[float] = None
    setpoint_reactive_l2: Optional[float] = None
    setpoint_reactive_l3: Optional[float] = None


@dataclass
class ReportChargingProfiles:
    custom_data: Optional[CustomData] = None


@dataclass
class RequestStartTransaction:
    status: RequestStartStopStatus
    custom_data: Optional[CustomData] = None
    status_info: Optional[StatusInfo] = None
    transaction_id: Optional[str] = None


@dataclass
class RequestStopTransaction:
    status: RequestStartStopStatus
    custom_data: Optional[CustomData] = None
    status_info: Optional[StatusInfo] = None


@dataclass
class ReservationStatusUpdate:
    custom_data: Optional[CustomData] = None


@dataclass
class ReserveNow:
    status: ReserveNowStatus
    custom_data: Optional[CustomData] = None
    status_info: Optional[StatusInfo] = None


@dataclass
class Reset:
    status: ResetStatus
    custom_data: Optional[CustomData] = None
    status_info: Optional[StatusInfo] = None


@dataclass
class SecurityEventNotification:
    custom_data: Optional[CustomData] = None


@dataclass
class SendLocalList:
    status: SendLocalListStatus
    custom_data: Optional[CustomData] = None
    status_info: Optional[StatusInfo] = None


@dataclass
class SetChargingProfile:
    status: ChargingProfileStatus
    custom_data: Optional[CustomData] = None
    status_info: Optional[StatusInfo] = None


@dataclass
class SetDisplayMessage:
    status: DisplayMessageStatus
    custom_data: Optional[CustomData] = None
    status_info: Optional[StatusInfo] = None


@dataclass
class SetMonitoringBase:
    status: GenericDeviceModelStatus
    custom_data: Optional[CustomData] = None
    status_info: Optional[StatusInfo] = None


@dataclass
class SetMonitoringLevel:
    status: GenericStatus
    custom_data: Optional[CustomData] = None
    status_info: Optional[StatusInfo] = None


@dataclass
class SetNetworkProfile:
    status: SetNetworkProfileStatus
    custom_data: Optional[CustomData] = None
    status_info: Optional[StatusInfo] = None


@dataclass
class SetVariableMonitoring:
    set_monitoring_result: List[SetMonitoringResult]
    custom_data: Optional[CustomData] = None


@dataclass
class SetVariables:
    set_variable_result: List[SetVariableResult]
    custom_data: Optional[CustomData] = None


@dataclass
class SignCertificate:
    status: GenericStatus
    custom_data: Optional[CustomData] = None
    status_info: Optional[StatusInfo] = None


@dataclass
class StatusNotification:
    custom_data: Optional[CustomData] = None


@dataclass
class TransactionEvent:
    charging_priority: Optional[int] = None
    custom_data: Optional[CustomData] = None
    id_token_info: Optional[IdTokenInfo] = None
    total_cost: Optional[float] = None
    updated_personal_message: Optional[MessageContent] = None


@dataclass
class TriggerMessage:
    status: TriggerMessageStatus
    custom_data: Optional[CustomData] = None
    status_info: Optional[StatusInfo] = None


@dataclass
class UnlockConnector:
    status: UnlockStatus
    custom_data: Optional[CustomData] = None
    status_info: Optional[StatusInfo] = None


@dataclass
class UnpublishFirmware:
    status: UnpublishFirmwareStatus
    custom_data: Optional[CustomData] = None


@dataclass
class UpdateDynamicSchedule:
    status: ChargingProfileStatus
    custom_data: Optional[CustomData] = None


@dataclass
class UpdateFirmware:
    status: UpdateFirmwareStatus
    custom_data: Optional[CustomData] = None
    status_info: Optional[StatusInfo] = None


@dataclass
class UsePriorityCharging:
    status: PriorityChargingStatus
    custom_data: Optional[CustomData] = None
    status_info: Optional[StatusInfo] = None
