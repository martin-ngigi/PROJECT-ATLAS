from  enum import  Enum

class ClimateTypes(Enum):
    TEMPERATURE = ("Temperature", "°C", "Celsius")
    PRECIPITATION= ("Precipitation", "mm", "Millimeters")

    HUMIDITY = ("Relative Humidity", "%", "Percentage")

    WIND_SPEED = ("Wind Speed", "m/s", "Meters per second")
    WIND_DIRECTION = ("Wind Direction", "°", "Degrees")

    ATMOSPHERIC_PRESSURE = ("Atmospheric Pressure", "hPa", "Hectopascals")

    CLOUD_COVER = ("Cloud Cover", "%", "Percentage")

    SOLAR_RADIATION = ("Solar Radiation", "MJ/m²", "Megajoules per square meter")

    VISIBILITY = ("Visibility", "m", "Meters")

    SOIL_MOISTURE = ("Soil Moisture", "m³/m³", "Volumetric water content")

    EVAPOTRANSPIRATION = ("Evapotranspiration", "mm", "Millimeters")

    DEW_POINT = ("Dew Point", "°C", "Celsius")

    UV_INDEX = ("UV Index", "", "Index value")

    @property
    def label(self):
        return self.value[0]

    @property
    def unit(self):
        return self.value[1]

    @property
    def unit_name(self):
        return self.value[2]

    @classmethod
    def choices(cls):
        return [(member.label, member.unit) for member in cls]

    @classmethod
    def get_unit_by_unit_name(cls, unit_name: str):
        """
        Return the unit symbol (e.g., '°C') given a unit name (e.g., 'Celsius').
        """
        for member in cls:
            if member.unit_name.lower() == unit_name.lower():
                return member.unit
        return None

    @classmethod
    def get_label_by_unit_name(cls, unit_name: str):
        """
        Return the unit label (e.g., 'Temperature') given a unit name (e.g., 'Celsius').
        """
        for member in cls:
            if member.unit_name.lower() == unit_name.lower():
                return member.label
        return None

    @classmethod
    def get_by_label(cls, label: str):
        """
        Return the entire enum member given a label (e.g., 'Temperature').
        """
        for member in cls:
            if member.label.lower() == label.lower():
                return member
        return None

