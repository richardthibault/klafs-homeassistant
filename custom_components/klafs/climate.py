"""Climate platform for Klafs Sauna."""
from __future__ import annotations

import logging
from typing import Any

from homeassistant.components.climate import (
    ClimateEntity,
    ClimateEntityFeature,
    HVACMode,
    PRESET_NONE,
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
    MODE_IR,
    TEMP_MAX_SANARIUM,
    TEMP_MAX_SAUNA,
    TEMP_MAX_IR,
    TEMP_MIN_SANARIUM,
    TEMP_MIN_SAUNA,
    TEMP_MIN_IR,
)
from .icon_mapping import get_icon_for_climate_state

_LOGGER = logging.getLogger(__name__)

# Preset modes
PRESET_SAUNA = "Sauna"
PRESET_SANARIUM = "SANARIUM"
PRESET_INFRARED = "Infrared"


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
    _attr_hvac_modes = [HVACMode.OFF, HVACMode.HEAT]

    def __init__(
        self, coordinator: KlafsDataUpdateCoordinator, sauna_id: str
    ) -> None:
        """Initialize the climate entity."""
        super().__init__(coordinator)
        self._sauna_id = sauna_id
        self._attr_unique_id = f"{sauna_id}_climate"
        self._attr_name = "Sauna"
        self._attr_min_humidity = 1
        self._attr_max_humidity = 10
        
        # Detect available preset modes based on sauna capabilities
        self._detect_available_modes()
    
    @property
    def supported_features(self) -> int:
        """Return the list of supported features."""
        features = (
            ClimateEntityFeature.TARGET_TEMPERATURE 
            | ClimateEntityFeature.TURN_ON 
            | ClimateEntityFeature.TURN_OFF
            | ClimateEntityFeature.PRESET_MODE
        )
        
        # Add humidity control only in SANARIUM mode
        if self.preset_mode == PRESET_SANARIUM:
            features |= ClimateEntityFeature.TARGET_HUMIDITY
        
        return features


    
    def _detect_available_modes(self) -> None:
        """Detect which preset modes are available on this sauna."""
        available_modes = [PRESET_SAUNA]  # Sauna mode is always available
        
        if self._sauna_id in self.coordinator.data:
            data = self.coordinator.data[self._sauna_id]
            
            # SANARIUM is available if selectedSanariumTemperature is reasonable (>= 40°C)
            sanarium_temp = data.get("selectedSanariumTemperature", 0)
            if sanarium_temp >= 40:
                available_modes.append(PRESET_SANARIUM)
            
            # Infrared is available if selectedIrTemperature is reasonable (>= 30°C)
            ir_temp = data.get("selectedIrTemperature", 0)
            if ir_temp >= 30:
                available_modes.append(PRESET_INFRARED)
        
        self._attr_preset_modes = available_modes
        _LOGGER.debug(
            "Detected available modes for sauna %s: %s", 
            self._sauna_id[:8], 
            available_modes
        )

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
        if self._sauna_id not in self.coordinator.data:
            return None
        
        data = self.coordinator.data[self._sauna_id]
        temp = data.get("currentTemperature")
        
        # Filter out invalid temperature values
        # When sauna is off, API returns 141°C (sentinel value)
        # Return None so HA displays "--" instead of invalid temperature
        if temp is None or temp > 120:
            return None
        
        return temp

    @property
    def target_temperature(self) -> float | None:
        """Return the target temperature."""
        if self._sauna_id not in self.coordinator.data:
            return None

        data = self.coordinator.data[self._sauna_id]
        
        # Return the temperature for the current mode
        if data.get("sanariumSelected"):
            return data.get("selectedSanariumTemperature")
        elif data.get("irSelected"):
            # IR mode uses sauna temperature field
            return data.get("selectedSaunaTemperature")
        else:
            return data.get("selectedSaunaTemperature")

    @property
    def current_humidity(self) -> int | None:
        """Return the current humidity (only in SANARIUM mode)."""
        if self._sauna_id not in self.coordinator.data:
            return None
        
        data = self.coordinator.data[self._sauna_id]
        
        # Only return humidity in SANARIUM mode
        if data.get("sanariumSelected"):
            return data.get("currentHumidity")
        
        return None

    @property
    def target_humidity(self) -> int | None:
        """Return the target humidity (only in SANARIUM mode)."""
        if self._sauna_id not in self.coordinator.data:
            return None
        
        data = self.coordinator.data[self._sauna_id]
        
        # Only return humidity in SANARIUM mode
        if data.get("sanariumSelected"):
            return data.get("selectedHumLevel")
        
        return None

    @property
    def hvac_mode(self) -> HVACMode:
        """Return current HVAC mode."""
        if self._sauna_id in self.coordinator.data:
            is_on = self.coordinator.data[self._sauna_id].get("isPoweredOn", False)
            return HVACMode.HEAT if is_on else HVACMode.OFF
        return HVACMode.OFF

    @property
    def preset_mode(self) -> str | None:
        """Return the current preset mode."""
        if self._sauna_id not in self.coordinator.data:
            return PRESET_SAUNA
        
        data = self.coordinator.data[self._sauna_id]
        if data.get("sanariumSelected"):
            return PRESET_SANARIUM
        elif data.get("irSelected"):
            return PRESET_INFRARED
        else:
            return PRESET_SAUNA

    @property
    def min_temp(self) -> float:
        """Return the minimum temperature."""
        preset = self.preset_mode
        if preset == PRESET_SANARIUM:
            return TEMP_MIN_SANARIUM
        elif preset == PRESET_INFRARED:
            return TEMP_MIN_IR
        return TEMP_MIN_SAUNA

    @property
    def max_temp(self) -> float:
        """Return the maximum temperature."""
        preset = self.preset_mode
        if preset == PRESET_SANARIUM:
            return TEMP_MAX_SANARIUM
        elif preset == PRESET_INFRARED:
            return TEMP_MAX_IR
        return TEMP_MAX_SAUNA

    async def async_set_temperature(self, **kwargs: Any) -> None:
        """Set new target temperature."""
        temperature = kwargs.get(ATTR_TEMPERATURE)
        if temperature is None:
            return

        # Clamp temperature to current mode limits
        temperature = max(self.min_temp, min(self.max_temp, temperature))

        # Determine mode from current preset
        preset = self.preset_mode
        if preset == PRESET_SANARIUM:
            mode = MODE_SANARIUM
        elif preset == PRESET_INFRARED:
            mode = MODE_IR
        else:
            mode = MODE_SAUNA

        await self.coordinator.client.set_temperature(
            self._sauna_id, int(temperature), mode
        )
        # Force immediate refresh
        await self.coordinator.async_refresh()

    async def async_set_humidity(self, humidity: int) -> None:
        """Set new target humidity (SANARIUM mode only)."""
        # Clamp humidity to valid range (1-10)
        humidity = max(1, min(10, humidity))
        
        await self.coordinator.client.set_humidity(self._sauna_id, humidity)
        # Force immediate refresh
        await self.coordinator.async_refresh()

    async def async_set_preset_mode(self, preset_mode: str) -> None:
        """Set new preset mode (Sauna/SANARIUM/Infrared)."""
        if preset_mode == PRESET_SANARIUM:
            mode = MODE_SANARIUM
        elif preset_mode == PRESET_INFRARED:
            mode = MODE_IR
        else:
            mode = MODE_SAUNA

        # Change mode on the sauna
        await self.coordinator.client.set_mode(self._sauna_id, mode)
        
        # Force immediate refresh to update UI quickly
        await self.coordinator.async_refresh()
        
        # The API automatically restores the preferred temperature for each mode
        # selectedSaunaTemperature is used for Sauna and IR modes
        # selectedSanariumTemperature is used for SANARIUM mode
        # No need to manually adjust temperature - the sauna remembers each mode's setting

    async def async_set_hvac_mode(self, hvac_mode: HVACMode) -> None:
        """Set new HVAC mode."""
        if hvac_mode == HVACMode.HEAT:
            # Get PIN for this specific sauna
            pin = self.coordinator.get_sauna_pin(self._sauna_id)
            await self.coordinator.client.power_on(self._sauna_id, pin)
        elif hvac_mode == HVACMode.OFF:
            await self.coordinator.client.power_off(self._sauna_id)

        # Force immediate refresh
        await self.coordinator.async_refresh()

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
        }

        # Add temperature status message when sauna is off
        raw_temp = data.get("currentTemperature")
        is_powered_on = data.get("isPoweredOn", False)
        if not is_powered_on and raw_temp is not None and raw_temp > 120:
            attrs["temperature_info"] = "Sauna must be powered on to read current temperature"
        
        # Add scheduled start time if configured
        time_selected = data.get("timeSelected", False)
        if time_selected:
            hour = data.get("selectedHour", 0)
            minute = data.get("selectedMinute", 0)
            attrs["scheduled_start_time"] = f"{hour:02d}:{minute:02d}"
            attrs["scheduled_start_enabled"] = True
        else:
            attrs["scheduled_start_enabled"] = False
        
        # Add humidity level ONLY for SANARIUM mode
        if data.get("sanariumSelected"):
            attrs["current_humidity"] = data.get("currentHumidity")
            attrs["humidity_level"] = data.get("selectedHumLevel")
            attrs["target_humidity"] = data.get("selectedHumLevel")

        return attrs
    
    @property
    def icon(self) -> str:
        """Return the icon based on HVAC mode and state."""
        if self._sauna_id not in self.coordinator.data:
            return "klafs:sauna"
        
        data = self.coordinator.data[self._sauna_id]
        return get_icon_for_climate_state(self.hvac_mode, data)
