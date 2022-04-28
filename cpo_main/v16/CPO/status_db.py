from database import models
from database.database import SessionLocal
from datetime import datetime

db = SessionLocal()

async def meter_value_db(charge_point_id: str, connector_id: int, meter_value: list, transaction_id: int = None):
    for list in meter_value:
        timestamp = list['timestamp']
        timestamp = datetime.strptime(timestamp, '%Y-%m-%dT%H:%M:%S.%f')
        sampled_value = list['sampled_value']
        for sample in sampled_value:
            current_measure = db.query(models.MeterValues).filter_by(measurand=sample['measurand']).first()
            if not current_measure:
                meter = models.MeterValues(
                    transaction_id=transaction_id,
                    charge_point_id=charge_point_id,
                    timestamp=timestamp, 
                    connector_id=connector_id,  
                    measurand=sample['measurand'], 
                    value=sample['value'], 
                    context=sample['context'], 
                    format=sample['format'], 
                    phase=sample['phase'], 
                    location=sample['location'], 
                    unit=sample['unit']
                    )
                db.add(meter)
                db.commit()
                db.refresh(meter)
            else:
                meter = db.query(models.MeterValues).filter(models.MeterValues.transaction_id == transaction_id, models.MeterValues.measurand == 
                sample['measurand']).update({
                    "transaction_id":transaction_id,
                    "charge_point_id":charge_point_id,
                    "timestamp":timestamp, 
                    "connector_id":connector_id,  
                    "measurand":sample['measurand'], 
                    "value":sample['value'], 
                    "context":sample['context'], 
                    "format":sample['format'], 
                    "phase":sample['phase'], 
                    "location":sample['location'], 
                    "unit":sample['unit']
                })
                db.commit()
    return meter
    
async def status_db(charge_point_id, connector_id: int, error_code: str, status: str, timestamp: str = None, info: str = None,
    vendor_id: str = None, vendor_error_code: str = None):
    new_status = models.ChargePointStatus(
        charge_point_id=charge_point_id,
        connector_id=connector_id, 
        error_code= error_code,
        status = status, 
        status_timestamp=timestamp, 
        info=info, 
        vendor_id = vendor_id, 
        vendor_error_code = vendor_error_code
        )
    active_cp = db.query(models.ChargePointStatus).filter(models.ChargePointStatus.charge_point_id == charge_point_id).all()
    if not active_cp:
        db.add(new_status)
        db.commit()
        db.refresh(new_status)
        return new_status
    else:
        updated_status = db.query(models.ChargePointStatus).filter(models.ChargePointStatus.charge_point_id == charge_point_id).update({
        "charge_point_id":charge_point_id,
        "connector_id":connector_id, 
        "error_code": error_code,
        "status": status, 
        "status_timestamp":timestamp, 
        "info":info,
        "vendor_id": vendor_id, 
        "vendor_error_code": vendor_error_code
        })
        db.commit()
        return updated_status

async def boot_notification_db(charge_point_id: str, charge_point_vendor: str, charge_point_model: str, 
charge_point_serial_number: str = None, firmware_version: str = None, charge_box_serial_number: str = None, iccid: str = None, 
imsi: str = None, meter_serial_number: str = None, meter_type: str = None):
    boot = models.ChargePoint(
        charge_point_id=charge_point_id,
        charge_point_vendor=charge_point_vendor,
        charge_point_model=charge_point_model, 
        charge_point_serial_number=charge_point_serial_number,
        firmware_version=firmware_version,
        charge_box_serial_number=charge_box_serial_number,
        iccid=iccid,
        imsi =imsi, 
        meter_serial_number = meter_serial_number, 
        meter_type = meter_type
        )
    active_cp = db.query(models.ChargePoint).filter(models.ChargePoint.charge_point_id == charge_point_id).all()
    if not active_cp:
        db.add(boot)
        db.commit()
        db.refresh(boot)
        return boot
    else:
        updated_boot = db.query(models.ChargePoint).filter(models.ChargePoint.charge_point_id == charge_point_id).update({
        "charge_point_id":charge_point_id,
        "charge_point_vendor":charge_point_vendor,
        "charge_point_model":charge_point_model, 
        "charge_point_serial_number":charge_point_serial_number,
        "firmware_version":firmware_version,
        "charge_box_serial_number":charge_box_serial_number,
        "iccid":iccid,
        "imsi":imsi, 
        "meter_serial_number": meter_serial_number, 
        "meter_type": meter_type
        })
        db.commit()
        return updated_boot

async def heartbeat_db(charge_point_id, timestamp):
    heartbeat = db.query(models.ChargePoint).filter(models.ChargePoint.charge_point_id == charge_point_id).update({'heartbeat': timestamp})
    db.commit()
    return heartbeat

async def transaction_db(charge_point_id: str, transaction_id: int, id_tag: str, meter_start:int, timestamp:str, reservation_id: str= None):
    transaction = models.ChargePointSessions(
        transaction_id=transaction_id,
        charge_point_id=charge_point_id,
        id_tag=id_tag,
        meter_start=meter_start,
        timestamp=timestamp,
        reservation_id=reservation_id
    )
    active_transaction = db.query(models.ChargePointSessions).filter(models.ChargePointSessions.charge_point_id == charge_point_id).all()
    if not active_transaction:
        db.add(transaction)
        db.commit()
        db.refresh(transaction)
        return transaction
    else:
        updated_transaction = db.query(models.ChargePointSessions).filter(models.ChargePointSessions.charge_point_id == charge_point_id).update({
            "transaction_id":transaction_id,
            "charge_point_id":charge_point_id,
            "id_tag":id_tag,
            "meter_start":meter_start,
            "timestamp":timestamp,
            "reservation_id":reservation_id
        })
        db.commit()
        return updated_transaction

async def stop_transaction_db(charge_point_id:str, transaction_id: int, id_tag: str, meter_stop:int, timestamp:str, reason:str, transaction_data:list):
    pass