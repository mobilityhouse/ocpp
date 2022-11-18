from ocpp.charge_point import ChargePoint as cp
from ocpp.messages import SchemaValidator


class ChargePoint(cp):
    _schema_validator = SchemaValidator(ocpp_version="2.0.1")
