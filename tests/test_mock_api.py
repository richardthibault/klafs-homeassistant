"""Mock API for testing without real Klafs sauna."""
import asyncio
from unittest.mock import AsyncMock, MagicMock


class MockKlafsApiClient:
    """Mock Klafs API client for testing."""

    def __init__(self, username: str, password: str, session):
        """Initialize mock client."""
        self.username = username
        self.password = password
        self.session = session
        self.is_authenticated = False
        self._mock_saunas = {
            "364cc9db-86f1-49d1-86cd-f6ef9b20a490": {
                "name": "Sauna Test 1",
                "type": "SANARIUM"
            },
            "7a8b9c0d-1e2f-3g4h-5i6j-7k8l9m0n1o2p": {
                "name": "Sauna Test 2",
                "type": "Sauna"
            }
        }

    async def login(self) -> bool:
        """Mock login."""
        # Simuler un délai réseau
        await asyncio.sleep(0.1)
        
        # Accepter n'importe quel username/password pour les tests
        if self.username and self.password:
            self.is_authenticated = True
            return True
        return False

    async def get_saunas(self) -> dict:
        """Mock get saunas."""
        await asyncio.sleep(0.1)
        return self._mock_saunas

    async def get_sauna_status(self, sauna_id: str) -> dict:
        """Mock get sauna status."""
        await asyncio.sleep(0.1)
        
        # Retourner un statut fictif
        return {
            "saunaId": sauna_id,
            "saunaSelected": True,
            "sanariumSelected": False,
            "irSelected": False,
            "selectedSaunaTemperature": 85,
            "selectedSanariumTemperature": 60,
            "selectedIrTemperature": 50,
            "selectedHumLevel": 5,
            "selectedIrLevel": 3,
            "selectedHour": 18,
            "selectedMinute": 0,
            "isConnected": True,
            "isPoweredOn": False,
            "isReadyForUse": False,
            "currentTemperature": 22,
            "currentHumidity": 30,
            "statusCode": 0,
            "statusMessage": None,
            "showBathingHour": False,
            "bathingHours": 0,
            "bathingMinutes": 0,
            "currentHumidityStatus": 0,
            "currentTemperatureStatus": 0
        }

    async def set_sauna_control(self, sauna_id: str, control_data: dict) -> bool:
        """Mock set sauna control."""
        await asyncio.sleep(0.1)
        print(f"Mock: Setting control for {sauna_id}: {control_data}")
        return True

    async def power_on(self, sauna_id: str, pin: str | None = None) -> bool:
        """Mock power on."""
        await asyncio.sleep(0.1)
        print(f"Mock: Powering on {sauna_id} with PIN: {pin}")
        return True

    async def power_off(self, sauna_id: str) -> bool:
        """Mock power off."""
        await asyncio.sleep(0.1)
        print(f"Mock: Powering off {sauna_id}")
        return True

    async def set_temperature(self, sauna_id: str, temperature: int, mode: int) -> bool:
        """Mock set temperature."""
        await asyncio.sleep(0.1)
        print(f"Mock: Setting temperature for {sauna_id} to {temperature}°C (mode {mode})")
        return True

    async def set_humidity(self, sauna_id: str, humidity_level: int) -> bool:
        """Mock set humidity."""
        await asyncio.sleep(0.1)
        print(f"Mock: Setting humidity for {sauna_id} to level {humidity_level}")
        return True

    async def set_mode(self, sauna_id: str, mode: int) -> bool:
        """Mock set mode."""
        await asyncio.sleep(0.1)
        print(f"Mock: Setting mode for {sauna_id} to {mode}")
        return True

    async def set_start_time(self, sauna_id: str, hour: int, minute: int) -> bool:
        """Mock set start time."""
        await asyncio.sleep(0.1)
        print(f"Mock: Setting start time for {sauna_id} to {hour:02d}:{minute:02d}")
        return True


# Pour utiliser le mock dans l'intégration
# Remplacer dans custom_components/klafs/__init__.py:
# from .api import KlafsApiClient
# par:
# from tests.test_mock_api import MockKlafsApiClient as KlafsApiClient
