from enum import Enum
from typing import Optional
from pydantic import BaseModel
from .classes import SessionType
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

class ConfigData(BaseModel):
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

class TriggerMessage(str, Enum):
    status_notification = "StatusNotification"
    meter_values = "MeterValues"
    diagnostics_status = "DiagnosticsStatusNotification"
    firmware_status = "FirmwareStatusNotification"