from .. import schemas, models, oauth2
from ..database import get_db
from sqlalchemy.orm import Session
from ..hashing import Hash
from ...charge_point_operator import CentralSystem
from fastapi import APIRouter, Depends, WebSocket, WebSocketDisconnect
from ...cpo_class import ChargePoint
from ..classes import WebsocketAdapter
from ...charge_point_operator import CentralSystem


router = APIRouter(tags=["Charge Point"])
cpo = CentralSystem()

@router.websocket("/chargepoints/{client_id}")
async def websocket_endpoint(websocket: WebSocket, client_id: str):
    try:
        await websocket.accept(subprotocol="ocpp1.6")
        cp_id = websocket.url.path.strip("/chargepoints")
        cp = ChargePoint(cp_id, WebsocketAdapter(websocket))
        queue = cpo.register_charger(cp)
        await queue.get()

    except WebSocketDisconnect:
        socket = WebsocketAdapter()
        await socket.disconnect(websocket)

@router.get("/chargepoints/{charge_point_id}")
async def get_charge_point(charge_point_id: str, db: Session = Depends(get_db),
        get_charge_point: schemas.ChargePoint = Depends(oauth2.get_current_user)):
    charge_point = db.query(models.ChargePoint).filter(models.ChargePoint.charge_point_id ==
         charge_point_id)
    return charge_point

@router.get("/chargepoints/{charge_point_id}/chargingsessions")
async def get_charge_point_session(charge_point_id: str, start_time: str, end_time: str, max_count: int,
        db: Session = Depends(get_db)):
    charge_point_session = db.query(models.ChargePointSessions).filter(models.ChargePointSessions.charge_point_id == 
        charge_point_id)
    return charge_point_session


@router.get("/chargepoints/{charge_point_id}/chargingsessions/{charging_session_id}")
async def get_charge_point_session_id(charge_point_id: str, charging_session_id: int,
        db: Session = Depends(get_db)):
    charge_point_session = db.query(models.ChargePointSessions).filter(models.ChargePointSessions.charging_session_id == 
        charging_session_id)
    return charge_point_session

@router.get("/ws/chargepoints/{charge_point_id}/connectors/{connector_id}/chargingsessions")
async def get_connector_session(charge_point_id: str, connector_id: int, db: Session = Depends(get_db)):
    charge_point_session = db.query(models.ChargePointSessions).filter(models.ChargePointSessions.connector_id == 
        connector_id)
    return charge_point_session

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

@router.get("/chargepoints/{charge_point_id}/connectors/{connector_id}/configure")
async def get_connector_config(request: schemas.GetConfig, charge_point_id:str):
    cp_id = charge_point_id
    key = request.key
    try:
        get_response = await cpo.get_configuration(cp_id, key)
        print(f"==> The response from charger==> {get_response}")
        return {'status': "Accepted"}
    except Exception as e:
        return(f"Failed to start remote charging: {e}")

@router.put("/chargepoints/{charge_point_id}/connectors/{connector_id}/configure")
async def put_connector_config(request: schemas.ConfigData, charge_point_id: str):
    cp_id = charge_point_id
    key = request.key
    value = request.value
    try:
        get_response = await cpo.change_configuration(cp_id, key, value)
        print(f"==> The response from charger==> {get_response}")
        return {'status': "Accepted"}
    except Exception as e:
        return(f"Failed to start remote charging: {e}")

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

@router.put("/chargepoints/{charge_point_id}/register")
async def register(charge_point_id, request: schemas.ChargePoint, db: Session = Depends(get_db)):
    new_charge_point = models.ChargePoint(charge_point_id=request.charge_point_id, password=Hash.bcrypt(request.password),
        charge_point_name=request.charge_point_name)
    db.add(new_charge_point)
    db.commit()
    db.refresh(new_charge_point)
    return new_charge_point

@router.get("/chargepoints/{charge_point_id}/schedule")
async def get_schedule(request: schemas.GetSchedule, charge_point_id: str):
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

@router.put("/chargepoints/{charge_point_id}/schedule")
async def put_schedule():
    return {'status': "Accepted"}

@router.post("/chargepoints/{charge_point_id}/schedule")
async def post_schedule():
    return {'status': "Accepted"}

@router.get("/chargepoints/{charge_point_id}/schedule/{schedule_id}")
async def get_schedule_id():
    return {'status': "Accepted"}

@router.delete("/chargepoints/{charge_point_id}/schedule/{schedule_id}")
async def get_schedule_id():
    return

@router.get("/chargepoints/{charge_point_id}/configure")
async def get_config(request: schemas.GetConfig, charge_point_id:str):
    cp_id = charge_point_id
    key = request.key
    try:
        get_response = await cpo.get_configuration(cp_id, key)
        print(f"==> The response from charger==> {get_response}")
        return {'status': "Accepted"}
    except Exception as e:
        return(f"Failed to start remote charging: {e}")

@router.put("/chargepoints/{charge_point_id}/configure")
async def put_config(request: schemas.ConfigData, charge_point_id:str):
    cp_id = charge_point_id
    key = request.key
    value = request.value
    try:
        get_response = await cpo.change_configuration(cp_id, key, value)
        print(f"==> The response from charger==> {get_response}")
        return {'status': "Accepted"}
    except Exception as e:
        return(f"Failed to start remote charging: {e}")

@router.get("/chargepoints/{charge_point_id}/status")
async def get_status(charge_point_id:str, connector_id):
    cp_id = charge_point_id
    requested_message = "StatusNotification"
    connector_id = connector_id
    try:
        get_response = await cpo.trigger(cp_id, requested_message, connector_id)
        print(f"==> The response from charger==> {get_response}")
        return {'status': "Accepted"}
    except Exception as e:
        return(f"Failed to start remote charging: {e}")

@router.put("/chargepoints/{charge_point_id}/unregister")
async def put_unregister():
    return {'status': "Accepted"}

@router.get("/chargepoints/owned")
async def get_owned():
    return {'status': "Accepted"}

