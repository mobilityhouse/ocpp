from ocpp.exceptions import ProtocolError


def test_exception_with_error_details():
    exception = ProtocolError("Some error", {'key': 'value'})

    assert exception.description == "Some error"
    assert exception.details == {'key': 'value'}


def test_exception_without_error_details():
    exception = ProtocolError()

    assert exception.description == "Payload for Action is incomplete"
    assert exception.details == {}
