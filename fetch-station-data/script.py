import requests
import json
import os
import pandas as pd
import datetime

from pprint import pprint
from tqdm import tqdm

import warnings
warnings.filterwarnings('ignore')

API_TOKEN = "e5709f22d8be4d70a738cc6b9dc764a2"
API_ROOT = "https://api.synopticdata.com/v2/"
API_EXTENSION = "stations/timeseries"
API_URL = os.path.join(API_ROOT, API_EXTENSION)
API_ARGS = {
    "token": API_TOKEN,
    # "recent": 43200
}

STATION_IDS = ['WBB', 'HOL', 'SB2', 'SNV',
               'MBY', 'DVB', 'EMPUT', 'GNI', 'HATUT']


def convertDateToString(date):
    return date.strftime("%Y%m%d%H%M")


file = open("../all-variables/variableNames.json")
variableNames = json.load(file)
variableNames = set(variableNames)

combinedDf = pd.DataFrame()

end = datetime.datetime.now()
start = end - datetime.timedelta(30)


for i in tqdm(range(13, 121)):
    print(
        f"Loop: {i}/{120}: From {start} to  {end}")
    for stationId in STATION_IDS:
        try:
            # print(
            #     f"\nStation {STATION_IDS.index(stationId) + 1}/{len(STATION_IDS)} : {stationId}")
            NEW_API_ARGS = API_ARGS
            NEW_API_ARGS['stid'] = stationId
            NEW_API_ARGS['start'] = convertDateToString(start)
            NEW_API_ARGS['end'] = convertDateToString(end)
            response = requests.get(API_URL, params=NEW_API_ARGS)
            response = json.loads(response.content)
            observations = response['STATION'][0]['OBSERVATIONS']

            fetchedData = {}

            for variable, observedValues in observations.items():
                variable = variable.split("_set_1d")[0].split("_set_1")[0]
                if variable in variableNames:
                    if type(observedValues[0]) is dict:
                        continue
                    fetchedData[variable] = observedValues
                elif variable == "date_time":
                    fetchedData['timestamp'] = observedValues

            fetchedDataDf = pd.DataFrame.from_dict(fetchedData)
            fetchedDataDf["stationId"] = stationId
            for variableName in variableNames:
                if variableName not in fetchedDataDf.columns:
                    fetchedDataDf[variableName] = None
            combinedDf = pd.concat([combinedDf, fetchedDataDf],
                                   axis=0, ignore_index=True)
        except Exception as e:
            print(
                f"Exception occured for i={i}, start={start}, end={end}: {e}")
            print(f"Additional info, station ID: {stationId}")

    if i % 12 == 0:
        filename = f"data/{i // 12}.csv"
        combinedDf.to_csv(filename, encoding="utf-8", index=False)
        combinedDf = pd.DataFrame()
        print(f"Saving to file: {filename}")

    start -= datetime.timedelta(days=30)
    end -= datetime.timedelta(days=30)
