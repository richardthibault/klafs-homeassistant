# Feuille de Route Future

**Lire dans d'autres langues :** [English](FUTURELOG.md) | **Français** | [Deutsch](FUTURELOG.de.md) | [Español](FUTURELOG.es.md)

Ce document présente les fonctionnalités et améliorations prévues pour les futures versions de l'intégration Klafs Sauna pour Home Assistant.

---

## [Non publié]

### Prévu pour les versions futures

#### [1.2.0] - À venir
- Support de plusieurs comptes Klafs
- Entité Number pour contrôler l'humidité via slider
- Entité Select pour choisir le mode (Sauna/SANARIUM/IR)
- Presets de température (Finlandais, Doux, Intense, etc.)
- Historique des sessions de sauna

#### [1.1.0] - À venir
- Support du mode Infrarouge complet
- Capteur de temps de bain restant
- Service pour définir la durée de bain
- Notifications push quand le sauna est prêt
- Graphiques de consommation énergétique (si disponible via API)

#### [2.0.0] - Long terme
- Support de l'API locale si Klafs la rend disponible
- Réduction de la latence avec WebSocket si disponible
- Support des saunas multi-zones
- Intégration avec les systèmes de ventilation
- Support des éclairages et aromathérapie si disponibles

---

## Idées en discussion

Ces fonctionnalités sont envisagées mais pas encore planifiées :

### Automatisation intelligente
- Intégration avec calendrier pour planification automatique
- Détection de présence pour allumage automatique
- Mode économie d'énergie intelligent basé sur les habitudes d'utilisation
- Intégration avec prévisions météo (prise en compte température extérieure)

### Analytiques & Surveillance
- Statistiques d'utilisation et rapports
- Suivi de la durée des sessions
- Analyse de consommation énergétique (si l'API fournit les données)
- Graphiques d'historique température/humidité

### Expérience utilisateur
- Support des profils utilisateurs multiples
- Améliorations assistants vocaux (Google Assistant, Alexa, Siri)
- Notifications mobiles avec actions enrichies
- Widgets d'actions rapides

### Fonctionnalités avancées
- Intégration avec capteurs de qualité d'air
- Intégration avec scènes domotiques
- Géofencing pour préchauffage automatique
- Apprentissage automatique pour temps de préchauffage optimal

### Intégration matérielle
- Support des accessoires Klafs additionnels
- Intégration avec systèmes d'éclairage intelligents
- Contrôle du diffuseur d'aromathérapie
- Intégration système audio/musique

---

## Comment contribuer des idées

Vous avez une demande de fonctionnalité ? Voici comment la suggérer :

1. **Vérifier les issues existantes** : https://github.com/richardthibault/klafs-homeassistant/issues
2. **Créer une demande de fonctionnalité** : Utiliser le template de feature request
3. **Discuter sur le forum** : https://community.home-assistant.io
4. **Voter pour les demandes existantes** : Ajouter 👍 aux issues que vous voulez

---

## Critères de priorité

Les fonctionnalités sont priorisées selon :

1. **Demande utilisateur** : Nombre de demandes et votes
2. **Disponibilité API** : Si l'API Klafs le supporte
3. **Complexité** : Effort de développement requis
4. **Compatibilité** : Bonnes pratiques Home Assistant
5. **Maintenance** : Considérations de support à long terme

---

## Planification des versions

### Court terme (1-3 mois)
- Corrections de bugs et améliorations de stabilité
- Ajouts de fonctionnalités mineures basés sur les retours utilisateurs
- Améliorations de la documentation

### Moyen terme (3-6 mois)
- Fonctionnalités de la version 1.1.0
- Capacités d'automatisation améliorées
- Meilleure gestion d'erreurs et diagnostics

### Long terme (6+ mois)
- Fonctionnalités des versions 1.2.0 et 2.0.0
- Améliorations architecturales majeures
- Intégrations avancées

---

## Contribuer

Vous voulez aider à implémenter ces fonctionnalités ?

- Voir [CONTRIBUTING.md](CONTRIBUTING.md) pour les directives de développement
- Consulter [GitHub Issues](https://github.com/richardthibault/klafs-homeassistant/issues) pour les tâches ouvertes
- Rejoindre les discussions sur le forum Home Assistant

---

**Note** : Cette feuille de route est sujette à changement selon les retours utilisateurs, les changements d'API et les priorités de développement.

Dernière mise à jour : 2026-02-09
