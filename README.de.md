# Klafs Sauna Integration für Home Assistant

**In anderen Sprachen lesen:** [English](README.md) | [Français](README.fr.md) | **Deutsch** | [Español](README.es.md)

[![hacs_badge](https://img.shields.io/badge/HACS-Custom-orange.svg)](https://github.com/custom-components/hacs)
[![GitHub release](https://img.shields.io/github/release/richardthibault/klafs-homeassistant.svg)](https://github.com/richardthibault/klafs-homeassistant/releases)
[![License](https://img.shields.io/github/license/richardthibault/klafs-homeassistant.svg)](LICENSE)

Diese benutzerdefinierte Integration ermöglicht es Ihnen, Ihre Klafs-Sauna über Home Assistant mit der Klafs Cloud-API zu steuern.

![Klafs Sauna](https://www.klafs.com/typo3conf/ext/klafs_sitepackage/Resources/Public/Images/logo.svg)

## Funktionen

- **Klimasteuerung**: Steuern Sie die Saunatemperatur wie ein Thermostat
- **Sensoren**: Überwachen Sie Temperatur, Luftfeuchtigkeit und Status in Echtzeit
- **Modi**: Wechseln Sie zwischen Sauna- und SANARIUM®-Modi
- **Ein/Aus**: Steuern Sie die Sauna-Stromversorgung aus der Ferne
- **Multi-Sauna-Unterstützung**: Verwalten Sie mehrere Saunen von einem Konto aus
- **Individuelle PINs**: Jede Sauna kann ihren eigenen PIN-Code haben

## Voraussetzungen

- Ein Klafs Sauna App-Konto
- Eine Klafs-Sauna mit WLAN-Modul und "KLAFS Sauna App"-Option
- Home Assistant 2023.1 oder höher

## Installation

### Installation über HACS (Empfohlen)

1. Öffnen Sie HACS in Home Assistant
2. Gehen Sie zu "Integrationen"
3. Klicken Sie auf die drei Punkte oben rechts
4. Wählen Sie "Benutzerdefinierte Repositories"
5. URL hinzufügen: `https://github.com/richardthibault/klafs-homeassistant`
6. Suchen Sie nach "Klafs Sauna" und installieren Sie
7. Starten Sie Home Assistant neu
8. Konfigurieren Sie die Integration über die Benutzeroberfläche

### Manuelle Installation

1. Kopieren Sie den Ordner `custom_components/klafs` in Ihren `config/custom_components/` Ordner
2. Starten Sie Home Assistant neu
3. Gehen Sie zu Konfiguration > Integrationen
4. Klicken Sie auf "+ Integration hinzufügen"
5. Suchen Sie nach "Klafs Sauna"
6. Geben Sie Ihre Klafs Sauna App-Anmeldedaten ein

## Konfiguration

Die Integration wird vollständig über die Home Assistant-Benutzeroberfläche in 3 Schritten konfiguriert:

### Schritt 1: Anmeldedaten
- **Benutzername**: Ihr Klafs Sauna App-Benutzername
- **Passwort**: Ihr Klafs Sauna App-Passwort

### Schritt 2: Sauna-Auswahl
- Wählen Sie die Saunen aus, die Sie über Home Assistant steuern möchten
- Sie können eine oder mehrere Saunen auswählen
- Jede Sauna erscheint als separates Gerät

### Schritt 3: PIN-Codes
- **PIN-Code** (optional): Der 4-stellige PIN-Code, der auf jeder Sauna konfiguriert ist
- Für jede Sauna kann ein anderer PIN konfiguriert werden
- Erforderlich, um die Sauna aus der Ferne einzuschalten

⚠️ **Wichtig**: 
- Klafs sperrt das Konto nach 3 fehlgeschlagenen Anmeldeversuchen. Stellen Sie sicher, dass Sie die richtigen Anmeldedaten eingeben.
- Jeder PIN-Code muss auf der entsprechenden Sauna über das Bedienfeld konfiguriert werden, bevor er verwendet werden kann.
- Ohne PIN können Sie den Saunastatus sehen, aber nicht aus der Ferne einschalten.
- Wenn Sie mehrere Saunen haben, kann jede ihren eigenen PIN-Code haben.

## Erstellte Entitäten

Für jede erkannte Sauna erstellt die Integration:

### Climate (Thermostat)
- **Entität**: `climate.klafs_sauna_XXXXXXXX`
- **Funktionen**: Temperaturregelung, Ein/Aus
- **Attribute**:
  - Aktueller Modus (Sauna/SANARIUM®/Infrarot)
  - Verbindungsstatus
  - Betriebsbereit
  - Luftfeuchtigkeitsstufe (nur SANARIUM®)

### Sensoren
- **Temperatur**: `sensor.klafs_sauna_XXXXXXXX_temperature`
- **Luftfeuchtigkeit**: `sensor.klafs_sauna_XXXXXXXX_humidity`
- **Status**: `sensor.klafs_sauna_XXXXXXXX_status` (Aus/Heizen/Bereit/Getrennt)

### Schalter
- **SANARIUM®-Modus**: `switch.klafs_sauna_XXXXXXXX_sanarium_mode`

## Verwendung

### Grundlegende Steuerung

```yaml
# Sauna auf 80°C einschalten (verwendet konfigurierten PIN)
service: climate.set_temperature
target:
  entity_id: climate.klafs_sauna_XXXXXXXX
data:
  temperature: 80
  hvac_mode: heat

# Mit spezifischem PIN einschalten
service: klafs.power_on_with_pin
target:
  entity_id: climate.klafs_sauna_XXXXXXXX
data:
  pin: "1234"

# Sauna ausschalten
service: climate.turn_off
target:
  entity_id: climate.klafs_sauna_XXXXXXXX

# Luftfeuchtigkeitsstufe einstellen (nur SANARIUM)
service: klafs.set_humidity_level
target:
  entity_id: climate.klafs_sauna_XXXXXXXX
data:
  humidity_level: 7

# Startzeit planen
service: klafs.set_start_time
target:
  entity_id: climate.klafs_sauna_XXXXXXXX
data:
  hour: 18
  minute: 30
```

### Automatisierungen

Siehe [EXAMPLES.md](EXAMPLES.md) für weitere Automatisierungsbeispiele und Lovelace-Karten.

## Vollständige Dokumentation

- 📖 [Schnellstartanleitung](QUICK_START.md)
- 🔧 [Detaillierte Installationsanleitung](INSTALLATION.md)
- 💡 [Automatisierungsbeispiele](EXAMPLES.md)
- 🔍 [API-Dokumentation](API_DOCUMENTATION.md)
- 🐛 [Fehlerbehebungsanleitung](TROUBLESHOOTING.md)
- 🏗️ [Multi-Sauna-Unterstützung](MULTI_SAUNA_SUPPORT.md)
- 🤝 [Beitragsanleitung](CONTRIBUTING.md)

## Klafs API

Diese Integration verwendet die Klafs Web-API (ASP.NET MVC-Anwendung):

- **Basis-URL**: `https://sauna-app.klafs.com`
- **Authentifizierung**: Cookie-basiert nach Login
- **Polling**: Aktualisierung standardmäßig alle 60 Sekunden

## Temperaturgrenzwerte

- **Sauna-Modus**: 10°C - 100°C
- **SANARIUM®-Modus**: 40°C - 75°C
- **Infrarot-Modus**: 30°C - 100°C

## Fehlerbehebung

### Integration verbindet sich nicht

1. Überprüfen Sie Ihre Anmeldedaten in der Klafs Sauna App
2. Stellen Sie sicher, dass Ihr Konto nicht gesperrt ist (max. 3 Versuche)
3. Überprüfen Sie die Home Assistant-Protokolle: `Konfiguration > Protokolle`

### Sauna erscheint nicht

1. Stellen Sie sicher, dass Ihre Sauna in der Klafs-App richtig konfiguriert ist
2. Überprüfen Sie, ob das WLAN-Modul verbunden ist
3. Starten Sie die Integration neu

### Befehle funktionieren nicht

1. Überprüfen Sie, ob die Sauna verbunden ist (`isConnected: true`)
2. Stellen Sie sicher, dass Sie einen PIN-Code auf Ihrer Sauna konfiguriert haben
3. Überprüfen Sie, ob die Saunatür kontrolliert wurde

Weitere Hilfe finden Sie in der [Fehlerbehebungsanleitung](TROUBLESHOOTING.md).

## Mitwirken

Beiträge sind willkommen! Fühlen Sie sich frei:

- Fehler zu melden
- Neue Funktionen vorzuschlagen
- Pull Requests einzureichen

Siehe [CONTRIBUTING.md](CONTRIBUTING.md) für weitere Details.

## Lizenz

MIT-Lizenz - Siehe [LICENSE](LICENSE)

## Danksagungen

- Basierend auf API-Forschung der OpenHAB-Community
- Inspiriert vom [IPSymconKlafsSaunaControl](https://github.com/Pommespanzer/IPSymconKlafsSaunaControl)-Projekt

## Haftungsausschluss

Diese Integration ist inoffiziell und nicht mit Klafs GmbH verbunden. Verwendung auf eigene Gefahr.
