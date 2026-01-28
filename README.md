# Intégration Klafs Sauna pour Home Assistant

[![hacs_badge](https://img.shields.io/badge/HACS-Custom-orange.svg)](https://github.com/custom-components/hacs)
[![GitHub release](https://img.shields.io/github/release/richardthibault/klafs-homeassistant.svg)](https://github.com/richardthibault/klafs-homeassistant/releases)
[![License](https://img.shields.io/github/license/richardthibault/klafs-homeassistant.svg)](LICENSE)

Cette intégration personnalisée permet de contrôler votre sauna Klafs via Home Assistant en utilisant l'API cloud de Klafs.

![Klafs Sauna](https://www.klafs.com/typo3conf/ext/klafs_sitepackage/Resources/Public/Images/logo.svg)

## Fonctionnalités

- **Contrôle climatique** : Contrôlez la température de votre sauna comme un thermostat
- **Capteurs** : Surveillez la température, l'humidité et le statut en temps réel
- **Modes** : Basculez entre les modes Sauna et SANARIUM®
- **Allumage/Extinction** : Contrôlez l'alimentation de votre sauna à distance
- **Multi-saunas** : Gérez plusieurs saunas depuis un seul compte
- **PIN individuels** : Chaque sauna peut avoir son propre code PIN

## Prérequis

- Un compte Klafs Sauna App
- Un sauna Klafs équipé du module Wi-Fi et de l'option "KLAFS Sauna App"
- Home Assistant 2023.1 ou supérieur

## Installation

### Installation manuelle

1. Copiez le dossier `custom_components/klafs` dans votre dossier `config/custom_components/`
2. Redémarrez Home Assistant
3. Allez dans Configuration > Intégrations
4. Cliquez sur "+ Ajouter une intégration"
5. Recherchez "Klafs Sauna"
6. Entrez vos identifiants Klafs Sauna App

### Installation via HACS (recommandé)

1. Ouvrez HACS dans Home Assistant
2. Allez dans "Intégrations"
3. Cliquez sur les trois points en haut à droite
4. Sélectionnez "Dépôts personnalisés"
5. Ajoutez l'URL de ce dépôt
6. Recherchez "Klafs Sauna" et installez-le
7. Redémarrez Home Assistant
8. Configurez l'intégration via l'interface utilisateur

## Configuration

L'intégration se configure entièrement via l'interface utilisateur de Home Assistant en 3 étapes :

### Étape 1 : Identifiants
- **Nom d'utilisateur** : Votre identifiant Klafs Sauna App
- **Mot de passe** : Votre mot de passe Klafs Sauna App

### Étape 2 : Sélection des saunas
- Sélectionnez les saunas que vous souhaitez contrôler via Home Assistant
- Vous pouvez en sélectionner un ou plusieurs
- Chaque sauna apparaîtra comme un appareil séparé

### Étape 3 : Codes PIN
- **Code PIN** (optionnel) : Le code PIN à 4 chiffres configuré sur chaque sauna
- Un PIN différent peut être configuré pour chaque sauna
- Requis pour allumer le sauna à distance

⚠️ **Important** : 
- Klafs bloque le compte après 3 tentatives de connexion échouées. Assurez-vous d'entrer les bons identifiants.
- Chaque code PIN doit être configuré sur le sauna correspondant via son panneau de contrôle avant de pouvoir l'utiliser.
- Sans PIN, vous pourrez voir l'état du sauna mais pas l'allumer à distance.
- Si vous avez plusieurs saunas, chacun peut avoir son propre code PIN.

## Entités créées

Pour chaque sauna détecté, l'intégration crée :

### Climate (Thermostat)
- **Entité** : `climate.klafs_sauna_XXXXXXXX`
- **Fonctions** : Contrôle de la température, allumage/extinction
- **Attributs** :
  - Mode actuel (Sauna/SANARIUM®/Infrarouge)
  - Connexion
  - Prêt à l'emploi
  - Niveau d'humidité (SANARIUM® uniquement)

### Capteurs
- **Température** : `sensor.klafs_sauna_XXXXXXXX_temperature`
- **Humidité** : `sensor.klafs_sauna_XXXXXXXX_humidity`
- **Statut** : `sensor.klafs_sauna_XXXXXXXX_status` (Off/Heating/Ready/Disconnected)

### Interrupteur
- **Mode SANARIUM®** : `switch.klafs_sauna_XXXXXXXX_sanarium_mode`

## Utilisation

### Contrôle basique

```yaml
# Allumer le sauna à 80°C (utilise le PIN configuré)
service: climate.set_temperature
target:
  entity_id: climate.klafs_sauna_XXXXXXXX
data:
  temperature: 80
  hvac_mode: heat

# Allumer avec un PIN spécifique
service: klafs.power_on_with_pin
target:
  entity_id: climate.klafs_sauna_XXXXXXXX
data:
  pin: "1234"

# Éteindre le sauna
service: climate.turn_off
target:
  entity_id: climate.klafs_sauna_XXXXXXXX

# Définir le niveau d'humidité (SANARIUM uniquement)
service: klafs.set_humidity_level
target:
  entity_id: climate.klafs_sauna_XXXXXXXX
data:
  humidity_level: 7

# Programmer l'heure de démarrage
service: klafs.set_start_time
target:
  entity_id: climate.klafs_sauna_XXXXXXXX
data:
  hour: 18
  minute: 30
```

### Automatisations

```yaml
# Démarrer le sauna 1 heure avant d'arriver à la maison
automation:
  - alias: "Préchauffer le sauna"
    trigger:
      - platform: time
        at: "18:00:00"
    action:
      - service: klafs.set_start_time
        target:
          entity_id: climate.klafs_sauna
        data:
          hour: 19
          minute: 0
      - service: climate.set_temperature
        target:
          entity_id: climate.klafs_sauna
        data:
          temperature: 85
          hvac_mode: heat

# Notification quand le sauna est prêt
automation:
  - alias: "Sauna prêt"
    trigger:
      - platform: state
        entity_id: sensor.klafs_sauna_status
        to: "Ready"
    action:
      - service: notify.mobile_app
        data:
          message: "Votre sauna est prêt !"

# Activer le mode SANARIUM avec humidité élevée le week-end
automation:
  - alias: "Mode SANARIUM week-end"
    trigger:
      - platform: time
        at: "10:00:00"
    condition:
      - condition: time
        weekday:
          - sat
          - sun
    action:
      - service: switch.turn_on
        target:
          entity_id: switch.klafs_sauna_sanarium_mode
      - service: klafs.set_humidity_level
        target:
          entity_id: climate.klafs_sauna
        data:
          humidity_level: 8
      - service: climate.set_temperature
        target:
          entity_id: climate.klafs_sauna
        data:
          temperature: 65
          hvac_mode: heat
```

### Carte Lovelace

```yaml
type: thermostat
entity: climate.klafs_sauna
```

Ou pour une carte plus détaillée :

```yaml
type: entities
entities:
  - entity: climate.klafs_sauna
  - entity: sensor.klafs_sauna_temperature
  - entity: sensor.klafs_sauna_humidity
  - entity: sensor.klafs_sauna_status
  - entity: switch.klafs_sauna_sanarium_mode
```

## API Klafs

Cette intégration utilise l'API web de Klafs (application ASP.NET MVC) :

- **URL de base** : `https://sauna-app.klafs.com`
- **Authentification** : Cookie-based après login
- **Polling** : Mise à jour toutes les 60 secondes par défaut

### Endpoints utilisés

- `/Account/Login` : Authentification
- `/SaunaApp/GetData` : Récupération du statut d'un sauna
- `/SaunaApp/StartCabin` : Démarrage du sauna
- `/SaunaApp/StopCabin` : Arrêt du sauna
- `/SaunaApp/ChangeTemperature` : Changement de température
- `/SaunaApp/ChangeHumLevel` : Changement d'humidité
- `/SaunaApp/SetMode` : Changement de mode

## Limites de température

- **Mode Sauna** : 10°C - 100°C
- **Mode SANARIUM®** : 40°C - 75°C
- **Mode Infrarouge** : 30°C - 100°C

## Dépannage

### L'intégration ne se connecte pas

1. Vérifiez vos identifiants dans l'application Klafs Sauna App
2. Assurez-vous que votre compte n'est pas bloqué (3 tentatives max)
3. Vérifiez les logs Home Assistant : `Configuration > Logs`

### Le sauna n'apparaît pas

1. Assurez-vous que votre sauna est bien configuré dans l'application Klafs
2. Vérifiez que le module Wi-Fi est connecté
3. Redémarrez l'intégration

### Les commandes ne fonctionnent pas

1. Vérifiez que le sauna est connecté (`isConnected: true`)
2. Assurez-vous d'avoir configuré un code PIN sur votre sauna
3. Vérifiez que la porte du sauna a été contrôlée

## Contribution

Les contributions sont les bienvenues ! N'hésitez pas à :

- Signaler des bugs
- Proposer de nouvelles fonctionnalités
- Soumettre des pull requests

## Licence

MIT License

## Crédits

- Basé sur la recherche de l'API par la communauté OpenHAB
- Inspiré du projet [IPSymconKlafsSaunaControl](https://github.com/Pommespanzer/IPSymconKlafsSaunaControl)

## Avertissement

Cette intégration n'est pas officielle et n'est pas affiliée à Klafs GmbH. Utilisez-la à vos propres risques.

