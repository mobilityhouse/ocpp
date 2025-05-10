Client side usage
=================

This document explains how to create a charge point and connect it to a central system.

The following snippet creates a simple websocket client that connects to a central system running locally on port 9000.

.. code-block:: python

    # client.py
    import asyncio

    import websockets

    from ocpp.v16 import ChargePoint as cp
    from ocpp.v16 import call, call_result
    from ocpp.v16.enums import RegistrationStatus


    class ChargePoint(cp):

        async def send_boot_notification(self):
            request = call.BootNotification(
                charge_point_model="Wallbox XYZ",
                charge_point_vendor="acme",
            )
            response: call_result.BootNotification = await self.call(request)

            if response.status == RegistrationStatus.accepted:
                print("Connected to central system.")


    async def main():
        async with websockets.connect(
            "ws://localhost:9000/CP_1", subprotocols=["ocpp1.6"]
        ) as ws:
            charge_point = ChargePoint("CP_1", ws)

            await asyncio.gather(
                charge_point.start(),
                charge_point.send_boot_notification(),
            )


    if __name__ == "__main__":
        asyncio.run(main())



A few things to note about the above code:

- The `websockets.connect()`_ method is used to create a websocket connection to the server.
  The first argument is the URL on which the connection is made. Note the ``CP_1`` suffix which is the charge point identifier.

- The subprotocol parameter is used to specify the OCPP version that the client supports.
  To connect with OCPP 2.0.1, you can specify the subprotocol as follows:
    
    .. code-block:: python
    
        subprotocols=["ocpp2.0.1"]

- The ``ChargePoint`` class subclasses the same `ocpp.v16.ChargePoint`_ class that is used in the server example.
  This class implements the OCPP protocol and handles the communication with the server.

- The ``send_boot_notification()`` method sends a ``BootNotification`` request to the server.
  To create a valid OCPP 1.6 message, the ocpp package provides support via pre-defined dataclasses that can be found in the `call`_ module.

- The `ocpp.v16.ChargePoint`_ expose a public coroutine: `call()`_, that accepts a payload, serializes it to a OCPP compliant message, and sends it to the server.
  It returns a serialized message in the form of the corresponding `call_result`_ dataclass. In the above case it's the `ocpp.v16.call_result.BootNotification`_ dataclass.
  This allows you to focus on the business logic and let ocpp package handle all the heavy lifting which includes serialization, deserialization, and validation of payloads.

- The `asyncio.gather()`_ method is used to run multiple corouting concurrently.
  In this case, the ``start()`` method starts listening messages from the server and the ``send_boot_notification()`` method sends the ``BootNotification`` request to the server.

After running the above script, you should see the following output:

.. code-block:: bash

    $ python client.py
    CP_1: send [2, "e4c131d6-6b2c-4f50-9a0e-9242a37acb7a", "BootNotification", {"chargePointVendor": "Wallbox XYZ", "chargePointModel": "acme"}]
    CP_1: receive message [3, "e4c131d6-6b2c-4f50-9a0e-9242a37acb7a", {"currentTime": "2025-05-10T12:00:00+00:00", "interval": 10, "status": "Accepted"}]
    Connected to central system.

.. _websockets.connect(): https://websockets.readthedocs.io/en/stable/reference/asyncio/client.html#websockets.asyncio.client.connect
.. _ocpp.v16.ChargePoint: https://github.com/search?q=repo%3Amobilityhouse%2Focpp+%22class+ChargePoint%28%22+path%3A%2F%5Eocpp%5C%2Fv16%5C%2F%2F&type=code
.. _call: https://github.com/mobilityhouse/ocpp/blob/master/ocpp/v16/call.py
.. _call_result: https://github.com/mobilityhouse/ocpp/blob/master/ocpp/v16/call_result.py
.. _call(): https://github.com/search?q=repo%3Amobilityhouse%2Focpp+%22def+call%22&type=code
.. _ocpp.v16.call_result.BootNotification: https://github.com/search?q=repo%3Amobilityhouse%2Focpp+%22class+BootNotification%22+path%3A%2F%5Eocpp%5C%2Fv16%5C%2Fcall_result%2F&type=code
.. _asyncio.gather(): https://docs.python.org/3/library/asyncio-task.html#running-tasks-concurrently
