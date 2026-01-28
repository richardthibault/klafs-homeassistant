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
        """Return the icon."""
        if self._sauna_id not in self.coordinator.data:
            return "mdi:sauna"

        data = self.coordinator.data[self._sauna_id]
        if data.get("isReadyForUse"):
            return "mdi:check-circle"
        elif data.get("isPoweredOn"):
            return "mdi:fire"
        elif not data.get("isConnected"):
            return "mdi:cloud-off-outline"
        else:
            return "mdi:sauna"
