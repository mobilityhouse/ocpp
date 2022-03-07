import websockets
from functools import partial
import logging

from http_cpo import CentralSystem
from cp_cpo import ChargePoint


async def on_connect(websocket, path, cpo):
    """ For every new charge point that connects, create a ChargePoint instance
    and start listening for messages.

    The ChargePoint is registered at the CSMS.

    """

    try:
        authorization = websocket.request_headers[
            'Authorization'
        ]
    except KeyError:
        logging.error(
           "Client hasn't requested any Authorization. Closing Connection"
        )
        return await websocket.close()

    try:
        requested_protocols = websocket.request_headers[
            'Sec-WebSocket-Protocol']
    except KeyError:
        logging.error(
            "Client hasn't requested any Subprotocol. Closing Connection"
        )
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

    print(authorization)


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
    return await websockets.serve(handler, "localhost", 9000, subprotocols=["ocpp1.6"]
    )