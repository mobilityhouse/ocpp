import asyncio
import logging
import json
from datetime import datetime
from dataclasses import dataclass, asdict

try:
    import websockets
except ModuleNotFoundError:
    print("This example relies on the 'websockets' package.")
    print("Please install it by running: ")
    print()
    print(" $ pip install websockets")
    import sys

    sys.exit(1)

from ocpp.routing import on
from ocpp.v16 import ChargePoint as cp
from ocpp.v16 import call_result, call
from ocpp.v16.enums import (Action,
                            RegistrationStatus,
                            PNCMessageIDType,
                            GetCertificateIdUseEnumType,
                            HashAlgorithmEnumType)
from ocpp.v16.datatypes_ext import (
    InstallCertificateReq,
    InstallCertificateUseEnumType,
    GetInstallCertificateIdsReq,
    DeleteCertificateReq,
    CertificateHashDataType
    )

logging.basicConfig(level=logging.DEBUG)


class ChargePoint(cp):
    @on(Action.BootNotification)
    def on_boot_notification(
            self, charge_point_vendor: str, charge_point_model: str, **kwargs
    ):
        # asyncio.create_task(self.send_install_certificate())
        # asyncio.create_task(self.send_get_installed_certificate_ids_req())

        return call_result.BootNotificationPayload(
            current_time=datetime.utcnow().isoformat(),
            interval=10,
            status=RegistrationStatus.accepted,
        )


    @on(Action.StatusNotification)
    def on_status_notification(
            self, connectorId, errorCode, info, status, timestamp, vendorId, vendorErrorCode
    ):

        return call_result.StatusNotificationPayload(

        )

    @on(Action.Heartbeat)
    def on_heartbeat(self):
        asyncio.create_task(self.send_install_certificate())
        asyncio.create_task(self.send_get_installed_certificate_ids_req())
        return call_result.HeartbeatPayload(
            current_time=datetime.utcnow().isoformat()
        )

    @on(Action.DataTransfer)
    async def send_install_certificate(self):
        # Create InstallCertificate.req json that will be put in data field of Datatransfer
        install_certificate_req: InstallCertificateReq = InstallCertificateReq(
            certificateType=InstallCertificateUseEnumType.mo_root_certificate)

        # Convert install_certificate_req to dict and then to json string/ will be put in the data field of DataTransfer
        install_certificate_req_json = json.dumps(asdict(install_certificate_req))

        request = call.DataTransferPayload(
            message_id=PNCMessageIDType.install_certificate,
            data=install_certificate_req_json,
            vendor_id="org.openchargealliance.iso15118pnc"
        )

        response = await self.call(request)

    @on(Action.DataTransfer)
    async def send_get_installed_certificate_ids_req(self):
        get_install_certificate_ids_req: GetInstallCertificateIdsReq = GetInstallCertificateIdsReq(
            [GetCertificateIdUseEnumType.mo_root_certificate,
             GetCertificateIdUseEnumType.v2g_root_certificate]
        )

        get_install_certificate_req_json = json.dumps(asdict(get_install_certificate_ids_req))

        request = call.DataTransferPayload(
            message_id=PNCMessageIDType.get_installed_certificate_ids,
            data=get_install_certificate_req_json,
            vendor_id="org.openchargealliance.iso15118pnc"
        )

        response = await self.call(request)

    @on(Action.DataTransfer)
    async def delete_certificate_req(self):
        certificate_hash_data_type: CertificateHashDataType= CertificateHashDataType(

        )
        delete_certificate_req: DeleteCertificateReq = DeleteCertificateReq()


async def on_connect(websocket, path):
    """For every new charge point that connects, create a ChargePoint
    instance and start listening for messages.
    """
    try:
        requested_protocols = websocket.request_headers["Sec-WebSocket-Protocol"]
    except KeyError:
        logging.error("Client hasn't requested any Subprotocol. Closing Connection")
        return await websocket.close()
    if websocket.subprotocol:
        logging.info("Protocols Matched: %s", websocket.subprotocol)
    else:
        # In the websockets lib if no subprotocols are supported by the
        # client and the server, it proceeds without a subprotocol,
        # so we have to manually close the connection.
        logging.warning(
            "Protocols Mismatched | Expected Subprotocols: %s,"
            " but client supports  %s | Closing connection",
            websocket.available_subprotocols,
            requested_protocols,
        )
        return await websocket.close()

    charge_point_id = path.strip("/")
    cp = ChargePoint(charge_point_id, websocket)

    await cp.start()


async def main():
    server = await websockets.serve(
        on_connect, "0.0.0.0", 9000, subprotocols=["ocpp1.6"]
    )

    logging.info("Server Started listening to new connections...")
    await server.wait_closed()


if __name__ == "__main__":
    # asyncio.run() is used when running this example with Python >= 3.7v
    asyncio.run(main())
