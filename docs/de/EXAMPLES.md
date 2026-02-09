**In anderen Sprachen lesen:** [English](../en/EXAMPLES.md) | [Français](../../EXAMPLES.md) | [Deutsch](../de/EXAMPLES.md) | [Español](../es/EXAMPLES.md)

# Nutzungsbeispiele - Klafs Sauna

## Steuerkarte hinzufügen (Empfohlen) 🎨

Um alle Sauna-Steuerelemente in einer Karte zu gruppieren:

**Einfache Schritte:**

1. Öffnen Sie ein Dashboard (oder erstellen Sie ein neues)
2. Klicken Sie auf **+ Karte hinzufügen**
3. Wählen Sie **"Entitäten"**
4. Fügen Sie diese Entitäten hinzu:
   - `climate.klafs_sauna` (Hauptthermostat)
   - `time.klafs_sauna_scheduled_start_time` (Geplante Startzeit)
   - `sensor.klafs_sauna_status` (Sauna-Status)
5. Klicken Sie auf **"Speichern"**

**Die Karte zeigt:**
- 🌡️ Temperatursteuerung mit Schieberegler
- 🔥 Modusauswahl (Sauna / SANARIUM / Infrarot)
- ⏰ Zeitplaner (mit Scrollrädern)
- 🔘 Ein/Aus-Tasten
- 📊 Echtzeit-Status

**YAML-Konfiguration (optional):**

Wenn Sie YAML bevorzugen:

```yaml
type: entities
title: Sauna-Steuerung
entities:
  - entity: climate.klafs_sauna
  - entity: time.klafs_sauna_scheduled_start_time
    name: Geplanter Start
  - entity: sensor.klafs_sauna_status
    name: Status
```

---

## Verfügbare Dienste

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
