from typing import Optional
from pydantic import BaseModel
from .classes import SessionType
from datetime import datetime
from ocpp.v16.enums import ConfigurationKey, ResetType, ChargingRateUnitType

from pydantic import BaseModel

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
    username: Optional[str] = None

class ChargePoint(BaseModel):
    charge_point_id: str
    password: str
    charge_point_name: str

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

class GetSchedule(BaseModel):
    connector_id: int
    duration: int
    charging_rate_unit: ChargingRateUnitType