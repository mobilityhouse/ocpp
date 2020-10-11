class OCPPError(Exception):
    """ Base class for all OCPP errors. It shouldn't be raised, only it
    subclasses.
    """
    default_description = ""

    def __init__(self, description=None, details=None):
        self.description = description
        if description is None:
            self.description = self.default_description

        self.details = details
        if self.details is None:
            self.details = {}

    def __eq__(self, other):
        if other.__class__ is self.__class__:
            return (self.description, self.details) == \
                (other.description, other.details)

        return NotImplemented

    def __repr__(self):
        return f"<{self.__class__.__name__} - description={self.description},"\
               f" details={self.details}>"

    def __str__(self):
        return f"{self.__class__.__name__}: {self.description},"\
               f" {self.details}"


class NotImplementedError(OCPPError):
    code = "NotImplemented"
    default_description = "Request Action is recognized but not supported by \
                          the receiver"


class InternalError(OCPPError):
    code = "InternalError"
    default_description = "An internal error occurred and the receiver was \
                          able to process the requested Action successfully"


class ProtocolError(OCPPError):
    code = "ProtocolError"
    default_description = "Payload for Action is incomplete"


class SecurityError(OCPPError):
    code = "SecurityError"
    default_description = "During the processing of Action a security issue \
                          occurred preventing receiver from completing the \
                          Action successfully"


class FormatViolationError(OCPPError):
    code = "FormatViolation"
    default_description = "Payload for Action is syntactically incorrect or \
                          structure for Action"


class PropertyConstraintViolationError(OCPPError):
    code = "PropertyConstraintViolation"
    default_description = "Payload is syntactically correct but at least \
                          one field contains an invalid value"


class OccurenceConstraintViolationError(OCPPError):
    code = "OccurenceConstraintViolation"
    default_description = "Payload for Action is syntactically correct but \
                          at least one of the fields violates occurence \
                          constraints"


class TypeConstraintViolationError(OCPPError):
    code = "TypeConstraintViolation"
    default_description = "Payload for Action is syntactically correct but at \
                          least one of the fields violates data type \
                          constraints (e.g. “somestring”: 12)"


class GenericError(OCPPError):
    code = "GenericError"
    default_description = "Any other error not all other OCPP defined errors"


class ValidationError(Exception):
    """ ValidationError should be raised if validation a message payload fails.

    Note this isn't an official OCPP error!
    """
    pass


class UnknownCallErrorCodeError(Exception):
    """ Raised when a CALLERROR is received with unknown error code. """
    pass
