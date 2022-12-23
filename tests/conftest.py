try:
    from unittest.mock import AsyncMock
except ImportError:
    from asynctest import CoroutineMock as AsyncMock

import pytest


@pytest.fixture
def connection():
    class Connection:
        pass

    connection = Connection()
    connection.send = AsyncMock()

    return connection
