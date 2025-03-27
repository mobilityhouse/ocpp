Implementing a Charge Point
===========================

In the OCPP specification the charge point represents the client side of the websocket connection.
It is a physical charging station that connects to the server for management and
reports state information to the server.

Implementing a charge point is similar to implementing a CSMS. The ChargePoint object
is the representation of a physical charge point. The difference between a CSMS and a
Charge Point is how this object is implemented. More specifically which PDUs or action
types it handles and which it sends.

The OCPP specification describes both CSMS-initiated PDUs (the CSMS sends the call to the charge point;
the charge point responds with the call result) and charge point-initiated PDUs
(the charge point sends the call to the CSMS; the CSMS responds with the call result).
See `OCPP documentation <https://github.com/mobilityhouse/ocpp/tree/master/docs>`_ for details.

.. seealso::

   Most concepts are explained in the :doc:`CSMS tutorial</tutorial/csms>`.
   This tutorial will focus on the differences when implementing a charge point.
   It is recommended to read the :doc:`CSMS tutorial</tutorial/csms>` to get an
   understanding of this library's core concepts.

The ChargePoint Object
----------------------

A central PDU is the BootNotification. This is initiated by the charge point whenever
it boots.

.. tab:: v16

    .. code-block:: python
        :caption: chargepoint.py

        import asyncio

        from ocpp.v16 import ChargePoint as cp
        from ocpp.v16 import call, enums

        class ChargePoint(cp):
            async def send_boot_notification(self):
                request = call.BootNotification(
                    charge_point_model="Optimus", charge_point_vendor="The Mobility House"
                )

                response = await self.call(request)

                if response.status == enums.RegistrationStatus.accepted:
                    await self.synchronize_internal_clock(response.current_time)
                    await self.send_heartbeats(response.interval)
                    print("Connected to central system.")

                if response.status == enums.RegistrationStatus.rejected:
                    print("CSMS rejected connection")
                    await self._connection.close()

                if response.status == enums.RegistrationStatus.pending:
                    print("Status pending | Charge point should not initiate any new messages "
                            "until CSMS accepts registration")

            async def synchronize_internal_clock(self, time):
                print("Setting system time")

            async def send_heartbeats(self, interval):
                while True:
                    await asyncio.sleep(interval)
                    response = await self.call(call.Heartbeat())
                    await self.synchronize_internal_clock(response.current_time)

.. tab:: v201

    .. code-block:: python
        :caption: chargepoint.py

        import asyncio

        from ocpp.v201 import ChargePoint as cp
        from ocpp.v201 import call, enums
        from ocpp.v201.datatypes import ChargingStationType

        class ChargePoint(cp):
            async def send_boot_notification(self):
                station = ChargingStationType(
                    vendor_name="The Mobility House", model="Optimus"
                )
                request = call.BootNotification(
                    charging_station=station, reason=enums.BootReasonEnumType.power_up
                )

                response = await self.call(request)

                if response.status == enums.RegistrationStatusEnumType.accepted:
                    await self.synchronize_internal_clock(response.current_time)
                    await self.send_heartbeats(response.interval)
                    print("Connected to central system.")

                if response.status == enums.RegistrationStatusEnumType.rejected:
                    print("CSMS rejected connection")
                    await self._connection.close()

                if response.status == enums.RegistrationStatusEnumType.pending:
                    print("Status pending | Charge point should not initiate any new messages "
                            "until CSMS accepts registration")

            async def synchronize_internal_clock(self, time):
                print("Setting system time")

            async def send_heartbeats(self, interval):
                while True:
                    await asyncio.sleep(interval)
                    response = await self.call(call.Heartbeat())
                    await self.synchronize_internal_clock(response.current_time)

The BootNotification is also used to synchronize the charge point's internal clock and
to set the interval for when the charge point should send a Heartbeat PDU to the CSMS.

Start the client
----------------

We can use the websockets library as a websocket client as well.
We will need the URL to connect to, our charge point ID for the path, and we should
specify subprotocols.

.. tab:: v16

    .. code-block:: python
        :caption: chargepoint.py

        ...
        import logging

        ...
        from websockets import connect
        from websockets.exceptions import ConnectionClosedOK

        ...

        async def main():
            async with connect("ws://localhost:8765/SOME_ID", subprotocols=["ocpp1.6"]) as connection:
                cp = ChargePoint("SOME_ID", connection)

                try:
                    await asyncio.gather(cp.start(), cp.send_boot_notification())
                except ConnectionClosedOK:
                    print("CSMS closed the connection")

        if __name__ == "__main__":
            logging.basicConfig(level=logging.INFO)
            asyncio.run(main())

.. tab:: v201

    .. code-block:: python
        :caption: chargepoint.py

        ...
        import logging

        ...
        from websockets import connect
        from websockets.exceptions import ConnectionClosedOK

        ...

        async def main():
            async with connect("ws://localhost:8765/SOME_ID", subprotocols=["ocpp2.0.1"]) as connection:
                cp = ChargePoint("SOME_ID", connection)

                try:
                    await asyncio.gather(cp.start(), cp.send_boot_notification())
                except ConnectionClosedOK:
                    print("CSMS closed the connection")

        if __name__ == "__main__":
            logging.basicConfig(level=logging.INFO)
            asyncio.run(main())

After connecting to the CSMS we both run the ``.start()`` coroutine so our charge point is
able to receive messages, and we also send a BootNotification right away.

Testing the Charge Point
------------------------

Let us use our :doc:`CSMS </tutorial/csms>` to test our OCPP Charge Point.
To see the heartbeats in the log, we will adjust the heartbeat interval in our CSMS
to 10 seconds.

.. important::

   You will also need to add a handler for the Heartbeat PDU in the CSMS.

First, open a shell and run the CSMS:

.. code-block:: bash

   $ python csms.py

In another shell, run the charge point:

.. code-block:: bash

   $ python chargepoint.py

The logs from the CSMS should look like this:

.. tab:: v16

    .. code-block:: bash

        INFO:websockets.server:server listening on 127.0.0.1:8765
        INFO:websockets.server:server listening on [::1]:8765
        INFO:websockets.server:connection open
        INFO:ocpp:SOME_ID: receive message [2,"71f1ad82-3336-4f7b-924f-d70f32efec39","BootNotification",{"chargePointModel":"Optimus","chargePointVendor":"The Mobility House"}]
        INFO:ocpp:SOME_ID: send [3,"71f1ad82-3336-4f7b-924f-d70f32efec39",{"currentTime":"2025-03-01T19:23:52.046499+00:00","interval":10,"status":"Accepted"}]
        Registering data in the database
        INFO:ocpp:SOME_ID: receive message [2,"cc18de3d-dbdd-4c25-abb4-c9731963fe5d","Heartbeat",{}]
        Got a heartbeat from SOME_ID
        INFO:ocpp:SOME_ID: send [3,"cc18de3d-dbdd-4c25-abb4-c9731963fe5d",{"currentTime":"2025-03-01T19:24:02.056385+00:00"}]
        INFO:ocpp:SOME_ID: receive message [2,"75461f31-9838-4905-9274-97335e45cf92","Heartbeat",{}]
        Got a heartbeat from SOME_ID
        INFO:ocpp:SOME_ID: send [3,"75461f31-9838-4905-9274-97335e45cf92",{"currentTime":"2025-03-01T19:24:12.064939+00:00"}]

.. tab:: v201

    .. code-block:: bash

        INFO:websockets.server:server listening on 127.0.0.1:8765
        INFO:websockets.server:server listening on [::1]:8765
        INFO:websockets.server:connection open
        INFO:ocpp:SOME_ID: receive message [2,"cd268c5f-175d-485d-b1f1-078b978a2d5c","BootNotification",{"chargingStation":{"vendorName":"The Mobility House","model":"Optimus"},"reason":"PowerUp"}]
        INFO:ocpp:SOME_ID: send [3,"cd268c5f-175d-485d-b1f1-078b978a2d5c",{"currentTime":"2025-03-01T19:29:51.165292+00:00","interval":10,"status":"Accepted"}]
        Registering data in the database
        INFO:ocpp:SOME_ID: receive message [2,"030190f0-0de6-4527-ad1b-75eeeb7c6bb0","Heartbeat",{}]
        Got a heartbeat from SOME_ID
        INFO:ocpp:SOME_ID: send [3,"030190f0-0de6-4527-ad1b-75eeeb7c6bb0",{"currentTime":"2025-03-01T19:30:01.176776+00:00"}]
        INFO:ocpp:SOME_ID: receive message [2,"d11a9516-8e6b-41f2-96e6-7f3ce78da860","Heartbeat",{}]
        Got a heartbeat from SOME_ID
        INFO:ocpp:SOME_ID: send [3,"d11a9516-8e6b-41f2-96e6-7f3ce78da860",{"currentTime":"2025-03-01T19:30:11.185701+00:00"}]

And from the Charge Point you will see:

.. tab:: v16

    .. code-block:: bash

        INFO:ocpp:SOME_ID: send [2,"71f1ad82-3336-4f7b-924f-d70f32efec39","BootNotification",{"chargePointModel":"Optimus","chargePointVendor":"The Mobility House"}]
        INFO:ocpp:SOME_ID: receive message [3,"71f1ad82-3336-4f7b-924f-d70f32efec39",{"currentTime":"2025-03-01T19:23:52.046499+00:00","interval":10,"status":"Accepted"}]
        Setting system time
        INFO:ocpp:SOME_ID: send [2,"cc18de3d-dbdd-4c25-abb4-c9731963fe5d","Heartbeat",{}]
        INFO:ocpp:SOME_ID: receive message [3,"cc18de3d-dbdd-4c25-abb4-c9731963fe5d",{"currentTime":"2025-03-01T19:24:02.056385+00:00"}]
        Setting system time
        INFO:ocpp:SOME_ID: send [2,"75461f31-9838-4905-9274-97335e45cf92","Heartbeat",{}]
        INFO:ocpp:SOME_ID: receive message [3,"75461f31-9838-4905-9274-97335e45cf92",{"currentTime":"2025-03-01T19:24:12.064939+00:00"}]
        Setting system time

.. tab:: v201

    .. code-block:: bash

        INFO:ocpp:SOME_ID: send [2,"cd268c5f-175d-485d-b1f1-078b978a2d5c","BootNotification",{"chargingStation":{"vendorName":"The Mobility House","model":"Optimus"},"reason":"PowerUp"}]
        INFO:ocpp:SOME_ID: receive message [3,"cd268c5f-175d-485d-b1f1-078b978a2d5c",{"currentTime":"2025-03-01T19:29:51.165292+00:00","interval":10,"status":"Accepted"}]
        Setting system time
        INFO:ocpp:SOME_ID: send [2,"030190f0-0de6-4527-ad1b-75eeeb7c6bb0","Heartbeat",{}]
        INFO:ocpp:SOME_ID: receive message [3,"030190f0-0de6-4527-ad1b-75eeeb7c6bb0",{"currentTime":"2025-03-01T19:30:01.176776+00:00"}]
        Setting system time
        INFO:ocpp:SOME_ID: send [2,"d11a9516-8e6b-41f2-96e6-7f3ce78da860","Heartbeat",{}]
        INFO:ocpp:SOME_ID: receive message [3,"d11a9516-8e6b-41f2-96e6-7f3ce78da860",{"currentTime":"2025-03-01T19:30:11.185701+00:00"}]
        Setting system time

Full example
------------

.. tab:: v16

    .. literalinclude:: ../../../examples/tutorial/v16/chargepoint.py
        :caption: chargepoint.py
        :language: python
        :linenos:

.. tab:: v201

    .. literalinclude:: ../../../examples/tutorial/v201/chargepoint.py
        :caption: chargepoint.py
        :language: python
        :linenos:
