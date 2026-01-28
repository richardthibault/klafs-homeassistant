"""Climate platform for Klafs Sauna."""
from __future__ import annotations

import logging
from typing import Any

from homeassistant.components.climate import (
    ClimateEntity,
    ClimateEntityFeature,
    HVACMode,
)
from homeassistant.config_entries import ConfigEntry
from homeassistant.const import ATTR_TEMPERATURE, UnitOfTemperature
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from . import KlafsDataUpdateCoordinator
from .const import (
    DOMAIN,
    MODE_SANARIUM,
    MODE_SAUNA,
    TEMP_MAX_SANARIUM,
    TEMP_MAX_SAUNA,
    TEMP_MIN_SANARIUM,
    TEMP_MIN_SAUNA,
)

_LOGGER = logging.getLogger(__name__)


async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up Klafs climate entities."""
    coordinator: KlafsDataUpdateCoordinator = hass.data[DOMAIN][entry.entry_id]

    entities = []
    for sauna_id in coordinator.data:
        entities.append(KlafsSaunaClimate(coordinator, sauna_id))

    async_add_entities(entities)


class KlafsSaunaClimate(CoordinatorEntity, ClimateEntity):
    """Representation of a Klafs Sauna as a climate entity."""

    _attr_has_entity_name = True
    _attr_temperature_unit = UnitOfTemperature.CELSIUS
    _attr_supported_features = (
        ClimateEntityFeature.TARGET_TEMPERATURE | ClimateEntityFeature.TURN_ON | ClimateEntityFeature.TURN_OFF
    )
    _attr_hvac_modes = [HVACMode.OFF, HVACMode.HEAT]

    def __init__(
        self, coordinator: KlafsDataUpdateCoordinator, sauna_id: str
    ) -> None:
        """Initialize the climate entity."""
        super().__init__(coordinator)
        self._sauna_id = sauna_id
        self._attr_unique_id = f"{sauna_id}_climate"
        self._attr_name = "Sauna"

    @property
    def device_info(self):
        """Return device information."""
        sauna_name = self.coordinator.get_sauna_name(self._sauna_id)
        return {
            "identifiers": {(DOMAIN, self._sauna_id)},
            "name": f"Klafs {sauna_name}",
            "manufacturer": "Klafs",
            "model": "Sauna",
        }

    @property
    def current_temperature(self) -> float | None:
        """Return the current temperature."""
        if self._sauna_id in self.coordinator.data:
            return self.coordinator.data[self._sauna_id].get("currentTemperature")
        return None

    @property
    def target_temperature(self) -> float | None:
        """Return the target temperature."""
        if self._sauna_id not in self.coordinator.data:
            return None

        data = self.coordinator.data[self._sauna_id]
        if data.get("sanariumSelected"):
            return data.get("selectedSanariumTemperature")
        else:
            return data.get("selectedSaunaTemperature")

    @property
    def hvac_mode(self) -> HVACMode:
        """Return current HVAC mode."""
        if self._sauna_id in self.coordinator.data:
            is_on = self.coordinator.data[self._sauna_id].get("isPoweredOn", False)
            return HVACMode.HEAT if is_on else HVACMode.OFF
        return HVACMode.OFF

    @property
    def min_temp(self) -> float:
        """Return the minimum temperature."""
        if self._sauna_id in self.coordinator.data:
            data = self.coordinator.data[self._sauna_id]
            if data.get("sanariumSelected"):
                return TEMP_MIN_SANARIUM
        return TEMP_MIN_SAUNA

    @property
    def max_temp(self) -> float:
        """Return the maximum temperature."""
        if self._sauna_id in self.coordinator.data:
            data = self.coordinator.data[self._sauna_id]
            if data.get("sanariumSelected"):
                return TEMP_MAX_SANARIUM
        return TEMP_MAX_SAUNA

    async def async_set_temperature(self, **kwargs: Any) -> None:
        """Set new target temperature."""
        temperature = kwargs.get(ATTR_TEMPERATURE)
        if temperature is None:
            return

        data = self.coordinator.data[self._sauna_id]
        mode = MODE_SANARIUM if data.get("sanariumSelected") else MODE_SAUNA

        await self.coordinator.client.set_temperature(
            self._sauna_id, int(temperature), mode
        )
        await self.coordinator.async_request_refresh()

    async def async_set_hvac_mode(self, hvac_mode: HVACMode) -> None:
        """Set new HVAC mode."""
        if hvac_mode == HVACMode.HEAT:
            # Get PIN for this specific sauna
            pin = self.coordinator.get_sauna_pin(self._sauna_id)
            await self.coordinator.client.power_on(self._sauna_id, pin)
        elif hvac_mode == HVACMode.OFF:
            await self.coordinator.client.power_off(self._sauna_id)

        await self.coordinator.async_request_refresh()

    @property
    def extra_state_attributes(self) -> dict[str, Any]:
        """Return additional state attributes."""
        if self._sauna_id not in self.coordinator.data:
            return {}

        data = self.coordinator.data[self._sauna_id]
        attrs = {
            "is_connected": data.get("isConnected", False),
            "is_ready_for_use": data.get("isReadyForUse", False),
            "status_code": data.get("statusCode"),
            "current_humidity": data.get("currentHumidity"),
        }

        if data.get("sanariumSelected"):
            attrs["mode"] = "SANARIUM"
            attrs["humidity_level"] = data.get("selectedHumLevel")
        elif data.get("saunaSelected"):
            attrs["mode"] = "Sauna"
        elif data.get("irSelected"):
            attrs["mode"] = "Infrared"

        return attrs
