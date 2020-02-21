# flake8: noqa
from ocpp.v16.enums import *


def test_authorization_status():
    assert AuthorizationStatus.accepted == "Accepted"
    assert AuthorizationStatus.blocked == "Blocked"
    assert AuthorizationStatus.expired == "Expired"
    assert AuthorizationStatus.invalid == "Invalid"
    assert AuthorizationStatus.concurrenttx == "ConcurrentTx"


def test_availability_status():
    assert AvailabilityStatus.accepted == "Accepted"
    assert AvailabilityStatus.rejected == "Rejected"
    assert AvailabilityStatus.scheduled == "Scheduled"


def test_availability_type():
    assert AvailabilityType.inoperative == "Inoperative"
    assert AvailabilityType.operative == "Operative"


def test_cancel_reservation_status():
    assert CancelReservationStatus.accepted == "Accepted"
    assert CancelReservationStatus.rejected == "Rejected"


def test_charge_point_error_code():
    assert (ChargePointErrorCode.connectorLockFailure ==
            "ConnectorLockFailure")
    assert (ChargePointErrorCode.evCommunicationError ==
            "EVCommunicationError")
    assert ChargePointErrorCode.groundFailure == "GroundFailure"
    assert (ChargePointErrorCode.highTemperature ==
            "HighTemperature")
    assert ChargePointErrorCode.internalError == "InternalError"
    assert (ChargePointErrorCode.localListConflict ==
            "LocalListConflict")
    assert ChargePointErrorCode.noError == "NoError"
    assert ChargePointErrorCode.otherError == "OtherError"
    assert (ChargePointErrorCode.overCurrentFailure ==
            "OverCurrentFailure")
    assert ChargePointErrorCode.overVoltage == "OverVoltage"
    assert (ChargePointErrorCode.powerMeterFailure ==
            "PowerMeterFailure")
    assert (ChargePointErrorCode.powerSwitchFailure ==
            "PowerSwitchFailure")
    assert ChargePointErrorCode.readerFailure == "ReaderFailure"
    assert ChargePointErrorCode.resetFailure == "ResetFailure"
    assert ChargePointErrorCode.underVoltage == "UnderVoltage"
    assert ChargePointErrorCode.weakSignal == "WeakSignal"


def test_charge_point_status():
    assert ChargePointStatus.available == 'Available'
    assert ChargePointStatus.preparing == 'Preparing'
    assert ChargePointStatus.charging == 'Charging'
    assert ChargePointStatus.suspendedevse == 'SuspendedEVSE'
    assert ChargePointStatus.suspendedev == 'SuspendedEV'
    assert ChargePointStatus.finishing == 'Finishing'
    assert ChargePointStatus.reserved == 'Reserved'
    assert ChargePointStatus.unavailable == 'Unavailable'
    assert ChargePointStatus.faulted == 'Faulted'


def test_charging_profile_kind_type():
    assert ChargingProfileKindType.absolute == 'Absolute'
    assert ChargingProfileKindType.recurring == 'Recurring'
    assert ChargingProfileKindType.relative == 'Relative'


def test_charging_profile_purpose_type():
    assert (ChargingProfilePurposeType.chargepointmaxprofile ==
            'ChargePointMaxProfile')
    assert (ChargingProfilePurposeType.txdefaultprofile ==
            'TxDefaultProfile')
    assert ChargingProfilePurposeType.txprofile == 'TxProfile'


def test_charging_profile_status():
    assert ChargingProfileStatus.accepted == "Accepted"
    assert ChargingProfileStatus.rejected == "Rejected"
    assert ChargingProfileStatus.notSupported == "NotSupported"


def test_charging_rate_unit():
    assert ChargingRateUnitType.watts == "W"
    assert ChargingRateUnitType.amps == "A"


def test_clear_cache_status():
    assert ClearCacheStatus.accepted == "Accepted"
    assert ClearCacheStatus.rejected == "Rejected"


def test_clear_charging_profile_status():
    assert ClearChargingProfileStatus.accepted == "Accepted"
    assert ClearChargingProfileStatus.unknown == "Unknown"


def test_configuration_status():
    assert ConfigurationStatus.accepted == "Accepted"
    assert ConfigurationStatus.rejected == "Rejected"
    assert ConfigurationStatus.rebootRequired == "RebootRequired"
    assert ConfigurationStatus.notSupported == "NotSupported"


def test_data_transfer_status():
    assert DataTransferStatus.accepted == "Accepted"
    assert DataTransferStatus.rejected == "Rejected"
    assert (DataTransferStatus.unknownMessageId ==
            "UnknownMessageId")
    assert DataTransferStatus.unknownVendorId == "UnknownVendorId"


def test_diagnostics_status():
    assert DiagnosticsStatus.idle == "Idle"
    assert DiagnosticsStatus.uploaded == "Uploaded"
    assert DiagnosticsStatus.uploadFailed == "UploadFailed"
    assert DiagnosticsStatus.uploading == "Uploading"


def test_firmware_status():
    assert FirmwareStatus.downloaded == "Downloaded"
    assert FirmwareStatus.downloadFailed == "DownloadFailed"
    assert FirmwareStatus.downloading == "Downloading"
    assert FirmwareStatus.idle == "Idle"
    assert (FirmwareStatus.installationFailed ==
            "InstallationFailed")
    assert FirmwareStatus.installing == "Installing"
    assert FirmwareStatus.installed == "Installed"


def test_get_composite_schedule_status():
    assert GetCompositeScheduleStatus.accepted == "Accepted"
    assert GetCompositeScheduleStatus.rejected == "Rejected"


def test_location():
    assert Location.inlet == "Inlet"
    assert Location.outlet == "Outlet"
    assert Location.body == "Body"
    assert Location.cable == "Cable"
    assert Location.ev == "EV"


def test_measurand():
    assert (Measurand.energyActiveExportRegister ==
            "Energy.Active.Export.Register")
    assert (Measurand.energyActiveImportRegister ==
            "Energy.Active.Import.Register")
    assert (Measurand.energyReactiveExportRegister ==
            "Energy.Reactive.Export.Register")
    assert (Measurand.energyReactiveImportRegister ==
            "Energy.Reactive.Import.Register")
    assert (Measurand.energyActiveExportInterval ==
            "Energy.Active.Export.Interval")
    assert (Measurand.energyActiveImportInterval ==
            "Energy.Active.Import.Interval")
    assert (Measurand.energyReactiveExportInterval ==
            "Energy.Reactive.Export.Interval")
    assert (Measurand.energyReactiveImportInterval ==
            "Energy.Reactive.Import.Interval")
    assert Measurand.frequency == "Frequency"
    assert Measurand.powerActiveExport == "Power.Active.Export"
    assert Measurand.powerActiveImport == "Power.Active.Import"
    assert Measurand.powerFactor == "Power.Factor"
    assert Measurand.powerOffered == "Power.Offered"
    assert (Measurand.powerReactiveExport ==
            "Power.Reactive.Export")
    assert (Measurand.powerReactiveImport ==
            "Power.Reactive.Import")
    assert Measurand.currentExport == "Current.Export"
    assert Measurand.currentImport == "Current.Import"
    assert Measurand.currentOffered == "Current.Offered"
    assert Measurand.rpm == "RPM"
    assert Measurand.soc == "SoC"
    assert Measurand.voltage == "Voltage"
    assert Measurand.temperature == "Temperature"


def test_message_trigger():
    assert MessageTrigger.bootNotification == "BootNotification"
    assert (MessageTrigger.diagnosticsStatusNotification ==
            "DiagnosticsStatusNotification")
    assert (MessageTrigger.firmwareStatusNotification ==
            "FirmwareStatusNotification")
    assert MessageTrigger.heartbeat == "Heartbeat"
    assert MessageTrigger.meterValues == "MeterValues"
    assert (MessageTrigger.statusNotification ==
            "StatusNotification")


def test_phase():
    assert Phase.l1 == "L1"
    assert Phase.l2 == "L2"
    assert Phase.l3 == "L3"
    assert Phase.n == "N"
    assert Phase.l1n == "L1-N"
    assert Phase.l2n == "L2-N"
    assert Phase.l3n == "L3-N"
    assert Phase.l1l2 == "L1-L2"
    assert Phase.l2l3 == "L2-L3"
    assert Phase.l3l1 == "L3-L1"


def test_reading_context():
    assert (ReadingContext.interruptionBegin ==
            "Interruption.Begin")
    assert ReadingContext.interruptionEnd == "Interruption.End"
    assert ReadingContext.other == "Other"
    assert ReadingContext.sampleClock == "Sample.Clock"
    assert ReadingContext.samplePeriodic == "Sample.Periodic"
    assert ReadingContext.transactionBegin == "Transaction.Begin"
    assert ReadingContext.transactionEnd == "Transaction.End"
    assert ReadingContext.trigger == "Trigger"


def test_reason():
    assert Reason.emergencyStop == "EmergencyStop"
    assert Reason.evDisconnected == "EVDisconnected"
    assert Reason.hardReset == "HardReset"
    assert Reason.local == "Local"
    assert Reason.other == "Other"
    assert Reason.powerLoss == "PowerLoss"
    assert Reason.reboot == "Reboot"
    assert Reason.remote == "Remote"
    assert Reason.softReset == "SoftReset"
    assert Reason.unlockCommand == "UnlockCommand"
    assert Reason.deAuthorized == "DeAuthorized"


def test_recurrency_kind():
    assert RecurrencyKind.daily == 'Daily'
    assert RecurrencyKind.weekly == 'Weekly'


def test_registration_status():
    assert RegistrationStatus.accepted == "Accepted"
    assert RegistrationStatus.pending == "Pending"
    assert RegistrationStatus.rejected == "Rejected"


def test_remote_start_stop_status():
    assert RemoteStartStopStatus.accepted == "Accepted"
    assert RemoteStartStopStatus.rejected == "Rejected"


def test_reservation_status():
    assert ReservationStatus.accepted == "Accepted"
    assert ReservationStatus.faulted == "Faulted"
    assert ReservationStatus.occupied == "Occupied"
    assert ReservationStatus.rejected == "Rejected"
    assert ReservationStatus.unavailable == "Unavailable"


def test_reset_status():
    assert ResetStatus.accepted == "Accepted"
    assert ResetStatus.rejected == "Rejected"


def test_reset_type():
    assert ResetType.hard == "Hard"
    assert ResetType.soft == "Soft"


def test_trigger_message_status():
    assert TriggerMessageStatus.accepted == "Accepted"
    assert TriggerMessageStatus.rejected == "Rejected"
    assert TriggerMessageStatus.notImplemented == "NotImplemented"


def test_unit_of_measure():
    assert UnitOfMeasure.wh == "Wh"
    assert UnitOfMeasure.kwh == "kWh"
    assert UnitOfMeasure.varh == "varh"
    assert UnitOfMeasure.kvarh == "kvarh"
    assert UnitOfMeasure.w == "W"
    assert UnitOfMeasure.kw == "kW"
    assert UnitOfMeasure.va == "VA"
    assert UnitOfMeasure.kva == "kVA"
    assert UnitOfMeasure.var == "var"
    assert UnitOfMeasure.kvar == "kvar"
    assert UnitOfMeasure.a == "A"
    assert UnitOfMeasure.v == "V"
    assert UnitOfMeasure.celsius == "Celsius"
    assert UnitOfMeasure.fahrenheit == "Fahrenheit"
    assert UnitOfMeasure.k == "K"
    assert UnitOfMeasure.percent == "Percent"
    assert UnitOfMeasure.hertz == "Hertz"


def test_unlock_status():
    assert UnlockStatus.unlocked == "Unlocked"
    assert UnlockStatus.unlockFailed == "UnlockFailed"
    assert UnlockStatus.notSupported == "NotSupported"


def test_update_status():
    assert UpdateStatus.accepted == "Accepted"
    assert UpdateStatus.failed == "Failed"
    assert UpdateStatus.notSupported == "NotSupported"
    assert UpdateStatus.versionMismatch == "VersionMismatch"


def test_update_type():
    assert UpdateType.differential == "Differential"
    assert UpdateType.full == "Full"


def test_value_format():
    assert ValueFormat.raw == "Raw"
    assert ValueFormat.signedData == "SignedData"
