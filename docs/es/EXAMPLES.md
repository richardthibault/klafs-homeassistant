**Leer en otros idiomas:** [English](../en/EXAMPLES.md) | [Français](../../EXAMPLES.md) | [Deutsch](../de/EXAMPLES.md) | [Español](../es/EXAMPLES.md)

# Ejemplos de Uso - Klafs Sauna

## Agregar Tarjeta de Control (Recomendado) 🎨

Para tener todos los controles de la sauna agrupados en una sola tarjeta:

**Pasos simples:**

1. Abra un panel (o cree uno nuevo)
2. Haga clic en **+ Agregar tarjeta**
3. Seleccione **"Entidades"**
4. Agregue estas entidades:
   - `climate.klafs_sauna` (Termostato principal)
   - `time.klafs_sauna_scheduled_start_time` (Hora de inicio programada)
   - `sensor.klafs_sauna_status` (Estado de la sauna)
5. Haga clic en **"Guardar"**

**La tarjeta mostrará:**
- 🌡️ Control de temperatura con deslizador
- 🔥 Selección de modos (Sauna / SANARIUM / Infrarrojo)
- ⏰ Selector de hora programada (con ruedas de desplazamiento)
- 🔘 Botones Encender/Apagar
- 📊 Estado en tiempo real

**Configuración YAML (opcional):**

Si prefiere configurar en YAML:

```yaml
type: entities
title: Control Sauna
entities:
  - entity: climate.klafs_sauna
  - entity: time.klafs_sauna_scheduled_start_time
    name: Inicio Programado
  - entity: sensor.klafs_sauna_status
    name: Estado
```

---

## Servicios Disponibles

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
