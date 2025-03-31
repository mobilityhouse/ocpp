from enum import Enum


class PaymentStatusEnum(str, Enum):
    """
    The status of the settlement attempt.
    """

    SETTLED = "Settled"
    CANCELED = "Canceled"
    REJECTED = "Rejected"
    FAILED = "Failed"


class HashAlgorithmEnum(str, Enum):
    """
    Used algorithms for the hashes provided.
    """

    SHA256 = "SHA256"
    SHA384 = "SHA384"
    SHA512 = "SHA512"


class AuthorizationStatusEnum(str, Enum):
    """
    Current status of the ID Token.
    """

    ACCEPTED = "Accepted"
    BLOCKED = "Blocked"
    CONCURRENT_TX = "ConcurrentTx"
    EXPIRED = "Expired"
    INVALID = "Invalid"
    NO_CREDIT = "NoCredit"
    NOT_ALLOWED_TYPE_EVSE = "NotAllowedTypeEVSE"
    NOT_AT_THIS_LOCATION = "NotAtThisLocation"
    NOT_AT_THIS_TIME = "NotAtThisTime"
    UNKNOWN = "Unknown"


class AuthorizeCertificateStatusEnum(str, Enum):
    """
    Certificate status information.
    - if all certificates are valid: return 'Accepted'.
    - if one of the certificates was revoked, return 'CertificateRevoked'.
    """

    ACCEPTED = "Accepted"
    SIGNATURE_ERROR = "SignatureError"
    CERTIFICATE_EXPIRED = "CertificateExpired"
    CERTIFICATE_REVOKED = "CertificateRevoked"
    NO_CERTIFICATE_AVAILABLE = "NoCertificateAvailable"
    CERT_CHAIN_ERROR = "CertChainError"
    CONTRACT_CANCELLED = "ContractCancelled"


class DayOfWeekEnum(str, Enum):
    """
    Days of the week.
    """

    MONDAY = "Monday"
    TUESDAY = "Tuesday"
    WEDNESDAY = "Wednesday"
    THURSDAY = "Thursday"
    FRIDAY = "Friday"
    SATURDAY = "Saturday"
    SUNDAY = "Sunday"


class EnergyTransferModeEnum(str, Enum):
    """
    Energy transfer modes.
    """

    AC_SINGLE_PHASE = "AC_single_phase"
    AC_TWO_PHASE = "AC_two_phase"
    AC_THREE_PHASE = "AC_three_phase"
    DC = "DC"
    AC_BPT = "AC_BPT"
    AC_BPT_DER = "AC_BPT_DER"
    AC_DER = "AC_DER"
    DC_BPT = "DC_BPT"
    DC_ACDP = "DC_ACDP"
    DC_ACDP_BPT = "DC_ACDP_BPT"
    WPT = "WPT"


class EvseKindEnum(str, Enum):
    """
    Type of EVSE (AC, DC) this tariff applies to.
    """

    AC = "AC"
    DC = "DC"


class MessageFormatEnum(str, Enum):
    """
    Format of the message.
    """

    ASCII = "ASCII"
    HTML = "HTML"
    URI = "URI"
    UTF8 = "UTF8"
    QRCODE = "QRCODE"


class BootReasonEnum(str, Enum):
    """
    This contains the reason for sending this message to the CSMS.
    """

    APPLICATION_RESET = "ApplicationReset"
    FIRMWARE_UPDATE = "FirmwareUpdate"
    LOCAL_RESET = "LocalReset"
    POWER_UP = "PowerUp"
    REMOTE_RESET = "RemoteReset"
    SCHEDULED_RESET = "ScheduledReset"
    TRIGGERED = "Triggered"
    UNKNOWN = "Unknown"
    WATCHDOG = "Watchdog"


class RegistrationStatusEnum(str, Enum):
    """
    This contains whether the Charging Station has been registered within the CSMS.
    """

    ACCEPTED = "Accepted"
    PENDING = "Pending"
    REJECTED = "Rejected"


class CancelReservationStatusEnum(str, Enum):
    """
    This indicates the success or failure of the canceling of a reservation by CSMS.
    """

    ACCEPTED = "Accepted"
    REJECTED = "Rejected"


class CertificateSigningUseEnum(str, Enum):
    """
    Indicates the type of the signed certificate that is returned. When omitted the certificate is used for both the 15118 connection (if implemented) and the Charging Station to CSMS connection.
    This field is required when a typeOfCertificate was included in the SignCertificateRequest that requested this certificate to be signed AND both the 15118 connection and the Charging Station connection are implemented.
    """

    CHARGING_STATION_CERTIFICATE = "ChargingStationCertificate"
    V2G_CERTIFICATE = "V2GCertificate"
    V2G20_CERTIFICATE = "V2G20Certificate"


class CertificateSignedStatusEnum(str, Enum):
    """
    Returns whether certificate signing has been accepted, otherwise rejected.
    """

    ACCEPTED = "Accepted"
    REJECTED = "Rejected"


class GenericStatusEnum(str, Enum):
    """
    Status of operation.
    """

    ACCEPTED = "Accepted"
    REJECTED = "Rejected"


class BatterySwapEventEnum(str, Enum):
    """
    Battery in/out event types.
    """

    BATTERY_IN = "BatteryIn"
    BATTERY_OUT = "BatteryOut"
    BATTERY_OUT_TIMEOUT = "BatteryOutTimeout"


class OperationalStatusEnum(str, Enum):
    """
    This contains the type of availability change that the Charging Station should perform.
    """

    INOPERATIVE = "Inoperative"
    OPERATIVE = "Operative"


class ChangeAvailabilityStatusEnum(str, Enum):
    """
    This indicates whether the Charging Station is able to perform the availability change.
    """

    ACCEPTED = "Accepted"
    REJECTED = "Rejected"
    SCHEDULED = "Scheduled"


class TariffChangeStatusEnum(str, Enum):
    """
    Status of the operation.
    """

    ACCEPTED = "Accepted"
    REJECTED = "Rejected"
    TOO_MANY_ELEMENTS = "TooManyElements"
    CONDITION_NOT_SUPPORTED = "ConditionNotSupported"
    TX_NOT_FOUND = "TxNotFound"
    NO_CURRENCY_CHANGE = "NoCurrencyChange"


class ClearCacheStatusEnum(str, Enum):
    """
    Accepted if the Charging Station has executed the request, otherwise rejected.
    """

    ACCEPTED = "Accepted"
    REJECTED = "Rejected"


class ClearMessageStatusEnum(str, Enum):
    """
    Returns whether the Charging Station has been able to remove the message.
    """

    ACCEPTED = "Accepted"
    UNKNOWN = "Unknown"
    REJECTED = "Rejected"


class ChargingProfilePurposeEnum(str, Enum):
    """
    Specifies to purpose of the charging profiles that will be cleared, if they meet the other criteria in the request.
    """

    CHARGING_STATION_EXTERNAL_CONSTRAINTS = "ChargingStationExternalConstraints"
    CHARGING_STATION_MAX_PROFILE = "ChargingStationMaxProfile"
    TX_DEFAULT_PROFILE = "TxDefaultProfile"
    TX_PROFILE = "TxProfile"
    PRIORITY_CHARGING = "PriorityCharging"
    LOCAL_GENERATION = "LocalGeneration"


class ClearChargingProfileStatusEnum(str, Enum):
    """
    Indicates if the Charging Station was able to execute the request.
    """

    ACCEPTED = "Accepted"
    UNKNOWN = "Unknown"


class DERControlEnum(str, Enum):
    """
    Name of control settings to clear. Not used when controlId is provided.
    """

    ENTER_SERVICE = "EnterService"
    FREQ_DROOP = "FreqDroop"
    FREQ_WATT = "FreqWatt"
    FIXED_PF_ABSORB = "FixedPFAbsorb"
    FIXED_PF_INJECT = "FixedPFInject"
    FIXED_VAR = "FixedVar"
    GRADIENTS = "Gradients"
    HF_MUST_TRIP = "HFMustTrip"
    HF_MAY_TRIP = "HFMayTrip"
    HV_MUST_TRIP = "HVMustTrip"
    HV_MOM_CESS = "HVMomCess"
    HV_MAY_TRIP = "HVMayTrip"
    LIMIT_MAX_DISCHARGE = "LimitMaxDischarge"
    LF_MUST_TRIP = "LFMustTrip"
    LV_MUST_TRIP = "LVMustTrip"
    LV_MOM_CESS = "LVMomCess"
    LV_MAY_TRIP = "LVMayTrip"
    POWER_MONITORING_MUST_TRIP = "PowerMonitoringMustTrip"
    VOLT_VAR = "VoltVar"
    VOLT_WATT = "VoltWatt"
    WATT_PF = "WattPF"
    WATT_VAR = "WattVar"


class DERControlStatusEnum(str, Enum):
    """
    Result of operation.
    """

    ACCEPTED = "Accepted"
    REJECTED = "Rejected"
    NOT_SUPPORTED = "NotSupported"
    NOT_FOUND = "NotFound"


class ChargingLimitSourceEnum(str, Enum):
    """
    Source of the charging limit.
    """

    EMS = "EMS"
    OTHER = "Other"
    SO = "SO"
    CSO = "CSO"


class TariffClearStatusEnum(str, Enum):
    """
    Status of clearing tariffs.
    """

    ACCEPTED = "Accepted"
    REJECTED = "Rejected"
    NO_TARIFF = "NoTariff"


class ClearMonitoringStatusEnum(str, Enum):
    """
    Result of the clear request for this monitor, identified by its Id.
    """

    ACCEPTED = "Accepted"
    REJECTED = "Rejected"
    NOT_FOUND = "NotFound"


class CustomerInformationStatusEnum(str, Enum):
    """
    Indicates whether the customer information request was accepted.
    """

    ACCEPTED = "Accepted"
    REJECTED = "Rejected"
    INVALID = "Invalid"


class DataTransferStatusEnum(str, Enum):
    """
    This indicates the success or failure of the data transfer.
    """

    ACCEPTED = "Accepted"
    REJECTED = "Rejected"
    UNKNOWN_MESSAGE_ID = "UnknownMessageId"
    UNKNOWN_VENDOR_ID = "UnknownVendorId"


class DeleteCertificateStatusEnum(str, Enum):
    """
    Charging Station indicates if it can process the certificate deletion request.
    """

    accepted = "Accepted"
    failed = "Failed"
    not_found = "NotFound"


class FirmwareStatusEnum(str, Enum):
    """
    This contains the progress status of the firmware installation.
    """

    DOWNLOADED = "Downloaded"
    DOWNLOAD_FAILED = "DownloadFailed"
    DOWNLOADING = "Downloading"
    DOWNLOAD_SCHEDULED = "DownloadScheduled"
    DOWNLOAD_PAUSED = "DownloadPaused"
    IDLE = "Idle"
    INSTALLATION_FAILED = "InstallationFailed"
    INSTALLING = "Installing"
    INSTALLED = "Installed"
    INSTALL_REBOOTING = "InstallRebooting"
    INSTALL_SCHEDULED = "InstallScheduled"
    INSTALL_VERIFICATION_FAILED = "InstallVerificationFailed"
    INVALID_SIGNATURE = "InvalidSignature"
    SIGNATURE_VERIFIED = "SignatureVerified"


class CertificateActionEnum(str, Enum):
    """
    Defines whether certificate needs to be installed or updated.
    """

    INSTALL = "Install"
    UPDATE = "Update"


class Iso15118EVCertificateStatusEnum(str, Enum):
    """
    Indicates whether the message was processed properly.
    """

    ACCEPTED = "Accepted"
    FAILED = "Failed"


class ReportBaseEnum(str, Enum):
    """
    This field specifies the report base.
    """

    CONFIGURATION_INVENTORY = "ConfigurationInventory"
    FULL_INVENTORY = "FullInventory"
    SUMMARY_INVENTORY = "SummaryInventory"


class GenericDeviceModelStatusEnum(str, Enum):
    """
    This indicates whether the Charging Station is able to accept this request.
    """

    ACCEPTED = "Accepted"
    REJECTED = "Rejected"
    NOT_SUPPORTED = "NotSupported"
    EMPTY_RESULT_SET = "EmptyResultSet"


class CertificateStatusSourceEnum(str, Enum):
    """
    Source of status: OCSP, CRL
    """

    CRL = "CRL"
    OCSP = "OCSP"


class CertificateStatusEnum(str, Enum):
    """
    Status of certificate: good, revoked or unknown.
    """

    GOOD = "Good"
    REVOKED = "Revoked"
    UNKNOWN = "Unknown"
    FAILED = "Failed"


class GetCertificateStatusEnum(str, Enum):
    """
    This indicates whether the charging station was able to retrieve the OCSP certificate status.
    """

    ACCEPTED = "Accepted"
    FAILED = "Failed"


class GetChargingProfileStatusEnum(str, Enum):
    """
    This indicates whether the Charging Station is able to process this request and will send ReportChargingProfilesRequest messages.
    """

    ACCEPTED = "Accepted"
    NO_PROFILES = "NoProfiles"


class ChargingRateUnitEnum(str, Enum):
    """
    Can be used to force a power or current profile.
    """

    W = "W"
    A = "A"


class OperationModeEnum(str, Enum):
    """
    Charging operation mode to use during this time interval.
    When absent defaults to 'ChargingOnly'.
    """

    IDLE = "Idle"
    CHARGING_ONLY = "ChargingOnly"
    CENTRAL_SETPOINT = "CentralSetpoint"
    EXTERNAL_SETPOINT = "ExternalSetpoint"
    EXTERNAL_LIMITS = "ExternalLimits"
    CENTRAL_FREQUENCY = "CentralFrequency"
    LOCAL_FREQUENCY = "LocalFrequency"
    LOCAL_LOAD_BALANCING = "LocalLoadBalancing"


class GetCertificateIdUseEnum(str, Enum):
    """
    Indicates the type of the requested certificate(s).
    """

    V2G_ROOT_CERTIFICATE = "V2GRootCertificate"
    MO_ROOT_CERTIFICATE = "MORootCertificate"
    CSMS_ROOT_CERTIFICATE = "CSMSRootCertificate"
    V2G_CERTIFICATE_CHAIN = "V2GCertificateChain"
    MANUFACTURER_ROOT_CERTIFICATE = "ManufacturerRootCertificate"
    OEM_ROOT_CERTIFICATE = "OEMRootCertificate"


class GetInstalledCertificateStatusEnum(str, Enum):
    """
    Charging Station indicates if it can process the request.
    """

    ACCEPTED = "Accepted"
    NOT_FOUND = "NotFound"


class MessagePriorityEnum(str, Enum):
    """
    Priority of a message.
    """

    ALWAYS_FRONT = "AlwaysFront"
    IN_FRONT = "InFront"
    NORMAL_CYCLE = "NormalCycle"


class MessageStateEnum(str, Enum):
    """
    States for a message.
    """

    CHARGING = "Charging"
    FAULTED = "Faulted"
    IDLE = "Idle"
    UNAVAILABLE = "Unavailable"
    SUSPENDED = "Suspended"
    DISCHARGING = "Discharging"


class GetDisplayMessagesStatusEnum(str, Enum):
    """
    Indicates if the Charging Station has Display Messages that match the request criteria.
    """

    ACCEPTED = "Accepted"
    UNKNOWN = "Unknown"


class LogEnumType(str, Enum):
    """
    This contains the type of log file that the Charging Station should send.
    """

    DIAGNOSTICS_LOG = "DiagnosticsLog"
    SECURITY_LOG = "SecurityLog"
    DATA_COLLECTOR_LOG = "DataCollectorLog"


class LogStatusEnumType(str, Enum):
    """
    This field indicates whether the Charging Station was able to accept the request.
    """

    ACCEPTED = "Accepted"
    REJECTED = "Rejected"
    ACCEPTED_CANCELED = "AcceptedCanceled"


class MonitoringCriterionEnum(str, Enum):
    """
    Criteria for components for which a monitoring report is requested.
    """

    THRESHOLD_MONITORING = "ThresholdMonitoring"
    DELTA_MONITORING = "DeltaMonitoring"
    PERIODIC_MONITORING = "PeriodicMonitoring"


class ComponentCriterionEnum(str, Enum):
    """
    This field contains criteria for components for which a report is requested.
    """

    ACTIVE = "Active"
    AVAILABLE = "Available"
    ENABLED = "Enabled"
    PROBLEM = "Problem"
