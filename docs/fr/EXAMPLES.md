# Exemples d'utilisation - Klafs Sauna

## Services disponibles

### 1. Allumer avec code PIN

```yaml
service: klafs.power_on_with_pin
target:
  entity_id: climate.klafs_sauna
data:
  pin: "1234"
```

### 2. Définir le niveau d'humidité (SANARIUM)

```yaml
service: klafs.set_humidity_level
target:
  entity_id: climate.klafs_sauna
data:
  humidity_level: 7  # 1-10
```

### 3. Programmer l'heure de démarrage

```yaml
service: klafs.set_start_time
target:
  entity_id: climate.klafs_sauna
data:
  hour: 18
  minute: 30
```

## Automatisations avancées

### Routine matinale week-end

```yaml
automation:
  - alias: "Sauna matinal week-end"
    trigger:
      - platform: time
        at: "08:00:00"
    condition:
      - condition: time
        weekday:
          - sat
          - sun
      - condition: state
        entity_id: person.vous
        state: "home"
    action:
      # Activer mode SANARIUM
      - service: switch.turn_on
        target:
          entity_id: switch.klafs_sauna_sanarium_mode
      # Régler température et humidité
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
      # Allumer
      - service: climate.turn_on
        target:
          entity_id: climate.klafs_sauna
```

### Préchauffage intelligent basé sur la localisation

```yaml
automation:
  - alias: "Préchauffer sauna en rentrant"
    trigger:
      - platform: zone
        entity_id: person.vous
        zone: zone.travail
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
      # Calculer l'heure d'arrivée (30 min de trajet)
      - service: klafs.set_start_time
        target:
          entity_id: climate.klafs_sauna
        data:
          hour: "{{ now().hour }}"
          minute: "{{ (now().minute + 30) % 60 }}"
      # Régler en mode Sauna classique
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
          message: "Sauna en préchauffage, prêt à votre arrivée !"
```

### Extinction automatique après utilisation

```yaml
automation:
  - alias: "Éteindre sauna après 2h"
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
          message: "Sauna éteint automatiquement après 2h"
```

### Alerte si sauna allumé et personne à la maison

```yaml
automation:
  - alias: "Alerte sauna allumé sans personne"
    trigger:
      - platform: state
        entity_id: climate.klafs_sauna
        to: "heat"
        for:
          minutes: 10
    condition:
      - condition: state
        entity_id: zone.home
        state: "0"  # Personne à la maison
    action:
      - service: notify.mobile_app
        data:
          message: "⚠️ Le sauna est allumé mais personne n'est à la maison !"
          data:
            actions:
              - action: "TURN_OFF_SAUNA"
                title: "Éteindre"
              - action: "IGNORE"
                title: "Ignorer"

  - alias: "Action éteindre sauna"
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

### Programme hebdomadaire

```yaml
automation:
  # Lundi, Mercredi, Vendredi : Sauna classique
  - alias: "Sauna classique MWF"
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

  # Mardi, Jeudi : SANARIUM doux
  - alias: "SANARIUM doux TT"
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

### Intégration avec capteur de présence

```yaml
automation:
  - alias: "Démarrer sauna avec présence"
    trigger:
      - platform: state
        entity_id: binary_sensor.presence_salle_de_bain
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

## Cartes Lovelace

### Carte simple

```yaml
type: thermostat
entity: climate.klafs_sauna
```

### Carte détaillée

```yaml
type: vertical-stack
cards:
  - type: thermostat
    entity: climate.klafs_sauna
  - type: entities
    entities:
      - entity: sensor.klafs_sauna_temperature
        name: Température actuelle
      - entity: sensor.klafs_sauna_humidity
        name: Humidité
      - entity: sensor.klafs_sauna_status
        name: Statut
      - entity: switch.klafs_sauna_sanarium_mode
        name: Mode SANARIUM
```

### Carte avec contrôles avancés

```yaml
type: vertical-stack
cards:
  - type: thermostat
    entity: climate.klafs_sauna
    name: Contrôle Sauna
  
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
        name: Température
        icon: mdi:thermometer
      - entity: sensor.klafs_sauna_humidity
        name: Humidité
        icon: mdi:water-percent
      - entity: sensor.klafs_sauna_status
        name: Statut
```

### Carte avec slider d'humidité

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
          name: Humidité SANARIUM
          min: 1
          max: 10
          step: 1
```

## Scripts utiles

### Script mode SANARIUM

```yaml
script:
  sanarium_mode:
    alias: "Activer mode SANARIUM"
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

### Script sauna finlandais

```yaml
script:
  finnish_sauna:
    alias: "Sauna Finlandais"
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

### Script arrêt d'urgence

```yaml
script:
  sauna_emergency_stop:
    alias: "Arrêt d'urgence sauna"
    sequence:
      - service: climate.turn_off
        target:
          entity_id: climate.klafs_sauna
      - service: notify.all_devices
        data:
          message: "🚨 Sauna éteint en urgence"
```

## Intégration avec Google Assistant / Alexa

### Scènes pour commandes vocales

```yaml
scene:
  - name: "Sauna Classique"
    entities:
      climate.klafs_sauna:
        state: heat
        temperature: 85
      switch.klafs_sauna_sanarium_mode:
        state: off

  - name: "Sauna Doux"
    entities:
      climate.klafs_sauna:
        state: heat
        temperature: 60
      switch.klafs_sauna_sanarium_mode:
        state: on
```

Commandes vocales :
- "Ok Google, active la scène Sauna Classique"
- "Alexa, éteins le sauna"
- "Ok Google, règle le sauna à 80 degrés"
