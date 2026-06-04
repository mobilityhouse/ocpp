import json
from dataclasses import asdict, dataclass
from typing import TypeVar

from ocpp.v16.call import RemoteStartTransaction
from ocpp.v16.datatypes import ChargingProfile, ChargingSchedule, ChargingSchedulePeriod
from ocpp.v16.enums import (
    ChargingProfileKindType,
    ChargingProfilePurposeType,
    ChargingRateUnitType,
    RecurrencyKind,
)

T = TypeVar("T", bound="dataclass")


def to_datatype(cls, dc: T):
    to_dict = asdict(dc)
    to_json = json.dumps(to_dict)
    from_json = json.loads(to_json)
    return cls(**from_json)


def test_remote_start_transaction_as_dict():
    cp: T = ChargingProfile(
        charging_profile_id=1,
        stack_level=1,
        charging_profile_purpose=ChargingProfilePurposeType.charge_point_max_profile,
        charging_profile_kind=ChargingProfileKindType.absolute,
        charging_schedule=ChargingSchedule(
            charging_rate_unit=ChargingRateUnitType.watts,
            charging_schedule_period=[
                ChargingSchedulePeriod(start_period=0, limit=10, number_phases=3)
            ],
        ),
        transaction_id=1,
        recurrency_kind=RecurrencyKind.daily,
        valid_from="2021-01-01T00:00:00Z",
        valid_to="2021-01-02T00:00:00Z",
    )

    cp_dict = asdict(cp)

    rst = RemoteStartTransaction(
        id_tag="12345", connector_id=1, charging_profile=cp_dict
    )

    new_rst = to_datatype(RemoteStartTransaction, rst)

    # Verify top level attributes
    assert rst.id_tag == new_rst.id_tag
    assert rst.connector_id == new_rst.connector_id

    # Verify ChargingProfile attributes
    charging_profile = rst.charging_profile
    new_charging_profile = new_rst.charging_profile
    assert (
        charging_profile["charging_profile_id"]
        == new_charging_profile["charging_profile_id"]
    )
    assert charging_profile["stack_level"] == new_charging_profile["stack_level"]
    assert (
        charging_profile["charging_profile_purpose"]
        == new_charging_profile["charging_profile_purpose"]
    )
    assert (
        charging_profile["charging_profile_kind"]
        == new_charging_profile["charging_profile_kind"]
    )
    assert charging_profile["transaction_id"] == new_charging_profile["transaction_id"]
    assert (
        charging_profile["recurrency_kind"] == new_charging_profile["recurrency_kind"]
    )
    assert charging_profile["valid_from"] == new_charging_profile["valid_from"]
    assert charging_profile["valid_to"] == new_charging_profile["valid_to"]

    # Verify ChargingSchedule attributes
    charging_schedule = charging_profile["charging_schedule"]
    new_charging_schedule = new_charging_profile["charging_schedule"]
    assert (
        charging_schedule["charging_rate_unit"]
        == new_charging_schedule["charging_rate_unit"]
    )

    # Verify ChargingSchedulePeriod attributes
    charging_period = charging_schedule["charging_schedule_period"][0]
    new_charging_period = new_charging_schedule["charging_schedule_period"][0]
    assert charging_period["start_period"] == new_charging_period["start_period"]
    assert charging_period["limit"] == new_charging_period["limit"]
    assert charging_period["number_phases"] == new_charging_period["number_phases"]


def test_remote_start_transaction_as_class():
    cp: T = ChargingProfile(
        charging_profile_id=1,
        stack_level=1,
        charging_profile_purpose=ChargingProfilePurposeType.charge_point_max_profile,
        charging_profile_kind=ChargingProfileKindType.absolute,
        charging_schedule=ChargingSchedule(
            charging_rate_unit=ChargingRateUnitType.watts,
            charging_schedule_period=[
                ChargingSchedulePeriod(start_period=0, limit=10, number_phases=3)
            ],
        ),
        transaction_id=1,
        recurrency_kind=RecurrencyKind.daily,
        valid_from="2021-01-01T00:00:00Z",
        valid_to="2021-01-02T00:00:00Z",
    )

    rst = RemoteStartTransaction(id_tag="12345", connector_id=1, charging_profile=cp)

    new_rst = to_datatype(RemoteStartTransaction, rst)

    # Verify top level attributes
    assert rst.id_tag == new_rst.id_tag
    assert rst.connector_id == new_rst.connector_id

    # Verify ChargingProfile attributes
    charging_profile = rst.charging_profile
    new_charging_profile = new_rst.charging_profile
    assert (
        charging_profile.charging_profile_id
        == new_charging_profile["charging_profile_id"]
    )
    assert charging_profile.stack_level == new_charging_profile["stack_level"]
    assert (
        charging_profile.charging_profile_purpose
        == new_charging_profile["charging_profile_purpose"]
    )
    assert (
        charging_profile.charging_profile_kind
        == new_charging_profile["charging_profile_kind"]
    )
    assert charging_profile.transaction_id == new_charging_profile["transaction_id"]
    assert charging_profile.recurrency_kind == new_charging_profile["recurrency_kind"]
    assert charging_profile.valid_from == new_charging_profile["valid_from"]
    assert charging_profile.valid_to == new_charging_profile["valid_to"]

    # Verify ChargingSchedule attributes
    charging_schedule = charging_profile.charging_schedule
    new_charging_schedule = new_charging_profile["charging_schedule"]
    assert (
        charging_schedule.charging_rate_unit
        == new_charging_schedule["charging_rate_unit"]
    )

    # Verify ChargingSchedulePeriod attributes
    charging_period = charging_schedule.charging_schedule_period[0]
    new_charging_period = new_charging_schedule["charging_schedule_period"][0]
    assert charging_period.start_period == new_charging_period["start_period"]
    assert charging_period.limit == new_charging_period["limit"]
    assert charging_period.number_phases == new_charging_period["number_phases"]
