# ✅ v1.1.2 - Preset Mode Fix | Correction modes preset | Preset-Modus-Fix | Corrección modos preset

**Read in your language:** [🇬🇧 English](#user-content-english) | [🇫🇷 Français](#user-content-français) | [🇩🇪 Deutsch](#user-content-deutsch) | [🇪🇸 Español](#user-content-español)

---

<a id="user-content-english"></a>
## 🇬🇧 English

### Fixed
- **Preset mode switching**: Fixed API parameter name from `mode` to `selected_mode`
- Preset mode changes now work correctly via Home Assistant interface
- No more HTTP 500 errors when changing modes

### What's New
This critical fix resolves the HTTP 500 error when changing preset modes. The issue was a simple parameter name mismatch - the Klafs API expects `selected_mode` but we were sending `mode`. Now preset mode switching works perfectly!

**Now working:**
- ✅ Switch between Sauna / SANARIUM / Infrared modes
- ✅ Temperature limits adjust automatically
- ✅ Each mode remembers its preferred temperature
- ✅ No more API errors

### Upgrade Instructions
**Via HACS (Recommended)**
1. Open HACS → Integrations
2. Find "Klafs Sauna" → Update to v1.1.2
3. Restart Home Assistant
4. Try changing modes - it works now!

---

<a id="user-content-français"></a>
## 🇫🇷 Français

### Corrigé
- **Changement de mode preset** : Correction du nom du paramètre API de `mode` vers `selected_mode`
- Les changements de mode preset fonctionnent maintenant correctement via l'interface Home Assistant
- Plus d'erreurs HTTP 500 lors du changement de mode

### Nouveautés
Ce correctif critique résout l'erreur HTTP 500 lors du changement de modes preset. Le problème était une simple incompatibilité de nom de paramètre - l'API Klafs attend `selected_mode` mais nous envoyions `mode`. Maintenant le changement de mode preset fonctionne parfaitement !

**Maintenant fonctionnel :**
- ✅ Basculer entre les modes Sauna / SANARIUM / Infrarouge
- ✅ Les limites de température s'ajustent automatiquement
- ✅ Chaque mode mémorise sa température préférée
- ✅ Plus d'erreurs API

### Instructions de mise à jour
**Via HACS (Recommandé)**
1. Ouvrir HACS → Intégrations
2. Trouver "Klafs Sauna" → Mettre à jour vers v1.1.2
3. Redémarrer Home Assistant
4. Essayer de changer de mode - ça fonctionne maintenant !

---

<a id="user-content-deutsch"></a>
## 🇩🇪 Deutsch

### Behoben
- **Preset-Modus-Wechsel**: API-Parametername von `mode` zu `selected_mode` korrigiert
- Preset-Modus-Änderungen funktionieren jetzt korrekt über die Home Assistant-Oberfläche
- Keine HTTP 500-Fehler mehr beim Moduswechsel

### Was ist neu
Dieser kritische Fix behebt den HTTP 500-Fehler beim Wechseln von Preset-Modi. Das Problem war eine einfache Parameternamens-Inkompatibilität - die Klafs-API erwartet `selected_mode`, aber wir sendeten `mode`. Jetzt funktioniert der Preset-Modus-Wechsel perfekt!

**Jetzt funktioniert:**
- ✅ Wechsel zwischen Sauna / SANARIUM / Infrarot-Modi
- ✅ Temperaturgrenzen passen sich automatisch an
- ✅ Jeder Modus merkt sich seine bevorzugte Temperatur
- ✅ Keine API-Fehler mehr

### Aktualisierungsanleitung
**Via HACS (Empfohlen)**
1. HACS öffnen → Integrationen
2. "Klafs Sauna" finden → Auf v1.1.2 aktualisieren
3. Home Assistant neu starten
4. Versuchen Sie, Modi zu wechseln - es funktioniert jetzt!

---

<a id="user-content-español"></a>
## 🇪🇸 Español

### Corregido
- **Cambio de modo preset**: Corregido nombre de parámetro API de `mode` a `selected_mode`
- Los cambios de modo preset ahora funcionan correctamente a través de la interfaz de Home Assistant
- No más errores HTTP 500 al cambiar de modo

### Novedades
Esta corrección crítica resuelve el error HTTP 500 al cambiar modos preset. El problema era una simple incompatibilidad de nombre de parámetro - la API de Klafs espera `selected_mode` pero enviábamos `mode`. ¡Ahora el cambio de modo preset funciona perfectamente!

**Ahora funciona:**
- ✅ Cambiar entre modos Sauna / SANARIUM / Infrarrojo
- ✅ Los límites de temperatura se ajustan automáticamente
- ✅ Cada modo recuerda su temperatura preferida
- ✅ No más errores de API

### Instrucciones de actualización
**Via HACS (Recomendado)**
1. Abrir HACS → Integraciones
2. Buscar "Klafs Sauna" → Actualizar a v1.1.2
3. Reiniciar Home Assistant
4. Intentar cambiar de modo - ¡funciona ahora!

---

**Full Changelog**: https://github.com/richardthibault/klafs-homeassistant/compare/v1.1.1...v1.1.2
