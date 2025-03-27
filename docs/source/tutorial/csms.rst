Implementing a Charging Station Management System
=================================================

The Charging Station Management System (CSMS) or the Central System is defined as the *manager of the Charging Stations and has the information for authorizing Users for using its Charging Stations*.

.. seealso::

   You van find the OCPP specifications in the `docs <https://github.com/mobilityhouse/ocpp/tree/master/docs>`_ directory of the repository.

Practically the CSMS acts as a server communicating with the Charging Stations in its fleet. The CSMS should implement a websocket endpoint and handle the websocket messages sent by the Charging Stations returning the correctly formatted responses. The CSMS can also initiate websocket messages sent to the Charging Station.

In this tutorial we will use the `websockets library <https://websockets.readthedocs.io/en/stable/index.html>`_ to implement our CSMS and show how ocpp (this library) can be used to implement OCPP compliant messages and responses.

.. note::

   For other websocket implementations refere to the :doc:`/howto/index`

The ChargePoint object
----------------------

The central element in this library is the ChargePoint object. The base class handles the websocket connection, routing of messages and validation of the *Payloads*. Furthermore the class implements both parsing and serialization of the *payloads* so you can work with python native and snake cased objects.

.. note::

   **Payloads** or **PDU** is the term used for the message structures defined in *OCPP*. Typically the messages is a JSON array consisting of a MessageTypeId (call, call result or call error), a unique id for the call (to be used by the call result or errors that follow that call), the action or call type, and the payload object specific to that action/call type.

For each physical Charge Point a ChargePoint object should be instantiated.

.. tab:: v16

    .. code-block:: python
        :caption: csms.py

        from ocpp.v16 import ChargePoint

        async def main():
            cp = ChargePoint("SOME_ID", websocket_connection)
            await cp.start()

.. tab:: v201

    .. code-block:: python
        :caption: csms.py

        from ocpp.v201 import ChargePoint

        async def main():
            cp = ChargePoint("SOME_ID", websocket_connection)
            await cp.start()

The constructor takes an id for the Charge Point and the websocket connection object for that Charge Point. It can also take two optional arguments for response_timeout (default is 30 seconds) and a logger (default logs as the ocpp logger).

.. seealso::

    See :doc:`/topic/logging` for information on how this library handles logging.

It is important to note that this library is an asynchronus implementation of OCPP. Refer to :doc:`/topic/threading` for information on multithreading implementations.  
The main couroutine for our ChargePoint is ``.start()``. This couroutine will await websocket messages and route them to the appropriate handler. If ``.start()`` is not awaited we will not be able to receive calls from the Charge Point nor be able to receive call results from calls we initiated.

Routing
-------

Our ChargePoint object can receive websocket messages currently, but will always fail with a ``NotImplementedError``. This is because we have not implemented any handlers yet.  
To do so we need to subclass the ChargePoint class.

.. note::

   ocpp makes sure to respond with call error according to the OCPP specification when errors are raised during handling of a call.  
   See :doc:`/topic/errorhandling`.

The first message our CSMS will receive is the BootNotification PDU. Let us implement a handler to handle this type of message.

.. tab:: v16

    .. code-block:: python
        :caption: csms.py

        from ocpp.routing import on
        from ocpp.v16 import ChargePoint as cp
        from ocpp.v16 import enums


        class ChargePoint(cp):
            @on(enums.Action.boot_notification)
            def on_boot_notification(self, **kwargs):
                ...

.. tab:: v201

    .. code-block:: python
        :caption: csms.py

        from ocpp.routing import on
        from ocpp.v201 import ChargePoint as cp
        from ocpp.v201 import enums


        class ChargePoint(cp):
            @on(enums.Action.boot_notification)
            def on_boot_notification(self, **kwargs):
                ...

A couple of things are happening in the above code. We are defining a handler for the BootNotification PDU.
To register this handler we use the ``@on()`` decorator. This decorator takes an *Action type* 
and the skip_schema_validation optional boolean (defaults to False).

The Action enum is a convenient way to specify the OCPP PDU types. It has a string constant for every type of 
PDU defined in the OCPP specification. Finally our handler will be passed keyword arguments corresponding to the 
data defined for that action in the OCPP specification.

We are not doing anything in the handler yet, we will get to that. But before let us take a look on another interesting 
routing option. We generally want to avoid blocking the Charge Point, so we will want to respond to the call as quick as possible.
But what if we want to register the Charge Point information in our database, a process that will introduce a slow IO call. 
First, since we are building an async server we want to implement a non-blocking database call. The handler can be both
a regular class method or a couroutine. But an even better solution is to use the ``@after()`` decorator.

.. tab:: v16

    .. code-block:: python
        :caption: csms.py

        import asyncio

        from ocpp.routing import after, on
        ...

        async def slow_db_call(data):
            print("Registering data in the database")
            await asyncio.sleep(5)


        class ChargePoint(cp):
            ...

            @after(enums.Action.boot_notification)
            async def after_boot_notification(self, **kwargs):
                await slow_db_call(kwargs)

.. tab:: v201

    .. code-block:: python
        :caption: csms.py

        import asyncio

        from ocpp.routing import after, on
        ...

        async def slow_db_call(data):
            print("Registering data in the database")
            await asyncio.sleep(5)


        class ChargePoint(cp):
            ...

            @after(enums.Action.boot_notification)
            async def after_boot_notification(self, **kwargs):
                await slow_db_call(kwargs)

The ``@after()`` works similar to ``@on()``. The difference is that the after handler will run after the on handler, which lets us respond to the Charge Point first and run processes that are independent of that response after. The ``@after()`` decorator can also register both regular methods and couroutines.

Now we have handlers for the BootNotification PDU, but our CSMS will still fail, because we have not returned the call result to the Charge Point. Let us see how that is done.

.. note::

   OCPP defines messages with camel case but throughout this library this is converted to snake case for a more pythonic style.

Dataclasses and Enums
---------------------

ocpp library include dataclasses corresponding to each call and call result from the OCPP specification. 
We can use them to make sure our messages are correctly formatted and include the necessary data according to the OCPP specification. 
To return a call result to the Charge Point our ``on`` handler is expected to return a call result dataclass.

.. tab:: v16

    .. code-block:: python
        :caption: csms.py

        ...
        from datetime import datetime, timezone

        ...
        from ocpp.v16 import call_result, enums
        ...


        class ChargePoint(cp):
            @on(enums.Action.boot_notification)
            def on_boot_notification(self, **kwargs):
                time = datetime.now(timezone.utc).isoformat()
                response = call_result.BootNotification(
                    current_time=time,
                    interval=3600,
                    status=enums.RegistrationStatus.accepted
                )
                return response

            ...

.. tab:: v201

    .. code-block:: python
        :caption: csms.py

        ...
        from datetime import datetime, timezone

        ...
        from ocpp.v201 import call_result, enums
        ...


        class ChargePoint(cp):
            @on(enums.Action.boot_notification)
            def on_boot_notification(self, **kwargs):
                time = datetime.now(timezone.utc).isoformat()
                response = call_result.BootNotification(
                    current_time=time,
                    interval=3600,
                    status=enums.RegistrationStatusEnumType.accepted
                )
                return response

            ...

Our handler uses the ``BootNotification`` dataclass to create a response to the Charge Point. 
This dataclass expects 3 attributes corresponding to the OCPP specification (v16 has furthermore two optional attributes). 
We also utilize the registration status enum to ensure the string is compliant with the registration status enum defined 
in the OCPP.

The ``call_result`` module contains dataclasses for all call results defined in the OCPP specification while the ``enums`` module
contains enums for all enums defined in the OCPP specification. Note that these modules are version specific.

The ocpp library not only implements dataclasses for the PDU types (calls and call results) and enums for the OCPP defined enums. 
We can also use dataclasses corresponding to datatypes defined by the OCPP specification.

CSMS Initiated Call
-------------------

Let us implement a call from our CSMS to the Charge Point to start a charging session.

.. tab:: v16

    .. code-block:: python
        :caption: csms.py

        ...
        from ocpp.v16 import call, call_result, enums
        from ocpp.v16.datatypes import ChargingProfile, ChargingSchedule, ChargingSchedulePeriod
        ...


        class ChargePoint(cp):
            ...
            async def remote_start_transaction(self):
                period = ChargingSchedulePeriod(
                    start_period=0,
                    limit=16
                )
                schedule = ChargingSchedule(
                    charging_rate_unit=enums.ChargingRateUnitType.amps,
                    charging_schedule_period=[period]
                )
                profile = ChargingProfile(
                    charging_profile_id=1,
                    stack_level=1,
                    charging_profile_purpose=enums.ChargingProfilePurposeType.tx_default_profile,
                    charging_profile_kind=enums.ChargingProfileKindType.absolute,
                    charging_schedule=schedule
                )
                payload = call.RemoteStartTransaction(id_tag="SOME_ID", charging_profile=profile)

                call_result = await self.call(payload)

.. tab:: v201

    .. code-block:: python
        :caption: csms.py

        ...
        from ocpp.v201 import call, call_result, enums
        from ocpp.v201.datatypes import ChargingSchedulePeriodType, ChargingProfileType, ChargingScheduleType, IdTokenType
        ...


        class ChargePoint(cp):
            ...
            async def remote_start_transaction(self):
                period = ChargingSchedulePeriodType(
                    start_period=0,
                    limit=16
                )
                schedule = ChargingScheduleType(
                    id=1,
                    charging_rate_unit=enums.ChargingRateUnitEnumType.amps,
                    charging_schedule_period=[period]
                )
                profile = ChargingProfileType(
                    id=1,
                    stack_level=1,
                    charging_profile_purpose=enums.ChargingProfilePurposeEnumType.tx_default_profile,
                    charging_profile_kind=enums.ChargingProfileKindEnumType.absolute,
                    charging_schedule=[schedule]
                )
                token = IdTokenType(
                    id_token="SOME_ID",
                    type=enums.IdTokenEnumType.central
                )
                payload = call.RequestStartTransaction(
                    id_token=token,
                    remote_start_id=1,
                    charging_profile=profile
                )

                call_result = await self.call(payload)

We are using multiple dataclasses corresponding to OCPP datatypes. This way we ensure we have the necessary data for the 
payload and that the data is formatted correctly. To send a CSMS initiated call to the Charge Point we simply 
await the ``.call()`` method. The method takes a call dataclass and handles JSON serialization, validation and catching 
the call result. The method will return the corresponding call result parsed as a native dataclass object from our ``call_result`` module.

The ``call`` module contains dataclasses for all calls defined in the OCPP specification while the ``datatypes`` module
contains dataclasses for all datatypes defined in the OCPP specification. Note that these modules are version specific.

The Websocket Server
--------------------

Now we have implemented a basic ChargePoint class that handles BootNotification sent from the Charge Point 
and can send a message to the Charge Point to start charging.

.. important::

   OCPP defines feature profiles that describe which calls the CSMS needs to handle.  
   It is a good idea to implement calls according to the set of feature profiles you want to support.

We are still missing our websocket server that enables the Charge Point to connect. For this we will use the websockets library.

.. note::

   websockets can be installed with ``$ pip install websockets`` or with your preferred package manager.

First we need a connection handler that can instantiate a ChargePoint for every connection and await our start couroutine.

.. code-block:: python
    :caption: csms.py

    ...

    async def on_connect(connection):
        charge_point_id = connection.request.path.strip("/")
        cp = ChargePoint(charge_point_id, connection)
        await cp.start()

This is a simple connection handler that takes a single argument, the websocket connection, 
instantiates a ChargePoint object and awaits ``.start()``. The handler extracts the charge points 
identifier from the request path as specified by the OCPP specification.

We should consider handling when the client closes the connection. 
Right now if the connection is closed websockets raises a ``ConnectionClosedOK`` exception.

.. code-block:: python
    :caption: csms.py

    ...
    import logging

    ...
    from websockets.exceptions import ConnectionClosedOK

    async def on_connect(connection):
        ...

        try:
            await cp.start()
        except ConnectionClosedOK:
            logging.info(f"Charge point <{charge_point_id}> closed the connection")

Instead of getting an exception we simply log that the connection was closed.

.. note::

   It might also be relevant to handle the ``ConnectionClosedError`` exception. This is raised if the connection closes without receiving a proper closing frame.

Last thing to do is to start our server.

.. tab:: v16

    .. code-block:: python
        :caption: csms.py

        ...

        ...
        from websockets import serve
        ...

        async def main():
            async with serve(on_connect, "localhost", 8765, subprotocols=["ocpp1.6"]) as server:
                await server.wait_closed()

.. tab:: v201

    .. code-block:: python
        :caption: csms.py

        ...

        ...
        from websockets import serve
        ...

        async def main():
            async with serve(on_connect, "localhost", 8765, subprotocols=["ocpp2.0.1"]) as server:
                await server.wait_closed()

The above couroutine starts a websocket server that calls ``on_connect()`` for every new connection to ``ws://localhost:8765``.  
We also specify the subprotocol to the correct OCPP version. If the charge point does not request a supported subprotocol in 
the request header, the connection will be rejected in accordance to the OCPP specification.

Finally we want the server to gracefully terminate connections when shutdown. A process is typically terminated with **SIGTERM**. It can also be terminated with *CTRL + C* where a **SIGINT** will be sent.  
Let us intercept the signals and make sure connections are closed gracefully before shutting down.

.. tab:: v16

    .. code-block:: python
        :caption: csms.py

        ...
        import signal

        ...

        async def main():
            async with serve(on_connect, "localhost", 8765, subprotocols=["ocpp1.6"]) as server:
                loop = asyncio.get_running_loop()
                loop.add_signal_handler(signal.SIGINT, server.close)
                loop.add_signal_handler(signal.SIGTERM, server.close)
                await server.wait_closed()


        if __name__ == "__main__":
            logging.basicConfig(level=logging.INFO)
            asyncio.run(main())

.. tab:: v201

    .. code-block:: python
        :caption: csms.py

        ...
        import signal

        ...

        async def main():
            async with serve(on_connect, "localhost", 8765, subprotocols=["ocpp2.0.1"]) as server:
                loop = asyncio.get_running_loop()
                loop.add_signal_handler(signal.SIGINT, server.close)
                loop.add_signal_handler(signal.SIGTERM, server.close)
                await server.wait_closed()


        if __name__ == "__main__":
            logging.basicConfig(level=logging.INFO)
            asyncio.run(main())

Now if the process receives a **SIGINT** or **SIGTERM** it will call ``server.close()`` before shutting down. This ensures that clients receive a proper closing frame.

We also added a starting point where we set the logging level to INFO and start the event loop with ``main()``.

Testing the CSMS
----------------

.. warning::

   Websockets CLI client does not allow for specification of subprotcols.  
   For the following example to work remove the subprotocol argument from your server in the example code.

Websockets provides an interactive websocket client CLI. We can use this to test out our CSMS. First let us start our server.

.. code-block:: shell

   $ python csms.py

In another shell run the websockets client and connect with the CSMS. We can use the interactive client to send messages to the CSMS and see responses.

.. tab:: v16

    .. code-block:: shell

        $ websockets ws://localhost:8765/SOME_ID
        Connected to ws://localhost:8765/SOME_ID
        > [2, "12345", "BootNotification", {"chargePointVendor": "The Mobility House", "chargePointModel": "Optimus"}]
        < [3, "12345", {"currentTime": "2019-06-16T11:18:09.591716", "interval": 3600, "status": "Accepted"}]

.. tab:: v201

    .. code-block:: shell

        $ websockets ws://localhost:8765/SOME_ID
        Connected to ws://localhost:8765/SOME_ID
        > [2, "12345", "BootNotification", {"chargingStation": {"vendorName": "The Mobility House", "model": "Optimus"}, "reason": "PowerUp"}]
        < [3, "12345", {"currentTime": "2019-06-16T11:18:09.591716", "interval": 3600, "status": "Accepted"}]

Our CSMS returns a correctly formatted call result for the BootNotification.
We can see the server activity in our logs.

.. tab:: v16

    .. code-block:: shell

        INFO:websockets.server:server listening on [::1]:8765
        INFO:websockets.server:server listening on 127.0.0.1:8765
        INFO:websockets.server:connection open
        INFO:ocpp:SOME_ID: receive message [2, "12345", "BootNotification", {"chargePointVendor": "The Mobility House", "chargePointModel": "Optimus"}]
        INFO:ocpp:SOME_ID: send [3,"12345",{"currentTime":"2025-02-28T09:26:03.436672+00:00","interval":3600,"status":"Accepted"}]
        Registering data in the database
        INFO:root:Charge point <SOME_ID> closed the connection

.. tab:: v201

    .. code-block:: shell

        INFO:websockets.server:server listening on 127.0.0.1:8765
        INFO:websockets.server:server listening on [::1]:8765
        INFO:websockets.server:connection open
        INFO:ocpp:SOME_ID: receive message [2, "12345", "BootNotification", {"chargingStation": {"vendorName": "The Mobility House", "model": "Optimus"}, "reason": "PowerUp"}]
        INFO:ocpp:SOME_ID: send [3,"12345",{"currentTime":"2025-02-28T09:31:15.045731+00:00","interval":3600,"status":"Accepted"}]
        Registering data in the database
        INFO:root:Charge point <SOME_ID> closed the connection

Full example
------------

.. tab:: v16

    .. literalinclude:: ../../../examples/tutorial/v16/csms.py
        :caption: csms.py
        :language: python
        :linenos:

.. tab:: v201

    .. literalinclude:: ../../../examples/tutorial/v201/csms.py
        :caption: csms.py
        :language: python
        :linenos: