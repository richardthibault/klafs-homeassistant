**In anderen Sprachen lesen:** [English](../en/TROUBLESHOOTING.md) | [Français](../../TROUBLESHOOTING.md) | [Deutsch](../de/TROUBLESHOOTING.md) | [Español](../es/TROUBLESHOOTING.md)

# Fehlerbehebung - Klafs Sauna

## Zusammenfassung

Dieser Leitfaden hilft bei der Lösung häufiger Probleme mit der Klafs Sauna Integration:

### Häufige Probleme

- **Authentifizierungsfehler**: Ungültige Anmeldedaten, gesperrtes Konto, abgelaufene Sitzung
- **Erkennungsprobleme**: Keine Sauna gefunden, Sauna als "Disconnected" angezeigt
- **Steuerungsprobleme**: Sauna lässt sich nicht einschalten, Temperaturänderungen funktionieren nicht, SANARIUM-Modus funktioniert nicht
- **Leistungsprobleme**: Langsame Updates, Timeout-Fehler
- **Installationsprobleme**: Integration erscheint nicht, Versionsfehler

### Schnelle Lösungen

#### Sauna lässt sich nicht einschalten
1. PIN-Code in der Integration konfigurieren
2. Tür öffnen und schließen (Türkontrolle erforderlich)
3. Dienst mit PIN verwenden:
   ```yaml
   service: klafs.power_on_with_pin
   target:
     entity_id: climate.klafs_sauna
   data:
     pin: "1234"
   ```

#### Keine Sauna gefunden
1. Klafs App überprüfen - Sauna muss dort sichtbar sein
2. Wi-Fi-Modul der Sauna neu starten
3. Integration neu laden: `Konfiguration > Integrationen > Klafs > Neu laden`

#### Langsame Updates
- Normal: Integration fragt alle 60 Sekunden ab
- Klafs API hat Verzögerung bei der Übertragung
- Änderungen können 1-2 Minuten dauern

## Vollständige Dokumentation

Für detaillierte Fehlerbehebungsschritte, erweiterte Debugging-Techniken und bekannte Probleme, siehe die [englische Version](../en/TROUBLESHOOTING.md).

## Debugging aktivieren

Fügen Sie zu `configuration.yaml` hinzu:

```yaml
logger:
  default: info
  logs:
    custom_components.klafs: debug
    custom_components.klafs.api: debug
```

## Hilfe erhalten

### Benötigte Informationen

Wenn Sie um Hilfe bitten, geben Sie an:
1. Home Assistant Version
2. Integrations-Version
3. Relevante Logs (ohne Passwörter)
4. Beobachtetes vs. erwartetes Verhalten

### Wo Sie Hilfe finden

- [GitHub Issues](https://github.com/your-username/klafs-homeassistant/issues)
- [Home Assistant Forum](https://community.home-assistant.io)
- [Home Assistant Discord](https://discord.gg/home-assistant) - #custom-components

## Weitere Ressourcen

- [Vollständige Fehlerbehebung (EN)](../en/TROUBLESHOOTING.md) - Alle Lösungen und Details
- [Nutzungsbeispiele (DE)](EXAMPLES.md) - Konfigurationsbeispiele
- [Hauptdokumentation](../../README.md) - Installation und Konfiguration
- [API-Dokumentation](../../API_DOCUMENTATION.md) - Technische Details
