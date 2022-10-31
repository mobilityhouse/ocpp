from ocpp.v201.enums import ConnectorType, TxStartStopPointType


def test_connector_type():
    assert ConnectorType.c_ccs1 == "cCCS1"
    assert ConnectorType.c_ccs2 == "cCCS2"
    assert ConnectorType.c_chao_ji == "cChaoJi"
    assert ConnectorType.c_g105 == "cG105"
    assert ConnectorType.c_gbt == "cGBT"
    assert ConnectorType.c_tesla == "cTesla"
    assert ConnectorType.c_type1 == "cType1"
    assert ConnectorType.c_type2 == "cType2"
    assert ConnectorType.s309_1p_16a == "s309-1P-16A"
    assert ConnectorType.s309_1p_32a == "s309-1P-32A"
    assert ConnectorType.s309_3p_16a == "s309-3P-16A"
    assert ConnectorType.s309_3p_32a == "s309-3P-32A"
    assert ConnectorType.s_bs1361 == "sBS1361"
    assert ConnectorType.s_cee_7_7 == "sCEE-7-7"
    assert ConnectorType.s_type2 == "sType2"
    assert ConnectorType.s_type3 == "sType3"
    assert ConnectorType.opp_charge == "OppCharge"
    assert ConnectorType.other_1ph_max_16a == "Other1PhMax16A"
    assert ConnectorType.other_1ph_over_16a == "Other1PhOver16A"
    assert ConnectorType.other_3ph == "Other3Ph"
    assert ConnectorType.pan == "Pan"
    assert ConnectorType.w_inductive == "wInductive"
    assert ConnectorType.w_resonant == "wResonant"
    assert ConnectorType.undetermined == "Undetermined"
    assert ConnectorType.unknown == "Unknown"


def test_tx_start_stop_point():
    assert TxStartStopPointType.authorized == "Authorized"
    assert TxStartStopPointType.data_signed == "DataSigned"
    assert TxStartStopPointType.energy_transfer == "EnergyTransfer"
    assert TxStartStopPointType.ev_connected == "EVConnected"
    assert TxStartStopPointType.parking_bay_occupancy == "ParkingBayOccupancy"
    assert TxStartStopPointType.power_path_closed == "PowerPathClosed"
