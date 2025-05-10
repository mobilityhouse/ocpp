OCPP 2.0.1 Datatypes
=================

.. module:: ocpp.v201.datatypes

This module contains dataclasses that define complex data types used in OCPP 2.0.1 messages. OCPP 2.0.1 introduces many more structured datatypes compared to OCPP 1.6.

Core Types
---------

.. py:class:: StatusInfoType

   Element providing more information about the status.
   
   :param reason_code: Reason code for the status
   :type reason_code: str
   :param additional_info: Additional information about the status (optional)
   :type additional_info: str, optional

Authentication Types
-----------------

.. py:class:: IdTokenType

   Contains an identifier to use for authorization and the type of authorization.
   
   :param id_token: The ID token
   :type id_token: str
   :param type: Type of the ID token
   :type type: enums.IdTokenEnumType
   :param additional_info: Additional information about the ID token (optional)
   :type additional_info: list[AdditionalInfoType], optional

.. py:class:: AdditionalInfoType

   Contains a case insensitive identifier and the type of identifier.
   
   :param additional_id_token: The additional ID token
   :type additional_id_token: str
   :param type: Type of the additional ID token
   :type type: str

.. py:class:: IdTokenInfoType

   Contains status information about an identifier.
   
   :param status: Status of the ID token
   :type status: enums.AuthorizationStatusEnumType
   :param cache_expiry_date_time: Expiry date of the cached token (optional)
   :type cache_expiry_date_time: str, optional
   :param charging_priority: Priority for charging (optional)
   :type charging_priority: int, optional
   :param language_1: Preferred language (optional)
   :type language_1: str, optional
   :param evse_id: List of EVSE IDs the token is allowed to use (optional)
   :type evse_id: list[int], optional
   :param language_2: Secondary preferred language (optional)
   :type language_2: str, optional
   :param group_id_token: Group ID token (optional)
   :type group_id_token: IdTokenType, optional
   :param personal_message: Personal message for the token holder (optional)
   :type personal_message: MessageContentType, optional

Component Types
------------

.. py:class:: ComponentType

   A physical or logical component.
   
   :param name: Name of the component
   :type name: str
   :param instance: Instance name of the component (optional)
   :type instance: str, optional
   :param evse: EVSE information (optional)
   :type evse: EVSEType, optional

.. py:class:: EVSEType

   Electric Vehicle Supply Equipment.
   
   :param id: EVSE ID
   :type id: int
   :param connector_id: Connector ID (optional)
   :type connector_id: int, optional

.. py:class:: VariableType

   Reference key to a component-variable.
   
   :param name: Name of the variable
   :type name: str
   :param instance: Instance name of the variable (optional)
   :type instance: str, optional

Charging Types
-----------

.. py:class:: ChargingStationType

   The physical system where an Electrical Vehicle (EV) can be charged.
   
   :param vendor_name: Vendor name of the charging station
   :type vendor_name: str
   :param model: Model of the charging station
   :type model: str
   :param modem: Modem information (optional)
   :type modem: ModemType, optional
   :param serial_number: Serial number (optional)
   :type serial_number: str, optional
   :param firmware_version: Firmware version (optional)
   :type firmware_version: str, optional

.. py:class:: ChargingProfileType

   A ChargingProfile consists of ChargingSchedule, describing the amount of power or current that can be delivered.
   
   :param id: ID of the charging profile
   :type id: int
   :param stack_level: Stack level of the profile
   :type stack_level: int
   :param charging_profile_purpose: Purpose of the charging profile
   :type charging_profile_purpose: enums.ChargingProfilePurposeEnumType
   :param charging_profile_kind: Kind of the charging profile
   :type charging_profile_kind: enums.ChargingProfileKindEnumType
   :param charging_schedule: List of charging schedules
   :type charging_schedule: list[ChargingScheduleType]
   :param valid_from: Start time of validity (optional)
   :type valid_from: str, optional
   :param valid_to: End time of validity (optional)
   :type valid_to: str, optional
   :param transaction_id: Transaction ID this profile is intended for (optional)
   :type transaction_id: str, optional
   :param recurrency_kind: Recurrency kind of this profile (optional)
   :type recurrency_kind: enums.RecurrencyKindEnumType, optional

.. py:class:: ChargingScheduleType

   Charging schedule structure defines a list of charging periods.
   
   :param id: ID of the charging schedule
   :type id: int
   :param charging_rate_unit: Unit of the charging schedule
   :type charging_rate_unit: enums.ChargingRateUnitEnumType
   :param charging_schedule_period: List of periods in this schedule
   :type charging_schedule_period: list[ChargingSchedulePeriodType]
   :param start_schedule: Starting point of the schedule (optional)
   :type start_schedule: str, optional
   :param duration: Duration of the schedule in seconds (optional)
   :type duration: int, optional
   :param min_charging_rate: Minimum charging rate (optional)
   :type min_charging_rate: float, optional
   :param sales_tariff: Sales tariff (optional)
   :type sales_tariff: SalesTariffType, optional

.. py:class:: ChargingSchedulePeriodType

   Charging schedule period structure defines a time period in a charging schedule.
   
   :param start_period: Start of the period in seconds from start of schedule
   :type start_period: int
   :param limit: Power or current limit during the period
   :type limit: float
   :param number_phases: Number of phases (optional)
   :type number_phases: int, optional
   :param phase_to_use: Phase to use (optional)
   :type phase_to_use: int, optional

Transaction Types
--------------

.. py:class:: TransactionType

   Information about a transaction.
   
   :param transaction_id: ID of the transaction
   :type transaction_id: str
   :param charging_state: State of charging (optional)
   :type charging_state: enums.ChargingStateEnumType, optional
   :param time_spent_charging: Time spent charging in seconds (optional)
   :type time_spent_charging: int, optional
   :param stopped_reason: Reason the transaction was stopped (optional)
   :type stopped_reason: enums.ReasonEnumType, optional
   :param remote_start_id: ID of the remote start request (optional)
   :type remote_start_id: int, optional

.. py:class:: MeterValueType

   Collection of sampled values taken at a point in time.
   
   :param timestamp: Timestamp of the samples
   :type timestamp: str
   :param sampled_value: List of sampled values
   :type sampled_value: list[SampledValueType]

.. py:class:: SampledValueType

   Single sampled value in MeterValues.
   
   :param value: The sampled value
   :type value: float
   :param context: Context of the value (optional)
   :type context: enums.ReadingContextEnumType, optional
   :param measurand: Type of measurand (optional)
   :type measurand: enums.MeasurandEnumType, optional
   :param phase: Phase to which this value applies (optional)
   :type phase: enums.PhaseEnumType, optional
   :param location: Location of the measurement (optional)
   :type location: enums.LocationEnumType, optional
   :param signed_meter_value: Signed meter value (optional)
   :type signed_meter_value: SignedMeterValueType, optional
   :param unit_of_measure: Unit of measure (optional)
   :type unit_of_measure: UnitOfMeasureType, optional

Variable Management Types
----------------------

.. py:class:: GetVariableDataType

   Class to hold parameters for GetVariables request.
   
   :param component: Component containing the variable
   :type component: ComponentType
   :param variable: Variable to get
   :type variable: VariableType
   :param attribute_type: Type of attribute to get (optional)
   :type attribute_type: enums.AttributeEnumType, optional

.. py:class:: GetVariableResultType

   Class to hold results of GetVariables request.
   
   :param attribute_status: Status of the get operation
   :type attribute_status: enums.GetVariableStatusEnumType
   :param component: Component containing the variable
   :type component: ComponentType
   :param variable: Variable that was retrieved
   :type variable: VariableType
   :param attribute_type: Type of attribute (optional)
   :type attribute_type: enums.AttributeEnumType, optional
   :param attribute_value: Value of the attribute (optional)
   :type attribute_value: str, optional
   :param attribute_status_info: Additional status information (optional)
   :type attribute_status_info: StatusInfoType, optional

.. py:class:: SetVariableDataType

   Class to hold parameters for SetVariables request.
   
   :param attribute_value: Value to set
   :type attribute_value: str
   :param component: Component containing the variable
   :type component: ComponentType
   :param variable: Variable to set
   :type variable: VariableType
   :param attribute_type: Type of attribute to set (optional)
   :type attribute_type: enums.AttributeEnumType, optional

.. py:class:: SetVariableResultType

   Class to hold results of SetVariables request.
   
   :param attribute_status: Status of the set operation
   :type attribute_status: enums.SetVariableStatusEnumType
   :param component: Component containing the variable
   :type component: ComponentType
   :param variable: Variable that was set
   :type variable: VariableType
   :param attribute_type: Type of attribute (optional)
   :type attribute_type: enums.AttributeEnumType, optional
   :param attribute_status_info: Additional status information (optional)
   :type attribute_status_info: StatusInfoType, optional

Monitoring Types
-------------

.. py:class:: SetMonitoringDataType

   Class to hold parameters of SetVariableMonitoring request.
   
   :param value: Value to monitor
   :type value: float
   :param type: Type of monitoring
   :type type: enums.MonitorEnumType
   :param severity: Severity level
   :type severity: int
   :param component: Component containing the variable
   :type component: ComponentType
   :param variable: Variable to monitor
   :type variable: VariableType
   :param id: ID of the monitor (optional)
   :type id: int, optional
   :param transaction: Whether to monitor during transactions (optional)
   :type transaction: bool, optional

.. py:class:: SetMonitoringResultType

   Class to hold result of SetVariableMonitoring request.
   
   :param status: Status of the operation
   :type status: enums.SetMonitoringStatusEnumType
   :param type: Type of monitoring
   :type type: enums.MonitorEnumType
   :param severity: Severity level
   :type severity: int
   :param component: Component containing the variable
   :type component: ComponentType
   :param variable: Variable being monitored
   :type variable: VariableType
   :param id: ID of the monitor (optional)
   :type id: int, optional
   :param status_info: Additional status information (optional)
   :type status_info: StatusInfoType, optional

Note: This list is not exhaustive; OCPP 2.0.1 defines many more complex datatypes that are used in the messages described in the call and call_result modules.
