# Changelog

**Leer en otros idiomas:** [English](CHANGELOG.md) | [Français](CHANGELOG.fr.md) | [Deutsch](CHANGELOG.de.md) | **Español**

Todos los cambios notables de este proyecto se documentarán en este archivo.

El formato se basa en [Keep a Changelog](https://keepachangelog.com/es-ES/1.0.0/),
y este proyecto se adhiere a [Semantic Versioning](https://semver.org/lang/es/).

**Para funciones futuras planificadas, consulte [FUTURELOG.es.md](FUTURELOG.es.md)**

---

## [1.0.4] - 2026-02-09

### Añadido
- **Conjunto de Iconos Personalizados**: La integración ahora incluye iconos personalizados con prefijo `klafs:`
  - `klafs:sauna` - Estado predeterminado/neutral
  - `klafs:sauna-heating` - Sauna calentando (con ondas de calor)
  - `klafs:sauna-ready` - Sauna lista (termómetro lleno + marca de verificación)
  - `klafs:sauna-off` - Sauna apagada (elementos atenuados)
  - Los iconos cambian automáticamente según el estado de la sauna
  - Todos los iconos usan `fill="currentColor"` para compatibilidad con temas
  - Funciona con Home Assistant ≥ 2023.x
- **Documentación Multilingüe**: Documentación de iconos personalizados en 4 idiomas (EN/FR/DE/ES)
- **Mapeo Automático de Iconos**: Los iconos cambian automáticamente según el estado de la entidad
  - No se requiere configuración
  - Funciona con entidades sensor y climate

### Cambiado
- Iconos movidos de `icons/` a `frontend/icons/`
- Los iconos ahora se sirven como archivos estáticos a través de `/local/klafs/icons/`
- Añadido `icon_mapping.py` para gestión centralizada de estados de iconos

### Técnico
- Añadido `frontend/iconset.js` para registro de iconos en el frontend de Home Assistant
- Actualizado `__init__.py` para registrar rutas estáticas y cargar iconset
- Actualizado `sensor.py` y `climate.py` para usar propiedades de iconos dinámicas
- Los iconos se adaptan automáticamente a temas claros/oscuros

---

## [1.0.3] - 2026-02-09

### Corregido
- **Problema de visualización de iconos**: Iconos personalizados `klafs:sauna-*` reemplazados por iconos MDI estándar
  - Los iconos SVG personalizados se mantienen en el repositorio para uso futuro
  - Ahora se usa `mdi:sauna` (predeterminado/apagado), `mdi:fire` (calentando), `mdi:check-circle` (listo)
  - Los iconos ahora se muestran correctamente sin configuración adicional

### Técnico
- Las integraciones personalizadas de Home Assistant no pueden integrar fácilmente conjuntos de iconos personalizados sin dependencias externas
- Los iconos MDI estándar ofrecen mejor compatibilidad y funcionalidad inmediata

---

Changelog completo (EN): [CHANGELOG.md](CHANGELOG.md)
