Messages
=======

.. module:: ocpp.messages

The messages module contains classes and functions for handling OCPP messages.

Constants
--------

.. class:: MessageType

   Constants identifying the different types of OCPP messages.

   .. attribute:: Call
      :type: int
      :value: 2
      
      Identifies a request message.
   
   .. attribute:: CallResult
      :type: int
      :value: 3
      
      Identifies a successful response message.
   
   .. attribute:: CallError
      :type: int
      :value: 4
      
      Identifies an error response message.

Functions
--------

.. function:: unpack(msg)

   Unpacks a JSON message string into a Call, CallResult, or CallError object.
   
   :param msg: The JSON message to unpack
   :type msg: str
   :return: A Call, CallResult, or CallError object
   :raises FormatViolationError: If the message is not valid JSON
   :raises ProtocolError: If the message doesn't have the correct format
   :raises PropertyConstraintViolationError: If the message type is invalid

.. function:: pack(msg)

   Returns the JSON representation of a Call, CallResult, or CallError object.
   
   :param msg: The message object to pack
   :type msg: Call, CallResult, or CallError
   :return: A JSON string representation of the message
   :rtype: str

.. function:: get_validator(message_type_id, action, ocpp_version, parse_float=float)

   Read schema from disk and return as `Draft4Validator`. Instances will be cached for performance reasons.
   
   :param message_type_id: Type of message (from MessageType)
   :type message_type_id: int
   :param action: The OCPP action (e.g., "BootNotification")
   :type action: str
   :param ocpp_version: OCPP version (e.g., "1.6", "2.0", "2.0.1")
   :type ocpp_version: str
   :param parse_float: Function to parse float values, default is float()
   :type parse_float: callable
   :return: A JSON schema validator
   :rtype: jsonschema.Draft4Validator
   :raises ValueError: If ocpp_version is not one of "1.6", "2.0", "2.0.1"

.. function:: validate_payload(message, ocpp_version)
   :async:

   Validate the payload of a message using JSON schemas.
   
   :param message: The message to validate
   :type message: Call or CallResult
   :param ocpp_version: OCPP version (e.g., "1.6", "2.0", "2.0.1")
   :type ocpp_version: str
   :raises ValidationError: If validation fails
   :raises FormatViolationError: If payload format is invalid
   :raises TypeConstraintViolationError: If type constraints are violated
   :raises ProtocolError: If required fields are missing

Message Classes
-------------

.. class:: Call

   A Call is a message that initiates a request/response sequence.
   
   :param unique_id: Unique ID for the call
   :type unique_id: str
   :param action: The action to perform (e.g., "BootNotification")
   :type action: str
   :param payload: The payload for the action
   :type payload: dict or dataclass
   
   .. attribute:: message_type_id
      :type: int
      :value: 2
      
      The OCPP message type identifier for Call messages.
   
   .. method:: to_json()
      
      Return a valid JSON representation of the instance.
      
      :return: JSON string
      :rtype: str
   
   .. method:: create_call_result(payload)
      
      Create a CallResult object for this Call.
      
      :param payload: Response payload
      :type payload: dict
      :return: CallResult object
      :rtype: CallResult
   
   .. method:: create_call_error(exception)
      
      Create a CallError object for this Call.
      
      :param exception: The exception that caused the error
      :type exception: Exception
      :return: CallError object
      :rtype: CallError

.. class:: CallResult

   A CallResult is a message indicating that a Call has been handled successfully.
   
   :param unique_id: Unique ID matching the original Call
   :type unique_id: str
   :param payload: The response payload
   :type payload: dict
   :param action: The action from the original Call (optional, used for validation)
   :type action: str, optional
   
   .. attribute:: message_type_id
      :type: int
      :value: 3
      
      The OCPP message type identifier for CallResult messages.
   
   .. method:: to_json()
      
      Return a valid JSON representation of the instance.
      
      :return: JSON string
      :rtype: str

.. class:: CallError

   A CallError is a response to a Call that indicates an error.
   
   :param unique_id: Unique ID matching the original Call
   :type unique_id: str
   :param error_code: The error code (usually from an OCPPError subclass)
   :type error_code: str
   :param error_description: Description of the error
   :type error_description: str
   :param error_details: Additional error details
   :type error_details: dict, optional
   
   .. attribute:: message_type_id
      :type: int
      :value: 4
      
      The OCPP message type identifier for CallError messages.
   
   .. method:: to_json()
      
      Return a valid JSON representation of the instance.
      
      :return: JSON string
      :rtype: str
   
   .. method:: to_exception()
      
      Return the exception that corresponds to this CallError.
      
      :return: Exception object
      :rtype: OCPPError subclass
      :raises UnknownCallErrorCodeError: If the error code is not recognized
