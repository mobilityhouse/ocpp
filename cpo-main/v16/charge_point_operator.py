import asyncio

from ocpp.v16 import ChargePoint as cp

from .cpo_class import ChargePoint
from typing import Dict, Optional


"""This Class register chargers and forward the inputs from http_server to the correct Charge Point.
"""


class CentralSystem(cp):
    def __init__(self):
        self._chargers = {}
        self._count = 0

    def register_charger(self, cp: ChargePoint) -> asyncio.Queue:
        """ Register a new ChargePoint at the CPO. The function returns a
        queue.  The CPO will put a message on the queue if the CPO wants to
        close the connection. 
        Tested on hardware"""
        queue = asyncio.Queue(maxsize=1)

        # Store a reference to the task so we can cancel it later if needed.
        task = asyncio.create_task(self.start_charger(cp, queue))
        self._chargers[cp] = task
        self._count = self._count + 1

        return queue

    async def start_charger(self, cp, queue):
        """ Start listening for message of charger.
        Tested on hardware"""
        try:
            await cp.start()
        except Exception as e:
            print(f"Charger {cp.id} disconnected: {e}")
        finally:
            # Deletes the reference to the charger when the connection is closed.
            del self._chargers[cp]
            self._count = self._count - 1
            await queue.put(True)


    async def change_configuration(self, cp_id: str, key: str, value: str):
        """Changes the configuration
        Tested on hardware"""
        for cp, task in self._chargers.items():
            if cp.id == cp_id:
                await cp.send_change_configuration(key, value)                
                return 
            raise ValueError(f"Charger {id} not connected.")

    async def get_schedule(self, cp_id: str, connector_id: int, duration: int, charging_rate_unit: str):
        """ Get Schedule of one connector of a charge point
        Not tested"""
        for cp, task in self._chargers.items():
            if cp.id == cp_id:
                await cp.send_get_schedule(connector_id, duration, charging_rate_unit)                
                return 
            raise ValueError(f"Charger {id} not connected.")

    async def get_local_list(self, cp_id: str):
        """Get the local white list
        Not tested"""
        for cp, task in self._chargers.items():
            if cp.id == cp_id:
                await cp.send_get_local_list()                
                return 
            raise ValueError(f"Charger {id} not connected.")

    async def get_configuration(self, cp_id: str, key: str):
        """Get the current configuration of a specfic Key of a charge point.
        Tested but not on hardware"""
        for cp, task in self._chargers.items():
            if cp.id == cp_id:
                await cp.send_get_configuration(key)                
                return 
            raise ValueError(f"Charger {id} not connected.")

    async def get_diagnostics(self, cp_id: str, location: str, retries: int, retry_interval: int, start_time: str, stop_time: str):
        """Get the diagnostics of a specific physical part of a specific charge point for a set amount of time
        Not tested"""
        for cp, task in self._chargers.items():
            if cp.id == cp_id:
                await cp.send_get_configuration(location, retries, retry_interval, start_time, stop_time)                
                return 
            raise ValueError(f"Charger {id} not connected.")
            

    async def change_availability(self, cp_id: str, connector_id: int, type: str):
        """Changes the Availability of a specific charge point
        Tested on hardware"""
        for cp, task in self._chargers.items():
            if cp.id == cp_id:
                await cp.send_change_availability(connector_id, type)
                return 
            raise ValueError(f"Charger {id} not connected.")
            

    async def clear_cache(self, cp_id: str):
        """Clear the white list of authorized users of a specific charge point
        Tested but not on hardware"""
        for cp, task in self._chargers.items():
            if cp.id == cp_id:
                await cp.send_clear_cache()
                return 
        raise ValueError(f"Charger {id} not connected.")

    async def disconnect_charger(self, cp_id: str):
        """Disconnects a specific charger
        Tested on hardware"""
        for cp, task in self._chargers.items():
            if cp.id == cp_id:
                task.cancel()
                return 
        raise ValueError(f"Charger {id} not connected.")

    async def start_remote(self, cp_id: str, id_tag: str, connector_id: Optional[int] = None):
        """Starts a transaction remotely
        Not tested"""
        for cp, task in self._chargers.items():
            if cp.id == cp_id:
                await cp.send_remote_start_transaction(id_tag, connector_id)
                return 
        raise ValueError(f"Charger {cp_id} not connected.")
            

    async def stop_remote(self, cp_id, id: str, transaction_id):
        """Stops a trasaction remotely
        Not tested"""
        for cp, task in self._chargers.items():
            if cp.id == cp_id:
                await cp.send_remote_stop_transaction(transaction_id)
                return 
        raise ValueError(f"Charger {id} not connected.")            
    
    async def authorize(self, id_tag: str):
        """Authorize a user. This can be done through app, physical tag or local list
        Not developed"""
        pass


    async def data_transfer(self, vendor_id: str, message_id: str, data: str):
        """Transfers the data from charge point to CPO
        Not developed"""
        pass

    async def meter_values(self, connector_id: int, meter_values: Dict, transaction_id: int):
        """Get the meter values of a current or past transaction
        Not developed"""
        pass

    async def reset(self, cp_id: str, type: str):
        """Reset a specific charge point
        Tested on hardware"""
        for cp, task in self._chargers.items():
            if cp.id == cp_id:
                await cp.send_reset(type)
                return 
        raise ValueError(f"Charger {id} not connected.")

    async def start_transaction(self, connector_id, id_tag, meter_start, time_stamp, reservation_id):
        """Charge point starts a transaction which CPO register
        Not developed"""
        pass

    async def stop_transaction(self, transaction_id, timestamp, meter_stop):
        """Charge point stop a transaction and CPO register. CPO also retrieves data of that transaction
        Not developed"""
        pass

    async def reserve(self, cp_id: str, connector_id: int, expiry_date: str, id_tag: str, parent_id_tag: str, reservation_id: int):
        """CPO reserves a specific charge point with date and time
        Not tested"""
        for cp, task in self._chargers.items():
            if cp.id == cp_id:
                await cp.send_reserve_now(connector_id, expiry_date, id_tag, parent_id_tag, reservation_id)
                return 
        raise ValueError(f"Charger {id} not connected.")

    async def cancel_reservation(self, cp_id, reservation_id: int):
        """CPO cancel a reservation.
        Not tested"""
        for cp, task in self._chargers.items():
            if cp.id == cp_id:
                await cp.send_cancel_reservation(reservation_id)
                return 
        raise ValueError(f"Charger {id} not connected.")    


    async def clear_charging_profile(self, cp_id: str, connector_id: int, charging_profile_purpose: str, stack_level: int):
        """CPO clear the charging profile of a charge point
        Not tested"""
        for cp, task in self._chargers.items():
            if cp.id == cp_id:
                await cp.send_clear_charging_profile(connector_id, charging_profile_purpose, stack_level)
                return 
        raise ValueError(f"Charger {id} not connected.")  

    async def send_local_list(self, cp_id: str, list_version: int, local_authorization_list: list, update_info: str):
        """CPO PUT a local authorization list to a charge point
        Tested but not on hardware"""
        for cp, task in self._chargers.items():
            if cp.id == cp_id:
                await cp.send_local_list(list_version, local_authorization_list, update_info)
                return 
        raise ValueError(f"Charger {id} not connected.") 


    async def trigger(self, cp_id: str, requested_message: str, connector_id: int):
        """CPO sends a signal to trigger certain messages of the charge point.
        Not tested"""
        for cp, task in self._chargers.items():
            if cp.id == cp_id:
                await cp.send_trigger(requested_message, connector_id)
                return 
        raise ValueError(f"Charger {id} not connected.")


    async def unlock_connector(self, cp_id: str, connector_id: int):
        """CPO unlock a specific connector of a specific charge point.
        Not tested"""
        for cp, task in self._chargers.items():
            if cp.id == cp_id:
                await cp.send_unlock_connector(connector_id)
                return 
        raise ValueError(f"Charger {id} not connected.")
            