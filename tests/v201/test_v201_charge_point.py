import json
import pytest

from ocpp.routing import on, after, create_route_map
from ocpp.v201 import call_result


@pytest.mark.asyncio
async def test_route_message_with_existing_route(base_central_system,
                                                 boot_notification_call):
    """ Test if the correct handler is called when routing a message.
    Also test if payload of request is injected correctly in handler.

    """
    @on("BootNotification")
    def on_boot_notification(reason, charging_station, **kwargs):
        assert reason == 'PowerUp'
        assert charging_station == {
            'vendor_name': 'ICU Eve Mini',
            'firmware_version': "#1:3.4.0-2990#N:217H;1.0-223",
            'model': 'ICU Eve Mini',
        }

        return call_result.BootNotificationPayload(
            current_time='2018-05-29T17:37:05.495259',
            interval=350,
            status='Accepted',
        )

    @after("BootNotification")
    def after_boot_notification(reason, charging_station, **kwargs):
        assert reason == 'PowerUp'
        assert charging_station == {
            'vendor_name': 'ICU Eve Mini',
            'firmware_version': "#1:3.4.0-2990#N:217H;1.0-223",
            'model': 'ICU Eve Mini',
        }

    setattr(base_central_system, 'on_boot_notification', on_boot_notification)
    setattr(base_central_system, 'after_boot_notification',
            after_boot_notification)
    base_central_system.route_map = create_route_map(base_central_system)

    await base_central_system.route_message(boot_notification_call)
    base_central_system._connection.send.assert_called_once_with(
        json.dumps([
            3,
            "1",
            {
                'currentTime': '2018-05-29T17:37:05.495259',
                'interval': 350,
                'status': 'Accepted',
            }
        ],
            separators=(',', ':')
        )
    )


@pytest.mark.asyncio
async def test_route_message_with_no_route(base_central_system,
                                           heartbeat_call):
    """
    Test that a CALLERROR is sent back, reporting that no handler is
    registred for it.

    """
    # Empty the route map
    base_central_system.route_map = {}

    await base_central_system.route_message(heartbeat_call)
    base_central_system._connection.send.assert_called_once_with(
        json.dumps([
            4,
            1,
            "NotSupported",
            "Request Action is recognized but not supported by the receiver",
            {"cause": "No handler for Heartbeat registered."}
        ],
            separators=(',', ':')
        )
    )
