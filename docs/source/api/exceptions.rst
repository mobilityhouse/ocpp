Exceptions
=========

.. module:: ocpp.exceptions

The exceptions module contains custom exceptions used by the OCPP library.

Base Exception
-------------

.. exception:: OCPPError

   Base class for all OCPP errors. This class should not be raised directly, only its subclasses.
   
   :param description: Description of the error
   :type description: str, optional
   :param details: Additional details about the error
   :type details: dict, optional
   
   .. attribute:: default_description
      :type: str
      
      Default description used if no description is provided.
   
   .. attribute:: code
      :type: str
      
      The error code used in OCPP CallError messages. Defined in subclasses.

Protocol Error Exceptions
-----------------------

.. exception:: NotImplementedError

   Raised when a requested action is recognized but not supported by the receiver.
   
   .. attribute:: code
      :type: str
      :value: "NotImplemented"
   
   .. attribute:: default_description
      :type: str
      :value: "Request Action is recognized but not supported by the receiver"

.. exception:: NotSupportedError

   Raised when a requested action is not known by the receiver.
   
   .. attribute:: code
      :type: str
      :value: "NotSupported"
   
   .. attribute:: default_description
      :type: str
      :value: "Requested Action is not known by receiver"

.. exception:: InternalError

   Raised when an internal error occurred and the receiver was not able to process the request.
   
   .. attribute:: code
      :type: str
      :value: "InternalError"
   
   .. attribute:: default_description
      :type: str
      :value: "An internal error occurred and the receiver was not able to process the requested Action successfully"

.. exception:: ProtocolError

   Raised when the payload for an action is incomplete.
   
   .. attribute:: code
      :type: str
      :value: "ProtocolError"
   
   .. attribute:: default_description
      :type: str
      :value: "Payload for Action is incomplete"

.. exception:: SecurityError

   Raised when a security issue prevents the receiver from completing the action.
   
   .. attribute:: code
      :type: str
      :value: "SecurityError"
   
   .. attribute:: default_description
      :type: str
      :value: "During the processing of Action a security issue occurred preventing receiver from completing the Action successfully"

Format Violation Exceptions
-------------------------

.. exception:: FormatViolationError

   Raised when the payload for an action is syntactically incorrect.
   
   .. attribute:: code
      :type: str
      :value: "FormatViolation"
   
   .. attribute:: default_description
      :type: str
      :value: "Payload for Action is syntactically incorrect or structure for Action"

.. exception:: FormationViolationError

   Used for strict OCPP 1.6 compliance (typo in the specification).
   
   .. attribute:: code
      :type: str
      :value: "FormationViolation"
   
   .. attribute:: default_description
      :type: str
      :value: "Payload for Action is syntactically incorrect or structure for Action"

Constraint Violation Exceptions
-----------------------------

.. exception:: PropertyConstraintViolationError

   Raised when a field contains an invalid value.
   
   .. attribute:: code
      :type: str
      :value: "PropertyConstraintViolation"
   
   .. attribute:: default_description
      :type: str
      :value: "Payload is syntactically correct but at least one field contains an invalid value"

.. exception:: OccurenceConstraintViolationError

   Used for strict OCPP 1.6 compliance (typo in the specification).
   
   .. attribute:: code
      :type: str
      :value: "OccurenceConstraintViolation"
   
   .. attribute:: default_description
      :type: str
      :value: "Payload for Action is syntactically correct but at least one of the fields violates occurence constraints"

.. exception:: OccurrenceConstraintViolationError

   Raised when a field violates occurrence constraints.
   
   .. attribute:: code
      :type: str
      :value: "OccurrenceConstraintViolation"
   
   .. attribute:: default_description
      :type: str
      :value: "Payload for Action is syntactically correct but at least one of the fields violates occurence constraints"

.. exception:: TypeConstraintViolationError

   Raised when a field violates data type constraints.
   
   .. attribute:: code
      :type: str
      :value: "TypeConstraintViolation"
   
   .. attribute:: default_description
      :type: str
      :value: "Payload for Action is syntactically correct but at least one of the fields violates data type constraints (e.g. \"somestring\": 12)"

Other Exceptions
--------------

.. exception:: GenericError

   Generic error for all other types of errors.
   
   .. attribute:: code
      :type: str
      :value: "GenericError"
   
   .. attribute:: default_description
      :type: str
      :value: "Any other error not all other OCPP defined errors"

.. exception:: ValidationError

   Raised when validation of a message payload fails. This is not an official OCPP error.

.. exception:: UnknownCallErrorCodeError

   Raised when a CallError is received with an unknown error code.
