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

**Schritt 1: Dateien überprüfen**
- Prüfen Sie, ob SVG-Dateien in `custom_components/klafs/` existieren
- Prüfen Sie, ob `frontend/iconset.js` existiert

**Schritt 2: Lovelace-Ressource hinzufügen (ERFORDERLICH)**
1. Gehen Sie zu **Einstellungen** > **Dashboards** > **Ressourcen** (⋮ Menü oben rechts)
2. Klicken Sie auf **+ RESSOURCE HINZUFÜGEN**
3. URL: `/local/klafs/iconset.js`
4. Ressourcentyp: **JavaScript-Modul**
5. Klicken Sie auf **ERSTELLEN**

**Schritt 3: Cache leeren und neu laden**
1. Home Assistant neu starten
2. Browser-Cache leeren (Strg+F5 oder Umschalt+F5)
3. Seite neu laden

**Schritt 4: In Browser-Konsole überprüfen**
1. F12 drücken, um Entwicklertools zu öffnen
2. Zur Konsole-Tab gehen
3. Suchen nach: `[Klafs Icons] Registered icon set`
4. Falls nicht vorhanden, auf Fehler prüfen

**Schritt 5: Symbol-URLs testen**
- Testen: `http://ihre-ha-ip:8123/local/klafs/icons/sauna.svg`
- Sollte das SVG-Symbol anzeigen

**Schritt 6: Entitäts-Symbole prüfen**
1. Zu Entwicklertools > Zustände gehen
2. Ihre Klafs-Entitäten finden
3. Das `icon`-Attribut prüfen
4. Sollte `klafs:sauna-xxx` anzeigen

### Immer noch nicht funktionierend?

**Option A: MDI-Symbole als Fallback verwenden**
Die Integration wechselt automatisch zu Material Design Icons, wenn benutzerdefinierte Symbole nicht geladen werden können.

**Option B: Symbol manuell überschreiben**
```yaml
type: entities
entities:
  - entity: climate.klafs_sauna
    icon: mdi:sauna
```

### Weitere Hilfe?

- Home Assistant Logs auf "Klafs"-Fehler prüfen
- Vollständige Dokumentation (EN): `_dev/ICONS_INSTALLATION_GUIDE.md`
- Probleme auf GitHub melden

---

## Kompatibilität

- Home Assistant ≥ 2023.x
- HACS-kompatibel
- Funktioniert auf Desktop und Mobil
- Passt sich an helle/dunkle Themes an

---

**Version:** 1.0.0  
**Datum:** 2026-02-09
