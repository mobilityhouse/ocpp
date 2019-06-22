import asyncio
import websockets


async def on_connect(websocket, path):
    await websocket.send('Connection made succesfully.')
    print(f'charge point connected at {path}')

    while True:
        print(await websocket.recv())


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
