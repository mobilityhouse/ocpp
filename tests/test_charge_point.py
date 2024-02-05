from dataclasses import asdict

import pytest

from ocpp.charge_point import camel_to_snake_case, remove_nones, snake_to_camel_case
from ocpp.messages import Call
from ocpp.routing import after, create_route_map, on
from ocpp.v16 import ChargePoint as cp_16
from ocpp.v16.call import (
    BootNotificationPayload,
    GetConfigurationPayload,
    MeterValuesPayload,
)
from ocpp.v16.call_result import (
    BootNotificationPayload as BootNotificationResultPayload,
)
from ocpp.v16.datatypes import MeterValue, SampledValue
from ocpp.v16.enums import Action, RegistrationStatus
from ocpp.v20 import ChargePoint as cp_20
from ocpp.v201.call import SetNetworkProfilePayload
from ocpp.v201.datatypes import NetworkConnectionProfileType
from ocpp.v201.enums import OCPPInterfaceType, OCPPTransportType, OCPPVersionType


def test_getters_should_not_be_called_during_routemap_setup():
    class ChargePoint(cp_20):
        @property
        def foo(self):
            raise RuntimeError("this will be raised")

    try:
        ChargePoint("blah", None)
    except RuntimeError as e:
        assert str(e) == "this will be raised"
        pytest.fail("Getter was called during ChargePoint creation")


def test_multiple_classes_with_same_name_for_handler():
    class ChargerA(cp_20):
        @on(Action.Heartbeat)
        def heartbeat(self, **kwargs):
            pass

    class ChargerB(cp_20):
        @on(Action.Heartbeat)
        def heartbeat(self, **kwargs):
            pass

    A = ChargerA("A", None)
    B = ChargerB("B", None)
    route_mapA = create_route_map(A)
    route_mapB = create_route_map(B)
    assert route_mapA["Heartbeat"] != route_mapB["Heartbeat"]


@pytest.mark.parametrize(
    "test_input,expected",
    [
        ({"transactionId": "74563478"}, {"transaction_id": "74563478"}),
        ({"fullSoC": 100}, {"full_soc": 100}),
        ({"responderURL": "foo.com"}, {"responder_url": "foo.com"}),
    ],
)
def test_camel_to_snake_case(test_input, expected):
    result = camel_to_snake_case(test_input)
    assert result == expected


@pytest.mark.parametrize(
    "test_input,expected",
    [
        ({"transaction_id": "74563478"}, {"transactionId": "74563478"}),
        ({"full_soc": 100}, {"fullSoC": 100}),
        ({"ev_min_v2x_energy_request": 200}, {"evMinV2XEnergyRequest": 200}),
        ({"v2x_charging_ctrlr": 200}, {"v2xChargingCtrlr": 200}),
        ({"responder_url": "foo.com"}, {"responderURL": "foo.com"}),
        ({"url": "foo.com"}, {"url": "foo.com"}),
    ],
)
def test_snake_to_camel_case(test_input, expected):
    result = snake_to_camel_case(test_input)
    assert result == expected


def test_remove_nones():
    expected_payload = {"charge_point_model": "foo", "charge_point_vendor": "bar"}

    payload = BootNotificationPayload(
        charge_point_model="foo",
        charge_point_vendor="bar",
        charge_box_serial_number=None,
    )
    payload = asdict(payload)

    assert expected_payload == remove_nones(payload)


def test_nested_remove_nones():
    expected_payload = {
        "configuration_slot": 1,
        "connection_data": {
            "ocpp_version": "OCPP20",
            "ocpp_transport": "JSON",
            "ocpp_csms_url": "wss://localhost:9000",
            "message_timeout": 60,
            "security_profile": 1,
            "ocpp_interface": "Wired0",
        },
    }

    connection_data = NetworkConnectionProfileType(
        ocpp_version=OCPPVersionType.ocpp20,
        ocpp_transport=OCPPTransportType.json,
        ocpp_csms_url="wss://localhost:9000",
        message_timeout=60,
        security_profile=1,
        ocpp_interface=OCPPInterfaceType.wired0,
        vpn=None,
        apn=None,
    )

    payload = SetNetworkProfilePayload(
        configuration_slot=1, connection_data=connection_data
    )
    payload = asdict(payload)

    assert expected_payload == remove_nones(payload)


def test_nested_list_remove_nones():
    expected_payload = {
        "connector_id": 3,
        "meter_value": [
            {
                "timestamp": "2017-08-17T07:08:06.186748+00:00",
                "sampled_value": [
                    {
                        "value": "10",
                        "context": "Sample.Periodic",
                        "measurand": "Power.Active.Import",
                        "unit": "W",
                    },
                    {
                        "value": "50000",
                        "context": "Sample.Periodic",
                        "measurand": "Power.Active.Import",
                        "phase": "L1",
                        "unit": "W",
                    },
                ],
            },
            {
                "timestamp": "2017-08-17T07:07:07.186748+00:00",
                "sampled_value": [
                    {
                        "value": "10",
                        "context": "Sample.Periodic",
                        "measurand": "Power.Active.Import",
                        "unit": "W",
                    },
                    {
                        "value": "50000",
                        "context": "Sample.Periodic",
                        "measurand": "Power.Active.Import",
                        "phase": "L1",
                        "unit": "W",
                    },
                ],
            },
        ],
        "transaction_id": 5,
    }

    payload = MeterValuesPayload(
        connector_id=3,
        meter_value=[
            MeterValue(
                timestamp="2017-08-17T07:08:06.186748+00:00",
                sampled_value=[
                    SampledValue(
                        value="10",
                        context="Sample.Periodic",
                        format=None,
                        measurand="Power.Active.Import",
                        phase=None,
                        location=None,
                        unit="W",
                    ),
                    SampledValue(
                        value="50000",
                        context="Sample.Periodic",
                        format=None,
                        measurand="Power.Active.Import",
                        phase="L1",
                        location=None,
                        unit="W",
                    ),
                ],
            ),
            MeterValue(
                timestamp="2017-08-17T07:07:07.186748+00:00",
                sampled_value=[
                    SampledValue(
                        value="10",
                        context="Sample.Periodic",
                        format=None,
                        measurand="Power.Active.Import",
                        phase=None,
                        location=None,
                        unit="W",
                    ),
                    SampledValue(
                        value="50000",
                        context="Sample.Periodic",
                        format=None,
                        measurand="Power.Active.Import",
                        phase="L1",
                        location=None,
                        unit="W",
                    ),
                ],
            ),
        ],
        transaction_id=5,
    )

    payload = asdict(payload)
    assert expected_payload == remove_nones(payload)


def test_remove_nones_with_list_of_strings():
    """Make sure that `remove_nones()` doesn't crash when it encounters an
    iterable other than a list or dict. See
    https://github.com/mobilityhouse/ocpp/issues/289.
    """
    payload = asdict(
        GetConfigurationPayload(key=["ClockAlignedDataInterval", "ConnectionTimeOut"])
    )

    assert remove_nones(payload) == {
        "key": ["ClockAlignedDataInterval", "ConnectionTimeOut"]
    }


@pytest.mark.asyncio
async def test_call_unique_id_added_to_handler_args_correctly(connection):
    """
    This test ensures that the `call_unique_id` is getting passed to the
    `on` and `after` handlers only if it is explicitly set in the handler signature.

    To cover all possible cases, we define two chargers:

    ChargerA:
    `call_unique_id` not required on `on` handler but required on `after` handler.

    ChargerB:
    `call_unique_id` required on `on` handler but not required on `after` handler.

    Each handler verifies a set of asserts to verify that the `call_unique_id`
    is passed correctly.
    To confirm that the handlers are actually being called and hence the asserts
    are being ran, we introduce a set of counters that increase each time a specific
    handler runs.
    """
    charger_a_test_call_unique_id = "charger_a_1234"
    charger_b_test_call_unique_id = "charger_b_5678"
    payload_a = {"chargePointVendor": "foo_a", "chargePointModel": "bar_a"}
    payload_b = {"chargePointVendor": "foo_b", "chargePointModel": "bar_b"}

    class ChargerA(cp_16):
        on_boot_notification_call_count = 0
        after_boot_notification_call_count = 0

        @on(Action.BootNotification)
        def on_boot_notification(self, *args, **kwargs):
            # call_unique_id should not be passed as arg nor kwarg
            assert kwargs == camel_to_snake_case(payload_a)
            assert args == ()
            ChargerA.on_boot_notification_call_count += 1
            return BootNotificationResultPayload(
                current_time="foo", interval=1, status=RegistrationStatus.accepted
            )

        @after(Action.BootNotification)
        def after_boot_notification(self, call_unique_id, *args, **kwargs):
            assert call_unique_id == charger_a_test_call_unique_id
            assert kwargs == camel_to_snake_case(payload_a)
            # call_unique_id should not be passed as arg
            assert args == ()
            ChargerA.after_boot_notification_call_count += 1
            return BootNotificationResultPayload(
                current_time="foo", interval=1, status=RegistrationStatus.accepted
            )

    class ChargerB(cp_16):
        on_boot_notification_call_count = 0
        after_boot_notification_call_count = 0

        @on(Action.BootNotification)
        def on_boot_notification(self, call_unique_id, *args, **kwargs):
            assert call_unique_id == charger_b_test_call_unique_id
            assert kwargs == camel_to_snake_case(payload_b)
            # call_unique_id should not be passed as arg
            assert args == ()
            ChargerB.on_boot_notification_call_count += 1
            return BootNotificationResultPayload(
                current_time="foo", interval=1, status=RegistrationStatus.accepted
            )

        @after(Action.BootNotification)
        def after_boot_notification(self, *args, **kwargs):
            # call_unique_id should not be passed as arg nor kwarg
            assert kwargs == camel_to_snake_case(payload_b)
            assert args == ()
            ChargerB.after_boot_notification_call_count += 1
            return BootNotificationResultPayload(
                current_time="foo", interval=1, status=RegistrationStatus.accepted
            )

    charger_a = ChargerA("charger_a_id", connection)
    charger_b = ChargerB("charger_b_id", connection)

    msg_a = Call(
        unique_id=charger_a_test_call_unique_id,
        action=Action.BootNotification.value,
        payload=payload_a,
    )
    await charger_a._handle_call(msg_a)

    msg_b = Call(
        unique_id=charger_b_test_call_unique_id,
        action=Action.BootNotification.value,
        payload=payload_b,
    )
    await charger_b._handle_call(msg_b)

    assert ChargerA.on_boot_notification_call_count == 1
    assert ChargerA.after_boot_notification_call_count == 1
    assert ChargerB.on_boot_notification_call_count == 1
    assert ChargerB.after_boot_notification_call_count == 1
