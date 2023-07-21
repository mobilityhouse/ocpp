from typing import Optional

from ocpp.charge_point import ChargePoint as cp
from ocpp.messages import SchemaValidator
from ocpp.v21 import call, call_result


class ChargePoint(cp):
    _call = call
    _call_result = call_result
    _ocpp_version = "2.1"

    def __init__(
        self,
        id,
        connection,
        validator: Optional[SchemaValidator] = None,
        *args,
        **kwargs
    ):
        # The ocpp package doesn't come with the JSON schemas for OCPP 2.1.
        if validator is None:
            raise RuntimeError(
                "Failed to initiate `ChargePoint` implementing OCPP 2.1: `validator` is not set. The ocpp package doesn't come with JSON schemas for OCPP 2.1. See https://github.com/mobilityhouse/ocpp/issues/458 for more information."
            )

        super().__init__(id, connection, validator, *args, **kwargs)
