from ocpp.charge_point import ChargePoint as cp


class ChargePoint(cp):
    def __init__(self, *args, **kwargs):
        super().__init__(ocpp_version='2.0', *args, **kwargs)
