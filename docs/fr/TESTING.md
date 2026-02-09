# Guide de test - Intégration Klafs

## Options de test

### Option 1 : Test avec sauna réel (Production)

Si tu as un sauna Klafs avec module Wi-Fi :

1. **Déployer l'intégration**
   ```bash
   # Copier dans Home Assistant
   xcopy /E /I custom_components\klafs "C:\path\to\homeassistant\config\custom_components\klafs"
   ```

2. **Redémarrer Home Assistant**

3. **Configurer l'intégration**
   - Configuration > Intégrations > + Ajouter
   - Rechercher "Klafs Sauna"
   - Entrer tes vrais identifiants Klafs
   - Sélectionner tes saunas
   - Entrer les PINs

4. **Tester les fonctionnalités**
   - Vérifier que les entités apparaissent
   - Tester l'allumage/extinction
   - Tester le changement de température
   - Tester le mode SANARIUM

### Option 2 : Test avec API mock (Développement)

Si tu n'as pas de sauna ou veux tester sans risque :

#### Étape 1 : Activer le mode mock

Modifier `custom_components/klafs/__init__.py` :

```python
# En haut du fichier, ajouter :
import os
MOCK_MODE = os.getenv("KLAFS_MOCK_MODE", "false").lower() == "true"

# Dans async_setup_entry, remplacer :
if MOCK_MODE:
    from tests.test_mock_api import MockKlafsApiClient
    client = MockKlafsApiClient(
        entry.data["username"],
        entry.data["password"],
        hass.helpers.aiohttp_client.async_get_clientsession(),
    )
else:
    client = KlafsApiClient(
        entry.data["username"],
        entry.data["password"],
        hass.helpers.aiohttp_client.async_get_clientsession(),
    )
```

#### Étape 2 : Lancer HA en mode mock

```bash
# Windows
set KLAFS_MOCK_MODE=true
hass -c config

# Linux/Mac
export KLAFS_MOCK_MODE=true
hass -c config
```

#### Étape 3 : Configurer avec des identifiants fictifs

- Username : `test@example.com`
- Password : `test123`
- Les saunas "Sauna Test 1" et "Sauna Test 2" apparaîtront
- Utiliser n'importe quel PIN (ex: 1234, 5678)

## Installation d'un environnement de développement

### Méthode 1 : Home Assistant Core (Python)

```bash
# 1. Créer un environnement virtuel
python -m venv ha-dev
cd ha-dev

# Windows
Scripts\activate

# Linux/Mac
source bin/activate

# 2. Installer Home Assistant
pip install homeassistant

# 3. Créer la structure
mkdir config
mkdir config\custom_components

# 4. Copier l'intégration
# Windows
xcopy /E /I ..\Klafs-HA\custom_components\klafs config\custom_components\klafs
xcopy /E /I ..\Klafs-HA\tests config\tests

# Linux/Mac
cp -r ../Klafs-HA/custom_components/klafs config/custom_components/
cp -r ../Klafs-HA/tests config/

# 5. Activer le mode mock (optionnel)
# Windows
set KLAFS_MOCK_MODE=true

# Linux/Mac
export KLAFS_MOCK_MODE=true

# 6. Lancer Home Assistant
hass -c config --debug

# 7. Ouvrir le navigateur
# http://localhost:8123
```

### Méthode 2 : Home Assistant Container (Docker)

```bash
# 1. Créer docker-compose.yml
```

```yaml
version: '3'
services:
  homeassistant:
    container_name: ha-klafs-dev
    image: homeassistant/home-assistant:latest
    volumes:
      - ./config:/config
      - ./custom_components/klafs:/config/custom_components/klafs
      - ./tests:/config/tests
    environment:
      - KLAFS_MOCK_MODE=true  # Activer le mode mock
    ports:
      - "8123:8123"
    restart: unless-stopped
```

```bash
# 2. Lancer
docker-compose up -d

# 3. Voir les logs
docker-compose logs -f

# 4. Ouvrir le navigateur
# http://localhost:8123
```

### Méthode 3 : Home Assistant OS (VM)

1. **Installer Home Assistant OS** dans VirtualBox/VMware
2. **Accéder via SSH** (activer le add-on SSH)
3. **Copier l'intégration**
   ```bash
   # Via Samba ou SSH
   scp -r custom_components/klafs root@homeassistant.local:/config/custom_components/
   ```
4. **Redémarrer** via l'UI

## Checklist de test

### Tests de base

- [ ] **Installation**
  - [ ] L'intégration apparaît dans la liste
  - [ ] Pas d'erreur dans les logs au démarrage

- [ ] **Configuration - Étape 1 (Identifiants)**
  - [ ] Le formulaire s'affiche correctement
  - [ ] Validation des identifiants fonctionne
  - [ ] Message d'erreur si identifiants invalides
  - [ ] Passage à l'étape 2 si succès

- [ ] **Configuration - Étape 2 (Sélection saunas)**
  - [ ] La liste des saunas s'affiche
  - [ ] Sélection multiple fonctionne
  - [ ] Message d'erreur si aucun sauna sélectionné
  - [ ] Passage à l'étape 3 si au moins 1 sélectionné

- [ ] **Configuration - Étape 3 (PINs)**
  - [ ] Un champ par sauna sélectionné
  - [ ] Les noms des saunas sont corrects
  - [ ] Les PINs sont optionnels
  - [ ] Création de l'entry si succès

### Tests des entités

- [ ] **Climate (Thermostat)**
  - [ ] Entité créée pour chaque sauna
  - [ ] Température actuelle affichée
  - [ ] Température cible modifiable
  - [ ] Mode HVAC (OFF/HEAT) fonctionne
  - [ ] Limites de température respectées

- [ ] **Sensors**
  - [ ] Capteur de température créé
  - [ ] Capteur d'humidité créé
  - [ ] Capteur de statut créé
  - [ ] Valeurs mises à jour

- [ ] **Switch**
  - [ ] Interrupteur SANARIUM créé
  - [ ] Basculement Sauna/SANARIUM fonctionne

### Tests des services

- [ ] **power_on_with_pin**
  - [ ] Service disponible
  - [ ] Fonctionne avec PIN
  - [ ] Erreur si PIN invalide (avec vrai sauna)

- [ ] **set_humidity_level**
  - [ ] Service disponible
  - [ ] Niveaux 1-10 acceptés
  - [ ] Erreur si hors limites

- [ ] **set_start_time**
  - [ ] Service disponible
  - [ ] Heure/minute acceptées
  - [ ] Erreur si valeurs invalides

### Tests multi-saunas

- [ ] **2 saunas configurés**
  - [ ] 2 devices créés
  - [ ] Noms différents
  - [ ] Entités séparées
  - [ ] PINs différents utilisés

- [ ] **Contrôle indépendant**
  - [ ] Allumer sauna 1 n'affecte pas sauna 2
  - [ ] Températures indépendantes
  - [ ] Modes indépendants

### Tests d'erreur

- [ ] **Connexion perdue**
  - [ ] Entités deviennent "unavailable"
  - [ ] Reconnexion automatique fonctionne

- [ ] **Session expirée**
  - [ ] Re-login automatique
  - [ ] Pas d'interruption de service

- [ ] **Sauna déconnecté**
  - [ ] Statut "Disconnected" affiché
  - [ ] Pas de crash de l'intégration

## Logs de débogage

### Activer les logs détaillés

Dans `configuration.yaml` :

```yaml
logger:
  default: info
  logs:
    custom_components.klafs: debug
    custom_components.klafs.api: debug
    custom_components.klafs.config_flow: debug
```

### Consulter les logs

```bash
# Via l'UI
Configuration > Logs

# Via CLI
tail -f config/home-assistant.log | grep klafs

# Via Docker
docker logs -f ha-klafs-dev | grep klafs
```

### Logs importants à vérifier

```
# Démarrage
INFO (MainThread) [custom_components.klafs] Setting up Klafs integration

# Login
INFO (MainThread) [custom_components.klafs.api] Successfully logged in to Klafs API

# Découverte saunas
DEBUG (MainThread) [custom_components.klafs] Found 2 saunas

# Mise à jour
DEBUG (MainThread) [custom_components.klafs] Updating sauna status for 364cc9db...

# Erreurs
ERROR (MainThread) [custom_components.klafs.api] Failed to login: Invalid credentials
```

## Tests automatisés (Futur)

Pour l'instant, les tests sont manuels. Voici ce qui pourrait être ajouté :

### Tests unitaires

```python
# tests/test_api.py
import pytest
from custom_components.klafs.api import KlafsApiClient

@pytest.mark.asyncio
async def test_login_success():
    client = KlafsApiClient("user", "pass", mock_session)
    result = await client.login()
    assert result is True

@pytest.mark.asyncio
async def test_get_saunas():
    client = KlafsApiClient("user", "pass", mock_session)
    await client.login()
    saunas = await client.get_saunas()
    assert len(saunas) > 0
```

### Tests d'intégration

```python
# tests/test_integration.py
import pytest
from homeassistant.setup import async_setup_component

@pytest.mark.asyncio
async def test_setup_integration(hass):
    config = {
        "klafs": {
            "username": "test",
            "password": "test"
        }
    }
    result = await async_setup_component(hass, "klafs", config)
    assert result is True
```

## Dépannage

### L'intégration n'apparaît pas

1. Vérifier que le dossier est bien placé :
   ```
   config/custom_components/klafs/
   ```

2. Vérifier les permissions :
   ```bash
   # Linux
   chmod -R 755 config/custom_components/klafs
   ```

3. Vérifier les logs au démarrage

4. Redémarrer en mode sans échec

### Erreur au démarrage

1. Vérifier la syntaxe Python :
   ```bash
   python -m py_compile custom_components/klafs/*.py
   ```

2. Vérifier les imports :
   ```bash
   python -c "from custom_components.klafs import *"
   ```

3. Consulter les logs détaillés

### Config flow ne s'affiche pas

1. Vérifier `manifest.json` :
   ```json
   {
     "config_flow": true
   }
   ```

2. Vérifier `strings.json` existe

3. Redémarrer Home Assistant

## Ressources

- [Home Assistant Developer Docs](https://developers.home-assistant.io/)
- [Testing Integrations](https://developers.home-assistant.io/docs/development_testing)
- [Config Flow Testing](https://developers.home-assistant.io/docs/config_entries_config_flow_handler#testing)

## Prochaines étapes

Une fois les tests manuels validés :

1. Créer des tests automatisés (pytest)
2. Configurer CI/CD (GitHub Actions)
3. Tester avec plusieurs versions de HA
4. Tester sur différentes plateformes (Linux, Windows, Docker)
5. Beta testing avec la communauté
