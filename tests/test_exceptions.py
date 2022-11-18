import pytest

from ocpp.exceptions import (
    FormatViolationError,
    ProtocolError,
    TypeConstraintViolationError,
)
from ocpp.messages import Call, OCPPVersion, SchemaValidator, validate_payload

v16_validator = SchemaValidator(ocpp_version=OCPPVersion.v16)


def test_exception_with_error_details():
    exception = ProtocolError("Some error", {"key": "value"})

    assert exception.description == "Some error"
    assert exception.details == {"key": "value"}


def test_exception_without_error_details():
    exception = ProtocolError()

    assert exception.description == "Payload for Action is incomplete"
    assert exception.details == {}


def test_exception_show_triggered_message_type_constraint():
    # chargePointVendor should be a string, not an integer,
    # so this should raise a TypeConstraintViolationError
    call = Call(
        unique_id=123456,
        action="BootNotification",
        payload={"chargePointVendor": 1, "chargePointModel": "SingleSocketCharger"},
    )
    ocpp_message = (
        "'ocpp_message': <Call - unique_id=123456, action=BootNotification, "
        "payload={'chargePointVendor': 1, 'chargePointModel': 'SingleSocketCharger'}"
    )

    with pytest.raises(TypeConstraintViolationError) as exception_info:
        validate_payload(call, v16_validator)
    assert ocpp_message in str(exception_info.value)


def test_exception_show_triggered_message_format():
    # The payload is syntactically incorrect, should trigger a FormatViolationError
    call = Call(
        unique_id=123457,
        action="BootNotification",
        payload={"syntactically": "incorrect"},
    )

    ocpp_message = (
        "'ocpp_message': <Call - unique_id=123457, action=BootNotification, "
        "payload={'syntactically': 'incorrect'}"
    )

    with pytest.raises(FormatViolationError) as exception_info:
        validate_payload(call, v16_validator)
    assert ocpp_message in str(exception_info.value)
