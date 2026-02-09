# Changelog

**In anderen Sprachen lesen:** [English](CHANGELOG.md) | [Français](CHANGELOG.fr.md) | **Deutsch** | [Español](CHANGELOG.es.md)

Alle wichtigen Änderungen an diesem Projekt werden in dieser Datei dokumentiert.

Das Format basiert auf [Keep a Changelog](https://keepachangelog.com/de/1.0.0/),
und dieses Projekt folgt [Semantic Versioning](https://semver.org/lang/de/).

**Für geplante zukünftige Funktionen siehe [FUTURELOG.de.md](FUTURELOG.de.md)**

---

## [1.0.4] - 2026-02-09

### Hinzugefügt
- **Benutzerdefiniertes Icon-Set**: Integration enthält jetzt benutzerdefinierte Symbole mit `klafs:` Präfix
  - `klafs:sauna` - Standard/neutraler Zustand
  - `klafs:sauna-heating` - Sauna heizt auf (mit Hitzewellen)
  - `klafs:sauna-ready` - Sauna ist bereit (volles Thermometer + Häkchen)
  - `klafs:sauna-off` - Sauna ist ausgeschaltet (ausgegraute Elemente)
  - Symbole ändern sich automatisch je nach Saunastatus
  - Alle Symbole verwenden `fill="currentColor"` für Theme-Kompatibilität
  - Funktioniert mit Home Assistant ≥ 2023.x
- **Mehrsprachige Dokumentation**: Dokumentation für benutzerdefinierte Symbole in 4 Sprachen (EN/FR/DE/ES)
- **Automatisches Icon-Mapping**: Symbole ändern sich automatisch basierend auf Entitätsstatus
  - Keine Konfiguration erforderlich
  - Funktioniert mit Sensor- und Climate-Entitäten

### Geändert
- Symbole von `icons/` nach `frontend/icons/` verschoben
- Symbole werden jetzt als statische Dateien über `/local/klafs/icons/` bereitgestellt
- `icon_mapping.py` für zentralisierte Icon-Status-Verwaltung hinzugefügt

### Technisch
- `frontend/iconset.js` für Icon-Registrierung im Home Assistant Frontend hinzugefügt
- `__init__.py` aktualisiert, um statische Pfade zu registrieren und Iconset zu laden
- `sensor.py` und `climate.py` aktualisiert, um dynamische Icon-Eigenschaften zu verwenden
- Symbole passen sich automatisch an helle/dunkle Themes an

---

## [1.0.3] - 2026-02-09

### Behoben
- **Icon-Anzeigeproblem**: Benutzerdefinierte `klafs:sauna-*` Symbole durch Standard-MDI-Symbole ersetzt
  - Benutzerdefinierte SVG-Symbole werden im Repository für zukünftige Verwendung aufbewahrt
  - Jetzt werden `mdi:sauna` (Standard/aus), `mdi:fire` (Heizen), `mdi:check-circle` (Bereit) verwendet
  - Symbole werden jetzt korrekt ohne zusätzliche Konfiguration angezeigt

### Technisch
- Benutzerdefinierte Home Assistant Integrationen können nicht einfach benutzerdefinierte Icon-Sets ohne externe Abhängigkeiten einbetten
- Standard-MDI-Symbole bieten bessere Kompatibilität und sofortige Funktionalität

---

Vollständiges Changelog (EN): [CHANGELOG.md](CHANGELOG.md)
