import asyncio
import json
from unittest import mock

import pytest

from ocpp.exceptions import FormatViolationError, GenericError
from ocpp.messages import CallError
from ocpp.routing import after, create_route_map, on
from ocpp.v16 import ChargePoint, call, call_result
from ocpp.v16.enums import Action


@pytest.mark.asyncio
async def test_route_message_with_existing_route(
    base_central_system, boot_notification_call
):
    """Test if the correct handler is called when routing a message.
    Also test if payload of request is injected correctly in handler.

    """

    @on(Action.boot_notification)
    def on_boot_notification(charge_point_model, charge_point_vendor, **kwargs):  # noqa
        assert charge_point_vendor == "Alfen BV"
        assert charge_point_model == "ICU Eve Mini"
        assert kwargs["firmware_version"] == "#1:3.4.0-2990#N:217H;1.0-223"

        return call_result.BootNotification(
            current_time="2018-05-29T17:37:05.495259",
            interval=350,
            status="Accepted",
        )

    @after(Action.boot_notification)
    async def after_boot_notification(
        charge_point_model, charge_point_vendor, **kwargs
    ):  # noqa
        assert charge_point_vendor == "Alfen BV"
        assert charge_point_model == "ICU Eve Mini"

    setattr(base_central_system, "on_boot_notification", on_boot_notification)
    setattr(base_central_system, "after_boot_notification", after_boot_notification)
    base_central_system.route_map = create_route_map(base_central_system)

    await base_central_system.route_message(boot_notification_call)
    base_central_system._connection.send.assert_called_once_with(
        json.dumps(
            [
                3,
                "1",
                {
                    "currentTime": "2018-05-29T17:37:05.495259",
                    "interval": 350,
                    "status": "Accepted",
                },
            ],
            separators=(",", ":"),
        )
    )


@pytest.mark.asyncio
async def test_route_message_without_validation(base_central_system):
    @on(Action.boot_notification, skip_schema_validation=True)
    def on_boot_notification(**kwargs):  # noqa
        assert kwargs["firmware_version"] == "#1:3.4.0-2990#N:217H;1.0-223"

        return call_result.BootNotification(
            current_time="2018-05-29T17:37:05.495259",
            interval=350,
            # 'Yolo' is not a valid value for for field status.
            status="Yolo",
        )

    setattr(base_central_system, "on_boot_notification", on_boot_notification)
    base_central_system.route_map = create_route_map(base_central_system)

    await base_central_system.route_message(
        json.dumps(
            [
                2,
                1,
                "BootNotification",
                {
                    # The payload is missing the required fields 'chargepointVendor'
                    # and 'chargePointModel'.
                    "firmwareVersion": "#1:3.4.0-2990#N:217H;1.0-223"
                },
            ],
            separators=(",", ":"),
        )
    )

    base_central_system._connection.send.call_args == mock.call(
        json.dumps(
            [
                3,
                "1",
                {
                    "currentTime": "2018-05-29T17:37:05.495259",
                    "interval": 350,
                    "status": "Yolo",
                },
            ],
            separators=(",", ":"),
        )
    )


@pytest.mark.asyncio
async def test_route_message_not_supported(base_central_system, not_supported_call):
    """
    Test that a CALLERROR is sent back, reporting that it is
    not supported by OCPP version.

    """

    @on(Action.boot_notification)
    def on_boot_notification(**kwargs):  # noqa
        assert kwargs["firmware_version"] == "#1:3.4.0-2990#N:217H;1.0-223"

        return call_result.BootNotification(
            current_time="2018-05-29T17:37:05.495259",
            interval=350,
            # 'Yolo' is not a valid value for for field status.
            status="Yolo",
        )

    setattr(base_central_system, "on_boot_notification", on_boot_notification)
    base_central_system.route_map = create_route_map(base_central_system)

    await base_central_system.route_message(not_supported_call)
    base_central_system._connection.send.assert_called_once_with(
        json.dumps(
            [
                4,
                1,
                "NotSupported",
                "Requested Action is not known by receiver",
                {"cause": "InvalidAction not supported by OCPP1.6."},
            ],
            separators=(",", ":"),
        )
    )


@pytest.mark.asyncio
async def test_route_message_with_no_route(base_central_system, heartbeat_call):
    """
    Test that a CALLERROR is sent back, reporting that no handler is
    registred for it.

    """
    # Empty the route map
    base_central_system.route_map = {}

    await base_central_system.route_message(heartbeat_call)
    base_central_system._connection.send.assert_called_once_with(
        json.dumps(
            [
                4,
                1,
                "NotImplemented",
                "Request Action is recognized but not supported by the receiver",
                {"cause": "No handler for Heartbeat registered."},
            ],
            separators=(",", ":"),
        )
    )


@pytest.mark.asyncio
async def test_send_call_with_timeout(connection):
    cs = ChargePoint(id=1234, connection=connection, response_timeout=0.1)

    payload = call.Reset(type="Hard")

    with pytest.raises(asyncio.TimeoutError):
        await cs.call(payload)

    # Verify that lock is released if call() crahses. Not releasing the lock
    # in case of an exception could lead to a deadlock. See
    # https://github.com/mobilityhouse/ocpp/issues/46
    assert cs._call_lock.locked() is False


@pytest.mark.asyncio
async def test_send_invalid_call(base_central_system):
    payload = call.Reset(type="Medium")

    with pytest.raises(FormatViolationError):
        await base_central_system.call(payload)


@pytest.mark.asyncio
async def test_raise_call_error(base_central_system):
    """
    Test that getting a CallError will raise an Exception
    if suppress argument is not True.

    """
    call_error = CallError(
        unique_id="1337",
        error_code="GenericError",
        error_description="test_raise_call_error",
    )
    await base_central_system.route_message(call_error.to_json())

    payload = call.ClearCache()
    with pytest.raises(GenericError):
        await base_central_system.call(payload, suppress=False)


@pytest.mark.asyncio
async def test_suppress_call_error(base_central_system):
    """
    Test that getting a CallError will suppress Exception
    by default

    """
    call_error = CallError(
        unique_id="1337",
        error_code="GenericError",
        error_description="test_raise_call_error",
    )
    await base_central_system.route_message(call_error.to_json())

    payload = call.ClearCache()
    await base_central_system.call(payload)


@pytest.mark.asyncio
async def test_call_with_unique_id_should_return_same_id(
    mock_boot_request, mock_base_central_system
):

    expected_unique_id = "12345"
    # Call the method being tested with a unique_id as a parameter
    await mock_base_central_system.call(mock_boot_request, unique_id=expected_unique_id)
    (
        actual_unique_id,
        _,
    ) = mock_base_central_system._get_specific_response.call_args_list[0][0]

    # Check the actual unique id is equals to the one passed to the call method
    assert actual_unique_id == expected_unique_id


@pytest.mark.asyncio
async def test_call_without_unique_id_should_return_a_random_value(
    mock_boot_request, mock_base_central_system
):

    expected_unique_id = str(mock_base_central_system._unique_id_generator())

    # Call the method being tested without passing a unique_id as a parameter
    await mock_base_central_system.call(mock_boot_request)

    (
        actual_unique_id,
        _,
    ) = mock_base_central_system._get_specific_response.call_args_list[0][0]
    # Check the actual unique id is equals to the one internally generated
    assert actual_unique_id == expected_unique_id


@pytest.mark.asyncio
async def test_call_skip_schema_validation(
    mock_invalid_boot_request, mock_base_central_system
):
    """
    Test that schema validation is skipped for an invalid boot notification request.

    """

    expected_unique_id = "12345"
    # Call the method being tested with an invalid boot notification request
    # and a unique_id as a parameter
    await mock_base_central_system.call(
        mock_invalid_boot_request,
        unique_id=expected_unique_id,
        skip_schema_validation=True,
    )
    (
        actual_unique_id,
        _,
    ) = mock_base_central_system._get_specific_response.call_args_list[0][0]

    # Check the actual unique id is equals to the one passed to the call method
    assert actual_unique_id == expected_unique_id
