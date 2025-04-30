.. image:: https://github.com/mobilityhouse/ocpp/actions/workflows/pull-request.yml/badge.svg?style=svg
   :target: https://github.com/mobilityhouse/ocpp/actions/workflows/pull-request.yml

.. image:: https://img.shields.io/pypi/pyversions/ocpp.svg
   :target: https://pypi.org/project/ocpp/

.. image:: https://img.shields.io/readthedocs/ocpp.svg
   :target: https://ocpp.readthedocs.io/en/latest/

OCPP
----

Python package implementing the JSON version of the Open Charge Point Protocol
(OCPP). Currently OCPP 1.6 (errata v4), OCPP 2.0.1 (Edition 2 FINAL, 2022-12-15 and Edition 3 errata 2024-11)
are supported.

You can find the documentation on `rtd`_.

The purpose of this library is to provide the building blocks to construct a
charging station/charge point and/or charging station management system
(CSMS)/central system. The library does not provide a completed solution, as any
implementation is specific for its intended use. The documents in this library
should be inspected, as these documents provided guidance on how best to
build a complete solution.

Note: "OCPP 2.0.1 contains fixes for all the known issues, to date, not only
the fixes to the messages. This version replaces OCPP 2.0. OCA advises
implementers of OCPP to no longer implement OCPP 2.0 and only use version
2.0.1 going forward."

Installation
------------

You can either the project install from Pypi:

.. code-block:: bash

   $ pip install ocpp

Or clone the project and install it manually using:

.. code-block:: bash

   $ pip install .

Quick start
-----------

Below you can find examples on how to create a simple OCPP 1.6 or 2.0.1 Central
System/CSMS as well as the respective OCPP 1.6 or 2.0.1
Charging Station/Charge Point.

.. note::

   To run these examples the dependency websockets_ is required! Install it by running:

   .. code-block:: bash

      $ pip install websockets

Charging Station Management System (CSMS) / Central System
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The code snippet below creates a simple OCPP 2.0.1 CSMS which
is able to handle BootNotification calls. You can find a detailed explanation of the
code in the `Central System documentation`_.


.. code-block:: python

    import asyncio
    import logging
    import websockets
    from datetime import datetime

    from ocpp.routing import on
    from ocpp.v201 import ChargePoint as cp
    from ocpp.v201 import call_result
    from ocpp.v201.enums import RegistrationStatusEnumType

    logging.basicConfig(level=logging.INFO)


    class ChargePoint(cp):
        @on('BootNotification')
        async def on_boot_notification(self, charging_station, reason, **kwargs):
            return call_result.BootNotificationPayload(
                current_time=datetime.utcnow().isoformat(),
                interval=10,
                status=RegistrationStatusEnumType.accepted
            )


    async def on_connect(websocket, path):
        """ For every new charge point that connects, create a ChargePoint
        instance and start listening for messages.
        """
        try:
            requested_protocols = websocket.request_headers[
                'Sec-WebSocket-Protocol']
        except KeyError:
            logging.info("Client hasn't requested any Subprotocol. "
                     "Closing Connection")
            return await websocket.close()

        if websocket.subprotocol:
            logging.info("Protocols Matched: %s", websocket.subprotocol)
        else:
            # In the websockets lib if no subprotocols are supported by the
            # client and the server, it proceeds without a subprotocol,
            # so we have to manually close the connection.
            logging.warning('Protocols Mismatched | Expected Subprotocols: %s,'
                            ' but client supports  %s | Closing connection',
                            websocket.available_subprotocols,
                            requested_protocols)
            return await websocket.close()

        charge_point_id = path.strip('/')
        cp = ChargePoint(charge_point_id, websocket)

        await cp.start()


    async def main():
        server = await websockets.serve(
            on_connect,
            '0.0.0.0',
            9000,
            subprotocols=['ocpp2.0.1']
        )
        logging.info("WebSocket Server Started")
        await server.wait_closed()

    if __name__ == '__main__':
        asyncio.run(main())

Charging Station / Charge point
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    import asyncio

    from ocpp.v201.enums import RegistrationStatusEnumType
    import logging
    import websockets

    from ocpp.v201 import call
    from ocpp.v201 import ChargePoint as cp

    logging.basicConfig(level=logging.INFO)


    class ChargePoint(cp):

        async def send_boot_notification(self):
            request = call.BootNotificationPayload(
                charging_station={
                    'model': 'Wallbox XYZ',
                    'vendor_name': 'anewone'
                },
                reason="PowerUp"
            )
            response = await self.call(request)

            if response.status == RegistrationStatusEnumType.accepted:
                print("Connected to central system.")


    async def main():
        async with websockets.connect(
                'ws://localhost:9000/CP_1',
                subprotocols=['ocpp2.0.1']
        ) as ws:
            cp = ChargePoint('CP_1', ws)

            await asyncio.gather(cp.start(), cp.send_boot_notification())


    if __name__ == '__main__':
        asyncio.run(main())

Debugging
---------

Python's default log level is `logging.WARNING`. As result most of the logs
generated by this package are discarded. To see the log output of this package
lower the log level to `logging.DEBUG`.

.. code-block:: python

  import logging
  logging.basicConfig(level=logging.DEBUG)

However, this approach defines the log level for the complete logging system.
In other words: the log level of all dependencies is set to `logging.DEBUG`.

To lower the logs for this package only use the following code:

.. code-block:: python

  import logging
  logging.getLogger('ocpp').setLevel(level=logging.DEBUG)
  logging.getLogger('ocpp').addHandler(logging.StreamHandler())

Aknowledgements
---------------

Till the end of 2024, this project has been lead and maintained by `Auke Oosterhoff`_ and
`Jared Newell`_. We thank them for work their work! 

Since than, the project is lead by `Chad Meadowcroft`_, `Mohit Jain`_ and `Patrick Roelke`_.

License
-------

Except from the documents in `docs/v16` and `docs/v201` everything is licensed under MIT_.
© `The Mobility House`_

The documents in `docs/v16` and `docs/v201` are licensed under Creative Commons
Attribution-NoDerivatives 4.0 International Public License.

.. _Central System documentation: https://ocpp.readthedocs.io/en/latest/central_system.html
.. _MIT: https://github.com/mobilityhouse/ocpp/blob/master/LICENSE
.. _rtd: https://ocpp.readthedocs.io/en/latest/index.html
.. _The Mobility House: https://www.mobilityhouse.com/int_en/
.. _websockets: https://pypi.org/project/websockets/

.. _Auke Oosterhoff:  https://github.com/orangetux
.. _Jared Newell: https://github.com/Jared-Newell-Mobility
.. _Chad Meadowcroft: https://github.com/mdwcrft
.. _Mohit Jain: https://github.com/jainmohit2001
.. _Patrick Roelke: https://github.com/proelke
