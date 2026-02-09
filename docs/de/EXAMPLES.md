**In anderen Sprachen lesen:** [English](../en/EXAMPLES.md) | [Français](../../EXAMPLES.md) | [Deutsch](../de/EXAMPLES.md) | [Español](../es/EXAMPLES.md)

# Nutzungsbeispiele - Klafs Sauna

## Zusammenfassung

Dieses Dokument enthält umfassende Beispiele für die Verwendung der Klafs Sauna Integration in Home Assistant, einschließlich:

- **Verfügbare Dienste**: Einschalten mit PIN, Luftfeuchtigkeit einstellen, Startzeit programmieren
- **Erweiterte Automatisierungen**: Wochenend-Morgenroutine, intelligentes Vorheizen basierend auf Standort, automatisches Ausschalten
- **Sicherheitsautomatisierungen**: Warnungen wenn niemand zu Hause ist
- **Wochenpläne**: Verschiedene Modi für verschiedene Wochentage
- **Lovelace-Karten**: Einfache und erweiterte UI-Konfigurationen
- **Nützliche Skripte**: SANARIUM-Modus, Finnische Sauna, Notausschaltung
- **Sprachassistenten-Integration**: Google Assistant und Alexa Szenen

## Vollständige Dokumentation

Für detaillierte Beispiele mit vollständigem Code, siehe die [englische Version](../en/EXAMPLES.md).

## Schnellstart-Beispiele

### Sauna mit PIN einschalten

```yaml
service: klafs.power_on_with_pin
target:
  entity_id: climate.klafs_sauna
data:
  pin: "1234"
```

### SANARIUM-Modus aktivieren

```yaml
service: switch.turn_on
target:
  entity_id: switch.klafs_sauna_sanarium_mode
```

### Luftfeuchtigkeit einstellen

```yaml
service: klafs.set_humidity_level
target:
  entity_id: climate.klafs_sauna
data:
  humidity_level: 7  # 1-10
```

### Einfache Thermostat-Karte

```yaml
type: thermostat
entity: climate.klafs_sauna
```

## Weitere Informationen

- [Vollständige Beispiele (EN)](../en/EXAMPLES.md) - Alle Automatisierungen und Konfigurationen
- [Fehlerbehebung (DE)](TROUBLESHOOTING.md) - Probleme lösen
- [Hauptdokumentation](../../README.md) - Installations- und Konfigurationsanleitung
