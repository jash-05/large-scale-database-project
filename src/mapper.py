def getDataframe(fileNumber):

    import pandas as pd

    path = f"/Applications/projects/large-scale-database-project/fetch-station-data/data/{fileNumber}.csv"

    data = pd.read_csv(path)

    data_of_interest = data[
        [
            "stationId",
            "timestamp",
            "air_temp",
            "dew_point_temperature",
            "relative_humidity",
            "wind_gust",
            "wind_speed",
            "wind_cardinal_direction",
            "wind_direction",
            "volt",
            "altimeter",
            "solar_radiation",
            "sea_level_pressure",
            "pressure",
            "precip_accum_one_minute",
            "precip_accum_five_minute",
            "wind_chill",
            "heat_index",
            "snow_interval",
            "ozone_concentration",
            "sensor_error_code",
            "PM_25_concentration",
            "snow_depth",
            "precip_accum_fifteen_minute",
            "air_temp_2m",
        ]
    ]

    # print(data_of_interest.info())

    cols = [
        "stationId",
        "timestamp",
        "air_temp",
        "dew_point_temperature",
        "relative_humidity",
        "wind_gust",
        "wind_speed",
        "wind_cardinal_direction",
        "wind_direction",
        "volt",
        "altimeter",
        "solar_radiation",
        "sea_level_pressure",
        "pressure",
        "precip_accum_one_minute",
        "precip_accum_five_minute",
        "wind_chill",
        "heat_index",
        "snow_interval",
        "ozone_concentration",
        "sensor_error_code",
        "PM_25_concentration",
        "snow_depth",
        "precip_accum_fifteen_minute",
        "air_temp_2m",
    ]

    for col in cols:
        data_of_interest[col] = data_of_interest[col].astype(str)

    return data_of_interest


print(getDataframe(1).iloc[0]["stationId"])
