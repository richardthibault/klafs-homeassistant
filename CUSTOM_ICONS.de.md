**In anderen Sprachen lesen:** [English](CUSTOM_ICONS.md) | [Français](CUSTOM_ICONS.fr.md) | [Deutsch](CUSTOM_ICONS.de.md) | [Español](CUSTOM_ICONS.es.md)

---

# 🎨 Benutzerdefinierte Symbole

## Übersicht

Die Klafs-Integration verwendet jetzt **benutzerdefinierte Symbole**, die sich automatisch je nach Saunastatus ändern.

---

## Verfügbare Symbole

| Symbol | Status | Beschreibung |
|--------|--------|--------------|
| 🔥 `klafs:sauna-heating` | Aufheizen | Sauna heizt auf |
| ✅ `klafs:sauna-ready` | Bereit | Sauna hat Zieltemperatur erreicht |
| ⚫ `klafs:sauna-off` | Aus | Sauna ist ausgeschaltet |
| 🏠 `klafs:sauna` | Standard | Neutraler Zustand |

Die Symbole passen sich automatisch an das helle/dunkle Theme von Home Assistant an.

---

## Installation

### Über HACS (Empfohlen)

1. Klafs-Integration über HACS aktualisieren
2. Home Assistant neu starten
3. Browser-Cache leeren (Strg+F5)
4. Symbole erscheinen automatisch

### Manuelle Installation

1. Ordner `custom_components/klafs/` nach Home Assistant kopieren
2. Home Assistant neu starten
3. Browser-Cache leeren (Strg+F5)

---

## Verwendung

### Automatisch (Empfohlen)

Symbole werden automatisch auf alle Klafs-Entitäten angewendet:

```yaml
type: entities
entities:
  - entity: climate.klafs_sauna
  - entity: sensor.klafs_sauna_status
```

### Manuell

Sie können ein bestimmtes Symbol erzwingen:

```yaml
type: entities
entities:
  - entity: climate.klafs_sauna
    icon: klafs:sauna-ready
```

---

## Fehlerbehebung

### Symbole werden nicht angezeigt?

1. Home Assistant neu starten
2. Browser-Cache leeren (Strg+F5)
3. Browser-Konsole (F12) auf Fehler prüfen
4. URL testen: `http://ihr-ha.local:8123/local/klafs/icons/sauna.svg`

### Weitere Hilfe?

Vollständige Dokumentation (EN): `_dev/ICONS_INSTALLATION_GUIDE.md`

---

## Kompatibilität

- Home Assistant ≥ 2023.x
- HACS-kompatibel
- Funktioniert auf Desktop und Mobil
- Passt sich an helle/dunkle Themes an

---

**Version:** 1.0.0  
**Datum:** 2026-02-09
