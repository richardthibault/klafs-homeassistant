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
  "saunaId": "108aac58-da8d-48b2-956a-af160ac26326",
  "saunaSelected": false,           // Mode Sauna sélectionné
  "sanariumSelected": true,          // Mode SANARIUM sélectionné
  "irSelected": false,               // Mode Infrarouge sélectionné
  "selectedSaunaTemperature": 81,    // Température préférée mode Sauna
  "selectedSanariumTemperature": 75, // Température préférée mode SANARIUM
  "selectedIrTemperature": 27,       // Température préférée mode IR (27 = non supporté)
  "selectedHumLevel": 0,             // Niveau humidité SANARIUM (0-10)
  "selectedIrLevel": 3,              // Niveau IR (1-5)
  "selectedHour": 21,                // Heure démarrage programmé
  "selectedMinute": 35,              // Minute démarrage programmé
  "isConnected": true,               // Sauna connecté au réseau
  "isPoweredOn": false,              // Sauna allumé
  "isReadyForUse": false,            // Sauna prêt (température atteinte)
  "currentTemperature": 141,         // Température actuelle (°C)
  "currentHumidity": 0,              // Humidité actuelle (%)
  "statusCode": 0,                   // Code statut (0=OK)
  "statusMessage": null,             // Message statut
  "showRemainingBathingTime": false, // Afficher temps restant
  "remainingBathingHours": 0,        // Heures restantes
  "remainingBathingMinutes": 0,      // Minutes restantes
  "currentHumidityStatus": 0,        // Statut humidité
  "currentTemperatureStatus": 0,     // Statut température
  "selectedMode": 2,                 // Mode actuel (1=Sauna, 2=SANARIUM, 3=IR)
  "selectedTemperature": 75,         // Température cible du mode actuel
  "lightIsOn": false,                // Lumière allumée
  "lightBrightness": 0,              // Luminosité (0-100)
  "colorLightIsOn": false,           // Lumière couleur allumée
  "sunsetIsOn": false,               // Mode sunset actif
  "sunsetBrightness": 0,             // Luminosité sunset
  "colorLightBrightness": 0,         // Luminosité couleur
  "colorLightColor": 2,              // Couleur (1-7)
  "opStatus": 0,                     // Statut opérationnel
  "timeSelected": false,             // Démarrage programmé actif
  "bathingTimeSelected": false,      // Durée bain définie
  "selectedBathingTimeHours": 0,     // Heures durée bain
  "selectedBathingTimeMinutes": 0,   // Minutes durée bain
  "supportedProtocolVersion": 1.06,  // Version protocole
  "Success": true,                   // Requête réussie
  "LoginRequired": false,            // Login requis
  "ErrorMessageHeader": "Erreur",    // Titre erreur
  "ErrorMessage": ""                 // Message erreur
}
```

**Notes importantes :**
- `selectedMode` indique le mode actuellement actif (1=Sauna, 2=SANARIUM, 3=IR)
- Les champs `saunaSelected`, `sanariumSelected`, `irSelected` sont des booléens indiquant le mode actif
- Chaque mode a sa propre température préférée mémorisée dans le sauna
- Si `selectedIrTemperature` < 30°C, le mode IR n'est probablement pas supporté par le sauna
- Si `selectedSanariumTemperature` < 40°C, le mode SANARIUM n'est probablement pas supporté

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
  "selected_mode": 1  // 1=Sauna, 2=Sanarium, 3=IR
}

Response: JSON { "Success": true/false, ... }
```

**Note importante:** Le paramètre doit être `selected_mode` et non `mode`.

**Notes sur les valeurs de température :**
- `currentTemperature` : Température actuelle mesurée
  - ⚠️ Quand le sauna est éteint, l'API retourne 141°C (valeur sentinelle invalide)
  - Filtrer les valeurs > 120°C pour éviter d'afficher des températures aberrantes
  - Températures valides : 10-100°C pour Sauna, 40-75°C pour SANARIUM, 30-100°C pour IR

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
  "time_set": true,  // true pour activer, false pour désactiver
  "hours": 18,       // Heure (0-23)
  "minutes": 30      // Minutes (0-59)
}

Response: JSON { "Success": true/false, ... }
```

**Note importante:** Les paramètres sont `time_set`, `hours`, `minutes` (pas `hour`, `minute`).

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
