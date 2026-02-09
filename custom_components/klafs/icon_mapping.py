"""Icon mapping for Klafs Sauna entities based on state."""
from __future__ import annotations

from typing import Any

# Icon mapping based on sauna state
ICON_MAP = {
    "off": "klafs:sauna-off",
    "heating": "klafs:sauna-heating",
    "ready": "klafs:sauna-ready",
    "on": "klafs:sauna",
    "disconnected": "mdi:cloud-off-outline",
    "unknown": "klafs:sauna",
}


def get_icon_for_state(data: dict[str, Any]) -> str:
    """
    Get the appropriate icon based on sauna state.
    
    Args:
        data: Dictionary containing sauna status data
        
    Returns:
        Icon string (e.g., "klafs:sauna-heating")
    """
    if not data:
        return ICON_MAP["unknown"]
    
    # Check connection status first
    if not data.get("isConnected", False):
        return ICON_MAP["disconnected"]
    
    # Check if ready for use
    if data.get("isReadyForUse", False):
        return ICON_MAP["ready"]
    
    # Check if heating
    if data.get("isPoweredOn", False):
        return ICON_MAP["heating"]
    
    # Default to off state
    return ICON_MAP["off"]


def get_icon_for_climate_state(hvac_mode: str, data: dict[str, Any]) -> str:
    """
    Get the appropriate icon for climate entity based on HVAC mode and state.
    
    Args:
        hvac_mode: Current HVAC mode ("off", "heat", etc.)
        data: Dictionary containing sauna status data
        
    Returns:
        Icon string (e.g., "klafs:sauna-heating")
    """
    if hvac_mode == "off":
        return ICON_MAP["off"]
    
    return get_icon_for_state(data)
