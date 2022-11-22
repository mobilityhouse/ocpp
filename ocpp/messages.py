""" Module containing classes that model the several OCPP messages types. It
also contain some helper functions for packing and unpacking messages.  """
from __future__ import annotations

import decimal
import json
from dataclasses import asdict, is_dataclass
from typing import Dict, Union

from jsonschema import Draft4Validator
from jsonschema import _validators as SchemaValidators
from jsonschema.exceptions import ValidationError as SchemaValidationError

from ocpp.exceptions import (
    FormatViolationError,
    NotImplementedError,
    OCPPError,
    PropertyConstraintViolationError,
    ProtocolError,
    TypeConstraintViolationError,
    UnknownCallErrorCodeError,
    ValidationError,
)

_validators: Dict[str, Draft4Validator] = {}


class _DecimalEncoder(json.JSONEncoder):
    """Encode values of type `decimal.Decimal` using 1 decimal point.

    A custom encoder is required because `json.dumps()` cannot encode a value
    of type decimal.Decimal. This raises a TypeError:

        >>> import decimal
        >>> import json
        >>> >>> json.dumps(decimal.Decimal(3))
        Traceback (most recent call last):
          File "<stdin>", line 1, in <module>
          File "/home/developer/.pyenv/versions/3.7.0/lib/python3.7/json/__init__.py", line 231, in dumps  # noqa
            return _default_encoder.encode(obj)
          File "/home/developer/.pyenv/versions/3.7.0/lib/python3.7/json/encoder.py", line 199, in encode
            chunks = self.iterencode(o, _one_shot=True)
          File "/home/developer/.pyenv/versions/3.7.0/lib/python3.7/json/encoder.py", line 257, in iterencode
            return _iterencode(o, 0)
          File "/home/developer/.pyenv/versions/3.7.0/lib/python3.7/json/encoder.py", line 179, in default
            raise TypeError(f'Object of type {o.__class__.__name__} '
        TypeError: Object of type Decimal is not JSON serializable

    This can be prevented by using a custom encoder.

    """

    def default(self, obj):
        if isinstance(obj, decimal.Decimal):
            return float("%.1f" % obj)
        return json.JSONEncoder.default(self, obj)


class SchemaValidator:
    def __init__(self, path_to_schemas: str):
        self.path_to_schemas = path_to_schemas

    def get_schema_for_call(self, action: str):
        schema_name = action + "Request"
        return self._get_validator(schema_name)

    def get_schema_for_call_result(self, action: str):
        schema_name = action + "Response"
        return self._get_validator(schema_name)

    def _get_validator(self, schema_name: str):
        path = f"{self.path_to_schemas}/{schema_name}.json"

        if path in _validators:
            return _validators[path]

        # The JSON schemas for OCPP 2.0 start with a byte order mark (BOM)
        # character. If no encoding is given, reading the schema would fail with:
        #
        #     Unexpected UTF-8 BOM (decode using utf-8-sig):
        with open(path, "r", encoding="utf-8-sig") as f:
            data = f.read()
            validator = Draft4Validator(json.loads(data, parse_float=decimal.Decimal))
            _validators[path] = validator

        return _validators[path]


class MessageType:
    """Number identifying the different types of OCPP messages."""

    #: Call identifies a request.
    Call = 2

    #: CallResult identifies a successful response.
    CallResult = 3

    #: CallError identifies an erroneous response.
    CallError = 4


def unpack(msg):
    """
    Unpacks a message into either a Call, CallError or CallResult.
    """
    try:
        msg = json.loads(msg)
    except json.JSONDecodeError:
        raise FormatViolationError(
            details={"cause": "Message is not valid JSON", "ocpp_message": msg}
        )

    if not isinstance(msg, list):
        raise ProtocolError(
            details={
                "cause": (
                    "OCPP message hasn't the correct format. It "
                    f"should be a list, but got '{type(msg)}' "
                    "instead"
                )
            }
        )

    for cls in [Call, CallResult, CallError]:
        try:
            if msg[0] == cls.message_type_id:
                return cls(*msg[1:])
        except IndexError:
            raise ProtocolError(
                details={"cause": "Message does not contain MessageTypeId"}
            )
        except TypeError:
            raise ProtocolError(details={"cause": "Message is missing elements."})

    raise PropertyConstraintViolationError(
        details={"cause": f"MessageTypeId '{msg[0]}' isn't valid"}
    )


def pack(msg):
    """
    Returns the JSON representation of a Call, CallError or CallResult.

    It just calls the 'to_json()' method of the message. But it is here mainly
    to complement the 'unpack' function of this module.
    """
    return msg.to_json()


def validate_payload(
    message: Union[Call, CallResult], schema_validator: SchemaValidator
):
    """Validate the payload of the message using JSON schemas."""
    if type(message) not in [Call, CallResult]:
        raise ValidationError(
            "Payload can't be validated because message "
            f"type. It's '{type(message)}', but it should "
            "be either 'Call'  or 'CallResult'."
        )

    try:
        if message.message_type_id == MessageType.Call:
            validator = schema_validator.get_schema_for_call(action=message.action)
        elif message.message_type_id == MessageType.CallResult:
            validator = schema_validator.get_schema_for_call_result(
                action=message.action
            )

        message.payload = json.loads(
            json.dumps(message.payload), parse_float=decimal.Decimal
        )

    except (OSError, json.JSONDecodeError):
        raise NotImplementedError(
            details={"cause": f"Failed to validate action: {message.action}"}
        )

    try:
        validator.validate(message.payload)
    except SchemaValidationError as e:
        if e.validator == SchemaValidators.type.__name__:
            raise TypeConstraintViolationError(
                details={"cause": e.message, "ocpp_message": message}
            )
        elif e.validator == SchemaValidators.additionalProperties.__name__:
            raise FormatViolationError(
                details={"cause": e.message, "ocpp_message": message}
            )
        elif e.validator == SchemaValidators.required.__name__:
            raise ProtocolError(details={"cause": e.message})
        elif e.validator == "maxLength":
            raise TypeConstraintViolationError(
                details={"cause": e.message, "ocpp_message": message}
            ) from e
        else:
            raise FormatViolationError(
                details={
                    "cause": f"Payload '{message.payload} for action "
                    f"'{message.action}' is not valid: {e}",
                    "ocpp_message": message,
                }
            )


class Call:
    """A Call is a type of message that initiate a request/response sequence.
    Both central systems and charge points can send this message.

    From the specification:

        A Call always consists of 4 elements: The standard elements
        MessageTypeId and UniqueId, a specific Action that is required on the
        other side and a payload, the arguments to the Action. The syntax of a
        call looks like this:

            [<MessageTypeId>, "<UniqueId>", "<Action>", {<Payload>}]

        ...

        For example, a BootNotification request could look like this:

            [2,
             "19223201",
             "BootNotification",
             {
              "chargePointVendor": "VendorX",
              "chargePointModel": "SingleSocketCharger"
             }
            ]
    """

    message_type_id = 2

    def __init__(self, unique_id, action, payload):
        self.unique_id = unique_id
        self.action = action
        self.payload = payload

        if is_dataclass(payload):
            self.payload = asdict(payload)

    def to_json(self):
        """Return a valid JSON representation of the instance."""
        return json.dumps(
            [
                self.message_type_id,
                self.unique_id,
                self.action,
                self.payload,
            ],
            # By default json.dumps() adds a white space after every separator.
            # By setting the separator manually that can be avoided.
            separators=(",", ":"),
            cls=_DecimalEncoder,
        )

    def create_call_result(self, payload):
        call_result = CallResult(self.unique_id, payload)
        call_result.action = self.action
        return call_result

    def create_call_error(self, exception):
        error_code = "InternalError"
        error_description = "An unexpected error occurred."
        error_details = {}

        if isinstance(exception, OCPPError):
            error_code = exception.code
            error_description = exception.description
            error_details = exception.details

        return CallError(
            self.unique_id,
            error_code,
            error_description,
            error_details,
        )

    def __repr__(self):
        return (
            f"<Call - unique_id={self.unique_id}, action={self.action}, "
            f"payload={self.payload}>"
        )


class CallResult:
    """
    A CallResult is a message indicating that a Call has been handled
    successfully.

    From the specification:

        A CallResult always consists of 3 elements: The standard elements
        MessageTypeId, UniqueId and a payload, containing the response to the
        Action in the original Call. The syntax of a call looks like this:

            [<MessageTypeId>, "<UniqueId>", {<Payload>}]

        ...

        For example, a BootNotification response could look like this:

            [3,
             "19223201",
             {
              "status":"Accepted",
              "currentTime":"2013-02-01T20:53:32.486Z",
              "heartbeatInterval":300
             }
            ]

    """

    message_type_id = 3

    def __init__(self, unique_id, payload, action=None):
        self.unique_id = unique_id
        self.payload = payload

        # Strictly speaking no action is required in a CallResult. But in order
        # to validate the message it is needed.
        self.action = action

    def to_json(self):
        return json.dumps(
            [
                self.message_type_id,
                self.unique_id,
                self.payload,
            ],
            # By default json.dumps() adds a white space after every separator.
            # By setting the separator manually that can be avoided.
            separators=(",", ":"),
            cls=_DecimalEncoder,
        )

    def __repr__(self):
        return (
            f"<CallResult - unique_id={self.unique_id}, "
            f"action={self.action}, "
            f"payload={self.payload}>"
        )


class CallError:
    """
    A CallError is a response to a Call that indicates an error.

    From the specification:

        CallError always consists of 5 elements: The standard elements
        MessageTypeId and UniqueId, an errorCode string, an errorDescription
        string and an errorDetails object.

        The syntax of a call looks like this:

            [<MessageTypeId>, "<UniqueId>", "<errorCode>", "<errorDescription>", {<errorDetails>}] # noqa
    """

    message_type_id = 4

    def __init__(self, unique_id, error_code, error_description, error_details=None):
        self.unique_id = unique_id
        self.error_code = error_code
        self.error_description = error_description
        self.error_details = error_details

    def to_json(self):
        return json.dumps(
            [
                self.message_type_id,
                self.unique_id,
                self.error_code,
                self.error_description,
                self.error_details,
            ],
            # By default json.dumps() adds a white space after every separator.
            # By setting the separator manually that can be avoided.
            separators=(",", ":"),
            cls=_DecimalEncoder,
        )

    def to_exception(self):
        """Return the exception that corresponds to the CallError."""
        for error in OCPPError.__subclasses__():
            if error.code == self.error_code:
                return error(
                    description=self.error_description, details=self.error_details
                )

        raise UnknownCallErrorCodeError(
            "Error code '%s' is not defined by the" " OCPP specification",
            self.error_code,
        )

    def __repr__(self):
        return (
            f"<CallError - unique_id={self.unique_id}, "
            f"error_code={self.error_code}, "
            f"error_description={self.error_description}, "
            f"error_details={self.error_details}>"
        )
