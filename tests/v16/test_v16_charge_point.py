import json
import pytest
import asyncio
from unittest import mock

from ocpp.exceptions import NotImplementedError, ValidationError, GenericError
from ocpp.messages import CallError
from ocpp.routing import on, after, create_route_map
from ocpp.v16.enums import Action
from ocpp.v16 import call_result, call, ChargePoint


@pytest.mark.asyncio
async def test_route_message_with_existing_route(base_central_system,
                                                 boot_notification_call):
    """ Test if the correct handler is called when routing a message.
    Also test if payload of request is injected correctly in handler.

    """
    @on(Action.BootNotification)
    def on_boot_notification(charge_point_model, charge_point_vendor, **kwargs):  # noqa
        assert charge_point_vendor == "Alfen BV"
        assert charge_point_model == "ICU Eve Mini"
        assert kwargs['firmware_version'] == "#1:3.4.0-2990#N:217H;1.0-223"

        return call_result.BootNotificationPayload(
            current_time='2018-05-29T17:37:05.495259Z',
            interval=350,
            status='Accepted',
        )

    @after(Action.BootNotification)
    async def after_boot_notification(charge_point_model, charge_point_vendor,
                                **kwargs):  # noqa
        assert charge_point_vendor == "Alfen BV"
        assert charge_point_model == "ICU Eve Mini"

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
                'currentTime': '2018-05-29T17:37:05.495259Z',
                'interval': 350,
                'status': 'Accepted',
            }
        ],
            separators=(',', ':')
        )
    )


@pytest.mark.asyncio
async def test_route_message_without_validation(base_central_system):
    @on(Action.BootNotification, skip_schema_validation=True)
    def on_boot_notification(**kwargs):  # noqa
        assert kwargs['firmware_version'] == "#1:3.4.0-2990#N:217H;1.0-223"

        return call_result.BootNotificationPayload(
            current_time='2018-05-29T17:37:05.495259Z',
            interval=350,
            # 'Yolo' is not a valid value for for field status.
            status='Yolo',
        )

    setattr(base_central_system, 'on_boot_notification', on_boot_notification)
    base_central_system.route_map = create_route_map(base_central_system)

    await base_central_system.route_message(json.dumps([
        2,
        1,
        "BootNotification",
        {
            # The payload is missing the required fields 'chargepointVendor'
            # and 'chargePointModel'.
            "firmwareVersion": "#1:3.4.0-2990#N:217H;1.0-223"
        }
    ],
        separators=(',', ':')
    ))

    base_central_system._connection.send.call_args == \
        mock.call(json.dumps([
            3,
            "1",
            {
                'currentTime': '2018-05-29T17:37:05.495259Z',
                'interval': 350,
                'status': 'Yolo',
            }
        ],
            separators=(',', ':')
        ))


@pytest.mark.asyncio
async def test_route_message_with_no_route(base_central_system,
                                           heartbeat_call):
    """
    Test that NotImplementedError is raised when message received without a
    handler registred for it.

    """
    # Empty the route map
    base_central_system.route_map = {}

    with pytest.raises(NotImplementedError):
        await base_central_system.route_message(heartbeat_call)


@pytest.mark.asyncio
async def test_send_call_with_timeout(connection):
    cs = ChargePoint(
        id=1234,
        connection=connection,
        response_timeout=0.1
    )

    payload = call.ResetPayload(type="Hard")

    with pytest.raises(asyncio.TimeoutError):
        await cs.call(payload)

    # Verify that lock is released if call() crahses. Not releasing the lock
    # in case of an exception could lead to a deadlock. See
    # https://github.com/mobilityhouse/ocpp/issues/46
    assert cs._call_lock.locked() is False


@pytest.mark.asyncio
async def test_send_invalid_call(base_central_system):
    payload = call.ResetPayload(type="Medium")

    with pytest.raises(ValidationError):
        await base_central_system.call(payload)


@pytest.mark.asyncio
async def test_raise_call_error(base_central_system):
    """
    Test that getting a CallError will raise an Exception
    if suppress argument is not True.

    """
    call_error = CallError(
            unique_id='1337',
            error_code="GenericError",
            error_description='test_raise_call_error',
    )
    await base_central_system.route_message(call_error.to_json())

    payload = call.ClearCachePayload()
    with pytest.raises(GenericError):
        await base_central_system.call(payload, suppress=False)


@pytest.mark.asyncio
async def test_suppress_call_error(base_central_system):
    """
    Test that getting a CallError will suppress Exception
    by default

    """
    call_error = CallError(
            unique_id='1337',
            error_code="GenericError",
            error_description='test_raise_call_error',
    )
    await base_central_system.route_message(call_error.to_json())

    payload = call.ClearCachePayload()
    await base_central_system.call(payload)
