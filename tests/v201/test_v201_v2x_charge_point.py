import json

import pytest

from ocpp.charge_point import ChargePoint
from ocpp.messages import CallResult
from ocpp.routing import create_route_map, on
from ocpp.v201.v2x import call, call_result


@pytest.mark.asyncio
async def test_route_message_with_v2x_extension_route(
    base_central_system: ChargePoint,
    notify_priority_charging_call: call.NotifyPriorityChargingPayload,
) -> None:
    """Test if the correct handler is called when routing a V2X message.
    Also test if payload of request is injected correctly in handler.

    """

    @on("NotifyPriorityCharging", extension="v2x")
    def on_notify_priority_charging(transaction_id, activated):
        assert transaction_id == "1337"
        assert activated is True

        return call_result.NotifyPriorityChargingPayload()

    setattr(
        base_central_system, "on_notify_priority_charging", on_notify_priority_charging
    )
    base_central_system.route_map = create_route_map(base_central_system)

    await base_central_system.route_message(notify_priority_charging_call)
    base_central_system._connection.send.assert_called_once_with(
        json.dumps(
            [
                3,
                "1",
                {},
            ],
            separators=(",", ":"),
        )
    )


@pytest.mark.asyncio
async def test_call_with_v2x_extension(base_central_system: ChargePoint) -> None:
    """Test if the correct handler is called when routing a V2X message.
    Also test if payload of request is injected correctly in handler.

    """
    payload = call.NotifyPriorityChargingPayload(transaction_id="1337", activated=True)

    response_payload = CallResult(
        unique_id="1337",
        payload={},
        action="NotifyPriorityCharging",
    )

    base_central_system._response_queue.put_nowait(response_payload)

    response = await base_central_system.call(
        payload, extension="v2x", extension_call_result=call_result
    )

    assert isinstance(response, call_result.NotifyPriorityChargingPayload)
