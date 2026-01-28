"""The Klafs Sauna integration."""
from __future__ import annotations

import logging
from datetime import timedelta

import voluptuous as vol

from homeassistant.config_entries import ConfigEntry
from homeassistant.const import CONF_PASSWORD, CONF_USERNAME, Platform
from homeassistant.core import HomeAssistant, ServiceCall
from homeassistant.helpers import config_validation as cv
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator, UpdateFailed

from .api import KlafsApiClient
from .const import DOMAIN

_LOGGER = logging.getLogger(__name__)

PLATFORMS: list[Platform] = [
    Platform.CLIMATE,
    Platform.SENSOR,
    Platform.SWITCH,
]

SCAN_INTERVAL = timedelta(seconds=60)

# Service schemas
SERVICE_POWER_ON_WITH_PIN = "power_on_with_pin"
SERVICE_SET_HUMIDITY = "set_humidity_level"
SERVICE_SET_START_TIME = "set_start_time"

POWER_ON_SCHEMA = vol.Schema(
    {
        vol.Required("entity_id"): cv.entity_id,
        vol.Required("pin"): cv.string,
    }
)

HUMIDITY_SCHEMA = vol.Schema(
    {
        vol.Required("entity_id"): cv.entity_id,
        vol.Required("humidity_level"): vol.All(vol.Coerce(int), vol.Range(min=1, max=10)),
    }
)

START_TIME_SCHEMA = vol.Schema(
    {
        vol.Required("entity_id"): cv.entity_id,
        vol.Required("hour"): vol.All(vol.Coerce(int), vol.Range(min=0, max=23)),
        vol.Required("minute"): vol.All(vol.Coerce(int), vol.Range(min=0, max=59)),
    }
)


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up Klafs from a config entry."""
    _LOGGER.info("Setting up Klafs integration")
    _LOGGER.debug("Entry data keys: %s", list(entry.data.keys()))
    
    hass.data.setdefault(DOMAIN, {})

    try:
        username = entry.data.get(CONF_USERNAME)
        password = entry.data.get(CONF_PASSWORD)
        
        if not username or not password:
            _LOGGER.error("Missing username or password in config entry")
            return False
        
        _LOGGER.debug("Creating API client for user: %s", username)
        
        from homeassistant.helpers.aiohttp_client import async_get_clientsession
        
        client = KlafsApiClient(
            username,
            password,
            async_get_clientsession(hass),
        )

        _LOGGER.debug("Creating coordinator")
        coordinator = KlafsDataUpdateCoordinator(hass, client, entry)
        
        _LOGGER.debug("Performing first refresh")
        await coordinator.async_config_entry_first_refresh()

        hass.data[DOMAIN][entry.entry_id] = coordinator

        _LOGGER.debug("Setting up platforms: %s", PLATFORMS)
        await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)
    except Exception as err:
        _LOGGER.exception("Error setting up Klafs integration: %s", err)
        return False

    # Register services
    async def handle_power_on_with_pin(call: ServiceCall) -> None:
        """Handle power on with PIN service."""
        entity_id = call.data["entity_id"]
        pin = call.data["pin"]
        
        # Find the climate entity and get sauna_id
        for coord in hass.data[DOMAIN].values():
            if isinstance(coord, KlafsDataUpdateCoordinator):
                for sauna_id in coord.data:
                    # Match entity_id pattern
                    if entity_id.endswith(sauna_id[:8].lower()):
                        await coord.client.power_on(sauna_id, pin)
                        await coord.async_request_refresh()
                        return

    async def handle_set_humidity(call: ServiceCall) -> None:
        """Handle set humidity level service."""
        entity_id = call.data["entity_id"]
        humidity_level = call.data["humidity_level"]
        
        for coord in hass.data[DOMAIN].values():
            if isinstance(coord, KlafsDataUpdateCoordinator):
                for sauna_id in coord.data:
                    if entity_id.endswith(sauna_id[:8].lower()):
                        await coord.client.set_humidity(sauna_id, humidity_level)
                        await coord.async_request_refresh()
                        return

    async def handle_set_start_time(call: ServiceCall) -> None:
        """Handle set start time service."""
        entity_id = call.data["entity_id"]
        hour = call.data["hour"]
        minute = call.data["minute"]
        
        for coord in hass.data[DOMAIN].values():
            if isinstance(coord, KlafsDataUpdateCoordinator):
                for sauna_id in coord.data:
                    if entity_id.endswith(sauna_id[:8].lower()):
                        await coord.client.set_start_time(sauna_id, hour, minute)
                        await coord.async_request_refresh()
                        return

    hass.services.async_register(
        DOMAIN, SERVICE_POWER_ON_WITH_PIN, handle_power_on_with_pin, schema=POWER_ON_SCHEMA
    )
    hass.services.async_register(
        DOMAIN, SERVICE_SET_HUMIDITY, handle_set_humidity, schema=HUMIDITY_SCHEMA
    )
    hass.services.async_register(
        DOMAIN, SERVICE_SET_START_TIME, handle_set_start_time, schema=START_TIME_SCHEMA
    )

    return True


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Unload a config entry."""
    if unload_ok := await hass.config_entries.async_unload_platforms(entry, PLATFORMS):
        hass.data[DOMAIN].pop(entry.entry_id)

    return unload_ok


class KlafsDataUpdateCoordinator(DataUpdateCoordinator):
    """Class to manage fetching Klafs data."""

    def __init__(
        self, hass: HomeAssistant, client: KlafsApiClient, entry: ConfigEntry
    ) -> None:
        """Initialize."""
        self.client = client
        self.entry = entry
        self.saunas_config = entry.data.get("saunas", {})

        super().__init__(
            hass,
            _LOGGER,
            name=DOMAIN,
            update_interval=SCAN_INTERVAL,
        )

    async def _async_update_data(self):
        """Update data via library."""
        _LOGGER.debug("Starting data update for Klafs")
        try:
            if not self.client.is_authenticated:
                _LOGGER.debug("Client not authenticated, logging in")
                await self.client.login()

            # Update status for configured saunas only
            data = {}
            _LOGGER.debug("Configured saunas: %s", list(self.saunas_config.keys()))
            
            for sauna_id in self.saunas_config:
                _LOGGER.debug("Fetching status for sauna: %s", sauna_id)
                status = await self.client.get_sauna_status(sauna_id)
                if status:
                    data[sauna_id] = status
                    _LOGGER.debug("Got status for sauna %s: isPoweredOn=%s, currentTemp=%s", 
                                sauna_id[:8], status.get("isPoweredOn"), status.get("currentTemperature"))
                else:
                    _LOGGER.warning("No status returned for sauna: %s", sauna_id)

            _LOGGER.info("Data update completed, got data for %d sauna(s)", len(data))
            return data
        except Exception as err:
            _LOGGER.exception("Error updating data: %s", err)
            raise UpdateFailed(f"Error communicating with API: {err}") from err
    
    def get_sauna_pin(self, sauna_id: str) -> str | None:
        """Get PIN for a specific sauna."""
        if sauna_id in self.saunas_config:
            return self.saunas_config[sauna_id].get("pin")
        return None
    
    def get_sauna_name(self, sauna_id: str) -> str:
        """Get name for a specific sauna."""
        if sauna_id in self.saunas_config:
            return self.saunas_config[sauna_id].get("name", sauna_id[:8])
        return sauna_id[:8]
