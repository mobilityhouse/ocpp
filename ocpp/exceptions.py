class OCPPError(Exception):
    """Base class for all OCPP errors. It shouldn't be raised, only it
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
            return (self.description, self.details) == (
                other.description,
                other.details,
            )

        return NotImplemented

    def __repr__(self):
        return (
            f"<{self.__class__.__name__} - description={self.description}, "
            f" details={self.details}>"
        )

    def __str__(self):
        return f"{self.__class__.__name__}: {self.description}, " f" {self.details}"


class NotImplementedError(OCPPError):
    code = "NotImplemented"
    default_description = (
        "Request Action is recognized but not supported by the receiver"
    )


class NotSupportedError(OCPPError):
    code = "NotSupported"
    default_description = "Requested Action is not known by receiver"


class InternalError(OCPPError):
    code = "InternalError"
    default_description = (
        "An internal error occurred and the receiver was "
        "not able to process the requested Action successfully"
    )


class ProtocolError(OCPPError):
    code = "ProtocolError"
    default_description = "Payload for Action is incomplete"


class SecurityError(OCPPError):
    code = "SecurityError"
    default_description = (
        "During the processing of Action a security issue "
        "occurred preventing receiver from completing the "
        "Action successfully"
    )


class FormatViolationError(OCPPError):
    """
    Not strict OCPP 1.6 - see FormationViolationError
    Valid OCPP 2.0.1
    """

    code = "FormatViolation"
    default_description = (
        "Payload for Action is syntactically incorrect or " "structure for Action"
    )


class FormationViolationError(OCPPError):
    """
    To allow for strict OCPP 1.6 compliance
        5. Known issues that will not be fixed
        5.2. Page 14, par 4.2.3. CallError: incorrect name in enum: FormationViolation
        Incorrect name in enum: FormationViolation
    """

    code = "FormationViolation"
    default_description = (
        "Payload for Action is syntactically incorrect or structure for Action"
    )


class PropertyConstraintViolationError(OCPPError):
    code = "PropertyConstraintViolation"
    default_description = (
        "Payload is syntactically correct but at least "
        "one field contains an invalid value"
    )


class OccurenceConstraintViolationError(OCPPError):
    """
    To allow for strict OCPP 1.6 compliance
    ocpp-j-1.6-errata-sheet.pdf
        5. Known issues that will not be fixed
        5.1. Page 14, par 4.2.3: CallError: Typo in enum
        Typo in enum: OccurenceConstraintViolation
    Valid in 2.0.1
    """

    code = "OccurenceConstraintViolation"
    default_description = (
        "Payload for Action is syntactically correct but "
        "at least one of the fields violates occurence "
        "constraints"
    )


class OccurrenceConstraintViolationError(OCPPError):
    """
    Not strict OCPP 1.6 - see OccurenceConstraintViolationError
    Not valid OCPP 2.0.1
    Valid in OCPP 2.1
    """

    code = "OccurrenceConstraintViolation"
    default_description = (
        "Payload for Action is syntactically correct but "
        "at least one of the fields violates occurence "
        "constraints"
    )


class TypeConstraintViolationError(OCPPError):
    code = "TypeConstraintViolation"
    default_description = (
        "Payload for Action is syntactically correct but "
        "at least one of the fields violates data type "
        "constraints (e.g. “somestring”: 12)"
    )


class GenericError(OCPPError):
    code = "GenericError"
    default_description = "Any other error not all other OCPP defined errors"


class ValidationError(Exception):
    """ValidationError should be raised if validation a message payload fails.

    Note this isn't an official OCPP error!
    """

    pass


class UnknownCallErrorCodeError(Exception):
    """Raised when a CALLERROR is received with unknown error code."""

    pass
