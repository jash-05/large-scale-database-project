from model import WeatherStation
from db_config import session, mysql_db, cursor
from tqdm import tqdm
from mapper import getDataframe

# Base.metadata.drop_all(engine)


class InsertService:
    def bulkInsert(self):
        bulk = []

        print("Creating data frames from csv")
        for i in tqdm(range(6, 11)):
            df = getDataframe(int(i))
            bulk.append(df)

        df = getDataframe(int(1))
        bulk.append(df)

        for df_idx in range(len(bulk)):

            print(f"{df_idx} => Inserting df into SQL db")
            bulk_insert_data = []

            for idx in tqdm(range(len(bulk[df_idx]))):

                stationId = bulk[df_idx].iloc[idx]["stationId"]
                timestamp = bulk[df_idx].iloc[idx]["timestamp"]
                air_temp = bulk[df_idx].iloc[idx]["air_temp"]
                dew_point_temperature = bulk[df_idx].iloc[idx]["dew_point_temperature"]
                relative_humidity = bulk[df_idx].iloc[idx]["relative_humidity"]
                wind_gust = bulk[df_idx].iloc[idx]["wind_gust"]
                wind_speed = bulk[df_idx].iloc[idx]["wind_speed"]
                wind_cardinal_direction = bulk[df_idx].iloc[idx][
                    "wind_cardinal_direction"
                ]
                wind_direction = bulk[df_idx].iloc[idx]["wind_direction"]
                volt = bulk[df_idx].iloc[idx]["volt"]
                altimeter = bulk[df_idx].iloc[idx]["altimeter"]
                solar_radiation = bulk[df_idx].iloc[idx]["solar_radiation"]
                sea_level_pressure = bulk[df_idx].iloc[idx]["sea_level_pressure"]
                pressure = bulk[df_idx].iloc[idx]["pressure"]
                precip_accum_one_minute = bulk[df_idx].iloc[idx][
                    "precip_accum_one_minute"
                ]
                precip_accum_five_minute = bulk[df_idx].iloc[idx][
                    "precip_accum_five_minute"
                ]
                wind_chill = bulk[df_idx].iloc[idx]["wind_chill"]
                heat_index = bulk[df_idx].iloc[idx]["heat_index"]
                snow_interval = bulk[df_idx].iloc[idx]["snow_interval"]
                ozone_concentration = bulk[df_idx].iloc[idx]["ozone_concentration"]
                sensor_error_code = bulk[df_idx].iloc[idx]["sensor_error_code"]
                PM_25_concentration = bulk[df_idx].iloc[idx]["PM_25_concentration"]
                snow_depth = bulk[df_idx].iloc[idx]["snow_depth"]
                precip_accum_fifteen_minute = bulk[df_idx].iloc[idx][
                    "precip_accum_fifteen_minute"
                ]
                air_temp_2m = bulk[df_idx].iloc[idx]["air_temp_2m"]

                bulk_insert_data.append(
                    (
                        stationId,
                        timestamp,
                        air_temp,
                        dew_point_temperature,
                        relative_humidity,
                        wind_gust,
                        wind_speed,
                        wind_cardinal_direction,
                        wind_direction,
                        volt,
                        altimeter,
                        solar_radiation,
                        sea_level_pressure,
                        pressure,
                        precip_accum_one_minute,
                        precip_accum_five_minute,
                        wind_chill,
                        heat_index,
                        snow_interval,
                        ozone_concentration,
                        sensor_error_code,
                        PM_25_concentration,
                        snow_depth,
                        precip_accum_fifteen_minute,
                        air_temp_2m,
                    )
                )

            query = "INSERT INTO weather_station_data (stationId, timestamp, air_temp, dew_point_temperature, relative_humidity, wind_gust, wind_speed, wind_cardinal_direction, wind_direction, volt, altimeter, solar_radiation, sea_level_pressure, pressure, precip_accum_one_minute, precip_accum_five_minute, wind_chill, heat_index, snow_interval, ozone_concentration, sensor_error_code, PM_25_concentration, snow_depth, precip_accum_fifteen_minute, air_temp_2m) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            cursor.executemany(query, bulk_insert_data)
            mysql_db.commit()
            print("Bulk insert successful")

    def bulkInsertWithOrm(self):

        bulk = []

        print("Creating data frames from csv")
        # for i in tqdm(range(2, 6)):
        #     df = getDataframe(int(i))
        #     bulk.append(df)
        bulk.append(getDataframe(int(1)))
        for df_idx in range(len(bulk)):

            print(f"{df_idx} => Inserting df into SQL db")
            bulk_insert_data = []

            for idx in tqdm(range(len(bulk[df_idx]))):

                stationId = bulk[df_idx].iloc[idx]["stationId"]
                timestamp = bulk[df_idx].iloc[idx]["timestamp"]
                air_temp = bulk[df_idx].iloc[idx]["air_temp"]
                dew_point_temperature = bulk[df_idx].iloc[idx]["dew_point_temperature"]
                relative_humidity = bulk[df_idx].iloc[idx]["relative_humidity"]
                wind_gust = bulk[df_idx].iloc[idx]["wind_gust"]
                wind_speed = bulk[df_idx].iloc[idx]["wind_speed"]
                wind_cardinal_direction = bulk[df_idx].iloc[idx][
                    "wind_cardinal_direction"
                ]
                wind_direction = bulk[df_idx].iloc[idx]["wind_direction"]
                volt = bulk[df_idx].iloc[idx]["volt"]
                altimeter = bulk[df_idx].iloc[idx]["altimeter"]
                solar_radiation = bulk[df_idx].iloc[idx]["solar_radiation"]
                sea_level_pressure = bulk[df_idx].iloc[idx]["sea_level_pressure"]
                pressure = bulk[df_idx].iloc[idx]["pressure"]
                precip_accum_one_minute = bulk[df_idx].iloc[idx][
                    "precip_accum_one_minute"
                ]
                precip_accum_five_minute = bulk[df_idx].iloc[idx][
                    "precip_accum_five_minute"
                ]
                wind_chill = bulk[df_idx].iloc[idx]["wind_chill"]
                heat_index = bulk[df_idx].iloc[idx]["heat_index"]
                snow_interval = bulk[df_idx].iloc[idx]["snow_interval"]
                ozone_concentration = bulk[df_idx].iloc[idx]["ozone_concentration"]
                sensor_error_code = bulk[df_idx].iloc[idx]["sensor_error_code"]
                PM_25_concentration = bulk[df_idx].iloc[idx]["PM_25_concentration"]
                snow_depth = bulk[df_idx].iloc[idx]["snow_depth"]
                precip_accum_fifteen_minute = bulk[df_idx].iloc[idx][
                    "precip_accum_fifteen_minute"
                ]
                air_temp_2m = bulk[df_idx].iloc[idx]["air_temp_2m"]

                weather_station = WeatherStation()
                weather_station.stationId = stationId
                weather_station.timestamp = timestamp
                weather_station.air_temp = air_temp
                weather_station.dew_point_temperature = dew_point_temperature
                weather_station.relative_humidity = relative_humidity
                weather_station.wind_gust = wind_gust
                weather_station.wind_speed = wind_speed
                weather_station.wind_cardinal_direction = wind_cardinal_direction
                weather_station.wind_direction = wind_direction
                weather_station.volt = volt
                weather_station.altimeter = altimeter
                weather_station.solar_radiation = solar_radiation
                weather_station.sea_level_pressure = sea_level_pressure
                weather_station.pressure = pressure
                weather_station.precip_accum_one_minute = precip_accum_one_minute
                weather_station.precip_accum_five_minute = precip_accum_five_minute
                weather_station.wind_chill = wind_chill
                weather_station.heat_index = heat_index
                weather_station.snow_interval = snow_interval
                weather_station.ozone_concentration = ozone_concentration
                weather_station.sensor_error_code = sensor_error_code
                weather_station.PM_25_concentration = PM_25_concentration
                weather_station.snow_depth = snow_depth
                weather_station.precip_accum_fifteen_minute = (
                    precip_accum_fifteen_minute
                )
                weather_station.air_temp_2m = air_temp_2m

                bulk_insert_data.append(weather_station)

            session.bulk_save_objects(bulk_insert_data)
            session.commit()
