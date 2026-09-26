"""Nested v201 datatypes carry custom_data through serialize_as_dict + snake_to_camel_case."""

from ocpp.charge_point import serialize_as_dict, snake_to_camel_case
from ocpp.v201 import datatypes


def test_evse_type_custom_data_serializes_to_custom_data_vendor_id():
    evse = datatypes.EVSEType(
        id=1,
        connector_id=2,
        custom_data={"vendor_id": "ACME"},
    )
    payload = snake_to_camel_case(serialize_as_dict(evse))
    assert payload == {
        "id": 1,
        "connectorId": 2,
        "customData": {"vendorId": "ACME"},
    }


def test_nested_charging_station_custom_data_on_modem():
    station = datatypes.ChargingStationType(
        vendor_name="V",
        model="M",
        modem=datatypes.ModemType(
            iccid="1",
            imsi=None,
            custom_data={"vendor_id": "ModemVendor"},
        ),
        custom_data={"vendor_id": "StationVendor"},
    )
    payload = snake_to_camel_case(serialize_as_dict(station))
    assert payload["customData"] == {"vendorId": "StationVendor"}
    assert payload["modem"]["customData"] == {"vendorId": "ModemVendor"}
