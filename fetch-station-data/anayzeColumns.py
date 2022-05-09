from numpy import require
import pandas as pd
import json

data = pd.read_csv("data/0.csv")

counts = data.isna().sum()
counts = counts.sort_values()[:25]
s = counts

requiredColumns = []
i = 0
for index, value in s.items():
    requiredColumns.append(index)
    i += 1
    if i == 25:
        break

print(len(requiredColumns))

with open("requiredColumns.json", "w") as outfile:
    outfile.write(json.dumps(requiredColumns))
