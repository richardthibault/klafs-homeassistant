# Changelog

**Read in other languages:** **English** | [Français](CHANGELOG.fr.md) | [Deutsch](CHANGELOG.de.md) | [Español](CHANGELOG.es.md)

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/).

**For planned future features, see [FUTURELOG.md](FUTURELOG.md)**

---

## [1.0.21] - 2026-02-09

### Fixed
- **Official HA icon API**: Switched to `ha-iconset-svg` Web Components (official Home Assistant method)
- Icons now render correctly with all visual elements (radiator, thermometer, heat waves)
- Fixes SVG path parsing error from v1.0.20

### Technical Details
- Uses `<ha-iconset-svg>` Web Component with inline SVG definitions
- Accepts complete SVG markup (`<rect>`, `<circle>`, `<line>`, `<path>`)
- Preserves all attributes: colors, strokes, opacity
- No external files needed (HACS-compatible)
- Official HA API for custom icons since 2020

---

## [1.0.20] - 2026-02-09

### Fixed
- **Complete icon rendering**: Restored full SVG icons with radiator, thermometer, and heat waves
- Icons now include all visual details: electric heater bars (gray), heating stones, bench, thermometer with fill levels
- `sauna-heating` shows animated heat waves above stones
- `sauna-ready` displays checkmark indicator
- `sauna-off` uses reduced opacity for inactive state

### Technical Details
- Embedded complete SVG markup in iconset.js (inline approach)
- Parse SVG to extract innerHTML and viewBox for HA icon API
- Preserves colors (`currentColor`, `#888`), strokes, and opacity attributes
- No external SVG files needed (HACS-compatible)

---

## [1.0.19] - 2026-02-09

### Fixed
- **Dual API compatibility**: Added support for both `customIconsets` and `customIcons` APIs
- Synchronous icon functions for better compatibility across HA versions
- Icons now work with both legacy and modern Home Assistant icon systems

### Technical Details
- Registered with `window.customIconsets["klafs"]` (legacy API)
- Registered with `window.customIcons["klafs"]` (alternative API)
- Both return `{path, viewBox}` objects synchronously
- Maximum compatibility with HA 2020-2024+ versions

---

## [1.0.18] - 2026-02-09

### Fixed
- **Modern HA API**: Use `async_register_static_paths` with `StaticPathConfig` (official HA 2024+ method)
- Fixed deprecated `register_static_path` causing AttributeError in recent Home Assistant versions
- Function now properly async with `await` call in setup

### Technical Details
- Import `StaticPathConfig` from `homeassistant.components.http`
- Import `add_extra_js_url` from `homeassistant.components.frontend`
- Use `await hass.http.async_register_static_paths([StaticPathConfig(...)])`
- Icons should now load correctly at `/klafs/iconset.js`

---

## [1.0.17] - 2026-02-09

### Fixed
- **HTTP serving**: Serve iconset.js via HTTP instead of data URL (CSP-safe)
- Use `register_static_path` to serve frontend directory
- Icons now loaded via HTTP URL: `/klafs/iconset.js`

### Changed
- Removed data URL approach (blocked by CSP in recent HA versions)
- Simplified to synchronous registration function

---

## [1.0.16] - 2026-02-09

### Fixed
- **Correct API usage**: Use `from homeassistant.components import frontend` then `frontend.add_extra_js_url()`
- **Proper iconset format**: Use `window.customIconsets` API as per HA documentation
- Icons now use official Home Assistant custom iconsets API (2020+)

### Changed
- Rewrote iconset.js to use `window.customIconsets` with async function returning `{path, viewBox}`
- Simplified SVG paths for better compatibility

---

## [1.0.15] - 2026-02-09

### Fixed
- **Data URL injection**: Use base64 data URL instead of register_static_path
- Fixed AttributeError: `'HomeAssistantHTTP' object has no attribute 'register_static_path'`
- Icons now injected directly into frontend without HTTP server dependency

---

## [1.0.14] - 2026-02-09

### Changed
- **Inline iconset**: SVG icons now embedded directly in iconset.js
- Removed `icons/` directory - no longer needed
- Simplified to single file deployment (frontend/iconset.js only)
- More reliable: no dependency on HACS copying subdirectories

### Fixed
- Icons will now deploy correctly via HACS (single JS file, no subdirectories)

---

## [1.0.13] - 2026-02-09

### Fixed
- **Import error**: Removed non-existent `StaticPathConfig` import
- Use simple `register_static_path` method that works across all HA versions
- Fixed ImportError: `cannot import name 'StaticPathConfig'`

---

## [1.0.12] - 2026-02-09

### Fixed
- **Static path registration**: Use `StaticPathConfig` objects instead of dictionaries
- Fixed AttributeError: `'dict' object has no attribute 'url_path'`

---

## [1.0.11] - 2026-02-09

### Fixed
- **API compatibility**: Fixed `register_static_path` → `async_register_static_paths` for modern Home Assistant
- **Icon location**: Moved icons from `frontend/icons/` to `icons/` for simpler structure
- Fixed AttributeError on Home Assistant startup

### Changed
- Icons now in `custom_components/klafs/icons/` directory
- Using correct async API for static path registration

---

## [1.0.10] - 2026-02-09

### Fixed
- **HACS file whitelist**: Added `files` array to `hacs.json` to explicitly include all files
- This fixes HACS filtering out non-Python files (SVG, JS) from subdirectories
- HACS will now install ALL files including `frontend/icons/*.svg`

### Changed
- Updated `hacs.json` with `files: ["custom_components/klafs/**"]` whitelist

---

## [1.0.9] - 2026-02-09

### Fixed
- **HACS deployment**: Fixed `hacs.json` with `content_in_root: false` to ensure all files are deployed
- This fixes the issue where `frontend/icons/` directory was not copied by HACS

### Changed
- Simplified `hacs.json` (removed redundant fields that belong in manifest.json)

---

## [1.0.8] - 2026-02-09

### Fixed
- **Icon file location**: Moved SVG files to correct location `frontend/icons/` for proper serving
- **Static path registration**: Simplified to serve entire frontend directory under `/local/klafs/`
- **Automatic loading**: Icons now load automatically without manual Lovelace resource addition
- **Icon resolver**: Updated iconset.js to use resolver function for better compatibility

### Changed
- SVG files moved from `custom_components/klafs/` to `custom_components/klafs/frontend/icons/`
- Simplified iconset.js with resolver function approach
- No manual Lovelace resource addition required anymore

---

## [1.0.7] - 2026-02-09

### Fixed
- **Icon loading method**: Replaced deprecated `add_extra_js_url()` with manual Lovelace resource registration
- **Static path registration**: Fixed incorrect file path registration for iconset.js
- **Icon registration**: Improved compatibility with Home Assistant 2023+ icon system

### Changed
- Custom icons now require manual Lovelace resource addition (see CUSTOM_ICONS.md)
- Updated iconset.js with multiple registration methods for better compatibility
- Enhanced logging for icon registration debugging

### Documentation
- Added comprehensive troubleshooting guide in all 4 languages (EN/FR/DE/ES)
- Step-by-step instructions for adding Lovelace resource
- Browser console debugging tips

---

## [1.0.6] - 2026-02-09

### Fixed
- **HACS compatibility**: Moved SVG icons to integration root directory for proper HACS deployment
- HACS was not copying the `frontend/icons/` subdirectory, causing icons to be missing after installation

---

## [1.0.5] - 2026-02-09

### Fixed
- **Icon registration timing**: Icons are now registered after platforms are loaded, ensuring proper initialization
- This fixes the issue where custom icons were not appearing in the frontend

---

## [1.0.4] - 2026-02-09

### Added
- **Custom Icon Set**: Integration now includes custom icons with `klafs:` prefix
  - `klafs:sauna` - Default/neutral state
  - `klafs:sauna-heating` - Sauna is heating up (with heat waves)
  - `klafs:sauna-ready` - Sauna is ready for use (full thermometer + checkmark)
  - `klafs:sauna-off` - Sauna is turned off (grayed elements)
  - Icons automatically change based on sauna state
  - All icons use `fill="currentColor"` for theme compatibility
  - Works with Home Assistant ≥ 2023.x
- **Multilingual Documentation**: Custom icons documentation in 4 languages (EN/FR/DE/ES)
- **Automatic Icon Mapping**: Icons change automatically based on entity state
  - No configuration required
  - Works with both sensor and climate entities

### Changed
- Moved icons from `icons/` to `frontend/icons/` directory
- Icons are now served as static files via `/local/klafs/icons/`
- Added `icon_mapping.py` for centralized icon state management

### Technical
- Added `frontend/iconset.js` for icon registration in Home Assistant frontend
- Updated `__init__.py` to register static paths and load iconset
- Updated `sensor.py` and `climate.py` to use dynamic icon properties
- Icons adapt to light/dark themes automatically

---

## [1.0.3] - 2026-02-09

### Fixed
- **Icon display issue**: Replaced custom `klafs:sauna-*` icons with standard MDI icons
  - Custom SVG icons are kept in the repository for future use
  - Now using `mdi:sauna` (default/off), `mdi:fire` (heating), `mdi:check-circle` (ready)
  - Icons now display correctly without requiring additional configuration

### Technical
- Home Assistant custom integrations cannot easily embed custom icon sets without external dependencies
- Standard MDI icons provide better compatibility and immediate functionality

---

## [1.0.2] - 2026-02-09

### Added
- **Custom SVG icons** with dynamic color support
  - 4 state-specific icons: default, off, heating, ready
  - Icons adapt to Home Assistant theme (light/dark mode)
  - Radiator with visible bars and heating stones design
  - Thermometer indicates temperature level (0%, 25%, 50%, 100%)
  - Heat waves animation for heating state
  - Check mark for ready state
- **PNG branding icons** for HACS and Home Assistant
  - 256x256 icon for HACS integration list
  - High-resolution 512x512 icon for Retina displays
  - Warm gradient background (orange/red tones)

### Changed
- Updated sensor icons to use custom `klafs:sauna-*` icons instead of generic MDI icons
- Icons now provide better visual feedback for sauna state

### Technical
- Icons use `currentColor` for automatic theme adaptation
- SVG format ensures crisp display at any size
- No external dependencies or copyright issues

---

## [1.0.1] - 2026-02-09

### Fixed
- **Critical reconnection bug**: Sauna was no longer detected after WiFi connection loss
  - Coordinator now keeps saunas in data even when disconnected
  - Improved error handling per individual sauna
  - Entities remain available and reconnect automatically
  - No longer need to uninstall/reinstall integration after connection loss

### Release Notes

This version fixes a critical bug that prevented automatic sauna reconnection after WiFi connection loss. The coordinator now maintains entities even when the sauna is disconnected, allowing transparent reconnection.

---

## [1.0.0] - 2026-01-28

### Added
- Initial integration with Klafs API
- Authentication via Klafs Sauna App credentials
- **Multi-sauna support**: Manage multiple saunas from a single account
- **Individual PIN code per sauna**: Each sauna can have its own PIN
- **3-step config flow**: Credentials → Sauna selection → PIN configuration
- Climate entity (thermostat) to control each sauna
- Temperature, humidity and status sensors per sauna
- Switch to toggle between Sauna and SANARIUM modes per sauna
- `power_on_with_pin` service to turn on with specific PIN
- `set_humidity_level` service to control humidity (SANARIUM)
- `set_start_time` service to schedule start time
- Support for modes: Classic Sauna, SANARIUM, Infrared
- Automatic polling every 60 seconds
- Automatic detection of all account saunas
- Configuration via user interface (Config Flow)
- French and English translations
- Complete documentation (README, API, examples, troubleshooting, multi-sauna)
- HACS support for easy installation
- Automatic reconnection handling on session expiration

### Features
- Temperature control (10-100°C depending on mode)
- Remote power on/off
- Real-time temperature and humidity monitoring
- Sauna connection status
- "Ready" indication when sauna is ready
- Extended attributes (active mode, humidity level, etc.)
- Temperature limits adapted to selected mode

### Security
- Secure credential storage
- Mandatory PIN code support for power on
- Failed login attempt handling
- HTTPS communication only

### Documentation
- README.md: Main documentation
- INSTALLATION.md: Detailed installation guide
- API_DOCUMENTATION.md: Technical API documentation
- EXAMPLES.md: Automation examples and Lovelace cards
- TROUBLESHOOTING.md: Troubleshooting guide
- MULTI_SAUNA_SUPPORT.md: Multi-sauna guide
- CHANGELOG.md: Version history

### Release Notes

This first stable version offers all basic features to control your Klafs sauna via Home Assistant. The integration was developed based on reverse engineering of the Klafs API used by the official mobile application.

**Highlights:**
- Simple configuration via user interface
- Full support for Sauna and SANARIUM modes
- Custom services for advanced control
- Comprehensive documentation
- HACS compatible

**Known Limitations:**
- Polling every 60 seconds (no real-time push)
- Depends on Klafs cloud (no local control)
- Infrared mode partially tested
- No support for advanced features (lighting, aromatherapy)

**Compatibility:**
- Home Assistant 2023.1.0 or higher
- Python 3.10 or higher
- All Klafs saunas with Wi-Fi module and "KLAFS Sauna App" option

**Acknowledgments:**
- OpenHAB community for initial API research
- IPSymconKlafsSaunaControl project for implementation examples
- Home Assistant community contributors and testers

---

## Migration

### From Previous Version

#### From 1.0.0 to 1.0.1
No action required. Simply update via HACS and restart Home Assistant.

### From Other Integrations

If you currently use another method to control your Klafs sauna (scripts, REST commands, etc.), you can migrate to this integration:

1. Backup your existing automations
2. Install this integration
3. Configure with your Klafs credentials
4. Update your automations to use the new entities
5. Remove the old configuration

---

## Support

To report a bug or request a feature:
- GitHub Issues: https://github.com/richardthibault/klafs-homeassistant/issues
- Home Assistant Forum: https://community.home-assistant.io

## Contributing

Contributions are welcome! See [CONTRIBUTING.md](CONTRIBUTING.md) to understand the project architecture.

---

**Legend:**
- `Added`: New features
- `Changed`: Changes in existing features
- `Deprecated`: Features to be removed soon
- `Removed`: Removed features
- `Fixed`: Bug fixes
- `Security`: Security vulnerability fixes
