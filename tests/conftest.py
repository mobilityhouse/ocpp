import pytest
from ocpp.v16 import ChargePoint
from ocpp.v16.enums import Action
from ocpp.messages import Call
from asynctest import CoroutineMock


@pytest.fixture
def heartbeat_call():
    return Call(unique_id=1, action=Action.Heartbeat, payload={}).to_json()


@pytest.fixture
def boot_notification_call():
    return Call(
        unique_id="1",
        action=Action.BootNotification,
        payload={
            'chargePointVendor': 'Alfen BV',
            'chargePointModel': 'ICU Eve Mini',
            'firmwareVersion': "#1:3.4.0-2990#N:217H;1.0-223",
        }).to_json()


@pytest.fixture
def base_central_system(connection):
    cs = ChargePoint(
            id=1234,
            connection=connection
    )

    cs._unique_id_generator = lambda: 1337

    return cs


@pytest.fixture
def connection():
    class Connection:
        pass

    connection = Connection()
    connection.send = CoroutineMock()

    return connection
