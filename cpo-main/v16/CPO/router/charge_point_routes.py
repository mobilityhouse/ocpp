from datetime import timedelta
from ocpp import charge_point
from .. import schemas, models, oauth2
from ..database import get_db
from sqlalchemy.orm import Session
from ..hashing import Hash
from ...charge_point_operator import CentralSystem
from fastapi import APIRouter, Depends, WebSocket, WebSocketDisconnect, HTTPException, status
from ...cpo_class import ChargePoint
from ..classes import WebsocketAdapter
from ...charge_point_operator import CentralSystem
from fastapi.security import OAuth2PasswordRequestForm
from .. import token, database


router = APIRouter(tags=["Charge Point"])
cpo = CentralSystem()


"""
REGISTER
Function to connect a Charge Point to the CPO through websockets
Done
"""

@router.websocket("/chargepoints/{client_id}")
async def websocket_endpoint(websocket: WebSocket, client_id: str):
    try:
        await websocket.accept(subprotocol="ocpp1.6")
        print("st")
        cp_id = websocket.url.path.strip("/chargepoints")
        print("Stop")
        cp = ChargePoint(cp_id, WebsocketAdapter(websocket))
        print("Stopp")
        queue = cpo.register_charger(cp)
        await queue.get()

    except WebSocketDisconnect:
        socket = WebsocketAdapter()
        await socket.disconnect(websocket)


"""
Get Charge Points
GET a Charge Point connected to the CPO
Done
"""

@router.get("/chargepoints/{charge_point_id}")
async def get_charge_point(charge_point_id: str, request: schemas.ChargePoint = Depends(oauth2.get_current_user),
db: Session = Depends(get_db)):
    charge_point = db.query(models.ChargePoint).filter(models.ChargePoint.charge_point_id == charge_point_id).first()
    return charge_point


"""
Get Charging Sessions
GET all active Charging Sessions on a Charge Point
Under development
"""

@router.get("/chargepoints/{charge_point_id}/chargingsessions")
async def get_charge_point_session(request: schemas.ChargingSession, charge_point_id: str,
start_time: str, end_time: str, max_count: int, db: Session = Depends(get_db)):
    charge_point_session = db.query(models.ChargePointSessions).filter(models.ChargePointSessions.charge_point_id == 
        charge_point_id).first()
    return charge_point_session


"""
Get ONE Charging Session
GET a specific Charging Session with session ID
Under development
"""

@router.get("/chargepoints/{charge_point_id}/chargingsessions/{charging_session_id}")
async def get_charge_point_session_id(request: schemas.ChargingSession,charge_point_id: str, charging_session_id: int,
db: Session = Depends(get_db)):
    charge_point_session = db.query(models.ChargePointSessions).filter(models.ChargePointSessions.charging_session_id == 
        charging_session_id).first()
    return charge_point_session


"""
Get Connector related Charging Sessions
GET the Charging Sessions relevant to a connector
Under development
"""

@router.get("/chargepoints/{charge_point_id}/connectors/{connector_id}/chargingsessions")
async def get_connector_session( charge_point_id: str, connector_id: int, request: schemas.ChargingSession = Depends(), 
db: Session = Depends(get_db)):
    charge_point_session = db.query(models.ChargePointSessions).filter(models.ChargePointSessions.connector_id == 
        connector_id).first()
    return charge_point_session


"""
Start a Charging Session
PUT a Remote Start request to start charging
Done
"""

@router.put("/chargepoints/{charge_point_id}/connectors/{connector_id}/remotestart")
async def remote_start(request: schemas.ChargeSession, charge_point_id: str, connector_id: int):
    cp_id = charge_point_id
    id_tag = request.username
    connector_id = connector_id
    try:
        get_response = await cpo.start_remote(cp_id, id_tag, connector_id)
        print(f"==> The response from charger==> {get_response}")
        return {'status': "Accepted"}
    except Exception as e:
        return(f"Failed to start remote charging: {e}")


"""
Stop a Charging Session
PUT a Remote Stop request to stop the charging session
Need Transaction ID Implemented
"""

@router.put("/chargepoints/{charge_point_id}/connectors/{connector_id}/remotestop")
async def remote_stop(charge_point_id: str, connector_id: int):
    cp_id = charge_point_id
    connector_id = connector_id
    try:
        get_response = await cpo.stop_remote(cp_id, connector_id)
        print(f"==> The response from charger==> {get_response}")
        return {'status': "Accepted"}
    except Exception as e:
        return(f"Failed to start remote charging: {e}")


"""
Get Configurations of a connector
GET Configurations set to a connector
Done
"""

@router.get("/chargepoints/{charge_point_id}/connectors/{connector_id}/configure")
async def get_connector_config(request: schemas.ViewConnectorCofiguration, charge_point_id:str, connector_id: int):
    cp_id = charge_point_id
    key = request.key
    try:
        get_response = await cpo.get_configuration(cp_id, key)
        print(f"==> The response from charger==> {get_response}")
        return {'status': "Accepted"}
    except Exception as e:
        return(f"Failed to start remote charging: {e}")

"""
Configure Connector
PUT a request to change Configuration within the ConfigurationKey Enum
Done
"""

@router.put("/chargepoints/{charge_point_id}/connectors/{connector_id}/configure")
async def put_connector_config(request: schemas.CreateConnectorConfiguration, charge_point_id: str, connector_id: int):
    cp_id = charge_point_id
    key = request.key
    value = request.value
    try:
        get_response = await cpo.change_configuration(cp_id, key, value)
        print(f"==> The response from charger==> {get_response}")
        return {'status': "Accepted"}
    except Exception as e:
        return(f"Failed to start remote charging: {e}")


"""
Reset Charge Point
PUT a request to reset Charge Point
Done
"""

@router.put("/chargepoints/{charge_point_id}/reset")
async def reset(request: schemas.Reset, charge_point_id: str):
    cp_id = charge_point_id
    type = request.type
    try:
        get_response = await cpo.reset(cp_id, type)
        print(f"==> The response from charger==> {get_response}")
        return {'status': "Accepted"}
    except Exception as e:
        return(f"Failed to start remote charging: {e}")



"""
Register a Charge Point
PUT a Register request and store in database
Done
"""

@router.post("/chargepoints/{charge_point_id}/register")
async def register(charge_point_id: str, request: schemas.ChargePointRegistrationInfo = Depends(), db: Session = Depends(get_db)):
    new_charge_point = models.ChargePoint(charge_point_id=request.charge_point_id, password=Hash.bcrypt(request.password),
        charge_point_name = request.charge_point_name)
    db.add(new_charge_point)
    db.commit()
    db.refresh(new_charge_point)
    return new_charge_point

"""
Get Charge Point Schedule
GET all the Schedules registered to a Charge Point
Under development
Not Essential
"""

@router.get("/chargepoints/{charge_point_id}/schedule")
async def get_schedule(request: schemas.Schedule, charge_point_id: str):
    cp_id = charge_point_id
    connector_id = request.connector_id
    duration = request.duration
    charging_rate_unit = request.charging_rate_unit
    try:
        get_response = await cpo.get_schedule(cp_id, connector_id, duration, charging_rate_unit)
        print(f"==> The response from charger==> {get_response}")
        return {'status': "Accepted"}
    except Exception as e:
        return(f"Failed to start remote charging: {e}")


"""
Register a Schedule
PUT a Schedule with charging behavior of a Charge Point
Not Started
Not Essential
"""

@router.put("/chargepoints/{charge_point_id}/schedule")
async def put_schedule(request: schemas.Schedule, charge_point_id: str):
    cp_id = charge_point_id
    return {'status': "Accepted"}


"""
Register a Schedule
POST a Schedule with charging behavior of a Charge Point
Not started
Not Essential
"""

@router.post("/chargepoints/{charge_point_id}/schedule")
async def post_schedule(request: schemas.Schedule, charge_point_id: str):
    cp_id = charge_point_id
    return {'status': "Accepted"}


"""
Get Schedule
GET a specific Schedule of a Charge Point
Not started
Not Essential
"""

@router.get("/chargepoints/{charge_point_id}/schedule/{schedule_id}")
async def get_schedule_id(request: schemas.Schedule, charge_point_id: str):
    cp_id = charge_point_id
    return {'status': "Accepted"}


"""
Delete a Schedule
Not started
Not Essential
"""

@router.delete("/chargepoints/{charge_point_id}/schedule/{schedule_id}")
async def get_schedule_id(charge_point_id: str, schedule_id: int):
    cp_id = charge_point_id
    return {'status': "Accepted"}


"""
Get Charge Point Configurations
GET a specific Configuration of a Charge Point
Under development
"""

@router.get("/chargepoints/{charge_point_id}/configure")
async def get_config(request: schemas.ChargePointConfiguration, charge_point_id:str):
    cp_id = charge_point_id
    key = request.key
    try:
        get_response = await cpo.get_configuration(cp_id, key)
        print(f"==> The response from charger==> {get_response}")
        return {'status': "Accepted"}
    except Exception as e:
        return(f"Failed to start remote charging: {e}")


"""
Configure Charge Point
PUT a Configure to a Charge Point within the ConfigurationKey Enum
Under development
"""

@router.put("/chargepoints/{charge_point_id}/configure")
async def put_config(request: schemas.ChargePointConfiguration, charge_point_id:str):
    cp_id = charge_point_id
    key = request.key
    value = request.value
    try:
        get_response = await cpo.change_configuration(cp_id, key, value)
        print(f"==> The response from charger==> {get_response}")
        return {'status': "Accepted"}
    except Exception as e:
        return(f"Failed to start remote charging: {e}")



"""
Get Status of Charge Point
GET a Status Notification from a Charge Point by sending a Trigger Message
Under development
"""

@router.get("/chargepoints/{charge_point_id}/status")
async def get_status(request: schemas.ChargePointStatus, charge_point_id:str):
    cp_id = charge_point_id
    requested_message = "StatusNotification"
    connector_id = connector_id
    try:
        get_response = await cpo.trigger(cp_id, requested_message, connector_id)
        print(f"==> The response from charger==> {get_response}")
        return {'status': "Accepted"}
    except Exception as e:
        return(f"Failed to start remote charging: {e}")


"""
Unregister a Charge Point
PUT a request to Unregister a Charge Point
Not started
"""

@router.put("/chargepoints/{charge_point_id}/unregister")
async def put_unregister(request: schemas.ChargePointAuth, charge_point_id: str, db: Session =Depends(get_db)):
    charge_point = db.query(models.ChargePoint).filter(models.ChargePoint.charge_point_id ==
         request.charge_point_id, models.ChargePoint.password == request.password).delete(synchronize_session=False)
    db.commit()
    return {'status': 'Charge Point deleted'}


"""
Get all Charge Points
GET all Charge Points that are connected to the CPO
Not started
"""

@router.get("/chargepoints/owned")
async def get_owned(request: schemas.ChargePoint = Depends(), db: Session = Depends(get_db)):
    charge_points = db.query(models.ChargePoint).all()
    return charge_points

