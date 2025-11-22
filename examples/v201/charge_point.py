import asyncio
import logging
# from datetime import datetime
import datetime
from dataclasses import dataclass
from typing import List, Dict, Optional, Any

# Attempt to import the 'websockets' package, exiting if not found
try:
    import websockets
except ModuleNotFoundError:
    print("This example relies on the 'websockets' package.")
    print("Please install it by running: ")
    print()
    print(" $ pip install websockets")
    import sys

    sys.exit(1)

# Import necessary classes from the OCPP 2.0.1 package
from ocpp.v201 import ChargePoint as cp
from ocpp.v201 import call

# Configure logging to display information
logging.basicConfig(level=logging.INFO)

# Data class to represent a sampled value in a meter reading
@dataclass
class SampledValue:
    value: str
    context: str = "Sample.Periodic"
    format: str = "Raw"
    measurand: str = "Energy.Active.Import.Register"
    unit: str = "Wh"

# Data class to represent a meter value containing sampled values and a timestamp
@dataclass
class MeterValue:
    timestamp: str
    sampled_value: List[SampledValue]


# Define the ChargePoint class, inheriting from the OCPP ChargePoint class
class ChargePoint(cp):
    
    # Method to periodically send heartbeat messages to the central system
    async def send_heartbeat(self, interval):
        request = call.Heartbeat()
        while True:
            try:
                await self.call(request)  # Send the heartbeat request
            except Exception as e:
                logging.error(f"Failed to send Heartbeat: {e}")
            await asyncio.sleep(interval)
    # Method to send a boot notification to the central system
    async def send_boot_notification(self):
        try:
            request = call.BootNotification(
                charging_station={"model": "Wallbox XYZ", "vendor_name": "anewone"},
                reason="PowerUp",
            )
            response = await self.call(request)

            if response.status == "Accepted":
                await self.send_heartbeat(response.interval)  
                 
        except Exception as e:
            logging.error(f"Failed to send Boot Notification: {e}")

    # Method to send a cancel reservation request to the central system
    async def send_cancel_reservation(self, reservation_id):
        try:
            request = call.CancelReservation(
                reservation_id=reservation_id
            )
            response = await self.call(request)  # Send the cancel reservation request

            if response is not None and response.status == "Accepted":
                print("**********Reservation successfully canceled.********* \n")
            else:
                print("Failed to cancel reservation.\n")
        except Exception as e:
            logging.error(f"Failed to cancel reservation: {e}")

    # Method to send a status notification to the central system
    async def send_status_notification(self, evse_id: int, connector_id: int, is_connected: bool):
        try:
            connector_status = "Available" if is_connected else "Unavailable"  # Determine connector status based on connection state
            request = call.StatusNotification(
                timestamp=self.get_current_time(),  
                connector_status=connector_status,
                connector_id=connector_id,
                evse_id=evse_id,
            )
            response = await self.call(request)  
             
        except Exception as e:
            logging.error(f"Failed to send Status Notification: {e}")

    # Method to send a security event notification to the central system
    async def send_security_event_notification(self):
        try:
            request = call.SecurityEventNotification(
                type="Secure",
                timestamp=self.get_current_time(),  
            )
            response = await self.call(request)   
             
        except Exception as e:
            logging.error(f"Failed to send Security Event Notification: {e}")


    async def send_meter_values(self, evse_id: int, sampled_values: List[SampledValue]):
        try:
            # Create a meter value dictionary with the current timestamp and sampled values
            meter_value = {
                'timestamp': self.get_current_time(),
                'sampledValue': [
                    {
                        'value': sv.value,
                    } for sv in sampled_values
                ]
            }

            request = call.MeterValues(
                evse_id=evse_id,
                meter_value=[meter_value]
            ) 
            response = await self.call(request)
             
        except Exception as e:
            logging.error(f"Failed to send MeterValues: {e}")
             
    # Helper method to get the current time in ISO 8601 format
    def get_current_time(self):
        return datetime.datetime.now().isoformat()

    # Method to send an authorization request to the central system
    async def send_authorization(self):
        try:
            request = call.Authorize(
                id_token={"idToken": "13", "type": "ISO14443" }
            )
            response = await self.call(request) 
            
        except Exception as e:
            logging.error(f"Failed to send Authorization: {e}")
    
    
     


# Main function to start the ChargePoint and send various messages
async def main():
    try:
        async with websockets.connect(
            "ws://localhost:9000/CP_1", subprotocols=["ocpp2.0.1"]
            
        ) as ws:
            charge_point = ChargePoint("CP_1", ws)  
            reservation_id = 12345 

            # Create a list of sampled values for the meter values message
            sampled_values = [
                  SampledValue(value=2000),
                SampledValue(value=1000)
            ]  
            
            is_vehicle_connected = True 
 
            # Gather and run all asynchronous tasks concurrently
            await asyncio.gather(
                charge_point.start(),
                charge_point.send_boot_notification(),
                charge_point.send_cancel_reservation(reservation_id),
                charge_point.send_status_notification(evse_id=2, connector_id=1, is_connected=is_vehicle_connected),
                charge_point.send_security_event_notification(),
                charge_point.send_meter_values(evse_id=1, sampled_values = sampled_values),
                charge_point.send_authorization(),
                 
            )
            
    except Exception as e:
        logging.error(f"Connection failed: {e}")

# Entry point of the script
if __name__ == "__main__":
    asyncio.run(main())


      