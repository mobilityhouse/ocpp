from abc import ABC
from abc import abstractmethod


class AsyncMessageHandler(ABC):
    @abstractmethod
    async def handle(self, connection_uid: str, message: str) -> None:
        """
        Handle the given message (which can be for a specific connection, if a
        single handler is used to handle messages to multiple connections).
        """
        pass
