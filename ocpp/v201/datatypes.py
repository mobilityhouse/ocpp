from dataclasses import dataclass
from typing import Optional

from ocpp.v201 import enums


@dataclass
class ACChargingParametersType:
    """
    EV AC charging parameters.
    ACChargingParametersType is used by: ChargingNeedsType
    """

    energy_amount: int
    ev_min_current: int
    ev_max_current: int
    ev_max_voltage: int


@dataclass
class AdditionalInfoType:
    """
    Contains a case insensitive identifier to use for the authorization and the
    type of authorization to support multiple forms of identifiers.
    AdditionalInfoType is used by: IdTokenType
    """

    additional_id_token: str
    type: str


@dataclass
class APNType:
    """
    Collection of configuration data needed to make a data-connection over a
    cellular network.
    APNType is used by: SetNetworkProfileRequest.NetworkConnectionProfileType
    """

    apn: str
    apn_authentication: enums.APNAuthenticationType
    apn_user_name: Optional[str] = None
    apn_password: Optional[str] = None
    sim_pin: Optional[int] = None
    preferred_network: Optional[str] = None
    use_only_preferred_network: Optional[bool] = None


@dataclass
class CertificateHashDataType:
    """
    CertificateHashDataType is used by: CertificateHashDataChainType,
    DeleteCertificateRequest, CustomerInformationRequest
    """

    hash_algorithm: enums.HashAlgorithmType
    issuer_name_hash: str
    issuer_key_hash: str
    serial_number: str


@dataclass
class CertificateHashDataChainType:
    """
    CertificateHashDataChainType is used by: GetInstalledCertificateIdsResponse
    """

    certificate_type: enums.GetCertificateIdUseType
    certificate_hash_data: CertificateHashDataType
    child_certificate_hash_data: CertificateHashDataType


@dataclass
class ChargingLimitType:
    """ChargingLimitType is used by: NotifyChargingLimitRequest"""

    charging_limit_source: enums.ChargingLimitSourceType
    is_grid_critical: Optional[bool] = None


@dataclass
class DCChargingParametersType:
    """
    EV DC charging parameters
    DCChargingParametersType is used by: ChargingNeedsType
    """

    ev_max_current: int
    ev_max_voltage: int
    energy_amount: Optional[int] = None
    ev_max_power: Optional[int] = None
    state_of_charge: Optional[int] = None
    ev_energy_capacity: Optional[int] = None
    full_soc: Optional[int] = None
    bulk_soc: Optional[int] = None


@dataclass
class ChargingNeedsType:
    """
    ChargingNeedsType is used by: NotifyEVChargingNeedsRequest
    """

    request_energy_transfer: enums.EnergyTransferModeType
    departure_time: Optional[str] = None
    ac_charging_parameters: Optional[ACChargingParametersType] = None
    dc_charging_parameters: Optional[DCChargingParametersType] = None


@dataclass
class ChargingProfileCriterionType:
    """
    A ChargingProfile consists of ChargingSchedule, describing the amount of
    power or current that can be delivered per time interval.
    ChargingProfileCriterionType is used by: GetChargingProfilesRequest
    """

    charging_profile_purpose: Optional[enums.ChargingProfilePurposeType] = None
    stack_level: Optional[int] = None
    charging_profile_id: Optional[int] = None
    charging_limit_source: Optional[enums.ChargingLimitSourceType] = None


@dataclass
class ChargingSchedulePeriodType:
    """
    Charging schedule period structure defines a time period in a charging
    schedule.
    ChargingSchedulePeriodType is used by: ChargingScheduleType,
    CompositeScheduleType
    """

    start_period: int
    limit: float
    number_phases: Optional[int] = None
    phase_to_use: Optional[int] = None


@dataclass
class RelativeTimeIntervalType:
    """RelativeTimeIntervalType is used by: SalesTariffEntryType"""

    start: int
    duration: Optional[int] = None


@dataclass
class CostType:
    """
    CostType is used by: ConsumptionCostType
    """

    cost_kind: enums.CostKindType
    amount: int
    amount_multiplier: Optional[int] = None


@dataclass
class ConsumptionCostType:
    """
    ConsumptionCostType is used by: SalesTariffEntryType
    """

    start_value: float
    cost: CostType


@dataclass
class SalesTariffEntryType:
    """SalesTariffEntryType is used by: SalesTariffType"""

    relative_time_interval: RelativeTimeIntervalType
    consumption_cost: Optional[ConsumptionCostType] = None
    e_price_level: Optional[int] = None


@dataclass
class SalesTariffType:
    """
    This dataType is based on dataTypes from ISO 15118-2.
    SalesTariffType is used by: ChargingScheduleType
    """

    id: int
    sales_tariff_entry: SalesTariffEntryType
    sales_tariff_description: Optional[str] = None
    num_e_price_levels: Optional[int] = None


@dataclass
class ChargingScheduleType:
    """
    Charging schedule structure defines a list of charging periods, as used in:
    GetCompositeSchedule.conf and ChargingProfile.
    ChargingScheduleType is used by: ChargingProfileType,
    NotifyChargingLimitRequest, NotifyEVChargingScheduleRequest
    """

    id: int
    charging_rate_unit: enums.ChargingRateUnitType
    charging_schedule_period: ChargingSchedulePeriodType
    start_schedule: Optional[str] = None
    duration: Optional[int] = None
    min_charging_rate: Optional[float] = None
    sales_tariff: Optional[SalesTariffType] = None


@dataclass
class ChargingProfileType:
    """
    A ChargingProfile consists of ChargingSchedule, describing the amount of
    power or current that can be delivered per time interval.
    ChargingProfileType is used by: RequestStartTransactionRequest,
    SetChargingProfileRequest, ReportChargingProfilesRequest
    """

    id: int
    stack_level: int
    charging_profile_purpose: enums.ChargingProfilePurposeType
    charging_profile_kind: enums.ChargingProfileKindType
    charging_schedule: ChargingScheduleType
    valid_from: Optional[str] = None
    valid_to: Optional[str] = None
    transaction_id: Optional[str] = None
    recurrency_kind: Optional[enums.RecurrencyKindType] = None


@dataclass
class ClearChargingProfileType:
    """
    A ChargingProfile consists of a ChargingSchedule, describing the amount of
    power or current that can be delivered per time interval.
    ClearChargingProfileType is used by: ClearChargingProfileRequest
    """

    evse_id: Optional[int] = None
    charging_profile_purpose: Optional[enums.ChargingProfilePurposeType] = None
    stack_level: Optional[int] = None


@dataclass
class StatusInfoType:
    """
    Element providing more information about the status.
    StatusInfoType is used by: ClearMonitoringResultType,
    BootNotificationResponse, CancelReservationResponse,
    TriggerMessageResponse, UnlockConnectorResponse, UpdateFirmwareResponse,
    ClearDisplayMessageResponse, Get15118EVCertificateResponse,
    GetCompositeScheduleResponse, ChangeAvailabilityResponse, GetLogResponse,
    ClearChargingProfileResponse, NotifyEVChargingNeedsResponse,
    ClearCacheResponse, NotifyEVChargingScheduleResponse,
    RequestStartTransactionResponse, RequestStopTransactionResponse,
    SetChargingProfileResponse, SetDisplayMessageResponse,
    SetNetworkProfileResponse, SignCertificateResponse, DataTransferResponse,
    CertificateSignedResponse, DeleteCertificateResponse,
    GetChargingProfilesResponse, GetInstalledCertificateIdsResponse,
    InstallCertificateResponse, GetBaseReportResponse,
    GetMonitoringReportResponse, GetReportResponse,
    GetVariablesResponse.GetVariableResultType, ReserveNowResponse,
    SetMonitoringBaseResponse, SetMonitoringLevelResponse,
    SetVariableMonitoringResponse.SetMonitoringResultType,
    SetVariablesResponse.SetVariableResultType, PublishFirmwareResponse,
    GetCertificateStatusResponse, ResetResponse, GetDisplayMessagesResponse,
    CustomerInformationResponse, SendLocalListResponse
    """

    reason_code: str
    additional_info: Optional[str] = None


@dataclass
class ClearMonitoringResultType:
    """
    ClearMonitoringResultType is used by: ClearVariableMonitoringResponse
    """

    status: enums.ClearMonitoringStatusType
    id: int
    status_info: Optional[StatusInfoType] = None


@dataclass
class EVSEType:
    """
    Electric Vehicle Supply Equipment
    EVSEType is used by: ComponentType, TriggerMessageRequest,
    ChangeAvailabilityRequest, TransactionEventRequest
    """

    id: int
    connector_id: Optional[int] = None


@dataclass
class ComponentType:
    """
    A physical or logical component.
    ComponentType is used by: ComponentVariableType, MessageInfoType,
    GetVariablesRequest.GetVariableDataType,
    GetVariablesResponse.GetVariableResultType,
    NotifyMonitoringReportRequest.MonitoringDataType,
    NotifyReportRequest.ReportDataType,
    SetVariableMonitoringRequest.SetMonitoringDataType,
    SetVariableMonitoringResponse.SetMonitoringResultType,
    SetVariablesRequest.SetVariableDataType,
    SetVariablesResponse.SetVariableResultType,
    NotifyEventRequest.EventDataType
    """

    name: str
    instance: Optional[str] = None
    evse: Optional[EVSEType] = None


@dataclass
class VariableType:
    """
    Reference key to a component-variable.
    VariableType is used by: ComponentVariableType,
    GetVariablesRequest.GetVariableDataType,
    GetVariablesResponse.GetVariableResultType,
    NotifyMonitoringReportRequest.MonitoringDataType,
    NotifyReportRequest.ReportDataType,
    SetVariableMonitoringRequest.SetMonitoringDataType,
    SetVariableMonitoringResponse.SetMonitoringResultType,
    SetVariablesRequest.SetVariableDataType,
    SetVariablesResponse.SetVariableResultType,
    NotifyEventRequest.EventDataType
    """

    name: str
    instance: Optional[str] = None


@dataclass
class ComponentVariableType:
    """
    Class to report components, variables and variable attributes and
    characteristics.
    ComponentVariableType is used by: GetMonitoringReportRequest,
    GetReportRequest
    """

    component: ComponentType
    variable: Optional[VariableType] = None


@dataclass
class CompositeScheduleType:
    """
    CompositeScheduleType is used by: GetCompositeScheduleResponse
    """

    evse_id: int
    duration: int
    schedule_start: str
    charging_rate_unit: enums.ChargingRateUnitType
    charging_schedule_period: ChargingSchedulePeriodType


@dataclass
class CostType:
    """
    CostType is used by: ConsumptionCostType
    """

    cost_kind: enums.CostKindType
    amount: int
    amount_multiplier: Optional[int] = None


@dataclass
class ConsumptionCostType:
    """
    ConsumptionCostType is used by: SalesTariffEntryType
    """

    start_value: float
    cost: CostType


@dataclass
class EventDataType:
    """
    Class to report an event notification for a component-variable.
    EventDataType is used by: NotifyEventRequest
    """

    event_id: int
    timestamp: str
    trigger: enums.EventTriggerType
    actual_value: str
    event_notification_type: enums.EventNotificationType
    component: ComponentType
    variable: VariableType
    cause: Optional[int] = None
    tech_code: Optional[str] = None
    cleared: Optional[bool] = None
    transaction_id: Optional[str] = None
    variable_monitoring_id: Optional[int] = None


@dataclass
class FirmwareType:
    """
    Represents a copy of the firmware that can be loaded/updated on the
    Charging Station.
    FirmwareType is used by: UpdateFirmwareRequest
    """

    location: str
    retrieval_date_time: str
    install_date_time: Optional[str] = None
    signing_certificate: Optional[str] = None
    signature: Optional[str] = None


@dataclass
class GetVariableDataType:
    """
    Class to hold parameters for GetVariables request.
    GetVariableDataType is used by: GetVariablesRequest
    """

    component: ComponentType
    variable: VariableType
    attribute_type: Optional[enums.AttributeType] = None


@dataclass
class GetVariableResultType:
    """
    Class to hold results of GetVariables request.
    GetVariableResultType is used by: GetVariablesResponse
    """

    attribute_status: enums.GetVariableStatusType
    component: ComponentType
    attribute_type: Optional[enums.AttributeType] = None
    attribute_value: Optional[str] = None


@dataclass
class IdTokenType:
    """
    Contains a case insensitive identifier to use for the authorization and the
    type of authorization to support multiple forms of identifiers.
    IdTokenType is used by: AuthorizationData, Common:IdTokenInfoType,
    RequestStartTransactionRequest, AuthorizeRequest, TransactionEventRequest,
    ReserveNowRequest, CustomerInformationRequest
    """

    id_token: str
    type: enums.IdTokenType
    additional_info: Optional[AdditionalInfoType] = None


@dataclass
class MessageContentType:
    """
    Contains message details, for a message to be displayed on a Charging
    Station.
    MessageContentType is used by: IdTokenInfoType, MessageInfoType,
    TransactionEventResponse
    """

    format: enums.MessageFormatType
    content: str
    language: Optional[str] = None


@dataclass
class IdTokenInfoType:
    """
    Contains status information about an identifier. It is advised to not stop
    charging for a token that expires during charging, as ExpiryDate is only
    used for caching purposes. If ExpiryDate is not given, the status has no
    end date.
    IdTokenInfoType is used by: AuthorizationData, AuthorizeResponse,
    TransactionEventResponse
    """

    status: enums.AuthorizationStatusType
    cache_expiry_date_time: Optional[str] = None
    charging_priority: Optional[int] = None
    language_1: Optional[str] = None
    evse_id: Optional[int] = None
    language_2: Optional[str] = None
    group_id_token: Optional[IdTokenType] = None
    personal_message: Optional[MessageContentType] = None


@dataclass
class AuthorizationData:
    """
    Contains the identifier to use for authorization.
    AuthorizationData is used by: SendLocalListRequest
    """

    id_token: IdTokenType
    id_token_info: Optional[IdTokenInfoType] = None


@dataclass
class LogParametersType:
    """
    Generic class for the configuration of logging entries.
    LogParametersType is used by: GetLogRequest
    """

    remote_location: str
    oldest_timestamp: Optional[str] = None
    latest_timestamp: Optional[str] = None


@dataclass
class MessageInfoType:
    """
    Contains message details, for a message to be displayed on a Charging
    Station.
    MessageInfoType is used by: SetDisplayMessageRequest,
    NotifyDisplayMessagesRequest
    """

    id: int
    priority: enums.MessagePriorityType
    message: MessageContentType
    state: Optional[enums.MessageStateType] = None
    start_date_time: Optional[str] = None
    end_data_time: Optional[str] = None
    transaction_id: Optional[str] = None
    display: Optional[ComponentType] = None


@dataclass
class SignedMeterValueType:
    """
    Represent a signed version of the meter value.
    SignedMeterValueType is used by: SampledValueType
    """

    signed_meter_data: str
    signing_method: str
    encoding_method: str
    public_key: str


@dataclass
class UnitOfMeasureType:
    """
    Represents a UnitOfMeasure with a multiplier
    UnitOfMeasureType is used by: SampledValueType
    """

    unit: Optional[str] = None
    multiplier: Optional[int] = None


@dataclass
class SampledValueType:
    """
    Single sampled value in MeterValues. Each value can be accompanied by
    optional fields.
    To save on mobile data usage, default values of all of the optional fields
    are such that. The value without any additional fields will be interpreted,
    as a register reading of active import energy in Wh (Watt-hour) units.
    SampledValueType is used by: MeterValueType
    """

    value: float
    context: Optional[enums.ReadingContextType] = None
    phase: Optional[enums.PhaseType] = None
    location: Optional[enums.LocationType] = None
    signed_meter_value: Optional[SignedMeterValueType] = None
    unit_of_measure: Optional[UnitOfMeasureType] = None


@dataclass
class MeterValueType:
    """
    Collection of one or more sampled values in MeterValuesRequest and
    TransactionEvent. All sampled values in a MeterValue are sampled at the
    same point in time.
    MeterValueType is used by: MeterValuesRequest, TransactionEventRequest
    """

    timestamp: str
    sampled_value: SampledValueType


@dataclass
class ModemType:
    """
    Defines parameters required for initiating and maintaining wireless
    communication with other devices.
    ModemType is used by: BootNotificationRequest.ChargingStationType
    """

    iccid: Optional[str] = None
    imsi: Optional[str] = None


@dataclass
class VariableMonitoringType:
    """
    A monitoring setting for a variable.
    VariableMonitoringType is used by:
    NotifyMonitoringReportRequest.MonitoringDataType
    """

    id: int
    transaction: bool
    value: float
    type: enums.MonitorType
    severity: int


@dataclass
class MonitoringDataType:
    """
    Class to hold parameters of SetVariableMonitoring request.
    MonitoringDataType is used by: NotifyMonitoringReportRequest
    """

    component: ComponentType
    variable: VariableType
    variable_monitoring: VariableMonitoringType


@dataclass
class VPNType:
    """
    VPN Configuration settings
    VPNType is used by: SetNetworkProfileRequest.NetworkConnectionProfileType
    """

    server: str
    user: str
    password: str
    key: str
    type: enums.VPNType
    group: Optional[str] = None


@dataclass
class NetworkConnectionProfileType:
    """
    The NetworkConnectionProfile defines the functional and technical
    parameters of a communication link.
    NetworkConnectionProfileType is used by: SetNetworkProfileRequest
    """

    ocpp_version: enums.OCPPVersionType
    ocpp_transport: enums.OCPPTransportType
    ocpp_csms_url: str
    message_timeout: int
    security_profile: int
    ocpp_interface: enums.OCPPInterfaceType
    vpn: Optional[VPNType] = None
    apn: Optional[APNType] = None


@dataclass
class ChargingStationType:
    """
    The physical system where an Electrical Vehicle (EV) can be charged.
    ChargingStationType is used by: BootNotificationRequest
    """

    vendor_name: str
    model: str
    modem: Optional[ModemType] = None
    serial_number: Optional[str] = None
    firmware_version: Optional[str] = None


@dataclass
class OCSPRequestDataType:
    """
    OCSPRequestDataType is used by: AuthorizeRequest,
    GetCertificateStatusRequest
    """

    hash_algorithm: enums.HashAlgorithmType
    issuer_name_hash: str
    issuer_key_hash: str
    serial_number: str
    responder_url: str


@dataclass
class VariableAttributeType:
    """
    Attribute data of a variable.
    VariableAttributeType is used by: NotifyReportRequest.ReportDataType
    """

    type: Optional[enums.AttributeType] = None
    value: Optional[str] = None
    mutability: Optional[enums.MutabilityType] = None
    persistent: Optional[bool] = None
    constant: Optional[bool] = None


@dataclass
class VariableCharacteristicsType:
    """
    Fixed read-only parameters of a variable.
    VariableCharacteristicsType is used by: NotifyReportRequest.ReportDataType
    """

    data_type: enums.DataType
    supports_monitoring: bool
    unit: Optional[str] = None
    min_limit: Optional[float] = None
    max_limit: Optional[float] = None
    values_list: Optional[str] = None


@dataclass
class ReportDataType:
    """
    Class to report components, variables and variable attributes and
    characteristics
    ReportDataType is used by: NotifyReportRequest
    """

    component: ComponentType
    variable: VariableType
    variable_attribute: VariableAttributeType
    variable_characteristics: Optional[VariableCharacteristicsType] = None


@dataclass
class SalesTariffType:
    """
    This dataType is based on dataTypes from ISO 15118-2.
    SalesTariffType is used by: ChargingScheduleType
    """

    id: int
    sales_tariff_entry: SalesTariffEntryType
    sales_tariff_description: Optional[str] = None
    num_e_price_levels: Optional[int] = None


@dataclass
class SetMonitoringDataType:
    """
    Class to hold parameters of SetVariableMonitoring request.
    SetMonitoringDataType is used by: SetVariableMonitoringRequest
    """

    value: float
    type: enums.MonitorType
    severity: int
    component: ComponentType
    variable: VariableType
    id: Optional[int] = None
    transaction: Optional[bool] = None


@dataclass
class SetMonitoringResultType:
    """
    Class to hold result of SetVariableMonitoring request.
    SetMonitoringResultType is used by: SetVariableMonitoringResponse
    """

    status: enums.SetMonitoringStatusType
    type: enums.MonitorType
    severity: int
    component: ComponentType
    variable: VariableType
    id: Optional[int] = None
    status_info: Optional[StatusInfoType] = None


@dataclass
class SetVariableDataType:
    """SetVariableDataType is used by: SetVariablesRequest"""

    attribute_value: str
    component: ComponentType
    variable: VariableType
    attribute_type: Optional[enums.AttributeType] = None


@dataclass
class SetVariableResultType:
    """SetVariableResultType is used by: SetVariablesResponse"""

    attribute_status: enums.SetVariableStatusType
    component: ComponentType
    variable: VariableType
    attribute_type: Optional[enums.AttributeType] = None
    attribute_status_info: Optional[StatusInfoType] = None


@dataclass
class TransactionType:
    """TransactionType is used by: TransactionEventRequest"""

    transaction_id: str
    charging_state: Optional[enums.ChargingStateType] = None
    time_spent_charging: Optional[int] = None
    stopped_reason: Optional[enums.ReasonType] = None
    remote_start_id: Optional[int] = None
