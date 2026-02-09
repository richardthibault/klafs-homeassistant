# Changelog

**Leer en otros idiomas:** [English](CHANGELOG.md) | [Français](CHANGELOG.fr.md) | [Deutsch](CHANGELOG.de.md) | **Español**

Todos los cambios notables de este proyecto se documentarán en este archivo.

El formato se basa en [Keep a Changelog](https://keepachangelog.com/es-ES/1.0.0/),
y este proyecto se adhiere a [Semantic Versioning](https://semver.org/lang/es/).

**Para funciones futuras planificadas, consulte [FUTURELOG.es.md](FUTURELOG.es.md)**

---

## [1.3.0] - 2026-02-09

### Corregido
- **Control de temperatura**: Corregido parámetro API para cambios de temperatura
  - Cambio de parámetro `temp` a `temperature`
  - Valor de temperatura ahora enviado como string en lugar de integer
  - Los ajustes de temperatura ahora funcionan correctamente para todos los modos (Sauna/SANARIUM/Infrarrojo)

---

## [1.2.1] - 2026-02-09

### Añadido
- **Entidad time nativa para hora programada**: Nueva entidad `time.klafs_sauna_scheduled_start_time`
  - Hermoso selector de hora con ruedas de desplazamiento en la interfaz de Home Assistant
  - Directamente modificable desde cualquier panel
  - Se sincroniza automáticamente con el hardware de la sauna
  - 100% plug & play - no requiere configuración manual
- **Documentación simplificada**: EXAMPLES.md actualizado con enfoque simple de tarjeta "Entidades"
  - Eliminados requisitos complejos de tarjeta Lovelace personalizada
  - Todos los controles accesibles mediante tarjetas estándar de Home Assistant

### Cambiado
- **Mejoras en documentación**: Instrucciones más claras para agregar tarjetas de control a los paneles
  - Guía paso a paso para agregar tarjeta de Entidades
  - Eliminados pasos confusos de instalación de tarjeta personalizada

---

## [1.2.0] - 2026-02-09

### Añadido
- **Detección inteligente de modos**: Detecta automáticamente los modos de sauna disponibles según las capacidades del hardware
  - Modo Infrarrojo oculto si no es compatible con su sauna
  - Modo SANARIUM oculto si no es compatible con su sauna
- **Visualización hora programada**: Muestra la hora de inicio programada en los atributos de la entidad
  - `scheduled_start_time`: Muestra la hora en formato HH:MM
  - `scheduled_start_enabled`: Booleano que indica si la programación está activa

### Corregido
- **Visualización temperatura**: Filtra lecturas de temperatura inválidas cuando la sauna está apagada
  - La API devuelve 141°C cuando la sauna está apagada (valor centinela)
  - Ahora muestra "no disponible" en lugar de temperatura incorrecta
  - Añadido atributo `temperature_info` explicando por qué la temperatura no está disponible
- **API modo preset**: Corregido nombre de parámetro de `mode` a `selected_mode`
  - Corrige errores HTTP 500 al cambiar de modo
  - El cambio de modo ahora funciona correctamente
- **API hora de inicio**: Corregidos parámetros para el endpoint SetSelectedTime
  - Cambiado de `hour`/`minute` a `hours`/`minutes`/`time_set`
  - Coincide con los requisitos reales de la API Klafs

### Técnico
- Documentación API mejorada con descripciones completas de campos
- Añadida validación de temperatura (filtra valores > 120°C)
- Detección de modos basada en valores `selectedIrTemperature` y `selectedSanariumTemperature`

---

## [1.1.2] - 2026-02-09

### Corregido
- **Cambio de modo preset**: Corregido nombre de parámetro API de `mode` a `selected_mode`
- Los cambios de modo preset ahora funcionan correctamente a través de la interfaz de Home Assistant
- No más errores HTTP 500 al cambiar de modo

### Técnico
- Cambiado payload `/SaunaApp/SetMode` de `{"mode": X}` a `{"selected_mode": X}`
- Coincide con el formato exacto usado por la aplicación web Klafs

---

## [1.1.1] - 2026-02-09

### Corregido
- **Registro de depuración**: Añadido registro detallado para diagnosticar errores de API de modos preset
- Archivo de registro de depuración creado en `/config/klafs_debug.log` para solución de problemas
- Mensajes de error mejorados para llamadas API

### Técnico
- Añadida función `_write_debug_log()` para escribir información detallada de llamadas API
- Los registros incluyen: endpoint, payload, estado de respuesta y cuerpo de respuesta
- Ayuda a diagnosticar errores HTTP 500 al cambiar de modo

---

## [1.1.0] - 2026-02-09

### Añadido
- **Modos Preset**: La entidad climate ahora soporta selección de modo directamente en la interfaz
  - Modo Sauna (10-100°C)
  - Modo SANARIUM (40-75°C + control de humedad)
  - Modo Infrarrojo (30-100°C)
- Selección de modo integrada en interfaz climate (no necesita interruptor separado)
- Límites de temperatura automáticos según el modo seleccionado
- Cada modo recuerda su temperatura preferida (almacenada en sauna)

### Cambiado
- La entidad climate ahora usa modos preset en lugar de requerir un interruptor SANARIUM separado
- Los límites de temperatura se ajustan automáticamente al cambiar de modo
- Mejor experiencia de usuario con interfaz unificada

### Técnico
- Añadido soporte `ClimateEntityFeature.PRESET_MODE`
- Añadido método `async_set_preset_mode()`
- Modos preset: "Sauna", "SANARIUM", "Infrared"
- El interruptor SANARIUM permanece disponible para compatibilidad hacia atrás
- Traducciones añadidas para modos preset (EN/FR)

---

## [1.0.24] - 2026-02-09

### Cambiado
- **Visualización de iconos ampliada**: ViewBox ajustado para hacer los iconos más grandes
- Los iconos ahora coinciden con el tamaño de otros iconos de Home Assistant
- Mejor visibilidad en tarjetas de entidades y paneles

---

## [1.0.23] - 2026-02-09

### Cambiado
- **Diseño de iconos optimizado**: Banco eliminado para agrandar calentador y piedras
- Iconos ahora más visibles y claros
- Calentador y piedras centrados y agrandados para mejor visibilidad

---

## [1.0.22] - 2026-02-09

### Corregido
- **Paths SVG puros**: Convertidos todos los elementos SVG a comandos path para compatibilidad
- Los iconos ahora se muestran correctamente con API `window.customIconsets` (funcionamiento probado en v1.0.19)
- Todos los elementos visuales preservados: barras radiador, piedras calientes, banco, termómetro, ondas de calor, checkmark

### Detalles técnicos
- Todos los elementos `<rect>`, `<circle>`, `<line>` convertidos a comandos `<path>` puros
- Renderizado monocromo (`currentColor` único - sin soporte multi-color)
- Usa APIs `window.customIconsets` + `window.customIcons`
- El termómetro muestra diferentes niveles: 50% (predeterminado), 75% (calentando), 100% (listo), 0% (apagado)

### Compromisos
- Barras del radiador mismo color que el resto (sin distinción gris)
- Sin variaciones de opacidad (todo sólido)
- Más simple que v1.0.20-21 pero funcional

---

## [1.0.21] - 2026-02-09

### Corregido
- **API oficial de HA**: Cambio a `ha-iconset-svg` Web Components (método oficial de Home Assistant)
- Los iconos ahora se renderizan correctamente con todos los elementos visuales (radiador, termómetro, ondas de calor)
- Corrige error de parsing de path SVG de v1.0.20

### Detalles técnicos
- Usa Web Component `<ha-iconset-svg>` con definiciones SVG inline
- Acepta markup SVG completo (`<rect>`, `<circle>`, `<line>`, `<path>`)
- Preserva todos los atributos: colores, strokes, opacidad
- No se necesitan archivos externos (compatible con HACS)
- API oficial de HA para iconos personalizados desde 2020

---

## [1.0.20] - 2026-02-09

### Corregido
- **Renderizado completo de iconos**: Restaurados iconos SVG completos con radiador, termómetro y ondas de calor
- Los iconos ahora incluyen todos los detalles visuales: barras del calentador eléctrico (gris), piedras calientes, banco, termómetro con niveles de llenado
- `sauna-heating` muestra ondas de calor animadas sobre las piedras
- `sauna-ready` muestra indicador de checkmark
- `sauna-off` usa opacidad reducida para estado inactivo

### Detalles técnicos
- SVG completo embebido en iconset.js (enfoque inline)
- Parse SVG para extraer innerHTML y viewBox para API de iconos HA
- Preserva colores (`currentColor`, `#888`), strokes y atributos de opacidad
- No se necesitan archivos SVG externos (compatible con HACS)

---

## [1.0.19] - 2026-02-09

### Corregido
- **Compatibilidad dual de API**: Añadido soporte para ambas APIs `customIconsets` y `customIcons`
- Funciones de iconos síncronas para mejor compatibilidad entre versiones de HA
- Los iconos ahora funcionan con sistemas de iconos de Home Assistant antiguos y modernos

### Detalles técnicos
- Registrado con `window.customIconsets["klafs"]` (API heredada)
- Registrado con `window.customIcons["klafs"]` (API alternativa)
- Ambos devuelven objetos `{path, viewBox}` de forma síncrona
- Máxima compatibilidad con versiones HA 2020-2024+

---

## [1.0.18] - 2026-02-09

### Corregido
- **API HA moderna**: Uso de `async_register_static_paths` con `StaticPathConfig` (método oficial HA 2024+)
- Corregido `register_static_path` obsoleto que causaba AttributeError en versiones recientes de Home Assistant
- Función ahora correctamente async con llamada `await` en setup

### Detalles técnicos
- Importación de `StaticPathConfig` desde `homeassistant.components.http`
- Importación de `add_extra_js_url` desde `homeassistant.components.frontend`
- Uso de `await hass.http.async_register_static_paths([StaticPathConfig(...)])`
- Los iconos ahora deberían cargarse correctamente en `/klafs/iconset.js`

---

## [1.0.7] - 2026-02-09

### Corregido
- **Método de carga de iconos**: Reemplazado `add_extra_js_url()` obsoleto por registro manual de recurso Lovelace
- **Registro de ruta estática**: Corregido registro incorrecto de ruta de archivo para iconset.js
- **Registro de iconos**: Mejorada compatibilidad con sistema de iconos Home Assistant 2023+

### Cambiado
- Los iconos personalizados ahora requieren agregar recurso Lovelace manualmente (ver CUSTOM_ICONS.es.md)
- Actualizado iconset.js con múltiples métodos de registro para mejor compatibilidad
- Mejorado registro de logs para depuración de registro de iconos

### Documentación
- Añadida guía completa de solución de problemas en los 4 idiomas (EN/FR/DE/ES)
- Instrucciones paso a paso para agregar recurso Lovelace
- Consejos de depuración en consola del navegador

---

## [1.0.6] - 2026-02-09

### Corregido
- **Compatibilidad HACS**: SVG movidos a la raíz de la integración para despliegue HACS correcto
- HACS no copiaba el subdirectorio `frontend/icons/`, causando que faltaran los iconos después de la instalación

---

## [1.0.5] - 2026-02-09

### Corregido
- **Timing de registro de iconos**: Los iconos ahora se registran después de cargar las plataformas, asegurando una inicialización correcta
- Esto corrige el problema donde los iconos personalizados no aparecían en el frontend

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
