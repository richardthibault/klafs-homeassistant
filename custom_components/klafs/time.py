"""Time platform for Klafs Sauna."""
from __future__ import annotations

from datetime import time
import logging
from typing import Any

from homeassistant.components.time import TimeEntity
from homeassistant.config_entries import ConfigEntry
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
    """Set up Klafs time entities."""
    coordinator: KlafsDataUpdateCoordinator = hass.data[DOMAIN][entry.entry_id]

    entities = []
    for sauna_id in coordinator.data:
        entities.append(KlafsSaunaScheduledStartTime(coordinator, sauna_id))

    async_add_entities(entities)


class KlafsSaunaScheduledStartTime(CoordinatorEntity, TimeEntity):
    """Scheduled start time for Klafs Sauna."""

    _attr_has_entity_name = True
    _attr_icon = "mdi:clock-start"

    def __init__(
        self, coordinator: KlafsDataUpdateCoordinator, sauna_id: str
    ) -> None:
        """Initialize the time entity."""
        super().__init__(coordinator)
        self._sauna_id = sauna_id
        self._attr_unique_id = f"{sauna_id}_scheduled_start_time"
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
    def native_value(self) -> time | None:
        """Return the scheduled start time."""
        if self._sauna_id not in self.coordinator.data:
            return None

        data = self.coordinator.data[self._sauna_id]
        time_selected = data.get("timeSelected", False)
        
        if not time_selected:
            return None
        
        hour = data.get("selectedHour", 0)
        minute = data.get("selectedMinute", 0)
        
        return time(hour=hour, minute=minute)

    async def async_set_value(self, value: time) -> None:
        """Set the scheduled start time."""
        await self.coordinator.client.set_start_time(
            self._sauna_id, value.hour, value.minute, time_set=True
        )
        await self.coordinator.async_request_refresh()

    @property
    def extra_state_attributes(self) -> dict[str, Any]:
        """Return additional state attributes."""
        if self._sauna_id not in self.coordinator.data:
            return {}
        
        data = self.coordinator.data[self._sauna_id]
        return {
            "enabled": data.get("timeSelected", False),
        }
