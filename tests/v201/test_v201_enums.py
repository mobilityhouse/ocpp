from ocpp.v201.enums import TxStartStopPointType


def test_tx_start_stop_point():
    assert TxStartStopPointType.authorized == "Authorized"
    assert TxStartStopPointType.data_signed == "DataSigned"
    assert TxStartStopPointType.energy_transfer == "EnergyTransfer"
    assert TxStartStopPointType.ev_connected == "EVConnected"
    assert TxStartStopPointType.parking_bay_occupancy == "ParkingBayOccupancy"
    assert TxStartStopPointType.power_path_closed == "PowerPathClosed"
