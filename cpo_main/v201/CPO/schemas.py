from typing import Dict, List, Optional
from dataclasses import dataclass
from ocpp.v201.enums import *
from enum import Enum
from v201.CPO.classes import SessionType
from datetime import datetime
from pydantic import BaseModel, constr

class User(BaseModel):
    username: str
    password: str

class Auth(BaseModel):
    username: str
    password: str
    
class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Optional[str] = None

class ConfigurationKey(str, Enum):
    """
    Configuration Key Names.
    """

    # 9.1 Core Profile
    allow_offline_tx_for_unknown_id = "AllowOfflineTxForUnknownId"
    authorization_cache_enabled = "AuthorizationCacheEnabled"
    authorize_remote_tx_requests = "AuthorizeRemoteTxRequests"
    blink_repeat = "BlinkRepeat"
    clock_aligned_data_interval = "ClockAlignedDataInterval"
    connection_time_out = "ConnectionTimeOut"
    connector_phase_rotation = "ConnectorPhaseRotation"
    connector_phase_rotation_max_length = "ConnectorPhaseRotationMaxLength"
    get_configuration_max_keys = "GetConfigurationMaxKeys"
    heartbeat_interval = "HeartbeatInterval"
    light_intensity = "LightIntensity"
    local_authorize_offline = "LocalAuthorizeOffline"
    local_pre_authorize = "LocalPreAuthorize"
    max_energy_on_invalid_id = "MaxEnergyOnInvalidId"
    meter_values_aligned_data = "MeterValuesAlignedData"
    meter_values_aligned_data_max_length = "MeterValuesAlignedDataMaxLength"
    meter_values_sampled_data = "MeterValuesSampledData"
    meter_values_sampled_data_max_length = "MeterValuesSampledDataMaxLength"
    meter_value_sample_interval = "MeterValueSampleInterval"
    minimum_status_duration = "MinimumStatusDuration"
    number_of_connectors = "NumberOfConnectors"
    reset_retries = "ResetRetries"
    stop_transaction_on_ev_side_disconnect = "StopTransactionOnEVSideDisconnect"
    stop_transaction_on_invalid_id = "StopTransactionOnInvalidId"
    stop_txn_aligned_data = "StopTxnAlignedData"
    stop_txn_aligned_data_max_length = "StopTxnAlignedDataMaxLength"
    stop_txn_sampled_data = "StopTxnSampledData"
    stop_txn_sampled_data_max_length = "StopTxnSampledDataMaxLength"
    supported_feature_profiles = "SupportedFeatureProfiles"
    supported_feature_profiles_max_length = "SupportedFeatureProfilesMaxLength"
    transaction_message_attempts = "TransactionMessageAttempts"
    transaction_message_retry_interval = "TransactionMessageRetryInterval"
    unlock_connector_on_ev_side_disconnect = "UnlockConnectorOnEVSideDisconnect"
    web_socket_ping_interval = "WebSocketPingInterval"

    # 9.2 Local Auth List Management Profile
    local_auth_list_enabled = "LocalAuthListEnabled"
    local_auth_list_max_length = "LocalAuthListMaxLength"
    send_local_list_max_length = "SendLocalListMaxLength"

    # 9.3 Reservation Profile
    reserve_connector_zero_supported = "ReserveConnectorZeroSupported"

    # 9.4 Smart Charging Profile
    charge_profile_max_stack_level = "ChargeProfileMaxStackLevel"
    charging_schedule_allowed_charging_rate_unit = "ChargingScheduleAllowedChargingRateUnit"
    charging_schedule_max_periods = "ChargingScheduleMaxPeriods"
    connector_switch_3to1_phase_supported = "ConnectorSwitch3to1PhaseSupported"
    max_charging_profiles_installed = "MaxChargingProfilesInstalled"

class Configuration(BaseModel):
    key: ConfigurationKey
    value: str

class GetConfig(BaseModel):
    key: ConfigurationKey
    
class Reset(BaseModel):
     type: ResetType

class TokenRefresh(BaseModel):
    token: Optional[str] = None
    password: Optional[str] = None

class UserCreate(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email: Optional[str] = None
    mobile: Optional[str] = None

class UserStatus(str, Enum):
    new = 'New'
    valid = 'Valid'
    locked = 'Locked'

class UserView(BaseModel):
    id: str
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email: Optional[str] = None
    mobile: Optional[str] = None
    user_status: UserStatus

class SessionType(str, Enum):
    one_phase = 'OnePhase'
    three_phase = 'ThreePhase'
    schuko = 'Shuko'

class ConnectorStatusType(str, Enum):
    available = 'Available'
    charging = 'Charging'
    connected = 'Connected'
    error = 'Error'
    unknown = 'Unknown'

class Phase(str, Enum):
    L1 = 'L1'
    L2 = 'L2'
    L3 = 'L3'

class Measurement(BaseModel):
    phase: Phase
    current: float
    voltage: float

class ConnectorStatus(BaseModel):
    charge_point_id: Optional[str] = None
    connector_id: int
    total_consumption_kwh: float
    session_type: SessionType
    status: ConnectorStatusType
    measurement: Measurement
    start_time: datetime
    end_time: datetime
    session_id: Optional[int] = None

class ChargePointStatusType(str, Enum):
    online = 'Online'
    offline = 'Offline'

class ChargePointStatus(BaseModel):
    id: Optional[str] = None
    status: ChargePointStatusType
    connector_status: ConnectorStatus

class ConnectorFunctionType(str, Enum):
    charger = 'charger'
    schuko = 'schuko'

class Connector(BaseModel):
    charge_point_id: Optional[str] = None
    connector_id: int
    type: ConnectorFunctionType

class DimmerValue(str, Enum):
    off = 'off'
    low = 'low'
    medium = 'medium'
    high = 'high'

class ChargePointConfiguration(BaseModel):
    id: Optional[str] = None
    dimmer: DimmerValue
    down_light: Optional[bool] = None
    max_current: Optional[float] = None

class ChargePoint(BaseModel):
    id: Optional[str] = None
    name: Optional[str] = None
    password: Optional[str] = None
    type: Optional[str] = None
    is_load_balanced: bool
    firmware_version: Optional[str] = None
    hardware_version: Optional[str] = None
    ocpp_version: Optional[str] = None
    configuration: Optional[ChargePointConfiguration] = None
    connectors: Optional[Connector] = None



class OnOffMode(str, Enum):
    on = 'on'
    off = 'off'
    schedule = 'schedule'

class ConnectorConfiguration(BaseModel):
    charge_point_id: Optional[str] = None
    connector_id: int
    max_current: Optional[float] = None
    mode = OnOffMode
    cable_lock = bool

class ChargePointRegistrationInfo(BaseModel):
    charge_point_id: constr(min_length=1)
    password: constr(min_length=1)
    charge_point_name: Optional[str] = None

class ChargePointAuth(BaseModel):
    charge_point_id: constr(min_length=1)
    password: constr(min_length=1)

class ChargingSession(BaseModel):
    id: int
    charge_point_id: Optional[str] = None
    connector_id: int
    organisation_id: Optional[str] = None
    session_type: str
    start_time: datetime
    end_time: datetime
    external_transaction_id: Optional[str] = None
    total_consumption_kwh: float
    external_id: Optional[str] = None

class ViewConnectorCofiguration(BaseModel):
    charge_point_id: Optional[str] = None
    connector_id: int
    max_current: Optional[float] = None
    mode: OnOffMode
    cable_lock: bool
    intallation_current: int

class CreateConnectorConfiguration(BaseModel):
    charge_point_id: Optional[str] = None
    connector_id: int
    max_current: Optional[float] = None
    mode: OnOffMode
    cable_lock: bool

class GetSchedule(BaseModel):
    connector_id: int
    duration: int
    charging_rate_unit: ChargingRateUnitType

class Schedule(BaseModel):
    id: int
    charge_point_id: Optional[str] = None
    name: Optional[str] = None
    active: bool
    start_hours: int
    start_minutes: int
    end_hours: int
    end_minutes: int
    time_zone: Optional[str] = None
    monday: bool
    tuesday: bool
    wednesday: bool
    thursday: bool
    friday: bool
    saturday: bool
    sunday: bool
    connector_id_list: Optional[str] = None

class Organisation(BaseModel):
    id: str
    name: Optional[str] = None
    description: Optional[str] = None

class Trigger(str, Enum):
    status_notification = "StatusNotification"
    meter_values = "MeterValues"
    diagnostics_status = "DiagnosticsStatusNotification"
    firmware_status = "FirmwareStatusNotification"


@dataclass
class Authorize(BaseModel):
    id_token: Dict
    certificate: Optional[str] = None
    iso15118_certificate_hash_data: Optional[List] = None


@dataclass
class BootNotification(BaseModel):
    charging_station: Dict
    reason: str


@dataclass
class CancelReservation(BaseModel):
    reservation_id: int


@dataclass
class CertificateSigned(BaseModel):
    certificate_chain: str
    certificate_type: Optional[str] = None


@dataclass
class ChangeAvailability(BaseModel):
    operational_status: str
    evse: Optional[Dict] = None


@dataclass
class ClearCache(BaseModel):
    pass


@dataclass
class ClearChargingProfile(BaseModel):
    charging_profile_id: Optional[int] = None
    charging_profile_criteria: Optional[Dict] = None


@dataclass
class ClearDisplayMessage(BaseModel):
    id: int


@dataclass
class ClearVariableMonitoring(BaseModel):
    id: List


@dataclass
class ClearedChargingLimit(BaseModel):
    charging_limit_source: str
    evse_id: Optional[int] = None


@dataclass
class CostUpdated(BaseModel):
    total_cost: int
    transaction_id: str


@dataclass
class CustomerInformation(BaseModel):
    request_id: int
    report: bool
    clear: bool
    customer_certificate: Optional[Dict] = None
    id_token: Optional[Dict] = None
    customer_identifier: Optional[str] = None


@dataclass
class DataTransfer(BaseModel):
    vendor_id: str
    message_id: Optional[str] = None
    data: Optional[str] = None


@dataclass
class DeleteCertificate(BaseModel):
    certificate_hash_data: Dict


@dataclass
class FirmwareStatusNotification(BaseModel):
    status: str
    request_id: Optional[int] = None


@dataclass
class Get15118EVCertificate(BaseModel):
    iso15118_schema_version: str
    action: str
    exi_request: str


@dataclass
class GetBaseReport(BaseModel):
    request_id: int
    report_base: str


@dataclass
class GetCertificateStatus(BaseModel):
    ocsp_request_data: Dict


@dataclass
class GetChargingProfiles(BaseModel):
    request_id: int
    charging_profile: Dict
    evse_id: Optional[int] = None


@dataclass
class GetCompositeSchedule(BaseModel):
    duration: int
    evse_id: int
    charging_rate_unit: Optional[str] = None


@dataclass
class GetDisplayMessages(BaseModel):
    request_id: int
    id: Optional[List] = None
    priority: Optional[str] = None
    state: Optional[str] = None


@dataclass
class GetInstalledCertificateIds(BaseModel):
    certificate_type: Optional[List] = None


@dataclass
class GetLocalListVersion(BaseModel):
    pass


@dataclass
class GetLog(BaseModel):
    log: Dict
    log_type: str
    request_id: int
    retries: Optional[int] = None
    retry_interval: Optional[int] = None


@dataclass
class GetMonitoringReport(BaseModel):
    request_id: int
    component_variable: Optional[List] = None
    monitoring_criteria: Optional[List] = None


@dataclass
class GetReport(BaseModel):
    request_id: int
    component_variable: Optional[List] = None
    component_criteria: Optional[List] = None


@dataclass
class GetTransactionStatus(BaseModel):
    transaction_id: Optional[str] = None


@dataclass
class GetVariables(BaseModel):
    get_variable_data: List


@dataclass
class Heartbeat(BaseModel):
    pass


@dataclass
class InstallCertificate(BaseModel):
    certificate_type: str
    certificate: str


@dataclass
class LogStatusNotification(BaseModel):
    status: str
    request_id: Optional[int] = None


@dataclass
class MeterValues(BaseModel):
    evse_id: int
    meter_value: List


@dataclass
class NotifyChargingLimit(BaseModel):
    charging_limit: Dict
    charging_schedule: Optional[List] = None
    evse_id: Optional[int] = None


@dataclass
class NotifyCustomerInformation(BaseModel):
    data: str
    seq_no: int
    generated_at: str
    request_id: int
    tbc: Optional[bool] = None


@dataclass
class NotifyDisplayMessages(BaseModel):
    request_id: int
    message_info: Optional[List] = None
    tbc: Optional[bool] = None


@dataclass
class NotifyEVChargingNeeds(BaseModel):
    charging_needs: Dict
    evse_id: int
    max_schedule_tuples: Optional[int] = None


@dataclass
class NotifyEVChargingSchedule(BaseModel):
    time_base: str
    charging_schedule: Dict
    evse_id: int


@dataclass
class NotifyEvent(BaseModel):
    generated_at: str
    seq_no: int
    event_data: List
    tbc: Optional[bool] = None


@dataclass
class NotifyMonitoringReport(BaseModel):
    request_id: int
    seq_no: int
    generated_at: str
    monitor: Optional[List] = None
    tbc: Optional[bool] = None


@dataclass
class NotifyReport(BaseModel):
    request_id: int
    generated_at: str
    seq_no: int
    report_data: Optional[List] = None
    tbc: Optional[bool] = None


@dataclass
class PublishFirmware(BaseModel):
    location: str
    checksum: str
    request_id: int
    retries: Optional[int] = None
    retry_interval: Optional[int] = None


@dataclass
class PublishFirmwareStatusNotification(BaseModel):
    status: str
    location: Optional[List] = None
    request_id: Optional[int] = None


@dataclass
class ReportChargingProfiles(BaseModel):
    request_id: int
    charging_limit_source: str
    charging_profile: List
    evse_id: int
    tbc: Optional[bool] = None


class RequestStartTransaction(BaseModel):
    id_token: dict
    remote_start_id: int
    evse_id: Optional[int] = None
    group_id_token: Optional[Dict] = None
    charging_profile: Optional[Dict] = None


@dataclass
class RequestStopTransaction:
    transaction_id: str


@dataclass
class ReservationStatusUpdate:
    reservation_id: int
    reservation_update_status: str


@dataclass
class ReserveNow:
    id: int
    expiry_date_time: str
    id_token: Dict
    connector_type: Optional[str] = None
    evse_id: Optional[int] = None
    group_id_token: Optional[Dict] = None


@dataclass
class Reset:
    type: str
    evse_id: Optional[int] = None


@dataclass
class SecurityEventNotification:
    type: str
    timestamp: str
    tech_info: Optional[str] = None


@dataclass
class SendLocalList:
    version_number: int
    update_type: str
    local_authorization_list: Optional[List] = None


@dataclass
class SetChargingProfile:
    evse_id: int
    charging_profile: Dict


@dataclass
class SetDisplayMessage:
    message: Dict


@dataclass
class SetMonitoringBase:
    monitoring_base: str


@dataclass
class SetMonitoringLevel:
    severity: int


@dataclass
class SetNetworkProfile:
    configuration_slot: int
    connection_data: Dict


@dataclass
class SetVariableMonitoring:
    set_monitoring_data: List


@dataclass
class SetVariables:
    set_variable_data: List


@dataclass
class SignCertificate:
    csr: str
    certificate_type: Optional[str] = None


@dataclass
class StatusNotification:
    timestamp: str
    connector_status: str
    evse_id: int
    connector_id: int


@dataclass
class TransactionEvent:
    event_type: str
    timestamp: str
    trigger_reason: str
    seq_no: int
    transaction_info: Dict
    meter_value: Optional[List] = None
    offline: Optional[bool] = None
    number_of_phases_used: Optional[int] = None
    cable_max_current: Optional[int] = None
    reservation_id: Optional[int] = None
    evse: Optional[Dict] = None
    id_token: Optional[Dict] = None


@dataclass
class TriggerMessage:
    requested_message: str
    evse: Optional[Dict] = None


@dataclass
class UnlockConnector:
    evse_id: int
    connector_id: int


@dataclass
class UnpublishFirmware:
    checksum: str


@dataclass
class UpdateFirmware:
    request_id: int
    firmware: Dict
    retries: Optional[int] = None
    retry_interval: Optional[int] = None
