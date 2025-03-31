from dataclasses import dataclass
from datetime import datetime
from typing import List, Optional

from ocpp.v21.enums import (
    AuthorizationStatusEnum,
    CertificateStatusEnum,
    CertificateStatusSourceEnum,
    ChargingProfilePurposeEnum,
    ChargingRateUnitEnum,
    ClearMonitoringStatusEnum,
    DayOfWeekEnum,
    EvseKindEnum,
    GetCertificateIdUseEnum,
    HashAlgorithmEnum,
    MessageFormatEnum,
    OperationModeEnum,
    TariffClearStatusEnum,
)


@dataclass
class CustomData:
    """
    This class can be extended with arbitrary JSON properties to allow adding custom data.
    """

    vendor_id: str


@dataclass
class Address:
    """
    (2.1) A generic address format.
    """

    name: str
    address1: str
    city: str
    country: str
    address2: Optional[str] = None
    postal_code: Optional[str] = None
    custom_data: Optional[CustomData] = None


@dataclass
class AdditionalInfo:
    """
    Contains a case insensitive identifier to use for the authorization and the type of authorization to support multiple forms of identifiers.
    """

    additional_id_token: str
    type: str
    custom_data: Optional[CustomData] = None


@dataclass
class IdToken:
    """
    Contains a case insensitive identifier to use for the authorization and the type of authorization to support multiple forms of identifiers.
    """

    id_token: str
    type: str
    additional_info: Optional[List[AdditionalInfo]] = None
    custom_data: Optional[CustomData] = None


@dataclass
class OCSPRequestData:
    """
    Information about a certificate for an OCSP check.
    """

    hash_algorithm: HashAlgorithmEnum
    issuer_name_hash: str
    issuer_key_hash: str
    serial_number: str
    responder_url: str
    custom_data: Optional[CustomData] = None


@dataclass
class MessageContent:
    """
    Contains message details, for a message to be displayed on a Charging Station.
    """

    format: MessageFormatEnum
    content: str
    language: Optional[str] = None
    custom_data: Optional[CustomData] = None


@dataclass
class TaxRate:
    """
    Tax rate information.
    """

    rate: float
    custom_data: Optional[CustomData] = None


@dataclass
class Price:
    """
    Price with and without tax. At least one of excl_tax, incl_tax must be present.
    """

    excl_tax: Optional[float] = None
    incl_tax: Optional[float] = None
    tax_rates: Optional[List["TaxRate"]] = None
    custom_data: Optional[CustomData] = None


@dataclass
class TariffConditionsFixed:
    """
    These conditions describe if a FixedPrice applies at start of the transaction.
    When more than one restriction is set, they are to be treated as a logical AND. All need to be valid before this price is active.
    NOTE: start_time_of_day and end_time_of_day are in local time, because it is the time in the tariff as it is shown to the EV driver at the Charging Station.
    A Charging Station will convert this to the internal time zone that it uses (which is recommended to be UTC) when performing cost calculation.
    """

    start_time_of_day: Optional[str] = None
    end_time_of_day: Optional[str] = None
    day_of_week: Optional[List[DayOfWeekEnum]] = None
    valid_from_date: Optional[str] = None
    valid_to_date: Optional[str] = None
    evse_kind: Optional[EvseKindEnum] = None
    payment_brand: Optional[str] = None
    payment_recognition: Optional[str] = None
    custom_data: Optional[CustomData] = None


@dataclass
class TariffConditions:
    """
    These conditions describe if and when a TariffEnergyType or TariffTimeType applies during a transaction.
    When more than one restriction is set, they are to be treated as a logical AND. All need to be valid before this price is active.
    For reverse energy flow (discharging) negative values of energy, power and current are used.
    NOTE: minXXX (where XXX = Kwh/A/Kw) must be read as "closest to zero", and maxXXX as "furthest from zero".
    NOTE: start_time_of_day and end_time_of_day are in local time, because it is the time in the tariff as it is shown to the EV driver at the Charging Station.
    A Charging Station will convert this to the internal time zone that it uses (which is recommended to be UTC) when performing cost calculation.
    """

    start_time_of_day: Optional[str] = None
    end_time_of_day: Optional[str] = None
    day_of_week: Optional[List[DayOfWeekEnum]] = None
    valid_from_date: Optional[str] = None
    valid_to_date: Optional[str] = None
    evse_kind: Optional[EvseKindEnum] = None
    min_energy: Optional[float] = None
    max_energy: Optional[float] = None
    min_current: Optional[float] = None
    max_current: Optional[float] = None
    min_power: Optional[float] = None
    max_power: Optional[float] = None
    min_time: Optional[int] = None
    max_time: Optional[int] = None
    min_charging_time: Optional[int] = None
    max_charging_time: Optional[int] = None
    min_idle_time: Optional[int] = None
    max_idle_time: Optional[int] = None
    custom_data: Optional[CustomData] = None


@dataclass
class TariffEnergyPrice:
    """
    Tariff with optional conditions for an energy price.
    """

    price_kwh: float
    conditions: Optional[TariffConditions] = None
    custom_data: Optional[CustomData] = None


@dataclass
class IdTokenInfo:
    """
    Contains status information about an identifier.
    It is advised to not stop charging for a token that expires during charging, as ExpiryDate is only used for caching purposes.
    If ExpiryDate is not given, the status has no end date.
    """

    status: AuthorizationStatusEnum
    cache_expiry_date_time: Optional[datetime] = None
    charging_priority: Optional[int] = None
    group_id_token: Optional[IdToken] = None
    language1: Optional[str] = None
    language2: Optional[str] = None
    evse_id: Optional[List[int]] = None
    personal_message: Optional[MessageContent] = None
    custom_data: Optional[CustomData] = None


@dataclass
class Modem:
    """
    Defines parameters required for initiating and maintaining wireless communication with other devices.
    """

    iccid: Optional[str] = None
    imsi: Optional[str] = None
    custom_data: Optional[CustomData] = None


@dataclass
class ChargingStation:
    """
    The physical system where an Electrical Vehicle (EV) can be charged.
    """

    model: str
    vendor_name: str
    serial_number: Optional[str] = None
    modem: Optional[Modem] = None
    firmware_version: Optional[str] = None
    custom_data: Optional[CustomData] = None


@dataclass
class StatusInfo:
    """
    Element providing more information about the status.
    """

    reason_code: str
    additional_info: Optional[str] = None
    custom_data: Optional[CustomData] = None


@dataclass
class PeriodicEventStreamParams:
    """
    Parameters for periodic event stream configuration.
    """

    interval: int
    values: int
    custom_data: Optional[CustomData] = None


@dataclass
class BatteryData:
    """
    Data about a battery being swapped.
    """

    evse_id: int
    serial_number: str
    so_c: float
    so_h: float
    production_date: Optional[datetime] = None
    vendor_info: Optional[str] = None
    custom_data: Optional[CustomData] = None


@dataclass
class EVSE:
    """
    Electric Vehicle Supply Equipment.
    """

    id: int
    connector_id: Optional[int] = None
    custom_data: Optional[CustomData] = None


@dataclass
class TariffEnergy:
    """
    Price elements and tax for energy.
    """

    prices: List[TariffEnergyPrice]
    tax_rates: Optional[List[TaxRate]] = None
    custom_data: Optional[CustomData] = None


@dataclass
class TariffFixedPrice:
    """
    Tariff with optional conditions for a fixed price.
    """

    price_fixed: float
    conditions: Optional[TariffConditionsFixed] = None
    custom_data: Optional[CustomData] = None


@dataclass
class TariffFixed:
    """
    Fixed tariff information.
    """

    prices: List[TariffFixedPrice]
    tax_rates: Optional[List[TaxRate]] = None
    custom_data: Optional[CustomData] = None


@dataclass
class TariffTimePrice:
    """
    Tariff with optional conditions for a time duration price.
    """

    price_minute: float
    conditions: Optional[TariffConditions] = None
    custom_data: Optional[CustomData] = None


@dataclass
class TariffTime:
    """
    Price elements and tax for time.
    """

    prices: List[TariffTimePrice]
    tax_rates: Optional[List[TaxRate]] = None
    custom_data: Optional[CustomData] = None


@dataclass
class Tariff:
    """
    A tariff is described by fields with prices for:
    energy,
    charging time,
    idle time,
    fixed fee,
    reservation time,
    reservation fixed fee.
    Each of these fields may have (optional) conditions that specify when a price is applicable.
    The description contains a human-readable explanation of the tariff to be shown to the user.
    The other fields are parameters that define the tariff. These are used by the charging station to calculate the price.
    """

    tariff_id: str
    currency: str
    description: Optional[List[MessageContent]] = None
    energy: Optional[TariffEnergy] = None
    valid_from: Optional[datetime] = None
    charging_time: Optional[TariffTime] = None
    idle_time: Optional[TariffTime] = None
    fixed_fee: Optional[TariffFixed] = None
    reservation_time: Optional[TariffTime] = None
    reservation_fixed: Optional[TariffFixed] = None
    min_cost: Optional[Price] = None
    max_cost: Optional[Price] = None
    custom_data: Optional[CustomData] = None


@dataclass
class ClearChargingProfile:
    """
    A ClearChargingProfileType is a filter for charging profiles to be cleared by ClearChargingProfileRequest.
    """

    evse_id: Optional[int] = None
    charging_profile_purpose: Optional[ChargingProfilePurposeEnum] = None
    stack_level: Optional[int] = None
    custom_data: Optional[CustomData] = None


@dataclass
class ClearTariffsResult:
    """
    Result of clearing a tariff.
    """

    status: TariffClearStatusEnum
    tariff_id: Optional[str] = None
    status_info: Optional[StatusInfo] = None
    custom_data: Optional[CustomData] = None


@dataclass
class ClearMonitoringResult:
    """
    Result of a clear monitoring request for a specific monitor.
    """

    status: ClearMonitoringStatusEnum
    id: int
    status_info: Optional[StatusInfo] = None
    custom_data: Optional[CustomData] = None


@dataclass
class CertificateHashData:
    """
    Certificate hash data.
    """

    hash_algorithm: HashAlgorithmEnum
    issuer_name_hash: str
    issuer_key_hash: str
    serial_number: str
    custom_data: Optional[CustomData] = None


@dataclass
class CertificateStatusRequestInfo:
    """
    Data necessary to request the revocation status of a certificate.
    """

    certificate_hash_data: CertificateHashData
    source: CertificateStatusSourceEnum
    urls: List[str]
    custom_data: Optional[CustomData] = None


@dataclass
class CertificateStatus:
    """
    Revocation status of certificate
    """

    certificate_hash_data: CertificateHashData
    source: CertificateStatusSourceEnum
    status: CertificateStatusEnum
    next_update: datetime
    custom_data: Optional[CustomData] = None


@dataclass
class ChargingProfileCriterion:
    """
    A ChargingProfileCriterion is a filter for charging profiles to be selected by a GetChargingProfilesRequest.
    """

    charging_profile_purpose: ChargingProfilePurposeEnum
    stack_level: Optional[int] = None
    charging_profile_id: Optional[List[int]] = None
    charging_limit_source: Optional[List[str]] = None
    custom_data: Optional[CustomData] = None


@dataclass
class V2XFreqWattPoint:
    """
    A point of a frequency-watt curve.
    """

    frequency: float
    power: float
    custom_data: Optional[CustomData] = None


@dataclass
class V2XSignalWattPoint:
    """
    A point of a signal-watt curve.
    """

    signal: int
    power: float
    custom_data: Optional[CustomData] = None


@dataclass
class ChargingSchedulePeriod:
    """
    Charging schedule period structure defines a time period in a charging schedule.
    It is used in: CompositeSchedule and in ChargingSchedule.
    When used in a NotifyEVChargingScheduleRequest only start_period, limit, limit_L2, limit_L3 are relevant.
    """

    start_period: int
    limit: Optional[float] = None
    limit_L2: Optional[float] = None
    limit_L3: Optional[float] = None
    number_phases: Optional[int] = None
    phase_to_use: Optional[int] = None
    discharge_limit: Optional[float] = None
    discharge_limit_L2: Optional[float] = None
    discharge_limit_L3: Optional[float] = None
    setpoint: Optional[float] = None
    setpoint_L2: Optional[float] = None
    setpoint_L3: Optional[float] = None
    setpoint_reactive: Optional[float] = None
    setpoint_reactive_L2: Optional[float] = None
    setpoint_reactive_L3: Optional[float] = None
    preconditioning_request: Optional[bool] = None
    evse_sleep: Optional[bool] = None
    v2x_baseline: Optional[float] = None
    operation_mode: Optional[OperationModeEnum] = None
    v2x_freq_watt_curve: Optional[List[V2XFreqWattPoint]] = None
    v2x_signal_watt_curve: Optional[List[V2XSignalWattPoint]] = None
    custom_data: Optional[CustomData] = None


@dataclass
class CompositeSchedule:
    """
    Composite schedule that represents the charging profile over a period.
    """

    evse_id: int
    duration: int
    schedule_start: datetime
    charging_rate_unit: ChargingRateUnitEnum
    charging_schedule_period: List[ChargingSchedulePeriod]
    custom_data: Optional[CustomData] = None


@dataclass
class CertificateHashDataChain:
    """
    Certificate chain information for GetInstalledCertificateIds.
    """

    certificate_hash_data: CertificateHashData
    certificate_type: GetCertificateIdUseEnum
    child_certificate_hash_data: Optional[List[CertificateHashData]] = None
    custom_data: Optional[CustomData] = None


@dataclass
class LogParameters:
    """
    Generic class for the configuration of logging entries.
    """

    remote_location: str
    oldest_timestamp: Optional[datetime] = None
    latest_timestamp: Optional[datetime] = None
    custom_data: Optional[CustomData] = None


@dataclass
class Variable:
    """
    Reference key to a component-variable.
    """

    name: str
    instance: Optional[str] = None
    custom_data: Optional[CustomData] = None


@dataclass
class Component:
    """
    A physical or logical component.
    """

    name: str
    evse: Optional[EVSE] = None
    instance: Optional[str] = None
    custom_data: Optional[CustomData] = None


@dataclass
class ComponentVariable:
    """
    Class to report components, variables and variable attributes and characteristics.
    """

    component: Component
    variable: Optional[Variable] = None
    custom_data: Optional[CustomData] = None


@dataclass
class ConstantStreamData:
    """
    Data for a constant event stream.
    """

    id: int
    variable_monitoring_id: int
    params: PeriodicEventStreamParams
    custom_data: Optional[CustomData] = None
