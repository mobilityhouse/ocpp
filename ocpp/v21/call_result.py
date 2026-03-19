from dataclasses import dataclass
from typing import List, Optional

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
from ocpp.v21.enums import (
    AuthorizeCertificateStatusEnumType,
    CancelReservationStatusEnumType,
    CertificateSignedStatusEnumType,
    ChangeAvailabilityStatusEnumType,
    ChargingProfileStatusEnumType,
    ClearCacheStatusEnumType,
    ClearChargingProfileStatusEnumType,
    ClearMessageStatusEnumType,
    CustomerInformationStatusEnumType,
    DataTransferStatusEnumType,
    DeleteCertificateStatusEnumType,
    DERControlStatusEnumType,
    DisplayMessageStatusEnumType,
    EnergyTransferModeEnumType,
    GenericDeviceModelStatusEnumType,
    GenericStatusEnumType,
    GetCertificateStatusEnumType,
    GetChargingProfileStatusEnumType,
    GetDisplayMessagesStatusEnumType,
    GetInstalledCertificateStatusEnumType,
    InstallCertificateStatusEnumType,
    Iso15118EVCertificateStatusEnumType,
    LogStatusEnumType,
    NotifyAllowedEnergyTransferStatusEnumType,
    NotifyEVChargingNeedsStatusEnumType,
    PriorityChargingStatusEnumType,
    RegistrationStatusEnumType,
    RequestStartStopStatusEnumType,
    ReserveNowStatusEnumType,
    ResetStatusEnumType,
    SendLocalListStatusEnumType,
    SetNetworkProfileStatusEnumType,
    TariffChangeStatusEnumType,
    TariffGetStatusEnumType,
    TariffSetStatusEnumType,
    TriggerMessageStatusEnumType,
    UnlockStatusEnumType,
    UnpublishFirmwareStatusEnumType,
    UpdateFirmwareStatusEnumType,
)


@dataclass
class AFRRSignal:
    status: GenericStatusEnumType
    custom_data: Optional[CustomDataType] = None
    status_info: Optional[StatusInfoType] = None


@dataclass
class AdjustPeriodicEventStream:
    status: GenericStatusEnumType
    custom_data: Optional[CustomDataType] = None
    status_info: Optional[StatusInfoType] = None


@dataclass
class Authorize:
    id_token_info: IdTokenInfoType
    allowed_energy_transfer: Optional[List[EnergyTransferModeEnumType]] = None
    certificate_status: Optional[AuthorizeCertificateStatusEnumType] = None
    custom_data: Optional[CustomDataType] = None
    tariff: Optional[TariffType] = None


@dataclass
class BatterySwap:
    custom_data: Optional[CustomDataType] = None


@dataclass
class BootNotification:
    current_time: str
    interval: int
    status: RegistrationStatusEnumType
    custom_data: Optional[CustomDataType] = None
    status_info: Optional[StatusInfoType] = None


@dataclass
class CancelReservation:
    status: CancelReservationStatusEnumType
    custom_data: Optional[CustomDataType] = None
    status_info: Optional[StatusInfoType] = None


@dataclass
class CertificateSigned:
    status: CertificateSignedStatusEnumType
    custom_data: Optional[CustomDataType] = None
    status_info: Optional[StatusInfoType] = None


@dataclass
class ChangeAvailability:
    status: ChangeAvailabilityStatusEnumType
    custom_data: Optional[CustomDataType] = None
    status_info: Optional[StatusInfoType] = None


@dataclass
class ChangeTransactionTariff:
    status: TariffChangeStatusEnumType
    custom_data: Optional[CustomDataType] = None
    status_info: Optional[StatusInfoType] = None


@dataclass
class ClearCache:
    status: ClearCacheStatusEnumType
    custom_data: Optional[CustomDataType] = None
    status_info: Optional[StatusInfoType] = None


@dataclass
class ClearChargingProfile:
    status: ClearChargingProfileStatusEnumType
    custom_data: Optional[CustomDataType] = None
    status_info: Optional[StatusInfoType] = None


@dataclass
class ClearDERControl:
    status: DERControlStatusEnumType
    custom_data: Optional[CustomDataType] = None
    status_info: Optional[StatusInfoType] = None


@dataclass
class ClearDisplayMessage:
    status: ClearMessageStatusEnumType
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
    status: CustomerInformationStatusEnumType
    custom_data: Optional[CustomDataType] = None
    status_info: Optional[StatusInfoType] = None


@dataclass
class DataTransfer:
    status: DataTransferStatusEnumType
    custom_data: Optional[CustomDataType] = None
    data: Optional[str] = None
    status_info: Optional[StatusInfoType] = None


@dataclass
class DeleteCertificate:
    status: DeleteCertificateStatusEnumType
    custom_data: Optional[CustomDataType] = None
    status_info: Optional[StatusInfoType] = None


@dataclass
class FirmwareStatusNotification:
    custom_data: Optional[CustomDataType] = None


@dataclass
class Get15118EVCertificate:
    exi_response: str
    status: Iso15118EVCertificateStatusEnumType
    custom_data: Optional[CustomDataType] = None
    remaining_contracts: Optional[int] = None
    status_info: Optional[StatusInfoType] = None


@dataclass
class GetBaseReport:
    status: GenericDeviceModelStatusEnumType
    custom_data: Optional[CustomDataType] = None
    status_info: Optional[StatusInfoType] = None


@dataclass
class GetCertificateChainStatus:
    certificate_status: List[CertificateStatusType]
    custom_data: Optional[CustomDataType] = None


@dataclass
class GetCertificateStatus:
    status: GetCertificateStatusEnumType
    custom_data: Optional[CustomDataType] = None
    ocsp_result: Optional[str] = None
    status_info: Optional[StatusInfoType] = None


@dataclass
class GetChargingProfiles:
    status: GetChargingProfileStatusEnumType
    custom_data: Optional[CustomDataType] = None
    status_info: Optional[StatusInfoType] = None


@dataclass
class GetCompositeSchedule:
    status: GenericStatusEnumType
    custom_data: Optional[CustomDataType] = None
    schedule: Optional[CompositeScheduleType] = None
    status_info: Optional[StatusInfoType] = None


@dataclass
class GetDERControl:
    status: DERControlStatusEnumType
    custom_data: Optional[CustomDataType] = None
    status_info: Optional[StatusInfoType] = None


@dataclass
class GetDisplayMessages:
    status: GetDisplayMessagesStatusEnumType
    custom_data: Optional[CustomDataType] = None
    status_info: Optional[StatusInfoType] = None


@dataclass
class GetInstalledCertificateIds:
    status: GetInstalledCertificateStatusEnumType
    certificate_hash_data_chain: Optional[List[CertificateHashDataChainType]] = None
    custom_data: Optional[CustomDataType] = None
    status_info: Optional[StatusInfoType] = None


@dataclass
class GetLocalListVersion:
    version_number: int
    custom_data: Optional[CustomDataType] = None


@dataclass
class GetLog:
    status: LogStatusEnumType
    custom_data: Optional[CustomDataType] = None
    filename: Optional[str] = None
    status_info: Optional[StatusInfoType] = None


@dataclass
class GetMonitoringReport:
    status: GenericDeviceModelStatusEnumType
    custom_data: Optional[CustomDataType] = None
    status_info: Optional[StatusInfoType] = None


@dataclass
class GetPeriodicEventStream:
    constant_stream_data: Optional[List[ConstantStreamDataType]] = None
    custom_data: Optional[CustomDataType] = None


@dataclass
class GetReport:
    status: GenericDeviceModelStatusEnumType
    custom_data: Optional[CustomDataType] = None
    status_info: Optional[StatusInfoType] = None


@dataclass
class GetTariffs:
    status: TariffGetStatusEnumType
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
    status: InstallCertificateStatusEnumType
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
    status: NotifyAllowedEnergyTransferStatusEnumType
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
    status: NotifyEVChargingNeedsStatusEnumType
    custom_data: Optional[CustomDataType] = None
    status_info: Optional[StatusInfoType] = None


@dataclass
class NotifyEVChargingSchedule:
    status: GenericStatusEnumType
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
    status: GenericStatusEnumType
    custom_data: Optional[CustomDataType] = None
    status_info: Optional[StatusInfoType] = None


@dataclass
class PublishFirmware:
    status: GenericStatusEnumType
    custom_data: Optional[CustomDataType] = None
    status_info: Optional[StatusInfoType] = None


@dataclass
class PublishFirmwareStatusNotification:
    custom_data: Optional[CustomDataType] = None


@dataclass
class PullDynamicScheduleUpdate:
    status: ChargingProfileStatusEnumType
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
    status: GenericStatusEnumType
    custom_data: Optional[CustomDataType] = None
    status_info: Optional[StatusInfoType] = None


@dataclass
class RequestStartTransaction:
    status: RequestStartStopStatusEnumType
    custom_data: Optional[CustomDataType] = None
    status_info: Optional[StatusInfoType] = None
    transaction_id: Optional[str] = None


@dataclass
class RequestStopTransaction:
    status: RequestStartStopStatusEnumType
    custom_data: Optional[CustomDataType] = None
    status_info: Optional[StatusInfoType] = None


@dataclass
class ReservationStatusUpdate:
    custom_data: Optional[CustomDataType] = None


@dataclass
class ReserveNow:
    status: ReserveNowStatusEnumType
    custom_data: Optional[CustomDataType] = None
    status_info: Optional[StatusInfoType] = None


@dataclass
class Reset:
    status: ResetStatusEnumType
    custom_data: Optional[CustomDataType] = None
    status_info: Optional[StatusInfoType] = None


@dataclass
class SecurityEventNotification:
    custom_data: Optional[CustomDataType] = None


@dataclass
class SendLocalList:
    status: SendLocalListStatusEnumType
    custom_data: Optional[CustomDataType] = None
    status_info: Optional[StatusInfoType] = None


@dataclass
class SetChargingProfile:
    status: ChargingProfileStatusEnumType
    custom_data: Optional[CustomDataType] = None
    status_info: Optional[StatusInfoType] = None


@dataclass
class SetDERControl:
    status: DERControlStatusEnumType
    custom_data: Optional[CustomDataType] = None
    status_info: Optional[StatusInfoType] = None
    superseded_ids: Optional[List[str]] = None


@dataclass
class SetDefaultTariff:
    status: TariffSetStatusEnumType
    custom_data: Optional[CustomDataType] = None
    status_info: Optional[StatusInfoType] = None


@dataclass
class SetDisplayMessage:
    status: DisplayMessageStatusEnumType
    custom_data: Optional[CustomDataType] = None
    status_info: Optional[StatusInfoType] = None


@dataclass
class SetMonitoringBase:
    status: GenericDeviceModelStatusEnumType
    custom_data: Optional[CustomDataType] = None
    status_info: Optional[StatusInfoType] = None


@dataclass
class SetMonitoringLevel:
    status: GenericStatusEnumType
    custom_data: Optional[CustomDataType] = None
    status_info: Optional[StatusInfoType] = None


@dataclass
class SetNetworkProfile:
    status: SetNetworkProfileStatusEnumType
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
    status: GenericStatusEnumType
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
    status: TriggerMessageStatusEnumType
    custom_data: Optional[CustomDataType] = None
    status_info: Optional[StatusInfoType] = None


@dataclass
class UnlockConnector:
    status: UnlockStatusEnumType
    custom_data: Optional[CustomDataType] = None
    status_info: Optional[StatusInfoType] = None


@dataclass
class UnpublishFirmware:
    status: UnpublishFirmwareStatusEnumType
    custom_data: Optional[CustomDataType] = None


@dataclass
class UpdateDynamicSchedule:
    status: ChargingProfileStatusEnumType
    custom_data: Optional[CustomDataType] = None
    status_info: Optional[StatusInfoType] = None


@dataclass
class UpdateFirmware:
    status: UpdateFirmwareStatusEnumType
    custom_data: Optional[CustomDataType] = None
    status_info: Optional[StatusInfoType] = None


@dataclass
class UsePriorityCharging:
    status: PriorityChargingStatusEnumType
    custom_data: Optional[CustomDataType] = None
    status_info: Optional[StatusInfoType] = None


@dataclass
class VatNumberValidation:
    status: GenericStatusEnumType
    vat_number: str
    company: Optional[AddressType] = None
    custom_data: Optional[CustomDataType] = None
    evse_id: Optional[int] = None
    status_info: Optional[StatusInfoType] = None
