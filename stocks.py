import os

import pandas as pd

# from create_df import partition_1d

# fetch symbol
stocks = []
for file_name in sorted(os.listdir('./data/1d')):
    symbol = file_name.split('_SET')[0]
    stocks.append(symbol.lower())

# fetch datetime by timeframe
# not done
first_date = "2021-09-06 09:00:00+07:00"
raw_1d = pd.read_csv("./data/1d/AAV_SET.csv")
raw_1d["datetime"] = pd.to_datetime(raw_1d["datetime"])
raw_1d.set_index("datetime", inplace=True)
date_1d = raw_1d[first_date:].index


# fetch price by symbol and timeframe
def get_price(symbol: str, tf: str):
    raw = pd.read_csv(f"./data/{tf}/{symbol}_SET.csv")
    raw["datetime"] = pd.to_datetime(raw["datetime"])
    raw.set_index("datetime", inplace=True)
    return raw["Close"][first_date:]


print("eval us")
