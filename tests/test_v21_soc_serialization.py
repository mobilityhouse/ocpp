"""Regression tests for context-aware OCPP 2.1 soc/soh wire-key serialization."""

import asyncio
import json
from typing import Any, List, Optional

from ocpp.charge_point import (
    camel_to_snake_case,
    remove_nones,
    serialize_as_dict,
    snake_to_camel_case,
)
from ocpp.messages import MessageType, get_validator
from ocpp.v21 import ChargePoint
from ocpp.v21.call import (
    BatterySwap,
    NotifyEVChargingNeeds,
    SetChargingProfile,
)
from ocpp.v21.datatypes import (
    BatteryDataType,
    ChargingNeedsType,
    ChargingProfileType,
    ChargingSchedulePeriodType,
    ChargingScheduleType,
    CustomDataType,
    DCChargingParametersType,
    IdTokenType,
    LimitAtSoCType,
    TransactionLimitType,
    V2XChargingParametersType,
)
from ocpp.v21.enums import (
    BatterySwapEventEnumType,
    ChargingProfileKindEnumType,
    ChargingProfilePurposeEnumType,
    ChargingRateUnitEnumType,
    EnergyTransferModeEnumType,
)


class _InMemoryConnection:
    """In-memory connection that returns synthetic CallResult on send()."""

    def __init__(self, response_payload: dict[str, Any]) -> None:
        self.response_payload = response_payload
        self.sent_messages: List[str] = []
        self.charge_point: Optional[ChargePoint] = None

    async def send(self, message: str) -> None:
        self.sent_messages.append(message)
        frame = json.loads(message)
        unique_id = frame[1]
        assert self.charge_point is not None
        await self.charge_point.route_message(
            json.dumps([3, unique_id, self.response_payload])
        )


def test_batteryswap_charge_point_call_and_schema_validation() -> None:
    """G11-01: BatteryDataType.soc/soh serialize to soC/soH in ChargePoint.call()."""
    msg = BatterySwap(
        battery_data=[
            BatteryDataType(
                evse_id=1,
                serial_number="BATT-S0",
                soc=45.0,
                soh=95.0,
                custom_data=CustomDataType(vendor_id="VolMax"),
            )
        ],
        event_type=BatterySwapEventEnumType.battery_in,
        id_token=IdTokenType(id_token="TAG-S0", type="ISO14443"),
        request_id=101,
    )

    async def _run() -> List[str]:
        conn = _InMemoryConnection(response_payload={})
        cp = ChargePoint("cp-g11-01", conn)
        conn.charge_point = cp
        await cp.call(
            msg,
            suppress=False,
            unique_id="uid-bs-1",
            skip_schema_validation=False,
        )
        return conn.sent_messages

    sent = asyncio.run(_run())
    assert len(sent) == 1
    frame = json.loads(sent[0])
    assert frame[2] == "BatterySwap"
    payload = frame[3]
    assert payload["batteryData"][0] == {
        "evseId": 1,
        "serialNumber": "BATT-S0",
        "soC": 45.0,
        "soH": 95.0,
        "customData": {"vendorId": "VolMax"},
    }
    validator = get_validator(MessageType.Call, "BatterySwap", "2.1")
    assert list(validator.iter_errors(payload)) == []


def test_set_charging_profile_limit_at_soc_charge_point_call_and_schema() -> None:
    """G11-02: LimitAtSoCType.soc serializes to 'soc' and passes ChargePoint.call()."""
    msg = SetChargingProfile(
        evse_id=1,
        charging_profile=ChargingProfileType(
            id=1,
            stack_level=0,
            charging_profile_purpose=ChargingProfilePurposeEnumType.tx_profile,
            charging_profile_kind=ChargingProfileKindEnumType.absolute,
            charging_schedule=[
                ChargingScheduleType(
                    id=1,
                    charging_rate_unit=ChargingRateUnitEnumType.a,
                    charging_schedule_period=[
                        ChargingSchedulePeriodType(start_period=0, limit=16.0)
                    ],
                    limit_at_soc=LimitAtSoCType(limit=11.0, soc=80),
                )
            ],
        ),
    )

    async def _run() -> List[str]:
        conn = _InMemoryConnection(response_payload={"status": "Accepted"})
        cp = ChargePoint("cp-g11-02", conn)
        conn.charge_point = cp
        await cp.call(
            msg,
            suppress=False,
            unique_id="uid-scp-1",
            skip_schema_validation=False,
        )
        return conn.sent_messages

    sent = asyncio.run(_run())
    assert len(sent) == 1
    frame = json.loads(sent[0])
    assert frame[2] == "SetChargingProfile"
    payload = frame[3]
    assert payload["chargingProfile"]["chargingSchedule"][0]["limitAtSoC"] == {
        "limit": 11.0,
        "soc": 80,
    }
    validator = get_validator(MessageType.Call, "SetChargingProfile", "2.1")
    assert list(validator.iter_errors(payload)) == []


def test_standalone_dataclass_and_order_independence() -> None:
    """Both remove_nones/snake_to_camel_case orders work even without parent key."""
    battery = BatteryDataType(evse_id=1, serial_number="BATT-1", soc=45.0, soh=95.0)
    limit = LimitAtSoCType(limit=11.0, soc=80)

    expected_battery = {
        "evseId": 1,
        "serialNumber": "BATT-1",
        "soC": 45.0,
        "soH": 95.0,
    }
    expected_limit = {"limit": 11.0, "soc": 80}

    assert (
        remove_nones(snake_to_camel_case(serialize_as_dict(battery)))
        == expected_battery
    )
    assert (
        snake_to_camel_case(remove_nones(serialize_as_dict(battery)))
        == expected_battery
    )
    assert remove_nones(snake_to_camel_case(serialize_as_dict(limit))) == expected_limit
    assert snake_to_camel_case(remove_nones(serialize_as_dict(limit))) == expected_limit

    for action in (
        "SetChargingProfile",
        "NotifyEVChargingSchedule",
        "ReportChargingProfiles",
        "NotifyChargingLimit",
        "RequestStartTransaction",
    ):
        schema = get_validator(MessageType.Call, action, "2.1").schema
        limit_props = schema["definitions"]["LimitAtSoCType"]["properties"]
        assert "soc" in limit_props and "SoC" not in limit_props


def test_positive_control_existing_soc_conventions_preserved() -> None:
    """fullSoC, bulkSoC, maxSoC, targetSoC and E2E NotifyEVChargingNeeds still pass."""
    dc_params = DCChargingParametersType(
        ev_max_current=100.0,
        ev_max_voltage=400.0,
        full_soc=95,
        bulk_soc=80,
    )
    tx_limit = TransactionLimitType(max_soc=90)
    v2x_params = V2XChargingParametersType(target_soc=75)

    assert remove_nones(snake_to_camel_case(serialize_as_dict(dc_params))) == {
        "evMaxCurrent": 100.0,
        "evMaxVoltage": 400.0,
        "fullSoC": 95,
        "bulkSoC": 80,
    }
    assert remove_nones(snake_to_camel_case(serialize_as_dict(tx_limit))) == {
        "maxSoC": 90
    }
    assert remove_nones(snake_to_camel_case(serialize_as_dict(v2x_params))) == {
        "targetSoC": 75
    }

    msg = NotifyEVChargingNeeds(
        evse_id=1,
        charging_needs=ChargingNeedsType(
            requested_energy_transfer=EnergyTransferModeEnumType.dc,
            dc_charging_parameters=dc_params,
        ),
    )

    async def _run() -> List[str]:
        conn = _InMemoryConnection(response_payload={"status": "Accepted"})
        cp = ChargePoint("cp-g11-pos", conn)
        conn.charge_point = cp
        await cp.call(
            msg,
            suppress=False,
            unique_id="uid-necn-1",
            skip_schema_validation=False,
        )
        return conn.sent_messages

    sent = asyncio.run(_run())
    assert len(sent) == 1
    validator = get_validator(MessageType.Call, "NotifyEVChargingNeeds", "2.1")
    assert list(validator.iter_errors(json.loads(sent[0])[3])) == []


def test_inbound_camel_to_snake_compatibility() -> None:
    """Inbound camel_to_snake_case decodes both BatteryDataType and LimitAtSoCType."""
    assert camel_to_snake_case({"soC": 45.0, "soH": 95.0}) == {
        "soc": 45.0,
        "soh": 95.0,
    }
    assert camel_to_snake_case({"limit": 11.0, "soc": 80}) == {
        "limit": 11.0,
        "soc": 80,
    }
