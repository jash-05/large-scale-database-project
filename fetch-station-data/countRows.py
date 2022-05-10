import pandas as pd
from codetiming import Timer


@Timer(name="decorator")
def x():
    totalRows = 0
    for i in range(1, 11):
        filename = f"data/{i}.csv"
        data = pd.read_csv(filename)
        rows = len(data)
        print(rows)
        totalRows += rows

    print(f"\nTotal Rows: {totalRows}")


print(x())
