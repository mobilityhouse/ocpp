Installation
============

You can either install the project from Pypi:

.. code-block:: bash

   pip install ocpp

Or clone the project and install it manually using:

.. code-block:: bash

   pip install .

**Dependencies**

- Python 3.11 or higher
- The project also requires a websocket library. We recommend using `websockets`_:

    .. code-block:: bash

        pip install websockets

**Supported Python versions**

This project supports every CPython version that has not reached its
`end of life`_. Support for a new Python version is added once it is
released, and support for a version is dropped in the first minor release
after it reaches end of life. Older releases of this package remain
installable on older interpreters, because ``pip`` only selects releases
whose ``requires-python`` matches the running interpreter.

.. _websockets: https://pypi.org/project/websockets/
.. _end of life: https://devguide.python.org/versions/
