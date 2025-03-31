from dataclasses import dataclass
from datetime import datetime
from typing import List, Optional

from ocpp.v21.datatypes import (
    CertificateHashDataChain,
    CertificateStatus,
    ClearMonitoringResult,
    ClearTariffsResult,
    CompositeSchedule,
    ConstantStreamData,
    CustomData,
    IdTokenInfo,
    StatusInfo,
)
from ocpp.v21.enums import (
    AuthorizeCertificateStatusEnum,
    CancelReservationStatusEnum,
    CertificateSignedStatusEnum,
    ChangeAvailabilityStatusEnum,
    ClearCacheStatusEnum,
    ClearChargingProfileStatusEnum,
    ClearMessageStatusEnum,
    CustomerInformationStatusEnum,
    DataTransferStatusEnum,
    DeleteCertificateStatusEnum,
    DERControlStatusEnum,
    GenericDeviceModelStatusEnum,
    GenericStatusEnum,
    GetCertificateStatusEnum,
    GetChargingProfileStatusEnum,
    GetDisplayMessagesStatusEnum,
    GetInstalledCertificateStatusEnum,
    Iso15118EVCertificateStatusEnum,
    LogStatusEnumType,
    RegistrationStatusEnum,
    TariffChangeStatusEnum,
)


@dataclass
class NotifySettlementResponse:
    """
    OCPP 2.1 NotifySettlementResponse message.
    """

    receipt_url: Optional[str] = None
    receipt_id: Optional[str] = None
    custom_data: Optional[CustomData] = None


@dataclass
class AuthorizeResponse:
    """
    OCPP 2.1 AuthorizeResponse message.
    """

    id_token_info: IdTokenInfo
    certificate_status: Optional[AuthorizeCertificateStatusEnum] = None
    custom_data: Optional[CustomData] = None


@dataclass
class BootNotificationResponse:
    """
    OCPP 2.1 BootNotificationResponse message.
    """

    current_time: datetime
    interval: int
    status: RegistrationStatusEnum
    status_info: Optional[StatusInfo] = None
    custom_data: Optional[CustomData] = None


@dataclass
class CancelReservationResponse:
    """
    OCPP 2.1 CancelReservationResponse message.
    """

    status: CancelReservationStatusEnum
    status_info: Optional[StatusInfo] = None
    custom_data: Optional[CustomData] = None


@dataclass
class CertificateSignedResponse:
    """
    OCPP 2.1 CertificateSignedResponse message.
    """

    status: CertificateSignedStatusEnum
    status_info: Optional[StatusInfo] = None
    custom_data: Optional[CustomData] = None


@dataclass
class AdjustPeriodicEventStreamResponse:
    """
    OCPP 2.1 AdjustPeriodicEventStreamResponse message.
    """

    status: GenericStatusEnum
    status_info: Optional[StatusInfo] = None
    custom_data: Optional[CustomData] = None


@dataclass
class AFRRSignalResponse:
    """
    OCPP 2.1 AFRRSignalResponse message.
    """

    status: GenericStatusEnum
    status_info: Optional[StatusInfo] = None
    custom_data: Optional[CustomData] = None


@dataclass
class BatterySwapResponse:
    """
    OCPP 2.1 BatterySwapResponse message.
    This is an empty response that just acknowledges receipt of the request. (The request cannot be rejected).
    """

    custom_data: Optional[CustomData] = None


@dataclass
class ChangeAvailabilityResponse:
    """
    OCPP 2.1 ChangeAvailabilityResponse message.
    """

    status: ChangeAvailabilityStatusEnum
    status_info: Optional[StatusInfo] = None
    custom_data: Optional[CustomData] = None


@dataclass
class ChangeTransactionTariffResponse:
    """
    OCPP 2.1 ChangeTransactionTariffResponse message.
    """

    status: TariffChangeStatusEnum
    status_info: Optional[StatusInfo] = None
    custom_data: Optional[CustomData] = None


@dataclass
class ClearCacheResponse:
    """
    OCPP 2.1 ClearCacheResponse message.
    """

    status: ClearCacheStatusEnum
    status_info: Optional[StatusInfo] = None
    custom_data: Optional[CustomData] = None


@dataclass
class ClearDisplayMessageResponse:
    """
    OCPP 2.1 ClearDisplayMessageResponse message.
    """

    status: ClearMessageStatusEnum
    status_info: Optional[StatusInfo] = None
    custom_data: Optional[CustomData] = None


@dataclass
class ClearChargingProfileResponse:
    """
    OCPP 2.1 ClearChargingProfileResponse message.
    """

    status: ClearChargingProfileStatusEnum
    status_info: Optional[StatusInfo] = None
    custom_data: Optional[CustomData] = None


@dataclass
class ClearDERControlResponse:
    """
    OCPP 2.1 ClearDERControlResponse message.
    """

    status: DERControlStatusEnum
    status_info: Optional[StatusInfo] = None
    custom_data: Optional[CustomData] = None


@dataclass
class ClearedChargingLimitResponse:
    """
    OCPP 2.1 ClearedChargingLimitResponse message.
    """

    custom_data: Optional[CustomData] = None


@dataclass
class ClearTariffsResponse:
    """
    OCPP 2.1 ClearTariffsResponse message.
    """

    clear_tariffs_result: List[ClearTariffsResult]
    custom_data: Optional[CustomData] = None


@dataclass
class ClearVariableMonitoringResponse:
    """
    OCPP 2.1 ClearVariableMonitoringResponse message.
    """

    clear_monitoring_result: List[ClearMonitoringResult]
    custom_data: Optional[CustomData] = None


@dataclass
class ClosePeriodicEventStreamResponse:
    """
    OCPP 2.1 ClosePeriodicEventStreamResponse message.
    """

    custom_data: Optional[CustomData] = None


@dataclass
class CostUpdatedResponse:
    """
    OCPP 2.1 CostUpdatedResponse message.
    """

    custom_data: Optional[CustomData] = None


@dataclass
class CustomerInformationResponse:
    """
    OCPP 2.1 CustomerInformationResponse message.
    """

    status: CustomerInformationStatusEnum
    status_info: Optional[StatusInfo] = None
    custom_data: Optional[CustomData] = None


@dataclass
class DataTransferResponse:
    """
    OCPP 2.1 DataTransferResponse message.
    """

    status: DataTransferStatusEnum
    data: Optional[dict] = None
    status_info: Optional[StatusInfo] = None
    custom_data: Optional[CustomData] = None


@dataclass
class DeleteCertificateResponse:
    """
    OCPP 2.1 DeleteCertificateResponse message.
    """

    status: DeleteCertificateStatusEnum
    status_info: Optional[StatusInfo] = None
    custom_data: Optional[CustomData] = None


@dataclass
class FirmwareStatusNotificationResponse:
    """
    OCPP 2.1 FirmwareStatusNotificationResponse message.
    """

    custom_data: Optional[CustomData] = None


@dataclass
class Get15118EVCertificateResponse:
    """
    OCPP 2.1 Get15118EVCertificateResponse message.
    """

    status: Iso15118EVCertificateStatusEnum
    exi_response: str
    status_info: Optional[StatusInfo] = None
    remaining_contracts: Optional[int] = None
    custom_data: Optional[CustomData] = None


@dataclass
class GetBaseReportResponse:
    """
    OCPP 2.1 GetBaseReportResponse message.
    """

    status: GenericDeviceModelStatusEnum
    status_info: Optional[StatusInfo] = None
    custom_data: Optional[CustomData] = None


@dataclass
class GetCertificateChainStatusResponse:
    """
    OCPP 2.1 GetCertificateChainStatusResponse message.
    """

    certificate_status: List[CertificateStatus]
    custom_data: Optional[CustomData] = None


@dataclass
class GetCertificateStatusResponse:
    """
    OCPP 2.1 GetCertificateStatusResponse message.
    """

    status: GetCertificateStatusEnum
    ocsp_result: Optional[str] = None
    status_info: Optional[StatusInfo] = None
    custom_data: Optional[CustomData] = None


@dataclass
class GetChargingProfilesResponse:
    """
    OCPP 2.1 GetChargingProfilesResponse message.
    """

    status: GetChargingProfileStatusEnum
    status_info: Optional[StatusInfo] = None
    custom_data: Optional[CustomData] = None


@dataclass
class GetCompositeScheduleResponse:
    """
    OCPP 2.1 GetCompositeScheduleResponse message.
    """

    status: GenericStatusEnum
    schedule: Optional[CompositeSchedule] = None
    status_info: Optional[StatusInfo] = None
    custom_data: Optional[CustomData] = None


@dataclass
class GetInstalledCertificateIdsResponse:
    """
    OCPP 2.1 GetInstalledCertificateIdsResponse message.
    """

    status: GetInstalledCertificateStatusEnum
    certificate_hash_data_chain: Optional[List[CertificateHashDataChain]] = None
    status_info: Optional[StatusInfo] = None
    custom_data: Optional[CustomData] = None


@dataclass
class GetDERControlResponse:
    """
    OCPP 2.1 GetDERControlResponse message.
    """

    status: DERControlStatusEnum
    status_info: Optional[StatusInfo] = None
    custom_data: Optional[CustomData] = None


@dataclass
class GetDisplayMessagesResponse:
    """
    OCPP 2.1 GetDisplayMessagesResponse message.
    """

    status: GetDisplayMessagesStatusEnum
    status_info: Optional[StatusInfo] = None
    custom_data: Optional[CustomData] = None


@dataclass
class GetLocalListVersionResponse:
    """
    OCPP 2.1 GetLocalListVersionResponse message.
    """

    version_number: int
    custom_data: Optional[CustomData] = None


@dataclass
class GetLogResponse:
    """
    OCPP 2.1 GetLogResponse message.
    """

    status: LogStatusEnumType
    status_info: Optional[StatusInfo] = None
    filename: Optional[str] = None
    custom_data: Optional[CustomData] = None


@dataclass
class GetMonitoringReportResponse:
    """
    OCPP 2.1 GetMonitoringReportResponse message.
    """

    status: GenericDeviceModelStatusEnum
    status_info: Optional[StatusInfo] = None
    custom_data: Optional[CustomData] = None


@dataclass
class GetReportResponse:
    """
    OCPP 2.1 GetReportResponse message.
    """

    status: GenericDeviceModelStatusEnum
    status_info: Optional[StatusInfo] = None
    custom_data: Optional[CustomData] = None


@dataclass
class GetPeriodicEventStreamResponse:
    """
    OCPP 2.1 GetPeriodicEventStreamResponse message.
    """

    constant_stream_data: Optional[List[ConstantStreamData]] = None
    custom_data: Optional[CustomData] = None
