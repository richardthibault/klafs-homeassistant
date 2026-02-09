/**
 * Klafs Custom Icon Set - Pure SVG Paths (Optimized)
 * Simplified icons focusing on heater and stones (no bench)
 * Uses window.customIconsets API
 */

// Icon definitions with pure SVG paths - optimized for visibility
const KLAFS_ICONS = {
  "sauna": {
    // Radiateur électrique (agrandi, centré)
    path: "M8,10 L16,10 L16,14 L8,14 Z " +
          // Barres du radiateur (lignes verticales)
          "M9,10.5 L9,13.5 M10,10.5 L10,13.5 M11,10.5 L11,13.5 M12,10.5 L12,13.5 M13,10.5 L13,13.5 M14,10.5 L14,13.5 M15,10.5 L15,13.5 " +
          // Pierres chauffantes (3 cercles agrandis)
          "M9,7.5 A1.5,1.5 0 1,0 9,10.5 A1.5,1.5 0 1,0 9,7.5 Z " +
          "M15,7.5 A1.5,1.5 0 1,0 15,10.5 A1.5,1.5 0 1,0 15,7.5 Z " +
          "M12,5 A2,2 0 1,0 12,9 A2,2 0 1,0 12,5 Z " +
          // Thermomètre (50% rempli, à droite)
          "M20,16 A1.5,1.5 0 1,0 20,19 A1.5,1.5 0 1,0 20,16 Z " +
          "M19.5,11 L20.5,11 L20.5,17 L19.5,17 Z " +
          "M19.5,14 L20.5,14 L20.5,17 L19.5,17 Z " +
          "M18,15 L19.5,15 M18,13 L19.5,13 M18,11.5 L19.5,11.5",
    viewBox: "0 0 24 24"
  },
  
  "sauna-heating": {
    // Radiateur + pierres (identique)
    path: "M8,10 L16,10 L16,14 L8,14 Z " +
          "M9,10.5 L9,13.5 M10,10.5 L10,13.5 M11,10.5 L11,13.5 M12,10.5 L12,13.5 M13,10.5 L13,13.5 M14,10.5 L14,13.5 M15,10.5 L15,13.5 " +
          "M9,7.5 A1.5,1.5 0 1,0 9,10.5 A1.5,1.5 0 1,0 9,7.5 Z " +
          "M15,7.5 A1.5,1.5 0 1,0 15,10.5 A1.5,1.5 0 1,0 15,7.5 Z " +
          "M12,5 A2,2 0 1,0 12,9 A2,2 0 1,0 12,5 Z " +
          // Thermomètre (75% rempli)
          "M20,16 A1.5,1.5 0 1,0 20,19 A1.5,1.5 0 1,0 20,16 Z " +
          "M19.5,11 L20.5,11 L20.5,17 L19.5,17 Z " +
          "M19.5,12.5 L20.5,12.5 L20.5,17 L19.5,17 Z " +
          "M18,15 L19.5,15 M18,13 L19.5,13 M18,11.5 L19.5,11.5 " +
          // Ondes de chaleur (6 courbes)
          "M5,8 Q5,6.5 5.5,6.5 T6,8 " +
          "M6.5,7 Q6.5,5.5 7,5.5 T7.5,7 " +
          "M16.5,7 Q16.5,5.5 17,5.5 T17.5,7 " +
          "M18,8 Q18,6.5 18.5,6.5 T19,8 " +
          "M11,5.5 Q11,4 11.5,4 T12,5.5 " +
          "M12.5,5 Q12.5,3.5 13,3.5 T13.5,5",
    viewBox: "0 0 24 24"
  },
  
  "sauna-ready": {
    // Radiateur + pierres (identique)
    path: "M8,10 L16,10 L16,14 L8,14 Z " +
          "M9,10.5 L9,13.5 M10,10.5 L10,13.5 M11,10.5 L11,13.5 M12,10.5 L12,13.5 M13,10.5 L13,13.5 M14,10.5 L14,13.5 M15,10.5 L15,13.5 " +
          "M9,7.5 A1.5,1.5 0 1,0 9,10.5 A1.5,1.5 0 1,0 9,7.5 Z " +
          "M15,7.5 A1.5,1.5 0 1,0 15,10.5 A1.5,1.5 0 1,0 15,7.5 Z " +
          "M12,5 A2,2 0 1,0 12,9 A2,2 0 1,0 12,5 Z " +
          // Thermomètre (100% rempli)
          "M20,16 A1.5,1.5 0 1,0 20,19 A1.5,1.5 0 1,0 20,16 Z " +
          "M19.5,11 L20.5,11 L20.5,17 L19.5,17 Z " +
          "M19.5,11 L20.5,11 L20.5,17 L19.5,17 Z " +
          "M18,15 L19.5,15 M18,13 L19.5,13 M18,11.5 L19.5,11.5 " +
          // Checkmark (prêt)
          "M3,8 L5,10 L9,6",
    viewBox: "0 0 24 24"
  },
  
  "sauna-off": {
    // Radiateur + pierres (identique)
    path: "M8,10 L16,10 L16,14 L8,14 Z " +
          "M9,10.5 L9,13.5 M10,10.5 L10,13.5 M11,10.5 L11,13.5 M12,10.5 L12,13.5 M13,10.5 L13,13.5 M14,10.5 L14,13.5 M15,10.5 L15,13.5 " +
          "M9,7.5 A1.5,1.5 0 1,0 9,10.5 A1.5,1.5 0 1,0 9,7.5 Z " +
          "M15,7.5 A1.5,1.5 0 1,0 15,10.5 A1.5,1.5 0 1,0 15,7.5 Z " +
          "M12,5 A2,2 0 1,0 12,9 A2,2 0 1,0 12,5 Z " +
          // Thermomètre (vide - 0%)
          "M20,16 A1.5,1.5 0 1,0 20,19 A1.5,1.5 0 1,0 20,16 Z " +
          "M19.5,11 L20.5,11 L20.5,17 L19.5,17 Z " +
          "M18,15 L19.5,15 M18,13 L19.5,13 M18,11.5 L19.5,11.5",
    viewBox: "0 0 24 24"
  }
};

// Register with both APIs for maximum compatibility
window.customIconsets = window.customIconsets || {};
window.customIconsets["klafs"] = (name) => KLAFS_ICONS[name] || null;

window.customIcons = window.customIcons || {};
window.customIcons["klafs"] = {
  getIcon: (name) => KLAFS_ICONS[name] || null
};

console.info("[Klafs Icons] Loaded (optimized, no bench):", Object.keys(KLAFS_ICONS));
