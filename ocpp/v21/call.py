from dataclasses import dataclass
from typing import List, Optional

from ocpp.v21.datatypes import (
    AddressType,
    AuthorizationData,
    BatteryDataType,
    CertificateHashDataType,
    CertificateStatusRequestInfoType,
    ChargingLimitType,
    ChargingNeedsType,
    ChargingProfileCriterionType,
    ChargingProfileType,
    ChargingScheduleType,
    ChargingScheduleUpdateType,
    ChargingStationType,
    ClearChargingProfileType,
    ComponentVariableType,
    ConstantStreamDataType,
    CostDetailsType,
    CustomDataType,
    DERCurveGetType,
    DERCurveType,
    EnterServiceGetType,
    EnterServiceType,
    EventDataType,
    EVSEType,
    FirmwareType,
    FixedPFGetType,
    FixedPFType,
    FixedVarGetType,
    FixedVarType,
    FreqDroopGetType,
    FreqDroopType,
    GetVariableDataType,
    GradientGetType,
    GradientType,
    IdTokenType,
    LimitMaxDischargeGetType,
    LimitMaxDischargeType,
    LogParametersType,
    MessageInfoType,
    MeterValueType,
    MonitoringDataType,
    NetworkConnectionProfileType,
    OCSPRequestDataType,
    PeriodicEventStreamParamsType,
    ReportDataType,
    SetMonitoringDataType,
    SetVariableDataType,
    StatusInfoType,
    TariffType,
    TransactionType,
)
from ocpp.v21.enums import (
    BatterySwapEventEnumType,
    BootReasonEnumType,
    CertificateActionEnumType,
    CertificateSigningUseEnumType,
    ChargingRateUnitEnumType,
    ComponentCriterionEnumType,
    ConnectorStatusEnumType,
    DERControlEnumType,
    EnergyTransferModeEnumType,
    FirmwareStatusEnumType,
    GetCertificateIdUseEnumType,
    GridEventFaultEnumType,
    InstallCertificateUseEnumType,
    LogEnumType,
    MessagePriorityEnumType,
    MessageStateEnumType,
    MessageTriggerEnumType,
    MonitoringBaseEnumType,
    MonitoringCriterionEnumType,
    OperationalStatusEnumType,
    PaymentStatusEnumType,
    PreconditioningStatusEnumType,
    PublishFirmwareStatusEnumType,
    ReportBaseEnumType,
    ReservationUpdateStatusEnumType,
    ResetEnumType,
    TransactionEventEnumType,
    TriggerReasonEnumType,
    UpdateEnumType,
    UploadLogStatusEnumType,
)


@dataclass
class AFRRSignal:
    signal: int
    timestamp: str
    custom_data: Optional[CustomDataType] = None


@dataclass
class AdjustPeriodicEventStream:
    id: int
    params: PeriodicEventStreamParamsType
    custom_data: Optional[CustomDataType] = None


@dataclass
class Authorize:
    id_token: IdTokenType
    certificate: Optional[str] = None
    custom_data: Optional[CustomDataType] = None
    iso_15118_certificate_hash_data: Optional[List[OCSPRequestDataType]] = None


@dataclass
class BatterySwap:
    battery_data: List[BatteryDataType]
    event_type: BatterySwapEventEnumType
    id_token: IdTokenType
    request_id: int
    custom_data: Optional[CustomDataType] = None


@dataclass
class BootNotification:
    charging_station: ChargingStationType
    reason: BootReasonEnumType
    custom_data: Optional[CustomDataType] = None


@dataclass
class CancelReservation:
    reservation_id: int
    custom_data: Optional[CustomDataType] = None


@dataclass
class CertificateSigned:
    certificate_chain: str
    certificate_type: Optional[CertificateSigningUseEnumType] = None
    custom_data: Optional[CustomDataType] = None
    request_id: Optional[int] = None


@dataclass
class ChangeAvailability:
    operational_status: OperationalStatusEnumType
    custom_data: Optional[CustomDataType] = None
    evse: Optional[EVSEType] = None


@dataclass
class ChangeTransactionTariff:
    tariff: TariffType
    transaction_id: str
    custom_data: Optional[CustomDataType] = None


@dataclass
class ClearCache:
    custom_data: Optional[CustomDataType] = None


@dataclass
class ClearChargingProfile:
    charging_profile_criteria: Optional[ClearChargingProfileType] = None
    charging_profile_id: Optional[int] = None
    custom_data: Optional[CustomDataType] = None


@dataclass
class ClearDERControl:
    is_default: bool
    control_id: Optional[str] = None
    control_type: Optional[DERControlEnumType] = None
    custom_data: Optional[CustomDataType] = None


@dataclass
class ClearDisplayMessage:
    id: int
    custom_data: Optional[CustomDataType] = None


@dataclass
class ClearTariffs:
    custom_data: Optional[CustomDataType] = None
    evse_id: Optional[int] = None
    tariff_ids: Optional[List[str]] = None


@dataclass
class ClearVariableMonitoring:
    id: List[int]
    custom_data: Optional[CustomDataType] = None


@dataclass
class ClearedChargingLimit:
    charging_limit_source: str
    custom_data: Optional[CustomDataType] = None
    evse_id: Optional[int] = None


@dataclass
class ClosePeriodicEventStream:
    id: int
    custom_data: Optional[CustomDataType] = None


@dataclass
class CostUpdated:
    total_cost: float
    transaction_id: str
    custom_data: Optional[CustomDataType] = None


@dataclass
class CustomerInformation:
    clear: bool
    report: bool
    request_id: int
    custom_data: Optional[CustomDataType] = None
    customer_certificate: Optional[CertificateHashDataType] = None
    customer_identifier: Optional[str] = None
    id_token: Optional[IdTokenType] = None


@dataclass
class DataTransfer:
    vendor_id: str
    custom_data: Optional[CustomDataType] = None
    data: Optional[str] = None
    message_id: Optional[str] = None


@dataclass
class DeleteCertificate:
    certificate_hash_data: CertificateHashDataType
    custom_data: Optional[CustomDataType] = None


@dataclass
class FirmwareStatusNotification:
    status: FirmwareStatusEnumType
    custom_data: Optional[CustomDataType] = None
    request_id: Optional[int] = None
    status_info: Optional[StatusInfoType] = None


@dataclass
class Get15118EVCertificate:
    action: CertificateActionEnumType
    exi_request: str
    iso_15118_schema_version: str
    custom_data: Optional[CustomDataType] = None
    maximum_contract_certificate_chains: Optional[int] = None
    prioritized_emaids: Optional[List[str]] = None


@dataclass
class GetBaseReport:
    report_base: ReportBaseEnumType
    request_id: int
    custom_data: Optional[CustomDataType] = None


@dataclass
class GetCertificateChainStatus:
    certificate_status_requests: List[CertificateStatusRequestInfoType]
    custom_data: Optional[CustomDataType] = None


@dataclass
class GetCertificateStatus:
    ocsp_request_data: OCSPRequestDataType
    custom_data: Optional[CustomDataType] = None


@dataclass
class GetChargingProfiles:
    charging_profile: ChargingProfileCriterionType
    request_id: int
    custom_data: Optional[CustomDataType] = None
    evse_id: Optional[int] = None


@dataclass
class GetCompositeSchedule:
    duration: int
    evse_id: int
    charging_rate_unit: Optional[ChargingRateUnitEnumType] = None
    custom_data: Optional[CustomDataType] = None


@dataclass
class GetDERControl:
    request_id: int
    control_id: Optional[str] = None
    control_type: Optional[DERControlEnumType] = None
    custom_data: Optional[CustomDataType] = None
    is_default: Optional[bool] = None


@dataclass
class GetDisplayMessages:
    request_id: int
    custom_data: Optional[CustomDataType] = None
    id: Optional[List[int]] = None
    priority: Optional[MessagePriorityEnumType] = None
    state: Optional[MessageStateEnumType] = None


@dataclass
class GetInstalledCertificateIds:
    certificate_type: Optional[List[GetCertificateIdUseEnumType]] = None
    custom_data: Optional[CustomDataType] = None


@dataclass
class GetLocalListVersion:
    custom_data: Optional[CustomDataType] = None


@dataclass
class GetLog:
    log: LogParametersType
    log_type: LogEnumType
    request_id: int
    custom_data: Optional[CustomDataType] = None
    retries: Optional[int] = None
    retry_interval: Optional[int] = None


@dataclass
class GetMonitoringReport:
    request_id: int
    component_variable: Optional[List[ComponentVariableType]] = None
    custom_data: Optional[CustomDataType] = None
    monitoring_criteria: Optional[List[MonitoringCriterionEnumType]] = None


@dataclass
class GetPeriodicEventStream:
    custom_data: Optional[CustomDataType] = None


@dataclass
class GetReport:
    request_id: int
    component_criteria: Optional[List[ComponentCriterionEnumType]] = None
    component_variable: Optional[List[ComponentVariableType]] = None
    custom_data: Optional[CustomDataType] = None


@dataclass
class GetTariffs:
    evse_id: int
    custom_data: Optional[CustomDataType] = None


@dataclass
class GetTransactionStatus:
    custom_data: Optional[CustomDataType] = None
    transaction_id: Optional[str] = None


@dataclass
class GetVariables:
    get_variable_data: List[GetVariableDataType]
    custom_data: Optional[CustomDataType] = None


@dataclass
class Heartbeat:
    custom_data: Optional[CustomDataType] = None


@dataclass
class InstallCertificate:
    certificate: str
    certificate_type: InstallCertificateUseEnumType
    custom_data: Optional[CustomDataType] = None


@dataclass
class LogStatusNotification:
    status: UploadLogStatusEnumType
    custom_data: Optional[CustomDataType] = None
    request_id: Optional[int] = None
    status_info: Optional[StatusInfoType] = None


@dataclass
class MeterValues:
    evse_id: int
    meter_value: List[MeterValueType]
    custom_data: Optional[CustomDataType] = None


@dataclass
class NotifyAllowedEnergyTransfer:
    allowed_energy_transfer: List[EnergyTransferModeEnumType]
    transaction_id: str
    custom_data: Optional[CustomDataType] = None


@dataclass
class NotifyChargingLimit:
    charging_limit: ChargingLimitType
    charging_schedule: Optional[List[ChargingScheduleType]] = None
    custom_data: Optional[CustomDataType] = None
    evse_id: Optional[int] = None


@dataclass
class NotifyCustomerInformation:
    data: str
    generated_at: str
    request_id: int
    seq_no: int
    custom_data: Optional[CustomDataType] = None
    tbc: bool = False


@dataclass
class NotifyDERAlarm:
    control_type: DERControlEnumType
    timestamp: str
    alarm_ended: Optional[bool] = None
    custom_data: Optional[CustomDataType] = None
    extra_info: Optional[str] = None
    grid_event_fault: Optional[GridEventFaultEnumType] = None


@dataclass
class NotifyDERStartStop:
    control_id: str
    started: bool
    timestamp: str
    custom_data: Optional[CustomDataType] = None
    superseded_ids: Optional[List[str]] = None


@dataclass
class NotifyDisplayMessages:
    request_id: int
    custom_data: Optional[CustomDataType] = None
    message_info: Optional[List[MessageInfoType]] = None
    tbc: bool = False


@dataclass
class NotifyEVChargingNeeds:
    charging_needs: ChargingNeedsType
    evse_id: int
    custom_data: Optional[CustomDataType] = None
    max_schedule_tuples: Optional[int] = None
    timestamp: Optional[str] = None


@dataclass
class NotifyEVChargingSchedule:
    charging_schedule: ChargingScheduleType
    evse_id: int
    time_base: str
    custom_data: Optional[CustomDataType] = None
    power_tolerance_acceptance: Optional[bool] = None
    selected_charging_schedule_id: Optional[int] = None


@dataclass
class NotifyEvent:
    event_data: List[EventDataType]
    generated_at: str
    seq_no: int
    custom_data: Optional[CustomDataType] = None
    tbc: bool = False


@dataclass
class NotifyMonitoringReport:
    generated_at: str
    request_id: int
    seq_no: int
    custom_data: Optional[CustomDataType] = None
    monitor: Optional[List[MonitoringDataType]] = None
    tbc: bool = False


@dataclass
class NotifyPriorityCharging:
    activated: bool
    transaction_id: str
    custom_data: Optional[CustomDataType] = None


@dataclass
class NotifyReport:
    generated_at: str
    request_id: int
    seq_no: int
    custom_data: Optional[CustomDataType] = None
    report_data: Optional[List[ReportDataType]] = None
    tbc: bool = False


@dataclass
class NotifySettlement:
    psp_ref: str
    settlement_amount: float
    settlement_time: str
    status: PaymentStatusEnumType
    custom_data: Optional[CustomDataType] = None
    receipt_id: Optional[str] = None
    receipt_url: Optional[str] = None
    status_info: Optional[str] = None
    transaction_id: Optional[str] = None
    vat_company: Optional[AddressType] = None
    vat_number: Optional[str] = None


@dataclass
class NotifyWebPaymentStarted:
    evse_id: int
    timeout: int
    custom_data: Optional[CustomDataType] = None


@dataclass
class OpenPeriodicEventStream:
    constant_stream_data: ConstantStreamDataType
    custom_data: Optional[CustomDataType] = None


@dataclass
class PublishFirmware:
    checksum: str
    location: str
    request_id: int
    custom_data: Optional[CustomDataType] = None
    retries: Optional[int] = None
    retry_interval: Optional[int] = None


@dataclass
class PublishFirmwareStatusNotification:
    status: PublishFirmwareStatusEnumType
    custom_data: Optional[CustomDataType] = None
    location: Optional[List[str]] = None
    request_id: Optional[int] = None
    status_info: Optional[StatusInfoType] = None


@dataclass
class PullDynamicScheduleUpdate:
    charging_profile_id: int
    custom_data: Optional[CustomDataType] = None


@dataclass
class ReportChargingProfiles:
    charging_limit_source: str
    charging_profile: List[ChargingProfileType]
    evse_id: int
    request_id: int
    custom_data: Optional[CustomDataType] = None
    tbc: bool = False


@dataclass
class ReportDERControl:
    request_id: int
    curve: Optional[List[DERCurveGetType]] = None
    custom_data: Optional[CustomDataType] = None
    enter_service: Optional[List[EnterServiceGetType]] = None
    fixed_pf_absorb: Optional[List[FixedPFGetType]] = None
    fixed_pf_inject: Optional[List[FixedPFGetType]] = None
    fixed_var: Optional[List[FixedVarGetType]] = None
    freq_droop: Optional[List[FreqDroopGetType]] = None
    gradient: Optional[List[GradientGetType]] = None
    limit_max_discharge: Optional[List[LimitMaxDischargeGetType]] = None
    tbc: Optional[bool] = None


@dataclass
class RequestBatterySwap:
    id_token: IdTokenType
    request_id: int
    custom_data: Optional[CustomDataType] = None


@dataclass
class RequestStartTransaction:
    id_token: IdTokenType
    remote_start_id: int
    charging_profile: Optional[ChargingProfileType] = None
    custom_data: Optional[CustomDataType] = None
    evse_id: Optional[int] = None
    group_id_token: Optional[IdTokenType] = None


@dataclass
class RequestStopTransaction:
    transaction_id: str
    custom_data: Optional[CustomDataType] = None


@dataclass
class ReservationStatusUpdate:
    reservation_id: int
    reservation_update_status: ReservationUpdateStatusEnumType
    custom_data: Optional[CustomDataType] = None


@dataclass
class ReserveNow:
    expiry_date_time: str
    id: int
    id_token: IdTokenType
    connector_type: Optional[str] = None
    custom_data: Optional[CustomDataType] = None
    evse_id: Optional[int] = None
    group_id_token: Optional[IdTokenType] = None


@dataclass
class Reset:
    type: ResetEnumType
    custom_data: Optional[CustomDataType] = None
    evse_id: Optional[int] = None


@dataclass
class SecurityEventNotification:
    timestamp: str
    type: str
    custom_data: Optional[CustomDataType] = None
    tech_info: Optional[str] = None


@dataclass
class SendLocalList:
    update_type: UpdateEnumType
    version_number: int
    custom_data: Optional[CustomDataType] = None
    local_authorization_list: Optional[List[AuthorizationData]] = None


@dataclass
class SetChargingProfile:
    charging_profile: ChargingProfileType
    evse_id: int
    custom_data: Optional[CustomDataType] = None


@dataclass
class SetDERControl:
    control_id: str
    control_type: DERControlEnumType
    is_default: bool
    curve: Optional[DERCurveType] = None
    custom_data: Optional[CustomDataType] = None
    enter_service: Optional[EnterServiceType] = None
    fixed_pf_absorb: Optional[FixedPFType] = None
    fixed_pf_inject: Optional[FixedPFType] = None
    fixed_var: Optional[FixedVarType] = None
    freq_droop: Optional[FreqDroopType] = None
    gradient: Optional[GradientType] = None
    limit_max_discharge: Optional[LimitMaxDischargeType] = None


@dataclass
class SetDefaultTariff:
    evse_id: int
    tariff: TariffType
    custom_data: Optional[CustomDataType] = None


@dataclass
class SetDisplayMessage:
    message: MessageInfoType
    custom_data: Optional[CustomDataType] = None


@dataclass
class SetMonitoringBase:
    monitoring_base: MonitoringBaseEnumType
    custom_data: Optional[CustomDataType] = None


@dataclass
class SetMonitoringLevel:
    severity: int
    custom_data: Optional[CustomDataType] = None


@dataclass
class SetNetworkProfile:
    configuration_slot: int
    connection_data: NetworkConnectionProfileType
    custom_data: Optional[CustomDataType] = None


@dataclass
class SetVariableMonitoring:
    set_monitoring_data: List[SetMonitoringDataType]
    custom_data: Optional[CustomDataType] = None


@dataclass
class SetVariables:
    set_variable_data: List[SetVariableDataType]
    custom_data: Optional[CustomDataType] = None


@dataclass
class SignCertificate:
    csr: str
    certificate_type: Optional[CertificateSigningUseEnumType] = None
    custom_data: Optional[CustomDataType] = None
    hash_root_certificate: Optional[CertificateHashDataType] = None
    request_id: Optional[int] = None


@dataclass
class StatusNotification:
    connector_id: int
    connector_status: ConnectorStatusEnumType
    evse_id: int
    timestamp: str
    custom_data: Optional[CustomDataType] = None


@dataclass
class TransactionEvent:
    event_type: TransactionEventEnumType
    seq_no: int
    timestamp: str
    transaction_info: TransactionType
    trigger_reason: TriggerReasonEnumType
    cable_max_current: Optional[int] = None
    cost_details: Optional[CostDetailsType] = None
    custom_data: Optional[CustomDataType] = None
    evse: Optional[EVSEType] = None
    evse_sleep: Optional[bool] = None
    id_token: Optional[IdTokenType] = None
    meter_value: Optional[List[MeterValueType]] = None
    number_of_phases_used: Optional[int] = None
    offline: bool = False
    preconditioning_status: Optional[PreconditioningStatusEnumType] = None
    reservation_id: Optional[int] = None


@dataclass
class TriggerMessage:
    requested_message: MessageTriggerEnumType
    custom_data: Optional[CustomDataType] = None
    custom_trigger: Optional[str] = None
    evse: Optional[EVSEType] = None


@dataclass
class UnlockConnector:
    connector_id: int
    evse_id: int
    custom_data: Optional[CustomDataType] = None


@dataclass
class UnpublishFirmware:
    checksum: str
    custom_data: Optional[CustomDataType] = None


@dataclass
class UpdateDynamicSchedule:
    charging_profile_id: int
    schedule_update: ChargingScheduleUpdateType
    custom_data: Optional[CustomDataType] = None


@dataclass
class UpdateFirmware:
    firmware: FirmwareType
    request_id: int
    custom_data: Optional[CustomDataType] = None
    retries: Optional[int] = None
    retry_interval: Optional[int] = None


@dataclass
class UsePriorityCharging:
    activate: bool
    transaction_id: str
    custom_data: Optional[CustomDataType] = None


@dataclass
class VatNumberValidation:
    vat_number: str
    custom_data: Optional[CustomDataType] = None
    evse_id: Optional[int] = None
