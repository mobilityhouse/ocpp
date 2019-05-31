# OCPP

Python package implementing the JSON version of the Open Charge Point Protocol (OCPP). Currently
only OCPP 1.6 is supported.

## Installation

You can either install from Pypi:

``` bash
$ pip install ocpp
```

Or install the package by running:

``` bash
$ pip install .
```

## Usage

Below you can find examples on how to create a simple charge point as well as a charge point.

**Note**: to run these examples the dependency `websockets` is required! Install it by running:

``` bash
$  pip install websockets
```

### Central system

``` python
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
```

### Charge point

``` python
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
```

# License

Except from the documents in `docs/v16/specification/` everything is licensed under [MIT](LICENSE).
[© The Mobility House](https://www.mobilityhouse.com/int_en/).

The documents in `docs/v16/specification/` are licensed under Creative Commons
Attribution-NoDerivatives 4.0 International Public License.
