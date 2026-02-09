# Changelog

**In anderen Sprachen lesen:** [English](CHANGELOG.md) | [Français](CHANGELOG.fr.md) | **Deutsch** | [Español](CHANGELOG.es.md)

Alle wichtigen Änderungen an diesem Projekt werden in dieser Datei dokumentiert.

**Für geplante zukünftige Funktionen siehe [FUTURELOG.de.md](FUTURELOG.de.md)**

Für die vollständige Versionshistorie siehe die [englische Version](CHANGELOG.md).

---

## [1.0.1] - 2026-02-09

### Behoben
- **Kritischer Wiederverbindungsfehler**: Sauna wurde nach WLAN-Verbindungsverlust nicht mehr erkannt
  - Koordinator behält Saunen jetzt auch bei Trennung in den Daten
  - Verbesserte Fehlerbehandlung pro einzelner Sauna
  - Entitäten bleiben verfügbar und verbinden sich automatisch wieder
  - Keine Deinstallation/Neuinstallation der Integration nach Verbindungsverlust mehr erforderlich

---

## [1.0.0] - 2026-01-28

### Hinzugefügt
- Erste Integration mit Klafs API
- **Multi-Sauna-Unterstützung**: Mehrere Saunen von einem Konto verwalten
- **Individueller PIN-Code pro Sauna**: Jede Sauna kann ihren eigenen PIN haben
- **3-Schritt-Konfiguration**: Anmeldedaten → Sauna-Auswahl → PIN-Konfiguration
- Climate-Entität (Thermostat) zur Steuerung jeder Sauna
- Temperatur-, Feuchtigkeits- und Statussensoren pro Sauna
- Schalter zum Umschalten zwischen Sauna- und SANARIUM-Modi
- Dienste: `power_on_with_pin`, `set_humidity_level`, `set_start_time`
- Unterstützung für Modi: Klassische Sauna, SANARIUM, Infrarot
- Automatisches Polling alle 60 Sekunden
- Französische und englische Übersetzungen
- Vollständige Dokumentation
- HACS-Unterstützung

### Funktionen
- Temperaturregelung (10-100°C je nach Modus)
- Fernbedienung Ein/Aus
- Echtzeit-Überwachung von Temperatur und Luftfeuchtigkeit
- Sauna-Verbindungsstatus
- "Bereit"-Anzeige wenn Sauna bereit ist

### Sicherheit
- Sichere Speicherung der Anmeldedaten
- Obligatorische PIN-Code-Unterstützung zum Einschalten
- Nur HTTPS-Kommunikation

---

## Vollständige Versionshinweise

Für detaillierte Versionshinweise, Migrationsanleitungen und vollständige Änderungslisten siehe die [englische Version](CHANGELOG.md).

---

**Legende:**
- `Hinzugefügt`: Neue Funktionen
- `Geändert`: Änderungen an bestehenden Funktionen
- `Veraltet`: Bald zu entfernende Funktionen
- `Entfernt`: Entfernte Funktionen
- `Behoben`: Fehlerbehebungen
- `Sicherheit`: Behebung von Sicherheitslücken
