**Leer en otros idiomas:** [English](../en/EXAMPLES.md) | [Français](../../EXAMPLES.md) | [Deutsch](../de/EXAMPLES.md) | [Español](../es/EXAMPLES.md)

# Ejemplos de Uso - Klafs Sauna

## Resumen

Este documento contiene ejemplos completos para usar la integración Klafs Sauna en Home Assistant, incluyendo:

- **Servicios disponibles**: Encender con PIN, ajustar humedad, programar hora de inicio
- **Automatizaciones avanzadas**: Rutina matinal de fin de semana, precalentamiento inteligente basado en ubicación, apagado automático
- **Automatizaciones de seguridad**: Alertas cuando nadie está en casa
- **Programas semanales**: Diferentes modos para diferentes días de la semana
- **Tarjetas Lovelace**: Configuraciones de UI simples y avanzadas
- **Scripts útiles**: Modo SANARIUM, Sauna finlandés, parada de emergencia
- **Integración con asistentes de voz**: Escenas para Google Assistant y Alexa

## Documentación Completa

Para ejemplos detallados con código completo, consulte la [versión en inglés](../en/EXAMPLES.md).

## Ejemplos de Inicio Rápido

### Encender sauna con PIN

```yaml
service: klafs.power_on_with_pin
target:
  entity_id: climate.klafs_sauna
data:
  pin: "1234"
```

### Activar modo SANARIUM

```yaml
service: switch.turn_on
target:
  entity_id: switch.klafs_sauna_sanarium_mode
```

### Ajustar nivel de humedad

```yaml
service: klafs.set_humidity_level
target:
  entity_id: climate.klafs_sauna
data:
  humidity_level: 7  # 1-10
```

### Tarjeta de termostato simple

```yaml
type: thermostat
entity: climate.klafs_sauna
```

## Más Información

- [Ejemplos completos (EN)](../en/EXAMPLES.md) - Todas las automatizaciones y configuraciones
- [Solución de problemas (ES)](TROUBLESHOOTING.md) - Resolver problemas
- [Documentación principal](../../README.md) - Guía de instalación y configuración
