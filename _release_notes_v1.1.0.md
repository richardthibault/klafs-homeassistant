# 🎛️ v1.1.0 - Preset Modes | Modes Preset | Preset-Modi | Modos Preset

**Read in your language:** [🇬🇧 English](#user-content-english) | [🇫🇷 Français](#user-content-français) | [🇩🇪 Deutsch](#user-content-deutsch) | [🇪🇸 Español](#user-content-español)

---

<a id="user-content-english"></a>
## 🇬🇧 English

### Added
- **Preset Modes**: Climate entity now supports mode selection directly in the interface
  - Sauna mode (10-100°C)
  - SANARIUM mode (40-75°C + humidity control)
  - Infrared mode (30-100°C)
- Mode selection integrated in climate interface (no need for separate switch)
- Automatic temperature limits based on selected mode
- Each mode remembers its preferred temperature (stored in sauna)

### Changed
- Climate entity now uses preset modes instead of requiring separate SANARIUM switch
- Temperature limits automatically adjust when changing modes
- Better user experience with unified interface

### What's New
This major update transforms the climate interface by integrating mode selection directly into the thermostat. No more separate SANARIUM switch - just select your mode from the climate entity and the temperature limits adjust automatically. Each mode remembers its preferred temperature, so switching between Sauna and SANARIUM is seamless.

**Key Benefits:**
- ✅ Unified interface - everything in one place
- ✅ No more temperature conflicts when switching modes
- ✅ Each mode remembers its preferred temperature
- ✅ Automatic temperature limit adjustment
- ✅ SANARIUM switch still available for backward compatibility

### Upgrade Instructions
**Via HACS (Recommended)**
1. Open HACS → Integrations
2. Find "Klafs Sauna" → Update
3. Restart Home Assistant
4. Open your sauna climate entity - you'll see a "Mode" button at the bottom

**Note:** The SANARIUM switch remains available for existing automations, but the new preset mode interface is recommended.

### Documentation
- 📖 [README](https://github.com/richardthibault/klafs-homeassistant/blob/main/README.md)
- 📝 [CHANGELOG](https://github.com/richardthibault/klafs-homeassistant/blob/main/CHANGELOG.md)
- 🔧 [Installation](https://github.com/richardthibault/klafs-homeassistant/blob/main/docs/en/INSTALLATION.md)
- 💡 [Examples](https://github.com/richardthibault/klafs-homeassistant/blob/main/docs/en/EXAMPLES.md)
- 🐛 [Troubleshooting](https://github.com/richardthibault/klafs-homeassistant/blob/main/docs/en/TROUBLESHOOTING.md)

---

<a id="user-content-français"></a>
## 🇫🇷 Français

### Ajouté
- **Modes Preset** : L'entité climate supporte maintenant la sélection de mode directement dans l'interface
  - Mode Sauna (10-100°C)
  - Mode SANARIUM (40-75°C + contrôle humidité)
  - Mode Infrarouge (30-100°C)
- Sélection de mode intégrée dans l'interface climate (plus besoin de switch séparé)
- Limites de température automatiques selon le mode sélectionné
- Chaque mode mémorise sa température préférée (stockée dans le sauna)

### Modifié
- L'entité climate utilise maintenant les modes preset au lieu de nécessiter un switch SANARIUM séparé
- Les limites de température s'ajustent automatiquement lors du changement de mode
- Meilleure expérience utilisateur avec interface unifiée

### Nouveautés
Cette mise à jour majeure transforme l'interface climate en intégrant la sélection de mode directement dans le thermostat. Plus besoin de switch SANARIUM séparé - il suffit de sélectionner votre mode depuis l'entité climate et les limites de température s'ajustent automatiquement. Chaque mode mémorise sa température préférée, rendant le passage entre Sauna et SANARIUM transparent.

**Avantages clés :**
- ✅ Interface unifiée - tout au même endroit
- ✅ Plus de conflits de température lors du changement de mode
- ✅ Chaque mode mémorise sa température préférée
- ✅ Ajustement automatique des limites de température
- ✅ Le switch SANARIUM reste disponible pour compatibilité ascendante

### Instructions de mise à jour
**Via HACS (Recommandé)**
1. Ouvrir HACS → Intégrations
2. Trouver "Klafs Sauna" → Mettre à jour
3. Redémarrer Home Assistant
4. Ouvrir votre entité climate sauna - vous verrez un bouton "Mode" en bas

**Note :** Le switch SANARIUM reste disponible pour les automatisations existantes, mais la nouvelle interface preset mode est recommandée.

### Documentation
- 📖 [README](https://github.com/richardthibault/klafs-homeassistant/blob/main/README.fr.md)
- 📝 [CHANGELOG](https://github.com/richardthibault/klafs-homeassistant/blob/main/CHANGELOG.fr.md)
- 🔧 [Installation](https://github.com/richardthibault/klafs-homeassistant/blob/main/docs/fr/INSTALLATION.md)
- 💡 [Exemples](https://github.com/richardthibault/klafs-homeassistant/blob/main/docs/fr/EXAMPLES.md)
- 🐛 [Dépannage](https://github.com/richardthibault/klafs-homeassistant/blob/main/docs/fr/TROUBLESHOOTING.md)

---

<a id="user-content-deutsch"></a>
## 🇩🇪 Deutsch

### Hinzugefügt
- **Preset-Modi**: Climate-Entität unterstützt jetzt Modusauswahl direkt in der Oberfläche
  - Sauna-Modus (10-100°C)
  - SANARIUM-Modus (40-75°C + Feuchtigkeitskontrolle)
  - Infrarot-Modus (30-100°C)
- Modusauswahl in Climate-Oberfläche integriert (kein separater Schalter erforderlich)
- Automatische Temperaturgrenzen basierend auf ausgewähltem Modus
- Jeder Modus merkt sich seine bevorzugte Temperatur (in Sauna gespeichert)

### Geändert
- Climate-Entität verwendet jetzt Preset-Modi anstelle eines separaten SANARIUM-Schalters
- Temperaturgrenzen passen sich automatisch beim Moduswechsel an
- Bessere Benutzererfahrung mit einheitlicher Oberfläche

### Was ist neu
Dieses große Update transformiert die Climate-Oberfläche durch Integration der Modusauswahl direkt in den Thermostat. Kein separater SANARIUM-Schalter mehr - wählen Sie einfach Ihren Modus aus der Climate-Entität und die Temperaturgrenzen passen sich automatisch an. Jeder Modus merkt sich seine bevorzugte Temperatur, sodass der Wechsel zwischen Sauna und SANARIUM nahtlos ist.

**Hauptvorteile:**
- ✅ Einheitliche Oberfläche - alles an einem Ort
- ✅ Keine Temperaturkonflikte mehr beim Moduswechsel
- ✅ Jeder Modus merkt sich seine bevorzugte Temperatur
- ✅ Automatische Anpassung der Temperaturgrenzen
- ✅ SANARIUM-Schalter bleibt für Abwärtskompatibilität verfügbar

### Aktualisierungsanleitung
**Via HACS (Empfohlen)**
1. HACS öffnen → Integrationen
2. "Klafs Sauna" finden → Aktualisieren
3. Home Assistant neu starten
4. Ihre Sauna-Climate-Entität öffnen - Sie sehen einen "Mode"-Button unten

**Hinweis:** Der SANARIUM-Schalter bleibt für bestehende Automatisierungen verfügbar, aber die neue Preset-Mode-Oberfläche wird empfohlen.

### Dokumentation
- 📖 [README](https://github.com/richardthibault/klafs-homeassistant/blob/main/README.de.md)
- 📝 [CHANGELOG](https://github.com/richardthibault/klafs-homeassistant/blob/main/CHANGELOG.de.md)
- 🔧 [Installation](https://github.com/richardthibault/klafs-homeassistant/blob/main/docs/de/INSTALLATION.md)
- 💡 [Beispiele](https://github.com/richardthibault/klafs-homeassistant/blob/main/docs/de/EXAMPLES.md)
- 🐛 [Fehlerbehebung](https://github.com/richardthibault/klafs-homeassistant/blob/main/docs/de/TROUBLESHOOTING.md)

---

<a id="user-content-español"></a>
## 🇪🇸 Español

### Añadido
- **Modos Preset**: La entidad climate ahora soporta selección de modo directamente en la interfaz
  - Modo Sauna (10-100°C)
  - Modo SANARIUM (40-75°C + control de humedad)
  - Modo Infrarrojo (30-100°C)
- Selección de modo integrada en interfaz climate (no necesita interruptor separado)
- Límites de temperatura automáticos según el modo seleccionado
- Cada modo recuerda su temperatura preferida (almacenada en sauna)

### Cambiado
- La entidad climate ahora usa modos preset en lugar de requerir un interruptor SANARIUM separado
- Los límites de temperatura se ajustan automáticamente al cambiar de modo
- Mejor experiencia de usuario con interfaz unificada

### Novedades
Esta actualización mayor transforma la interfaz climate integrando la selección de modo directamente en el termostato. No más interruptor SANARIUM separado - simplemente seleccione su modo desde la entidad climate y los límites de temperatura se ajustan automáticamente. Cada modo recuerda su temperatura preferida, haciendo que el cambio entre Sauna y SANARIUM sea fluido.

**Beneficios clave:**
- ✅ Interfaz unificada - todo en un lugar
- ✅ No más conflictos de temperatura al cambiar de modo
- ✅ Cada modo recuerda su temperatura preferida
- ✅ Ajuste automático de límites de temperatura
- ✅ El interruptor SANARIUM permanece disponible para compatibilidad hacia atrás

### Instrucciones de actualización
**Via HACS (Recomendado)**
1. Abrir HACS → Integraciones
2. Buscar "Klafs Sauna" → Actualizar
3. Reiniciar Home Assistant
4. Abrir su entidad climate sauna - verá un botón "Mode" en la parte inferior

**Nota:** El interruptor SANARIUM permanece disponible para automatizaciones existentes, pero se recomienda la nueva interfaz de modo preset.

### Documentación
- 📖 [README](https://github.com/richardthibault/klafs-homeassistant/blob/main/README.es.md)
- 📝 [CHANGELOG](https://github.com/richardthibault/klafs-homeassistant/blob/main/CHANGELOG.es.md)
- 🔧 [Instalación](https://github.com/richardthibault/klafs-homeassistant/blob/main/docs/es/INSTALLATION.md)
- 💡 [Ejemplos](https://github.com/richardthibault/klafs-homeassistant/blob/main/docs/es/EXAMPLES.md)
- 🐛 [Solución de problemas](https://github.com/richardthibault/klafs-homeassistant/blob/main/docs/es/TROUBLESHOOTING.md)

---

## 🔮 Future Plans

See [FUTURELOG](https://github.com/richardthibault/klafs-homeassistant/blob/main/FUTURELOG.md) for planned features in:
- [🇬🇧 English](https://github.com/richardthibault/klafs-homeassistant/blob/main/FUTURELOG.md)
- [🇫🇷 Français](https://github.com/richardthibault/klafs-homeassistant/blob/main/FUTURELOG.fr.md)
- [🇩🇪 Deutsch](https://github.com/richardthibault/klafs-homeassistant/blob/main/FUTURELOG.de.md)
- [🇪🇸 Español](https://github.com/richardthibault/klafs-homeassistant/blob/main/FUTURELOG.es.md)

---

**Full Changelog**: https://github.com/richardthibault/klafs-homeassistant/compare/v1.0.24...v1.1.0
