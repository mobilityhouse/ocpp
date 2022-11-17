import pytest

from ocpp.exceptions import ProtocolError, TypeConstraintViolationError, FormatViolationError
from ocpp.messages import validate_payload, Call


def test_exception_with_error_details():
    exception = ProtocolError("Some error", {"key": "value"})

    assert exception.description == "Some error"
    assert exception.details == {"key": "value"}


def test_exception_without_error_details():
    exception = ProtocolError()

    assert exception.description == "Payload for Action is incomplete"
    assert exception.details == {}


def test_exception_show_triggered_message_type_constraint():
    # chargePointVendor should be a string, not an integer, so this should raise a TypeConstraintViolationError
    call = Call(unique_id=123456,
                action="BootNotification",
                payload={"chargePointVendor": 1, "chargePointModel": "SingleSocketCharger"})

    regex_pattern = r"'ocpp_message': <Call - unique_id=123456, action=BootNotification, payload={" \
                    r"'chargePointVendor': 1, 'chargePointModel': 'SingleSocketCharger'}"

    with pytest.raises(TypeConstraintViolationError, match=regex_pattern):
        validate_payload(call, "1.6")


def test_exception_show_triggered_message_format():
    # The payload is syntactically incorrect, which should trigger a FormatViolationError
    call = Call(unique_id=123457,
                action="BootNotification",
                payload={"syntactically": "incorrect"})

    regex_pattern = r"'ocpp_message': <Call - unique_id=123457, action=BootNotification, payload={" \
                    r"'syntactically': 'incorrect'}"

    with pytest.raises(FormatViolationError, match=regex_pattern):
        validate_payload(call, "1.6")
