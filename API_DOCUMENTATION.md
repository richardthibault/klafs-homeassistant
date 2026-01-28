# Documentation API Klafs

Cette documentation détaille l'API REST utilisée par Klafs pour contrôler les saunas via le cloud.

## URL de base

```
https://sauna-app.klafs.com
```

## Authentification

### Login

**Endpoint:** `POST /Account/Login`

**Headers:**
```
Content-Type: application/x-www-form-urlencoded
```

**Body:**
```
UserName=votre_email@example.com&Password=votre_mot_de_passe
```

**Réponse:**
- Status 200 : Authentification réussie
- Cookies : Session cookie pour les requêtes suivantes

**Exemple curl:**
```bash
curl -vL https://sauna-app.klafs.com/Account/Login \
  -H "Content-Type: application/x-www-form-urlencoded" \
  --data "UserName=user@example.com&Password=secret" \
  --cookie-jar cookie.txt
```

⚠️ **Important:** Klafs bloque le compte après 3 tentatives échouées.

## Endpoints

### 1. Obtenir la liste des saunas

**Endpoint:** `GET /Control/GetSaunas`

**Headers:**
```
Cookie: [session cookie from login]
```

**Réponse:**
```json
[
  {
    "saunaId": "364cc9db-86f1-49d1-86cd-f6ef9b20a490",
    "name": "Mon Sauna",
    "type": "SANARIUM"
  }
]
```

### 2. Obtenir le statut d'un sauna

**Endpoint:** `POST /Control/GetSaunaStatus`

**Headers:**
```
Content-Type: application/json
Cookie: [session cookie]
```

**Body:**
```json
{
  "saunaId": "364cc9db-86f1-49d1-86cd-f6ef9b20a490"
}
```

**Réponse:**
```json
{
  "saunaId": "364cc9db-86f1-49d1-86cd-f6ef9b20a490",
  "saunaSelected": false,
  "sanariumSelected": true,
  "irSelected": false,
  "selectedSaunaTemperature": 90,
  "selectedSanariumTemperature": 70,
  "selectedIrTemperature": 100,
  "selectedHumLevel": 7,
  "selectedIrLevel": 3,
  "selectedHour": 12,
  "selectedMinute": 40,
  "isConnected": false,
  "isPoweredOn": false,
  "isReadyForUse": false,
  "currentTemperature": 18,
  "currentHumidity": 0,
  "statusCode": 2,
  "statusMessage": null,
  "showBathingHour": false,
  "bathingHours": 0,
  "bathingMinutes": 0,
  "currentHumidityStatus": 0,
  "currentTemperatureStatus": 0
}
```

**Exemple curl:**
```bash
curl -v --cookie cookie.txt \
  https://sauna-app.klafs.com/Control/GetSaunaStatus \
  -H "Content-Type: application/json" \
  --data '{"saunaId":"364cc9db-86f1-49d1-86cd-f6ef9b20a490"}'
```

### 3. Contrôler le sauna

**Endpoint:** `POST /Control/SetSaunaControl`

**Headers:**
```
Content-Type: application/json
Cookie: [session cookie]
```

**Body (exemples):**

#### Allumer le sauna
```json
{
  "saunaId": "364cc9db-86f1-49d1-86cd-f6ef9b20a490",
  "powerOn": true,
  "pin": "1234"
}
```

#### Éteindre le sauna
```json
{
  "saunaId": "364cc9db-86f1-49d1-86cd-f6ef9b20a490",
  "powerOn": false
}
```

#### Changer la température (mode Sauna)
```json
{
  "saunaId": "364cc9db-86f1-49d1-86cd-f6ef9b20a490",
  "selectedSaunaTemperature": 85
}
```

#### Changer la température (mode SANARIUM)
```json
{
  "saunaId": "364cc9db-86f1-49d1-86cd-f6ef9b20a490",
  "selectedSanariumTemperature": 65
}
```

#### Changer le niveau d'humidité (SANARIUM)
```json
{
  "saunaId": "364cc9db-86f1-49d1-86cd-f6ef9b20a490",
  "selectedHumLevel": 7
}
```

#### Changer le mode
```json
{
  "saunaId": "364cc9db-86f1-49d1-86cd-f6ef9b20a490",
  "saunaSelected": false,
  "sanariumSelected": true,
  "irSelected": false
}
```

#### Programmer l'heure de démarrage
```json
{
  "saunaId": "364cc9db-86f1-49d1-86cd-f6ef9b20a490",
  "selectedHour": 18,
  "selectedMinute": 30
}
```

## Champs de réponse

### Statut du sauna

| Champ | Type | Description |
|-------|------|-------------|
| `saunaId` | string | Identifiant unique du sauna |
| `saunaSelected` | boolean | Mode Sauna classique activé |
| `sanariumSelected` | boolean | Mode SANARIUM activé |
| `irSelected` | boolean | Mode Infrarouge activé |
| `selectedSaunaTemperature` | int | Température cible mode Sauna (10-100°C) |
| `selectedSanariumTemperature` | int | Température cible mode SANARIUM (40-75°C) |
| `selectedIrTemperature` | int | Température cible mode IR (30-100°C) |
| `selectedHumLevel` | int | Niveau d'humidité SANARIUM (1-10) |
| `selectedIrLevel` | int | Niveau infrarouge (1-10) |
| `selectedHour` | int | Heure de démarrage programmée (0-23) |
| `selectedMinute` | int | Minute de démarrage programmée (0-59) |
| `isConnected` | boolean | Sauna connecté au cloud |
| `isPoweredOn` | boolean | Sauna allumé |
| `isReadyForUse` | boolean | Sauna prêt (température atteinte) |
| `currentTemperature` | int | Température actuelle en °C |
| `currentHumidity` | int | Humidité actuelle en % |
| `statusCode` | int | Code de statut (voir ci-dessous) |
| `statusMessage` | string | Message de statut |
| `bathingHours` | int | Heures de bain restantes |
| `bathingMinutes` | int | Minutes de bain restantes |

### Codes de statut

| Code | Description |
|------|-------------|
| 0 | Éteint |
| 1 | En chauffe |
| 2 | Prêt |
| 3 | Erreur |

## Limites et contraintes

### Températures

| Mode | Min | Max |
|------|-----|-----|
| Sauna | 10°C | 100°C |
| SANARIUM | 40°C | 75°C |
| Infrarouge | 30°C | 100°C |

### Humidité (SANARIUM uniquement)

- Niveaux : 1 à 10
- 1 = Faible humidité
- 10 = Humidité maximale

### Sécurité

- **Code PIN requis** pour allumer le sauna
- Le PIN doit être configuré sur le panneau de contrôle du sauna
- **Contrôle de porte** requis avant l'allumage
- **Timeout automatique** après un certain temps d'utilisation

### Rate Limiting

- Pas de limite documentée officiellement
- Recommandation : polling toutes les 60 secondes maximum
- Éviter les requêtes trop fréquentes pour ne pas surcharger l'API

## Séquence typique d'utilisation

### 1. Démarrage du sauna

```bash
# 1. Login
curl -c cookie.txt -X POST https://sauna-app.klafs.com/Account/Login \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "UserName=user@example.com&Password=secret"

# 2. Obtenir la liste des saunas
curl -b cookie.txt https://sauna-app.klafs.com/Control/GetSaunas

# 3. Vérifier le statut
curl -b cookie.txt -X POST https://sauna-app.klafs.com/Control/GetSaunaStatus \
  -H "Content-Type: application/json" \
  -d '{"saunaId":"364cc9db-86f1-49d1-86cd-f6ef9b20a490"}'

# 4. Régler la température
curl -b cookie.txt -X POST https://sauna-app.klafs.com/Control/SetSaunaControl \
  -H "Content-Type: application/json" \
  -d '{"saunaId":"364cc9db-86f1-49d1-86cd-f6ef9b20a490","selectedSaunaTemperature":85}'

# 5. Allumer le sauna
curl -b cookie.txt -X POST https://sauna-app.klafs.com/Control/SetSaunaControl \
  -H "Content-Type: application/json" \
  -d '{"saunaId":"364cc9db-86f1-49d1-86cd-f6ef9b20a490","powerOn":true,"pin":"1234"}'

# 6. Vérifier le statut (polling)
while true; do
  curl -b cookie.txt -X POST https://sauna-app.klafs.com/Control/GetSaunaStatus \
    -H "Content-Type: application/json" \
    -d '{"saunaId":"364cc9db-86f1-49d1-86cd-f6ef9b20a490"}'
  sleep 60
done
```

## Gestion des erreurs

### Erreurs d'authentification

- **401 Unauthorized** : Session expirée, refaire le login
- **403 Forbidden** : Compte bloqué (3 tentatives échouées)

### Erreurs de contrôle

- **400 Bad Request** : Paramètres invalides
- **404 Not Found** : Sauna non trouvé
- **500 Internal Server Error** : Erreur serveur Klafs

### Recommandations

1. Implémenter un système de retry avec backoff exponentiel
2. Gérer l'expiration de session et re-login automatique
3. Logger les erreurs pour le débogage
4. Valider les paramètres avant l'envoi

## Notes d'implémentation

### Session Management

- Les cookies de session expirent après un certain temps d'inactivité
- Implémenter une détection d'expiration et re-login automatique
- Stocker les cookies de manière sécurisée

### Polling Strategy

- Intervalle recommandé : 60 secondes
- Augmenter la fréquence uniquement pendant le préchauffage
- Réduire la fréquence quand le sauna est éteint

### Sécurité

- Ne jamais logger le mot de passe ou le PIN
- Utiliser HTTPS uniquement
- Stocker les credentials de manière sécurisée (keyring, vault, etc.)

## Ressources

- Application web : https://sauna-app.klafs.com
- Site officiel : https://www.klafs.com
- Projet IP-Symcon : https://github.com/Pommespanzer/IPSymconKlafsSaunaControl
- Discussion OpenHAB : https://community.openhab.org/t/klafs-sauna-binding/75291

## Avertissement

Cette documentation est basée sur l'ingénierie inverse de l'API Klafs et n'est pas officielle. L'API peut changer sans préavis. Utilisez à vos propres risques.
