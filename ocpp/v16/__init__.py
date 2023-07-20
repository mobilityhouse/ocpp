import decimal
import json
import pathlib

from ocpp.charge_point import ChargePoint as cp
from ocpp.messages import SchemaValidator as sv
from ocpp.v16 import call, call_result


class SchemaValidator(sv):
    # Three OCPP 1.6 schedules have fields of type floats. The JSON schema
    # defines a precision of 1 decimal for these fields. A value of
    # 21.4 is valid, whereas a value if 4.11 is not.
    #
    # The problem is that Python's internal representation of 21.4 might
    # have more than 1 decimal. It might be 21.399999999999995. This would
    # make the validation fail, although the payload is correct. This is a
    # known issue with jsonschemas, see:
    # https://github.com/Julian/jsonschema/issues/247
    #
    # This issue can be fixed by using a different parser for floats than
    # the default one that is used.
    #
    # Both the schema and the payload must be parsed using the different
    # parser for floats.
    def validate_call(self, action: str, payload):
        if action in ["SetChargingProfile", "RemoteStartTransaction"]:
            payload = json.loads(json.dumps(payload), parse_float=decimal.Decimal)

        super().validate_call(action, payload)

    def validate_call_result(self, action: str, payload):
        if action == "GetCompositeSchedule":
            payload = json.loads(json.dumps(payload), parse_float=decimal.Decimal)

        super().validate_call_result(action, payload)


_schemas_dir = pathlib.Path(__file__).parent.joinpath("schemas").resolve()
validator = SchemaValidator(str(_schemas_dir))


class ChargePoint(cp):
    _call = call
    _call_result = call_result
    _ocpp_version = "1.6"

    def __init__(self, validator: SchemaValidator = validator, *args, **kwargs):
        super().__init__(validator=validator, *args, **kwargs)
