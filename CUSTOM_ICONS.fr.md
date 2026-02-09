**Lire dans d'autres langues :** [English](CUSTOM_ICONS.md) | [Français](CUSTOM_ICONS.fr.md) | [Deutsch](CUSTOM_ICONS.de.md) | [Español](CUSTOM_ICONS.es.md)

---

# 🎨 Icônes Personnalisées

## Présentation

L'intégration Klafs utilise maintenant des **icônes personnalisées** qui changent automatiquement selon l'état du sauna.

---

## Icônes Disponibles

| Icône | État | Description |
|-------|------|-------------|
| 🔥 `klafs:sauna-heating` | Chauffe | Le sauna est en train de chauffer |
| ✅ `klafs:sauna-ready` | Prêt | Le sauna a atteint la température cible |
| ⚫ `klafs:sauna-off` | Éteint | Le sauna est éteint |
| 🏠 `klafs:sauna` | Défaut | État neutre |

Les icônes s'adaptent automatiquement au thème clair/foncé de Home Assistant.

---

## Installation

### Via HACS (Recommandé)

1. Mettre à jour l'intégration Klafs via HACS
2. Redémarrer Home Assistant
3. Vider le cache navigateur (Ctrl+F5)
4. Les icônes apparaissent automatiquement

### Installation Manuelle

1. Copier le dossier `custom_components/klafs/` vers Home Assistant
2. Redémarrer Home Assistant
3. Vider le cache navigateur (Ctrl+F5)

---

## Utilisation

### Automatique (Recommandé)

Les icônes sont appliquées automatiquement à toutes les entités Klafs :

```yaml
type: entities
entities:
  - entity: climate.klafs_sauna
  - entity: sensor.klafs_sauna_status
```

### Manuel (Override)

Vous pouvez forcer une icône spécifique :

```yaml
type: entities
entities:
  - entity: climate.klafs_sauna
    icon: klafs:sauna-ready
```

---

## Dépannage

### Les icônes ne s'affichent pas ?

**Étape 1 : Vérifier les fichiers déployés**
- Vérifier que les fichiers SVG existent dans `custom_components/klafs/`
- Vérifier que `frontend/iconset.js` existe

**Étape 2 : Ajouter la ressource Lovelace (REQUIS)**
1. Aller dans **Paramètres** > **Tableaux de bord** > **Ressources** (menu ⋮ en haut à droite)
2. Cliquer sur **+ AJOUTER UNE RESSOURCE**
3. URL : `/local/klafs/iconset.js`
4. Type de ressource : **Module JavaScript**
5. Cliquer sur **CRÉER**

**Étape 3 : Vider le cache et recharger**
1. Redémarrer Home Assistant
2. Vider le cache navigateur (Ctrl+F5 ou Shift+F5)
3. Recharger la page

**Étape 4 : Vérifier dans la console navigateur**
1. Appuyer sur F12 pour ouvrir les Outils de développement
2. Aller dans l'onglet Console
3. Chercher : `[Klafs Icons] Registered icon set`
4. Si absent, vérifier les erreurs

**Étape 5 : Tester les URLs des icônes**
- Tester : `http://votre-ip-ha:8123/local/klafs/icons/sauna.svg`
- Devrait afficher l'icône SVG

**Étape 6 : Vérifier les icônes des entités**
1. Aller dans Outils de développement > États
2. Trouver vos entités Klafs
3. Vérifier l'attribut `icon`
4. Devrait afficher `klafs:sauna-xxx`

### Toujours pas fonctionnel ?

**Option A : Utiliser les icônes MDI de secours**
L'intégration basculera automatiquement vers les icônes Material Design si les icônes personnalisées ne se chargent pas.

**Option B : Forcer l'icône manuellement**
```yaml
type: entities
entities:
  - entity: climate.klafs_sauna
    icon: mdi:sauna
```

### Besoin d'aide ?

- Vérifier les logs Home Assistant pour les erreurs "Klafs"
- Consulter la documentation complète dans `_dev/ICONS_INSTALLATION_GUIDE.md`
- Signaler les problèmes sur GitHub

---

## Compatibilité

- Home Assistant ≥ 2023.x
- Compatible HACS
- Fonctionne sur desktop et mobile
- S'adapte aux thèmes clair/foncé

---

**Version :** 1.0.0  
**Date :** 2026-02-09
