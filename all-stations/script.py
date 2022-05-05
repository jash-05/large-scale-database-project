import requests
import json
import os

API_TOKEN = "e5709f22d8be4d70a738cc6b9dc764a2"
API_ROOT = "https://api.synopticdata.com/v2/"
API_EXTENSION = "stations/timeseries"
API_URL = os.path.join(API_ROOT, API_EXTENSION)
API_ARGS = {
    "token": API_TOKEN,
    "recent": 20
}

response = requests.get(API_URL, params=API_ARGS)
response = json.loads(response.content)

allStations = response['STATION']
stationIds = []
for stationObj in allStations:
    stationIds.append(stationObj['STID'])

print(f"Total number of stations found: {len(stationIds)}")

with open("stationIds.txt", "w") as outfile:
    outfile.write("\n".join(stationIds))