from ocpp.charge_point import ChargePoint as cp
from ocpp.v16 import call, call_result


class ChargePoint(cp):
    _call = call
    _call_result = call_result
    _ocpp_version = "1.6"
