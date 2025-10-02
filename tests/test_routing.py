from ocpp.routing import after, create_route_map, on
from ocpp.v16.enums import Action


def test_create_route_map():
    """
    This test validates that route map is created correctly and holds all
    functions decorated with the @on() and @after decorators.

    """

    class ChargePoint:
        @on(Action.heartbeat, skip_schema_validation=True)
        def on_heartbeat(self):
            pass

        @after(Action.heartbeat)
        def after_heartbeat(self):
            pass

        @on(Action.meter_values)
        def meter_values(self):
            pass

        def undecorated(self):
            pass

    cp = ChargePoint()
    route_map = create_route_map(cp)

    assert route_map == {
        Action.heartbeat: {
            "_on_action": cp.on_heartbeat,
            "_after_action": cp.after_heartbeat,
            "_skip_schema_validation": True,
        },
        Action.meter_values: {
            "_on_action": cp.meter_values,
            "_skip_schema_validation": False,
        },
    }
