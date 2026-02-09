# 🔍 v1.1.1 - Debug Logging | Logs de débogage | Debug-Protokollierung | Registro de depuración

**Read in your language:** [🇬🇧 English](#user-content-english) | [🇫🇷 Français](#user-content-français) | [🇩🇪 Deutsch](#user-content-deutsch) | [🇪🇸 Español](#user-content-español)

---

<a id="user-content-english"></a>
## 🇬🇧 English

### Fixed
- **Debug logging**: Added detailed logging to diagnose preset mode API errors
- Debug log file created at `/config/klafs_debug.log` for troubleshooting
- Enhanced error messages for API calls

### What's New
This patch release adds comprehensive debug logging to help diagnose HTTP 500 errors when changing preset modes. A debug log file is automatically created at `/config/klafs_debug.log` containing detailed information about API calls, payloads, and responses.

**For users experiencing mode change issues:**
1. Update to v1.1.1
2. Try changing modes (Sauna ↔ SANARIUM)
3. Check `/config/klafs_debug.log` for detailed error information
4. Share the log content for support

### Upgrade Instructions
**Via HACS (Recommended)**
1. Open HACS → Integrations
2. Find "Klafs Sauna" → Update
3. Restart Home Assistant

---

<a id="user-content-français"></a>
## 🇫🇷 Français

### Corrigé
- **Logs de débogage** : Ajout de logs détaillés pour diagnostiquer les erreurs API des modes preset
- Fichier de log de débogage créé à `/config/klafs_debug.log` pour dépannage
- Messages d'erreur améliorés pour les appels API

### Nouveautés
Cette version corrective ajoute des logs de débogage complets pour aider à diagnostiquer les erreurs HTTP 500 lors du changement de modes preset. Un fichier de log de débogage est automatiquement créé à `/config/klafs_debug.log` contenant des informations détaillées sur les appels API, les payloads et les réponses.

**Pour les utilisateurs rencontrant des problèmes de changement de mode :**
1. Mettre à jour vers v1.1.1
2. Essayer de changer de mode (Sauna ↔ SANARIUM)
3. Vérifier `/config/klafs_debug.log` pour les informations d'erreur détaillées
4. Partager le contenu du log pour support

### Instructions de mise à jour
**Via HACS (Recommandé)**
1. Ouvrir HACS → Intégrations
2. Trouver "Klafs Sauna" → Mettre à jour
3. Redémarrer Home Assistant

---

<a id="user-content-deutsch"></a>
## 🇩🇪 Deutsch

### Behoben
- **Debug-Protokollierung**: Detaillierte Protokollierung zur Diagnose von Preset-Modus-API-Fehlern hinzugefügt
- Debug-Protokolldatei erstellt unter `/config/klafs_debug.log` zur Fehlerbehebung
- Verbesserte Fehlermeldungen für API-Aufrufe

### Was ist neu
Diese Patch-Version fügt umfassende Debug-Protokollierung hinzu, um HTTP 500-Fehler beim Wechseln von Preset-Modi zu diagnostizieren. Eine Debug-Protokolldatei wird automatisch unter `/config/klafs_debug.log` erstellt und enthält detaillierte Informationen über API-Aufrufe, Payloads und Antworten.

**Für Benutzer mit Moduswechselproblemen:**
1. Auf v1.1.1 aktualisieren
2. Versuchen Sie, Modi zu wechseln (Sauna ↔ SANARIUM)
3. Überprüfen Sie `/config/klafs_debug.log` für detaillierte Fehlerinformationen
4. Teilen Sie den Protokollinhalt für Support

### Aktualisierungsanleitung
**Via HACS (Empfohlen)**
1. HACS öffnen → Integrationen
2. "Klafs Sauna" finden → Aktualisieren
3. Home Assistant neu starten

---

<a id="user-content-español"></a>
## 🇪🇸 Español

### Corregido
- **Registro de depuración**: Añadido registro detallado para diagnosticar errores de API de modos preset
- Archivo de registro de depuración creado en `/config/klafs_debug.log` para solución de problemas
- Mensajes de error mejorados para llamadas API

### Novedades
Esta versión de parche añade registro de depuración completo para ayudar a diagnosticar errores HTTP 500 al cambiar modos preset. Un archivo de registro de depuración se crea automáticamente en `/config/klafs_debug.log` conteniendo información detallada sobre llamadas API, payloads y respuestas.

**Para usuarios con problemas de cambio de modo:**
1. Actualizar a v1.1.1
2. Intentar cambiar de modo (Sauna ↔ SANARIUM)
3. Verificar `/config/klafs_debug.log` para información detallada de errores
4. Compartir el contenido del registro para soporte

### Instrucciones de actualización
**Via HACS (Recomendado)**
1. Abrir HACS → Integraciones
2. Buscar "Klafs Sauna" → Actualizar
3. Reiniciar Home Assistant

---

**Full Changelog**: https://github.com/richardthibault/klafs-homeassistant/compare/v1.1.0...v1.1.1
