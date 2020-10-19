import pytest
from ocpp.messages import Call
from ocpp.v201 import ChargePoint


@pytest.fixture
def heartbeat_call():
    return Call(unique_id=1, action="Heartbeat", payload={}).to_json()


@pytest.fixture
def boot_notification_call():
    return Call(
        unique_id="1",
        action='BootNotification',
        payload={
            'reason': 'PowerUp',
            'chargingStation': {
                'vendorName': 'ICU Eve Mini',
                'firmwareVersion': "#1:3.4.0-2990#N:217H;1.0-223",
                'model': 'ICU Eve Mini',
            },
        }).to_json()


@pytest.fixture
def base_central_system(connection):
    cs = ChargePoint(
        id=1234,
        connection=connection,
    )

    cs._unique_id_generator = lambda: 1337

    return cs
