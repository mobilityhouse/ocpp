Server side usage
=================

This document explains how to create a central system and how to model a charge point at server side.


Create a websocket server
-------------------------

The following snippet creates a simple websocket server that listens on port 9000.
For every new websocket connection, the server prints *'Charge point connected'*.

.. code-block:: python

    # server.py
    import asyncio
    import websockets

    async def on_connect(connection: websockets.ServerConnection):
        await connection.send('Connection made successfully')
        print(f'Charge point connected: {connection.request.path}')

    async def main():
        server = await websockets.serve(
            on_connect,
            '0.0.0.0',
            9000,
            subprotocols=['ocpp1.6'],
        )
        await server.wait_closed()
    
    if __name__ == '__main__':
        asyncio.run(main())

A few things to note about the above code:

- The ``on_connect()`` handler receives an instance of `websockets.ServerConnection`_.
  This is the handler that is executed on every new connection.

  You can access the request URI of the connection using `connection.request`_.
  The request URI is used as identifier for the charge point that made the connection.
  To quote a snippet from section 3.1.1 of the OCPP-J specification:

    *"The charge point's connection URL contains the charge point identity so that the Central System knows which charge point a Websocket connection belongs to."*

- The subprotocols parameter is used to specify the OCPP version that the server supports.
  You can specify multiple subprotocols as follows:

    .. code-block:: python
    
        subprotocols=['ocpp1.6', 'ocpp2.0.1']

After you have started the server, connect a websocket client to it by using the websockets interactive client:

.. code-block:: bash

   $ python -m websockets ws://localhost:9000/cp_id_1
   Connected to ws://localhost:9000/cp_id_1.
   < Connection made successfully
   Connection closed: 1000 (OK).

OCPP compliant handler
----------------------

The above example is a simple websocket server that does not implement the OCPP protocol.
Remove the ``on_connect()`` handler from the code above and replace it by the following snippet:

.. code-block:: python

    # server.py
    from datetime import datetime, timezone
    import websockets

    from ocpp.routing import on
    from ocpp.v16 import ChargePoint as cp
    from ocpp.v16 import call_result
    from ocpp.v16.enums import Action, RegistrationStatus


    class MyChargePoint(cp):
        @on(Action.boot_notification)
        async def on_boot_notification(
            self, charge_point_vendor, charge_point_model, **kwargs
        ):
            return call_result.BootNotification(
                current_time=datetime.now(tz=timezone.utc).isoformat(),
                interval=10,
                status=RegistrationStatus.accepted,
            )


    async def on_connect(connection: websockets.ServerConnection):
        """
        For every new connection, create a new ChargePoint instance,
        and start listening for messages.
        """
        charge_point_id = connection.request.path.split("/")[-1]
        charge_point = MyChargePoint(charge_point_id, connection)

        await charge_point.start()


The ``on_connect()`` handler has been updated and now creates an instance of a ``MyChargePoint`` class and calls the `start()`_ coroutine.

The ``MyChargePoint`` class subclasses the `ocpp.v16.ChargePoint`_ class which is the core of the ocpp package.
This class implements the routing of messages from the client to the correct handler. It also validates the messages are are being sent and received.

In the above example, the `MyChargePoint` class implements a method ``on_boot_notification`` that handles the ocpp ``BootNotification`` message.
The `@on()`_ decorator which takes a string with the name of an action as a required argument, is responsible for registering the handler for the `BootNotification` message.
This package also provides an `@after()`_ decorator that can be used to register a post request handler.

According to the OCPP specification a payload of a ``BootNotification`` request must contain two required arguments: ``chargePointModel`` and ``chargePointVendor``, as well as an seven optional arguments.
The handler reflects this by having two required arguments, ``charge_point_vendor`` and ``charge_point_model``.
The handler uses ``**kwargs`` for the optional arguments.

The handler returns an instance of `ocpp.v16.call_result.BootNotification`_.
This object is used to create a valid response that is to be sent back to the client.

.. important::

    OCPP uses a camelCase naming scheme for the keys in the JSON payload. Python, on the other hand, uses snake_case.
    Therefore this package converts all the keys in messages from camelCase to snake_case and vice versa to make sure that the code is Pythonic.

Now start the websocket server and connect a websocket client to it.
If the client is connected, send the following BootNotification message to the server:

.. code-block:: shell

    `[2, "12345", "BootNotification", {"chargePointVendor": "The Mobility House", "chargePointModel": "Optimus"}]`

The server should response and you should see something like this:

.. code-block:: shell

    $ python -m websockets ws://localhost:9000/cp_id_1
    Connected to ws://localhost:9000/cp_id_1.
    cp_id_1: receive message [2, "12345", "BootNotification", {"chargePointVendor": "The Mobility House", "chargePointModel": "Optimus"}]
    cp_id_1: send [3, "12345", {"currentTime": "2025-05-10T12:00:00+00:00", "interval": 10, "status": "Accepted"}]

.. _websockets.ServerConnection: https://websockets.readthedocs.io/en/stable/reference/asyncio/server.html#websockets.asyncio.server.ServerConnection
.. _connection.request: https://websockets.readthedocs.io/en/stable/reference/datastructures.html#websockets.http11.Request
.. _start(): https://github.com/search?q=repo%3Amobilityhouse%2Focpp+%22def+start%22&type=code
.. _ocpp.v16.ChargePoint: https://github.com/search?q=repo%3Amobilityhouse%2Focpp+%22class+ChargePoint%28%22+path%3A%2F%5Eocpp%5C%2Fv16%5C%2F%2F&type=code
.. _@on(): https://github.com/search?q=repo%3Amobilityhouse%2Focpp+%22def+on%28%22&type=code
.. _@after(): https://github.com/search?q=repo%3Amobilityhouse%2Focpp+%22def+after%28%22&type=code
.. _ocpp.v16.call_result.BootNotification: https://github.com/search?q=repo%3Amobilityhouse%2Focpp+%22class+BootNotification%22+path%3A%2F%5Eocpp%5C%2Fv16%5C%2Fcall_result%2F&type=code


Congratulations!
You have successfully created a simple websocket server that implements the OCPP protocol.
You can now start implementing the other messages that are required for your application.
