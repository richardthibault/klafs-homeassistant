/**
 * Klafs Custom Icon Set for Home Assistant
 * 
 * This file registers custom SVG icons with the prefix "klafs:"
 * Compatible with Home Assistant >= 2023.x
 */

// Wait for Home Assistant to be fully loaded
if (!customElements.get('ha-icon')) {
  console.warn('[Klafs Icons] ha-icon not yet defined, waiting...');
}

// Function to load and register icons
async function loadKlafsIcons() {
  try {
    // Get the icon manager from Home Assistant
    const iconManager = window.frontendVersion ? window : customElements.get('ha-icon');
    
    if (!iconManager) {
      console.error('[Klafs Icons] Icon manager not available');
      return;
    }

    // Define the icon set
    const iconSet = {
      name: 'klafs',
      icons: {
        'sauna': '/local/klafs/icons/sauna.svg',
        'sauna-heating': '/local/klafs/icons/sauna-heating.svg',
        'sauna-ready': '/local/klafs/icons/sauna-ready.svg',
        'sauna-off': '/local/klafs/icons/sauna-off.svg'
      }
    };

    // Register icons with Home Assistant
    if (window.customIconsets) {
      window.customIconsets.klafs = iconSet.icons;
    } else {
      window.customIconsets = { klafs: iconSet.icons };
    }

    console.info('[Klafs Icons] Successfully registered icon set with prefix "klafs:"');
    console.debug('[Klafs Icons] Available icons:', Object.keys(iconSet.icons));
    
  } catch (error) {
    console.error('[Klafs Icons] Error loading icon set:', error);
  }
}

// Load icons when DOM is ready
if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', loadKlafsIcons);
} else {
  loadKlafsIcons();
}

// Also try to load when Home Assistant is ready
window.addEventListener('load', () => {
  setTimeout(loadKlafsIcons, 1000);
});
