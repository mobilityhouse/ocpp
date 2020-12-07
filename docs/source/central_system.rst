Central System
==============

The Open Charge Point Protocol defines two roles: the charge point (or the client) and the central
server (or the server). The ocpp Python package can be used to model both sides of the connection.

This document explains how to create a central system and how to model a charge
point at server side. Most of the examples on this page use the `websockets`_
library as implementation of the websockets layer. Note that package isn't
required, other websocket implementations might work as well.


Create a websocket server
-------------------------

The snippet below creates a very simple websocket server that listens at port 9000 for connections
and that prints 'Charge point connected' for every new websocket connection made.

.. code-block:: python

   import asyncio
   import websockets


   async def on_connect(websocket, path):
      await websocket.send('Connection made successfully.')
      print(f'Charge point {path} connected')


   async def main():
      server = await websockets.serve(
         on_connect,
         '0.0.0.0',
         9000,
         subprotocols=['ocpp1.6']
      )

      await server.wait_closed()


   if __name__ == '__main__':
      asyncio.run(main())

There are two things that requires a few words of explanation.

* The `on_connect()` handler that is passed as a first argument to `websockets.serve()`_. This is
  the handler that is executed on every new connection.

  The handler is passed two arguments: an instance of `websockets.server.WebSocketServerProtocol`_
  and the request URI. The request URI is used as identifier for the charge point that made the
  connection. To quote a snippet from section 3.1.1 of the OCPP-J specification:

	*"The charge point's connection URL contains the charge point identity
	so that the Central System knows which charge point a Websocket connection
	belongs to."*

  The handler in this example sends a message to the client and prints a message to the console.


* The `subprotocols` argument in `websockets.serve()` is used to configure the server that it
  supports OCPP 1.6.

After you've started the server you can connect a client to it by using the `websockets` interactive
`client`_:


.. code-block:: shell

   $ python -m websockets ws://localhost:9000/test_charge_point
   Connected to ws://localhost:9000/test_charge_point.
   < Connection made successfully.
   Connection closed: code = 1000 (OK), no reason.


OCPP compliant handler
----------------------

.. note::

   This document describes how to create an central system that supports OCPP
   1.6. The ocpp Python package has support for OCPP 2.0 as well. This
   documentation will be updated soon to reflect that. In the mean time please
   consult the `examples/`_ to learn how to create an OCPP 2.0 central system.

The websocket server created above is not very useful and only sends a non-OCPP compliant message.

Remove the `on_connect()` handler from the code above and replace it by the following snippet.

.. code-block:: python

   from datetime import datetime

   from ocpp.routing import on
   from ocpp.v16 import ChargePoint as cp
   from ocpp.v16.enums import Action, RegistrationStatus
   from ocpp.v16 import call_result


   class MyChargePoint(cp):
       @on(Action.BootNotification)
       async def on_boot_notification(self, charge_point_vendor, charge_point_model, **kwargs):
           return call_result.BootNotificationPayload(
               current_time=datetime.utcnow().isoformat(),
               interval=10,
               status=RegistrationStatus.accepted
           )


   async def on_connect(websocket, path):
       """ For every new charge point that connects, create a ChargePoint instance
       and start listening for messages.

       """
       charge_point_id = path.strip('/')
       cp = MyChargePoint(charge_point_id, websocket)

       await cp.start()


The `on_connect()` handler has been updated and now creates a `MyChargePoint` instance and calls the
`start()`_ coroutine.

`MyChargePoint` subclasses from `ocpp.v16.ChargePoint`_. `ocpp.v16.ChargePoint` is the core of the
ocpp package. This class implements the routing of messages coming from the client to the correct handler.
It also will validate all messages that are being received or being send to the client and it
implements flow control.

Our `MyChargePoint` class uses the `@on()`_ decorator to implement a handler for 'BootNotification'
requests. The `@on()` takes a string with the name of an action as only argument. Although not used
in this example, the package also provides an `@after()`_ decorator that can be used the register a
post request handler.

According to the OCPP specification a payload of a BootNotification request must contain two
required arguments, 'chargePointModel' and 'chargePointVendor', as well as an seven optional
arguments. The handler reflects this by having two required arguments, `charge_point_vendor` and
`charge_point_model`. The handler uses `**kwargs` for the optional arguments.

The handler returns an instance of `ocpp.v16.call_result.BootNotificationPayload`_. This object
is used to create a response that is send back to the client.

.. note::

   OCPP uses a camelCase naming scheme for the keys in the payload. Python, on
   the other hand, uses snake_case.

   Therefore this ocpp package converts all keys in messages from camelCase to
   snake_case and vice versa to make sure you can write Pythonic code.


Now start the websocket server again and connect a client to it as you did before. If the client is
connected send this BootNotification to the central system:

.. code-block:: shell

	`[2, "12345", "BootNotification", {"chargePointVendor": "The Mobility House", "chargePointModel": "Optimus"}]`

The server should respond and the you should see something like this:

.. code-block:: shell

   $ python -m websockets ws://localhost:9000/test_charge_point
   Connected to ws://localhost:9000/test_charge_point.
   > [2, "12345", "BootNotification", {"chargePointVendor": "The Mobility House", "chargePointModel": "Optimus"}]
   < [3, "12345", {"currentTime": "2019-06-16T11:18:09.591716", "interval": 10, "status": "Accepted"}]`

Congratulations! You've created a central system.

You can find the source code of the central system created in this document in the `examples/`_
directory.

.. _client: https://websockets.readthedocs.io/en/stable/intro.html#one-more-thing
.. _examples/: https://github.com/mobilityhouse/ocpp/blob/master/examples
.. _ocpp.v16.call_result.BootNotificationPayload: https://github.com/mobilityhouse/ocpp/blob/3b92c2c53453dd6511a202e1dc1b9aa1a236389e/ocpp/v16/call_result.py#L28
.. _ocpp.v16.ChargePoint: https://github.com/mobilityhouse/ocpp/blob/master/ocpp/v16/charge_point.py#L80
.. _start(): https://github.com/mobilityhouse/ocpp/blob/3b92c2c53453dd6511a202e1dc1b9aa1a236389e/ocpp/v16/charge_point.py#L125
.. _websockets: https://websockets.readthedocs.io/en/stable/
.. _websockets.serve(): https://websockets.readthedocs.io/en/stable/api.html#module-websockets.server
.. _websockets.server.WebsocketServerProtocol: https://websockets.readthedocs.io/en/stable/api.html#websockets.server.WebSocketServerProtocol
.. _@on(): https://github.com/mobilityhouse/ocpp/blob/3b92c2c53453dd6511a202e1dc1b9aa1a236389e/ocpp/routing.py#L4
.. _@after(): https://github.com/mobilityhouse/ocpp/blob/3b92c2c53453dd6511a202e1dc1b9aa1a236389e/ocpp/routing.py#L34
