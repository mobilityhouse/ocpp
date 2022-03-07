from fastapi import APIRouter, Depends
from .. import schemas, models, oauth2
from ..database import get_chargepoint
from sqlalchemy.orm import Session
from ..hashing import Hash
from ...charge_point_operator import CentralSystem

router = APIRouter(tags=["Charge Point"])

@router.get("/chargepoints/{charge_point_id}")
async def get_charge_point(charge_point_id: str, db: Session = Depends(get_chargepoint),
        get_charge_point: schemas.ChargePoint = Depends(oauth2.get_current_user)):
    charge_point = db.query(models.ChargePoint).filter(models.ChargePoint.charge_point_id ==
         charge_point_id)
    return charge_point

@router.get("/chargepoints/{charge_point_id}/chargingsessions")
async def get_charge_point_session(charge_point_id: str, start_time: str, end_time: str, max_count: int,
        db: Session = Depends(get_chargepoint)):
    charge_point_session = db.query(models.ChargePointSessions).filter(models.ChargePointSessions.charge_point_id == 
        charge_point_id)
    return charge_point_session


@router.get("/chargepoints/{charge_point_id}/chargingsessions/{charging_session_id}")
async def get_charge_point_session_id(charge_point_id: str, charging_session_id: int,
        db: Session = Depends(get_chargepoint)):
    charge_point_session = db.query(models.ChargePointSessions).filter(models.ChargePointSessions.charging_session_id == 
        charging_session_id)
    return charge_point_session

@router.get("/ws/chargepoints/{charge_point_id}/connectors/{connector_id}/chargingsessions")
async def get_connector_session(charge_point_id: str, connector_id: int, db: Session = Depends(get_charge_point)):
    charge_point_session = db.query(models.ChargePointSessions).filter(models.ChargePointSessions.connector_id == 
        connector_id)
    return charge_point_session

@router.put("/chargepoints/{charge_point_id}/connectors/{connector_id}/remotestart")
async def remote_start(request: schemas.ChargeSession, charge_point_id: str, connector_id: int):
    cp_id = request.charge_point_id
    id_tag = request.username
    connector_id = request.connector_id
    transaction_id = 1
    try:
        await CentralSystem.start_remote(cp_id, id_tag, connector_id)
        return transaction_id
    except ValueError as e:
        return(f"Failed to start remote charging: {e}")


@router.put("/chargepoints/{charge_point_id}/connectors/{connector_id}/remotestop")
async def remote_stop(request: schemas.ChargeSession, charge_point_id: str, connector_id: int,
    get_auth: schemas.User = Depends(oauth2.get_current_user)):
    transaction_id = {'transaction_id': transaction_id}

@router.put("/chargepoints/{charge_point_id}/connectors/{connector_id}/configure")
async def get_connector_config():
    return {'status': "Accepted"}

@router.put("/chargepoints/{charge_point_id}/connectors/{connector_id}/configure")
async def put_connector_config():
    return {'status': "Accepted"}

@router.put("/chargepoints/{charge_point_id}/restart")
async def restart():
    return {'status': "Accepted"}

@router.put("/chargepoints/{charge_point_id}/register")
async def register(charge_point_id, request: schemas.ChargePoint, db: Session = Depends(get_chargepoint)):
    new_charge_point = models.ChargePoint(charge_point_id=request.charge_point_id, password=Hash.bcrypt(request.password),
        charge_point_name=request.charge_point_name)
    db.add(new_charge_point)
    db.commit()
    db.refresh(new_charge_point)
    return new_charge_point

@router.get("/chargepoints/{charge_point_id}/schedule")
async def get_schedule():
    return {'status': "Accepted"}

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
    return {'status': "Accepted"}

@router.get("/chargepoints/{charge_point_id}/configure")
async def get_config():
    return {'status': "Accepted"}

@router.put("/chargepoints/{charge_point_id}/configure")
async def put_config():
    return {'status': "Accepted"}

@router.get("/chargepoints/{charge_point_id}/status")
async def get_status():
    return {'status': "Accepted"}

@router.put("/chargepoints/{charge_point_id}/unregister")
async def put_unregister():
    return {'status': "Accepted"}

@router.get("/chargepoints/owned")
async def get_owned():
    return {'status': "Accepted"}