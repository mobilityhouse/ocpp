""" Module containing classes that model the several OCPP messages types. It
also contain some helper functions for packing and unpacking messages.  """
import os
import json
from dataclasses import asdict, is_dataclass

from jsonschema import validate
from jsonschema.exceptions import ValidationError as SchemaValidationError

from ocpp.v16.enums import MessageType
from ocpp.exceptions import (OCPPError, FormatViolationError,
                             PropertyConstraintViolationError,
                             ProtocolError, ValidationError,
                             UnknownCallErrorCodeError)

_schemas = {}


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


def get_schema(name):
    """
    Read schema from disk and return in. Reads will be cached for performance
    reasons.
    """
    if name in _schemas:
        return _schemas[name]

    dir,  _ = os.path.split(os.path.realpath(__file__))
    path = os.path.join(dir, f'v16/schemas/{name}.json')

    with open(path, 'r') as f:
        data = f.read()
        _schemas[name] = json.loads(data)

    return _schemas[name]


def validate_payload(payload, action, message_type_id):
    if message_type_id not in [MessageType.Call, MessageType.CallResult]:
        raise ValidationError("Payload can't be validated because message "
                              f"type id isn't valid. It's '{message_type_id}',"
                              f" but it should be either '{MessageType.Call}' "
                              f" or'{MessageType.CallResult}'.")

    schema_name = action
    if message_type_id == MessageType.CallResult:
        schema_name += 'Response'

    try:
        schema = get_schema(schema_name)
    except (OSError, json.JSONDecodeError) as e:
        raise ValidationError("Failed to load validation schema for action "
                              f"'{action}': {e}")

    if action in ['SetChargingProfile', 'RemoteStartTransaction']:
        # todo: special actions
        pass

    try:
        validate(payload, schema)
    except SchemaValidationError as e:
        raise ValidationError(f"Payload '{payload} for action '{action}' is "
                              f"not valid: {e}")


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
        validate_payload(self.payload, self.action, self.message_type_id)
        return json.dumps([
            self.message_type_id,
            self.unique_id,
            self.action,
            self.payload,
        ])

    def create_call_result(self, payload):
        call_result = CallResult(self.unique_id, payload)
        call_result.action = self.action
        return call_result

    def create_call_error(self, exception):
        error_code = "InternalError"
        error_description = "An unexpected error occured."
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
        MessageTypeId and UniqueId and apayload, containing the response to the
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
        validate_payload(self.payload, self.action, self.message_type_id)

        return json.dumps([
            self.message_type_id,
            self.unique_id,
            self.payload,
        ])

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
        ])

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
