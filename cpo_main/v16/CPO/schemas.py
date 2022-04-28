from enum import Enum
from typing import Optional
from v16.CPO.classes import SessionType
from datetime import datetime
from ocpp.v16.enums import *

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

class ChargeSession(BaseModel):
    username: str
    password: str

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
    id: int
    charge_point_id: str
    charge_point_vendor: str
    charge_point_model:Optional[str] = None
    charge_point_serial_number: Optional[str] = None
    firmware_version: Optional[str] = None
    charge_box_serial_number: Optional[str] = None
    iccid: Optional[str] = None
    imsi: Optional[str] = None
    meter_serial_number: Optional[str] = None
    meter_type: Optional[str] = None
    heartbeat: Optional[datetime] = None



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