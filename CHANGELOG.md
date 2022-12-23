# Change log

## 0.15.0 (2022-05-11)

* [#306](https://github.com/mobilityhouse/ocpp/issues/306) Fix type hint `ocpp.v201.datatypes.MeterValueType.sampled_value`. Thanks [@Shadowsith](https://github.com/Shadowsith)
* [#328](https://github.com/mobilityhouse/ocpp/issues/324) Add missing attribute `ocpp.v201.dataypes.SampledValueType.measurand`.Thanks [@maurerle](https://github.com/maurerle)
* [#335](https://github.com/mobilityhouse/ocpp/issues/335) Improve Exception handling and CallError responses. Thanks [@proelke](https://github.com/proelke)
* [#316](https://github.com/mobilityhouse/ocpp/issues/333) Drop Python 3.6 support and update jsonschema to 4.4. Thanks [@laysauchoa](https://github.com/laysauchoa)

## 0.14.1 (2022-03-08)

* [#316](https://github.com/mobilityhouse/ocpp/issues/316) Fix definition of `GetVariableResultType.variable`. Thanks [@HugoJP1](https://github.com/HugoJP1)

## 0.14.0 (2022-03-03)

* [#312](https://github.com/mobilityhouse/ocpp/issues/312) Raise `TypeConstraintViolationError` instead of `ValidationError` when value exceeds length limit. Thanks [@tmh-grunwald-markus](https://github.com/tmh-grunwald-markus)

## 0.13.1 (2022-02-02)

The tag 0.13.0 was created, but the build to publish the release failed to pypi failed.
Therefore, 0.13.0 is not listed in this CHANGELOG.md

* [#293](https://github.com/mobilityhouse/ocpp/issues/293) Add missing attributes to `GetVariableResultType`. Thanks [@proelke](https://github.com/proelke)
* [#294](https://github.com/mobilityhouse/ocpp/issues/294) Improved error handling when schema validation fails. Thanks [@joaomariord](https://github.com/joaomariord)

## 0.12.1 (2022-01-17)

* [#289](https://github.com/mobilityhouse/ocpp/issues/289) Fix bug in `remove_nones()` when processing `str`. 

## 0.12.0 (2022-01-12)

* [#272](https://github.com/mobilityhouse/ocpp/issues/272) Improve `remove_nones` so it handles nested data structures better. Thanks [@proelke](https://github.com/proelke)
* [#287](https://github.com/mobilityhouse/ocpp/issues/287) Add enum StatusCodeInfoType. Thanks [@proelke](https://github.com/proelke)
* [#288](https://github.com/mobilityhouse/ocpp/issues/288) Fixed typos in attributes. Thanks [@mdwcrft](https://github.com/mdwcrft)

## 0.11.0 (2021-11-26)

* [#250](https://github.com/mobilityhouse/ocpp/issues/250) Add v1.6 data types
* [#268](https://github.com/mobilityhouse/ocpp/issues/268) Move from CircleCI to Github Actions.
* [#270](https://github.com/mobilityhouse/ocpp/issues/270) Changes badges to reflect move to Github Action

## 0.10.1 (2021-11-18)

* [#252](https://github.com/mobilityhouse/ocpp/issues/252) Fix CI build.
* [#259](https://github.com/mobilityhouse/ocpp/issues/259) Fix typo on `Action.SetMonitoringBase`. Thanks [@shaikhasif15752](https://github.com/shaikhasif15752)

## 0.10.0 (2021-09-16)

* [#249](https://github.com/mobilityhouse/ocpp/issues/249) Remove depreciated function `get_schema_code()`. Thanks [@proelke](https://github.com/proelke)
* [#240](https://github.com/mobilityhouse/ocpp/issues/240) Add OCPP v2.0.1 data types. Thanks [@proelke](https://github.com/proelke)

## 0.9.0 (2021-09-02)

* Fix limit array in meterValue and sampledValue. Thanks [@laysauchoa](https://github.com/laysauchoa)
* [#141](https://github.com/mobilityhouse/ocpp/issues/141) Add security enhancement for OCPP 1.6. Thanks [@villekr](https://github.com/villekr)
* [#217](https://github.com/mobilityhouse/ocpp/issues/217) Fix parsing of floats in GetCompositeSchedule response. Thanks [@laysauchoa](https://github.com/laysauchoa)
* [#223](https://github.com/mobilityhouse/ocpp/issues/223) Fix type DataTransferPayload.status. Thanks [@laysauchoa](https://github.com/laysauchoa)

## 0.8.3 (2021-04-21)

* [#200](https://github.com/mobilityhouse/ocpp/issues/200) Add context to `asyncio.TimeoutError`s raised by `ocpp.ChargePoint.call()`.

## 0.8.2 (2021-04-21)

* [#167](https://github.com/mobilityhouse/ocpp/issues/167) Fix OCPP 2.0.1 call payloads for `RequestStartTransactionPayload` and `RequestStopTransactionPayload`.

## 0.8.1 (2020-11-14)

* [#114](https://github.com/mobilityhouse/ocpp/issues/114) Make casing of `ocpp.v16.enums`'s attributes consistent. Thanks [@tropxy](https://github.com/tropxy)
* [#147](https://github.com/mobilityhouse/ocpp/issues/147) Fix type hint for `ocpp.v16.call.ChangeAvailabilityPayload`. Thanks [@laysauchoa](https://github.com/laysauchoa)
* [#150](https://github.com/mobilityhouse/ocpp/issues/150) Log in to Docker hub to prevent being rate limited.
* [#154](https://github.com/mobilityhouse/ocpp/issues/154) Speed up handling of `Call`s by caching `Draft4Validator` instances.

## 0.8.0 (2020-10-27)

* [#104](https://github.com/mobilityhouse/ocpp/issues/104) Allow `CallError`s to be catched. Thanks [@tmh-azinhal](https://github.com/tmh-azinhal)
* [#142](https://github.com/mobilityhouse/ocpp/issues/142)[#143](https://github.com/mobilityhouse/ocpp/issues/143) Add support for OCPP 2.0.1. Thanks [@tropxy](https://github.com/tropxy)
* [#137](https://github.com/mobilityhouse/ocpp/issues/137) Fix generation route map when using `@property`. Thanks [@fa1k3n](https://github.com/fa1k3n)


## 0.7.2 (2020-10-17)

* [#127](https://github.com/mobilityhouse/ocpp/issues/127) Fix type hints of enums.
* [#130](https://github.com/mobilityhouse/ocpp/issues/130) Fix possible deadlock when using `@after()` handlers.
* [#131](https://github.com/mobilityhouse/ocpp/issues/131) Add CI support for Python 3.9. Thanks [@laysauchoa](https://github.com/laysauchoa)!


## 0.7.1 (2020-09-18)

* [#117](https://github.com/mobilityhouse/ocpp/issues/117) Fix handling of async `@after()` handlers.

## 0.7.0 (2020-09-13)

* [#95](https://github.com/mobilityhouse/ocpp/issues/95) Remove use of deprecated `asyncio.coroutine()`. Thanks [@laysauchoa](https://github.com/laysauchoa)!
* [#105](https://github.com/mobilityhouse/ocpp/issues/105) Implement `__str__()` for all exceptions. Thanks [@laysauchoa](https://github.com/laysauchoa)!
* [#110](https://github.com/mobilityhouse/ocpp/issues/110) Subclass OCPP 1.6 enums from `str` and `enum.Enum`.
* [#113](https://github.com/mobilityhouse/ocpp/issues/113) Use OCPP 1.6 enums as type hints in calls and call results.

## 0.6.4 (2020-03-22)

* [#76](https://github.com/mobilityhouse/ocpp/issues/76) Fix names of 2 OCPP OCPP 2.0 call payloads.

## 0.6.3 (2020-02-26)

* Add links to source and documentation in Pypi. [@adamchainz](https://github.com/adamchainz)

## 0.6.2 (2020-02-21)

* [#71](https://github.com/mobilityhouse/ocpp/issues/71) Add unit Hertz. [@bengarrett1971](https://github.com/bengarrett1971)

## 0.6.1 (2020-02-19)

* [#68](https://github.com/mobilityhouse/ocpp/issues/68) Fix validation of SetChargingProfile

## 0.6.0 (2020-02-10)

* [#63](https://github.com/mobilityhouse/ocpp/issues/63) Remove spaces after separators before sending message
* [#65](https://github.com/mobilityhouse/ocpp/issues/65) `ocpp.ChargePoint.call()` doesn't validate the messages


## 0.5.1 (2019-12-06)

* [#57](https://github.com/mobilityhouse/ocpp/issues/57) Implement errata v4 for OCPP 1.6. Thanks [@darander](https://github.com/darander)

## 0.5.0 (2019-12-03)

* [#54](https://github.com/mobilityhouse/ocpp/issues/54) Add option to `@on()` to skip schema validation

## 0.4.4 (2019-11-21)

* [#43](https://github.com/mobilityhouse/ocpp/issues/43) Fix validation of 3 OCPP v1.6 payloads containing floats

## 0.4.3 (2019-11-18)

* [#50](https://github.com/mobilityhouse/ocpp/issues/50) Fix RuntimeError when using ocpp.charge_point.ChargePoint.call

## 0.4.2 (2019-11-18)

* [#46](https://github.com/mobilityhouse/ocpp/issues/46) Fix potential deadlock
* [#48](https://github.com/mobilityhouse/ocpp/issues/48) Make ocpp.v16.call.ReserveNowPayload.parent_id_tag optional

## 0.4.1 (2019-11-11)

* [#37](https://github.com/mobilityhouse/ocpp/issues/37) Add Python 3.8 support
* Several fixes of typos and type hints in v16 dataclasses

## 0.4.0 (2019-10-29)

* [#29](https://github.com/mobilityhouse/ocpp/issues/29) Add OCPP 2.0 support

## 0.3.2 (2019-09-30)

* [#27](https://github.com/mobilityhouse/ocpp/issues/27) Fix possible dead lock when running `@after()` handler.

## 0.3.1 (2019-09-23)

* An invalid 0.3.0 release has been uploaded to pypi.org. pypi.org doesn't
allow reuploading a new release using the same file names. Therefore a new
release had to be made.

## 0.3.0 (2019-09-23)

** Backwards incompatible change with ocpp <= 0.2.2. **
* [#26](https://github.com/mobilityhouse/ocpp/issues/26) Pass request payload to `@after()` handler.

## 0.2.2 (2019-08-29)

* [#21](https://github.com/mobilityhouse/ocpp/issues/21) Fix several type hints

## 0.2.1 (2019-07-31)

### Bug fixes

* [#14](https://github.com/mobilityhouse/ocpp/issues/14) Fix typo in attribute of call.StartTransactionPayload
* [#16](https://github.com/mobilityhouse/ocpp/issues/16) Fix attributes of call.StopTransaction
* [#18](https://github.com/mobilityhouse/ocpp/issues/18) Fix typo in attribute of call.RemoteStopTransaction

## 0.2.0 (2019-06-07)

### Improvements

* [#5](https://github.com/mobilityhouse/ocpp/issues/5) Add support for Python 3.6 and move to Poetry

## 0.1.1 (2019-05-31)

### Improvements

* [#3](https://github.com/mobilityhouse/ocpp/issues/3) Add CircleCI integration.

### Bug fixes

* [#1](https://github.com/mobilityhouse/ocpp/issues/1) Add JSON schema's to distribution.

## 0.1.0 (2019-05-26)

* Initial release.
