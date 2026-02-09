**Read in other languages:** [English](CUSTOM_ICONS.md) | [Français](CUSTOM_ICONS.fr.md) | [Deutsch](CUSTOM_ICONS.de.md) | [Español](CUSTOM_ICONS.es.md)

---

# 🎨 Custom Icons

## Overview

The Klafs integration now uses **custom icons** that automatically change based on the sauna state.

---

## Available Icons

| Icon | State | Description |
|------|-------|-------------|
| 🔥 `klafs:sauna-heating` | Heating | Sauna is warming up |
| ✅ `klafs:sauna-ready` | Ready | Sauna has reached target temperature |
| ⚫ `klafs:sauna-off` | Off | Sauna is turned off |
| 🏠 `klafs:sauna` | Default | Neutral state |

Icons automatically adapt to Home Assistant's light/dark theme.

---

## Installation

### Via HACS (Recommended)

1. Update the Klafs integration via HACS
2. Restart Home Assistant
3. Clear browser cache (Ctrl+F5)
4. Icons will appear automatically

### Manual Installation

1. Copy the `custom_components/klafs/` folder to Home Assistant
2. Restart Home Assistant
3. Clear browser cache (Ctrl+F5)

---

## Usage

### Automatic (Recommended)

Icons are automatically applied to all Klafs entities:

```yaml
type: entities
entities:
  - entity: climate.klafs_sauna
  - entity: sensor.klafs_sauna_status
```

### Manual Override

You can force a specific icon:

```yaml
type: entities
entities:
  - entity: climate.klafs_sauna
    icon: klafs:sauna-ready
```

---

## Troubleshooting

### Icons not showing?

**Step 1: Verify files are deployed**
- Check that SVG files exist in `custom_components/klafs/`
- Check that `frontend/iconset.js` exists

**Step 2: Add Lovelace Resource (REQUIRED)**
1. Go to **Settings** > **Dashboards** > **Resources** (⋮ menu top right)
2. Click **+ ADD RESOURCE**
3. URL: `/local/klafs/iconset.js`
4. Resource type: **JavaScript Module**
5. Click **CREATE**

**Step 3: Clear cache and reload**
1. Restart Home Assistant
2. Clear browser cache (Ctrl+F5 or Shift+F5)
3. Reload the page

**Step 4: Verify in browser console**
1. Press F12 to open Developer Tools
2. Go to Console tab
3. Look for: `[Klafs Icons] Registered icon set`
4. If not present, check for errors

**Step 5: Test icon URLs**
- Test: `http://your-ha-ip:8123/local/klafs/icons/sauna.svg`
- Should display the SVG icon

**Step 6: Check entity icons**
1. Go to Developer Tools > States
2. Find your Klafs entities
3. Check the `icon` attribute
4. Should show `klafs:sauna-xxx`

### Still not working?

**Option A: Use MDI icons as fallback**
The integration will automatically fall back to Material Design Icons if custom icons fail to load.

**Option B: Manual icon override**
```yaml
type: entities
entities:
  - entity: climate.klafs_sauna
    icon: mdi:sauna
```

### Need more help?

- Check Home Assistant logs for "Klafs" errors
- See complete documentation in `_dev/ICONS_INSTALLATION_GUIDE.md`
- Report issues on GitHub

---

## Compatibility

- Home Assistant ≥ 2023.x
- HACS compatible
- Works on desktop and mobile
- Adapts to light/dark themes

---

**Version:** 1.0.0  
**Date:** 2026-02-09
