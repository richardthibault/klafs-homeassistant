/**
 * Klafs Custom Icon Set for Home Assistant
 * 
 * Registers custom SVG icons with the prefix "klafs:"
 * Compatible with Home Assistant >= 2023.x
 */

(async () => {
  // Wait for Home Assistant to be fully loaded
  await customElements.whenDefined("home-assistant");
  
  console.info('[Klafs Icons] Loading custom icon set...');
  
  // Register iconset with resolver function
  // This provides icons via URL: /local/klafs/icons/{name}.svg
  window.customIconsets = window.customIconsets || {};
  window.customIconsets["klafs"] = (name) => `/local/klafs/icons/${name}.svg`;
  
  console.info('[Klafs Icons] Iconset "klafs" registered successfully');
  console.info('[Klafs Icons] Available icons: klafs:sauna, klafs:sauna-heating, klafs:sauna-ready, klafs:sauna-off');
})();
