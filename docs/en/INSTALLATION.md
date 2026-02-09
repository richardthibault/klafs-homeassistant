# Installation Guide - Klafs Sauna Integration

**Read in other languages:** **English** | [Français](../fr/INSTALLATION.md) | [Deutsch](../de/INSTALLATION.md) | [Español](../es/INSTALLATION.md)

## Method 1: Manual Installation

### Step 1: Copy Files

1. Download or clone this repository
2. Copy the `custom_components/klafs` folder to your Home Assistant configuration folder:
   ```
   <config>/custom_components/klafs/
   ```

### Step 2: Restart Home Assistant

Restart Home Assistant to load the new integration.

### Step 3: Add Integration

1. Go to **Settings** > **Devices & Services**
2. Click **+ Add Integration**
3. Search for **"Klafs Sauna"**
4. Follow the on-screen instructions

## Method 2: Installation via HACS (Recommended)

### Prerequisites

- HACS must be installed in your Home Assistant
- If not, follow the [HACS installation guide](https://hacs.xyz/docs/setup/download)

### Step 1: Add Custom Repository

1. Open **HACS** in Home Assistant
2. Click on **Integrations**
3. Click the **three dots** in the top right
4. Select **Custom repositories**
5. Add URL: `https://github.com/richardthibault/klafs-homeassistant`
6. Select category: **Integration**
7. Click **Add**

### Step 2: Install Integration

1. Search for **"Klafs Sauna"** in HACS
2. Click **Download**
3. Restart Home Assistant

### Step 3: Configure Integration

1. Go to **Settings** > **Devices & Services**
2. Click **+ Add Integration**
3. Search for **"Klafs Sauna"**
4. **Step 1**: Enter your credentials
   - **Username**: Your Klafs email
   - **Password**: Your Klafs password
5. **Step 2**: Select saunas
   - Check the saunas you want to control
   - You can select one or multiple
6. **Step 3**: Configure PIN codes (optional)
   - Enter the PIN code for each selected sauna
   - Leave empty if you don't want to turn on the sauna remotely

## Configuration

### Required Credentials

You will need your **Klafs Sauna App** credentials:

- Email/username
- Password

⚠️ **Warning**: Klafs automatically blocks your account after 3 failed login attempts. Make sure to enter the correct credentials the first time.

### Configuration Verification

After adding the integration, you should see:

1. A new **Klafs Sauna** integration in your integrations
2. One or more devices corresponding to your saunas
3. Entities for each sauna:
   - `climate.klafs_sauna_XXXXXXXX` (thermostat)
   - `sensor.klafs_sauna_XXXXXXXX_temperature`
   - `sensor.klafs_sauna_XXXXXXXX_humidity`
   - `sensor.klafs_sauna_XXXXXXXX_status`
   - `switch.klafs_sauna_XXXXXXXX_sanarium_mode`

## Troubleshooting

### Integration doesn't appear

1. Verify files are in `<config>/custom_components/klafs/`
2. Check logs: **Settings** > **System** > **Logs**
3. Restart Home Assistant in safe mode to check for errors

### "Invalid credentials" error

1. Verify your credentials in the Klafs Sauna App
2. Make sure your account is not blocked
3. Try logging in at https://sauna-app.klafs.com

### Sauna not detected

1. Verify your sauna is properly configured in the Klafs app
2. Make sure the Wi-Fi module is connected and functional
3. Remove and re-add the integration

### Commands don't work

1. Verify the status sensor shows "Connected"
2. Make sure you have configured a PIN code on your sauna
3. Check that the sauna door has been controlled (safety)

## Updates

### Via HACS

1. Open HACS
2. Go to **Integrations**
3. Search for **Klafs Sauna**
4. Click **Update** if available
5. Restart Home Assistant

### Manually

1. Download the latest version
2. Replace the `custom_components/klafs/` folder
3. Restart Home Assistant

## Support

For help:

1. Check the [README.md](../../README.md) for complete documentation
2. Check [GitHub issues](https://github.com/richardthibault/klafs-homeassistant/issues)
3. Create a new issue if necessary

## Next Steps

Once installation is complete, check the [README.md](../../README.md) for:

- Automation examples
- Lovelace cards
- Advanced use cases
