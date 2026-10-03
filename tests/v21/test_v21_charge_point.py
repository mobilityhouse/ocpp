import json

import pytest

from ocpp.messages import Call
from ocpp.v21 import ChargePoint
from ocpp.v21.enums import Action


@pytest.fixture
def base_central_system(connection):
    return ChargePoint(id=1234, connection=connection)


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "action",
    [
        # Action shared with OCPP 2.0.1.
        Action.heartbeat,
        # Actions introduced in OCPP 2.1.
        Action.battery_swap,
        Action.notify_der_alarm,
        Action.set_der_control,
    ],
)
async def test_route_message_with_no_route(base_central_system, action):
    """
    Test that a CALLERROR NotImplemented is sent back for an OCPP 2.1 action
    for which no handler is registered.
    """
    base_central_system.route_map = {}

    await base_central_system.route_message(
        Call(unique_id=1, action=action, payload={}).to_json()
    )
    base_central_system._connection.send.assert_called_once_with(
        json.dumps(
            [
                4,
                1,
                "NotImplemented",
                "Request Action is recognized but not supported by the receiver",
                {"cause": f"No handler for {action} registered."},
            ],
            separators=(",", ":"),
        )
    )


@pytest.mark.asyncio
async def test_route_message_not_supported(base_central_system):
    """
    Test that a CALLERROR NotSupported is sent back for an action that isn't
    part of OCPP 2.1.
    """
    await base_central_system.route_message(
        Call(unique_id=1, action="InvalidAction", payload={}).to_json()
    )
    base_central_system._connection.send.assert_called_once_with(
        json.dumps(
            [
                4,
                1,
                "NotSupported",
                "Requested Action is not known by receiver",
                {"cause": "InvalidAction not supported by OCPP2.1."},
            ],
            separators=(",", ":"),
        )
    )
