from dataclasses import dataclass
from typing import Any, List, Optional

from ocpp.v21.datatypes import (
    AddressType,
    CertificateHashDataChainType,
    CertificateStatusType,
    ChargingScheduleUpdateType,
    ClearMonitoringResultType,
    ClearTariffsResultType,
    CompositeScheduleType,
    ConstantStreamDataType,
    CustomDataType,
    GetVariableResultType,
    IdTokenInfoType,
    MessageContentType,
    SetMonitoringResultType,
    SetVariableResultType,
    StatusInfoType,
    TariffAssignmentType,
    TariffType,
    TransactionLimitType,
)

from ocpp.v21 import enums
from ocpp.v21.enums import (
    AuthorizeCertificateStatus,
    CancelReservationStatus,
    CertificateSignedStatus,
    ChangeAvailabilityStatus,
    ChargingProfileStatus,
    ClearCacheStatus,
    ClearChargingProfileStatus,
    ClearMessageStatus,
    CustomerInformationStatus,
    DERControlStatus,
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
    TariffChangeStatus,
    TariffGetStatus,
    TariffSetStatus,
    TriggerMessageStatus,
    UnlockStatus,
    UnpublishFirmwareStatus,
    UpdateFirmwareStatus,
)


@dataclass
class AFRRSignal:
    status: GenericStatus
    custom_data: Optional[CustomDataType] = None
    status_info: Optional[StatusInfoType] = None


@dataclass
class AdjustPeriodicEventStream:
    status: GenericStatus
    custom_data: Optional[CustomDataType] = None
    status_info: Optional[StatusInfoType] = None


@dataclass
class Authorize:
    id_token_info: IdTokenInfoType
    allowed_energy_transfer: Optional[List[EnergyTransferMode]] = None
    certificate_status: Optional[AuthorizeCertificateStatus] = None
    custom_data: Optional[CustomDataType] = None
    tariff: Optional[TariffType] = None


@dataclass
class BatterySwap:
    custom_data: Optional[CustomDataType] = None


@dataclass
class BootNotification:
    current_time: str
    interval: int
    status: RegistrationStatus
    custom_data: Optional[CustomDataType] = None
    status_info: Optional[StatusInfoType] = None


@dataclass
class CancelReservation:
    status: CancelReservationStatus
    custom_data: Optional[CustomDataType] = None
    status_info: Optional[StatusInfoType] = None


@dataclass
class CertificateSigned:
    status: CertificateSignedStatus
    custom_data: Optional[CustomDataType] = None
    status_info: Optional[StatusInfoType] = None


@dataclass
class ChangeAvailability:
    status: ChangeAvailabilityStatus
    custom_data: Optional[CustomDataType] = None
    status_info: Optional[StatusInfoType] = None


@dataclass
class ChangeTransactionTariff:
    status: TariffChangeStatus
    custom_data: Optional[CustomDataType] = None
    status_info: Optional[StatusInfoType] = None


@dataclass
class ClearCache:
    status: ClearCacheStatus
    custom_data: Optional[CustomDataType] = None
    status_info: Optional[StatusInfoType] = None


@dataclass
class ClearChargingProfile:
    status: ClearChargingProfileStatus
    custom_data: Optional[CustomDataType] = None
    status_info: Optional[StatusInfoType] = None


@dataclass
class ClearDERControl:
    status: DERControlStatus
    custom_data: Optional[CustomDataType] = None
    status_info: Optional[StatusInfoType] = None


@dataclass
class ClearDisplayMessage:
    status: ClearMessageStatus
    custom_data: Optional[CustomDataType] = None
    status_info: Optional[StatusInfoType] = None


@dataclass
class ClearTariffs:
    clear_tariffs_result: List[ClearTariffsResultType]
    custom_data: Optional[CustomDataType] = None


@dataclass
class ClearVariableMonitoring:
    clear_monitoring_result: List[ClearMonitoringResultType]
    custom_data: Optional[CustomDataType] = None


@dataclass
class ClearedChargingLimit:
    custom_data: Optional[CustomDataType] = None


@dataclass
class ClosePeriodicEventStream:
    custom_data: Optional[CustomDataType] = None


@dataclass
class CostUpdated:
    custom_data: Optional[CustomDataType] = None


@dataclass
class CustomerInformation:
    status: CustomerInformationStatus
    custom_data: Optional[CustomDataType] = None
    status_info: Optional[StatusInfoType] = None


@dataclass
class DataTransfer:
    status: DataTransferStatus
    custom_data: Optional[CustomDataType] = None
    data: Optional[str] = None
    status_info: Optional[StatusInfoType] = None


@dataclass
class DeleteCertificate:
    status: DeleteCertificateStatus
    custom_data: Optional[CustomDataType] = None
    status_info: Optional[StatusInfoType] = None


@dataclass
class FirmwareStatusNotification:
    custom_data: Optional[CustomDataType] = None


@dataclass
class Get15118EVCertificate:
    exi_response: str
    status: Iso15118EVCertificateStatus
    custom_data: Optional[CustomDataType] = None
    remaining_contracts: Optional[int] = None
    status_info: Optional[StatusInfoType] = None


@dataclass
class GetBaseReport:
    status: GenericDeviceModelStatus
    custom_data: Optional[CustomDataType] = None
    status_info: Optional[StatusInfoType] = None


@dataclass
class GetCertificateChainStatus:
    certificate_status: List[CertificateStatusType]
    custom_data: Optional[CustomDataType] = None


@dataclass
class GetCertificateStatus:
    status: enums.GetCertificateStatus
    custom_data: Optional[CustomDataType] = None
    ocsp_result: Optional[str] = None
    status_info: Optional[StatusInfoType] = None


@dataclass
class GetChargingProfiles:
    status: GetChargingProfileStatus
    custom_data: Optional[CustomDataType] = None
    status_info: Optional[StatusInfoType] = None


@dataclass
class GetCompositeSchedule:
    status: GenericStatus
    custom_data: Optional[CustomDataType] = None
    schedule: Optional[CompositeScheduleType] = None
    status_info: Optional[StatusInfoType] = None


@dataclass
class GetDERControl:
    status: DERControlStatus
    custom_data: Optional[CustomDataType] = None
    status_info: Optional[StatusInfoType] = None


@dataclass
class GetDisplayMessages:
    status: GetDisplayMessagesStatus
    custom_data: Optional[CustomDataType] = None
    status_info: Optional[StatusInfoType] = None


@dataclass
class GetInstalledCertificateIds:
    status: GetInstalledCertificateStatus
    certificate_hash_data_chain: Optional[List[CertificateHashDataChainType]] = None
    custom_data: Optional[CustomDataType] = None
    status_info: Optional[StatusInfoType] = None


@dataclass
class GetLocalListVersion:
    version_number: int
    custom_data: Optional[CustomDataType] = None


@dataclass
class GetLog:
    status: LogStatus
    custom_data: Optional[CustomDataType] = None
    filename: Optional[str] = None
    status_info: Optional[StatusInfoType] = None


@dataclass
class GetMonitoringReport:
    status: GenericDeviceModelStatus
    custom_data: Optional[CustomDataType] = None
    status_info: Optional[StatusInfoType] = None


@dataclass
class GetPeriodicEventStream:
    constant_stream_data: Optional[List[ConstantStreamDataType]] = None
    custom_data: Optional[CustomDataType] = None


@dataclass
class GetReport:
    status: GenericDeviceModelStatus
    custom_data: Optional[CustomDataType] = None
    status_info: Optional[StatusInfoType] = None


@dataclass
class GetTariffs:
    status: TariffGetStatus
    custom_data: Optional[CustomDataType] = None
    status_info: Optional[StatusInfoType] = None
    tariff_assignments: Optional[List[TariffAssignmentType]] = None


@dataclass
class GetTransactionStatus:
    messages_in_queue: bool
    custom_data: Optional[CustomDataType] = None
    ongoing_indicator: Optional[bool] = None


@dataclass
class GetVariables:
    get_variable_result: List[GetVariableResultType]
    custom_data: Optional[CustomDataType] = None


@dataclass
class Heartbeat:
    current_time: str
    custom_data: Optional[CustomDataType] = None


@dataclass
class InstallCertificate:
    status: InstallCertificateStatus
    custom_data: Optional[CustomDataType] = None
    status_info: Optional[StatusInfoType] = None


@dataclass
class LogStatusNotification:
    custom_data: Optional[CustomDataType] = None


@dataclass
class MeterValues:
    custom_data: Optional[CustomDataType] = None


@dataclass
class NotifyAllowedEnergyTransfer:
    status: NotifyAllowedEnergyTransferStatus
    custom_data: Optional[CustomDataType] = None
    status_info: Optional[StatusInfoType] = None


@dataclass
class NotifyChargingLimit:
    custom_data: Optional[CustomDataType] = None


@dataclass
class NotifyCustomerInformation:
    custom_data: Optional[CustomDataType] = None


@dataclass
class NotifyDERAlarm:
    custom_data: Optional[CustomDataType] = None


@dataclass
class NotifyDERStartStop:
    custom_data: Optional[CustomDataType] = None


@dataclass
class NotifyDisplayMessages:
    custom_data: Optional[CustomDataType] = None


@dataclass
class NotifyEVChargingNeeds:
    status: NotifyEVChargingNeedsStatus
    custom_data: Optional[CustomDataType] = None
    status_info: Optional[StatusInfoType] = None


@dataclass
class NotifyEVChargingSchedule:
    status: GenericStatus
    custom_data: Optional[CustomDataType] = None
    status_info: Optional[StatusInfoType] = None


@dataclass
class NotifyEvent:
    custom_data: Optional[CustomDataType] = None


@dataclass
class NotifyMonitoringReport:
    custom_data: Optional[CustomDataType] = None


@dataclass
class NotifyPriorityCharging:
    custom_data: Optional[CustomDataType] = None


@dataclass
class NotifyReport:
    custom_data: Optional[CustomDataType] = None


@dataclass
class NotifySettlement:
    custom_data: Optional[CustomDataType] = None
    receipt_id: Optional[str] = None
    receipt_url: Optional[str] = None


@dataclass
class NotifyWebPaymentStarted:
    custom_data: Optional[CustomDataType] = None


@dataclass
class OpenPeriodicEventStream:
    status: GenericStatus
    custom_data: Optional[CustomDataType] = None
    status_info: Optional[StatusInfoType] = None


@dataclass
class PublishFirmware:
    status: GenericStatus
    custom_data: Optional[CustomDataType] = None
    status_info: Optional[StatusInfoType] = None


@dataclass
class PublishFirmwareStatusNotification:
    custom_data: Optional[CustomDataType] = None


@dataclass
class PullDynamicScheduleUpdate:
    status: ChargingProfileStatus
    custom_data: Optional[CustomDataType] = None
    schedule_update: Optional[ChargingScheduleUpdateType] = None
    status_info: Optional[StatusInfoType] = None


@dataclass
class ReportChargingProfiles:
    custom_data: Optional[CustomDataType] = None


@dataclass
class ReportDERControl:
    custom_data: Optional[CustomDataType] = None


@dataclass
class RequestBatterySwap:
    status: GenericStatus
    custom_data: Optional[CustomDataType] = None
    status_info: Optional[StatusInfoType] = None


@dataclass
class RequestStartTransaction:
    status: RequestStartStopStatus
    custom_data: Optional[CustomDataType] = None
    status_info: Optional[StatusInfoType] = None
    transaction_id: Optional[str] = None


@dataclass
class RequestStopTransaction:
    status: RequestStartStopStatus
    custom_data: Optional[CustomDataType] = None
    status_info: Optional[StatusInfoType] = None


@dataclass
class ReservationStatusUpdate:
    custom_data: Optional[CustomDataType] = None


@dataclass
class ReserveNow:
    status: ReserveNowStatus
    custom_data: Optional[CustomDataType] = None
    status_info: Optional[StatusInfoType] = None


@dataclass
class Reset:
    status: ResetStatus
    custom_data: Optional[CustomDataType] = None
    status_info: Optional[StatusInfoType] = None


@dataclass
class SecurityEventNotification:
    custom_data: Optional[CustomDataType] = None


@dataclass
class SendLocalList:
    status: SendLocalListStatus
    custom_data: Optional[CustomDataType] = None
    status_info: Optional[StatusInfoType] = None


@dataclass
class SetChargingProfile:
    status: ChargingProfileStatus
    custom_data: Optional[CustomDataType] = None
    status_info: Optional[StatusInfoType] = None


@dataclass
class SetDERControl:
    status: DERControlStatus
    custom_data: Optional[CustomDataType] = None
    status_info: Optional[StatusInfoType] = None
    superseded_ids: Optional[List[str]] = None


@dataclass
class SetDefaultTariff:
    status: TariffSetStatus
    custom_data: Optional[CustomDataType] = None
    status_info: Optional[StatusInfoType] = None


@dataclass
class SetDisplayMessage:
    status: DisplayMessageStatus
    custom_data: Optional[CustomDataType] = None
    status_info: Optional[StatusInfoType] = None


@dataclass
class SetMonitoringBase:
    status: GenericDeviceModelStatus
    custom_data: Optional[CustomDataType] = None
    status_info: Optional[StatusInfoType] = None


@dataclass
class SetMonitoringLevel:
    status: GenericStatus
    custom_data: Optional[CustomDataType] = None
    status_info: Optional[StatusInfoType] = None


@dataclass
class SetNetworkProfile:
    status: SetNetworkProfileStatus
    custom_data: Optional[CustomDataType] = None
    status_info: Optional[StatusInfoType] = None


@dataclass
class SetVariableMonitoring:
    set_monitoring_result: List[SetMonitoringResultType]
    custom_data: Optional[CustomDataType] = None


@dataclass
class SetVariables:
    set_variable_result: List[SetVariableResultType]
    custom_data: Optional[CustomDataType] = None


@dataclass
class SignCertificate:
    status: GenericStatus
    custom_data: Optional[CustomDataType] = None
    status_info: Optional[StatusInfoType] = None


@dataclass
class StatusNotification:
    custom_data: Optional[CustomDataType] = None


@dataclass
class TransactionEvent:
    charging_priority: Optional[int] = None
    custom_data: Optional[CustomDataType] = None
    id_token_info: Optional[IdTokenInfoType] = None
    total_cost: Optional[float] = None
    transaction_limit: Optional[TransactionLimitType] = None
    updated_personal_message: Optional[MessageContentType] = None
    updated_personal_message_extra: Optional[List[MessageContentType]] = None


@dataclass
class TriggerMessage:
    status: TriggerMessageStatus
    custom_data: Optional[CustomDataType] = None
    status_info: Optional[StatusInfoType] = None


@dataclass
class UnlockConnector:
    status: UnlockStatus
    custom_data: Optional[CustomDataType] = None
    status_info: Optional[StatusInfoType] = None


@dataclass
class UnpublishFirmware:
    status: UnpublishFirmwareStatus
    custom_data: Optional[CustomDataType] = None


@dataclass
class UpdateDynamicSchedule:
    status: ChargingProfileStatus
    custom_data: Optional[CustomDataType] = None
    status_info: Optional[StatusInfoType] = None


@dataclass
class UpdateFirmware:
    status: UpdateFirmwareStatus
    custom_data: Optional[CustomDataType] = None
    status_info: Optional[StatusInfoType] = None


@dataclass
class UsePriorityCharging:
    status: PriorityChargingStatus
    custom_data: Optional[CustomDataType] = None
    status_info: Optional[StatusInfoType] = None


@dataclass
class VatNumberValidation:
    status: GenericStatus
    vat_number: str
    company: Optional[AddressType] = None
    custom_data: Optional[CustomDataType] = None
    evse_id: Optional[int] = None
    status_info: Optional[StatusInfoType] = None
