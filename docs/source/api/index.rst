API Reference
============

This section provides detailed documentation for the OCPP library's API.

The library is structured around several core components:

* **ChargePoint** - The main class that handles communication between the Charge Point and Central System
* **Routing** - Decorators for routing incoming messages to handler methods
* **Messages** - Classes and functions for handling OCPP messages
* **Exceptions** - Custom exceptions for error handling
* **OCPP Versions** - Version-specific implementations (1.6 and 2.0.1)

.. toctree::
   :maxdepth: 2
   
   charge_point
   routing
   messages
   exceptions
   v16/index
   v201/index
