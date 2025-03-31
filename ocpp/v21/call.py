from dataclasses import dataclass
from datetime import datetime
from typing import List, Optional

from ocpp.v21.datatypes import (
    EVSE,
    Address,
    BatteryData,
    CertificateHashData,
    CertificateStatusRequestInfo,
    ChargingProfileCriterion,
    ChargingStation,
    ClearChargingProfile,
    ComponentVariable,
    CustomData,
    IdToken,
    LogParameters,
    OCSPRequestData,
    PeriodicEventStreamParams,
    StatusInfo,
    Tariff,
)
from ocpp.v21.enums import (
    BatterySwapEventEnum,
    BootReasonEnum,
    CertificateActionEnum,
    CertificateSigningUseEnum,
    ChargingLimitSourceEnum,
    ChargingRateUnitEnum,
    ComponentCriterionEnum,
    DERControlEnum,
    FirmwareStatusEnum,
    GetCertificateIdUseEnum,
    LogEnumType,
    MessagePriorityEnum,
    MessageStateEnum,
    MonitoringCriterionEnum,
    OperationalStatusEnum,
    PaymentStatusEnum,
    ReportBaseEnum,
)


@dataclass
class NotifySettlementRequest:
    """
    OCPP 2.1 NotifySettlementRequest message.
    """

    psp_ref: str
    status: PaymentStatusEnum
    settlement_amount: float
    settlement_time: datetime
    transaction_id: Optional[str] = None
    status_info: Optional[str] = None
    receipt_id: Optional[str] = None
    receipt_url: Optional[str] = None
    vat_company: Optional[Address] = None
    vat_number: Optional[str] = None
    custom_data: Optional[CustomData] = None


@dataclass
class AuthorizeRequest:
    """
    OCPP 2.1 AuthorizeRequest message.
    """

    id_token: IdToken
    certificate: Optional[str] = None
    iso15118_certificate_hash_data: Optional[List[OCSPRequestData]] = None
    custom_data: Optional[CustomData] = None


@dataclass
class BootNotificationRequest:
    """
    OCPP 2.1 BootNotificationRequest message.
    """

    charging_station: ChargingStation
    reason: BootReasonEnum
    custom_data: Optional[CustomData] = None


@dataclass
class CancelReservationRequest:
    """
    OCPP 2.1 CancelReservationRequest message.
    """

    reservation_id: int
    custom_data: Optional[CustomData] = None


@dataclass
class CertificateSignedRequest:
    """
    OCPP 2.1 CertificateSignedRequest message.
    """

    certificate_chain: str
    certificate_type: Optional[CertificateSigningUseEnum] = None
    request_id: Optional[int] = None
    custom_data: Optional[CustomData] = None


@dataclass
class AdjustPeriodicEventStreamRequest:
    """
    OCPP 2.1 AdjustPeriodicEventStreamRequest message.
    """

    id: int
    params: PeriodicEventStreamParams
    custom_data: Optional[CustomData] = None


@dataclass
class AFRRSignalRequest:
    """
    OCPP 2.1 AFRRSignalRequest message.
    """

    timestamp: datetime
    signal: int
    custom_data: Optional[CustomData] = None


@dataclass
class BatterySwapRequest:
    """
    OCPP 2.1 BatterySwapRequest message.
    """

    battery_data: List[BatteryData]
    event_type: BatterySwapEventEnum
    id_token: IdToken
    request_id: int
    custom_data: Optional[CustomData] = None


@dataclass
class ChangeAvailabilityRequest:
    """
    OCPP 2.1 ChangeAvailabilityRequest message.
    """

    operational_status: OperationalStatusEnum
    evse: Optional[EVSE] = None
    custom_data: Optional[CustomData] = None


@dataclass
class ChangeTransactionTariffRequest:
    """
    OCPP 2.1 ChangeTransactionTariffRequest message.
    """

    tariff: Tariff
    transaction_id: str
    custom_data: Optional[CustomData] = None


@dataclass
class ClearCacheRequest:
    """
    OCPP 2.1 ClearCacheRequest message.
    """

    custom_data: Optional[CustomData] = None


@dataclass
class ClearDisplayMessageRequest:
    """
    OCPP 2.1 ClearDisplayMessageRequest message.
    """

    id: int
    custom_data: Optional[CustomData] = None


@dataclass
class ClearChargingProfileRequest:
    """
    OCPP 2.1 ClearChargingProfileRequest message.
    """

    charging_profile_id: Optional[int] = None
    charging_profile_criteria: Optional[ClearChargingProfile] = None
    custom_data: Optional[CustomData] = None


@dataclass
class ClearDERControlRequest:
    """
    OCPP 2.1 ClearDERControlRequest message.
    """

    is_default: bool
    control_type: Optional[DERControlEnum] = None
    control_id: Optional[str] = None
    custom_data: Optional[CustomData] = None


@dataclass
class ClearedChargingLimitRequest:
    """
    OCPP 2.1 ClearedChargingLimitRequest message.
    """

    charging_limit_source: ChargingLimitSourceEnum
    evse_id: Optional[int] = None
    custom_data: Optional[CustomData] = None


@dataclass
class ClearTariffsRequest:
    """
    OCPP 2.1 ClearTariffsRequest message.
    """

    tariff_ids: Optional[List[str]] = None
    evse_id: Optional[int] = None
    custom_data: Optional[CustomData] = None


@dataclass
class ClearVariableMonitoringRequest:
    """
    OCPP 2.1 ClearVariableMonitoringRequest message.
    """

    id: List[int]
    custom_data: Optional[CustomData] = None


@dataclass
class ClosePeriodicEventStreamRequest:
    """
    OCPP 2.1 ClosePeriodicEventStreamRequest message.
    """

    id: int
    custom_data: Optional[CustomData] = None


@dataclass
class CostUpdatedRequest:
    """
    OCPP 2.1 CostUpdatedRequest message.
    """

    total_cost: float
    transaction_id: str
    custom_data: Optional[CustomData] = None


@dataclass
class CustomerInformationRequest:
    """
    OCPP 2.1 CustomerInformationRequest message.
    """

    request_id: int
    report: bool
    clear: bool
    customer_certificate: Optional[CertificateHashData] = None
    id_token: Optional[IdToken] = None
    customer_identifier: Optional[str] = None
    custom_data: Optional[CustomData] = None


@dataclass
class DataTransferRequest:
    """
    OCPP 2.1 DataTransferRequest message.
    """

    vendor_id: str
    message_id: Optional[str] = None
    data: Optional[dict] = None
    custom_data: Optional[CustomData] = None


@dataclass
class DeleteCertificateRequest:
    """
    OCPP 2.1 DeleteCertificateRequest message.
    """

    certificate_hash_data: CertificateHashData
    custom_data: Optional[CustomData] = None


@dataclass
class FirmwareStatusNotificationRequest:
    """
    OCPP 2.1 FirmwareStatusNotificationRequest message.
    """

    status: FirmwareStatusEnum
    request_id: Optional[int] = None
    status_info: Optional[StatusInfo] = None
    custom_data: Optional[CustomData] = None


@dataclass
class Get15118EVCertificateRequest:
    """
    OCPP 2.1 Get15118EVCertificateRequest message.
    """

    iso15118_schema_version: str
    action: CertificateActionEnum
    exi_request: str
    maximum_contract_certificate_chains: Optional[int] = None
    prioritized_emaids: Optional[List[str]] = None
    custom_data: Optional[CustomData] = None


@dataclass
class GetBaseReportRequest:
    """
    OCPP 2.1 GetBaseReportRequest message.
    """

    request_id: int
    report_base: ReportBaseEnum
    custom_data: Optional[CustomData] = None


@dataclass
class GetCertificateChainStatusRequest:
    """
    OCPP 2.1 GetCertificateChainStatusRequest message.
    """

    certificate_status_requests: List[CertificateStatusRequestInfo]
    custom_data: Optional[CustomData] = None


@dataclass
class GetCertificateStatusRequest:
    """
    OCPP 2.1 GetCertificateStatusRequest message.
    """

    ocsp_request_data: OCSPRequestData
    custom_data: Optional[CustomData] = None


@dataclass
class GetChargingProfilesRequest:
    """
    OCPP 2.1 GetChargingProfilesRequest message.
    """

    request_id: int
    charging_profile: ChargingProfileCriterion
    evse_id: Optional[int] = None
    custom_data: Optional[CustomData] = None


@dataclass
class GetCompositeScheduleRequest:
    """
    OCPP 2.1 GetCompositeScheduleRequest message.
    """

    duration: int
    evse_id: int
    charging_rate_unit: Optional[ChargingRateUnitEnum] = None
    custom_data: Optional[CustomData] = None


@dataclass
class GetInstalledCertificateIdsRequest:
    """
    OCPP 2.1 GetInstalledCertificateIdsRequest message.
    """

    certificate_type: Optional[List[GetCertificateIdUseEnum]] = None
    custom_data: Optional[CustomData] = None


@dataclass
class GetDERControlRequest:
    """
    OCPP 2.1 GetDERControlRequest message.
    """

    request_id: int
    is_default: bool
    control_type: Optional[DERControlEnum] = None
    control_id: Optional[str] = None
    custom_data: Optional[CustomData] = None


@dataclass
class GetDisplayMessagesRequest:
    """
    OCPP 2.1 GetDisplayMessagesRequest message.
    """

    request_id: int
    id: Optional[List[int]] = None
    priority: Optional[MessagePriorityEnum] = None
    state: Optional[MessageStateEnum] = None
    custom_data: Optional[CustomData] = None


@dataclass
class GetLocalListVersionRequest:
    """
    OCPP 2.1 GetLocalListVersionRequest message.
    """

    custom_data: Optional[CustomData] = None


@dataclass
class GetLogRequest:
    """
    OCPP 2.1 GetLogRequest message.
    """

    log_type: LogEnumType
    request_id: int
    log: LogParameters
    retries: Optional[int] = None
    retry_interval: Optional[int] = None
    custom_data: Optional[CustomData] = None


@dataclass
class GetMonitoringReportRequest:
    """
    OCPP 2.1 GetMonitoringReportRequest message.
    """

    request_id: int
    component_variable: Optional[List[ComponentVariable]] = None
    monitoring_criteria: Optional[List[MonitoringCriterionEnum]] = None
    custom_data: Optional[CustomData] = None


@dataclass
class GetReportRequest:
    """
    OCPP 2.1 GetReportRequest message.
    """

    request_id: int
    component_variable: Optional[List[ComponentVariable]] = None
    component_criteria: Optional[List[ComponentCriterionEnum]] = None
    custom_data: Optional[CustomData] = None


@dataclass
class GetPeriodicEventStreamRequest:
    """
    OCPP 2.1 GetPeriodicEventStreamRequest message.
    This message is empty and has no fields except for an optional customData field.
    """

    custom_data: Optional[CustomData] = None
