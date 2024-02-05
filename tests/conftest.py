try:
    from unittest.mock import AsyncMock
except ImportError:
    # Python 3.7 and below don't include unittest.mock.AsyncMock. Hence,
    # we need to resolve to a package on pypi.
    from asynctest import CoroutineMock as AsyncMock

import pytest


@pytest.fixture
def connection():
    class Connection:
        pass

    connection = Connection()
    connection.send = AsyncMock()

    return connection
