from ocpp.routing import after, create_route_map, on
from ocpp.v16.enums import Action


def test_create_route_map():
    """
    This test validates that route map is created correctly and holds all
    functions decorated with the @on() and @after decorators.

    """

    class ChargePoint:
        @on(Action.Heartbeat, skip_schema_validation=True)
        def on_heartbeat(self):
            pass

        @after(Action.Heartbeat)
        def after_heartbeat(self):
            pass

        @on(Action.MeterValues)
        def meter_values(self):
            pass

        def undecorated(self):
            pass

    cp = ChargePoint()
    route_map = create_route_map(cp)

    assert route_map == {
        Action.Heartbeat: {
            "_on_action": cp.on_heartbeat,
            "_after_action": cp.after_heartbeat,
            "_skip_schema_validation": True,
            "_extension": None,
        },
        Action.MeterValues: {
            "_on_action": cp.meter_values,
            "_skip_schema_validation": False,
            "_extension": None,
        },
    }
