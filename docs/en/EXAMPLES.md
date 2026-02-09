**Read in other languages:** [English](../en/EXAMPLES.md) | [Français](../../EXAMPLES.md) | [Deutsch](../de/EXAMPLES.md) | [Español](../es/EXAMPLES.md)

# Usage Examples - Klafs Sauna

## Add a Control Card (Recommended) 🎨

To have all sauna controls grouped in a single card:

**Simple steps:**

1. Open a dashboard (or create a new one)
2. Click **+ Add Card**
3. Select **"Entities"**
4. Add these entities:
   - `climate.klafs_sauna` (Main thermostat)
   - `time.klafs_sauna_scheduled_start_time` (Scheduled start time)
   - `sensor.klafs_sauna_status` (Sauna status)
5. Click **"Save"**

**The card will display:**
- 🌡️ Temperature control with slider
- 🔥 Mode selection (Sauna / SANARIUM / Infrared)
- ⏰ Scheduled time selector (with scroll wheels)
- 🔘 On/Off buttons
- 📊 Real-time status

**YAML configuration (optional):**

If you prefer to configure in YAML:

```yaml
type: entities
title: Sauna Control
entities:
  - entity: climate.klafs_sauna
  - entity: time.klafs_sauna_scheduled_start_time
    name: Scheduled Start
  - entity: sensor.klafs_sauna_status
    name: Status
```

---

## Available Services

### 1. Power On with PIN Code

```yaml
service: klafs.power_on_with_pin
target:
  entity_id: climate.klafs_sauna
data:
  pin: "1234"
```

### 2. Set Humidity Level (SANARIUM)

```yaml
service: klafs.set_humidity_level
target:
  entity_id: climate.klafs_sauna
data:
  humidity_level: 7  # 1-10
```

### 3. Schedule Start Time

```yaml
service: klafs.set_start_time
target:
  entity_id: climate.klafs_sauna
data:
  hour: 18
  minute: 30
```

## Advanced Automations

### Weekend Morning Routine

```yaml
automation:
  - alias: "Weekend Morning Sauna"
    trigger:
      - platform: time
        at: "08:00:00"
    condition:
      - condition: time
        weekday:
          - sat
          - sun
      - condition: state
        entity_id: person.you
        state: "home"
    action:
      # Enable SANARIUM mode
      - service: switch.turn_on
        target:
          entity_id: switch.klafs_sauna_sanarium_mode
      # Set temperature and humidity
      - service: climate.set_temperature
        target:
          entity_id: climate.klafs_sauna
        data:
          temperature: 60
      - service: klafs.set_humidity_level
        target:
          entity_id: climate.klafs_sauna
        data:
          humidity_level: 8
      # Turn on
      - service: climate.turn_on
        target:
          entity_id: climate.klafs_sauna
```

### Smart Preheating Based on Location

```yaml
automation:
  - alias: "Preheat Sauna When Coming Home"
    trigger:
      - platform: zone
        entity_id: person.you
        zone: zone.work
        event: leave
    condition:
      - condition: time
        after: "17:00:00"
        before: "20:00:00"
      - condition: time
        weekday:
          - mon
          - tue
          - wed
          - thu
          - fri
    action:
      # Calculate arrival time (30 min commute)
      - service: klafs.set_start_time
        target:
          entity_id: climate.klafs_sauna
        data:
          hour: "{{ now().hour }}"
          minute: "{{ (now().minute + 30) % 60 }}"
      # Set to classic Sauna mode
      - service: switch.turn_off
        target:
          entity_id: switch.klafs_sauna_sanarium_mode
      - service: climate.set_temperature
        target:
          entity_id: climate.klafs_sauna
        data:
          temperature: 85
      - service: climate.turn_on
        target:
          entity_id: climate.klafs_sauna
      # Notification
      - service: notify.mobile_app
        data:
          message: "Sauna preheating, ready when you arrive!"
```

### Automatic Shutdown After Use

```yaml
automation:
  - alias: "Turn Off Sauna After 2 Hours"
    trigger:
      - platform: state
        entity_id: sensor.klafs_sauna_status
        to: "Ready"
        for:
          hours: 2
    action:
      - service: climate.turn_off
        target:
          entity_id: climate.klafs_sauna
      - service: notify.mobile_app
        data:
          message: "Sauna automatically turned off after 2 hours"
```

### Alert if Sauna is On and Nobody Home

```yaml
automation:
  - alias: "Alert Sauna On Without Anyone Home"
    trigger:
      - platform: state
        entity_id: climate.klafs_sauna
        to: "heat"
        for:
          minutes: 10
    condition:
      - condition: state
        entity_id: zone.home
        state: "0"  # Nobody home
    action:
      - service: notify.mobile_app
        data:
          message: "⚠️ The sauna is on but nobody is home!"
          data:
            actions:
              - action: "TURN_OFF_SAUNA"
                title: "Turn Off"
              - action: "IGNORE"
                title: "Ignore"

  - alias: "Action Turn Off Sauna"
    trigger:
      - platform: event
        event_type: mobile_app_notification_action
        event_data:
          action: "TURN_OFF_SAUNA"
    action:
      - service: climate.turn_off
        target:
          entity_id: climate.klafs_sauna
```

### Weekly Schedule

```yaml
automation:
  # Monday, Wednesday, Friday: Classic Sauna
  - alias: "Classic Sauna MWF"
    trigger:
      - platform: time
        at: "19:00:00"
    condition:
      - condition: time
        weekday:
          - mon
          - wed
          - fri
    action:
      - service: switch.turn_off
        target:
          entity_id: switch.klafs_sauna_sanarium_mode
      - service: climate.set_temperature
        target:
          entity_id: climate.klafs_sauna
        data:
          temperature: 90
      - service: climate.turn_on
        target:
          entity_id: climate.klafs_sauna

  # Tuesday, Thursday: Gentle SANARIUM
  - alias: "Gentle SANARIUM TT"
    trigger:
      - platform: time
        at: "19:00:00"
    condition:
      - condition: time
        weekday:
          - tue
          - thu
    action:
      - service: switch.turn_on
        target:
          entity_id: switch.klafs_sauna_sanarium_mode
      - service: climate.set_temperature
        target:
          entity_id: climate.klafs_sauna
        data:
          temperature: 55
      - service: klafs.set_humidity_level
        target:
          entity_id: climate.klafs_sauna
        data:
          humidity_level: 5
      - service: climate.turn_on
        target:
          entity_id: climate.klafs_sauna
```

### Integration with Presence Sensor

```yaml
automation:
  - alias: "Start Sauna with Presence"
    trigger:
      - platform: state
        entity_id: binary_sensor.presence_bathroom
        to: "on"
        for:
          minutes: 5
    condition:
      - condition: time
        after: "18:00:00"
        before: "22:00:00"
      - condition: state
        entity_id: input_boolean.sauna_auto_mode
        state: "on"
    action:
      - service: climate.turn_on
        target:
          entity_id: climate.klafs_sauna
```

## Lovelace Cards

### Simple Card

```yaml
type: thermostat
entity: climate.klafs_sauna
```

### Detailed Card

```yaml
type: vertical-stack
cards:
  - type: thermostat
    entity: climate.klafs_sauna
  - type: entities
    entities:
      - entity: sensor.klafs_sauna_temperature
        name: Current Temperature
      - entity: sensor.klafs_sauna_humidity
        name: Humidity
      - entity: sensor.klafs_sauna_status
        name: Status
      - entity: switch.klafs_sauna_sanarium_mode
        name: SANARIUM Mode
```

### Card with Advanced Controls

```yaml
type: vertical-stack
cards:
  - type: thermostat
    entity: climate.klafs_sauna
    name: Sauna Control
  
  - type: horizontal-stack
    cards:
      - type: button
        entity: switch.klafs_sauna_sanarium_mode
        name: SANARIUM
        icon: mdi:water-percent
        tap_action:
          action: toggle
      
      - type: button
        name: Sauna 90°
        icon: mdi:fire
        tap_action:
          action: call-service
          service: climate.set_temperature
          service_data:
            entity_id: climate.klafs_sauna
            temperature: 90
            hvac_mode: heat
      
      - type: button
        name: SANARIUM 60°
        icon: mdi:water
        tap_action:
          action: call-service
          service: script.sanarium_mode
  
  - type: entities
    entities:
      - entity: sensor.klafs_sauna_temperature
        name: Temperature
        icon: mdi:thermometer
      - entity: sensor.klafs_sauna_humidity
        name: Humidity
        icon: mdi:water-percent
      - entity: sensor.klafs_sauna_status
        name: Status
```

### Card with Humidity Slider

```yaml
type: vertical-stack
cards:
  - type: thermostat
    entity: climate.klafs_sauna
  
  - type: conditional
    conditions:
      - entity: switch.klafs_sauna_sanarium_mode
        state: "on"
    card:
      type: entities
      entities:
        - type: custom:slider-entity-row
          entity: input_number.sauna_humidity
          name: SANARIUM Humidity
          min: 1
          max: 10
          step: 1
```

## Useful Scripts

### SANARIUM Mode Script

```yaml
script:
  sanarium_mode:
    alias: "Activate SANARIUM Mode"
    sequence:
      - service: switch.turn_on
        target:
          entity_id: switch.klafs_sauna_sanarium_mode
      - service: climate.set_temperature
        target:
          entity_id: climate.klafs_sauna
        data:
          temperature: 60
      - service: klafs.set_humidity_level
        target:
          entity_id: climate.klafs_sauna
        data:
          humidity_level: 7
      - service: climate.turn_on
        target:
          entity_id: climate.klafs_sauna
```

### Finnish Sauna Script

```yaml
script:
  finnish_sauna:
    alias: "Finnish Sauna"
    sequence:
      - service: switch.turn_off
        target:
          entity_id: switch.klafs_sauna_sanarium_mode
      - service: climate.set_temperature
        target:
          entity_id: climate.klafs_sauna
        data:
          temperature: 90
      - service: climate.turn_on
        target:
          entity_id: climate.klafs_sauna
```

### Emergency Stop Script

```yaml
script:
  sauna_emergency_stop:
    alias: "Sauna Emergency Stop"
    sequence:
      - service: climate.turn_off
        target:
          entity_id: climate.klafs_sauna
      - service: notify.all_devices
        data:
          message: "🚨 Sauna emergency shutdown"
```

## Integration with Google Assistant / Alexa

### Scenes for Voice Commands

```yaml
scene:
  - name: "Classic Sauna"
    entities:
      climate.klafs_sauna:
        state: heat
        temperature: 85
      switch.klafs_sauna_sanarium_mode:
        state: off

  - name: "Gentle Sauna"
    entities:
      climate.klafs_sauna:
        state: heat
        temperature: 60
      switch.klafs_sauna_sanarium_mode:
        state: on
```

Voice commands:
- "Ok Google, activate Classic Sauna scene"
- "Alexa, turn off the sauna"
- "Ok Google, set the sauna to 80 degrees"
