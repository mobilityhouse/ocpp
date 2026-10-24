from ocpp.v21.enums import (
    AlignedDataCtrlrVariableName,
    ConnectorEnumType,
    ControllerComponentName,
    EVSEVariableName,
    IdTokenEnumType,
)


def test_controller_component_name_includes_aligned_data_ctrlr():
    # Regression test for the exact gap reported in
    # https://github.com/mobilityhouse/ocpp/issues/774 -- AlignedDataCtrlr
    # (and its VariableName enum) exist in the OCPP 2.1 CSV appendices but
    # were missing from ocpp/v21/enums.py.
    assert ControllerComponentName.aligned_data_ctrlr == "AlignedDataCtrlr"
    assert AlignedDataCtrlrVariableName.available == "Available"
    assert AlignedDataCtrlrVariableName.enabled == "Enabled"
    assert AlignedDataCtrlrVariableName.interval == "Interval"


def test_evse_variable_name():
    assert EVSEVariableName.available == "Available"
    assert EVSEVariableName.ac_current == "ACCurrent"


def test_connector_enum_type():
    assert ConnectorEnumType.c_ccs1 == "cCCS1"
    assert ConnectorEnumType.c_type2 == "cType2"


def test_id_token_enum_type():
    assert IdTokenEnumType.central == "Central"
    assert IdTokenEnumType.iso14443 == "ISO14443"
