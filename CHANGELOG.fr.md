# Changelog

**Lire dans d'autres langues :** [English](CHANGELOG.md) | **Français** | [Deutsch](CHANGELOG.de.md) | [Español](CHANGELOG.es.md)

Toutes les modifications notables de ce projet seront documentées dans ce fichier.

Le format est basé sur [Keep a Changelog](https://keepachangelog.com/fr/1.0.0/),
et ce projet adhère au [Semantic Versioning](https://semver.org/lang/fr/).

**Pour les fonctionnalités futures prévues, voir [FUTURELOG.fr.md](FUTURELOG.fr.md)**

---

## [1.0.19] - 2026-02-09

### Corrigé
- **Compatibilité double API** : Ajout du support pour les APIs `customIconsets` et `customIcons`
- Fonctions d'icônes synchrones pour une meilleure compatibilité entre versions HA
- Les icônes fonctionnent maintenant avec les systèmes d'icônes Home Assistant anciens et modernes

### Détails techniques
- Enregistré avec `window.customIconsets["klafs"]` (API historique)
- Enregistré avec `window.customIcons["klafs"]` (API alternative)
- Les deux retournent des objets `{path, viewBox}` de manière synchrone
- Compatibilité maximale avec les versions HA 2020-2024+

---

## [1.0.18] - 2026-02-09

### Corrigé
- **API HA moderne** : Utilisation de `async_register_static_paths` avec `StaticPathConfig` (méthode officielle HA 2024+)
- Correction de `register_static_path` obsolète causant AttributeError dans les versions récentes de Home Assistant
- Fonction maintenant correctement async avec appel `await` dans setup

### Détails techniques
- Import de `StaticPathConfig` depuis `homeassistant.components.http`
- Import de `add_extra_js_url` depuis `homeassistant.components.frontend`
- Utilisation de `await hass.http.async_register_static_paths([StaticPathConfig(...)])`
- Les icônes devraient maintenant se charger correctement à `/klafs/iconset.js`

---

## [1.0.17] - 2026-02-09

### Corrigé
- **Service HTTP** : Service de iconset.js via HTTP au lieu de data URL (compatible CSP)
- Utilisation de `register_static_path` pour servir le répertoire frontend
- Icônes maintenant chargées via URL HTTP : `/klafs/iconset.js`

### Modifié
- Suppression de l'approche data URL (bloquée par CSP dans les versions récentes de HA)
- Simplification en fonction d'enregistrement synchrone

---

## [1.0.16] - 2026-02-09

### Corrigé
- **Utilisation API correcte** : Utilisation de `from homeassistant.components import frontend` puis `frontend.add_extra_js_url()`
- **Format iconset approprié** : Utilisation de l'API `window.customIconsets` selon la documentation HA
- Les icônes utilisent maintenant l'API officielle Home Assistant custom iconsets (2020+)

### Modifié
- Réécriture de iconset.js pour utiliser `window.customIconsets` avec fonction async retournant `{path, viewBox}`
- Simplification des chemins SVG pour une meilleure compatibilité

---

## [1.0.15] - 2026-02-09

### Corrigé
- **Injection data URL** : Utilisation d'une data URL base64 au lieu de register_static_path
- Correction AttributeError : `'HomeAssistantHTTP' object has no attribute 'register_static_path'`
- Icônes maintenant injectées directement dans le frontend sans dépendance au serveur HTTP

---

## [1.0.14] - 2026-02-09

### Modifié
- **Iconset inline** : Icônes SVG maintenant intégrées directement dans iconset.js
- Suppression du répertoire `icons/` - plus nécessaire
- Simplifié à un seul fichier de déploiement (frontend/iconset.js uniquement)
- Plus fiable : aucune dépendance sur la copie de sous-répertoires par HACS

### Corrigé
- Les icônes se déploieront maintenant correctement via HACS (un seul fichier JS, pas de sous-répertoires)

---

## [1.0.13] - 2026-02-09

### Corrigé
- **Erreur d'import** : Suppression de l'import inexistant `StaticPathConfig`
- Utilisation de la méthode simple `register_static_path` qui fonctionne sur toutes les versions HA
- Correction ImportError : `cannot import name 'StaticPathConfig'`

---

## [1.0.12] - 2026-02-09

### Corrigé
- **Enregistrement chemin statique** : Utilisation d'objets `StaticPathConfig` au lieu de dictionnaires
- Correction AttributeError : `'dict' object has no attribute 'url_path'`

---

## [1.0.11] - 2026-02-09

### Corrigé
- **Compatibilité API** : Correction `register_static_path` → `async_register_static_paths` pour Home Assistant moderne
- **Emplacement icônes** : Déplacement des icônes de `frontend/icons/` vers `icons/` pour une structure plus simple
- Correction AttributeError au démarrage de Home Assistant

### Modifié
- Icônes maintenant dans le répertoire `custom_components/klafs/icons/`
- Utilisation de l'API async correcte pour l'enregistrement des chemins statiques

---

## [1.0.10] - 2026-02-09

### Corrigé
- **Whitelist fichiers HACS** : Ajout du tableau `files` dans `hacs.json` pour inclure explicitement tous les fichiers
- Cela corrige le filtrage HACS des fichiers non-Python (SVG, JS) dans les sous-répertoires
- HACS installera maintenant TOUS les fichiers incluant `frontend/icons/*.svg`

### Modifié
- Mise à jour de `hacs.json` avec whitelist `files: ["custom_components/klafs/**"]`

---

## [1.0.9] - 2026-02-09

### Corrigé
- **Déploiement HACS** : Correction de `hacs.json` avec `content_in_root: false` pour assurer le déploiement de tous les fichiers
- Cela corrige le problème où le répertoire `frontend/icons/` n'était pas copié par HACS

### Modifié
- Simplification de `hacs.json` (suppression des champs redondants qui appartiennent à manifest.json)

---

## [1.0.8] - 2026-02-09

### Corrigé
- **Emplacement des fichiers icônes** : Déplacement des SVG vers l'emplacement correct `frontend/icons/` pour un service approprié
- **Enregistrement du chemin statique** : Simplifié pour servir tout le répertoire frontend sous `/local/klafs/`
- **Chargement automatique** : Les icônes se chargent maintenant automatiquement sans ajout manuel de ressource Lovelace
- **Résolveur d'icônes** : Mise à jour de iconset.js pour utiliser une fonction résolveur pour une meilleure compatibilité

### Modifié
- Fichiers SVG déplacés de `custom_components/klafs/` vers `custom_components/klafs/frontend/icons/`
- Simplification de iconset.js avec approche par fonction résolveur
- Aucun ajout manuel de ressource Lovelace requis désormais

---

## [1.0.7] - 2026-02-09

### Corrigé
- **Méthode de chargement des icônes** : Remplacement de `add_extra_js_url()` obsolète par l'enregistrement manuel de ressource Lovelace
- **Enregistrement du chemin statique** : Correction de l'enregistrement incorrect du chemin fichier pour iconset.js
- **Enregistrement des icônes** : Amélioration de la compatibilité avec le système d'icônes Home Assistant 2023+

### Modifié
- Les icônes custom nécessitent maintenant l'ajout manuel d'une ressource Lovelace (voir CUSTOM_ICONS.fr.md)
- Mise à jour de iconset.js avec plusieurs méthodes d'enregistrement pour une meilleure compatibilité
- Amélioration des logs pour le débogage de l'enregistrement des icônes

### Documentation
- Ajout d'un guide de dépannage complet dans les 4 langues (EN/FR/DE/ES)
- Instructions étape par étape pour ajouter la ressource Lovelace
- Conseils de débogage via la console navigateur

---

## [1.0.6] - 2026-02-09

### Corrigé
- **Compatibilité HACS** : Déplacement des SVG à la racine de l'intégration pour un déploiement HACS correct
- HACS ne copiait pas le sous-dossier `frontend/icons/`, causant l'absence des icônes après installation

---

## [1.0.5] - 2026-02-09

### Corrigé
- **Timing d'enregistrement des icônes** : Les icônes sont maintenant enregistrées après le chargement des plateformes, assurant une initialisation correcte
- Cela corrige le problème où les icônes custom n'apparaissaient pas dans le frontend

---

## [1.0.4] - 2026-02-09

### Ajouté
- **Jeu d'Icônes Personnalisées** : L'intégration inclut maintenant des icônes custom avec le préfixe `klafs:`
  - `klafs:sauna` - État par défaut/neutre
  - `klafs:sauna-heating` - Sauna en chauffe (avec ondes de chaleur)
  - `klafs:sauna-ready` - Sauna prêt à l'emploi (thermomètre plein + coche)
  - `klafs:sauna-off` - Sauna éteint (éléments grisés)
  - Les icônes changent automatiquement selon l'état du sauna
  - Toutes les icônes utilisent `fill="currentColor"` pour la compatibilité thème
  - Fonctionne avec Home Assistant ≥ 2023.x
- **Documentation Multilingue** : Documentation des icônes custom en 4 langues (EN/FR/DE/ES)
- **Mapping Automatique des Icônes** : Les icônes changent automatiquement selon l'état de l'entité
  - Aucune configuration nécessaire
  - Fonctionne avec les entités sensor et climate

### Modifié
- Déplacement des icônes de `icons/` vers `frontend/icons/`
- Les icônes sont maintenant servies comme fichiers statiques via `/local/klafs/icons/`
- Ajout de `icon_mapping.py` pour la gestion centralisée des états d'icônes

### Technique
- Ajout de `frontend/iconset.js` pour l'enregistrement des icônes dans le frontend Home Assistant
- Mise à jour de `__init__.py` pour enregistrer les chemins statiques et charger l'iconset
- Mise à jour de `sensor.py` et `climate.py` pour utiliser des propriétés d'icônes dynamiques
- Les icônes s'adaptent automatiquement aux thèmes clair/foncé

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
