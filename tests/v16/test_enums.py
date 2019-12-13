# flake8: noqa
from ocpp.v16.enums import *


def test_authorization_status():
    assert AuthorizationStatus.accepted.value == "Accepted"
    assert AuthorizationStatus.blocked.value == "Blocked"
    assert AuthorizationStatus.expired.value == "Expired"
    assert AuthorizationStatus.invalid.value == "Invalid"
    assert AuthorizationStatus.concurrenttx.value == "ConcurrentTx"


def test_availability_status():
    assert AvailabilityStatus.accepted.value == "Accepted"
    assert AvailabilityStatus.rejected.value == "Rejected"
    assert AvailabilityStatus.scheduled.value == "Scheduled"


def test_availability_type():
    assert AvailabilityType.inoperative.value == "Inoperative"
    assert AvailabilityType.operative.value == "Operative"


def test_cancel_reservation_status():
    assert CancelReservationStatus.accepted.value == "Accepted"
    assert CancelReservationStatus.rejected.value == "Rejected"


def test_charge_point_error_code():
    assert (ChargePointErrorCode.connectorLockFailure.value ==
            "ConnectorLockFailure")
    assert (ChargePointErrorCode.evCommunicationError.value ==
            "EVCommunicationError")
    assert ChargePointErrorCode.groundFailure.value == "GroundFailure"
    assert (ChargePointErrorCode.highTemperature.value ==
            "HighTemperature")
    assert ChargePointErrorCode.internalError.value == "InternalError"
    assert (ChargePointErrorCode.localListConflict.value ==
            "LocalListConflict")
    assert ChargePointErrorCode.noError.value == "NoError"
    assert ChargePointErrorCode.otherError.value == "OtherError"
    assert (ChargePointErrorCode.overCurrentFailure.value ==
            "OverCurrentFailure")
    assert ChargePointErrorCode.overVoltage.value == "OverVoltage"
    assert (ChargePointErrorCode.powerMeterFailure.value ==
            "PowerMeterFailure")
    assert (ChargePointErrorCode.powerSwitchFailure.value ==
            "PowerSwitchFailure")
    assert ChargePointErrorCode.readerFailure.value == "ReaderFailure"
    assert ChargePointErrorCode.resetFailure.value == "ResetFailure"
    assert ChargePointErrorCode.underVoltage.value == "UnderVoltage"
    assert ChargePointErrorCode.weakSignal.value == "WeakSignal"


def test_charge_point_status():
    assert ChargePointStatus.available.value == 'Available'
    assert ChargePointStatus.preparing.value == 'Preparing'
    assert ChargePointStatus.charging.value == 'Charging'
    assert ChargePointStatus.suspendedevse.value == 'SuspendedEVSE'
    assert ChargePointStatus.suspendedev.value == 'SuspendedEV'
    assert ChargePointStatus.finishing.value == 'Finishing'
    assert ChargePointStatus.reserved.value == 'Reserved'
    assert ChargePointStatus.unavailable.value == 'Unavailable'
    assert ChargePointStatus.faulted.value == 'Faulted'


def test_charging_profile_kind_type():
    assert ChargingProfileKindType.absolute.value == 'Absolute'
    assert ChargingProfileKindType.recurring.value == 'Recurring'
    assert ChargingProfileKindType.relative.value == 'Relative'


def test_charging_profile_purpose_type():
    assert (ChargingProfilePurposeType.chargepointmaxprofile.value ==
            'ChargePointMaxProfile')
    assert (ChargingProfilePurposeType.txdefaultprofile.value ==
            'TxDefaultProfile')
    assert ChargingProfilePurposeType.txprofile.value == 'TxProfile'


def test_charging_profile_status():
    assert ChargingProfileStatus.accepted.value == "Accepted"
    assert ChargingProfileStatus.rejected.value == "Rejected"
    assert ChargingProfileStatus.notSupported.value == "NotSupported"


def test_charging_rate_unit():
    assert ChargingRateUnitType.watts.value == "W"
    assert ChargingRateUnitType.amps.value == "A"


def test_clear_cache_status():
    assert ClearCacheStatus.accepted.value == "Accepted"
    assert ClearCacheStatus.rejected.value == "Rejected"


def test_clear_charging_profile_status():
    assert ClearChargingProfileStatus.accepted.value == "Accepted"
    assert ClearChargingProfileStatus.unknown.value == "Unknown"


def test_configuration_status():
    assert ConfigurationStatus.accepted.value == "Accepted"
    assert ConfigurationStatus.rejected.value == "Rejected"
    assert ConfigurationStatus.rebootRequired.value == "RebootRequired"
    assert ConfigurationStatus.notSupported.value == "NotSupported"


def test_data_transfer_status():
    assert DataTransferStatus.accepted.value == "Accepted"
    assert DataTransferStatus.rejected.value == "Rejected"
    assert (DataTransferStatus.unknownMessageId.value ==
            "UnknownMessageId")
    assert DataTransferStatus.unknownVendorId.value == "UnknownVendorId"


def test_diagnostics_status():
    assert DiagnosticsStatus.idle.value == "Idle"
    assert DiagnosticsStatus.uploaded.value == "Uploaded"
    assert DiagnosticsStatus.uploadFailed.value == "UploadFailed"
    assert DiagnosticsStatus.uploading.value == "Uploading"


def test_firmware_status():
    assert FirmwareStatus.downloaded.value == "Downloaded"
    assert FirmwareStatus.downloadFailed.value == "DownloadFailed"
    assert FirmwareStatus.downloading.value == "Downloading"
    assert FirmwareStatus.idle.value == "Idle"
    assert (FirmwareStatus.installationFailed.value ==
            "InstallationFailed")
    assert FirmwareStatus.installing.value == "Installing"
    assert FirmwareStatus.installed.value == "Installed"


def test_get_composite_schedule_status():
    assert GetCompositeScheduleStatus.accepted.value == "Accepted"
    assert GetCompositeScheduleStatus.rejected.value == "Rejected"


def test_location():
    assert Location.inlet.value == "Inlet"
    assert Location.outlet.value == "Outlet"
    assert Location.body.value == "Body"
    assert Location.cable.value == "Cable"
    assert Location.ev.value == "EV"


def test_measurand():
    assert (Measurand.energyActiveExportRegister.value ==
            "Energy.Active.Export.Register")
    assert (Measurand.energyActiveImportRegister.value ==
            "Energy.Active.Import.Register")
    assert (Measurand.energyReactiveExportRegister.value ==
            "Energy.Reactive.Export.Register")
    assert (Measurand.energyReactiveImportRegister.value ==
            "Energy.Reactive.Import.Register")
    assert (Measurand.energyActiveExportInterval.value ==
            "Energy.Active.Export.Interval")
    assert (Measurand.energyActiveImportInterval.value ==
            "Energy.Active.Import.Interval")
    assert (Measurand.energyReactiveExportInterval.value ==
            "Energy.Reactive.Export.Interval")
    assert (Measurand.energyReactiveImportInterval.value ==
            "Energy.Reactive.Import.Interval")
    assert Measurand.frequency.value == "Frequency"
    assert Measurand.powerActiveExport.value == "Power.Active.Export"
    assert Measurand.powerActiveImport.value == "Power.Active.Import"
    assert Measurand.powerFactor.value == "Power.Factor"
    assert Measurand.powerOffered.value == "Power.Offered"
    assert (Measurand.powerReactiveExport.value ==
            "Power.Reactive.Export")
    assert (Measurand.powerReactiveImport.value ==
            "Power.Reactive.Import")
    assert Measurand.currentExport.value == "Current.Export"
    assert Measurand.currentImport.value == "Current.Import"
    assert Measurand.currentOffered.value == "Current.Offered"
    assert Measurand.rpm.value == "RPM"
    assert Measurand.soc.value == "SoC"
    assert Measurand.voltage.value == "Voltage"
    assert Measurand.temperature.value == "Temperature"


def test_message_trigger():
    assert MessageTrigger.bootNotification.value == "BootNotification"
    assert (MessageTrigger.diagnosticsStatusNotification.value ==
            "DiagnosticsStatusNotification")
    assert (MessageTrigger.firmwareStatusNotification.value ==
            "FirmwareStatusNotification")
    assert MessageTrigger.heartbeat.value == "Heartbeat"
    assert MessageTrigger.meterValues.value == "MeterValues"
    assert (MessageTrigger.statusNotification.value ==
            "StatusNotification")


def test_phase():
    assert Phase.l1.value == "L1"
    assert Phase.l2.value == "L2"
    assert Phase.l3.value == "L3"
    assert Phase.n.value == "N"
    assert Phase.l1n.value == "L1-N"
    assert Phase.l2n.value == "L2-N"
    assert Phase.l3n.value == "L3-N"
    assert Phase.l1l2.value == "L1-L2"
    assert Phase.l2l3.value == "L2-L3"
    assert Phase.l3l1.value == "L3-L1"


def test_reading_context():
    assert (ReadingContext.interruptionBegin.value ==
            "Interruption.Begin")
    assert ReadingContext.interruptionEnd.value == "Interruption.End"
    assert ReadingContext.other.value == "Other"
    assert ReadingContext.sampleClock.value == "Sample.Clock"
    assert ReadingContext.samplePeriodic.value == "Sample.Periodic"
    assert ReadingContext.transactionBegin.value == "Transaction.Begin"
    assert ReadingContext.transactionEnd.value == "Transaction.End"
    assert ReadingContext.trigger.value == "Trigger"


def test_reason():
    assert Reason.emergencyStop.value == "EmergencyStop"
    assert Reason.evDisconnected.value == "EVDisconnected"
    assert Reason.hardReset.value == "HardReset"
    assert Reason.local.value == "Local"
    assert Reason.other.value == "Other"
    assert Reason.powerLoss.value == "PowerLoss"
    assert Reason.reboot.value == "Reboot"
    assert Reason.remote.value == "Remote"
    assert Reason.softReset.value == "SoftReset"
    assert Reason.unlockCommand.value == "UnlockCommand"
    assert Reason.deAuthorized.value == "DeAuthorized"


def test_recurrency_kind():
    assert RecurrencyKindType.daily.value == 'Daily'
    assert RecurrencyKindType.weekly.value == 'Weekly'


def test_registration_status():
    assert RegistrationStatus.accepted.value == "Accepted"
    assert RegistrationStatus.pending.value == "Pending"
    assert RegistrationStatus.rejected.value == "Rejected"


def test_remote_start_stop_status():
    assert RemoteStartStopStatus.accepted.value == "Accepted"
    assert RemoteStartStopStatus.rejected.value == "Rejected"


def test_reservation_status():
    assert ReservationStatus.accepted.value == "Accepted"
    assert ReservationStatus.faulted.value == "Faulted"
    assert ReservationStatus.occupied.value == "Occupied"
    assert ReservationStatus.rejected.value == "Rejected"
    assert ReservationStatus.unavailable.value == "Unavailable"


def test_reset_status():
    assert ResetStatus.accepted.value == "Accepted"
    assert ResetStatus.rejected.value == "Rejected"


def test_reset_type():
    assert ResetType.hard.value == "Hard"
    assert ResetType.soft.value == "Soft"


def test_trigger_message_status():
    assert TriggerMessageStatus.accepted.value == "Accepted"
    assert TriggerMessageStatus.rejected.value == "Rejected"
    assert TriggerMessageStatus.notImplemented.value == "NotImplemented"


def test_unit_of_measure():
    assert UnitOfMeasure.wh.value == "Wh"
    assert UnitOfMeasure.kwh.value == "kWh"
    assert UnitOfMeasure.varh.value == "varh"
    assert UnitOfMeasure.kvarh.value == "kvarh"
    assert UnitOfMeasure.w.value == "W"
    assert UnitOfMeasure.kw.value == "kW"
    assert UnitOfMeasure.va.value == "VA"
    assert UnitOfMeasure.kva.value == "kVA"
    assert UnitOfMeasure.var.value == "var"
    assert UnitOfMeasure.kvar.value == "kvar"
    assert UnitOfMeasure.a.value == "A"
    assert UnitOfMeasure.v.value == "V"
    assert UnitOfMeasure.celsius.value == "Celsius"
    assert UnitOfMeasure.fahrenheit.value == "Fahrenheit"
    assert UnitOfMeasure.k.value == "K"
    assert UnitOfMeasure.percent.value == "Percent"


def test_unlock_status():
    assert UnlockStatus.unlocked.value == "Unlocked"
    assert UnlockStatus.unlockFailed.value == "UnlockFailed"
    assert UnlockStatus.notSupported.value == "NotSupported"


def test_update_status():
    assert UpdateStatus.accepted.value == "Accepted"
    assert UpdateStatus.failed.value == "Failed"
    assert UpdateStatus.notSupported.value == "NotSupported"
    assert UpdateStatus.versionMismatch.value == "VersionMismatch"


def test_update_type():
    assert UpdateType.differential.value == "Differential"
    assert UpdateType.full.value == "Full"


def test_value_format():
    assert ValueFormat.raw.value == "Raw"
    assert ValueFormat.signedData.value == "SignedData"
