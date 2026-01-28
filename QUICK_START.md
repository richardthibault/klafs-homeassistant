# Quick Start - Démarrage Rapide

## 🚀 Installation en 3 étapes

### Étape 1 : Installer via HACS (Recommandé)

1. Ouvrez **HACS** dans Home Assistant
2. Allez dans **Intégrations**
3. Cliquez sur les **trois points** en haut à droite
4. Sélectionnez **Dépôts personnalisés**
5. Ajoutez l'URL : `https://github.com/richardthibault/klafs-homeassistant`
6. Catégorie : **Integration**
7. Recherchez **"Klafs Sauna"**
8. Cliquez sur **Télécharger**

### Étape 2 : Redémarrer Home Assistant

- Via l'UI : **Configuration** > **Système** > **Redémarrer**
- Via CLI : `ha core restart`

### Étape 3 : Configurer l'intégration

1. Aller dans **Configuration** > **Intégrations**
2. Cliquer sur **+ Ajouter une intégration**
3. Rechercher **"Klafs Sauna"**
4. Suivre les 3 étapes :
   - **Étape 1** : Entrer vos identifiants Klafs Sauna App
   - **Étape 2** : Sélectionner vos saunas
   - **Étape 3** : Entrer les codes PIN (optionnel)

## ✅ Vérification

### 1. Vérifier que l'intégration est chargée
- Aller dans **Configuration** > **Intégrations**
- "Klafs Sauna" doit apparaître dans la liste

### 2. Vérifier les logs
- **Configuration** > **Système** > **Journaux**
- Rechercher "klafs" pour voir les messages de l'intégration

### 3. Vérifier les entités créées
- Aller dans **Configuration** > **Entités**
- Filtrer par "klafs"
- Vous devriez voir les entités de votre/vos sauna(s)

## 🐛 Problèmes Courants

### L'intégration n'apparaît pas dans HACS

**Solution :**
1. Vérifier que vous avez bien ajouté le dépôt personnalisé
2. Rafraîchir HACS (Menu > Recharger les données)
3. Redémarrer Home Assistant

### Erreur "Invalid credentials"

**Solution :**
1. Vérifier vos identifiants sur https://sauna-app.klafs.com
2. Attention : 3 tentatives échouées = compte bloqué
3. Attendre 30 minutes ou contacter Klafs

### Aucun sauna détecté

**Solution :**
1. Vérifier que votre sauna est configuré dans l'app Klafs
2. Vérifier que le module Wi-Fi est connecté
3. Tester depuis l'application mobile Klafs

## 📚 Documentation complète

- [README.md](README.md) - Documentation principale
- [INSTALLATION.md](INSTALLATION.md) - Guide d'installation détaillé
- [TESTING.md](TESTING.md) - Guide de test complet
- [TROUBLESHOOTING.md](TROUBLESHOOTING.md) - Dépannage

## 💡 Aide

- **GitHub Issues** : [Créer une issue](https://github.com/richardthibault/klafs-homeassistant/issues)
- **Forum HA** : https://community.home-assistant.io
- **Discord HA** : Canal #custom-components

## 🎉 C'est tout !

Votre intégration Klafs est maintenant installée et prête à l'emploi !
