# Klafs Sauna pour Home Assistant

Contrôlez votre sauna Klafs directement depuis Home Assistant !

## Fonctionnalités

- 🌡️ **Contrôle de température** - Réglez la température de votre sauna comme un thermostat
- 🔥 **Allumage à distance** - Démarrez votre sauna avant d'arriver à la maison
- 💧 **Mode SANARIUM** - Basculez entre mode Sauna classique et SANARIUM avec contrôle d'humidité
- 📊 **Surveillance en temps réel** - Température, humidité et statut actuels
- 🏠 **Multi-saunas** - Gérez plusieurs saunas depuis un seul compte
- 🔐 **Code PIN individuel** - Chaque sauna peut avoir son propre code PIN de sécurité
- ⏰ **Programmation horaire** - Planifiez l'heure de démarrage de votre sauna
- 🤖 **Automatisations** - Créez des scénarios personnalisés

## Installation

### Via HACS (Recommandé)

1. Ouvrez HACS dans Home Assistant
2. Cliquez sur "Intégrations"
3. Cliquez sur les trois points en haut à droite
4. Sélectionnez "Dépôts personnalisés"
5. Ajoutez l'URL : `https://github.com/richardthibault/klafs-homeassistant`
6. Catégorie : "Integration"
7. Recherchez "Klafs Sauna" et installez
8. Redémarrez Home Assistant

### Configuration

1. Allez dans **Configuration** > **Intégrations**
2. Cliquez sur **+ Ajouter une intégration**
3. Recherchez **"Klafs Sauna"**
4. Suivez les 3 étapes :
   - Entrez vos identifiants Klafs Sauna App
   - Sélectionnez vos saunas
   - Configurez les codes PIN (optionnel)

## Prérequis

- Home Assistant 2023.1.0 ou supérieur
- Compte Klafs Sauna App
- Sauna Klafs avec module Wi-Fi et option "KLAFS Sauna App"

## Support

- [Documentation complète](https://github.com/richardthibault/klafs-homeassistant)
- [Signaler un bug](https://github.com/richardthibault/klafs-homeassistant/issues)
- [Forum Home Assistant](https://community.home-assistant.io)

## Exemple d'utilisation

```yaml
# Automatisation : Préchauffer le sauna en rentrant du travail
automation:
  - alias: "Sauna prêt à l'arrivée"
    trigger:
      - platform: zone
        entity_id: person.vous
        zone: zone.travail
        event: leave
    action:
      - service: climate.set_temperature
        target:
          entity_id: climate.klafs_sauna
        data:
          temperature: 85
          hvac_mode: heat
```

## Licence

MIT License - Voir [LICENSE](LICENSE)
