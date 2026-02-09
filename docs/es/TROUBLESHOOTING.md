**Leer en otros idiomas:** [English](../en/TROUBLESHOOTING.md) | [Français](../../TROUBLESHOOTING.md) | [Deutsch](../de/TROUBLESHOOTING.md) | [Español](../es/TROUBLESHOOTING.md)

# Guía de Solución de Problemas - Klafs Sauna

## Resumen

Esta guía ayuda a resolver problemas comunes con la integración Klafs Sauna:

### Problemas Comunes

- **Errores de autenticación**: Credenciales inválidas, cuenta bloqueada, sesión expirada
- **Problemas de descubrimiento**: No se detecta sauna, sauna aparece como "Disconnected"
- **Problemas de control**: No se puede encender el sauna, cambios de temperatura no funcionan, modo SANARIUM no funciona
- **Problemas de rendimiento**: Actualizaciones lentas, errores de timeout
- **Problemas de instalación**: La integración no aparece, error de versión

### Soluciones Rápidas

#### No se puede encender el sauna
1. Configurar código PIN en la integración
2. Abrir y cerrar la puerta (control de puerta requerido)
3. Usar servicio con PIN:
   ```yaml
   service: klafs.power_on_with_pin
   target:
     entity_id: climate.klafs_sauna
   data:
     pin: "1234"
   ```

#### No se detecta sauna
1. Verificar en la app Klafs - el sauna debe ser visible allí
2. Reiniciar el módulo Wi-Fi del sauna
3. Recargar integración: `Configuración > Integraciones > Klafs > Recargar`

#### Actualizaciones lentas
- Normal: La integración consulta cada 60 segundos
- La API de Klafs tiene retraso de propagación
- Los cambios pueden tardar 1-2 minutos

## Documentación Completa

Para pasos detallados de solución de problemas, técnicas avanzadas de depuración y problemas conocidos, consulte la [versión en inglés](../en/TROUBLESHOOTING.md).

## Activar Depuración

Agregar a `configuration.yaml`:

```yaml
logger:
  default: info
  logs:
    custom_components.klafs: debug
    custom_components.klafs.api: debug
```

## Obtener Ayuda

### Información Necesaria

Al solicitar ayuda, incluya:
1. Versión de Home Assistant
2. Versión de la integración
3. Logs relevantes (sin contraseñas)
4. Comportamiento observado vs. esperado

### Dónde Obtener Ayuda

- [GitHub Issues](https://github.com/your-username/klafs-homeassistant/issues)
- [Foro de Home Assistant](https://community.home-assistant.io)
- [Discord de Home Assistant](https://discord.gg/home-assistant) - #custom-components

## Recursos Adicionales

- [Solución de problemas completa (EN)](../en/TROUBLESHOOTING.md) - Todas las soluciones y detalles
- [Ejemplos de uso (ES)](EXAMPLES.md) - Ejemplos de configuración
- [Documentación principal](../../README.md) - Instalación y configuración
- [Documentación API](../../API_DOCUMENTATION.md) - Detalles técnicos
