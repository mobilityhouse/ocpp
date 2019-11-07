import uuid
from datetime import datetime
from ocpp.v20.enums import (AttributeType,
                            ChargingRateUnitType,
                            ChargingProfilePurposeType,
                            ChargingProfileKindType
                            )


def remove_nones(dict_to_scan):
    dict_to_scan = {
        k: v for k, v in dict_to_scan.items()
        if v is not None
    }
    return dict_to_scan


def variables_list_creator(list_to_be_used, variable_component_name,
                           variable_name, variable_value,
                           attribute_type=AttributeType.actual.value,
                           evse_id=None, connector_id=0, append=True,
                           set_attribute_value=True):
    """
    This method is an helper to construct the nested dictionary necessary
    for SetVariablesRequest and GetVariablesRequest payloads.
    Args:
        list_to_be_used: List to which the variables will be appended
        variable_component_name: Component to which the variable belongs to
        variable_name: Variable Name
        variable_value: Variable Value
        attribute_type: Type of Value: Actual, Min/Max, Target
        evse_id: Id of the EVSE
        connector_id: Connector belonging to the EVSE id
        append: If it is false it cleans the list before it appends
        set_attribute_value: If get_variables_list must be used then this
        field must be set as False
    Returns:
    """
    # variable_component_name = "AuthCtrl"
    # variable_name = "Enabled"
    # variable_value = "True"
    evse_type = None
    if evse_id:
        evse_type = {'id': evse_id, 'connector_id': connector_id}
    component_type = {'name': variable_component_name,
                      'instance': None,
                      'evse': evse_type}
    component_type = remove_nones(component_type)
    variable_type = {'name': variable_name,
                     'instance': None}
    variable_type = remove_nones(variable_type)
    setvariable_datatype = {'attribute_type': attribute_type,
                            'component': component_type,
                            'variable': variable_type}
    if set_attribute_value is True:
        setvariable_datatype.update({'attribute_value': variable_value})
    # If it is not to append, then clean the list and append after
    if not append:
        list_to_be_used = []
    list_to_be_used.append(setvariable_datatype)

    return list_to_be_used


class ChargingSchedulePeriodConstructor:

    def __init__(self, startperiod, limit, numberphases=None,
                 phase_to_use=None):
        """

        Args:
            startperiod: Start of the period, in seconds from the start
            of schedule.
            limit: Power limit during the schedule period, expressed in
            Amperes or Watts.
            numberphases: The number of phases that can be used for charging.
            phasetouse: Values: 1..3, Used if numberPhases=1 and if the
            EVSE is capable of switching the phase connected to the EV, i.e.
            ACPhaseSwitchingSupported is defined and true. It’s not allowed
            unless both conditions above are true. If both conditions are true,
            and phaseToUse is omitted, the Charging Station / EVSE will make
            the selection on its own.
        """
        self.chargingscheduleperiod = {"startPeriod": startperiod,
                                       "limit": limit,
                                       "numberPhases": numberphases,
                                       "phaseToUse": phase_to_use}
        self.remove_none_items()

    def remove_none_items(self):
        self.chargingscheduleperiod = remove_nones(self.chargingscheduleperiod)

    @property
    def start_period(self):
        return self.chargingscheduleperiod['startPeriod']

    @start_period.setter
    def start_period(self, value=0):
        self.chargingscheduleperiod['startPeriod'] = value

    @property
    def power(self):
        return self.chargingscheduleperiod['limit']

    @power.setter
    def power(self, value):
        self.chargingscheduleperiod['limit'] = value

    @property
    def current(self):
        return self.chargingscheduleperiod['limit']

    @current.setter
    def current(self, value):
        self.chargingscheduleperiod['limit'] = value

    @property
    def number_phases(self):
        return self.chargingscheduleperiod['numberPhases']

    @number_phases.setter
    def number_phases(self, value=3):
        self.chargingscheduleperiod['numberPhases'] = value

    def __dict__(self):
        return self.chargingscheduleperiod


class ChargingScheduleConstructor:

    def __init__(self, chargingscheduleperiod, duration=None,
                 startschedule=None,
                 chargingrateunit=ChargingRateUnitType.watts.value,
                 minchargingrate=None):
        """

        Args:
            chargingscheduleperiod (ChargingSchedulePeriodConstructor):
            List of ChargingSchedulePeriod elements defining maximum power or
            current usage over time.
            duration (int): Duration of the charging schedule in seconds.
            If the duration is left empty, the last period will continue
            indefinitely
            startschedule (DateTime): Starting point of an absolute schedule.
            If absent the schedule will be relative to start of charging.
            chargingrateunit (ChargingRateUnitType): The unit of measure Limit
            is expressed in.
            minchargingrate (float): Minimum charging rate supported by
            the electric vehicle.
        """
        self.chargingscheduleperiodlist = [chargingscheduleperiod.__dict__()]
        self.chargingschedule = {
            "startSchedule": startschedule,
            "duration": duration,
            "chargingRateUnit": chargingrateunit,
            "minChargingRate": minchargingrate,
            "chargingSchedulePeriod": self.chargingscheduleperiodlist,
        }
        self.remove_none_items()

    def remove_none_items(self):
        self.chargingschedule = remove_nones(self.chargingschedule)

    @property
    def duration(self):
        return self.chargingschedule['duration']

    @duration.setter
    def duration(self, value=0):
        self.chargingschedule['duration'] = value

    @property
    def start_schedule(self):
        return self.chargingschedule['startSchedule']

    @start_schedule.setter
    def start_schedule(self, value=datetime.utcnow().isoformat()):
        self.chargingschedule['startSchedule'] = value

    @property
    def charging_unit(self):
        return self.chargingschedule['chargingRateUnit']

    @charging_unit.setter
    def charging_unit(self, value=ChargingRateUnitType.watts.value):
        self.chargingschedule['chargingRateUnit'] = value

    @property
    def min_charging_rate(self):
        return self.chargingschedule['minChargingRate']

    @min_charging_rate.setter
    def min_charging_rate(self, value=0.0):
        self.chargingschedule['minChargingRate'] = value

    def append_new_chargingscheduleperiod(self, chargingscheduleperiod):
        self.chargingscheduleperiodlist.append(
            chargingscheduleperiod.__dict__())
        self.chargingschedule[
            "chargingSchedulePeriod"] = self.chargingscheduleperiodlist

    def remove_last_chargingscheduleperiod(self):
        self.chargingscheduleperiodlist.pop()
        self.chargingschedule[
            "chargingSchedulePeriod"] = self.chargingscheduleperiodlist

    def __dict__(self):
        return self.chargingschedule


class ChargingProfileConstructor:
    def __init__(
            self, chargingschedule,
            chargingprofileid=uuid.uuid4().__int__(),
            primary=True, transactionid=None, stacklevel=0,
            chargingprofilepurpose=ChargingProfilePurposeType.txprofile.value,
            chargingprofilekind=ChargingProfileKindType.absolute.value,
            recurrencykind=None, validfrom=None, validto=None):

        """
        Args:
            chargingschedule(ChargingScheduleConstructor): Contains limits
            for the available power or current over time.
            chargingprofileid (int): Unique identifier for this profile.
            transactionid (int): Only valid if ChargingProfilePurpose is set
            to TxProfile
            stacklevel (int): Value determining level in hierarchy stack of
            profiles.
            chargingprofilepurpose (ChargingProfilePurpose): Defines the
            purpose of the schedule transferred by this message.
            chargingprofilekind (ChargingProfileKind): Indicates the kind of
            schedule.
            recurrencykind (RecurrencyKind): Indicates the start point of a
            recurrence.
            validfrom (DateTime): Not to be used when ChargingProfilePurpose
            is TxProfile.
            validto (DateTime): Not to be used when ChargingProfilePurpose
            is TxProfile.
        """

        self.chargingprofile = {
            "id": chargingprofileid,
            "stackLevel": stacklevel,
            "primary": primary,
            "chargingProfilePurpose": chargingprofilepurpose,
            "chargingProfileKind": chargingprofilekind,
            "recurrencyKind": recurrencykind,
            "validFrom": validfrom,
            "validTo": validto,
            "transactionId": transactionid,
            "chargingSchedule": chargingschedule.__dict__()
        }
        self.remove_none_items()

    def remove_none_items(self):
        # Removal of optional and not present fields
        self.chargingprofile = remove_nones(self.chargingprofile)

    @property
    def chargingprofileid(self):
        return self.chargingprofile['chargingProfileId']

    @chargingprofileid.setter
    def chargingprofileid(self, value=1):
        self.chargingprofile['chargingProfileId'] = value

    @property
    def transaction_id(self):
        return self.chargingprofile['transactionId']

    @transaction_id.setter
    def transaction_id(self, value=1):
        self.chargingprofile['transactionId'] = value

    @property
    def stacklevel(self):
        return self.chargingprofile['stackLevel']

    @stacklevel.setter
    def stacklevel(self, value=1):
        self.chargingprofile['stackLevel'] = value

    @property
    def profilepurpose(self):
        return self.chargingprofile['chargingProfilePurpose']

    @profilepurpose.setter
    def profilepurpose(self, value=ChargingProfilePurposeType.txprofile.value):
        self.chargingprofile['chargingProfilePurpose'] = value

    @property
    def profilekind(self):
        return self.chargingprofile['chargingProfileKind']

    @profilekind.setter
    def profilekind(self, value=ChargingProfileKindType.absolute.value):
        self.chargingprofile['chargingProfileKind'] = value

    @property
    def recurrencykind(self):
        return self.chargingprofile['recurrencyKind']

    @recurrencykind.setter
    def recurrencykind(self, value=None):
        self.chargingprofile['recurrencyKind'] = value

    @property
    def validfrom(self):
        return self.chargingprofile['validFrom']

    @validfrom.setter
    def validfrom(self, value=datetime.utcnow().isoformat()):
        self.chargingprofile['validFrom'] = value

    @property
    def validto(self):
        return self.chargingprofile['validTo']

    @validto.setter
    def validto(self, value=datetime.utcnow().isoformat()):
        self.chargingprofile['validTo'] = value

    @property
    def charging_schedule(self):
        return self.chargingprofile['chargingSchedule']

    @charging_schedule.setter
    def charging_schedule(self, value):
        self.chargingprofile['chargingSchedule'] = value.__dict__()

    def __dict__(self):
        return self.chargingprofile

