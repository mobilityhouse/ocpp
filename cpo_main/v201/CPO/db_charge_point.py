from sqlalchemy.orm import Session
from database.database import get_db, engine
from v201.CPO import models

db = Session(bind=engine)

async def save_charge_point(charge_point_serial_number, charge_point_vendor, charge_point_model, firmware_version):
    serial_numbers = db.query(models.ChargePoint).filter_by(models.ChargePoint.charge_point_serial_number)
    print (serial_numbers)
    if charge_point_serial_number == serial_numbers:
        return
    elif charge_point_serial_number != serial_numbers:
        new_charge_point = models.ChargePoint(
            charge_point_serial_number=charge_point_serial_number,
            charge_point_vendor=charge_point_vendor,
            charge_point_model=charge_point_model,
            firmware_version=firmware_version)
        db.add(new_charge_point)
        db.commit()
        db.refresh(new_charge_point)
        return new_charge_point