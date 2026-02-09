# Changelog

**In anderen Sprachen lesen:** [English](CHANGELOG.md) | [Français](CHANGELOG.fr.md) | **Deutsch** | [Español](CHANGELOG.es.md)

Alle wichtigen Änderungen an diesem Projekt werden in dieser Datei dokumentiert.

Das Format basiert auf [Keep a Changelog](https://keepachangelog.com/de/1.0.0/),
und dieses Projekt folgt [Semantic Versioning](https://semver.org/lang/de/).

**Für geplante zukünftige Funktionen siehe [FUTURELOG.de.md](FUTURELOG.de.md)**

---

## [1.0.23] - 2026-02-09

### Geändert
- **Optimiertes Icon-Layout**: Bank entfernt, um Heizung und Steine zu vergrößern
- Symbole jetzt sichtbarer und klarer
- Heizung und Steine zentriert und vergrößert für bessere Sichtbarkeit

---

## [1.0.22] - 2026-02-09

### Behoben
- **Reine SVG-Paths**: Alle SVG-Elemente in Path-Befehle für Kompatibilität konvertiert
- Symbole werden jetzt korrekt mit `window.customIconsets` API angezeigt (bewährt in v1.0.19)
- Alle visuellen Elemente erhalten: Heizkörperstäbe, Heizsteine, Bank, Thermometer, Hitzewellen, Checkmark

### Technische Details
- Alle `<rect>`, `<circle>`, `<line>` Elemente in reine `<path>` Befehle konvertiert
- Monochromes Rendering (einzelnes `currentColor` - keine Mehrfarben-Unterstützung)
- Verwendet `window.customIconsets` + `window.customIcons` APIs
- Thermometer zeigt verschiedene Füllstände: 50% (Standard), 75% (Heizen), 100% (Bereit), 0% (Aus)

### Kompromisse
- Heizkörperstäbe gleiche Farbe wie Rest (keine graue Unterscheidung)
- Keine Opazitätsvariationen (alles solid)
- Einfacher als v1.0.20-21 aber funktional

---

## [1.0.21] - 2026-02-09

### Behoben
- **Offizielle HA-API**: Wechsel zu `ha-iconset-svg` Web Components (offizielle Home Assistant Methode)
- Symbole werden jetzt korrekt mit allen visuellen Elementen gerendert (Heizkörper, Thermometer, Hitzewellen)
- Behebt SVG-Path-Parsing-Fehler aus v1.0.20

### Technische Details
- Verwendet `<ha-iconset-svg>` Web Component mit Inline-SVG-Definitionen
- Akzeptiert vollständiges SVG-Markup (`<rect>`, `<circle>`, `<line>`, `<path>`)
- Bewahrt alle Attribute: Farben, Strokes, Opazität
- Keine externen Dateien erforderlich (HACS-kompatibel)
- Offizielle HA-API für benutzerdefinierte Symbole seit 2020

---

## [1.0.20] - 2026-02-09

### Behoben
- **Vollständiges Icon-Rendering**: Vollständige SVG-Symbole mit Heizkörper, Thermometer und Hitzewellen wiederhergestellt
- Symbole enthalten jetzt alle visuellen Details: Elektrische Heizstäbe (grau), Heizsteine, Bank, Thermometer mit Füllständen
- `sauna-heating` zeigt animierte Hitzewellen über den Steinen
- `sauna-ready` zeigt Checkmark-Indikator
- `sauna-off` verwendet reduzierte Deckkraft für inaktiven Zustand

### Technische Details
- Vollständiges SVG-Markup in iconset.js eingebettet (Inline-Ansatz)
- Parse SVG um innerHTML und viewBox für HA Icon API zu extrahieren
- Bewahrt Farben (`currentColor`, `#888`), Strokes und Opacity-Attribute
- Keine externen SVG-Dateien erforderlich (HACS-kompatibel)

---

## [1.0.19] - 2026-02-09

### Behoben
- **Duale API-Kompatibilität**: Unterstützung für beide APIs `customIconsets` und `customIcons` hinzugefügt
- Synchrone Icon-Funktionen für bessere Kompatibilität über HA-Versionen hinweg
- Symbole funktionieren jetzt mit alten und modernen Home Assistant Icon-Systemen

### Technische Details
- Registriert mit `window.customIconsets["klafs"]` (Legacy-API)
- Registriert mit `window.customIcons["klafs"]` (Alternative API)
- Beide geben `{path, viewBox}` Objekte synchron zurück
- Maximale Kompatibilität mit HA 2020-2024+ Versionen

---

## [1.0.18] - 2026-02-09

### Behoben
- **Moderne HA-API**: Verwendung von `async_register_static_paths` mit `StaticPathConfig` (offizielle HA 2024+ Methode)
- Veraltetes `register_static_path` behoben, das AttributeError in neueren Home Assistant-Versionen verursachte
- Funktion jetzt korrekt async mit `await`-Aufruf im Setup

### Technische Details
- Import von `StaticPathConfig` aus `homeassistant.components.http`
- Import von `add_extra_js_url` aus `homeassistant.components.frontend`
- Verwendung von `await hass.http.async_register_static_paths([StaticPathConfig(...)])`
- Symbole sollten jetzt korrekt unter `/klafs/iconset.js` geladen werden

---

## [1.0.7] - 2026-02-09

### Behoben
- **Icon-Lademethode**: Veraltetes `add_extra_js_url()` durch manuelle Lovelace-Ressourcen-Registrierung ersetzt
- **Statische Pfad-Registrierung**: Fehlerhafte Dateipfad-Registrierung für iconset.js korrigiert
- **Icon-Registrierung**: Verbesserte Kompatibilität mit Home Assistant 2023+ Icon-System

### Geändert
- Benutzerdefinierte Symbole erfordern jetzt manuelle Lovelace-Ressourcen-Hinzufügung (siehe CUSTOM_ICONS.de.md)
- iconset.js mit mehreren Registrierungsmethoden für bessere Kompatibilität aktualisiert
- Verbesserte Protokollierung für Icon-Registrierungs-Debugging

### Dokumentation
- Umfassende Fehlerbehebungsanleitung in allen 4 Sprachen hinzugefügt (EN/FR/DE/ES)
- Schritt-für-Schritt-Anleitung zum Hinzufügen von Lovelace-Ressourcen
- Browser-Konsolen-Debugging-Tipps

---

## [1.0.6] - 2026-02-09

### Behoben
- **HACS-Kompatibilität**: SVG-Symbole in Integrations-Root verschoben für korrekte HACS-Bereitstellung
- HACS kopierte das Unterverzeichnis `frontend/icons/` nicht, was zu fehlenden Symbolen nach der Installation führte

---

## [1.0.5] - 2026-02-09

### Behoben
- **Icon-Registrierungs-Timing**: Symbole werden jetzt nach dem Laden der Plattformen registriert, um eine ordnungsgemäße Initialisierung sicherzustellen
- Dies behebt das Problem, dass benutzerdefinierte Symbole nicht im Frontend angezeigt wurden

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
