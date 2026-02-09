**Leer en otros idiomas:** [English](CUSTOM_ICONS.md) | [Français](CUSTOM_ICONS.fr.md) | [Deutsch](CUSTOM_ICONS.de.md) | [Español](CUSTOM_ICONS.es.md)

---

# 🎨 Iconos Personalizados

## Descripción

La integración Klafs ahora utiliza **iconos personalizados** que cambian automáticamente según el estado de la sauna.

---

## Iconos Disponibles

| Icono | Estado | Descripción |
|-------|--------|-------------|
| 🔥 `klafs:sauna-heating` | Calentando | La sauna se está calentando |
| ✅ `klafs:sauna-ready` | Lista | La sauna ha alcanzado la temperatura objetivo |
| ⚫ `klafs:sauna-off` | Apagada | La sauna está apagada |
| 🏠 `klafs:sauna` | Predeterminado | Estado neutral |

Los iconos se adaptan automáticamente al tema claro/oscuro de Home Assistant.

---

## Instalación

### Vía HACS (Recomendado)

1. Actualizar la integración Klafs vía HACS
2. Reiniciar Home Assistant
3. Limpiar caché del navegador (Ctrl+F5)
4. Los iconos aparecerán automáticamente

### Instalación Manual

1. Copiar la carpeta `custom_components/klafs/` a Home Assistant
2. Reiniciar Home Assistant
3. Limpiar caché del navegador (Ctrl+F5)

---

## Uso

### Automático (Recomendado)

Los iconos se aplican automáticamente a todas las entidades Klafs:

```yaml
type: entities
entities:
  - entity: climate.klafs_sauna
  - entity: sensor.klafs_sauna_status
```

### Manual

Puede forzar un icono específico:

```yaml
type: entities
entities:
  - entity: climate.klafs_sauna
    icon: klafs:sauna-ready
```

---

## Solución de Problemas

### ¿Los iconos no se muestran?

1. Reiniciar Home Assistant
2. Limpiar caché del navegador (Ctrl+F5)
3. Verificar consola del navegador (F12) para errores
4. Probar URL: `http://su-ha.local:8123/local/klafs/icons/sauna.svg`

### ¿Necesita más ayuda?

Documentación completa (EN): `_dev/ICONS_INSTALLATION_GUIDE.md`

---

## Compatibilidad

- Home Assistant ≥ 2023.x
- Compatible con HACS
- Funciona en escritorio y móvil
- Se adapta a temas claro/oscuro

---

**Versión:** 1.0.0  
**Fecha:** 2026-02-09
