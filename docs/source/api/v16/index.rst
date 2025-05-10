OCPP 1.6
========

.. module:: ocpp.v16

The ``ocpp.v16`` module provides the implementation for OCPP 1.6.

Overview
-------

OCPP 1.6 is a widely adopted version of the Open Charge Point Protocol. This module provides 
classes and utilities specific to this version of the protocol.

ChargePoint Class
---------------

.. class:: ChargePoint

   OCPP 1.6 implementation of the ChargePoint class.
   
   This class extends the base ChargePoint class with OCPP 1.6 specific functionality.
   
   .. attribute:: _call
      
      Reference to the v16 call module.
   
   .. attribute:: _call_result
      
      Reference to the v16 call_result module.
   
   .. attribute:: _ocpp_version
      :type: str
      :value: "1.6"
      
      OCPP version string.

Available Submodules
------------------

.. toctree::
   :maxdepth: 1
   
   call
   call_result
   datatypes
   enums
