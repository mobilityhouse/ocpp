import asyncio

from http_cpo import CentralSystem

import http_server
from websocket_server import create_websocket_server


async def main():
    cpo = CentralSystem()
    websocket_server = await create_websocket_server(cpo)
    http = await http_server.create_http_server(cpo)

    await asyncio.wait([websocket_server.wait_closed(), http.start()])


if __name__ == "__main__":
    asyncio.run(main())