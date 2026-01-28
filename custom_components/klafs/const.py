"""Constants for the Klafs Sauna integration."""

DOMAIN = "klafs"

# Configuration
CONF_PIN = "pin"
CONF_SAUNAS = "saunas"

# API Constants
API_BASE_URL = "https://sauna-app.klafs.com"
API_LOGIN_ENDPOINT = "/Account/Login"
API_GET_DATA_ENDPOINT = "/SaunaApp/GetData"
API_START_CABIN_ENDPOINT = "/SaunaApp/StartCabin"
API_STOP_CABIN_ENDPOINT = "/SaunaApp/StopCabin"
API_SET_MODE_ENDPOINT = "/SaunaApp/SetMode"
API_CHANGE_TEMPERATURE_ENDPOINT = "/SaunaApp/ChangeTemperature"
API_CHANGE_HUM_LEVEL_ENDPOINT = "/SaunaApp/ChangeHumLevel"
API_SET_SELECTED_TIME_ENDPOINT = "/SaunaApp/SetSelectedTime"

# Sauna Modes
MODE_SAUNA = 1
MODE_SANARIUM = 2
MODE_IR = 3

# Status Codes
STATUS_OFF = 0
STATUS_HEATING = 1
STATUS_READY = 2
STATUS_ERROR = 3

# Temperature Limits
TEMP_MIN_SAUNA = 10
TEMP_MAX_SAUNA = 100
TEMP_MIN_SANARIUM = 40
TEMP_MAX_SANARIUM = 75
TEMP_MIN_IR = 30
TEMP_MAX_IR = 100

# Humidity Levels (SANARIUM only)
HUMIDITY_MIN = 1
HUMIDITY_MAX = 10
