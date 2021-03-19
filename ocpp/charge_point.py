from ocpp.routing import Router, Context, LOGGER


class ChargePoint(Router):
    """
    Base Class for ChargePoints.
    """

    def __init__(self, id, connection, response_timeout=30):
        """
        Args:

            id (str): ID of the charger.
            connection: Connection to CP.
            response_timeout (int): When no response on a request is received
                within this interval, a asyncio.TimeoutError is raised.

        """
        context = Context(id=id, connection=connection)
        super().__init__(context=context, response_timeout=response_timeout)

    async def start(self):
        while True:
            message = await self._connection.recv()
            LOGGER.info("%s: receive message %s", self.id, message)

            await self.route_message(message)
