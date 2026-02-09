"""Sensor platform for Klafs Sauna."""
from __future__ import annotations

import logging

from homeassistant.components.sensor import (
    SensorDeviceClass,
    SensorEntity,
    SensorStateClass,
)
from homeassistant.config_entries import ConfigEntry
from homeassistant.const import PERCENTAGE, UnitOfTemperature
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from . import KlafsDataUpdateCoordinator
from .const import DOMAIN
from .icon_mapping import get_icon_for_state

_LOGGER = logging.getLogger(__name__)


async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up Klafs sensor entities."""
    coordinator: KlafsDataUpdateCoordinator = hass.data[DOMAIN][entry.entry_id]

    entities = []
    for sauna_id in coordinator.data:
        entities.extend(
            [
                KlafsSaunaTemperatureSensor(coordinator, sauna_id),
                KlafsSaunaHumiditySensor(coordinator, sauna_id),
                KlafsSaunaStatusSensor(coordinator, sauna_id),
                KlafsSaunaScheduledStartTimeSensor(coordinator, sauna_id),
            ]
        )

    async_add_entities(entities)


class KlafsSaunaTemperatureSensor(CoordinatorEntity, SensorEntity):
    """Temperature sensor for Klafs Sauna."""

    _attr_has_entity_name = True
    _attr_device_class = SensorDeviceClass.TEMPERATURE
    _attr_state_class = SensorStateClass.MEASUREMENT
    _attr_native_unit_of_measurement = UnitOfTemperature.CELSIUS

    def __init__(
        self, coordinator: KlafsDataUpdateCoordinator, sauna_id: str
    ) -> None:
        """Initialize the sensor."""
        super().__init__(coordinator)
        self._sauna_id = sauna_id
        self._attr_unique_id = f"{sauna_id}_temperature"
        self._attr_name = "Temperature"

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
    def native_value(self) -> float | None:
        """Return the current temperature."""
        if self._sauna_id in self.coordinator.data:
            return self.coordinator.data[self._sauna_id].get("currentTemperature")
        return None


class KlafsSaunaHumiditySensor(CoordinatorEntity, SensorEntity):
    """Humidity sensor for Klafs Sauna."""

    _attr_has_entity_name = True
    _attr_device_class = SensorDeviceClass.HUMIDITY
    _attr_state_class = SensorStateClass.MEASUREMENT
    _attr_native_unit_of_measurement = PERCENTAGE

    def __init__(
        self, coordinator: KlafsDataUpdateCoordinator, sauna_id: str
    ) -> None:
        """Initialize the sensor."""
        super().__init__(coordinator)
        self._sauna_id = sauna_id
        self._attr_unique_id = f"{sauna_id}_humidity"
        self._attr_name = "Humidity"

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
    def native_value(self) -> int | None:
        """Return the current humidity."""
        if self._sauna_id in self.coordinator.data:
            return self.coordinator.data[self._sauna_id].get("currentHumidity")
        return None


class KlafsSaunaStatusSensor(CoordinatorEntity, SensorEntity):
    """Status sensor for Klafs Sauna."""

    _attr_has_entity_name = True

    def __init__(
        self, coordinator: KlafsDataUpdateCoordinator, sauna_id: str
    ) -> None:
        """Initialize the sensor."""
        super().__init__(coordinator)
        self._sauna_id = sauna_id
        self._attr_unique_id = f"{sauna_id}_status"
        self._attr_name = "Status"

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
    def native_value(self) -> str | None:
        """Return the status."""
        if self._sauna_id not in self.coordinator.data:
            return None

        data = self.coordinator.data[self._sauna_id]
        if data.get("isReadyForUse"):
            return "Ready"
        elif data.get("isPoweredOn"):
            return "Heating"
        elif not data.get("isConnected"):
            return "Disconnected"
        else:
            return "Off"

    @property
    def icon(self) -> str:
        """Return the icon based on sauna state."""
        if self._sauna_id not in self.coordinator.data:
            return "klafs:sauna"

        data = self.coordinator.data[self._sauna_id]
        return get_icon_for_state(data)
    
    @property
    def extra_state_attributes(self) -> dict[str, str]:
        """Return additional state attributes."""
        if self._sauna_id not in self.coordinator.data:
            return {}
        
        data = self.coordinator.data[self._sauna_id]
        return {
            "raw_state": self.native_value,
            "is_connected": data.get("isConnected", False),
            "is_powered_on": data.get("isPoweredOn", False),
            "is_ready": data.get("isReadyForUse", False),
        }



class KlafsSaunaScheduledStartTimeSensor(CoordinatorEntity, SensorEntity):
    """Scheduled start time sensor for Klafs Sauna."""

    _attr_has_entity_name = True
    _attr_icon = "mdi:clock-start"

    def __init__(
        self, coordinator: KlafsDataUpdateCoordinator, sauna_id: str
    ) -> None:
        """Initialize the sensor."""
        super().__init__(coordinator)
        self._sauna_id = sauna_id
        self._attr_unique_id = f"{sauna_id}_scheduled_start_time_sensor"
        self._attr_name = "Scheduled Start Time"

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
    def native_value(self) -> str | None:
        """Return the scheduled start time."""
        if self._sauna_id not in self.coordinator.data:
            return None

        data = self.coordinator.data[self._sauna_id]
        time_selected = data.get("timeSelected", False)
        
        if not time_selected:
            return "Not scheduled"
        
        hour = data.get("selectedHour", 0)
        minute = data.get("selectedMinute", 0)
        return f"{hour:02d}:{minute:02d}"

    @property
    def extra_state_attributes(self) -> dict[str, any]:
        """Return additional state attributes."""
        if self._sauna_id not in self.coordinator.data:
            return {}
        
        data = self.coordinator.data[self._sauna_id]
        return {
            "enabled": data.get("timeSelected", False),
            "hour": data.get("selectedHour", 0),
            "minute": data.get("selectedMinute", 0),
        }
