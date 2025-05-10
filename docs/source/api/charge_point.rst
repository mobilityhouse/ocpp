ChargePoint
===========

.. module:: ocpp.charge_point

The ChargePoint module provides the base class for implementing a Charge Point in OCPP.

ChargePoint
-----------

.. autoclass:: ChargePoint
    :members:
    :undoc-members:
    :special-members: __init__

Core Methods
~~~~~~~~~~~~

.. method:: ChargePoint.start()
   :async:

   Start the main message processing loop.
   
   This method enters an infinite loop to constantly receive and process incoming messages.
   
   This is the main entry point that should be called after initializing a ChargePoint instance.
   
   :return: This method doesn't return, it runs until the connection is closed.

.. method:: ChargePoint.route_message(raw_msg)
   :async:

   Route a message received from a Central System.
   
   If the message is a Call, the corresponding handler is executed.
   If the message is a CallResult or CallError, the message is passed to the call() function.
   
   :param raw_msg: The raw message to route
   :type raw_msg: str
   :return: None

.. method:: ChargePoint.call(payload, suppress=True, unique_id=None, skip_schema_validation=False)
   :async:

   Send a Call message to the Central System and return the response payload.
   
   The given payload is transformed into a Call object by looking at the type.
   
   :param payload: The payload to send (a call.* dataclass)
   :type payload: dataclass
   :param suppress: If True, CallErrors will be suppressed
   :type suppress: bool
   :param unique_id: Unique ID for the call, if not provided a UUID will be generated
   :type unique_id: str, optional
   :param skip_schema_validation: If True, schema validation will be skipped
   :type skip_schema_validation: bool
   :return: The response payload (a call_result.* dataclass)
   :raises asyncio.TimeoutError: If no response is received within the timeout
   :raises CallError: If suppress is False and a CallError is received

Utility Functions
------------------

The ChargePoint module provides several utility functions that are used internally:

.. autofunction:: camel_to_snake_case
.. autofunction:: snake_to_camel_case
.. autofunction:: serialize_as_dict
.. autofunction:: remove_nones
