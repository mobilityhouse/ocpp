""" Module containing classes that model the several OCPP messages types. It
also contain some helper functions for packing and unpacking messages.  """
import os
import json
import decimal
from typing import Callable, Dict
from dataclasses import asdict, is_dataclass

from jsonschema import Draft4Validator
from jsonschema.exceptions import ValidationError as SchemaValidationError

from ocpp.exceptions import (OCPPError, FormatViolationError,
                             PropertyConstraintViolationError,
                             ProtocolError, ValidationError,
                             UnknownCallErrorCodeError)

_validators: Dict[str, Draft4Validator] = {}


class _DecimalEncoder(json.JSONEncoder):
    """ Encode values of type `decimal.Decimal` using 1 decimal point.

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


class MessageType:
    """ Number identifying the different types of OCPP messages. """
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
    except json.JSONDecodeError as e:
        raise FormatViolationError(f'Message is not valid JSON: {e}')

    if not isinstance(msg, list):
        raise ProtocolError("OCPP message hasn't the correct format. It "
                            f"should be a list, but got {type(msg)} instead")

    for cls in [Call, CallResult, CallError]:
        try:
            if msg[0] == cls.message_type_id:
                return cls(*msg[1:])
        except IndexError:
            raise ProtocolError("Message doesn\'t contain MessageTypeID")

    raise PropertyConstraintViolationError(f"MessageTypeId '{msg[0]}' isn't "
                                           "valid")


def pack(msg):
    """
    Returns the JSON representation of a Call, CallError or CallResult.

    It just calls the 'to_json()' method of the message. But it is here mainly
    to complement the 'unpack' function of this module.
    """
    return msg.to_json()


def get_validator(
        message_type_id: int,
        action: str,
        ocpp_version: str,
        parse_float: Callable = float
) -> Draft4Validator:
    """
    Read schema from disk and return as `Draft4Validator`. Instances will be
    cached for performance reasons.

    The `parse_float` argument can be used to set the conversion method that
    is used to parse floats. It must be a callable taking 1 argument. By
    default it is `float()`, but certain schema's require `decimal.Decimal()`.
    """
    if ocpp_version not in ["1.6", "2.0", "2.0.1"]:
        raise ValueError

    schemas_dir = 'v' + ocpp_version.replace('.', '')

    schema_name = action
    if message_type_id == MessageType.CallResult:
        schema_name += 'Response'
    elif message_type_id == MessageType.Call:
        if ocpp_version in ["2.0", "2.0.1"]:
            schema_name += 'Request'

    if ocpp_version == "2.0":
        schema_name += '_v1p0'

    cache_key = schema_name + '_' + ocpp_version
    if cache_key in _validators:
        return _validators[cache_key]

    dir,  _ = os.path.split(os.path.realpath(__file__))
    relative_path = f'{schemas_dir}/schemas/{schema_name}.json'
    path = os.path.join(dir, relative_path)

    # The JSON schemas for OCPP 2.0 start with a byte order mark (BOM)
    # character. If no encoding is given, reading the schema would fail with:
    #
    #     Unexpected UTF-8 BOM (decode using utf-8-sig):
    with open(path, 'r', encoding='utf-8-sig') as f:
        data = f.read()
        validator = Draft4Validator(json.loads(data, parse_float=parse_float))
        _validators[cache_key] = validator

    return _validators[cache_key]


def validate_payload(message, ocpp_version):
    """ Validate the payload of the message using JSON schemas. """
    if type(message) not in [Call, CallResult]:
        raise ValidationError("Payload can't be validated because message "
                              f"type. It's '{type(message)}', but it should "
                              "be either 'Call'  or 'CallResult'.")

    try:
        # 3 OCPP 1.6 schedules have fields of type floats. The JSON schema
        # defines a certain precision for these fields of 1 decimal. A value of
        # 21.4 is valid, whereas a value if 4.11 is not.
        #
        # The problem is that Python's internal representation of 21.4 might
        # have more than 1 decimal. It might be 21.399999999999995. This would
        # make the validation fail, although the payload is correct. This is a
        # known issue with jsonschemas, see:
        # https://github.com/Julian/jsonschema/issues/247
        #
        # This issue can be fixed by using a different parser for floats than
        # the default one that is used.
        #
        # Both the schema and the payload must be parsed using the different
        # parser for floats.
        if ocpp_version == '1.6' and (
            (type(message) == Call and
                message.action in ['SetChargingProfile', 'RemoteStartTransaction'])  # noqa
            or
            (type(message) == CallResult and
                message.action == 'GetCompositeSchedule')
        ):
            validator = get_validator(
                message.message_type_id, message.action,
                ocpp_version, parse_float=decimal.Decimal
            )

            message.payload = json.loads(
                json.dumps(message.payload), parse_float=decimal.Decimal
            )
        else:
            validator = get_validator(
                message.message_type_id, message.action, ocpp_version
            )
    except (OSError, json.JSONDecodeError) as e:
        raise ValidationError("Failed to load validation schema for action "
                              f"'{message.action}': {e}")

    try:
        validator.validate(message.payload)
    except SchemaValidationError as e:
        raise ValidationError(f"Payload '{message.payload} for action "
                              f"'{message.action}' is not valid: {e}")


class Call:
    """ A Call is a type of message that initiate a request/response sequence.
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
        """ Return a valid JSON representation of the instance. """
        return json.dumps([
            self.message_type_id,
            self.unique_id,
            self.action,
            self.payload,
        ],
            # By default json.dumps() adds a white space after every separator.
            # By setting the separator manually that can be avoided.
            separators=(',', ':'),
            cls=_DecimalEncoder
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
        return f"<Call - unique_id={self.unique_id}, action={self.action}, " \
               f"payload={self.payload}>"


class CallResult:
    """
    A CallResult is a message indicating that a Call has been handled
    succesfully.

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
        return json.dumps([
            self.message_type_id,
            self.unique_id,
            self.payload,
        ],
            # By default json.dumps() adds a white space after every separator.
            # By setting the separator manually that can be avoided.
            separators=(',', ':'),
            cls=_DecimalEncoder
        )

    def __repr__(self):
        return f"<CallResult - unique_id={self.unique_id}, " \
               f"action={self.action}, " \
               f"payload={self.payload}>"


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

    def __init__(self, unique_id, error_code, error_description,
                 error_details=None):
        self.unique_id = unique_id
        self.error_code = error_code
        self.error_description = error_description
        self.error_details = error_details

    def to_json(self):
        return json.dumps([
            self.message_type_id,
            self.unique_id,
            self.error_code,
            self.error_description,
            self.error_details,
        ],
            # By default json.dumps() adds a white space after every separator.
            # By setting the separator manually that can be avoided.
            separators=(',', ':'),
            cls=_DecimalEncoder
        )

    def to_exception(self):
        """ Return the exception that corresponds to the CallError. """
        for error in OCPPError.__subclasses__():
            if error.code == self.error_code:
                return error(
                    description=self.error_description,
                    details=self.error_details
                )

        raise UnknownCallErrorCodeError("Error code '%s' is not defined by the"
                                        " OCPP specification", self.error_code)

    def __repr__(self):
        return f"<CallError - unique_id={self.unique_id}, " \
               f"error_code={self.error_code}, " \
               f"error_description={self.error_description}, " \
               f"error_details={self.error_details}>"
