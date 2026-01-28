"""Config flow for Klafs Sauna integration."""
from __future__ import annotations

import logging
from typing import Any

import voluptuous as vol

from homeassistant import config_entries
from homeassistant.const import CONF_PASSWORD, CONF_USERNAME
from homeassistant.data_entry_flow import FlowResult
from homeassistant.helpers import config_validation as cv
from homeassistant.helpers.aiohttp_client import async_get_clientsession

from .api import KlafsApiClient
from .const import CONF_PIN, CONF_SAUNAS, DOMAIN

_LOGGER = logging.getLogger(__name__)

STEP_USER_DATA_SCHEMA = vol.Schema(
    {
        vol.Required(CONF_USERNAME): str,
        vol.Required(CONF_PASSWORD): str,
    }
)


class KlafsConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for Klafs Sauna."""

    VERSION = 1

    def __init__(self) -> None:
        """Initialize the config flow."""
        self._username: str | None = None
        self._password: str | None = None
        self._client: KlafsApiClient | None = None
        self._saunas: dict[str, Any] = {}
        self._selected_saunas: dict[str, dict[str, Any]] = {}

    async def async_step_user(
        self, user_input: dict[str, Any] | None = None
    ) -> FlowResult:
        """Handle the initial step - credentials."""
        errors: dict[str, str] = {}

        if user_input is not None:
            try:
                # Test the credentials
                session = async_get_clientsession(self.hass)
                self._client = KlafsApiClient(
                    user_input[CONF_USERNAME],
                    user_input[CONF_PASSWORD],
                    session,
                )

                if await self._client.login():
                    # Store credentials
                    self._username = user_input[CONF_USERNAME]
                    self._password = user_input[CONF_PASSWORD]

                    # Get list of saunas
                    self._saunas = await self._client.get_saunas()

                    if not self._saunas:
                        errors["base"] = "no_saunas"
                    else:
                        # Move to sauna selection step
                        return await self.async_step_select_saunas()
                else:
                    errors["base"] = "invalid_auth"
            except Exception:  # pylint: disable=broad-except
                _LOGGER.exception("Unexpected exception")
                errors["base"] = "unknown"

        return self.async_show_form(
            step_id="user",
            data_schema=STEP_USER_DATA_SCHEMA,
            errors=errors,
        )

    async def async_step_select_saunas(
        self, user_input: dict[str, Any] | None = None
    ) -> FlowResult:
        """Handle sauna selection step."""
        errors: dict[str, str] = {}

        if user_input is not None:
            # Get selected saunas
            selected_sauna_ids = user_input.get("saunas", [])
            
            if not selected_sauna_ids:
                errors["base"] = "no_sauna_selected"
            else:
                # Store selected saunas
                for sauna_id in selected_sauna_ids:
                    if sauna_id in self._saunas:
                        self._selected_saunas[sauna_id] = {
                            "name": self._saunas[sauna_id].get("name", sauna_id[:8]),
                            "pin": None,
                        }
                
                # Move to PIN configuration step
                return await self.async_step_configure_pins()

        # Build sauna selection schema
        sauna_options = {
            sauna_id: f"{data.get('name', sauna_id[:8])} ({sauna_id[:8]})"
            for sauna_id, data in self._saunas.items()
        }

        schema = vol.Schema(
            {
                vol.Required("saunas"): cv.multi_select(sauna_options),
            }
        )

        return self.async_show_form(
            step_id="select_saunas",
            data_schema=schema,
            errors=errors,
            description_placeholders={
                "num_saunas": str(len(self._saunas)),
            },
        )

    async def async_step_configure_pins(
        self, user_input: dict[str, Any] | None = None
    ) -> FlowResult:
        """Handle PIN configuration for selected saunas."""
        errors: dict[str, str] = {}

        if user_input is not None:
            # Store PINs for each sauna
            for sauna_id in self._selected_saunas:
                pin_key = f"pin_{sauna_id}"
                if pin_key in user_input and user_input[pin_key]:
                    self._selected_saunas[sauna_id]["pin"] = user_input[pin_key]

            # Create entry with all data
            await self.async_set_unique_id(self._username)
            self._abort_if_unique_id_configured()

            return self.async_create_entry(
                title=f"Klafs Sauna ({self._username})",
                data={
                    CONF_USERNAME: self._username,
                    CONF_PASSWORD: self._password,
                    CONF_SAUNAS: self._selected_saunas,
                },
            )

        # Build PIN configuration schema
        schema_dict = {}
        description_lines = []
        for sauna_id, sauna_data in self._selected_saunas.items():
            sauna_name = sauna_data["name"]
            schema_dict[vol.Optional(f"pin_{sauna_id}")] = str
            description_lines.append(f"• {sauna_name}")

        schema = vol.Schema(schema_dict)

        return self.async_show_form(
            step_id="configure_pins",
            data_schema=schema,
            errors=errors,
            description_placeholders={
                "sauna_list": "\n".join(description_lines),
            },
        )
