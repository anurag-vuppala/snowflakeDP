import pandas as pd
import requests
import json
from datetime import datetime

URL =  "https://data.police.uk/api/crimes-street/all-crime?&date=2021-01"

head = {
        "poly": "",
        "month": "2021-12"
    }

r = requests.get(URL)

# data = r.json()

print(r)

# datadf = pd.DataFrame(data)

# print(datadf)

# datadf.to_csv('data_2021-12.csv')




