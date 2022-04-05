from sqlalchemy import Column, Integer, String
from database import Base_16
from datetime import datetime
from v16.CPO.classes import SessionType


class User(Base_16):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    password = Column(String)

class ChargePoint(Base_16):
    __tablename__ = "charge_point"
    id = Column(Integer, primary_key=True, index=True)
    charge_point_id = Column(String)
    password = Column(String)
    charge_point_name = Column(String)
    charge_point_vendor = Column(String)
    charge_point_model = Column(String)
    charge_point_serial_number = Column(String)
    firmware_version = Column(String)

class Token(Base_16):
    __tablename__ = "token"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    password = Column(String)
    token = Column(String)

class ChargePointSessions(Base_16):
    __tablename__ = "charging_sessions"
    id = Column(Integer, primary_key=True, index=True)
    charge_point_id: str
    connector_id: int
    organisation_id: str
    session_type: SessionType
    start_time: datetime
    end_time: datetime
    external_transaction_id: str
    total_consumption_kwh: int
    external_id: str
    charging_session_id: int

class Schedule(Base_16):
    __tablename__ = "schedule"
    id = Column(Integer, primary_key=True, index=True)
    charge_point_id: str
    name: str
    active: bool
    start_hours: int
    start_minutes: int
    end_hours: int
    end_minutes: int
    time_zone: str
    monday: bool
    tuesday: bool
    wednesday: bool
    thursday: bool
    friday: bool
    saturday: bool
    sunday: bool
    connector_id_list: str
