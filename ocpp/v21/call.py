from dataclasses import dataclass
from typing import Any, List, Optional

import enums
from datatypes import (
    EVSE,
    AuthorizationData,
    CertificateHashData,
    ChargingLimit,
    ChargingNeeds,
    ChargingProfile,
    ChargingProfileCriteria,
    ChargingSchedule,
    ChargingStation,
    ComponentVariable,
    ConnectionData,
    CustomData,
    CustomerCertificate,
    EventData,
    Firmware,
    GetVariableData,
    GroupIdToken,
    IdToken,
    Log,
    Message,
    MessageInfo,
    MeterValue,
    MonitoringData,
    OCSPRequestData,
    ReportData,
    SetMonitoringData,
    SetVariableData,
    TransactionInfo,
)
from enums import (
    BootReason,
    CertificateAction,
    CertificateSigningUse,
    ChargingLimitSource,
    ChargingRateUnit,
    ComponentCriterion,
    Connector,
    ConnectorStatus,
    EnergyTransferMode,
    FirmwareStatus,
    GetCertificateIdUse,
    InstallCertificateUse,
    Log,
    MessagePriority,
    MessageState,
    MessageTrigger,
    MonitoringBase,
    MonitoringCriterion,
    NotifyCRLStatus,
    OperationalStatus,
    PreconditioningStatus,
    PublishFirmwareStatus,
    ReportBase,
    ReservationUpdateStatus,
    TriggerReason,
    Update,
    UploadLogStatus,
)


@dataclass
class AFRRSignal:
    signal: int
    timestamp: str
    custom_data: Optional[CustomData] = None


@dataclass
class Authorize:
    id_token: IdToken
    certificate: Optional[str] = None
    custom_data: Optional[CustomData] = None
    iso_15118_certificate_hash_data: Optional[List[OCSPRequestData]] = None


@dataclass
class BootNotification:
    charging_station: ChargingStation
    reason: BootReason
    custom_data: Optional[CustomData] = None


@dataclass
class CancelReservation:
    reservation_id: int
    custom_data: Optional[CustomData] = None


@dataclass
class CertificateSigned:
    certificate_chain: str
    certificate_type: Optional[CertificateSigningUse] = None
    custom_data: Optional[CustomData] = None


@dataclass
class ChangeAvailability:
    operational_status: OperationalStatus
    custom_data: Optional[CustomData] = None
    evse: Optional[EVSE] = None


@dataclass
class ClearCache:
    custom_data: Optional[CustomData] = None


@dataclass
class ClearChargingProfile:
    charging_profile_criteria: Optional[ChargingProfileCriteria] = None
    charging_profile_id: Optional[int] = None
    custom_data: Optional[CustomData] = None


@dataclass
class ClearDisplayMessage:
    id: int
    custom_data: Optional[CustomData] = None


@dataclass
class ClearVariableMonitoring:
    id: List[int]
    custom_data: Optional[CustomData] = None


@dataclass
class ClearedChargingLimit:
    charging_limit_source: ChargingLimitSource
    custom_data: Optional[CustomData] = None
    evse_id: Optional[int] = None


@dataclass
class CostUpdated:
    total_cost: float
    transaction_id: str
    custom_data: Optional[CustomData] = None


@dataclass
class CustomerInformation:
    clear: bool
    report: bool
    request_id: int
    custom_data: Optional[CustomData] = None
    customer_certificate: Optional[CustomerCertificate] = None
    customer_identifier: Optional[str] = None
    id_token: Optional[IdToken] = None


@dataclass
class DataTransfer:
    vendor_id: str
    custom_data: Optional[CustomData] = None
    data: Any = None
    message_id: Optional[str] = None


@dataclass
class DeleteCertificate:
    certificate_hash_data: CertificateHashData
    custom_data: Optional[CustomData] = None


@dataclass
class FirmwareStatusNotification:
    status: FirmwareStatus
    custom_data: Optional[CustomData] = None
    request_id: Optional[int] = None


@dataclass
class Get15118EVCertificate:
    action: CertificateAction
    exi_request: str
    iso_15118_schema_version: str
    custom_data: Optional[CustomData] = None
    maximum_contract_certificate_chains: Optional[int] = None
    prioritized_emaids: Optional[List[str]] = None


@dataclass
class GetBaseReport:
    report_base: ReportBase
    request_id: int
    custom_data: Optional[CustomData] = None


@dataclass
class GetCRL:
    certificate_hash_data: CertificateHashData
    request_id: int
    custom_data: Optional[CustomData] = None


@dataclass
class GetCertificateStatus:
    ocsp_request_data: OCSPRequestData
    custom_data: Optional[CustomData] = None


@dataclass
class GetChargingProfiles:
    charging_profile: ChargingProfile
    request_id: int
    custom_data: Optional[CustomData] = None
    evse_id: Optional[int] = None


@dataclass
class GetCompositeSchedule:
    duration: int
    evse_id: int
    charging_rate_unit: Optional[ChargingRateUnit] = None
    custom_data: Optional[CustomData] = None


@dataclass
class GetDisplayMessages:
    request_id: int
    custom_data: Optional[CustomData] = None
    id: Optional[List[int]] = None
    priority: Optional[MessagePriority] = None
    state: Optional[MessageState] = None


@dataclass
class GetInstalledCertificateIds:
    certificate_type: Optional[List[GetCertificateIdUse]] = None
    custom_data: Optional[CustomData] = None


@dataclass
class GetLocalListVersion:
    custom_data: Optional[CustomData] = None


@dataclass
class GetLog:
    log: Log
    log_type: Log
    request_id: int
    custom_data: Optional[CustomData] = None
    retries: Optional[int] = None
    retry_interval: Optional[int] = None


@dataclass
class GetMonitoringReport:
    request_id: int
    component_variable: Optional[List[ComponentVariable]] = None
    custom_data: Optional[CustomData] = None
    monitoring_criteria: Optional[List[MonitoringCriterion]] = None


@dataclass
class GetReport:
    request_id: int
    component_criteria: Optional[List[ComponentCriterion]] = None
    component_variable: Optional[List[ComponentVariable]] = None
    custom_data: Optional[CustomData] = None


@dataclass
class GetTransactionStatus:
    custom_data: Optional[CustomData] = None
    transaction_id: Optional[str] = None


@dataclass
class GetVariables:
    get_variable_data: List[GetVariableData]
    custom_data: Optional[CustomData] = None


@dataclass
class Heartbeat:
    custom_data: Optional[CustomData] = None


@dataclass
class InstallCertificate:
    certificate: str
    certificate_type: InstallCertificateUse
    custom_data: Optional[CustomData] = None


@dataclass
class LogStatusNotification:
    status: UploadLogStatus
    custom_data: Optional[CustomData] = None
    request_id: Optional[int] = None


@dataclass
class MeterValues:
    evse_id: int
    meter_value: List[MeterValue]
    custom_data: Optional[CustomData] = None


@dataclass
class NotifyAllowedEnergyTransfer:
    allowed_energy_transfer: List[EnergyTransferMode]
    custom_data: Optional[CustomData] = None


@dataclass
class NotifyCRL:
    request_id: int
    status: NotifyCRLStatus
    custom_data: Optional[CustomData] = None
    location: Optional[str] = None


@dataclass
class NotifyChargingLimit:
    charging_limit: ChargingLimit
    charging_schedule: Optional[List[ChargingSchedule]] = None
    custom_data: Optional[CustomData] = None
    evse_id: Optional[int] = None


@dataclass
class NotifyCustomerInformation:
    data: str
    generated_at: str
    request_id: int
    seq_no: int
    custom_data: Optional[CustomData] = None
    tbc: bool = False


@dataclass
class NotifyDisplayMessages:
    request_id: int
    custom_data: Optional[CustomData] = None
    message_info: Optional[List[MessageInfo]] = None
    tbc: bool = False


@dataclass
class NotifyEVChargingNeeds:
    charging_needs: ChargingNeeds
    evse_id: int
    custom_data: Optional[CustomData] = None
    max_schedule_tuples: Optional[int] = None


@dataclass
class NotifyEVChargingSchedule:
    charging_schedule: ChargingSchedule
    evse_id: int
    time_base: str
    custom_data: Optional[CustomData] = None
    power_tolerance_acceptance: Optional[bool] = None
    selected_schedule_tuple_id: Optional[int] = None


@dataclass
class NotifyEvent:
    event_data: List[EventData]
    generated_at: str
    seq_no: int
    custom_data: Optional[CustomData] = None
    tbc: bool = False


@dataclass
class NotifyMonitoringReport:
    generated_at: str
    request_id: int
    seq_no: int
    custom_data: Optional[CustomData] = None
    monitor: Optional[List[MonitoringData]] = None
    tbc: bool = False


@dataclass
class NotifyPriorityCharging:
    activated: bool
    transaction_id: str
    custom_data: Optional[CustomData] = None


@dataclass
class NotifyReport:
    generated_at: str
    request_id: int
    seq_no: int
    custom_data: Optional[CustomData] = None
    report_data: Optional[List[ReportData]] = None
    tbc: bool = False


@dataclass
class PublishFirmware:
    checksum: str
    location: str
    request_id: int
    custom_data: Optional[CustomData] = None
    retries: Optional[int] = None
    retry_interval: Optional[int] = None


@dataclass
class PublishFirmwareStatusNotification:
    status: PublishFirmwareStatus
    custom_data: Optional[CustomData] = None
    location: Optional[List[str]] = None
    request_id: Optional[int] = None


@dataclass
class PullDynamicScheduleUpdate:
    charging_profile_id: int
    custom_data: Optional[CustomData] = None


@dataclass
class ReportChargingProfiles:
    charging_limit_source: ChargingLimitSource
    charging_profile: List[ChargingProfile]
    evse_id: int
    request_id: int
    custom_data: Optional[CustomData] = None
    tbc: bool = False


@dataclass
class RequestStartTransaction:
    id_token: IdToken
    remote_start_id: int
    charging_profile: Optional[ChargingProfile] = None
    custom_data: Optional[CustomData] = None
    evse_id: Optional[int] = None
    group_id_token: Optional[GroupIdToken] = None


@dataclass
class RequestStopTransaction:
    transaction_id: str
    custom_data: Optional[CustomData] = None


@dataclass
class ReservationStatusUpdate:
    reservation_id: int
    reservation_update_status: ReservationUpdateStatus
    custom_data: Optional[CustomData] = None


@dataclass
class ReserveNow:
    expiry_date_time: str
    id: int
    id_token: IdToken
    connector_type: Optional[Connector] = None
    custom_data: Optional[CustomData] = None
    evse_id: Optional[int] = None
    group_id_token: Optional[GroupIdToken] = None


@dataclass
class Reset:
    type: enums.Reset
    custom_data: Optional[CustomData] = None
    evse_id: Optional[int] = None


@dataclass
class SecurityEventNotification:
    timestamp: str
    type: str
    custom_data: Optional[CustomData] = None
    tech_info: Optional[str] = None


@dataclass
class SendLocalList:
    update_type: Update
    version_number: int
    custom_data: Optional[CustomData] = None
    local_authorization_list: Optional[List[AuthorizationData]] = None


@dataclass
class SetChargingProfile:
    charging_profile: ChargingProfile
    evse_id: int
    custom_data: Optional[CustomData] = None


@dataclass
class SetDisplayMessage:
    message: Message
    custom_data: Optional[CustomData] = None


@dataclass
class SetMonitoringBase:
    monitoring_base: MonitoringBase
    custom_data: Optional[CustomData] = None


@dataclass
class SetMonitoringLevel:
    severity: int
    custom_data: Optional[CustomData] = None


@dataclass
class SetNetworkProfile:
    configuration_slot: int
    connection_data: ConnectionData
    custom_data: Optional[CustomData] = None


@dataclass
class SetVariableMonitoring:
    set_monitoring_data: List[SetMonitoringData]
    custom_data: Optional[CustomData] = None


@dataclass
class SetVariables:
    set_variable_data: List[SetVariableData]
    custom_data: Optional[CustomData] = None


@dataclass
class SignCertificate:
    csr: str
    certificate_type: Optional[CertificateSigningUse] = None
    custom_data: Optional[CustomData] = None


@dataclass
class StatusNotification:
    connector_id: int
    connector_status: ConnectorStatus
    evse_id: int
    timestamp: str
    custom_data: Optional[CustomData] = None


@dataclass
class TransactionEvent:
    event_type: enums.TransactionEvent
    seq_no: int
    timestamp: str
    transaction_info: TransactionInfo
    trigger_reason: TriggerReason
    cable_max_current: Optional[float] = None
    custom_data: Optional[CustomData] = None
    evse: Optional[EVSE] = None
    id_token: Optional[IdToken] = None
    meter_value: Optional[List[MeterValue]] = None
    number_of_phases_used: Optional[int] = None
    offline: bool = False
    preconditioning_status: Optional[PreconditioningStatus] = None
    reservation_id: Optional[int] = None


@dataclass
class TriggerMessage:
    requested_message: MessageTrigger
    custom_data: Optional[CustomData] = None
    evse: Optional[EVSE] = None


@dataclass
class UnlockConnector:
    connector_id: int
    evse_id: int
    custom_data: Optional[CustomData] = None


@dataclass
class UnpublishFirmware:
    checksum: str
    custom_data: Optional[CustomData] = None


@dataclass
class UpdateDynamicSchedule:
    charging_profile_id: int
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
class UpdateFirmware:
    firmware: Firmware
    request_id: int
    custom_data: Optional[CustomData] = None
    retries: Optional[int] = None
    retry_interval: Optional[int] = None


@dataclass
class UsePriorityCharging:
    activate: bool
    transaction_id: str
    custom_data: Optional[CustomData] = None
