# Klafs Custom Icons

This directory contains the custom icon set for the Klafs Sauna integration.

## Structure

```
frontend/
├── iconset.js              # JavaScript file that registers the icon set
└── icons/                  # SVG icon files
    ├── sauna.svg           # Default sauna icon
    ├── sauna-heating.svg   # Sauna heating/warming up
    ├── sauna-ready.svg     # Sauna ready for use
    └── sauna-off.svg       # Sauna turned off
```

## Icon Prefix

All icons are registered with the prefix `klafs:` and can be used in Home Assistant like this:

- `klafs:sauna` - Default sauna icon
- `klafs:sauna-heating` - Sauna is heating
- `klafs:sauna-ready` - Sauna is ready
- `klafs:sauna-off` - Sauna is off

## Automatic Icon Mapping

The integration automatically assigns icons based on the sauna state:

| State | Icon | Description |
|-------|------|-------------|
| Off | `klafs:sauna-off` | Sauna is turned off |
| Heating | `klafs:sauna-heating` | Sauna is warming up |
| Ready | `klafs:sauna-ready` | Sauna has reached target temperature |
| Disconnected | `mdi:cloud-off-outline` | Sauna is not connected |
| Unknown | `klafs:sauna` | Default fallback icon |

## SVG Requirements

All SVG icons must:
- Use `viewBox="0 0 24 24"` (Material Design standard)
- Use `fill="currentColor"` to inherit theme colors
- Be monochrome (single color)
- Be optimized for small sizes (24x24px)

## Usage in Lovelace

The icons are automatically applied to entities, but you can also use them manually:

```yaml
type: entities
entities:
  - entity: climate.klafs_sauna
    icon: klafs:sauna-ready
  - entity: sensor.klafs_sauna_temperature
    icon: klafs:sauna-heating
```

## Debugging

If icons don't appear:

1. Check browser console for errors: `[Klafs Icons]`
2. Verify files are accessible:
   - `/local/klafs/icons/sauna.svg`
   - `/local/klafs/iconset.js`
3. Clear browser cache (Ctrl+F5)
4. Restart Home Assistant
5. Check Home Assistant logs for icon registration messages

## Technical Details

The icons are served as static files by Home Assistant and registered using the `add_extra_js_url` method. The JavaScript file (`iconset.js`) registers the icon set with Home Assistant's frontend, making them available throughout the UI.
