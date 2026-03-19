Basic usage
===========

This library provides foundational components for developing a Charging Station (Charge Point) and/or a Charging Station Management System (CSMS)/Central System.
It is not a complete out-of-the-box solution, as implementations are typically tailored to specific use cases.
Please refer to the accompanying documentation for guidance on how to effectively build a complete solution using this library.

The Open Charge Point Protocol defines two roles: the charge point (or the client) and the central server (or the server).
The ocpp Python package can be used to model both sides of the connection.

..  toctree::
    :maxdepth: 1

    server_side
    client_side
