# Support Multi-Saunas - Documentation

## Vue d'ensemble

L'intégration Klafs pour Home Assistant supporte maintenant la gestion de plusieurs saunas depuis un seul compte Klafs. Chaque sauna peut avoir son propre code PIN et apparaît comme un appareil séparé dans Home Assistant.

## Fonctionnement

### Architecture

```
Compte Klafs
    ├── Sauna 1 (Salon)
    │   ├── PIN: 1234
    │   ├── Entités: climate, sensors, switch
    │   └── Device: "Klafs Salon"
    │
    ├── Sauna 2 (Chambre)
    │   ├── PIN: 5678
    │   ├── Entités: climate, sensors, switch
    │   └── Device: "Klafs Chambre"
    │
    └── Sauna 3 (Spa)
        ├── PIN: 9012
        ├── Entités: climate, sensors, switch
        └── Device: "Klafs Spa"
```

### Processus de configuration

#### Étape 1 : Authentification
L'utilisateur entre ses identifiants Klafs (email + mot de passe).

```python
# config_flow.py - async_step_user()
- Demande username/password
- Teste la connexion avec l'API Klafs
- Si succès → Étape 2
```

#### Étape 2 : Sélection des saunas
L'intégration récupère la liste de tous les saunas du compte et permet à l'utilisateur de sélectionner ceux qu'il souhaite ajouter.

```python
# config_flow.py - async_step_select_saunas()
- Appelle API: GET /Control/GetSaunas
- Affiche une liste de sélection multiple
- L'utilisateur coche les saunas désirés
- Si au moins 1 sélectionné → Étape 3
```

**Réponse API exemple :**
```json
{
  "364cc9db-86f1-49d1-86cd-f6ef9b20a490": {
    "name": "Sauna Salon",
    "type": "SANARIUM"
  },
  "7a8b9c0d-1e2f-3g4h-5i6j-7k8l9m0n1o2p": {
    "name": "Sauna Chambre",
    "type": "Sauna"
  }
}
```

#### Étape 3 : Configuration des PINs
Pour chaque sauna sélectionné, l'utilisateur peut entrer un code PIN (optionnel).

```python
# config_flow.py - async_step_configure_pins()
- Affiche un champ de saisie par sauna
- Format: pin_<sauna_id>
- Optionnel: peut être laissé vide
- Sauvegarde dans entry.data
```

**Interface utilisateur :**
```
Configurez les codes PIN

Entrez le code PIN pour chaque sauna (optionnel mais requis 
pour allumer le sauna à distance).

Saunas sélectionnés :
• Sauna Salon
• Sauna Chambre

PIN pour Sauna Salon: [____]
PIN pour Sauna Chambre: [____]

[Suivant]
```

### Structure des données

#### Config Entry Data
```python
{
    "username": "user@example.com",
    "password": "secret_password",
    "saunas": {
        "364cc9db-86f1-49d1-86cd-f6ef9b20a490": {
            "name": "Sauna Salon",
            "pin": "1234"
        },
        "7a8b9c0d-1e2f-3g4h-5i6j-7k8l9m0n1o2p": {
            "name": "Sauna Chambre",
            "pin": "5678"
        }
    }
}
```

#### Coordinator Data
```python
{
    "364cc9db-86f1-49d1-86cd-f6ef9b20a490": {
        "saunaId": "364cc9db-86f1-49d1-86cd-f6ef9b20a490",
        "currentTemperature": 25,
        "isPoweredOn": False,
        "isConnected": True,
        ...
    },
    "7a8b9c0d-1e2f-3g4h-5i6j-7k8l9m0n1o2p": {
        "saunaId": "7a8b9c0d-1e2f-3g4h-5i6j-7k8l9m0n1o2p",
        "currentTemperature": 22,
        "isPoweredOn": False,
        "isConnected": True,
        ...
    }
}
```

## Implémentation technique

### Modifications du Config Flow

**Avant (version simple) :**
```python
class KlafsConfigFlow:
    async def async_step_user(self, user_input):
        # Demande username/password/pin
        # Crée l'entry directement
```

**Après (version multi-saunas) :**
```python
class KlafsConfigFlow:
    def __init__(self):
        self._username = None
        self._password = None
        self._client = None
        self._saunas = {}
        self._selected_saunas = {}
    
    async def async_step_user(self, user_input):
        # Demande username/password uniquement
        # Stocke les credentials
        # → async_step_select_saunas()
    
    async def async_step_select_saunas(self, user_input):
        # Récupère la liste des saunas
        # Affiche une sélection multiple
        # → async_step_configure_pins()
    
    async def async_step_configure_pins(self, user_input):
        # Demande un PIN par sauna
        # Crée l'entry avec toutes les données
```

### Modifications du Coordinator

**Nouvelles méthodes :**
```python
class KlafsDataUpdateCoordinator:
    def __init__(self, hass, client, entry):
        self.saunas_config = entry.data.get("saunas", {})
    
    async def _async_update_data(self):
        # Ne poll que les saunas configurés
        data = {}
        for sauna_id in self.saunas_config:
            status = await self.client.get_sauna_status(sauna_id)
            data[sauna_id] = status
        return data
    
    def get_sauna_pin(self, sauna_id: str) -> str | None:
        """Récupère le PIN d'un sauna spécifique."""
        if sauna_id in self.saunas_config:
            return self.saunas_config[sauna_id].get("pin")
        return None
    
    def get_sauna_name(self, sauna_id: str) -> str:
        """Récupère le nom d'un sauna spécifique."""
        if sauna_id in self.saunas_config:
            return self.saunas_config[sauna_id].get("name", sauna_id[:8])
        return sauna_id[:8]
```

### Modifications des Entités

**Climate Entity :**
```python
class KlafsSaunaClimate:
    async def async_set_hvac_mode(self, hvac_mode):
        if hvac_mode == HVACMode.HEAT:
            # Récupère le PIN spécifique à ce sauna
            pin = self.coordinator.get_sauna_pin(self._sauna_id)
            await self.coordinator.client.power_on(self._sauna_id, pin)
```

**Device Info :**
```python
@property
def device_info(self):
    # Utilise le nom configuré
    sauna_name = self.coordinator.get_sauna_name(self._sauna_id)
    return {
        "identifiers": {(DOMAIN, self._sauna_id)},
        "name": f"Klafs {sauna_name}",
        "manufacturer": "Klafs",
        "model": "Sauna",
    }
```

## Entités créées

Pour chaque sauna sélectionné, les entités suivantes sont créées :

### Exemple avec 2 saunas

**Sauna 1 : "Salon" (364cc9db)**
- `climate.klafs_salon`
- `sensor.klafs_salon_temperature`
- `sensor.klafs_salon_humidity`
- `sensor.klafs_salon_status`
- `switch.klafs_salon_sanarium_mode`

**Sauna 2 : "Chambre" (7a8b9c0d)**
- `climate.klafs_chambre`
- `sensor.klafs_chambre_temperature`
- `sensor.klafs_chambre_humidity`
- `sensor.klafs_chambre_status`
- `switch.klafs_chambre_sanarium_mode`

## Cas d'usage

### Scénario 1 : Maison avec 2 saunas

**Configuration :**
- Sauna principal (salon) : PIN 1234
- Sauna invités (sous-sol) : PIN 5678

**Automatisation :**
```yaml
automation:
  # Préchauffer le sauna principal en semaine
  - alias: "Sauna principal soir"
    trigger:
      - platform: time
        at: "18:00:00"
    condition:
      - condition: time
        weekday: [mon, tue, wed, thu, fri]
    action:
      - service: climate.turn_on
        target:
          entity_id: climate.klafs_salon

  # Préchauffer le sauna invités le week-end
  - alias: "Sauna invités week-end"
    trigger:
      - platform: time
        at: "10:00:00"
    condition:
      - condition: time
        weekday: [sat, sun]
    action:
      - service: climate.turn_on
        target:
          entity_id: climate.klafs_sous_sol
```

### Scénario 2 : Spa avec 3 saunas

**Configuration :**
- Sauna finlandais : PIN 1111
- Sauna infrarouge : PIN 2222
- SANARIUM : PIN 3333

**Dashboard :**
```yaml
type: vertical-stack
cards:
  - type: horizontal-stack
    cards:
      - type: thermostat
        entity: climate.klafs_finlandais
      - type: thermostat
        entity: climate.klafs_infrarouge
      - type: thermostat
        entity: climate.klafs_sanarium
  
  - type: entities
    title: Statuts
    entities:
      - sensor.klafs_finlandais_status
      - sensor.klafs_infrarouge_status
      - sensor.klafs_sanarium_status
```

## Migration depuis version simple

Si vous aviez configuré l'intégration avec la version simple (1 sauna, PIN global), vous devrez :

1. **Supprimer l'ancienne intégration**
   ```
   Configuration > Intégrations > Klafs > Supprimer
   ```

2. **Réinstaller avec la nouvelle version**
   ```
   Configuration > Intégrations > + Ajouter > Klafs Sauna
   ```

3. **Reconfigurer**
   - Entrez vos identifiants
   - Sélectionnez votre(vos) sauna(s)
   - Entrez le(s) PIN(s)

4. **Mettre à jour vos automatisations**
   - Les entity_id peuvent avoir changé
   - Vérifiez les noms des entités

## Limitations

### Actuelles
- Pas de support pour ajouter/retirer des saunas après configuration initiale
- Pour modifier les saunas sélectionnés, il faut supprimer et reconfigurer l'intégration
- Les PINs ne peuvent pas être modifiés sans reconfiguration

### Futures améliorations
- Options flow pour ajouter/retirer des saunas
- Options flow pour modifier les PINs
- Support de la reconfiguration sans suppression

## Sécurité

### Stockage des PINs
- Les PINs sont stockés dans `config_entries` (chiffrés par Home Assistant)
- Jamais loggés en clair
- Transmis uniquement via HTTPS à l'API Klafs

### Bonnes pratiques
- Utilisez des PINs différents pour chaque sauna
- Ne partagez pas vos PINs
- Changez les PINs régulièrement sur les saunas physiques
- Reconfigurez l'intégration après changement de PIN

## Dépannage

### Problème : Sauna non détecté

**Cause :** Le sauna n'est pas configuré dans l'application Klafs

**Solution :**
1. Ouvrez l'application Klafs Sauna App
2. Vérifiez que le sauna apparaît
3. Assurez-vous que le module Wi-Fi est connecté
4. Reconfigurez l'intégration

### Problème : PIN ne fonctionne pas

**Cause :** Le PIN n'est pas configuré sur le sauna ou est incorrect

**Solution :**
1. Vérifiez le PIN sur le panneau de contrôle du sauna
2. Reconfigurez l'intégration avec le bon PIN
3. Testez depuis l'application Klafs d'abord

### Problème : Impossible de sélectionner plusieurs saunas

**Cause :** Bug dans le config flow

**Solution :**
1. Vérifiez les logs Home Assistant
2. Créez une issue GitHub avec les logs
3. En attendant, configurez les saunas un par un (créez plusieurs intégrations)

## Tests

### Test manuel

1. **Configurer avec 2 saunas fictifs**
   - Utilisez des identifiants de test
   - Sélectionnez 2 saunas
   - Entrez des PINs différents

2. **Vérifier les entités**
   ```
   Developer Tools > States
   Rechercher : klafs
   ```

3. **Tester les commandes**
   ```yaml
   service: climate.turn_on
   target:
     entity_id: climate.klafs_sauna_1
   ```

4. **Vérifier les PINs**
   - Allumer chaque sauna
   - Vérifier dans les logs que le bon PIN est utilisé

## Ressources

- [Config Flow Documentation](https://developers.home-assistant.io/docs/config_entries_config_flow_handler)
- [Multi-Select Selector](https://www.home-assistant.io/docs/blueprint/selectors/#multi-select-selector)
- [Data Entry Flow](https://developers.home-assistant.io/docs/data_entry_flow_index)

## Changelog

### Version 1.0.0
- ✅ Support multi-saunas
- ✅ PIN individuel par sauna
- ✅ Config flow en 3 étapes
- ✅ Noms personnalisés par sauna
- ✅ Sélection multiple de saunas
