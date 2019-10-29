import pytest
from asynctest import CoroutineMock


@pytest.fixture
def connection():
    class Connection:
        pass

    connection = Connection()
    connection.send = CoroutineMock()

    return connection
