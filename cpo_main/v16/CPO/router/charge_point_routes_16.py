from v16.CPO import schemas, oauth2
from database.database import get_db
from database import models
from sqlalchemy.orm import Session
from v16.CPO.hashing import Hash
from fastapi import APIRouter, Depends, WebSocket, WebSocketDisconnect
from v16.cpo_class import ChargePoint
from v16.CPO.classes import WebsocketAdapter
from v16.charge_point_operator import CentralSystem
from ocpp.v16.enums import *
from v16.CPO.hashing import Hash


router = APIRouter(tags=["Charge Point"])
cpo = CentralSystem()


"""
REGISTER
Function to connect a Charge Point to the CPO through websockets
Done
"""

@router.websocket("/{client_id}")
async def websocket_endpoint(websocket: WebSocket, client_id: str):
    print(websocket.url.path)
    try:
        await websocket.accept(subprotocol="ocpp1.6")
        charge_point_id = websocket.url.path.strip("v16/api/v16")
        cp = ChargePoint(charge_point_id, WebsocketAdapter(websocket))
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

@router.get("/chargepoints/{charge_point_id}", response_model=schemas.ChargePoint)
async def get_charge_point(charge_point_id: str, request: schemas.ChargePoint,
db: Session = Depends(get_db), get_current_user: schemas.User = Depends(oauth2.get_current_user)):
    charge_point = db.query(models.ChargePoint).filter(models.ChargePoint.charge_point_id == charge_point_id).first()
    return charge_point


"""
Get Charging Sessions
GET all active Charging Sessions on a Charge Point
Under development
"""

@router.get("/chargepoints/{charge_point_id}/chargingsessions", response_model=schemas.ChargeSession)
async def get_charge_point_session(charge_point_id: str, request: schemas.ChargingSession,
db: Session = Depends(get_db), get_current_user: schemas.User = Depends(oauth2.get_current_user)):
    charge_point_session = db.query(models.ChargePointSessions).filter(models.ChargePointSessions.charge_point_id == 
        charge_point_id).first()
    return charge_point_session


"""
Get ONE Charging Session
GET a specific Charging Session with session ID
Under development
"""

@router.get("/chargepoints/{charge_point_id}/chargingsessions/{charging_session_id}", response_model=schemas.ChargeSession)
async def get_charge_point_session_id(charge_point_id: str, charging_session_id: int,
request: schemas.ChargingSession, db: Session = Depends(get_db),
get_current_user: schemas.User = Depends(oauth2.get_current_user)):
    charge_point_session = db.query(models.ChargePointSessions).filter(models.ChargePointSessions.charging_session_id == 
        charging_session_id).first()
    return charge_point_session


"""
Get Connector related Charging Sessions
GET the Charging Sessions relevant to a connector
Under development
"""

@router.get("/chargepoints/{charge_point_id}/connectors/{connector_id}/chargingsessions", response_model=schemas.ChargeSession)
async def get_connector_session(charge_point_id: str, connector_id: int, request: schemas.ChargingSession, 
db: Session = Depends(get_db), get_current_user: schemas.User = Depends(oauth2.get_current_user)):
    charge_point_session = db.query(models.ChargePointSessions).filter(models.ChargePointSessions.connector_id == 
        connector_id).first()
    return charge_point_session


"""
Start a Charging Session
PUT a Remote Start request to start charging
Done
"""

@router.put("/chargepoints/{charge_point_id}/connectors/{connector_id}/remotestart")
async def remote_start( charge_point_id: str, connector_id: int,
request: schemas.ChargeSession, get_current_user: schemas.User = Depends(oauth2.get_current_user)):
    charge_point_id = charge_point_id
    id_tag = request.username
    connector_id = connector_id
    try:
        get_response = await cpo.start_remote(charge_point_id, id_tag, connector_id)
        print(f"==> The response from charger==> {get_response}")
        return get_response
    except Exception as e:
        return(f"Failed to start remote charging: {e}")


"""
Stop a Charging Session
PUT a Remote Stop request to stop the charging session
Need Transaction ID Implemented
"""

@router.put("/chargepoints/{charge_point_id}/connectors/{connector_id}/remotestop")
async def remote_stop(charge_point_id: str, connector_id: int, transaction_id: int,
get_current_user: schemas.User = Depends(oauth2.get_current_user)):
    try:
        get_response = await cpo.stop_remote(charge_point_id, connector_id, transaction_id)
        print(f"==> The response from charger==> {get_response}")
        return get_response
    except Exception as e:
        return(f"Failed to stop remote charging: {e}")


"""
Get Configurations of a connector
GET Configurations set to a connector
Done
"""

@router.get("/chargepoints/{charge_point_id}/connectors/{connector_id}/configure", response_model=schemas.ViewConnectorCofiguration)
async def get_connector_config( charge_point_id:str, connector_id: int, key: str,
request: schemas.ViewConnectorCofiguration,
get_current_user: schemas.User = Depends(oauth2.get_current_user)):
    try:
        get_response = await cpo.get_configuration(charge_point_id, key)
        print(f"==> The response from charger==> {get_response}")
        return get_response
    except Exception as e:
        return(f"Failed to start remote charging: {e}")

"""
Configure Connector
PUT a request to change Configuration within the ConfigurationKey Enum
Done
"""

@router.put("/chargepoints/{charge_point_id}/connectors/{connector_id}/configure")
async def put_connector_config(charge_point_id: str, connector_id: int, key: str, value: int,
request: schemas.CreateConnectorConfiguration,
get_current_user: schemas.User = Depends(oauth2.get_current_user)):
    try:
        get_response = await cpo.change_configuration(charge_point_id, key, value)
        print(f"==> The response from charger==> {get_response}")
        return get_response
    except Exception as e:
        return(f"Failed to start remote charging: {e}")


"""
Reset Charge Point
PUT a request to reset Charge Point
Done
"""

@router.put("/chargepoints/{charge_point_id}/reset")
async def reset(charge_point_id: str, request: schemas.Reset,
get_current_user: schemas.User = Depends(oauth2.get_current_user)):
    type = request.type
    try:
        get_response = await cpo.reset(charge_point_id, type)
        print(f"==> The response from charger==> {get_response}")
        return get_response
    except Exception as e:
        return(f"Failed to start remote charging: {e}")



"""
Register a Charge Point
PUT a Register request and store in database
Done
"""

@router.put("/chargepoints/{charge_point_id}/register")
async def register(charge_point_id: str, charge_point_serial_number: str,
request: schemas.ChargePointRegistrationInfo, db: Session = Depends(get_db),
get_current_user: schemas.User = Depends(oauth2.get_current_user)):
    if charge_point_serial_number == models.ChargePoint.charge_point_serial_number:
        update_charge_point = models.ChargePoint(charge_point_id=request.charge_point_id, password=Hash.bcrypt(request.password),
            charge_point_name = request.charge_point_name)
        db.commit()
        db.refresh(update_charge_point)
        return update_charge_point

"""
Get Charge Point Schedule
GET all the Schedules registered to a Charge Point
Under development
Not Essential
"""

@router.get("/chargepoints/{charge_point_id}/schedule", response_model=schemas.Schedule)
async def get_schedule(charge_point_id: str, request: schemas.Schedule,
get_current_user: schemas.User = Depends(oauth2.get_current_user), db: Session = Depends(get_db)):
    get_schedule = db.query(models.Schedule).all()
    return get_schedule


"""
Register a Schedule
PUT a Schedule with charging behavior of a Charge Point
Not Started
Not Essential
"""

@router.put("/chargepoints/{charge_point_id}/schedule")
async def put_schedule(charge_point_id: str, request: schemas.Schedule,
get_current_user: schemas.User = Depends(oauth2.get_current_user), db: Session = Depends(get_db)):
    db.query(models.Schedule).filter(models.Schedule.id ==
        id).update(request)
    db.commit()
    return {'status': "Accepted"}


"""
Register a Schedule
POST a Schedule with charging behavior of a Charge Point
Not started
Not Essential
"""

@router.post("/chargepoints/{charge_point_id}/schedule")
async def post_schedule(charge_point_id: str, request: schemas.Schedule,
get_current_user: schemas.User = Depends(oauth2.get_current_user), db: Session = Depends(get_db)):
    new_schedule = models.Schedule(
        charge_point_id=request.charge_point_id,
        name=request.name,
        active=request.active,
        start_hours=request.start_hours,
        start_minutes=request.start_minutes,
        end_hours=request.end_hours,
        end_minutes=request.end_minutes,
        time_zone=request.time_zone,
        monday=request.monday,
        tuesday=request.tuesday,
        wednesday=request.wednesday,
        thursday=request.thursday,
        friday=request.friday,
        saturday=request.saturday,
        sunday=request.sunday,
        connector_id_list=request.connector_id_list
    )
    db.add(new_schedule)
    db.commit()
    db.refresh(new_schedule)
    return new_schedule


"""
Get Schedule
GET a specific Schedule of a Charge Point
Not started
Not Essential
"""

@router.get("/chargepoints/{charge_point_id}/schedule/{schedule_id}", response_model=schemas.Schedule)
async def get_schedule_id(charge_point_id: str, schedule_id: int, request: schemas.Schedule,
get_current_user: schemas.User = Depends(oauth2.get_current_user), db: Session = Depends(get_db)):
    get_schedule = db.query(models.Schedule).filter(models.Schedule.id == schedule_id).first()
    return get_schedule


"""
Delete a Schedule
Not started
Not Essential
"""

@router.delete("/chargepoints/{charge_point_id}/schedule/{schedule_id}")
async def get_schedule_id(charge_point_id: str, schedule_id: int, request: schemas.Schedule,
get_current_user: schemas.User = Depends(oauth2.get_current_user), db: Session = Depends(get_db)):
    schedule = db.query(models.Schedule).filter(models.Schedule.id ==
         schedule_id).delete(synchronize_session=False)
    db.commit()
    return {"status": "Schedule Deleted"}


"""
Get Charge Point Configurations
GET a specific Configuration of a Charge Point
Done
"""

@router.get("/chargepoints/{charge_point_id}/configure", response_model=schemas.Configuration)
async def get_config(charge_point_id:str, key: schemas.ConfigurationKey,
get_current_user: schemas.User = Depends(oauth2.get_current_user)):
    key = [key]
    try:
        get_response = await cpo.get_configuration(charge_point_id, key)
        print(f"==> The response from charger==> {get_response}")
        return get_response
    except Exception as e:
        return(f"Failed to get configuration: {e}")


"""
Configure Charge Point
PUT a Configure to a Charge Point within the ConfigurationKey Enum
Done
"""

@router.put("/chargepoints/{charge_point_id}/configure")
async def put_config(request: schemas.Configuration, charge_point_id:str,
get_current_user: schemas.User = Depends(oauth2.get_current_user)):
    key = request.key
    value = request.value
    try:
        get_response = await cpo.change_configuration(charge_point_id, key, value)
        print(f"==> The response from charger==> {get_response}")
        return get_response
    except Exception as e:
        return(f"Failed to change configuration: {e}")



"""
Get Trigger Message of Charge Point
GET a Status Notification from a Charge Point by sending a Trigger Message
Done
"""

@router.get("/chargepoints/{charge_point_id}/trigger", response_model=schemas.Trigger)
async def get_status(charge_point_id:str, connector_id: int, requested_message: schemas.Trigger,
get_current_user: schemas.User = Depends(oauth2.get_current_user)):
    try:
        get_response = await cpo.trigger(charge_point_id, requested_message, connector_id)
        print(f"==> The response from charger==> {get_response}")
        return get_response
    except Exception as e:
        return(f"Failed to GET Status: {e}")

@router.put("/chargepoints/{charge_point_id}/unlock")
async def get_status(charge_point_id:str, connector_id: int):
    try:
        get_response = await cpo.unlock_connector(charge_point_id, connector_id)
        print(f"==> The response from charger==> {get_response}")
        return get_response
    except Exception as e:
        return(f"Failed to unlock connector: {e}")


"""
Unregister a Charge Point
PUT a request to Unregister a Charge Point
Done
"""

@router.put("/chargepoints/{charge_point_id}/unregister")
async def put_unregister(request: schemas.ChargePointAuth, charge_point_id: str, db: Session = Depends(get_db),
get_current_user: schemas.User = Depends(oauth2.get_current_user)):
    charge_point = db.query(models.ChargePoint).filter(models.ChargePoint.charge_point_id ==
         request.charge_point_id, models.ChargePoint.password == request.password).delete(synchronize_session=False)
    db.commit()
    return {'status': 'Charge Point deleted'}


"""
Get all Charge Points
GET all Charge Points that are connected to the CPO
Done
"""

@router.get("/chargepoints/owned", response_model=schemas.ChargePoint)
async def get_owned(request: schemas.ChargePoint, db: Session = Depends(get_db),
get_current_user: schemas.User = Depends(oauth2.get_current_user)):
    charge_points = db.query(models.ChargePoint).all()
    return charge_points

