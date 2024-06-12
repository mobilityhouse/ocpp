from unittest.mock import AsyncMock

import pytest

from ocpp.messages import Call, CallResult
from ocpp.v201 import ChargePoint, call

chargingStation = {
    "vendorName": "ICU Eve Mini",
    "firmwareVersion": "#1:3.4.0-2990#N:217H;1.0-223",
    "model": "ICU Eve Mini",
}


@pytest.fixture
def heartbeat_call():
    return Call(unique_id=1, action="Heartbeat", payload={}).to_json()


@pytest.fixture
def boot_notification_call():
    return Call(
        unique_id="1",
        action="BootNotification",
        payload={
            "reason": "PowerUp",
            "chargingStation": chargingStation,
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
    return call.BootNotification(
        reason="PowerUp",
        charging_station=chargingStation,
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
