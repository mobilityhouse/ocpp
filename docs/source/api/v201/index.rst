OCPP 2.0.1
=========

.. module:: ocpp.v201

The ``ocpp.v201`` module provides the implementation for OCPP 2.0.1.

Overview
-------

OCPP 2.0.1 is the latest version of the Open Charge Point Protocol. This module provides 
classes and utilities specific to this version of the protocol, which introduces significant 
changes compared to OCPP 1.6 including new features and a revised message structure.

ChargePoint Class
---------------

.. class:: ChargePoint

   OCPP 2.0.1 implementation of the ChargePoint class.
   
   This class extends the base ChargePoint class with OCPP 2.0.1 specific functionality.
   
   .. attribute:: _call
      
      Reference to the v201 call module.
   
   .. attribute:: _call_result
      
      Reference to the v201 call_result module.
   
   .. attribute:: _ocpp_version
      :type: str
      :value: "2.0.1"
      
      OCPP version string.

Major Differences from OCPP 1.6
-----------------------------

* OCPP 2.0.1 introduces a more structured approach with component/variable model
* Introduces security profiles 
* Improved firmware management
* Transaction events instead of Start/Stop transaction
* Monitoring capabilities
* Enhanced diagnostics
* New charging-related features including Smart Charging

Available Submodules
------------------

.. toctree::
   :maxdepth: 1
   
   call
   call_result
   datatypes
   enums
