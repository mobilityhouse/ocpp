from unittest.mock import AsyncMock
import pytest


@pytest.fixture
def connection():
    class Connection:
        pass

    connection = Connection()
    connection.send = AsyncMock()

    return connection
