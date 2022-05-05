import requests
import json
import os

API_TOKEN = "e5709f22d8be4d70a738cc6b9dc764a2"
API_ROOT = "https://api.synopticdata.com/v2/"
API_EXTENSION = "variables"
API_URL = os.path.join(API_ROOT, API_EXTENSION)
API_ARGS = {
    "token": API_TOKEN,
}

response = requests.get(API_URL, params=API_ARGS)
response = json.loads(response.content)

allVariables = response['VARIABLES']
variableNames = []
for variableObj in allVariables:
    variableNames += list(variableObj.keys())

print(f"Total number of variables found: {len(allVariables)}")

with open("variableInfo.json", "w") as outfile:
    outfile.write(json.dumps(allVariables))

with open("variableNames.json", "w") as outfile:
    outfile.write(json.dumps(variableNames))