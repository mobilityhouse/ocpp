try:
    from unittest.mock import AsyncMock
except ImportError:
    # Python 3.7 and below don't include unittest.mock.AsyncMock. Hence,
    # we need to resolve to a package on pypi.
    from asynctest import CoroutineMock as AsyncMock

import pytest

from ocpp.messages import Call, CallResult
from ocpp.v16 import ChargePoint, call
from ocpp.v16.enums import Action


@pytest.fixture
def heartbeat_call():
    return Call(unique_id=1, action=Action.Heartbeat, payload={}).to_json()


@pytest.fixture
def notsupported_call():
    return Call(unique_id="1", action="InvalidAction", payload={}).to_json()


@pytest.fixture
def boot_notification_call():
    return Call(
        unique_id="1",
        action=Action.BootNotification,
        payload={
            "chargePointVendor": "Alfen BV",
            "chargePointModel": "ICU Eve Mini",
            "firmwareVersion": "#1:3.4.0-2990#N:217H;1.0-223",
        },
    ).to_json()


@pytest.fixture
def base_central_system(connection):
    cs = ChargePoint(
        id=1234,
        connection=connection,
    )

    cs._unique_id_generator = lambda: 1337

    return cs


@pytest.fixture
def mock_boot_request():
    return call.BootNotificationPayload(
        charge_point_vendor="dummy_vendor",
        charge_point_model="dummy_model",
    )


@pytest.fixture
def mock_base_central_system(base_central_system):
    mock_result_call = CallResult(
        unique_id=str(base_central_system._unique_id_generator()),
        action="BootNotification",
        payload={
            "currentTime": "2018-05-29T17:37:05.495259",
            "interval": 350,
            "status": "Accepted",
        },
    )

    base_central_system._send = AsyncMock()

    mock_response = AsyncMock()
    mock_response.return_value = mock_result_call
    base_central_system._get_specific_response = mock_response

    return base_central_system
