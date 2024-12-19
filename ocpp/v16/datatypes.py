from dataclasses import dataclass
from typing import List, Optional

from ocpp.v16 import enums


@dataclass
class IdTagInfo:
    """
    Contains status information about an identifier. It is returned in
    Authorize, Start Transaction and Stop Transaction responses.

    If expiryDate is not given, the status has no end date.
    """

    status: enums.AuthorizationStatus
    parent_id_tag: Optional[str] = None
    expiry_date: Optional[str] = None


@dataclass
class AuthorizationData:
    """
    Elements that constitute an entry of a Local Authorization List update.
    """

    id_tag: str
    id_tag_info: Optional[IdTagInfo] = None


@dataclass
class ChargingSchedulePeriod:
    start_period: int
    limit: float
    number_phases: Optional[int] = None


@dataclass
class ChargingSchedule:
    charging_rate_unit: enums.ChargingRateUnitType
    charging_schedule_period: List[ChargingSchedulePeriod]
    duration: Optional[int] = None
    start_schedule: Optional[str] = None
    min_charging_rate: Optional[float] = None


@dataclass
class ChargingProfile:
    """
    A ChargingProfile consists of a ChargingSchedule, describing the
    amount of power or current that can be delivered per time interval.
    """

    charging_profile_id: int
    stack_level: int
    charging_profile_purpose: enums.ChargingProfilePurposeType
    charging_profile_kind: enums.ChargingProfileKindType
    charging_schedule: ChargingSchedule
    transaction_id: Optional[int] = None
    recurrency_kind: Optional[enums.RecurrencyKind] = None
    valid_from: Optional[str] = None
    valid_to: Optional[str] = None


@dataclass
class KeyValue:
    """
    Contains information about a specific configuration key.
    It is returned in GetConfiguration.conf.
    """

    key: str
    readonly: bool
    value: Optional[str] = None

    def __post_init__(self):
        if len(self.key) > enums.CiStringType.ci_string_50:
            msg = "Field key is longer than 50 characters"
            raise ValueError(msg)

        if self.value and len(self.value) > enums.CiStringType.ci_string_500:
            msg = "Field key is longer than 500 characters"
            raise ValueError(msg)


@dataclass
class SampledValue:
    """
    Single sampled value in MeterValues. Each value can be accompanied by
    optional fields.
    """

    value: str
    context: Optional[enums.ReadingContext] = None
    format: Optional[enums.ValueFormat] = None
    measurand: Optional[enums.Measurand] = None
    phase: Optional[enums.Phase] = None
    location: Optional[enums.Location] = None
    unit: Optional[enums.UnitOfMeasure] = None


@dataclass
class MeterValue:
    """
    Collection of one or more sampled values in MeterValues.req.
    All sampled values in a MeterValue are sampled at the same point in time.
    """

    timestamp: str
    sampled_value: List[SampledValue]


# Security Extension


@dataclass
class CertificateHashData:
    """
    CertificateHashDataType is used by:
    DeleteCertificate.req, GetInstalledCertificateIds.conf
    """

    hash_algorithm: enums.HashAlgorithm
    issuer_name_hash: str
    issuer_key_hash: str
    serial_number: str


@dataclass
class Firmware:
    """
    Represents a copy of the firmware that can be loaded/updated on the Charge Point.
    FirmwareType is used by: SignedUpdateFirmware.req
    """

    location: str
    retrieve_date_time: str
    signing_certificate: str
    install_date_time: Optional[str] = None
    signature: Optional[str] = None


@dataclass
class LogParameters:
    """
    Class for detailed information the retrieval of logging entries.
    LogParametersType is used by: GetLog.req
    """

    remote_location: str
    oldest_timestamp: Optional[str] = None
    latest_timestamp: Optional[str] = None
