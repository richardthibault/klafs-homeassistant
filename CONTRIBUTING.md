# Guide de contribution

Merci de votre intérêt pour contribuer à l'intégration Klafs pour Home Assistant ! 🎉

## Code de conduite

En participant à ce projet, vous acceptez de respecter notre code de conduite :
- Soyez respectueux et inclusif
- Acceptez les critiques constructives
- Concentrez-vous sur ce qui est le mieux pour la communauté
- Faites preuve d'empathie envers les autres membres

## Comment contribuer

### Signaler un bug

Si vous trouvez un bug, créez une issue GitHub avec :

1. **Titre clair** : Décrivez le problème en une phrase
2. **Description détaillée** :
   - Version de Home Assistant
   - Version de l'intégration
   - Étapes pour reproduire le bug
   - Comportement attendu vs observé
3. **Logs** : Incluez les logs pertinents (anonymisez les données sensibles)
4. **Configuration** : Partagez votre configuration (sans credentials)

**Template d'issue pour bug :**

```markdown
## Description
[Description claire du bug]

## Environnement
- Home Assistant : 2024.1.0
- Intégration Klafs : 1.0.0
- Type de sauna : SANARIUM

## Étapes pour reproduire
1. Aller dans...
2. Cliquer sur...
3. Observer...

## Comportement attendu
[Ce qui devrait se passer]

## Comportement observé
[Ce qui se passe réellement]

## Logs
```
[Vos logs ici]
```

## Configuration
```yaml
# Votre configuration (anonymisée)
```
```

### Proposer une fonctionnalité

Pour proposer une nouvelle fonctionnalité :

1. **Vérifiez** qu'elle n'existe pas déjà ou n'est pas en cours de développement
2. **Créez une issue** avec le label "enhancement"
3. **Décrivez** :
   - Le problème que cela résout
   - Comment cela devrait fonctionner
   - Des exemples d'utilisation
   - L'impact sur les fonctionnalités existantes

**Template d'issue pour fonctionnalité :**

```markdown
## Fonctionnalité proposée
[Description de la fonctionnalité]

## Problème résolu
[Quel problème cela résout-il ?]

## Solution proposée
[Comment cela devrait fonctionner]

## Exemples d'utilisation
```yaml
# Exemple de code ou configuration
```

## Alternatives considérées
[Autres solutions envisagées]
```

### Contribuer du code

#### Prérequis

- Python 3.10 ou supérieur
- Home Assistant en environnement de développement
- Git
- Connaissance de Python et asyncio
- Familiarité avec Home Assistant

#### Configuration de l'environnement de développement

1. **Fork le repository**
   ```bash
   # Sur GitHub, cliquez sur "Fork"
   ```

2. **Clone votre fork**
   ```bash
   git clone https://github.com/votre-username/klafs-homeassistant.git
   cd klafs-homeassistant
   ```

3. **Créez une branche**
   ```bash
   git checkout -b feature/ma-nouvelle-fonctionnalite
   ```

4. **Installez dans Home Assistant**
   ```bash
   # Copiez dans votre config Home Assistant
   cp -r custom_components/klafs /path/to/homeassistant/config/custom_components/
   ```

5. **Activez les logs de debug**
   ```yaml
   # configuration.yaml
   logger:
     default: info
     logs:
       custom_components.klafs: debug
   ```

#### Standards de code

##### Style Python

Suivez [PEP 8](https://pep8.org/) et les [conventions Home Assistant](https://developers.home-assistant.io/docs/development_guidelines) :

```python
# Bon
async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up Klafs from a config entry."""
    coordinator = KlafsDataUpdateCoordinator(hass, client, entry)
    await coordinator.async_config_entry_first_refresh()
    return True

# Mauvais
def setup(hass,entry):
    coordinator=KlafsDataUpdateCoordinator(hass,client,entry)
    coordinator.async_config_entry_first_refresh()
    return True
```

##### Type hints

Utilisez toujours les type hints :

```python
# Bon
async def set_temperature(self, sauna_id: str, temperature: int) -> bool:
    """Set target temperature."""
    return await self.set_sauna_control(sauna_id, {"temp": temperature})

# Mauvais
async def set_temperature(self, sauna_id, temperature):
    return await self.set_sauna_control(sauna_id, {"temp": temperature})
```

##### Docstrings

Documentez toutes les fonctions et classes :

```python
# Bon
async def get_sauna_status(self, sauna_id: str) -> dict[str, Any]:
    """Get status of a specific sauna.
    
    Args:
        sauna_id: Unique identifier of the sauna
        
    Returns:
        Dictionary containing sauna status data
        
    Raises:
        ApiError: If the API request fails
    """
    pass

# Mauvais
async def get_sauna_status(self, sauna_id):
    pass
```

##### Logging

Utilisez le logging approprié :

```python
import logging

_LOGGER = logging.getLogger(__name__)

# Bon
_LOGGER.debug("Fetching status for sauna %s", sauna_id)
_LOGGER.info("Successfully logged in to Klafs API")
_LOGGER.warning("Session expired, re-authenticating")
_LOGGER.error("Failed to connect to API: %s", error)

# Mauvais
print("Fetching status")
_LOGGER.info(f"Sauna ID: {sauna_id}")  # Éviter f-strings dans les logs
```

##### Gestion des erreurs

Gérez les erreurs de manière appropriée :

```python
# Bon
try:
    await self.client.power_on(sauna_id, pin)
except ApiError as err:
    _LOGGER.error("Failed to power on sauna: %s", err)
    raise HomeAssistantError("Cannot power on sauna") from err
except Exception as err:
    _LOGGER.exception("Unexpected error")
    raise

# Mauvais
try:
    await self.client.power_on(sauna_id, pin)
except:
    pass
```

#### Tests

Avant de soumettre une PR :

1. **Testez manuellement**
   - Installez dans votre Home Assistant de dev
   - Testez toutes les fonctionnalités affectées
   - Vérifiez les logs pour les erreurs

2. **Vérifiez le code**
   ```bash
   # Formatage
   black custom_components/klafs/
   
   # Linting
   pylint custom_components/klafs/
   
   # Type checking
   mypy custom_components/klafs/
   ```

3. **Testez les cas limites**
   - Connexion échouée
   - Session expirée
   - Sauna déconnecté
   - Valeurs invalides

#### Processus de Pull Request

1. **Mettez à jour votre branche**
   ```bash
   git fetch upstream
   git rebase upstream/main
   ```

2. **Committez vos changements**
   ```bash
   git add .
   git commit -m "feat: ajoute support du mode infrarouge"
   ```

   **Format des commits :**
   - `feat:` Nouvelle fonctionnalité
   - `fix:` Correction de bug
   - `docs:` Documentation
   - `style:` Formatage
   - `refactor:` Refactoring
   - `test:` Tests
   - `chore:` Maintenance

3. **Poussez vers votre fork**
   ```bash
   git push origin feature/ma-nouvelle-fonctionnalite
   ```

4. **Créez la Pull Request**
   - Allez sur GitHub
   - Cliquez sur "New Pull Request"
   - Remplissez le template

**Template de Pull Request :**

```markdown
## Description
[Description des changements]

## Type de changement
- [ ] Bug fix (changement non-breaking qui corrige un bug)
- [ ] Nouvelle fonctionnalité (changement non-breaking qui ajoute une fonctionnalité)
- [ ] Breaking change (correction ou fonctionnalité qui casse la compatibilité)
- [ ] Documentation

## Checklist
- [ ] Mon code suit les standards du projet
- [ ] J'ai effectué une auto-review de mon code
- [ ] J'ai commenté les parties complexes
- [ ] J'ai mis à jour la documentation
- [ ] Mes changements ne génèrent pas de nouveaux warnings
- [ ] J'ai testé localement
- [ ] J'ai vérifié les logs

## Tests effectués
[Décrivez vos tests]

## Screenshots (si applicable)
[Ajoutez des captures d'écran]
```

#### Review process

1. Un mainteneur reviewera votre PR
2. Des changements peuvent être demandés
3. Une fois approuvée, la PR sera mergée
4. Votre contribution sera ajoutée au CHANGELOG

### Contribuer à la documentation

La documentation est aussi importante que le code !

#### Types de documentation

- **README.md** : Vue d'ensemble et guide rapide
- **INSTALLATION.md** : Guide d'installation détaillé
- **API_DOCUMENTATION.md** : Documentation technique de l'API
- **EXAMPLES.md** : Exemples d'utilisation
- **TROUBLESHOOTING.md** : Guide de dépannage
- **PROJECT_STRUCTURE.md** : Architecture du projet

#### Comment contribuer

1. Identifiez ce qui manque ou est incorrect
2. Créez une issue ou directement une PR
3. Suivez le style existant
4. Ajoutez des exemples concrets
5. Vérifiez l'orthographe et la grammaire

#### Standards de documentation

- **Clarté** : Écrivez pour un débutant
- **Exemples** : Incluez toujours des exemples
- **Structure** : Utilisez des titres et listes
- **Liens** : Liez vers d'autres sections pertinentes
- **Mise à jour** : Gardez la doc synchronisée avec le code

### Traduire l'intégration

Pour ajouter une nouvelle langue :

1. **Créez le fichier de traduction**
   ```bash
   cp custom_components/klafs/translations/en.json \
      custom_components/klafs/translations/de.json
   ```

2. **Traduisez le contenu**
   ```json
   {
     "config": {
       "step": {
         "user": {
           "title": "Klafs Sauna konfigurieren",
           "description": "Geben Sie Ihre Klafs Sauna App Anmeldedaten ein",
           ...
         }
       }
     }
   }
   ```

3. **Testez la traduction**
   - Changez la langue dans Home Assistant
   - Vérifiez que tout s'affiche correctement

4. **Soumettez une PR**

## Questions fréquentes

### Comment tester sans sauna Klafs ?

Vous pouvez créer des mocks pour tester :

```python
# test_api.py
from unittest.mock import Mock, patch

@patch('custom_components.klafs.api.KlafsApiClient')
async def test_login(mock_client):
    mock_client.login.return_value = True
    # Vos tests ici
```

### Puis-je ajouter du support pour d'autres marques ?

Cette intégration est spécifique à Klafs. Pour d'autres marques, créez une nouvelle intégration.

### Comment déboguer l'API Klafs ?

Utilisez curl ou Postman pour tester les endpoints :

```bash
curl -v https://sauna-app.klafs.com/Control/GetSaunaStatus \
  -H "Content-Type: application/json" \
  --cookie "session=..." \
  -d '{"saunaId":"..."}'
```

### Où trouver de l'aide ?

- **Documentation** : Lisez PROJECT_STRUCTURE.md
- **Issues** : Cherchez dans les issues existantes
- **Discord** : Canal #development sur le Discord Home Assistant
- **Forum** : https://community.home-assistant.io

## Ressources utiles

### Home Assistant
- [Developer Docs](https://developers.home-assistant.io/)
- [Architecture](https://developers.home-assistant.io/docs/architecture_index)
- [Integration Quality Scale](https://developers.home-assistant.io/docs/integration_quality_scale_index)

### Python
- [PEP 8](https://pep8.org/)
- [Type Hints](https://docs.python.org/3/library/typing.html)
- [Asyncio](https://docs.python.org/3/library/asyncio.html)

### Git
- [Git Basics](https://git-scm.com/book/en/v2/Getting-Started-Git-Basics)
- [GitHub Flow](https://guides.github.com/introduction/flow/)

## Remerciements

Merci à tous les contributeurs qui rendent ce projet possible ! 🙏

Votre nom sera ajouté ici après votre première contribution.

## Contact

- **Issues** : https://github.com/votre-username/klafs-homeassistant/issues
- **Discussions** : https://github.com/votre-username/klafs-homeassistant/discussions
- **Email** : [votre-email] (pour les questions sensibles uniquement)

---

**Rappel** : Toute contribution doit respecter la licence MIT du projet.
