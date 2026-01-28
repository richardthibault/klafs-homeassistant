# Guide d'installation - Intégration Klafs Sauna

## Méthode 1 : Installation manuelle

### Étape 1 : Copier les fichiers

1. Téléchargez ou clonez ce dépôt
2. Copiez le dossier `custom_components/klafs` dans votre dossier de configuration Home Assistant :
   ```
   <config>/custom_components/klafs/
   ```

### Étape 2 : Redémarrer Home Assistant

Redémarrez Home Assistant pour charger la nouvelle intégration.

### Étape 3 : Ajouter l'intégration

1. Allez dans **Configuration** > **Intégrations**
2. Cliquez sur **+ Ajouter une intégration**
3. Recherchez **"Klafs Sauna"**
4. Suivez les instructions à l'écran

## Méthode 2 : Installation via HACS (recommandé)

### Prérequis

- HACS doit être installé dans votre Home Assistant
- Si ce n'est pas le cas, suivez le [guide d'installation HACS](https://hacs.xyz/docs/setup/download)

### Étape 1 : Ajouter le dépôt personnalisé

1. Ouvrez **HACS** dans Home Assistant
2. Cliquez sur **Intégrations**
3. Cliquez sur les **trois points** en haut à droite
4. Sélectionnez **Dépôts personnalisés**
5. Ajoutez l'URL : `https://github.com/richardthibault/klafs-homeassistant`
6. Sélectionnez la catégorie : **Intégration**
7. Cliquez sur **Ajouter**

### Étape 2 : Installer l'intégration

1. Recherchez **"Klafs Sauna"** dans HACS
2. Cliquez sur **Télécharger**
3. Redémarrez Home Assistant

### Étape 3 : Configurer l'intégration

1. Allez dans **Configuration** > **Intégrations**
2. Cliquez sur **+ Ajouter une intégration**
3. Recherchez **"Klafs Sauna"**
4. **Étape 1** : Entrez vos identifiants
   - **Nom d'utilisateur** : Votre email Klafs
   - **Mot de passe** : Votre mot de passe Klafs
5. **Étape 2** : Sélectionnez les saunas
   - Cochez les saunas que vous souhaitez contrôler
   - Vous pouvez en sélectionner un ou plusieurs
6. **Étape 3** : Configurez les codes PIN (optionnel)
   - Entrez le code PIN pour chaque sauna sélectionné
   - Laissez vide si vous ne souhaitez pas allumer le sauna à distance

## Configuration

### Identifiants requis

Vous aurez besoin de vos identifiants de l'application **Klafs Sauna App** :

- Email/nom d'utilisateur
- Mot de passe

⚠️ **Attention** : Klafs bloque automatiquement votre compte après 3 tentatives de connexion échouées. Assurez-vous d'entrer les bons identifiants dès la première fois.

### Vérification de la configuration

Après l'ajout de l'intégration, vous devriez voir :

1. Une nouvelle intégration **Klafs Sauna** dans vos intégrations
2. Un ou plusieurs appareils correspondant à vos saunas
3. Des entités pour chaque sauna :
   - `climate.klafs_sauna_XXXXXXXX` (thermostat)
   - `sensor.klafs_sauna_XXXXXXXX_temperature`
   - `sensor.klafs_sauna_XXXXXXXX_humidity`
   - `sensor.klafs_sauna_XXXXXXXX_status`
   - `switch.klafs_sauna_XXXXXXXX_sanarium_mode`

## Dépannage

### L'intégration n'apparaît pas

1. Vérifiez que les fichiers sont bien dans `<config>/custom_components/klafs/`
2. Vérifiez les logs : **Configuration** > **Logs**
3. Redémarrez Home Assistant en mode sans échec pour vérifier les erreurs

### Erreur "Invalid credentials"

1. Vérifiez vos identifiants dans l'application Klafs Sauna App
2. Assurez-vous que votre compte n'est pas bloqué
3. Essayez de vous connecter sur https://sauna-app.klafs.com

### Le sauna n'est pas détecté

1. Vérifiez que votre sauna est bien configuré dans l'application Klafs
2. Assurez-vous que le module Wi-Fi est connecté et fonctionnel
3. Supprimez et réajoutez l'intégration

### Les commandes ne fonctionnent pas

1. Vérifiez que le capteur de statut indique "Connected"
2. Assurez-vous d'avoir configuré un code PIN sur votre sauna
3. Vérifiez que la porte du sauna a été contrôlée (sécurité)

## Mise à jour

### Via HACS

1. Ouvrez HACS
2. Allez dans **Intégrations**
3. Recherchez **Klafs Sauna**
4. Cliquez sur **Mettre à jour** si disponible
5. Redémarrez Home Assistant

### Manuellement

1. Téléchargez la dernière version
2. Remplacez le dossier `custom_components/klafs/`
3. Redémarrez Home Assistant

## Support

Pour obtenir de l'aide :

1. Consultez le [README.md](README.md) pour la documentation complète
2. Vérifiez les [issues GitHub](https://github.com/richardthibault/klafs-homeassistant/issues)
3. Créez une nouvelle issue si nécessaire

## Prochaines étapes

Une fois l'installation terminée, consultez le [README.md](README.md) pour :

- Des exemples d'automatisations
- Des cartes Lovelace
- Des cas d'usage avancés
