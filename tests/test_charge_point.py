import pytest
from ocpp.charge_point import remove_nones

from ocpp.v20 import ChargePoint as cp
from ocpp.routing import on, create_route_map
from ocpp.v16.enums import Action


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
    ('input_data', 'expected_output'),
    [
        ({}, {}),
        ({1: None}, {}),
        ({1: None, 2: 0}, {2: 0}),
        ({2: []}, {2: []}),
        ({2: ['a', None, 0, {2: 'b'}]}, {2: ['a', None, 0, {2: 'b'}]}),
        ({2: ['a', {3: None, 4: 'b'}]}, {2: ['a', {4: 'b'}]}),
        ({2: ({3: None, 4: 'b'})}, {2: ({4: 'b'})}),  # Tuple of dicts
        (
            {
                1: {'a': None, 'b': 1},
                2: [{'c': None, 'd': 2}, {'e': None}, {'f': [{'g': None}]}],
            },
            {
                1: {'b': 1},
                2: [{'d': 2}, {}, {'f': [{}]}]
            }
        )
    ]
)
def test_remove_nones(input_data, expected_output):
    assert remove_nones(input_data) == expected_output
