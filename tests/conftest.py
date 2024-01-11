import sys

from unittest.mock import AsyncMock

import pytest

if sys.version_info < (3, 8):
    from asynctest import CoroutineMock as AsyncMock
    

@pytest.fixture
def connection():
    class Connection:
        pass

    connection = Connection()
    connection.send = AsyncMock()

    return connection
