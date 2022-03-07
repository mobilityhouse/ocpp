import aiohttp_jinja2
import jinja2
from aiohttp import web


router = web.RouteTableDef()

#Each function is connected to the corresponding CPO function.
#The function also connects to the corresponding template in the template folder.
class HttpServer(web.View):

    """Index template that is empty"""
    @router.get("/")
    @aiohttp_jinja2.template('index.html')
    async def hello(self):
        return {}

    """Confirming authorization from CP to a database of collected IDs.
    Is currently not complete."""
    @router.post("/auth/login")
    @aiohttp_jinja2.template('authorize.html')
    async def authorize(self):
        data = await self.post()
        email = data["email"]
        password = data["password"]

    @router.post("/auth/refreshtoken")
    @aiohttp_jinja2.template('authorize.html')
    async def authorize(self):
        data = await self.post()
        token = data["token"]
        refresh_token = data["refresh_token"]
        cpo = self.app["cpo"]

    @router.post("/auth/register")
    @aiohttp_jinja2.template('authorize.html')
    async def authorize(self):
        data = await self.post()
        email = data["email"]
        password = data["password"]

    """Configuration template"""
    @router.get("/config")
    @aiohttp_jinja2.template('config.html')
    async def get_change_config(self):
        return {}

    """Changing configuration one charge point. """
    @router.post("/config")
    @aiohttp_jinja2.template('config.html')
    async def change_config(self):
        data = await self.post()
        cp_id = data['cp_id']
        key = data['key']
        value = data['value']
        cpo = self.app["cpo"]

        try:
            await cpo.change_configuration(cp_id, key, value)
        except ValueError as e:
            print(f"Failed to change configuration of charge point: {e}")
            return{}
        return {}

    """Get Configuration template"""
    @router.get("/getconfig")
    @aiohttp_jinja2.template('getconfig.html')
    async def get_get_config(self):
        return {}

    
    """Recieving the configuration of a specific key from one charge point."""
    @router.post("/getconfig")
    @aiohttp_jinja2.template('getconfig.html')
    async def get_config(self):

        data = await self.post()
        cp_id = data['cp_id']
        key = data['key']
        key = key.split(',')
        cpo = self.app["cpo"]

        try:
            await cpo.get_configuration(cp_id, key)
        except ValueError as e:
            print(f"Failed to get configuration of charge point: {e}")
            return{}
        return {}


    """Availability template"""
    @router.get("/availability")
    @aiohttp_jinja2.template('availability.html')
    async def get_availability(self):
        return {}

    """Changing the availability of one charge point"""
    @router.post("/availability")
    @aiohttp_jinja2.template('availability.html')
    async def availability(self):
        
        data = await self.post()
        cp_id = data['cp_id']
        connector_id = data['connector_id']
        connector_id = int(connector_id)
        type = data['type']
        cpo = self.app["cpo"]
        
        try:
            await cpo.change_availability(cp_id, connector_id, type)
        except ValueError as e:
            print(f"Failed to change availability of connector: {e}")
            return{}
        return {}

    """Start template"""
    @router.get("/start")
    @aiohttp_jinja2.template('generic.html')
    async def start_transaction(self):
        #Show timestamp and ID of charge point.
        return

    """Stop template"""
    @router.get("/stop")
    @aiohttp_jinja2.template('generic.html')
    async def stop_transaction(self):
        #Save transaction information to database connected to ID.
        return

    """Remote Start template"""
    @router.get("/remotestart")
    @aiohttp_jinja2.template('remotestart.html')
    async def get_start_remote(self):
        return {}

    @router.post("/remotestart")
    @aiohttp_jinja2.template('remotestart.html')
    async def start_remote(self):
        """Remotely start a transaction."""
        pass

    """Remote Stopp template"""
    @router.get("/remotestop")
    @aiohttp_jinja2.template('remotestop.html')
    async def get_stop_remote(self):
        return

    @router.post("/remotestop")
    @aiohttp_jinja2.template('remotestop.html')
    async def stop_remote(self):
        """Remotely stop a transaction. MUST be implemented in APP"""
        pass


    """Get Schedule template"""
    @router.get("/getschedule")
    @aiohttp_jinja2.template('getschedule.html')
    async def get_schedule(self):
        return {}

    """Get the set charge schedule of a charge point."""
    @router.post("/getschedule")
    @aiohttp_jinja2.template('getschedule.html')
    async def get_composite_schedule(self):
        
        data = await self.post()
        cp_id = data['cp_id']
        connector_id = data['connector_id']
        connector_id = int(connector_id)
        duration = data['duration']
        duration = int(duration)
        charging_rate_unit = data['charging_rate_unit']


        cpo = self.app["cpo"]

        try:
            await cpo.get_schedule(cp_id, connector_id, duration, charging_rate_unit)
        except ValueError as e:
            print(f"Failed to get schedule of charge point: {e}")
            return{}
        return{}

    """Get local list template"""
    @router.get("/getlocal")
    @aiohttp_jinja2.template('getlocal.html')
    async def get_local_list(self):
        return {}

    """Get the white list of authorized users as a local list."""
    @router.post("/getlocal")
    @aiohttp_jinja2.template('getlocal.html')
    async def local_list(self):
        """Remotely stop a transaction. MUST be implemented in APP"""
        
        data = await self.post()
        cp_id = data['cp_id']

        cpo = self.app["cpo"]

        try:
            await cpo.get_local_list(cp_id)
        except ValueError as e:
            print(f"Failed to get local list: {e}")
            return{}
        return{}

    """Send local list template"""
    @router.get("/sendlocallist")
    @aiohttp_jinja2.template('sendlocallist.html')
    async def get_send_local_list(self):
        return {}

    """Sends a local white list to a charge point.
    The white list contains a list of authorized users"""
    @router.post("/sendlocallist")
    @aiohttp_jinja2.template('sendlocallist.html')
    async def send_local_list(self):
        
        data = await self.post()
        cp_id = data['cp_id']
        list_version = data['list_version']
        list_version = int(list_version)
        id_tag = {'id_tag': data['id_tag']}
        expiry_date = data['expiry_date']
        parent_id_tag = data['parent_id_tag']
        status = data['status']
        id_tag_info = {"expiry_date": expiry_date, "parent_id_tag": parent_id_tag, "status": status}
        local_authorization_list = [id_tag, id_tag_info]
        update_type = data['update_type']

        cpo = self.app["cpo"]

        try:
            await cpo.send_local_list(cp_id, list_version, local_authorization_list, update_type)
        except ValueError as e:
            print(f"Failed to send local list: {e}")
            return{}
        return{}

    """Reserve template"""
    @router.get("/reserve")
    @aiohttp_jinja2.template('reserve.html')
    async def get_reserve(self):
        return{}

    """Reserves the connector of a charge point."""
    @router.post("/reserve")
    @aiohttp_jinja2.template('reserve.html')
    async def reserve(self):
        data = await self.post()
        cp_id = data['cp_id']
        connector_id = data['connector_id']
        connector_id = int(connector_id)
        expiry_date = data['expiry_date']
        id_tag = data['id_tag']
        parent_id_tag = data['parent_id_tag']
        reservation_id = data['reservation_id']
        reservation_id = int(reservation_id)

        cpo = self.app["cpo"]

        try:
            await cpo.reserve(cp_id, connector_id, expiry_date, id_tag, parent_id_tag, reservation_id)
        except ValueError as e:
            print(f"Failed to reserve the connector: {e}")
            return{}
        
        return{}

    """Cancel reservation template"""
    @router.get("/cancelreservation")
    @aiohttp_jinja2.template('cancelreservation.html')
    async def get_cancel_reservation(self):
        return{}

    """Cancels a current reservation at a connector"""
    @router.post("/cancelreservation")
    @aiohttp_jinja2.template('cancelreservation.html')
    async def cancel_reservation(self):
        data = await self.post()
        cp_id = data['cp_id'] #Needs to specify connector of that charge point
        reservation_id = data['reservation_id']
        reservation_id = int(reservation_id)

        cpo = self.app["cpo"]

        try:
            await cpo.cancel_reservation(cp_id, reservation_id)
        except ValueError as e:
            print(f"Failed to cancel reservation: {e}")
            return{}
        
        return{}

    """Clear charging profile template"""
    @router.get("/clearchargingprofile")
    @aiohttp_jinja2.template('clearchargingprofile.html')
    async def get_clear_charging_profile(self):
        return{}

    """Clears a current charging profile of a charge point.
    Currently not complete"""
    @router.post("/clearchargingprofile")
    @aiohttp_jinja2.template('clearchargingprofile.html')
    async def clear_charging_profile(self):
        data = await self.post()
        cp_id = data['cp_id']
        id = data['id']
        id = int(id)
        connector_id = data['connector_id']
        connector_id = int(connector_id)
        charging_profile_purpose = data['charging_profile_purpose']
        stack_level = data['stack_level']
        stack_level = int(stack_level)

        cpo = self.app["cpo"]

        try:
            await cpo.clear_charging_profile(cp_id, id, connector_id, charging_profile_purpose, stack_level)
        except ValueError as e:
            print(f"Failed to clear charging profile: {e}")
            return{}
        
        return{}

    """Data transfer template"""
    @router.get("/datatransfer")
    @aiohttp_jinja2.template('datatransfer.html')
    async def get_data_transfer(self):
        return{}

    """Sends data that is not supported by OCPP to charge point."""
    @router.post("/datatransfer")
    @aiohttp_jinja2.template('datatransfer.html')
    async def data_transfer(self, vendor_id, message_id, data):

        data = await self.post()
        cp_id = data['cp_id']
        vendor_id = data['vendor_id']
        message_id = data['message_id']
        data = data['data']
        cpo = self.app['cpo']       
        try:
            await cpo.data_transfer(cp_id, vendor_id, message_id, data)
        except ValueError as e:
            print(f"Failed to send data: {e}")
            return{}
        
        return{}

    """Get Diagnostics template"""
    @router.get("/diagnostics")
    @aiohttp_jinja2.template('diagnostics.html')
    async def get_diagnostics(self):
        return {}

    """Get the diagnostics of a component in a charge point during a specific interval"""
    @router.post("/diagnostics")
    @aiohttp_jinja2.template('diagnostics.html')
    async def diagnostics(self):
        data = await self.post()
        cp_id = data['cp_id']
        location = data['location']
        retries = data['retries']
        retries = int(retries)
        retry_interval = data['retry_interval']
        retry_interval = int(retry_interval)
        start_time = data['start_time']
        stop_time = data['stop_time']

        cpo = self.app["cpo"]   
        try:
            await cpo.get_diagnostics(cp_id, location, retries, retry_interval, start_time, stop_time)
        except ValueError as e:
            print(f"Failed to get diagnostics: {e}")
            return{}
        return {}

    """Meter value template"""
    @router.get("/meter")
    @aiohttp_jinja2.template('meter.html')
    async def meter_values(self):
        return {}

    """Get the meter values of a current transaction"""
    @router.post("/meter")
    @aiohttp_jinja2.template('meter.html')
    async def meter_values(self):
        data = await self.post()
        cp_id = data['cp_id']
        cpo = self.app["cpo"]

        try:
            await cpo.metervalues(cp_id)
        except ValueError as e:
            print(f"Failed to get meter values: {e}")
            return{}

        return {}
    
    """Clear Cache template"""
    @router.get("/cache")
    @aiohttp_jinja2.template('cache.html')
    async def get_cache(self):
        return {}

    """Clear the Authorization Cache of a charge point"""
    @router.post("/cache")
    @aiohttp_jinja2.template('cache.html')
    async def cache(self):
        data = await self.post()
        cp_id = data['cp_id']
        cpo = self.app["cpo"]
        try:
            await cpo.clear_cache(cp_id)
        except ValueError as e:
            print(f"Failed to clear cache of the charge point: {e}")
            return{}

        return{}

    """Unlock connector template"""
    @router.get("/unlock")
    @aiohttp_jinja2.template('unlock.html')
    async def getunlock(self):
        return {}

    """Unlocks a connector from the charge point"""
    @router.post("/unlock")
    @aiohttp_jinja2.template('unlock.html')
    async def unlock(self):
        """Unlock a specific connector to a specific CP"""
        data = await self.post()
        cp_id = data['cp_id']
        connector_id = data['connector_id']
        connector_id = int(connector_id)
        cpo = self.app["cpo"]   
        try:
            await cpo.unlock_connector(cp_id, connector_id)
        except ValueError as e:
            print(f"Failed to unlock connector: {e}")
            return{}
        return {}


    """Reset template"""
    @router.get("/reset")
    @aiohttp_jinja2.template('reset.html')
    async def get_reset(self):
        return {}


    """Resets the charge point"""
    @router.post("/reset")
    @aiohttp_jinja2.template('reset.html')
    async def reset(self):
        data = await self.post()
        cp_id = data['cp_id']
        type = data['type']
        cpo = self.app["cpo"]
        try:
            await cpo.reset(cp_id, type)
        except ValueError as e:
            print(f"Failed to reset charger: {e}")
            return{}
        return{}


    """Trigger template"""
    @router.get("/trigger")
    @aiohttp_jinja2.template('trigger.html')
    async def get_trigger(self):
        return {}

    """Trigger a message to be sent from charge point"""
    @router.post("/trigger")
    @aiohttp_jinja2.template('trigger.html')
    async def trigger(self):
        data = await self.post()
        cp_id = data['cp_id']
        requested_message = data['requested_message']
        connector_id = data['connector_id']
        connector_id = int(connector_id)

        cpo = self.app["cpo"]

        try:
            await cpo.trigger(cp_id, requested_message, connector_id)
        except ValueError as e:
            print(f"Failed to trigger message: {e}")
            return{}

        return{}

    """Disconnect template"""
    @router.get("/disconnect")
    @aiohttp_jinja2.template('disconnect.html')
    async def get_disconnect_charger(self):
        return {}

    """Disconnect the charge point from CPO."""
    @router.post("/disconnect")
    @aiohttp_jinja2.template('disconnect.html')
    async def disconnect_charger(self):
        """ HTTP handler for disconnecting a charger. """
        data = await self.post()
        cp_id = data['cp_id']
        cpo = self.app["cpo"]

        try:
            await cpo.disconnect_charger(cp_id)
        except ValueError as e:
            print(f"Failed to disconnect charger: {e}")
            return{}

        return{}

    

"""Creates a HTTP server."""
async def create_http_server(cpo) -> web.Application:
    app = web.Application()

    app.add_routes(router)

    aiohttp_jinja2.setup(
        app, loader=jinja2.FileSystemLoader(('C:/Users/MSI PC/cpo_concept/Drifter/templates')))
    app['static_root_url'] = '/static'

    app["cpo"] = cpo

    runner = web.AppRunner(app)
    await runner.setup()

    site = web.TCPSite(runner, "127.0.0.1", 5000)
    return site
