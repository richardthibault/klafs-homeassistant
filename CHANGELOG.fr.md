# Changelog

**Lire dans d'autres langues :** [English](CHANGELOG.md) | **Français** | [Deutsch](CHANGELOG.de.md) | [Español](CHANGELOG.es.md)

Toutes les modifications notables de ce projet seront documentées dans ce fichier.

Le format est basé sur [Keep a Changelog](https://keepachangelog.com/fr/1.0.0/),
et ce projet adhère au [Semantic Versioning](https://semver.org/lang/fr/).

**Pour les fonctionnalités futures prévues, voir [FUTURELOG.fr.md](FUTURELOG.fr.md)**

---

## [1.0.3] - 2026-02-09

### Corrigé
- **Problème d'affichage des icônes** : Remplacement des icônes personnalisées `klafs:sauna-*` par des icônes MDI standard
  - Les icônes SVG personnalisées sont conservées dans le dépôt pour usage futur
  - Utilisation maintenant de `mdi:sauna` (défaut/éteint), `mdi:fire` (en chauffe), `mdi:check-circle` (prêt)
  - Les icônes s'affichent maintenant correctement sans configuration supplémentaire

### Technique
- Les intégrations personnalisées Home Assistant ne peuvent pas facilement embarquer des jeux d'icônes personnalisés sans dépendances externes
- Les icônes MDI standard offrent une meilleure compatibilité et une fonctionnalité immédiate

---

## [1.0.2] - 2026-02-09

### Ajouté
- **Icônes SVG personnalisées** avec support de couleur dynamique
  - 4 icônes spécifiques par état : défaut, éteint, en chauffe, prêt
  - Les icônes s'adaptent au thème Home Assistant (clair/foncé)
  - Design radiateur avec barres visibles et pierres chauffantes
  - Thermomètre indique le niveau de température (0%, 25%, 50%, 100%)
  - Animation d'ondes de chaleur pour l'état en chauffe
  - Coche pour l'état prêt
- **Icônes PNG de branding** pour HACS et Home Assistant
  - Icône 256x256 pour la liste d'intégrations HACS
  - Icône haute résolution 512x512 pour écrans Retina
  - Fond dégradé chaud (tons orange/rouge)

### Modifié
- Mise à jour des icônes de capteurs pour utiliser les icônes personnalisées `klafs:sauna-*` au lieu des icônes MDI génériques
- Les icônes fournissent maintenant un meilleur retour visuel de l'état du sauna

### Technique
- Les icônes utilisent `currentColor` pour l'adaptation automatique au thème
- Format SVG garantit un affichage net à toute taille
- Aucune dépendance externe ni problème de droits d'auteur

---

## [1.0.1] - 2026-02-09

### Corrigé
- **Bug critique de reconnexion** : Le sauna n'était plus détecté après une perte de connexion WiFi
  - Le coordinateur garde maintenant les saunas dans les données même quand déconnectés
  - Gestion d'erreur améliorée par sauna individuel
  - Les entités restent disponibles et se reconnectent automatiquement
  - Plus besoin de désinstaller/réinstaller l'intégration après une perte de connexion

### Notes de version

Cette version corrige un bug critique qui empêchait la reconnexion automatique du sauna après une perte de connexion WiFi. Le coordinateur maintient maintenant les entités même quand le sauna est déconnecté, permettant une reconnexion transparente.

---

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
- MULTI_SAUNA_SUPPORT.md : Guide multi-saunas
- CHANGELOG.md : Historique des versions

### Notes de version

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

---

## Migration

### Depuis une version antérieure

#### De 1.0.0 vers 1.0.1
Aucune action requise. Mettez simplement à jour via HACS et redémarrez Home Assistant.

### Depuis d'autres intégrations

Si vous utilisez actuellement une autre méthode pour contrôler votre sauna Klafs (scripts, REST commands, etc.), vous pouvez migrer vers cette intégration :

1. Sauvegardez vos automatisations existantes
2. Installez cette intégration
3. Configurez avec vos identifiants Klafs
4. Mettez à jour vos automatisations pour utiliser les nouvelles entités
5. Supprimez l'ancienne configuration

---

## Support

Pour signaler un bug ou demander une fonctionnalité :
- GitHub Issues : https://github.com/richardthibault/klafs-homeassistant/issues
- Forum Home Assistant : https://community.home-assistant.io

## Contribution

Les contributions sont les bienvenues ! Consultez [CONTRIBUTING.md](CONTRIBUTING.md) pour comprendre l'architecture du projet.

---

**Légende :**
- `Ajouté` : Nouvelles fonctionnalités
- `Modifié` : Changements dans les fonctionnalités existantes
- `Déprécié` : Fonctionnalités bientôt supprimées
- `Supprimé` : Fonctionnalités supprimées
- `Corrigé` : Corrections de bugs
- `Sécurité` : Corrections de vulnérabilités
