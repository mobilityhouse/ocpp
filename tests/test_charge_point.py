import unittest
from ocpp.v20 import ChargePoint as cp

def test_getters_should_not_be_called_during_routemap_setup():
    class ChargePoint(cp):
        @property
        def foo(self):
            raise Exception("this will be raised")

    try:
        ChargePoint("blah", None)
    except Exception as e:
        assert str(e) == "this will be raised"
        assert False, "Getter was called during ChargePoint creation"
    assert True
