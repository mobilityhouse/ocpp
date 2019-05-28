.. image:: https://circleci.com/gh/mobilityhouse/ocpp/tree/master.svg?style=svg
   :target: https://circleci.com/gh/mobilityhouse/ocpp/tree/master

.. image:: https://img.shields.io/pypi/pyversions/ocpp.svg
   :target: https://pypi.org/project/ocpp/

.. image:: https://img.shields.io/readthedocs/ocpp.svg
   :target: https://ocpp.readthedocs.io/en/latest/

OCPP
----

Python package implementing the JSON version of the Open Charge Point Protocol (OCPP). Currently
only OCPP 1.6 is supported.

Installation
------------

You can either the project install from Pypi:

.. code-block:: bash

   $ pip install ocpp

Or clone the project and install it manually using:

.. code-block:: bash

   $ pip install .

Quick start
----------

Below you can find examples on how to create a simple charge point as well as a charge point.

.. note::

   To run these examples the dependency websockets_ is required! Install it by running:

   .. code-block:: bash

      $ pip install websockets

Central system
~~~~~~~~~~~~~~

.. code-block:: python

   import asyncio
   import websockets
   from datetime import datetime

   from ocpp.routing import on
   from ocpp.v16 import ChargePoint as cp
   from ocpp.v16.enums import Action, RegistrationStatus
   from ocpp.v16 import call_result


   class ChargePoint(cp):
       @on(Action.BootNotification)
       def on_boot_notitication(self, charge_point_vendor, charge_point_model, **kwargs):
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
       cp = ChargePoint(charge_point_id, websocket)

       await cp.start()


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

Charge point
~~~~~~~~~~~~

.. code-block:: python

   import asyncio
   import websockets

   from ocpp.v16 import call, ChargePoint as cp
   from ocpp.v16.enums import RegistrationStatus


   class ChargePoint(cp):
       async def send_boot_notification(self):
           request = call.BootNotificationPayload(
               charge_point_model="Optimus",
               charge_point_vendor="The Mobility House"
           )

           response = await self.call(request)

           if response.status ==  RegistrationStatus.accepted:
               print("Connected to central system.")


   async def main():
       async with websockets.connect(
           'ws://localhost:9000/CP_1',
            subprotocols=['ocpp1.6']
       ) as ws:

           cp = ChargePoint('CP_1', ws)

           await asyncio.gather(cp.start(), cp.send_boot_notification())


   if __name__ == '__main__':
       asyncio.run(main())

License
-------

Except from the documents in `docs/v16/specification/` everything is licensed under MIT_.
© `The Mobility House`_

The documents in `docs/v16/specification/` are licensed under Creative Commons
Attribution-NoDerivatives 4.0 International Public License.

.. _MIT: https://github.com/mobilityhouse/ocpp/blob/master/LICENSE
.. _The Mobility House: https://www.mobilityhouse.com/int_en/
.. _websockets: https://pypi.org/project/websockets/
