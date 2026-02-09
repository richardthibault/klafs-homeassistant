# Integración Klafs Sauna para Home Assistant

**Leer en otros idiomas:** [English](README.md) | [Français](README.fr.md) | [Deutsch](README.de.md) | **Español**

[![hacs_badge](https://img.shields.io/badge/HACS-Custom-orange.svg)](https://github.com/custom-components/hacs)
[![GitHub release](https://img.shields.io/github/release/richardthibault/klafs-homeassistant.svg)](https://github.com/richardthibault/klafs-homeassistant/releases)
[![License](https://img.shields.io/github/license/richardthibault/klafs-homeassistant.svg)](LICENSE)

Esta integración personalizada le permite controlar su sauna Klafs a través de Home Assistant utilizando la API en la nube de Klafs.

![Klafs Sauna](https://www.klafs.com/typo3conf/ext/klafs_sitepackage/Resources/Public/Images/logo.svg)

## Características

- **Control Climático**: Controle la temperatura de su sauna como un termostato
- **Sensores**: Monitoree temperatura, humedad y estado en tiempo real
- **Modos**: Cambie entre modos Sauna y SANARIUM®
- **Encendido/Apagado**: Controle la alimentación de su sauna de forma remota
- **Soporte Multi-sauna**: Gestione múltiples saunas desde una sola cuenta
- **PINs Individuales**: Cada sauna puede tener su propio código PIN

## Requisitos Previos

- Una cuenta de Klafs Sauna App
- Una sauna Klafs equipada con módulo Wi-Fi y opción "KLAFS Sauna App"
- Home Assistant 2023.1 o superior

## Instalación

### Instalación vía HACS (Recomendado)

1. Abra HACS en Home Assistant
2. Vaya a "Integraciones"
3. Haga clic en los tres puntos en la esquina superior derecha
4. Seleccione "Repositorios personalizados"
5. Añada la URL: `https://github.com/richardthibault/klafs-homeassistant`
6. Busque "Klafs Sauna" e instale
7. Reinicie Home Assistant
8. Configure la integración a través de la interfaz de usuario

### Instalación Manual

1. Copie la carpeta `custom_components/klafs` en su carpeta `config/custom_components/`
2. Reinicie Home Assistant
3. Vaya a Configuración > Integraciones
4. Haga clic en "+ Añadir integración"
5. Busque "Klafs Sauna"
6. Introduzca sus credenciales de Klafs Sauna App

## Configuración

La integración se configura completamente a través de la interfaz de usuario de Home Assistant en 3 pasos:

### Paso 1: Credenciales
- **Nombre de usuario**: Su nombre de usuario de Klafs Sauna App
- **Contraseña**: Su contraseña de Klafs Sauna App

### Paso 2: Selección de Saunas
- Seleccione las saunas que desea controlar a través de Home Assistant
- Puede seleccionar una o varias saunas
- Cada sauna aparecerá como un dispositivo separado

### Paso 3: Códigos PIN
- **Código PIN** (opcional): El código PIN de 4 dígitos configurado en cada sauna
- Se puede configurar un PIN diferente para cada sauna
- Requerido para encender la sauna de forma remota

⚠️ **Importante**: 
- Klafs bloquea la cuenta después de 3 intentos de inicio de sesión fallidos. Asegúrese de introducir las credenciales correctas.
- Cada código PIN debe configurarse en la sauna correspondiente a través de su panel de control antes de usarlo.
- Sin PIN, puede ver el estado de la sauna pero no encenderla de forma remota.
- Si tiene varias saunas, cada una puede tener su propio código PIN.

## Entidades Creadas

Para cada sauna detectada, la integración crea:

### Climate (Termostato)
- **Entidad**: `climate.klafs_sauna_XXXXXXXX`
- **Funciones**: Control de temperatura, encendido/apagado
- **Atributos**:
  - Modo actual (Sauna/SANARIUM®/Infrarrojo)
  - Estado de conexión
  - Listo para usar
  - Nivel de humedad (solo SANARIUM®)

### Sensores
- **Temperatura**: `sensor.klafs_sauna_XXXXXXXX_temperature`
- **Humedad**: `sensor.klafs_sauna_XXXXXXXX_humidity`
- **Estado**: `sensor.klafs_sauna_XXXXXXXX_status` (Apagado/Calentando/Listo/Desconectado)

### Interruptor
- **Modo SANARIUM®**: `switch.klafs_sauna_XXXXXXXX_sanarium_mode`

## Uso

### Control Básico

```yaml
# Encender sauna a 80°C (usa el PIN configurado)
service: climate.set_temperature
target:
  entity_id: climate.klafs_sauna_XXXXXXXX
data:
  temperature: 80
  hvac_mode: heat

# Encender con PIN específico
service: klafs.power_on_with_pin
target:
  entity_id: climate.klafs_sauna_XXXXXXXX
data:
  pin: "1234"

# Apagar sauna
service: climate.turn_off
target:
  entity_id: climate.klafs_sauna_XXXXXXXX

# Establecer nivel de humedad (solo SANARIUM)
service: klafs.set_humidity_level
target:
  entity_id: climate.klafs_sauna_XXXXXXXX
data:
  humidity_level: 7

# Programar hora de inicio
service: klafs.set_start_time
target:
  entity_id: climate.klafs_sauna_XXXXXXXX
data:
  hour: 18
  minute: 30
```

### Automatizaciones

Consulte [EXAMPLES.md](EXAMPLES.md) para más ejemplos de automatizaciones y tarjetas Lovelace.

## Documentación Completa

- 📖 [Guía de Inicio Rápido](QUICK_START.md)
- 🔧 [Guía de Instalación Detallada](INSTALLATION.md)
- 💡 [Ejemplos de Automatizaciones](EXAMPLES.md)
- 🔍 [Documentación API](API_DOCUMENTATION.md)
- 🐛 [Guía de Solución de Problemas](TROUBLESHOOTING.md)
- 🏗️ [Soporte Multi-sauna](MULTI_SAUNA_SUPPORT.md)
- 🤝 [Guía de Contribución](CONTRIBUTING.md)

## API de Klafs

Esta integración utiliza la API web de Klafs (aplicación ASP.NET MVC):

- **URL base**: `https://sauna-app.klafs.com`
- **Autenticación**: Basada en cookies después del inicio de sesión
- **Polling**: Actualizaciones cada 60 segundos por defecto

## Límites de Temperatura

- **Modo Sauna**: 10°C - 100°C
- **Modo SANARIUM®**: 40°C - 75°C
- **Modo Infrarrojo**: 30°C - 100°C

## Solución de Problemas

### La integración no se conecta

1. Verifique sus credenciales en la aplicación Klafs Sauna App
2. Asegúrese de que su cuenta no esté bloqueada (máximo 3 intentos)
3. Revise los registros de Home Assistant: `Configuración > Registros`

### La sauna no aparece

1. Asegúrese de que su sauna esté correctamente configurada en la aplicación Klafs
2. Verifique que el módulo Wi-Fi esté conectado
3. Reinicie la integración

### Los comandos no funcionan

1. Verifique que la sauna esté conectada (`isConnected: true`)
2. Asegúrese de haber configurado un código PIN en su sauna
3. Verifique que la puerta de la sauna haya sido controlada

Para más ayuda, consulte la [Guía de Solución de Problemas](TROUBLESHOOTING.md).

## Contribuir

¡Las contribuciones son bienvenidas! Siéntase libre de:

- Reportar errores
- Sugerir nuevas características
- Enviar pull requests

Consulte [CONTRIBUTING.md](CONTRIBUTING.md) para más detalles.

## Licencia

Licencia MIT - Ver [LICENSE](LICENSE)

## Créditos

- Basado en la investigación de API de la comunidad OpenHAB
- Inspirado en el proyecto [IPSymconKlafsSaunaControl](https://github.com/Pommespanzer/IPSymconKlafsSaunaControl)

## Descargo de Responsabilidad

Esta integración no es oficial y no está afiliada con Klafs GmbH. Úsela bajo su propio riesgo.
