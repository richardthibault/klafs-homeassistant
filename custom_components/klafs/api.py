"""API client for Klafs Sauna."""
from __future__ import annotations

import logging
from typing import Any

import aiohttp

from .const import (
    API_BASE_URL,
    API_CHANGE_HUM_LEVEL_ENDPOINT,
    API_CHANGE_TEMPERATURE_ENDPOINT,
    API_GET_DATA_ENDPOINT,
    API_LOGIN_ENDPOINT,
    API_SET_MODE_ENDPOINT,
    API_SET_SELECTED_TIME_ENDPOINT,
    API_START_CABIN_ENDPOINT,
    API_STOP_CABIN_ENDPOINT,
)

_LOGGER = logging.getLogger(__name__)


class KlafsApiClient:
    """Klafs API Client."""

    def __init__(
        self, username: str, password: str, session: aiohttp.ClientSession
    ) -> None:
        """Initialize the API client."""
        self.username = username
        self.password = password
        self.session = session
        self.cookies = None
        self.is_authenticated = False

    async def login(self) -> bool:
        """Login to Klafs API."""
        try:
            data = {
                "UserName": self.username,
                "Password": self.password,
            }

            async with self.session.post(
                f"{API_BASE_URL}{API_LOGIN_ENDPOINT}",
                data=data,
                headers={"Content-Type": "application/x-www-form-urlencoded"},
                allow_redirects=True,
            ) as response:
                if response.status == 200:
                    self.cookies = response.cookies
                    self.is_authenticated = True
                    _LOGGER.info("Successfully logged in to Klafs API")
                    return True
                else:
                    _LOGGER.error(
                        "Failed to login to Klafs API: %s", response.status
                    )
                    self.is_authenticated = False
                    return False
        except Exception as err:
            _LOGGER.error("Error during login: %s", err)
            self.is_authenticated = False
            return False

    async def get_saunas(self) -> dict[str, Any]:
        """Get list of saunas by parsing the SaunaApp page."""
        try:
            _LOGGER.debug("Fetching saunas from SaunaApp page")
            async with self.session.get(
                f"{API_BASE_URL}/SaunaApp",
                cookies=self.cookies,
            ) as response:
                _LOGGER.debug("Get saunas response status: %s", response.status)
                if response.status == 200:
                    html = await response.text()
                    _LOGGER.debug("Got SaunaApp page, parsing...")
                    
                    # Parse HTML to extract sauna list from <select> element
                    # Format: <option value="sauna-id">Sauna Name</option>
                    import re
                    saunas = {}
                    
                    # Find all option tags in SelectedCabin select
                    pattern = r'<option[^>]*value="([^"]+)"[^>]*>([^<]+)</option>'
                    matches = re.findall(pattern, html)
                    
                    for sauna_id, sauna_name in matches:
                        # Filter out empty or invalid IDs
                        if sauna_id and len(sauna_id) > 10:
                            saunas[sauna_id] = {
                                "saunaId": sauna_id,
                                "name": sauna_name.strip()
                            }
                    
                    _LOGGER.info("Found %d sauna(s)", len(saunas))
                    return saunas
                else:
                    _LOGGER.error("Failed to get saunas: %s", response.status)
                    return {}
        except Exception as err:
            _LOGGER.error("Error getting saunas: %s", err)
            return {}

    async def get_sauna_status(self, sauna_id: str) -> dict[str, Any]:
        """Get status of a specific sauna."""
        try:
            url = f"{API_BASE_URL}{API_GET_DATA_ENDPOINT}?id={sauna_id}"
            
            async with self.session.get(
                url,
                cookies=self.cookies,
            ) as response:
                if response.status == 200:
                    data = await response.json()
                    return data
                else:
                    _LOGGER.error(
                        "Failed to get sauna status: %s", response.status
                    )
                    return {}
        except Exception as err:
            _LOGGER.error("Error getting sauna status: %s", err)
            return {}

    async def set_sauna_control(
        self, sauna_id: str, endpoint: str, control_data: dict[str, Any]
    ) -> bool:
        """Send control commands to sauna."""
        try:
            payload = {"id": sauna_id, **control_data}

            async with self.session.post(
                f"{API_BASE_URL}{endpoint}",
                json=payload,
                cookies=self.cookies,
                headers={"Content-Type": "application/json"},
            ) as response:
                if response.status == 200:
                    result = await response.json()
                    if result.get("Success", False):
                        _LOGGER.info("Successfully sent control command")
                        return True
                    else:
                        _LOGGER.error("Control command failed: %s", result.get("ErrorMessage"))
                        return False
                else:
                    _LOGGER.error(
                        "Failed to send control command: %s", response.status
                    )
                    return False
        except Exception as err:
            _LOGGER.error("Error sending control command: %s", err)
            return False

    async def power_on(self, sauna_id: str, pin: str | None = None) -> bool:
        """Turn on the sauna."""
        control_data = {
            "pin": pin or "",
            "time_selected": False,
            "sel_hour": 0,
            "sel_min": 0
        }
        return await self.set_sauna_control(sauna_id, API_START_CABIN_ENDPOINT, control_data)

    async def power_off(self, sauna_id: str) -> bool:
        """Turn off the sauna."""
        return await self.set_sauna_control(sauna_id, API_STOP_CABIN_ENDPOINT, {})

    async def set_temperature(
        self, sauna_id: str, temperature: int, mode: int
    ) -> bool:
        """Set target temperature."""
        control_data = {"temp": temperature}
        return await self.set_sauna_control(sauna_id, API_CHANGE_TEMPERATURE_ENDPOINT, control_data)

    async def set_humidity(self, sauna_id: str, humidity_level: int) -> bool:
        """Set humidity level (SANARIUM only)."""
        control_data = {"level": humidity_level}
        return await self.set_sauna_control(sauna_id, API_CHANGE_HUM_LEVEL_ENDPOINT, control_data)

    async def set_mode(self, sauna_id: str, mode: int) -> bool:
        """Set sauna mode (Sauna/SANARIUM/IR)."""
        control_data = {"mode": mode}
        return await self.set_sauna_control(sauna_id, API_SET_MODE_ENDPOINT, control_data)

    async def set_start_time(self, sauna_id: str, hour: int, minute: int) -> bool:
        """Set start time for sauna preheating."""
        control_data = {
            "hour": hour,
            "minute": minute,
        }
        return await self.set_sauna_control(sauna_id, API_SET_SELECTED_TIME_ENDPOINT, control_data)
