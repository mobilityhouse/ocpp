import websockets
from functools import partial


from http_cpo import CentralSystem
from cp_cpo_v201 import ChargePoint


async def on_connect(websocket, path, cpo):
    """ For every new charge point that connects, create a ChargePoint instance
    and start listening for messages.

    The ChargePoint is registered at the CSMS.

    """
    charge_point_id = path.strip("/")
    cp = ChargePoint(charge_point_id, websocket)

    print(f"Charger {cp.id} connected.")

    # If this handler returns the connection will be destroyed. Therefore we need some
    # synchronization mechanism that blocks until CSMS wants to close the connection.
    # An `asyncio.Queue` is used for that.
    queue = cpo.register_charger(cp)
    await queue.get()

    
async def create_websocket_server(cpo: CentralSystem):
    """ Creating a websocket server that Charge Points can connect to. Using IP, Port and
    the subprotocol ocpp1.6 (ocpp2.0.1 for the newer version)"""
    handler = partial(on_connect, cpo=cpo)
    return await websockets.serve(handler, "0.0.0.0", 9000, subprotocols=["ocpp1.6"])