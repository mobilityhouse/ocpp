import pathlib

from ocpp.charge_point import ChargePoint as cp
from ocpp.messages import SchemaValidator
from ocpp.v201 import call, call_result

_schemas_dir = pathlib.Path(__file__).parent.joinpath("schemas").resolve()
validator = SchemaValidator(str(_schemas_dir))


class ChargePoint(cp):
    _call = call
    _call_result = call_result
    _ocpp_version = "2.0.1"

    def __init__(self, validator: SchemaValidator = validator, *args, **kwargs):
        super().__init__(validator=validator, *args, **kwargs)
