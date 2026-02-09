# Klafs Sauna Integration for Home Assistant

**Read this in other languages:** **English** | [Français](README.fr.md) | [Deutsch](README.de.md) | [Español](README.es.md)

[![hacs_badge](https://img.shields.io/badge/HACS-Custom-orange.svg)](https://github.com/custom-components/hacs)
[![GitHub release](https://img.shields.io/github/release/richardthibault/klafs-homeassistant.svg)](https://github.com/richardthibault/klafs-homeassistant/releases)
[![License](https://img.shields.io/github/license/richardthibault/klafs-homeassistant.svg)](LICENSE)

This custom integration allows you to control your Klafs sauna via Home Assistant using the Klafs cloud API.

![Klafs Sauna](https://www.klafs.com/typo3conf/ext/klafs_sitepackage/Resources/Public/Images/logo.svg)

## Features

- **Climate Control**: Control your sauna temperature like a thermostat
- **Sensors**: Monitor temperature, humidity and status in real-time
- **Modes**: Switch between Sauna and SANARIUM® modes
- **Power On/Off**: Control your sauna power remotely
- **Multi-sauna Support**: Manage multiple saunas from a single account
- **Individual PINs**: Each sauna can have its own PIN code

## Prerequisites

- A Klafs Sauna App account
- A Klafs sauna equipped with Wi-Fi module and "KLAFS Sauna App" option
- Home Assistant 2023.1 or higher

## Installation

### Installation via HACS (Recommended)

1. Open HACS in Home Assistant
2. Go to "Integrations"
3. Click the three dots in the top right
4. Select "Custom repositories"
5. Add URL: `https://github.com/richardthibault/klafs-homeassistant`
6. Search for "Klafs Sauna" and install
7. Restart Home Assistant
8. Configure the integration via the user interface

### Manual Installation

1. Copy the `custom_components/klafs` folder to your `config/custom_components/` folder
2. Restart Home Assistant
3. Go to Configuration > Integrations
4. Click "+ Add Integration"
5. Search for "Klafs Sauna"
6. Enter your Klafs Sauna App credentials

## Configuration

The integration is fully configured via the Home Assistant user interface in 3 steps:

### Step 1: Credentials
- **Username**: Your Klafs Sauna App username
- **Password**: Your Klafs Sauna App password

### Step 2: Sauna Selection
- Select the saunas you want to control via Home Assistant
- You can select one or multiple saunas
- Each sauna will appear as a separate device

### Step 3: PIN Codes
- **PIN Code** (optional): The 4-digit PIN code configured on each sauna
- A different PIN can be configured for each sauna
- Required to turn on the sauna remotely

⚠️ **Important**: 
- Klafs blocks the account after 3 failed login attempts. Make sure to enter the correct credentials.
- Each PIN code must be configured on the corresponding sauna via its control panel before use.
- Without a PIN, you can see the sauna status but cannot turn it on remotely.
- If you have multiple saunas, each can have its own PIN code.

## Created Entities

For each detected sauna, the integration creates:

### Climate (Thermostat)
- **Entity**: `climate.klafs_sauna_XXXXXXXX`
- **Functions**: Temperature control, power on/off
- **Attributes**:
  - Current mode (Sauna/SANARIUM®/Infrared)
  - Connection status
  - Ready for use
  - Humidity level (SANARIUM® only)

### Sensors
- **Temperature**: `sensor.klafs_sauna_XXXXXXXX_temperature`
- **Humidity**: `sensor.klafs_sauna_XXXXXXXX_humidity`
- **Status**: `sensor.klafs_sauna_XXXXXXXX_status` (Off/Heating/Ready/Disconnected)

### Switch
- **SANARIUM® Mode**: `switch.klafs_sauna_XXXXXXXX_sanarium_mode`

## Usage

### Basic Control

```yaml
# Turn on sauna at 80°C (uses configured PIN)
service: climate.set_temperature
target:
  entity_id: climate.klafs_sauna_XXXXXXXX
data:
  temperature: 80
  hvac_mode: heat

# Turn on with specific PIN
service: klafs.power_on_with_pin
target:
  entity_id: climate.klafs_sauna_XXXXXXXX
data:
  pin: "1234"

# Turn off sauna
service: climate.turn_off
target:
  entity_id: climate.klafs_sauna_XXXXXXXX

# Set humidity level (SANARIUM only)
service: klafs.set_humidity_level
target:
  entity_id: climate.klafs_sauna_XXXXXXXX
data:
  humidity_level: 7

# Schedule start time
service: klafs.set_start_time
target:
  entity_id: climate.klafs_sauna_XXXXXXXX
data:
  hour: 18
  minute: 30
```

### Automations

See [EXAMPLES.md](EXAMPLES.md) for more automation examples and Lovelace cards.

## Complete Documentation

- 📖 [Quick Start Guide](QUICK_START.md)
- 🔧 [Detailed Installation Guide](INSTALLATION.md)
- 💡 [Automation Examples](EXAMPLES.md)
- 🔍 [API Documentation](API_DOCUMENTATION.md)
- 🐛 [Troubleshooting Guide](TROUBLESHOOTING.md)
- 🏗️ [Multi-sauna Support](MULTI_SAUNA_SUPPORT.md)
- 🤝 [Contributing Guide](CONTRIBUTING.md)

## Klafs API

This integration uses the Klafs web API (ASP.NET MVC application):

- **Base URL**: `https://sauna-app.klafs.com`
- **Authentication**: Cookie-based after login
- **Polling**: Updates every 60 seconds by default

## Temperature Limits

- **Sauna Mode**: 10°C - 100°C
- **SANARIUM® Mode**: 40°C - 75°C
- **Infrared Mode**: 30°C - 100°C

## Troubleshooting

### Integration won't connect

1. Verify your credentials in the Klafs Sauna App
2. Make sure your account is not blocked (3 attempts max)
3. Check Home Assistant logs: `Configuration > Logs`

### Sauna doesn't appear

1. Make sure your sauna is properly configured in the Klafs app
2. Verify the Wi-Fi module is connected
3. Restart the integration

### Commands don't work

1. Verify the sauna is connected (`isConnected: true`)
2. Make sure you have configured a PIN code on your sauna
3. Check that the sauna door has been controlled

For more help, see the [Troubleshooting Guide](TROUBLESHOOTING.md).

## Contributing

Contributions are welcome! Feel free to:

- Report bugs
- Suggest new features
- Submit pull requests

See [CONTRIBUTING.md](CONTRIBUTING.md) for more details.

## License

MIT License - See [LICENSE](LICENSE)

## Credits

- Based on API research by the OpenHAB community
- Inspired by the [IPSymconKlafsSaunaControl](https://github.com/Pommespanzer/IPSymconKlafsSaunaControl) project

## Disclaimer

This integration is unofficial and not affiliated with Klafs GmbH. Use at your own risk.
