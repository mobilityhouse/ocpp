import json
from dataclasses import asdict, dataclass
from typing import TypeVar

from ocpp.v201.datatypes import (
    ACChargingParametersType,
    AdditionalInfoType,
    APNType,
    AuthorizationData,
    CertificateHashDataChainType,
    CertificateHashDataType,
    ChargingLimitType,
    ChargingNeedsType,
    ChargingProfileCriterionType,
    ChargingProfileType,
    ChargingSchedulePeriodType,
    ChargingScheduleType,
    ChargingStationType,
    ClearChargingProfileType,
    ClearMonitoringResultType,
    ComponentType,
    ComponentVariableType,
    CompositeScheduleType,
    ConsumptionCostType,
    CostType,
    DCChargingParametersType,
    EventDataType,
    EVSEType,
    FirmwareType,
    GetVariableDataType,
    GetVariableResultType,
    IdTokenInfoType,
    IdTokenType,
    LogParametersType,
    MessageContentType,
    MessageInfoType,
    MeterValueType,
    ModemType,
    MonitoringDataType,
    NetworkConnectionProfileType,
    OCSPRequestDataType,
    RelativeTimeIntervalType,
    ReportDataType,
    SalesTariffEntryType,
    SampledValueType,
    SetMonitoringDataType,
    SetMonitoringResultType,
    SetVariableResultType,
    StatusInfoType,
    UnitOfMeasureType,
    VariableAttributeType,
    VariableCharacteristicsType,
    VariableMonitoringType,
    VariableType,
)
from ocpp.v201.enums import (
    APNAuthenticationEnumType,
    AttributeEnumType,
    AuthorizationStatusEnumType,
    ChargingProfileKindEnumType,
    ChargingProfilePurposeEnumType,
    ChargingRateUnitEnumType,
    ChargingStateEnumType,
    ClearMonitoringStatusEnumType,
    CostKindEnumType,
    DataEnumType,
    EnergyTransferModeEnumType,
    EventNotificationEnumType,
    EventTriggerEnumType,
    HashAlgorithmEnumType,
    IdTokenEnumType,
    LocationEnumType,
    MeasurandEnumType,
    MessageFormatEnumType,
    MonitorEnumType,
    MutabilityEnumType,
    OCPPInterfaceEnumType,
    OCPPTransportEnumType,
    OCPPVersionEnumType,
    PhaseEnumType,
    ReadingContextEnumType,
    ReasonEnumType,
    SetMonitoringStatusEnumType,
    SetVariableStatusEnumType,
    StandardizedUnitsOfMeasureEnumType,
    VPNType,
)

T = TypeVar("T", bound="dataclass")


def to_datatype(cls, dc: T):
    to_dict = asdict(dc)
    to_json = json.dumps(to_dict)
    from_json = json.loads(to_json)
    return cls(**from_json)


def test_ac_charging_parameters_type():
    acpt = ACChargingParametersType(
        energy_amount=20.5, ev_min_current=10.0, ev_max_current=32.0, ev_max_voltage=400
    )

    new_acpt = to_datatype(ACChargingParametersType, acpt)

    assert new_acpt.energy_amount == acpt.energy_amount
    assert new_acpt.ev_min_current == acpt.ev_min_current
    assert new_acpt.ev_max_current == acpt.ev_max_current
    assert new_acpt.ev_max_voltage == acpt.ev_max_voltage


def test_additional_info_type():
    ait = AdditionalInfoType(
        additional_id_token="additional_token123", type="type_value"
    )

    new_ait = to_datatype(AdditionalInfoType, ait)

    assert new_ait.additional_id_token == ait.additional_id_token
    assert new_ait.type == ait.type


def test_apn_type():
    at = APNType(
        apn="internet.example.com",
        apn_authentication=APNAuthenticationEnumType.auto,
        apn_user_name="username",
        apn_password="password",
        sim_pin=1234,
        preferred_network="preferred",
        use_only_preferred_network=True,
    )

    new_at = to_datatype(APNType, at)

    assert new_at.apn == at.apn
    assert new_at.apn_authentication == at.apn_authentication
    assert new_at.apn_user_name == at.apn_user_name
    assert new_at.apn_password == at.apn_password
    assert new_at.sim_pin == at.sim_pin
    assert new_at.preferred_network == at.preferred_network
    assert new_at.use_only_preferred_network == at.use_only_preferred_network


def test_authorization_data():
    ad = AuthorizationData(
        id_token_info=IdTokenInfoType(
            status=AuthorizationStatusEnumType.accepted,
            cache_expiry_date_time="2024-01-01T10:00:00Z",
            charging_priority=1,
            language_1="en",
            language_2="fr",
            group_id_token=IdTokenType(
                type=IdTokenEnumType.central,
                id_token="1234567890",
            ),
        ),
        id_token=IdTokenEnumType.central,
    )

    new_ad = to_datatype(AuthorizationData, ad)

    assert isinstance(new_ad.id_token_info, dict)
    assert new_ad.id_token_info["status"] == ad.id_token_info.status
    assert (
        new_ad.id_token_info["cache_expiry_date_time"]
        == ad.id_token_info.cache_expiry_date_time
    )
    assert (
        new_ad.id_token_info["charging_priority"] == ad.id_token_info.charging_priority
    )
    assert new_ad.id_token_info["language_1"] == ad.id_token_info.language_1
    assert new_ad.id_token_info["language_2"] == ad.id_token_info.language_2
    assert isinstance(new_ad.id_token, str)
    assert new_ad.id_token == ad.id_token


def test_certificate_hash_data_chain_type():
    chdct = CertificateHashDataChainType(
        certificate_type="V2G",
        certificate_hash_data=CertificateHashDataType(
            hash_algorithm="SHA256",
            issuer_name_hash="issuer_hash",
            issuer_key_hash="key_hash",
            serial_number="serial123",
        ),
        child_certificate_hash_data=[
            CertificateHashDataType(
                hash_algorithm="SHA256",
                issuer_name_hash="child_issuer_hash",
                issuer_key_hash="child_key_hash",
                serial_number="child_serial123",
            )
        ],
    )

    new_chdct = to_datatype(CertificateHashDataChainType, chdct)

    assert new_chdct.certificate_type == chdct.certificate_type
    assert isinstance(new_chdct.certificate_hash_data, dict)
    assert (
        new_chdct.certificate_hash_data["hash_algorithm"]
        == chdct.certificate_hash_data.hash_algorithm
    )
    assert (
        new_chdct.certificate_hash_data["issuer_name_hash"]
        == chdct.certificate_hash_data.issuer_name_hash
    )
    assert (
        new_chdct.certificate_hash_data["issuer_key_hash"]
        == chdct.certificate_hash_data.issuer_key_hash
    )
    assert (
        new_chdct.certificate_hash_data["serial_number"]
        == chdct.certificate_hash_data.serial_number
    )
    assert isinstance(new_chdct.child_certificate_hash_data[0], dict)
    assert (
        new_chdct.child_certificate_hash_data[0]["hash_algorithm"]
        == chdct.child_certificate_hash_data[0].hash_algorithm
    )


def test_certificate_hash_data_type():
    chdt = CertificateHashDataType(
        hash_algorithm="SHA256",
        issuer_name_hash="issuer_hash",
        issuer_key_hash="key_hash",
        serial_number="serial123",
    )

    new_chdt = to_datatype(CertificateHashDataType, chdt)

    assert new_chdt.hash_algorithm == chdt.hash_algorithm
    assert new_chdt.issuer_name_hash == chdt.issuer_name_hash
    assert new_chdt.issuer_key_hash == chdt.issuer_key_hash
    assert new_chdt.serial_number == chdt.serial_number


def test_charging_limit_type():
    clt = ChargingLimitType(charging_limit_source="EMS", is_grid_critical=True)

    new_clt = to_datatype(ChargingLimitType, clt)

    assert new_clt.charging_limit_source == clt.charging_limit_source
    assert new_clt.is_grid_critical == clt.is_grid_critical


def test_charging_needs_type():
    cnt = ChargingNeedsType(
        requested_energy_transfer=EnergyTransferModeEnumType.dc,
        departure_time="2024-01-01T10:00:00Z",
        ac_charging_parameters=ACChargingParametersType(
            energy_amount=20, ev_min_current=10, ev_max_current=32, ev_max_voltage=400
        ),
        dc_charging_parameters=DCChargingParametersType(
            ev_max_current=100,
            ev_max_voltage=500,
            energy_amount=50,
            ev_max_power=50000,
            state_of_charge=80,
        ),
    )

    new_cnt = to_datatype(ChargingNeedsType, cnt)

    assert new_cnt.requested_energy_transfer == cnt.requested_energy_transfer
    assert new_cnt.departure_time == cnt.departure_time
    assert isinstance(new_cnt.ac_charging_parameters, dict)
    assert (
        new_cnt.ac_charging_parameters["energy_amount"]
        == cnt.ac_charging_parameters.energy_amount
    )
    assert (
        new_cnt.ac_charging_parameters["ev_min_current"]
        == cnt.ac_charging_parameters.ev_min_current
    )
    assert isinstance(new_cnt.dc_charging_parameters, dict)
    assert (
        new_cnt.dc_charging_parameters["ev_max_current"]
        == cnt.dc_charging_parameters.ev_max_current
    )
    assert (
        new_cnt.dc_charging_parameters["state_of_charge"]
        == cnt.dc_charging_parameters.state_of_charge
    )


def test_charging_profile_criterion_type():
    cpct = ChargingProfileCriterionType(
        charging_profile_purpose=ChargingProfilePurposeEnumType.tx_default_profile,
        stack_level=0,
        charging_profile_id=[1, 2, 3],
    )

    new_cpct = to_datatype(ChargingProfileCriterionType, cpct)

    assert new_cpct.charging_profile_purpose == cpct.charging_profile_purpose
    assert new_cpct.stack_level == cpct.stack_level
    assert new_cpct.charging_profile_id == cpct.charging_profile_id


def test_charging_profile_type():
    cpt = ChargingProfileType(
        id=1,
        stack_level=0,
        charging_profile_purpose=ChargingProfilePurposeEnumType.tx_default_profile,
        charging_profile_kind=ChargingProfileKindEnumType.absolute,
        charging_schedule=[
            ChargingScheduleType(
                id=1,
                charging_rate_unit=ChargingRateUnitEnumType.watts,
                charging_schedule_period=[
                    ChargingSchedulePeriodType(
                        start_period=0, limit=11000.0, number_phases=3
                    )
                ],
                start_schedule="2024-01-01T10:00:00Z",
                duration=3600,
            )
        ],
        valid_from="2024-01-01T00:00:00Z",
        valid_to="2024-12-31T23:59:59Z",
    )

    new_cpt = to_datatype(ChargingProfileType, cpt)

    assert new_cpt.id == cpt.id
    assert new_cpt.stack_level == cpt.stack_level
    assert new_cpt.charging_profile_purpose == cpt.charging_profile_purpose
    assert new_cpt.charging_profile_kind == cpt.charging_profile_kind
    assert isinstance(new_cpt.charging_schedule[0], dict)
    assert new_cpt.charging_schedule[0]["id"] == cpt.charging_schedule[0].id
    assert new_cpt.valid_from == cpt.valid_from
    assert new_cpt.valid_to == cpt.valid_to


def test_charging_schedule_period_type():
    cspt = ChargingSchedulePeriodType(
        start_period=0, limit=32.0, number_phases=3, phase_to_use=1
    )

    new_cspt = to_datatype(ChargingSchedulePeriodType, cspt)

    assert new_cspt.start_period == cspt.start_period
    assert new_cspt.limit == cspt.limit
    assert new_cspt.number_phases == cspt.number_phases
    assert new_cspt.phase_to_use == cspt.phase_to_use


def test_charging_station_type():
    cst = ChargingStationType(
        model="Station Model X",
        vendor_name="Vendor ABC",
        serial_number="SN123456",
        modem=ModemType(iccid="89001234567890123456", imsi="123456789012345"),
        firmware_version="1.2.3",
    )

    new_cst = to_datatype(ChargingStationType, cst)

    assert new_cst.model == cst.model
    assert new_cst.vendor_name == cst.vendor_name
    assert new_cst.serial_number == cst.serial_number
    assert isinstance(new_cst.modem, dict)
    assert new_cst.modem["iccid"] == cst.modem.iccid
    assert new_cst.modem["imsi"] == cst.modem.imsi
    assert new_cst.firmware_version == cst.firmware_version


def test_clear_charging_profile_type():
    ccpt = ClearChargingProfileType(
        evse_id=1,
        charging_profile_purpose=ChargingProfilePurposeEnumType.tx_default_profile,
        stack_level=0,
    )

    new_ccpt = to_datatype(ClearChargingProfileType, ccpt)

    assert new_ccpt.evse_id == ccpt.evse_id
    assert new_ccpt.charging_profile_purpose == ccpt.charging_profile_purpose
    assert new_ccpt.stack_level == ccpt.stack_level


def test_clear_monitoring_result_type():
    cmrt = ClearMonitoringResultType(
        status=ClearMonitoringStatusEnumType.accepted,
        id=123,
        status_info=StatusInfoType(
            reason_code=ReasonEnumType.other,
            additional_info="Successfully cleared monitoring",
        ),
    )

    new_cmrt = to_datatype(ClearMonitoringResultType, cmrt)

    assert new_cmrt.status == cmrt.status
    assert new_cmrt.id == cmrt.id
    assert isinstance(new_cmrt.status_info, dict)
    assert new_cmrt.status_info["reason_code"] == cmrt.status_info.reason_code
    assert new_cmrt.status_info["additional_info"] == cmrt.status_info.additional_info


def test_component_type():
    ct = ComponentType(
        name="MainController", instance="instance1", evse=EVSEType(id=1, connector_id=2)
    )

    new_ct = to_datatype(ComponentType, ct)

    assert new_ct.name == ct.name
    assert new_ct.instance == ct.instance
    assert isinstance(new_ct.evse, dict)
    assert new_ct.evse["id"] == ct.evse.id
    assert new_ct.evse["connector_id"] == ct.evse.connector_id


def test_component_variable_type():
    cvt = ComponentVariableType(
        component=ComponentType(name="MainController", instance="instance1"),
        variable=VariableType(name="CurrentLimit", instance="instance1"),
    )

    new_cvt = to_datatype(ComponentVariableType, cvt)

    assert isinstance(new_cvt.component, dict)
    assert new_cvt.component["name"] == cvt.component.name
    assert new_cvt.component["instance"] == cvt.component.instance
    assert isinstance(new_cvt.variable, dict)
    assert new_cvt.variable["name"] == cvt.variable.name
    assert new_cvt.variable["instance"] == cvt.variable.instance


def test_composite_schedule_type():
    cst = CompositeScheduleType(
        evse_id=1,
        duration=3600,
        schedule_start="2024-01-01T10:00:00Z",
        charging_rate_unit=ChargingRateUnitEnumType.watts,
        charging_schedule_period=[
            ChargingSchedulePeriodType(start_period=0, limit=11000.0, number_phases=3)
        ],
    )

    new_cst = to_datatype(CompositeScheduleType, cst)

    assert new_cst.evse_id == cst.evse_id
    assert new_cst.duration == cst.duration
    assert new_cst.schedule_start == cst.schedule_start
    assert new_cst.charging_rate_unit == cst.charging_rate_unit
    assert isinstance(new_cst.charging_schedule_period[0], dict)
    assert (
        new_cst.charging_schedule_period[0]["start_period"]
        == cst.charging_schedule_period[0].start_period
    )
    assert (
        new_cst.charging_schedule_period[0]["limit"]
        == cst.charging_schedule_period[0].limit
    )


def test_consumption_cost_type():
    cct = ConsumptionCostType(
        start_value=0.0,
        cost=[CostType(cost_kind="RelativePrice", amount=1.0, amount_multiplier=0)],
    )

    new_cct = to_datatype(ConsumptionCostType, cct)

    assert new_cct.start_value == cct.start_value
    assert isinstance(new_cct.cost[0], dict)
    assert new_cct.cost[0]["cost_kind"] == cct.cost[0].cost_kind
    assert new_cct.cost[0]["amount"] == cct.cost[0].amount
    assert new_cct.cost[0]["amount_multiplier"] == cct.cost[0].amount_multiplier


def test_cost_type():
    ct = CostType(
        cost_kind=CostKindEnumType.carbon_dioxide_emission,
        amount=1.0,
        amount_multiplier=0,
    )

    new_ct = to_datatype(CostType, ct)

    assert new_ct.cost_kind == ct.cost_kind
    assert new_ct.amount == ct.amount
    assert new_ct.amount_multiplier == ct.amount_multiplier


def test_event_data_type():
    edt = EventDataType(
        event_id=1,
        timestamp="2024-01-01T10:00:00Z",
        trigger=EventTriggerEnumType.alerting,
        actual_value="High Temperature",
        tech_code="TC001",
        tech_info="Temperature sensor reading high",
        cleared=False,
        transaction_id="TX001",
        variable_monitoring_id=1,
        event_notification_type=EventNotificationEnumType.hard_wired_notification,
        component=ComponentType(name="MainController", instance="instance1"),
        variable=VariableType(name="Temperature", instance="instance1"),
    )

    new_edt = to_datatype(EventDataType, edt)

    assert new_edt.event_id == edt.event_id
    assert new_edt.timestamp == edt.timestamp
    assert new_edt.trigger == edt.trigger
    assert new_edt.actual_value == edt.actual_value
    assert new_edt.tech_code == edt.tech_code
    assert new_edt.tech_info == edt.tech_info
    assert new_edt.cleared == edt.cleared
    assert new_edt.transaction_id == edt.transaction_id
    assert new_edt.variable_monitoring_id == edt.variable_monitoring_id
    assert new_edt.event_notification_type == edt.event_notification_type
    assert isinstance(new_edt.component, dict)
    assert new_edt.component["name"] == edt.component.name
    assert isinstance(new_edt.variable, dict)
    assert new_edt.variable["name"] == edt.variable.name


def test_firmware_type():
    ft = FirmwareType(
        location="https://firmware.example.com/v1.2.3",
        retrieve_date_time="2024-01-01T10:00:00Z",
        install_date_time="2024-01-01T11:00:00Z",
        signing_certificate="MIIB...",
        signature="SHA256...",
    )

    new_ft = to_datatype(FirmwareType, ft)

    assert new_ft.location == ft.location
    assert new_ft.retrieve_date_time == ft.retrieve_date_time
    assert new_ft.install_date_time == ft.install_date_time
    assert new_ft.signing_certificate == ft.signing_certificate
    assert new_ft.signature == ft.signature


def test_get_variable_data_type():
    gvdt = GetVariableDataType(
        component=ComponentType(name="MainController", instance="instance1"),
        variable=VariableType(name="CurrentLimit", instance="instance1"),
        attribute_type=AttributeEnumType.actual,
    )

    new_gvdt = to_datatype(GetVariableDataType, gvdt)

    assert isinstance(new_gvdt.component, dict)
    assert new_gvdt.component["name"] == gvdt.component.name
    assert new_gvdt.component["instance"] == gvdt.component.instance
    assert isinstance(new_gvdt.variable, dict)
    assert new_gvdt.variable["name"] == gvdt.variable.name
    assert new_gvdt.variable["instance"] == gvdt.variable.instance
    assert new_gvdt.attribute_type == gvdt.attribute_type


def test_get_variable_result_type():
    gvrt = GetVariableResultType(
        attribute_status="Accepted",
        attribute_type=AttributeEnumType.actual,
        attribute_value="100",
        component=ComponentType(name="MainController", instance="instance1"),
        variable=VariableType(name="CurrentLimit", instance="instance1"),
    )

    new_gvrt = to_datatype(GetVariableResultType, gvrt)

    assert new_gvrt.attribute_status == gvrt.attribute_status
    assert new_gvrt.attribute_type == gvrt.attribute_type
    assert new_gvrt.attribute_value == gvrt.attribute_value
    assert isinstance(new_gvrt.component, dict)
    assert new_gvrt.component["name"] == gvrt.component.name
    assert isinstance(new_gvrt.variable, dict)
    assert new_gvrt.variable["name"] == gvrt.variable.name


def test_id_token_info_type():
    itit = IdTokenInfoType(
        status="Accepted",
        cache_expiry_date_time="2024-01-01T10:00:00Z",
        charging_priority=1,
        language_1="en",
        language_2="fr",
        group_id_token=IdTokenEnumType.central,
        personal_message=MessageContentType(
            format=MessageFormatEnumType.ascii, content="Welcome back!", language="en"
        ),
    )

    new_itit = to_datatype(IdTokenInfoType, itit)

    assert new_itit.status == itit.status
    assert new_itit.cache_expiry_date_time == itit.cache_expiry_date_time
    assert new_itit.charging_priority == itit.charging_priority
    assert new_itit.language_1 == itit.language_1
    assert new_itit.language_2 == itit.language_2
    assert isinstance(new_itit.group_id_token, str)
    assert new_itit.group_id_token == itit.group_id_token
    assert isinstance(new_itit.personal_message, dict)
    assert new_itit.personal_message["content"] == itit.personal_message.content


def test_log_parameters_type():
    lpt = LogParametersType(
        remote_location="https://logs.example.com",
        oldest_timestamp="2024-01-01T00:00:00Z",
        latest_timestamp="2024-01-01T23:59:59Z",
    )

    new_lpt = to_datatype(LogParametersType, lpt)

    assert new_lpt.remote_location == lpt.remote_location
    assert new_lpt.oldest_timestamp == lpt.oldest_timestamp
    assert new_lpt.latest_timestamp == lpt.latest_timestamp


def test_message_info_type():
    mit = MessageInfoType(
        id=1,
        priority=1,
        message=MessageContentType(
            format=MessageFormatEnumType.ascii,
            content="Important notice",
            language="en",
        ),
        display=ComponentType(name="MainDisplay", instance="instance1"),
        state=ChargingStateEnumType.charging,
    )

    new_mit = to_datatype(MessageInfoType, mit)

    assert new_mit.id == mit.id
    assert new_mit.priority == mit.priority
    assert isinstance(new_mit.message, dict)
    assert new_mit.message["content"] == mit.message.content
    assert isinstance(new_mit.display, dict)
    assert new_mit.display["name"] == mit.display.name
    assert new_mit.state == mit.state


def test_meter_value_type():
    mvt = MeterValueType(
        timestamp="2024-01-01T10:00:00Z",
        sampled_value=[
            SampledValueType(
                value=230.0,
                context=ReadingContextEnumType.sample_periodic,
                measurand=MeasurandEnumType.voltage,
                phase=PhaseEnumType.l1,
                location=LocationEnumType.outlet,
            )
        ],
    )

    new_mvt = to_datatype(MeterValueType, mvt)

    assert new_mvt.timestamp == mvt.timestamp
    assert isinstance(new_mvt.sampled_value[0], dict)
    assert new_mvt.sampled_value[0]["value"] == mvt.sampled_value[0].value
    assert new_mvt.sampled_value[0]["context"] == mvt.sampled_value[0].context
    assert new_mvt.sampled_value[0]["measurand"] == mvt.sampled_value[0].measurand
    assert new_mvt.sampled_value[0]["phase"] == mvt.sampled_value[0].phase
    assert new_mvt.sampled_value[0]["location"] == mvt.sampled_value[0].location


def test_modem_type():
    mt = ModemType(iccid="89012345678901234567", imsi="123456789012345")

    new_mt = to_datatype(ModemType, mt)

    assert new_mt.iccid == mt.iccid
    assert new_mt.imsi == mt.imsi


def test_monitoring_data_type():
    mdt = MonitoringDataType(
        component=ComponentType(name="MainController", instance="instance1"),
        variable=VariableType(name="Temperature", instance="instance1"),
        variable_monitoring=VariableMonitoringType(
            id=1,
            transaction=True,
            value=100.0,
            type=MonitorEnumType.upper_threshold,
            severity=1,
        ),
    )

    new_mdt = to_datatype(MonitoringDataType, mdt)

    assert isinstance(new_mdt.component, dict)
    assert new_mdt.component["name"] == mdt.component.name
    assert isinstance(new_mdt.variable, dict)
    assert new_mdt.variable["name"] == mdt.variable.name
    assert isinstance(new_mdt.variable_monitoring, dict)
    assert new_mdt.variable_monitoring["id"] == mdt.variable_monitoring.id
    assert new_mdt.variable_monitoring["value"] == mdt.variable_monitoring.value


def test_network_connection_profile_type():
    ncpt = NetworkConnectionProfileType(
        ocpp_version=OCPPVersionEnumType.ocpp20,
        ocpp_transport=OCPPTransportEnumType.json,
        ocpp_csms_url="wss://example.com/ocpp",
        message_timeout=30,
        security_profile=1,
        ocpp_interface=OCPPInterfaceEnumType.wired0,
        vpn=VPNType.ikev2,
    )

    new_ncpt = to_datatype(NetworkConnectionProfileType, ncpt)

    assert new_ncpt.ocpp_version == ncpt.ocpp_version
    assert new_ncpt.ocpp_transport == ncpt.ocpp_transport
    assert new_ncpt.ocpp_csms_url == ncpt.ocpp_csms_url
    assert new_ncpt.message_timeout == ncpt.message_timeout
    assert new_ncpt.security_profile == ncpt.security_profile
    assert new_ncpt.ocpp_interface == ncpt.ocpp_interface
    assert new_ncpt.vpn == ncpt.vpn


def test_ocsp_request_data_type():
    ordt = OCSPRequestDataType(
        hash_algorithm=HashAlgorithmEnumType.sha256,
        issuer_name_hash="issuer_hash_value",
        issuer_key_hash="issuer_key_hash_value",
        serial_number="serial123",
        responder_url="https://ocsp.example.com",
    )

    new_ordt = to_datatype(OCSPRequestDataType, ordt)

    assert new_ordt.hash_algorithm == ordt.hash_algorithm
    assert new_ordt.issuer_name_hash == ordt.issuer_name_hash
    assert new_ordt.issuer_key_hash == ordt.issuer_key_hash
    assert new_ordt.serial_number == ordt.serial_number
    assert new_ordt.responder_url == ordt.responder_url


def test_relative_time_interval_type():
    rtit = RelativeTimeIntervalType(start=0, duration=3600)

    new_rtit = to_datatype(RelativeTimeIntervalType, rtit)

    assert new_rtit.start == rtit.start
    assert new_rtit.duration == rtit.duration


def test_report_data_type():
    rdt = ReportDataType(
        component=ComponentType(name="MainController", instance="instance1"),
        variable=VariableType(name="Temperature", instance="instance1"),
        variable_attribute=[
            VariableAttributeType(
                type=AttributeEnumType.actual,
                value="25.5",
                mutability="ReadWrite",
                persistent=True,
                constant=False,
            )
        ],
        variable_characteristics=VariableCharacteristicsType(
            unit="Celsius",
            data_type=DataEnumType.decimal,
            min_limit="-20",
            max_limit="50",
            values_list=["10", "20", "30"],
            supports_monitoring=True,
        ),
    )

    new_rdt = to_datatype(ReportDataType, rdt)

    assert isinstance(new_rdt.component, dict)
    assert new_rdt.component["name"] == rdt.component.name
    assert isinstance(new_rdt.variable, dict)
    assert new_rdt.variable["name"] == rdt.variable.name
    assert isinstance(new_rdt.variable_attribute[0], dict)
    assert new_rdt.variable_attribute[0]["type"] == rdt.variable_attribute[0].type
    assert new_rdt.variable_attribute[0]["value"] == rdt.variable_attribute[0].value
    assert isinstance(new_rdt.variable_characteristics, dict)
    assert new_rdt.variable_characteristics["unit"] == rdt.variable_characteristics.unit
    assert (
        new_rdt.variable_characteristics["data_type"]
        == rdt.variable_characteristics.data_type
    )
    assert (
        new_rdt.variable_characteristics["supports_monitoring"]
        == rdt.variable_characteristics.supports_monitoring
    )


def test_sales_tariff_entry_type():
    stet = SalesTariffEntryType(
        e_price_level=1,
        relative_time_interval=RelativeTimeIntervalType(start=0, duration=3600),
        consumption_cost=[
            ConsumptionCostType(
                start_value=0.0,
                cost=[
                    CostType(cost_kind="RelativePrice", amount=1.0, amount_multiplier=0)
                ],
            )
        ],
    )

    new_stet = to_datatype(SalesTariffEntryType, stet)

    assert new_stet.e_price_level == stet.e_price_level
    assert isinstance(new_stet.relative_time_interval, dict)
    assert new_stet.relative_time_interval["start"] == stet.relative_time_interval.start
    assert (
        new_stet.relative_time_interval["duration"]
        == stet.relative_time_interval.duration
    )
    assert isinstance(new_stet.consumption_cost[0], dict)
    assert (
        new_stet.consumption_cost[0]["start_value"]
        == stet.consumption_cost[0].start_value
    )
    assert isinstance(new_stet.consumption_cost[0]["cost"][0], dict)
    assert (
        new_stet.consumption_cost[0]["cost"][0]["cost_kind"]
        == stet.consumption_cost[0].cost[0].cost_kind
    )
    assert (
        new_stet.consumption_cost[0]["cost"][0]["amount"]
        == stet.consumption_cost[0].cost[0].amount
    )
    assert (
        new_stet.consumption_cost[0]["cost"][0]["amount_multiplier"]
        == stet.consumption_cost[0].cost[0].amount_multiplier
    )


def test_sampled_value_type():
    svt = SampledValueType(
        value=230.0,
        context=ReadingContextEnumType.sample_periodic,
        measurand=MeasurandEnumType.voltage,
        phase=PhaseEnumType.l1,
        location=LocationEnumType.outlet,
        unit_of_measure=UnitOfMeasureType(
            unit=StandardizedUnitsOfMeasureEnumType.v, multiplier=0
        ),
    )

    new_svt = to_datatype(SampledValueType, svt)

    assert new_svt.value == svt.value
    assert new_svt.context == svt.context
    assert new_svt.measurand == svt.measurand
    assert new_svt.phase == svt.phase
    assert new_svt.location == svt.location
    assert isinstance(new_svt.unit_of_measure, dict)
    assert new_svt.unit_of_measure["unit"] == svt.unit_of_measure.unit
    assert new_svt.unit_of_measure["multiplier"] == svt.unit_of_measure.multiplier


def test_set_monitoring_data_type():
    smdt = SetMonitoringDataType(
        value=100.0,
        type=MonitorEnumType.upper_threshold,
        severity=1,
        component=ComponentType(name="MainController", instance="instance1"),
        variable=VariableType(name="Temperature", instance="instance1"),
        id=123456,
    )

    new_smdt = to_datatype(SetMonitoringDataType, smdt)

    assert new_smdt.value == smdt.value
    assert new_smdt.type == smdt.type
    assert new_smdt.severity == smdt.severity
    assert isinstance(new_smdt.component, dict)
    assert new_smdt.component["name"] == smdt.component.name
    assert new_smdt.component["instance"] == smdt.component.instance
    assert isinstance(new_smdt.variable, dict)
    assert new_smdt.variable["name"] == smdt.variable.name
    assert new_smdt.variable["instance"] == smdt.variable.instance
    assert new_smdt.id == smdt.id


def test_set_monitoring_result_type():
    smrt = SetMonitoringResultType(
        status=SetMonitoringStatusEnumType.accepted,
        id=123,
        status_info=StatusInfoType(
            reason_code=ReasonEnumType.other,
            additional_info="Successfully set monitoring",
        ),
        type=MonitorEnumType.upper_threshold,
        severity=1,
        component=ComponentType(name="MainController", instance="instance1"),
        variable=VariableType(name="Temperature", instance="instance1"),
    )

    new_smrt = to_datatype(SetMonitoringResultType, smrt)

    assert new_smrt.status == smrt.status
    assert new_smrt.id == smrt.id
    assert isinstance(new_smrt.status_info, dict)
    assert new_smrt.status_info["reason_code"] == smrt.status_info.reason_code
    assert new_smrt.status_info["additional_info"] == smrt.status_info.additional_info
    assert new_smrt.type == smrt.type
    assert new_smrt.severity == smrt.severity
    assert isinstance(new_smrt.component, dict)
    assert new_smrt.component["name"] == smrt.component.name
    assert new_smrt.component["instance"] == smrt.component.instance
    assert isinstance(new_smrt.variable, dict)
    assert new_smrt.variable["name"] == smrt.variable.name
    assert new_smrt.variable["instance"] == smrt.variable.instance


def test_set_variable_result_type():
    svrt = SetVariableResultType(
        attribute_type=AttributeEnumType.actual,
        attribute_status=SetVariableStatusEnumType.accepted,
        component=ComponentType(name="MainController", instance="instance1"),
        variable=VariableType(name="CurrentLimit", instance="instance1"),
        attribute_status_info=StatusInfoType(
            reason_code=ReasonEnumType.other,
            additional_info="Successfully set variable",
        ),
    )

    new_svrt = to_datatype(SetVariableResultType, svrt)

    assert new_svrt.attribute_type == svrt.attribute_type
    assert new_svrt.attribute_status == svrt.attribute_status
    assert isinstance(new_svrt.component, dict)
    assert new_svrt.component["name"] == svrt.component.name
    assert new_svrt.component["instance"] == svrt.component.instance
    assert isinstance(new_svrt.variable, dict)
    assert new_svrt.variable["name"] == svrt.variable.name
    assert new_svrt.variable["instance"] == svrt.variable.instance
    assert isinstance(new_svrt.attribute_status_info, dict)
    assert (
        new_svrt.attribute_status_info["reason_code"]
        == svrt.attribute_status_info.reason_code
    )
    assert (
        new_svrt.attribute_status_info["additional_info"]
        == svrt.attribute_status_info.additional_info
    )


def test_unit_of_measure_type():
    uomt = UnitOfMeasureType(
        # unit=UnitOfMeasureType.w,
        multiplier=1
    )

    new_uomt = to_datatype(UnitOfMeasureType, uomt)

    assert new_uomt.unit == uomt.unit
    assert new_uomt.multiplier == uomt.multiplier


def test_variable_attribute_type():
    vat = VariableAttributeType(
        type=AttributeEnumType.actual,
        value="25.5",
        mutability=MutabilityEnumType.read_write,
        persistent=True,
        constant=False,
    )

    new_vat = to_datatype(VariableAttributeType, vat)

    assert new_vat.type == vat.type
    assert new_vat.value == vat.value
    assert new_vat.mutability == vat.mutability
    assert new_vat.persistent == vat.persistent
    assert new_vat.constant == vat.constant


def test_variable_characteristics_type():
    vct = VariableCharacteristicsType(
        unit="Celsius",
        data_type=DataEnumType.decimal,
        min_limit="-20",
        max_limit="50",
        values_list=["10", "20", "30"],
        supports_monitoring=True,
    )

    new_vct = to_datatype(VariableCharacteristicsType, vct)

    assert new_vct.unit == vct.unit
    assert new_vct.data_type == vct.data_type
    assert new_vct.min_limit == vct.min_limit
    assert new_vct.max_limit == vct.max_limit
    assert new_vct.values_list == vct.values_list
    assert new_vct.supports_monitoring == vct.supports_monitoring


def test_variable_monitoring_type():
    vmt = VariableMonitoringType(
        id=1,
        transaction=True,
        value=100.0,
        type=MonitorEnumType.upper_threshold,
        severity=1,
    )

    new_vmt = to_datatype(VariableMonitoringType, vmt)

    assert new_vmt.id == vmt.id
    assert new_vmt.transaction == vmt.transaction
    assert new_vmt.value == vmt.value
    assert new_vmt.type == vmt.type
    assert new_vmt.severity == vmt.severity
