Routing
=======

.. module:: ocpp.routing

The routing module provides decorators for routing OCPP messages to handler methods.

Decorators
---------

.. function:: on(action, *, skip_schema_validation=False)

   Function decorator to mark a method as handler for a specific OCPP action.
   
   The wrapped function may be async or sync. It will receive keyword arguments derived from
   the payload of the specific action. The handler should return a relevant payload to be
   returned to the Central System.
   
   :param action: The OCPP action to handle (from enums.Action)
   :type action: str
   :param skip_schema_validation: If True, skip schema validation for this action
   :type skip_schema_validation: bool
   :return: Decorated function
   
   Example usage::
   
       class MyChargePoint(cp):
           @on(Action.boot_notification)
           def on_boot_notification(self, charge_point_model, charge_point_vendor, **kwargs):
               # Handle boot notification
               return call_result.BootNotificationPayload(...)

.. function:: after(action)

   Function decorator to mark a method as post-request hook for a specific OCPP action.
   
   This hook is called after the primary handler has been executed and the response has been sent.
   It receives the same arguments as the primary handler.
   
   :param action: The OCPP action to hook after (from enums.Action)
   :type action: str
   :return: Decorated function
   
   Example usage::
   
       class MyChargePoint(cp):
           @after(Action.start_transaction)
           async def after_start_transaction(self, id_tag, connector_id, **kwargs):
               # Custom logic to perform after a transaction has started
               await self.update_transaction_log(id_tag, connector_id)

Helper Functions
--------------

.. function:: create_route_map(obj)

   Iterates over all attributes of the class looking for methods which have been
   decorated by the @on() or @after() decorators. It returns a dictionary where
   the action names are the keys and the decorated functions are the values.
   
   :param obj: Instance to create route map for
   :type obj: object
   :return: A dictionary mapping actions to handler functions
   :rtype: dict
