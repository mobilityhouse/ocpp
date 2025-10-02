from ocpp.routing import (
    after,
    after_message,
    before_message,
    create_route_map,
    discover_message_hooks,
    on,
)
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


def test_discover_message_hooks():
    """
    This test validates that message hooks is created correctly and holds all
    functions decorated with the @before_message and @after_message decorators.

    """

    class ChargePoint:
        @before_message
        def before_message_hook(self):
            pass

        @after_message
        def after_message_hook(self):
            pass

        def undecorated(self):
            pass

    cp = ChargePoint()
    hooks = discover_message_hooks(cp)

    assert hooks == {
        "before_message": [cp.before_message_hook],
        "after_message": [cp.after_message_hook],
    }


def test_discover_message_hooks_empty():
    """Test that discover_message_hooks works with no hooks."""

    class ChargePoint:
        @on(Action.heartbeat)
        def on_heartbeat(self):
            pass

        def undecorated(self):
            pass

    cp = ChargePoint()
    hooks = discover_message_hooks(cp)

    assert hooks == {
        "before_message": [],
        "after_message": [],
    }
