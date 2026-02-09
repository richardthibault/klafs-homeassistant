# Découverte de l'API Klafs - Résultats

## Résumé

L'API Klafs n'est **pas une API REST/JSON classique** mais une **application web ASP.NET MVC** avec des formulaires HTML et des appels AJAX.

## Architecture

- **Type**: Application web ASP.NET MVC (Microsoft-IIS/10.0)
- **Base URL**: `https://sauna-app.klafs.com`
- **Authentification**: Cookie-based (`__RequestVerificationToken`)
- **Format**: JSON pour les données, mais pas d'API REST pure

## Endpoints Découverts

### Authentification
```
POST /Account/Login
Content-Type: application/x-www-form-urlencoded

Body:
  UserName=<email>
  Password=<password>

Response: 200 OK + Cookie __RequestVerificationToken
```

### Liste des Saunas
```
GET /SaunaApp

Response: Page HTML contenant un <select> avec les saunas
Format: <option value="sauna-id">Sauna Name</option>
```

**Exemple de sauna:**
- Nom: `Mon Sauna`
- ID: `xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx`

### Récupérer le Statut
```
GET /SaunaApp/GetData?id={sauna_id}

Response: JSON
{
  "saunaId": "...",
  "isPoweredOn": true/false,
  "isReadyForUse": true/false,
  "currentTemperature": 79,
  "selectedSaunaTemperature": 81,
  "selectedMode": 1,  // 1=Sauna, 2=Sanarium, 3=IR
  "currentHumidity": 0,
  "selectedHumLevel": 0,
  "remainingBathingHours": 2,
  "remainingBathingMinutes": 39,
  "isConnected": true,
  "opStatus": 2,
  "Success": true,
  ...
}
```

### Démarrer le Sauna
```
POST /SaunaApp/StartCabin
Content-Type: application/json

Body:
{
  "id": "sauna-id",
  "pin": "1234",
  "time_selected": false,
  "sel_hour": 0,
  "sel_min": 0
}

Response: JSON { "Success": true/false, ... }
```

### Arrêter le Sauna
```
POST /SaunaApp/StopCabin
Content-Type: application/json

Body:
{
  "id": "sauna-id"
}

Response: JSON { "Success": true/false, ... }
```

### Changer le Mode
```
POST /SaunaApp/SetMode
Content-Type: application/json

Body:
{
  "id": "sauna-id",
  "mode": 1  // 1=Sauna, 2=Sanarium, 3=IR
}

Response: JSON { "Success": true/false, ... }
```

### Changer la Température
```
POST /SaunaApp/ChangeTemperature
Content-Type: application/json

Body:
{
  "id": "sauna-id",
  "temp": 85
}

Response: JSON { "Success": true/false, ... }
```

### Changer l'Humidité (Sanarium uniquement)
```
POST /SaunaApp/ChangeHumLevel
Content-Type: application/json

Body:
{
  "id": "sauna-id",
  "level": 7  // 0-10
}

Response: JSON { "Success": true/false, ... }
```

### Définir l'Heure de Démarrage
```
POST /SaunaApp/SetSelectedTime
Content-Type: application/json

Body:
{
  "id": "sauna-id",
  "hour": 18,
  "minute": 30
}

Response: JSON { "Success": true/false, ... }
```

## Autres Endpoints Disponibles

- `POST /SaunaApp/FavoriteSelected` - Sélectionner un programme favori
- `POST /SaunaApp/AddFavorite` - Ajouter un favori
- `POST /SaunaApp/DeleteFavorite` - Supprimer un favori
- `POST /SaunaApp/ChangeFavorite` - Modifier un favori
- `POST /SaunaApp/LightChange` - Contrôler l'éclairage
- `POST /SaunaApp/SetBathingTime` - Définir la durée de bain
- `POST /SaunaApp/StartInfusion` - Démarrer une infusion
- `POST /SaunaApp/ChangeIRLevel` - Changer le niveau IR

## Méthode de Découverte

1. **Test des endpoints supposés** → Tous retournaient 404
2. **Analyse de la page HTML** après login → Trouvé `/SaunaApp`
3. **Téléchargement des scripts JavaScript** → Trouvé `iw.global.js`
4. **Analyse du code JavaScript** → Trouvé `sendPostRequest('StartCabin', ...)`
5. **Extraction de la structure des données** → Trouvé les payloads JSON
6. **Test avec les vrais endpoints** → ✓ Succès !

## Implémentation dans Home Assistant

L'intégration a été mise à jour avec :
- ✓ Vrais endpoints API
- ✓ Parsing HTML pour récupérer la liste des saunas
- ✓ Structure de données correcte
- ✓ Gestion du PIN par sauna
- ✓ Support multi-sauna

## Prochaines Étapes

1. Redémarrer Home Assistant
2. Supprimer l'ancienne configuration Klafs
3. Reconfigurer l'intégration avec tes credentials
4. Tester le contrôle du sauna depuis Home Assistant

## Notes Importantes

- Le **PIN est obligatoire** pour démarrer le sauna
- L'API utilise des **cookies** pour l'authentification (pas de token JWT)
- Le **polling** est nécessaire pour les mises à jour de statut (pas de webhooks)
- La structure HTML peut changer, mais les endpoints AJAX sont plus stables
