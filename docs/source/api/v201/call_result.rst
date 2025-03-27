OCPP 2.0.1 Call Result Messages
============================

.. module:: ocpp.v201.call_result

This module contains dataclasses for OCPP 2.0.1 Call Result messages, which are responses to Call messages.

Common Structure
--------------

Most OCPP 2.0.1 response messages include:

* A ``status`` field indicating the result of the request
* A ``status_info`` field providing additional information about errors (optional)
* A ``custom_data`` field for custom information (optional)

Authentication Responses
---------------------

.. py:class:: Authorize

   Response to an Authorize request.
   
   :param id_token_info: Information about the ID token
   :type id_token_info: datatypes.IdTokenInfoType
   :param certificate_status: Status of the certificate (optional)
   :type certificate_status: enums.AuthorizeCertificateStatusEnumType, optional
   :param custom_data: Custom data (optional)
   :type custom_data: dict, optional

Boot and Status Responses
----------------------

.. py:class:: BootNotification

   Response to a BootNotification request.
   
   :param current_time: Current time in ISO 8601 format
   :type current_time: str
   :param interval: Heartbeat interval in seconds
   :type interval: int
   :param status: Status of the registration
   :type status: enums.RegistrationStatusEnumType
   :param status_info: Additional status information (optional)
   :type status_info: datatypes.StatusInfoType, optional
   :param custom_data: Custom data (optional)
   :type custom_data: dict, optional

.. py:class:: Heartbeat

   Response to a Heartbeat request.
   
   :param current_time: Current time in ISO 8601 format
   :type current_time: str
   :param custom_data: Custom data (optional)
   :type custom_data: dict, optional

.. py:class:: StatusNotification

   Response to a StatusNotification request. This is an empty class except for optional custom data.
   
   :param custom_data: Custom data (optional)
   :type custom_data: dict, optional

Transaction Responses
------------------

.. py:class:: TransactionEvent

   Response to a TransactionEvent request.
   
   :param total_cost: Total cost of the transaction (optional)
   :type total_cost: float, optional
   :param charging_priority: Priority of charging (optional)
   :type charging_priority: int, optional
   :param id_token_info: Information about the ID token (optional)
   :type id_token_info: datatypes.IdTokenInfoType, optional
   :param updated_personal_message: Updated personal message (optional)
   :type updated_personal_message: datatypes.MessageContentType, optional
   :param custom_data: Custom data (optional)
   :type custom_data: dict, optional

.. py:class:: MeterValues

   Response to a MeterValues request. This is an empty class except for optional custom data.
   
   :param custom_data: Custom data (optional)
   :type custom_data: dict, optional

Remote Control Responses
---------------------

.. py:class:: RequestStartTransaction

   Response to a RequestStartTransaction request.
   
   :param status: Status of the request
   :type status: enums.RequestStartStopStatusEnumType
   :param status_info: Additional status information (optional)
   :type status_info: datatypes.StatusInfoType, optional
   :param transaction_id: ID of the started transaction (optional)
   :type transaction_id: str, optional
   :param custom_data: Custom data (optional)
   :type custom_data: dict, optional

.. py:class:: RequestStopTransaction

   Response to a RequestStopTransaction request.
   
   :param status: Status of the request
   :type status: enums.RequestStartStopStatusEnumType
   :param status_info: Additional status information (optional)
   :type status_info: datatypes.StatusInfoType, optional
   :param custom_data: Custom data (optional)
   :type custom_data: dict, optional

Charging Profile Responses
-----------------------

.. py:class:: SetChargingProfile

   Response to a SetChargingProfile request.
   
   :param status: Status of the request
   :type status: enums.ChargingProfileStatusEnumType
   :param status_info: Additional status information (optional)
   :type status_info: datatypes.StatusInfoType, optional
   :param custom_data: Custom data (optional)
   :type custom_data: dict, optional

.. py:class:: ClearChargingProfile

   Response to a ClearChargingProfile request.
   
   :param status: Status of the request
   :type status: enums.ClearChargingProfileStatusEnumType
   :param status_info: Additional status information (optional)
   :type status_info: datatypes.StatusInfoType, optional
   :param custom_data: Custom data (optional)
   :type custom_data: dict, optional

.. py:class:: GetChargingProfiles

   Response to a GetChargingProfiles request.
   
   :param status: Status of the request
   :type status: enums.GetChargingProfileStatusEnumType
   :param status_info: Additional status information (optional)
   :type status_info: datatypes.StatusInfoType, optional
   :param custom_data: Custom data (optional)
   :type custom_data: dict, optional

.. py:class:: ReportChargingProfiles

   Response to a ReportChargingProfiles request. This is an empty class except for optional custom data.
   
   :param custom_data: Custom data (optional)
   :type custom_data: dict, optional

Reset and Availability Responses
-----------------------------

.. py:class:: Reset

   Response to a Reset request.
   
   :param status: Status of the request
   :type status: enums.ResetStatusEnumType
   :param status_info: Additional status information (optional)
   :type status_info: datatypes.StatusInfoType, optional
   :param custom_data: Custom data (optional)
   :type custom_data: dict, optional

.. py:class:: ChangeAvailability

   Response to a ChangeAvailability request.
   
   :param status: Status of the request
   :type status: enums.ChangeAvailabilityStatusEnumType
   :param status_info: Additional status information (optional)
   :type status_info: datatypes.StatusInfoType, optional
   :param custom_data: Custom data (optional)
   :type custom_data: dict, optional

Data Transfer Response
-------------------

.. py:class:: DataTransfer

   Response to a DataTransfer request.
   
   :param status: Status of the request
   :type status: enums.DataTransferStatusEnumType
   :param status_info: Additional status information (optional)
   :type status_info: datatypes.StatusInfoType, optional
   :param data: Data returned (optional)
   :type data: any, optional
   :param custom_data: Custom data (optional)
   :type custom_data: dict, optional

Variable and Monitoring Responses
------------------------------

.. py:class:: GetVariables

   Response to a GetVariables request.
   
   :param get_variable_result: List of results for the requested variables
   :type get_variable_result: list[datatypes.GetVariableResultType]
   :param custom_data: Custom data (optional)
   :type custom_data: dict, optional

.. py:class:: SetVariables

   Response to a SetVariables request.
   
   :param set_variable_result: List of results for the variables to set
   :type set_variable_result: list[datatypes.SetVariableResultType]
   :param custom_data: Custom data (optional)
   :type custom_data: dict, optional

.. py:class:: SetVariableMonitoring

   Response to a SetVariableMonitoring request.
   
   :param set_monitoring_result: List of results for the monitoring settings
   :type set_monitoring_result: list[datatypes.SetMonitoringResultType]
   :param custom_data: Custom data (optional)
   :type custom_data: dict, optional

.. py:class:: ClearVariableMonitoring

   Response to a ClearVariableMonitoring request.
   
   :param clear_monitoring_result: List of results for clearing monitoring
   :type clear_monitoring_result: list[enums.ClearMonitoringStatusEnumType]
   :param custom_data: Custom data (optional)
   :type custom_data: dict, optional

Firmware Responses
---------------

.. py:class:: UpdateFirmware

   Response to an UpdateFirmware request.
   
   :param status: Status of the request
   :type status: enums.FirmwareStatusEnumType
   :param status_info: Additional status information (optional)
   :type status_info: datatypes.StatusInfoType, optional
   :param custom_data: Custom data (optional)
   :type custom_data: dict, optional

.. py:class:: FirmwareStatusNotification

   Response to a FirmwareStatusNotification request. This is an empty class except for optional custom data.
   
   :param custom_data: Custom data (optional)
   :type custom_data: dict, optional

Note: This list is not exhaustive; OCPP 2.0.1 defines many more response message types that correspond to the request messages described in the call module.
