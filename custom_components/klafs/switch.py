"""Switch platform for Klafs Sauna."""
from __future__ import annotations

import logging
from typing import Any

from homeassistant.components.switch import SwitchEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from . import KlafsDataUpdateCoordinator
from .const import DOMAIN, MODE_SANARIUM, MODE_SAUNA

_LOGGER = logging.getLogger(__name__)


async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up Klafs switch entities."""
    coordinator: KlafsDataUpdateCoordinator = hass.data[DOMAIN][entry.entry_id]

    entities = []
    for sauna_id in coordinator.data:
        entities.append(KlafsSaunaModeSwitch(coordinator, sauna_id))

    async_add_entities(entities)


class KlafsSaunaModeSwitch(CoordinatorEntity, SwitchEntity):
    """Switch to toggle between Sauna and SANARIUM mode."""

    _attr_has_entity_name = True

    def __init__(
        self, coordinator: KlafsDataUpdateCoordinator, sauna_id: str
    ) -> None:
        """Initialize the switch."""
        super().__init__(coordinator)
        self._sauna_id = sauna_id
        self._attr_unique_id = f"{sauna_id}_sanarium_mode"
        self._attr_name = "SANARIUM Mode"
        self._attr_icon = "mdi:water-percent"

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
    def is_on(self) -> bool:
        """Return true if SANARIUM mode is enabled."""
        if self._sauna_id in self.coordinator.data:
            return self.coordinator.data[self._sauna_id].get("sanariumSelected", False)
        return False

    async def async_turn_on(self, **kwargs: Any) -> None:
        """Turn on SANARIUM mode."""
        await self.coordinator.client.set_mode(self._sauna_id, MODE_SANARIUM)
        await self.coordinator.async_request_refresh()

    async def async_turn_off(self, **kwargs: Any) -> None:
        """Turn off SANARIUM mode (switch to Sauna mode)."""
        await self.coordinator.client.set_mode(self._sauna_id, MODE_SAUNA)
        await self.coordinator.async_request_refresh()
