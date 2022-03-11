from dataclasses import asdict

import pytest
from ocpp.v20 import ChargePoint as cp
from ocpp.routing import on, create_route_map
from ocpp.v16.call import (BootNotificationPayload, MeterValuesPayload,
                           GetConfigurationPayload)
from ocpp.v16.enums import Action
from ocpp.v16.datatypes import MeterValue, SampledValue
from ocpp.v201.call import SetNetworkProfilePayload
from ocpp.v201.enums import (OCPPVersionType, OCPPTransportType,
                             OCPPInterfaceType)
from ocpp.v201.datatypes import NetworkConnectionProfileType
from ocpp.charge_point import (
    camel_to_snake_case, snake_to_camel_case, remove_nones)


def test_getters_should_not_be_called_during_routemap_setup():
    class ChargePoint(cp):
        @property
        def foo(self):
            raise RuntimeError("this will be raised")

    try:
        ChargePoint("blah", None)
    except RuntimeError as e:
        assert str(e) == "this will be raised"
        pytest.fail("Getter was called during ChargePoint creation")


def test_multiple_classes_with_same_name_for_handler():
    class ChargerA(cp):
        @on(Action.Heartbeat)
        def heartbeat(self, **kwargs):
            pass

    class ChargerB(cp):
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
    ],
)
def test_snake_to_camel_case(test_input, expected):
    result = snake_to_camel_case(test_input)
    assert result == expected


def test_remove_nones():
    expected_payload = {'charge_point_model': 'foo',
                        'charge_point_vendor': 'bar'}

    payload = BootNotificationPayload(
        charge_point_model='foo', charge_point_vendor='bar',
        charge_box_serial_number=None)
    payload = asdict(payload)

    assert expected_payload == remove_nones(payload)


def test_nested_remove_nones():
    expected_payload = {'configuration_slot': 1,
                        'connection_data': {
                            'ocpp_version': 'OCPP20', 'ocpp_transport': 'JSON',
                            'ocpp_csms_url': 'wss://localhost:9000',
                            'message_timeout': 60, 'security_profile': 1,
                            'ocpp_interface': 'Wired0'}}

    connection_data = NetworkConnectionProfileType(
        ocpp_version=OCPPVersionType.ocpp20,
        ocpp_transport=OCPPTransportType.json,
        ocpp_csms_url='wss://localhost:9000', message_timeout=60,
        security_profile=1, ocpp_interface=OCPPInterfaceType.wired0,
        vpn=None, apn=None)

    payload = SetNetworkProfilePayload(configuration_slot=1,
                                       connection_data=connection_data)
    payload = asdict(payload)

    assert expected_payload == remove_nones(payload)


def test_nested_list_remove_nones():
    expected_payload = {
        'connector_id': 3,
        'meter_value': [{
            'timestamp': '2017-08-17T07:08:06.186748+00:00',
            'sampled_value': [
                {'value': '10', 'context': 'Sample.Periodic',
                 'measurand': 'Power.Active.Import', 'unit': 'W'},
                {'value': '50000', 'context': 'Sample.Periodic',
                 'measurand': 'Power.Active.Import', 'phase': 'L1',
                 'unit': 'W'}]},
            {'timestamp': '2017-08-17T07:07:07.186748+00:00',
             'sampled_value': [
                 {'value': '10', 'context': 'Sample.Periodic',
                  'measurand': 'Power.Active.Import', 'unit': 'W'},
                 {'value': '50000', 'context': 'Sample.Periodic',
                  'measurand': 'Power.Active.Import', 'phase': 'L1',
                  'unit': 'W'}]}],
        'transaction_id': 5}

    payload = MeterValuesPayload(connector_id=3, meter_value=[
        MeterValue(timestamp='2017-08-17T07:08:06.186748+00:00',
                   sampled_value=[
                        SampledValue(value='10', context='Sample.Periodic',
                                     format=None,
                                     measurand='Power.Active.Import',
                                     phase=None, location=None, unit='W'),
                        SampledValue(value='50000', context='Sample.Periodic',
                                     format=None,
                                     measurand='Power.Active.Import',
                                     phase='L1', location=None, unit='W')]),
        MeterValue(timestamp='2017-08-17T07:07:07.186748+00:00',
                   sampled_value=[
                       SampledValue(value='10', context='Sample.Periodic',
                                    format=None,
                                    measurand='Power.Active.Import',
                                    phase=None, location=None, unit='W'),
                       SampledValue(value='50000', context='Sample.Periodic',
                                    format=None,
                                    measurand='Power.Active.Import',
                                    phase='L1', location=None, unit='W')])],
        transaction_id=5)

    payload = asdict(payload)
    assert expected_payload == remove_nones(payload)


def test_remove_nones_with_list_of_strings():
    """ Make sure that `remove_nones()` doesn't crash when it encounters an
    iterable other than a list or dict. See
    https://github.com/mobilityhouse/ocpp/issues/289.
    """
    payload = asdict(
        GetConfigurationPayload(
            key=["ClockAlignedDataInterval", "ConnectionTimeOut"]
        )
    )

    assert remove_nones(payload) == {
        'key': ['ClockAlignedDataInterval', 'ConnectionTimeOut']
    }
