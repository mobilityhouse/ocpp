from ocpp.charge_point import ChargePoint as cp
from ocpp.messages import OCPPVersion, SchemaValidator


class ChargePoint(cp):
    _schema_validator = SchemaValidator(ocpp_version=OCPPVersion.v20)
