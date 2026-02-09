**Read in other languages:** [English](../en/TROUBLESHOOTING.md) | [Français](../../TROUBLESHOOTING.md) | [Deutsch](../de/TROUBLESHOOTING.md) | [Español](../es/TROUBLESHOOTING.md)

# Troubleshooting Guide - Klafs Sauna

## Authentication Issues

### "Invalid credentials" Error

**Symptoms:**
- Error message during configuration
- Unable to add the integration

**Solutions:**

1. **Verify credentials**
   - Test your credentials at https://sauna-app.klafs.com
   - Make sure there are no leading/trailing spaces
   - Check uppercase/lowercase letters

2. **Account locked**
   - Klafs locks accounts after 3 failed attempts
   - Wait 30 minutes or contact Klafs support
   - Reset your password if necessary

3. **Check logs**
   ```
   Configuration > Logs
   Search for: "klafs"
   ```

### Session Expired

**Symptoms:**
- Integration was working then stops
- 401 error in logs

**Solutions:**
- The integration automatically reconnects
- If the problem persists, reload the integration:
  ```
  Configuration > Integrations > Klafs > Reload
  ```

## Discovery Issues

### No Sauna Detected

**Symptoms:**
- Integration installs but no entities appear
- "No devices found" message

**Solutions:**

1. **Check Klafs configuration**
   - Open the Klafs Sauna App
   - Verify your sauna appears
   - Make sure the Wi-Fi module is connected

2. **Check sauna connection**
   - The sauna's Wi-Fi indicator should be lit
   - Test control from the mobile app
   - Restart the Wi-Fi module if necessary

3. **Reload the integration**
   ```
   Configuration > Integrations > Klafs > Reload
   ```

4. **Remove and reinstall**
   ```
   Configuration > Integrations > Klafs > Remove
   Then reinstall the integration
   ```

### Sauna Shows as "Disconnected"

**Symptoms:**
- Entities created but status shows "Disconnected"
- `isConnected: false` in attributes

**Solutions:**

1. **Check Wi-Fi module**
   - Restart the sauna's Wi-Fi module
   - Verify the sauna's network connection
   - Make sure the sauna has Internet access

2. **Check in Klafs app**
   - If disconnected in the app, the issue is with the sauna
   - Follow Klafs instructions to reconnect

3. **Wait for synchronization**
   - Can take up to 5 minutes
   - Integration polls every 60 seconds

## Control Issues

### Unable to Turn On Sauna

**Symptoms:**
- Power button doesn't work
- Error in logs

**Solutions:**

1. **Check PIN code**
   - Is the PIN configured in the integration?
   - Does the PIN match the sauna's PIN?
   - Reconfigure the integration with the correct PIN:
     ```
     Configuration > Integrations > Klafs > Configure
     ```

2. **Check door control**
   - Klafs sauna requires door control
   - Open and close the sauna door
   - Check the door sensor

3. **Use service with PIN**
   ```yaml
   service: klafs.power_on_with_pin
   target:
     entity_id: climate.klafs_sauna
   data:
     pin: "1234"
   ```

4. **Check status**
   - Sauna must be connected (`isConnected: true`)
   - Verify there are no errors on the sauna

### Temperature Changes Don't Work

**Symptoms:**
- Temperature doesn't change
- No error but no effect

**Solutions:**

1. **Check limits**
   - Sauna mode: 10-100°C
   - SANARIUM mode: 40-75°C
   - IR mode: 30-100°C

2. **Check active mode**
   - Temperature must match the mode
   - Change mode if necessary

3. **Wait for synchronization**
   - Changes can take 1-2 minutes
   - Klafs API has propagation delay

4. **Check logs**
   ```
   Configuration > Logs
   Level: Debug
   Search for: "klafs"
   ```

### SANARIUM Mode Doesn't Work

**Symptoms:**
- SANARIUM switch doesn't do anything
- No humidity option

**Solutions:**

1. **Check compatibility**
   - Your sauna must have the SANARIUM option
   - Check in the Klafs app

2. **Check attributes**
   ```yaml
   # In Developer Tools > States
   climate.klafs_sauna
   # Attributes:
   sanariumSelected: true/false
   ```

3. **Use the service**
   ```yaml
   service: klafs.set_humidity_level
   target:
     entity_id: climate.klafs_sauna
   data:
     humidity_level: 7
   ```

## Performance Issues

### Slow Updates

**Symptoms:**
- Changes take time to appear
- Delay between action and update

**Explanation:**
- Integration polls every 60 seconds
- Klafs API has propagation delay
- This is normal and by design

**Solutions:**
- Reduce interval (not recommended):
  ```python
  # In custom_components/klafs/__init__.py
  SCAN_INTERVAL = timedelta(seconds=30)  # Instead of 60
  ```
- Accept the delay (recommended)

### Timeout Errors

**Symptoms:**
- "Timeout" errors in logs
- Entities become "unavailable"

**Solutions:**

1. **Check Internet connection**
   - Test Home Assistant's connection
   - Check DNS

2. **Check Klafs API**
   - Test https://sauna-app.klafs.com
   - May be under maintenance

3. **Increase timeout**
   ```python
   # In custom_components/klafs/api.py
   async with self.session.post(..., timeout=30) as response:
   ```

## Installation Issues

### Integration Doesn't Appear

**Symptoms:**
- No "Klafs Sauna" in integrations list

**Solutions:**

1. **Check installation**
   ```
   config/custom_components/klafs/
   ├── __init__.py
   ├── manifest.json
   ├── config_flow.py
   ├── ...
   ```

2. **Check permissions**
   - Files must be readable by Home Assistant
   - On Linux: `chmod -R 755 custom_components/klafs`

3. **Check startup logs**
   ```
   Configuration > Logs
   Search for: "klafs" or "custom_components"
   ```

4. **Restart in safe mode**
   ```
   Configuration > System > Restart in Safe Mode
   ```

5. **Check manifest.json**
   - Must be valid JSON
   - Verify with a JSON validator

### "Version required" Error

**Symptoms:**
- Error message at startup
- Integration doesn't load

**Solution:**
- Verify that `manifest.json` contains:
  ```json
  {
    "version": "1.0.0"
  }
  ```

## Advanced Debugging

### Enable Detailed Logs

Add to `configuration.yaml`:

```yaml
logger:
  default: info
  logs:
    custom_components.klafs: debug
    custom_components.klafs.api: debug
```

Then restart Home Assistant.

### Test API Manually

```bash
# Login
curl -c cookie.txt -X POST https://sauna-app.klafs.com/Account/Login \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "UserName=YOUR_EMAIL&Password=YOUR_PASSWORD"

# Get status
curl -b cookie.txt -X POST https://sauna-app.klafs.com/Control/GetSaunaStatus \
  -H "Content-Type: application/json" \
  -d '{"saunaId":"YOUR_SAUNA_ID"}'
```

### Check Entities

In Developer Tools > States:

```
climate.klafs_sauna_XXXXXXXX
sensor.klafs_sauna_XXXXXXXX_temperature
sensor.klafs_sauna_XXXXXXXX_humidity
sensor.klafs_sauna_XXXXXXXX_status
switch.klafs_sauna_XXXXXXXX_sanarium_mode
```

### Inspect Attributes

```yaml
# Developer Tools > States
# Select: climate.klafs_sauna

# Important attributes:
is_connected: true/false
is_ready_for_use: true/false
status_code: 0/1/2/3
mode: "Sauna" / "SANARIUM" / "Infrared"
```

## Known Issues

### 1. Update Delay

**Issue:** Changes take 1-2 minutes to appear

**Cause:** Polling every 60 seconds + Klafs API delay

**Solution:** This is normal, no solution

### 2. Account Locked After Error

**Issue:** 3 failed attempts = account locked

**Cause:** Klafs security

**Solution:** Wait 30 minutes or contact Klafs

### 3. PIN Required to Turn On

**Issue:** Cannot turn on without PIN

**Cause:** Klafs security

**Solution:** Configure PIN in the integration

## Getting Help

### Information to Provide

When asking for help, include:

1. **Home Assistant version**
   ```
   Configuration > Information > Version
   ```

2. **Integration version**
   ```
   Configuration > Integrations > Klafs > Version
   ```

3. **Relevant logs**
   ```
   Configuration > Logs
   Copy errors related to "klafs"
   ```

4. **Configuration (without credentials)**
   ```yaml
   # Anonymize username/password/pin
   username: "user@*****.com"
   password: "****"
   pin: "****"
   ```

5. **Observed vs expected behavior**

### Where to Ask for Help

1. **GitHub Issues**
   - https://github.com/your-username/klafs-homeassistant/issues
   - Create a new issue with the template

2. **Home Assistant Forum**
   - https://community.home-assistant.io
   - "Third party integrations" section

3. **Home Assistant Discord**
   - #custom-components channel

## Complete Reset

If nothing works:

1. **Remove the integration**
   ```
   Configuration > Integrations > Klafs > Remove
   ```

2. **Delete files**
   ```
   rm -rf config/custom_components/klafs
   ```

3. **Restart Home Assistant**

4. **Reinstall the integration**

5. **Reconfigure with correct credentials**

## Useful Resources

- [README.md](../../README.md) - Main documentation
- [API_DOCUMENTATION.md](../../API_DOCUMENTATION.md) - API details
- [EXAMPLES.md](EXAMPLES.md) - Usage examples
- [GitHub Issues](https://github.com/your-username/klafs-homeassistant/issues)
- [Home Assistant Forum](https://community.home-assistant.io)
