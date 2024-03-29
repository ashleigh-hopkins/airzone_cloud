"""Constants for the Airzone Cloud integration."""

from typing import Final

DOMAIN: Final[str] = "airzone_cloud"
MANUFACTURER: Final[str] = "Airzone"

SENSOR_COMPRESSOR_DISCHARGE_PRESSURE: Final[str] = "Compressor Discharge Pressure"
SENSOR_COMPRESSOR_DISCHARGE_TEMPERATURE: Final[str] = "Compressor Discharge Temperature"
SENSOR_EXTERNAL_TEMPERATURE: Final[str] = "External Temperature"
SENSOR_INDOOR_UNIT_HEAT_EXCHANGER_TEMPERATURE: Final[str] = "Indoor Unit Heat Exchanger Temperature"
SENSOR_OUTDOOR_UNIT_HEAT_EXCHANGER_TEMPERATURE: Final[str] = "Outdoor Unit Heat Exchanger Temperature"
SENSOR_POWER_CONSUMPTION: Final[str] = "Power Consumption"
SENSOR_RETURN_TEMPERATURE: Final[str] = "Return Temperature"
SENSOR_WORK_TEMPERATURE: Final[str] = "Work Temperature"

AIOAIRZONE_CLOUD_TIMEOUT_SEC: Final[int] = 30
