# Changelog

Toutes les modifications notables de ce projet seront documentées dans ce fichier.

Le format est basé sur [Keep a Changelog](https://keepachangelog.com/fr/1.0.0/),
et ce projet adhère au [Semantic Versioning](https://semver.org/lang/fr/).

## [1.0.0] - 2026-01-28

### Ajouté
- Intégration initiale avec l'API Klafs
- Authentification via identifiants Klafs Sauna App
- **Support multi-saunas** : Gérez plusieurs saunas depuis un seul compte
- **Code PIN individuel par sauna** : Chaque sauna peut avoir son propre PIN
- **Config flow en 3 étapes** : Identifiants → Sélection saunas → Configuration PINs
- Entité Climate (thermostat) pour contrôler chaque sauna
- Capteurs de température, humidité et statut par sauna
- Interrupteur pour basculer entre modes Sauna et SANARIUM par sauna
- Service `power_on_with_pin` pour allumer avec un PIN spécifique
- Service `set_humidity_level` pour contrôler l'humidité (SANARIUM)
- Service `set_start_time` pour programmer l'heure de démarrage
- Support des modes : Sauna classique, SANARIUM, Infrarouge
- Polling automatique toutes les 60 secondes
- Détection automatique de tous les saunas du compte
- Configuration via interface utilisateur (Config Flow)
- Traductions en français et anglais
- Documentation complète (README, API, exemples, dépannage, multi-saunas)
- Support HACS pour installation facile
- Gestion automatique de la reconnexion en cas d'expiration de session

### Fonctionnalités
- Contrôle de la température (10-100°C selon le mode)
- Allumage/extinction à distance
- Surveillance en temps réel de la température et humidité
- Statut de connexion du sauna
- Indication "Ready" quand le sauna est prêt
- Attributs étendus (mode actif, niveau d'humidité, etc.)
- Limites de température adaptées au mode sélectionné

### Sécurité
- Stockage sécurisé des identifiants
- Support du code PIN obligatoire pour l'allumage
- Gestion des tentatives de connexion échouées
- Communication HTTPS uniquement

### Documentation
- README.md : Documentation principale
- INSTALLATION.md : Guide d'installation détaillé
- API_DOCUMENTATION.md : Documentation technique de l'API
- EXAMPLES.md : Exemples d'automatisations et cartes Lovelace
- TROUBLESHOOTING.md : Guide de dépannage
- PROJECT_STRUCTURE.md : Architecture du projet
- CHANGELOG.md : Historique des versions

## [Non publié]

### Prévu pour les versions futures

#### [1.1.0] - À venir
- Support du mode Infrarouge complet
- Capteur de temps de bain restant
- Service pour définir la durée de bain
- Notifications push quand le sauna est prêt
- Graphiques de consommation énergétique (si disponible via API)

#### [1.2.0] - À venir
- Support de plusieurs comptes Klafs
- Entité Number pour contrôler l'humidité via slider
- Entité Select pour choisir le mode (Sauna/SANARIUM/IR)
- Presets de température (Finlandais, Doux, Intense, etc.)
- Historique des sessions de sauna

#### [2.0.0] - À venir
- Support de l'API locale si Klafs la rend disponible
- Réduction de la latence avec WebSocket si disponible
- Support des saunas multi-zones
- Intégration avec les systèmes de ventilation
- Support des éclairages et aromathérapie si disponibles

### Idées en discussion
- Intégration avec calendrier pour planification automatique
- Détection de présence pour allumage automatique
- Statistiques d'utilisation et rapports
- Support des profils utilisateurs multiples
- Mode économie d'énergie intelligent
- Intégration avec capteurs de qualité d'air

## Notes de version

### Version 1.0.0

Cette première version stable offre toutes les fonctionnalités de base pour contrôler votre sauna Klafs via Home Assistant. L'intégration a été développée en se basant sur l'ingénierie inverse de l'API Klafs utilisée par l'application mobile officielle.

**Points forts :**
- Configuration simple via l'interface utilisateur
- Support complet des modes Sauna et SANARIUM
- Services personnalisés pour un contrôle avancé
- Documentation exhaustive
- Compatible HACS

**Limitations connues :**
- Polling toutes les 60 secondes (pas de push en temps réel)
- Dépend du cloud Klafs (pas de contrôle local)
- Mode Infrarouge partiellement testé
- Pas de support des fonctionnalités avancées (éclairage, aromathérapie)

**Compatibilité :**
- Home Assistant 2023.1.0 ou supérieur
- Python 3.10 ou supérieur
- Tous les saunas Klafs avec module Wi-Fi et option "KLAFS Sauna App"

**Remerciements :**
- Communauté OpenHAB pour la recherche initiale sur l'API
- Projet IPSymconKlafsSaunaControl pour les exemples d'implémentation
- Contributeurs et testeurs de la communauté Home Assistant

## Migration

### Depuis une version antérieure

Aucune migration nécessaire - c'est la première version stable.

### Depuis d'autres intégrations

Si vous utilisez actuellement une autre méthode pour contrôler votre sauna Klafs (scripts, REST commands, etc.), vous pouvez migrer vers cette intégration :

1. Sauvegardez vos automatisations existantes
2. Installez cette intégration
3. Configurez avec vos identifiants Klafs
4. Mettez à jour vos automatisations pour utiliser les nouvelles entités
5. Supprimez l'ancienne configuration

## Support

Pour signaler un bug ou demander une fonctionnalité :
- GitHub Issues : https://github.com/richardthibault/klafs-homeassistant/issues
- Forum Home Assistant : https://community.home-assistant.io

## Contribution

Les contributions sont les bienvenues ! Consultez PROJECT_STRUCTURE.md pour comprendre l'architecture du projet.

---

**Légende :**
- `Ajouté` : Nouvelles fonctionnalités
- `Modifié` : Changements dans les fonctionnalités existantes
- `Déprécié` : Fonctionnalités bientôt supprimées
- `Supprimé` : Fonctionnalités supprimées
- `Corrigé` : Corrections de bugs
- `Sécurité` : Corrections de vulnérabilités
