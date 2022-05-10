from ast import Str
from sqlalchemy import Column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.types import Integer, String
from db_config import engine

"""
create models by defining Python classes that declarative_base from SQLAlchemy
"""
Base = declarative_base()


class WeatherStation(Base):

    __tablename__ = "weather_station_data"

    id = Column(Integer, primary_key=True, autoincrement="auto")
    stationId = Column(String(255))
    timestamp = Column(String(255))
    air_temp = Column(String(255))
    dew_point_temperature = Column(String(255))
    relative_humidity = Column(String(255))
    wind_gust = Column(String(255))
    wind_speed = Column(String(255))
    wind_cardinal_direction = Column(String(255))
    wind_direction = Column(String(255))
    volt = Column(String(255))
    altimeter = Column(String(255))
    solar_radiation = Column(String(255))
    sea_level_pressure = Column(String(255))
    pressure = Column(String(255))
    precip_accum_one_minute = Column(String(255))
    precip_accum_five_minute = Column(String(255))
    wind_chill = Column(String(255))
    heat_index = Column(String(255))
    snow_interval = Column(String(255))
    ozone_concentration = Column(String(255))
    sensor_error_code = Column(String(255))
    PM_25_concentration = Column(String(255))
    snow_depth = Column(String(255))
    precip_accum_fifteen_minute = Column(String(255))
    air_temp_2m = Column(String(255))


Base.metadata.create_all(engine)
