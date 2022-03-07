from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from ...cpo_class import ChargePoint
from ..classes import WebsocketAdapter
from ...charge_point_operator import CentralSystem

router = APIRouter(tags="WebSocket")
cpo = CentralSystem()

@router.websocket("/chargepoints/{client_id}")
async def websocket_endpoint(websocket: WebSocket, client_id: str):
    try:
        await websocket.accept(subprotocol="ocpp1.6")
        cp_id = websocket.url.path.strip("/chargepoints")
        cp = ChargePoint(cp_id, WebsocketAdapter(websocket))
        queue = cpo.register_charger(cp)
        await queue.get()

    except WebSocketDisconnect:
        socket = WebsocketAdapter()
        await socket.disconnect(websocket)