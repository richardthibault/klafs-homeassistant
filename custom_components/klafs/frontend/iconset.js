/**
 * Klafs Custom Icon Set for Home Assistant
 * 
 * This file registers custom SVG icons with the prefix "klafs:"
 * Compatible with Home Assistant >= 2023.x
 * 
 * INSTALLATION:
 * Add this file as a Lovelace resource:
 * 1. Go to Settings > Dashboards > Resources (top right menu)
 * 2. Add resource: /local/klafs/iconset.js
 * 3. Resource type: JavaScript Module
 * 4. Refresh browser (Ctrl+F5)
 */

console.info('[Klafs Icons] Loading custom icon set...');

// Define custom icons
const KLAFS_ICONS = {
  'sauna': '/local/klafs/icons/sauna.svg',
  'sauna-heating': '/local/klafs/icons/sauna-heating.svg',
  'sauna-ready': '/local/klafs/icons/sauna-ready.svg',
  'sauna-off': '/local/klafs/icons/sauna-off.svg'
};

// Function to register icons with Home Assistant
function registerKlafsIcons() {
  // Method 1: Register with customIconsets (HA 2023+)
  if (!window.customIconsets) {
    window.customIconsets = {};
  }
  window.customIconsets.klafs = KLAFS_ICONS;
  
  // Method 2: Register with customIcons (fallback)
  if (!window.customIcons) {
    window.customIcons = {};
  }
  Object.keys(KLAFS_ICONS).forEach(name => {
    window.customIcons[`klafs:${name}`] = KLAFS_ICONS[name];
  });
  
  console.info('[Klafs Icons] Registered icon set with prefix "klafs:"');
  console.info('[Klafs Icons] Available icons:', Object.keys(KLAFS_ICONS).map(k => `klafs:${k}`));
  
  // Dispatch event to notify Home Assistant
  window.dispatchEvent(new Event('klafs-icons-loaded'));
}

// Wait for Home Assistant to be ready
if (customElements.get('home-assistant')) {
  registerKlafsIcons();
} else {
  window.addEventListener('load', () => {
    setTimeout(registerKlafsIcons, 100);
  });
}

// Also register when DOM is ready
if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', registerKlafsIcons);
} else {
  registerKlafsIcons();
}
