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

1. Restart Home Assistant
2. Clear browser cache (Ctrl+F5)
3. Check browser console (F12) for errors
4. Test URL: `http://your-ha.local:8123/local/klafs/icons/sauna.svg`

### Need more help?

See the complete documentation in `_dev/ICONS_INSTALLATION_GUIDE.md`

---

## Compatibility

- Home Assistant ≥ 2023.x
- HACS compatible
- Works on desktop and mobile
- Adapts to light/dark themes

---

**Version:** 1.0.0  
**Date:** 2026-02-09
