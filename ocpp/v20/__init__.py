import pathlib

from ocpp.charge_point import ChargePoint as cp
from ocpp.messages import SchemaValidator

schema_path = str(pathlib.Path(__file__).parent.joinpath("schemas").resolve())
validator = SchemaValidator(path_to_schemas=schema_path)


class ChargePoint(cp):
    _schema_validator = validator
