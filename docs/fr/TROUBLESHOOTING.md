# Guide de dépannage - Klafs Sauna

## Problèmes d'authentification

### Erreur "Invalid credentials"

**Symptômes :**
- Message d'erreur lors de la configuration
- Impossible d'ajouter l'intégration

**Solutions :**

1. **Vérifier les identifiants**
   - Testez vos identifiants sur https://sauna-app.klafs.com
   - Assurez-vous qu'il n'y a pas d'espaces avant/après
   - Vérifiez les majuscules/minuscules

2. **Compte bloqué**
   - Klafs bloque après 3 tentatives échouées
   - Attendez 30 minutes ou contactez le support Klafs
   - Réinitialisez votre mot de passe si nécessaire

3. **Vérifier les logs**
   ```
   Configuration > Logs
   Rechercher : "klafs"
   ```

### Session expirée

**Symptômes :**
- L'intégration fonctionnait puis s'arrête
- Erreur 401 dans les logs

**Solutions :**
- L'intégration se reconnecte automatiquement
- Si le problème persiste, rechargez l'intégration :
  ```
  Configuration > Intégrations > Klafs > Recharger
  ```

## Problèmes de découverte

### Aucun sauna détecté

**Symptômes :**
- L'intégration s'installe mais aucune entité n'apparaît
- Message "No devices found"

**Solutions :**

1. **Vérifier la configuration Klafs**
   - Ouvrez l'application Klafs Sauna App
   - Vérifiez que votre sauna apparaît
   - Assurez-vous que le module Wi-Fi est connecté

2. **Vérifier la connexion du sauna**
   - Le voyant Wi-Fi du sauna doit être allumé
   - Testez le contrôle depuis l'application mobile
   - Redémarrez le module Wi-Fi si nécessaire

3. **Recharger l'intégration**
   ```
   Configuration > Intégrations > Klafs > Recharger
   ```

4. **Supprimer et réinstaller**
   ```
   Configuration > Intégrations > Klafs > Supprimer
   Puis réinstaller l'intégration
   ```

### Sauna apparaît comme "Disconnected"

**Symptômes :**
- Entités créées mais statut "Disconnected"
- `isConnected: false` dans les attributs

**Solutions :**

1. **Vérifier le module Wi-Fi**
   - Redémarrez le module Wi-Fi du sauna
   - Vérifiez la connexion réseau du sauna
   - Assurez-vous que le sauna a accès à Internet

2. **Vérifier dans l'application Klafs**
   - Si déconnecté dans l'app, le problème vient du sauna
   - Suivez les instructions Klafs pour reconnecter

3. **Attendre la synchronisation**
   - Peut prendre jusqu'à 5 minutes
   - L'intégration poll toutes les 60 secondes

## Problèmes de contrôle

### Impossible d'allumer le sauna

**Symptômes :**
- Le bouton d'allumage ne fonctionne pas
- Erreur dans les logs

**Solutions :**

1. **Vérifier le code PIN**
   - Le PIN est-il configuré dans l'intégration ?
   - Le PIN correspond-il à celui du sauna ?
   - Reconfigurez l'intégration avec le bon PIN :
     ```
     Configuration > Intégrations > Klafs > Configurer
     ```

2. **Vérifier le contrôle de porte**
   - Le sauna Klafs nécessite un contrôle de porte
   - Ouvrez et fermez la porte du sauna
   - Vérifiez le capteur de porte

3. **Utiliser le service avec PIN**
   ```yaml
   service: klafs.power_on_with_pin
   target:
     entity_id: climate.klafs_sauna
   data:
     pin: "1234"
   ```

4. **Vérifier le statut**
   - Le sauna doit être connecté (`isConnected: true`)
   - Vérifiez qu'il n'y a pas d'erreur sur le sauna

### Les changements de température ne fonctionnent pas

**Symptômes :**
- La température ne change pas
- Pas d'erreur mais pas d'effet

**Solutions :**

1. **Vérifier les limites**
   - Mode Sauna : 10-100°C
   - Mode SANARIUM : 40-75°C
   - Mode IR : 30-100°C

2. **Vérifier le mode actif**
   - La température doit correspondre au mode
   - Changez de mode si nécessaire

3. **Attendre la synchronisation**
   - Les changements peuvent prendre 1-2 minutes
   - L'API Klafs a un délai de propagation

4. **Vérifier les logs**
   ```
   Configuration > Logs
   Niveau : Debug
   Rechercher : "klafs"
   ```

### Le mode SANARIUM ne fonctionne pas

**Symptômes :**
- L'interrupteur SANARIUM ne change rien
- Pas d'option d'humidité

**Solutions :**

1. **Vérifier la compatibilité**
   - Votre sauna doit avoir l'option SANARIUM
   - Vérifiez dans l'application Klafs

2. **Vérifier les attributs**
   ```yaml
   # Dans Developer Tools > States
   climate.klafs_sauna
   # Attributs :
   sanariumSelected: true/false
   ```

3. **Utiliser le service**
   ```yaml
   service: klafs.set_humidity_level
   target:
     entity_id: climate.klafs_sauna
   data:
     humidity_level: 7
   ```

## Problèmes de performance

### Mises à jour lentes

**Symptômes :**
- Les changements mettent du temps à apparaître
- Délai entre l'action et la mise à jour

**Explications :**
- L'intégration poll toutes les 60 secondes
- L'API Klafs a un délai de propagation
- C'est normal et par design

**Solutions :**
- Réduire l'intervalle (non recommandé) :
  ```python
  # Dans custom_components/klafs/__init__.py
  SCAN_INTERVAL = timedelta(seconds=30)  # Au lieu de 60
  ```
- Accepter le délai (recommandé)

### Erreurs de timeout

**Symptômes :**
- Erreurs "Timeout" dans les logs
- Entités deviennent "unavailable"

**Solutions :**

1. **Vérifier la connexion Internet**
   - Testez la connexion de Home Assistant
   - Vérifiez les DNS

2. **Vérifier l'API Klafs**
   - Testez https://sauna-app.klafs.com
   - Peut être en maintenance

3. **Augmenter le timeout**
   ```python
   # Dans custom_components/klafs/api.py
   async with self.session.post(..., timeout=30) as response:
   ```

## Problèmes d'installation

### L'intégration n'apparaît pas

**Symptômes :**
- Pas de "Klafs Sauna" dans la liste des intégrations

**Solutions :**

1. **Vérifier l'installation**
   ```
   config/custom_components/klafs/
   ├── __init__.py
   ├── manifest.json
   ├── config_flow.py
   ├── ...
   ```

2. **Vérifier les permissions**
   - Les fichiers doivent être lisibles par Home Assistant
   - Sous Linux : `chmod -R 755 custom_components/klafs`

3. **Vérifier les logs au démarrage**
   ```
   Configuration > Logs
   Rechercher : "klafs" ou "custom_components"
   ```

4. **Redémarrer en mode sans échec**
   ```
   Configuration > Système > Redémarrer en mode sans échec
   ```

5. **Vérifier manifest.json**
   - Doit être un JSON valide
   - Vérifier avec un validateur JSON

### Erreur "Version required"

**Symptômes :**
- Message d'erreur au démarrage
- L'intégration ne charge pas

**Solution :**
- Vérifiez que `manifest.json` contient :
  ```json
  {
    "version": "1.0.0"
  }
  ```

## Débogage avancé

### Activer les logs détaillés

Ajoutez dans `configuration.yaml` :

```yaml
logger:
  default: info
  logs:
    custom_components.klafs: debug
    custom_components.klafs.api: debug
```

Puis redémarrez Home Assistant.

### Tester l'API manuellement

```bash
# Login
curl -c cookie.txt -X POST https://sauna-app.klafs.com/Account/Login \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "UserName=VOTRE_EMAIL&Password=VOTRE_PASSWORD"

# Obtenir le statut
curl -b cookie.txt -X POST https://sauna-app.klafs.com/Control/GetSaunaStatus \
  -H "Content-Type: application/json" \
  -d '{"saunaId":"VOTRE_SAUNA_ID"}'
```

### Vérifier les entités

Dans Developer Tools > States :

```
climate.klafs_sauna_XXXXXXXX
sensor.klafs_sauna_XXXXXXXX_temperature
sensor.klafs_sauna_XXXXXXXX_humidity
sensor.klafs_sauna_XXXXXXXX_status
switch.klafs_sauna_XXXXXXXX_sanarium_mode
```

### Inspecter les attributs

```yaml
# Developer Tools > States
# Sélectionner : climate.klafs_sauna

# Attributs importants :
is_connected: true/false
is_ready_for_use: true/false
status_code: 0/1/2/3
mode: "Sauna" / "SANARIUM" / "Infrared"
```

## Problèmes connus

### 1. Délai de mise à jour

**Problème :** Les changements prennent 1-2 minutes à apparaître

**Cause :** Polling toutes les 60 secondes + délai API Klafs

**Solution :** C'est normal, pas de solution

### 2. Compte bloqué après erreur

**Problème :** 3 tentatives échouées = compte bloqué

**Cause :** Sécurité Klafs

**Solution :** Attendre 30 minutes ou contacter Klafs

### 3. PIN requis pour allumer

**Problème :** Impossible d'allumer sans PIN

**Cause :** Sécurité Klafs

**Solution :** Configurer le PIN dans l'intégration

## Obtenir de l'aide

### Informations à fournir

Quand vous demandez de l'aide, incluez :

1. **Version de Home Assistant**
   ```
   Configuration > Informations > Version
   ```

2. **Version de l'intégration**
   ```
   Configuration > Intégrations > Klafs > Version
   ```

3. **Logs pertinents**
   ```
   Configuration > Logs
   Copier les erreurs liées à "klafs"
   ```

4. **Configuration (sans credentials)**
   ```yaml
   # Anonymisez username/password/pin
   username: "user@*****.com"
   password: "****"
   pin: "****"
   ```

5. **Comportement observé vs attendu**

### Où demander de l'aide

1. **GitHub Issues**
   - https://github.com/votre-username/klafs-homeassistant/issues
   - Créez une nouvelle issue avec le template

2. **Forum Home Assistant**
   - https://community.home-assistant.io
   - Section "Third party integrations"

3. **Discord Home Assistant**
   - Canal #custom-components

## Réinitialisation complète

Si rien ne fonctionne :

1. **Supprimer l'intégration**
   ```
   Configuration > Intégrations > Klafs > Supprimer
   ```

2. **Supprimer les fichiers**
   ```
   rm -rf config/custom_components/klafs
   ```

3. **Redémarrer Home Assistant**

4. **Réinstaller l'intégration**

5. **Reconfigurer avec les bons identifiants**

## Ressources utiles

- [README.md](README.md) - Documentation principale
- [API_DOCUMENTATION.md](API_DOCUMENTATION.md) - Détails de l'API
- [EXAMPLES.md](EXAMPLES.md) - Exemples d'utilisation
- [GitHub Issues](https://github.com/votre-username/klafs-homeassistant/issues)
- [Forum Home Assistant](https://community.home-assistant.io)
