from sqlalchemy import Column, Integer, String
from .database import Base
from datetime import datetime
from .classes import SessionType


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    password = Column(String)

class ChargePoint(Base):
    __tablename__ = "charge_points"
    id = Column(Integer, primary_key=True, index=True)
    charge_point_id = Column(String)
    password = Column(String)
    charge_point_name = Column(String)

class ChargePointTasks(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True, index=True)
    chargers = dict()

class ChargePointSessions(Base):
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