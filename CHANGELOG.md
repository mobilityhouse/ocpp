# Change log

## 0.8.0 (2020-10-27)

* [#104](https://github.com/mobilityhouse/ocpp/issues/104) Allow `CallError`s to be catched. Thanks [@tmh-azinhal](https://github.com/tmh-azinhal)
* [#142](https://github.com/mobilityhouse/ocpp/issues/142)[#143](https://github.com/mobilityhouse/ocpp/issues/143) Add support for OCPP 2.0.1. Thanks [@tropxy](https://github.com/tropxy)
* [#137](https://github.com/mobilityhouse/ocpp/issues/137) Fix generation route map when using `@property`. Thanks [@fa1k3n](https://github.com/fa1k3n)


## 0.7.2 (2020-10-17)

* [#127](https://github.com/mobilityhouse/ocpp/issues/127) Fix type hints of enums.
* [#130](https://github.com/mobilityhouse/ocpp/issues/130) Fix possible deadlock when using `@after()` handlers.
* [#131](https://github.com/mobilityhouse/ocpp/issues/131) Add CI support for Python 3.9. Thanks [@laysauchoa]](https://github.com/laysauchoa)!


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
