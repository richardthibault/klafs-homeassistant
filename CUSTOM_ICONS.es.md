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

**Paso 1: Verificar archivos desplegados**
- Verificar que los archivos SVG existan en `custom_components/klafs/`
- Verificar que `frontend/iconset.js` exista

**Paso 2: Agregar recurso Lovelace (REQUERIDO)**
1. Ir a **Configuración** > **Paneles** > **Recursos** (menú ⋮ arriba a la derecha)
2. Hacer clic en **+ AGREGAR RECURSO**
3. URL: `/local/klafs/iconset.js`
4. Tipo de recurso: **Módulo JavaScript**
5. Hacer clic en **CREAR**

**Paso 3: Limpiar caché y recargar**
1. Reiniciar Home Assistant
2. Limpiar caché del navegador (Ctrl+F5 o Shift+F5)
3. Recargar la página

**Paso 4: Verificar en consola del navegador**
1. Presionar F12 para abrir Herramientas de desarrollo
2. Ir a la pestaña Consola
3. Buscar: `[Klafs Icons] Registered icon set`
4. Si no está presente, verificar errores

**Paso 5: Probar URLs de iconos**
- Probar: `http://su-ip-ha:8123/local/klafs/icons/sauna.svg`
- Debería mostrar el icono SVG

**Paso 6: Verificar iconos de entidades**
1. Ir a Herramientas de desarrollo > Estados
2. Encontrar sus entidades Klafs
3. Verificar el atributo `icon`
4. Debería mostrar `klafs:sauna-xxx`

### ¿Todavía no funciona?

**Opción A: Usar iconos MDI como respaldo**
La integración cambiará automáticamente a iconos Material Design si los iconos personalizados no se cargan.

**Opción B: Forzar icono manualmente**
```yaml
type: entities
entities:
  - entity: climate.klafs_sauna
    icon: mdi:sauna
```

### ¿Necesita más ayuda?

- Verificar logs de Home Assistant para errores "Klafs"
- Documentación completa (EN): `_dev/ICONS_INSTALLATION_GUIDE.md`
- Reportar problemas en GitHub

---

## Compatibilidad

- Home Assistant ≥ 2023.x
- Compatible con HACS
- Funciona en escritorio y móvil
- Se adapta a temas claro/oscuro

---

**Versión:** 1.0.0  
**Fecha:** 2026-02-09
