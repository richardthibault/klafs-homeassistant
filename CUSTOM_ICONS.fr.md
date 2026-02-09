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

1. Redémarrer Home Assistant
2. Vider le cache navigateur (Ctrl+F5)
3. Vérifier la console navigateur (F12) pour erreurs
4. Tester l'URL : `http://votre-ha.local:8123/local/klafs/icons/sauna.svg`

### Besoin d'aide ?

Consultez la documentation complète dans `_dev/ICONS_INSTALLATION_GUIDE.md`

---

## Compatibilité

- Home Assistant ≥ 2023.x
- Compatible HACS
- Fonctionne sur desktop et mobile
- S'adapte aux thèmes clair/foncé

---

**Version :** 1.0.0  
**Date :** 2026-02-09
