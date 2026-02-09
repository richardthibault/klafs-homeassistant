# Changelog

**Leer en otros idiomas:** [English](CHANGELOG.md) | [Français](CHANGELOG.fr.md) | [Deutsch](CHANGELOG.de.md) | **Español**

Todos los cambios notables de este proyecto se documentarán en este archivo.

**Para características futuras planificadas, consulte [FUTURELOG.es.md](FUTURELOG.es.md)**

Para el historial completo de versiones, consulte la [versión en inglés](CHANGELOG.md).

---

## [1.0.2] - 2026-02-09

### Añadido
- **Iconos SVG personalizados** con soporte de color dinámico
  - 4 iconos específicos por estado: predeterminado, apagado, calentando, listo
  - Los iconos se adaptan al tema de Home Assistant (claro/oscuro)
  - Diseño de radiador con barras visibles y piedras calientes
  - Termómetro indica nivel de temperatura (0%, 25%, 50%, 100%)
- **Iconos PNG de marca** para HACS y Home Assistant (256x256, 512x512)

### Cambiado
- Los iconos de sensores ahora usan iconos personalizados `klafs:sauna-*`

---

## [1.0.1] - 2026-02-09

### Corregido
- **Error crítico de reconexión**: El sauna ya no se detectaba después de una pérdida de conexión WiFi
  - El coordinador ahora mantiene los saunas en los datos incluso cuando están desconectados
  - Manejo de errores mejorado por sauna individual
  - Las entidades permanecen disponibles y se reconectan automáticamente
  - Ya no es necesario desinstalar/reinstalar la integración después de una pérdida de conexión

---

## [1.0.0] - 2026-01-28

### Añadido
- Integración inicial con API de Klafs
- **Soporte multi-sauna**: Gestione múltiples saunas desde una sola cuenta
- **Código PIN individual por sauna**: Cada sauna puede tener su propio PIN
- **Flujo de configuración en 3 pasos**: Credenciales → Selección de saunas → Configuración de PIN
- Entidad Climate (termostato) para controlar cada sauna
- Sensores de temperatura, humedad y estado por sauna
- Interruptor para cambiar entre modos Sauna y SANARIUM
- Servicios: `power_on_with_pin`, `set_humidity_level`, `set_start_time`
- Soporte para modos: Sauna clásico, SANARIUM, Infrarrojo
- Polling automático cada 60 segundos
- Traducciones en francés e inglés
- Documentación completa
- Soporte HACS

### Características
- Control de temperatura (10-100°C según el modo)
- Encendido/apagado remoto
- Monitoreo en tiempo real de temperatura y humedad
- Estado de conexión del sauna
- Indicación "Listo" cuando el sauna está listo

### Seguridad
- Almacenamiento seguro de credenciales
- Soporte obligatorio de código PIN para encender
- Solo comunicación HTTPS

---

## Notas de Versión Completas

Para notas de versión detalladas, guías de migración y listas completas de cambios, consulte la [versión en inglés](CHANGELOG.md).

---

**Leyenda:**
- `Añadido`: Nuevas características
- `Cambiado`: Cambios en características existentes
- `Obsoleto`: Características que se eliminarán pronto
- `Eliminado`: Características eliminadas
- `Corregido`: Correcciones de errores
- `Seguridad`: Correcciones de vulnerabilidades de seguridad
