OCPP 1.6 Datatypes
================

.. module:: ocpp.v16.datatypes

This module contains dataclasses that define complex data types used in OCPP 1.6 messages.

.. py:class:: IdTagInfo

   Contains status information about an identifier.
   
   :param status: Authorization status (from enums.AuthorizationStatus)
   :type status: enums.AuthorizationStatus
   :param parent_id_tag: Parent ID tag (optional)
   :type parent_id_tag: str, optional
   :param expiry_date: Expiry date of the ID tag (optional)
   :type expiry_date: str, optional

.. py:class:: AuthorizationData

   Elements that constitute an entry of a Local Authorization List update.
   
   :param id_tag: The identifier
   :type id_tag: str
   :param id_tag_info: Information about the ID tag (optional)
   :type id_tag_info: IdTagInfo, optional

.. py:class:: ChargingSchedulePeriod

   Defines a period in a charging schedule.
   
   :param start_period: Start of the period in seconds from start of schedule
   :type start_period: int
   :param limit: Power or current limit during the period
   :type limit: float
   :param number_phases: Number of phases (optional)
   :type number_phases: int, optional

.. py:class:: ChargingSchedule

   Defines a charging schedule.
   
   :param charging_rate_unit: Unit of the charging schedule (from enums.ChargingRateUnitType)
   :type charging_rate_unit: enums.ChargingRateUnitType
   :param charging_schedule_period: List of periods in this schedule
   :type charging_schedule_period: list[ChargingSchedulePeriod]
   :param duration: Duration of the schedule in seconds (optional)
   :type duration: int, optional
   :param start_schedule: Starting point of the schedule (optional)
   :type start_schedule: str, optional
   :param min_charging_rate: Minimum charging rate (optional)
   :type min_charging_rate: float, optional

.. py:class:: ChargingProfile

   A ChargingProfile consists of a ChargingSchedule, describing the amount of power or current that can be delivered.
   
   :param charging_profile_id: Unique identifier for this profile
   :type charging_profile_id: int
   :param stack_level: Stack level of this profile
   :type stack_level: int
   :param charging_profile_purpose: Purpose of this profile (from enums.ChargingProfilePurposeType)
   :type charging_profile_purpose: enums.ChargingProfilePurposeType
   :param charging_profile_kind: Kind of this profile (from enums.ChargingProfileKindType)
   :type charging_profile_kind: enums.ChargingProfileKindType
   :param charging_schedule: The charging schedule
   :type charging_schedule: ChargingSchedule
   :param transaction_id: Transaction ID this profile is intended for (optional)
   :type transaction_id: int, optional
   :param recurrency_kind: Recurrency kind of this profile (optional)
   :type recurrency_kind: enums.RecurrencyKind, optional
   :param valid_from: Start time of validity (optional)
   :type valid_from: str, optional
   :param valid_to: End time of validity (optional)
   :type valid_to: str, optional

.. py:class:: KeyValue

   Contains information about a specific configuration key.
   
   :param key: The configuration key
   :type key: str
   :param readonly: Whether this key is read-only
   :type readonly: bool
   :param value: The configuration value (optional)
   :type value: str, optional

.. py:class:: SampledValue

   Single sampled value in MeterValues.
   
   :param value: The sampled value
   :type value: str
   :param context: Context of the value (optional)
   :type context: enums.ReadingContext, optional
   :param format: Format of the value (optional)
   :type format: enums.ValueFormat, optional
   :param measurand: Type of measurand (optional)
   :type measurand: enums.Measurand, optional
   :param phase: Phase to which this value applies (optional)
   :type phase: enums.Phase, optional
   :param location: Location of the measurement (optional)
   :type location: enums.Location, optional
   :param unit: Unit of the value (optional)
   :type unit: enums.UnitOfMeasure, optional

.. py:class:: MeterValue

   Collection of sampled values taken at a point in time.
   
   :param timestamp: Timestamp of the samples
   :type timestamp: str
   :param sampled_value: List of sampled values
   :type sampled_value: list[SampledValue]

Security Extension Data Types
---------------------------

The following datatypes are part of the OCPP 1.6 Security Extension:

.. py:class:: CertificateHashData

   Hash data for a certificate.
   
   :param hash_algorithm: Algorithm used for hashing (from enums.HashAlgorithm)
   :type hash_algorithm: enums.HashAlgorithm
   :param issuer_name_hash: Hash of the issuer name
   :type issuer_name_hash: str
   :param issuer_key_hash: Hash of the issuer key
   :type issuer_key_hash: str
   :param serial_number: Serial number of the certificate
   :type serial_number: str

.. py:class:: Firmware

   Represents firmware that can be loaded on the Charge Point.
   
   :param location: Location of the firmware
   :type location: str
   :param retrieve_date_time: Date and time at which the firmware should be retrieved
   :type retrieve_date_time: str
   :param signing_certificate: Certificate used to sign the firmware
   :type signing_certificate: str
   :param install_date_time: Date and time at which the firmware should be installed (optional)
   :type install_date_time: str, optional
   :param signature: Signature of the firmware (optional)
   :type signature: str, optional

.. py:class:: LogParameters

   Parameters for retrieving logging entries.
   
   :param remote_location: Location to which logging should be uploaded
   :type remote_location: str
   :param oldest_timestamp: Oldest timestamp to include in the logging (optional)
   :type oldest_timestamp: str, optional
   :param latest_timestamp: Latest timestamp to include in the logging (optional)
   :type latest_timestamp: str, optional
