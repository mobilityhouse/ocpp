from ocpp.v201.enums import ConnectorEnumType, DataEnumEnumType, TxStartStopPointEnumType


def test_connector_type():
    assert ConnectorEnumType.c_ccs1 == "cCCS1"
    assert ConnectorEnumType.c_ccs2 == "cCCS2"
    assert ConnectorEnumType.c_chao_ji == "cChaoJi"
    assert ConnectorEnumType.c_g105 == "cG105"
    assert ConnectorEnumType.c_gbt == "cGBT"
    assert ConnectorEnumType.c_tesla == "cTesla"
    assert ConnectorEnumType.c_type1 == "cType1"
    assert ConnectorEnumType.c_type2 == "cType2"
    assert ConnectorEnumType.s309_1p_16a == "s309-1P-16A"
    assert ConnectorEnumType.s309_1p_32a == "s309-1P-32A"
    assert ConnectorEnumType.s309_3p_16a == "s309-3P-16A"
    assert ConnectorEnumType.s309_3p_32a == "s309-3P-32A"
    assert ConnectorEnumType.s_bs1361 == "sBS1361"
    assert ConnectorEnumType.s_cee_7_7 == "sCEE-7-7"
    assert ConnectorEnumType.s_type2 == "sType2"
    assert ConnectorEnumType.s_type3 == "sType3"
    assert ConnectorEnumType.opp_charge == "OppCharge"
    assert ConnectorEnumType.other_1ph_max_16a == "Other1PhMax16A"
    assert ConnectorEnumType.other_1ph_over_16a == "Other1PhOver16A"
    assert ConnectorEnumType.other_3ph == "Other3Ph"
    assert ConnectorEnumType.pan == "Pan"
    assert ConnectorEnumType.w_inductive == "wInductive"
    assert ConnectorEnumType.w_resonant == "wResonant"
    assert ConnectorEnumType.undetermined == "Undetermined"
    assert ConnectorEnumType.unknown == "Unknown"


def test_data_type():
    assert DataEnumEnumType.string == "string"
    assert DataEnumEnumType.decimal == "decimal"
    assert DataEnumEnumType.integer == "integer"
    assert DataEnumEnumType.date_time == "dateTime"
    assert DataEnumEnumType.boolean == "boolean"
    assert DataEnumEnumType.option_list == "OptionList"
    assert DataEnumEnumType.sequence_list == "SequenceList"
    assert DataEnumEnumType.member_list == "MemberList"
    assert DataEnumEnumType.password_string == "passwordString"


def test_tx_start_stop_point():
    assert TxStartStopPointEnumType.authorized == "Authorized"
    assert TxStartStopPointEnumType.data_signed == "DataSigned"
    assert TxStartStopPointEnumType.energy_transfer == "EnergyTransfer"
    assert TxStartStopPointEnumType.ev_connected == "EVConnected"
    assert TxStartStopPointEnumType.parking_bay_occupancy == "ParkingBayOccupancy"
    assert TxStartStopPointEnumType.power_path_closed == "PowerPathClosed"
