# client.py
import asyncio
import websockets

async def main():
    async with websockets.connect(
        "wss://glowing-computing-machine-4jwxvv9gxvggc55r-9000.app.github.dev/cp_id_1",
        subprotocols=["ocpp1.6"],  # Advertise OCPP 1.6
    ) as ws:
        msg = await ws.recv()
        print("Server says:", msg)

asyncio.run(main())
