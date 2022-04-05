class WebsocketAdapter():
    def __init__(self, websocket):
        self._ws = websocket
  
    async def recv(self):
        return await self._ws.receive_text()

    async def send(self, msg):
        await self._ws.send_text(msg)

    def disconnect(self, websocket):
        self.active_connections.remove(websocket)

class SessionType():
    one_phase = "OnePhase"
    three_phase = "ThreePhase"