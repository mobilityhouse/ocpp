# Change log

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
