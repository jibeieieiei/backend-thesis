# import json
# from pathlib import Path

import pandas as pd

# import requests
from sqlalchemy import create_engine

# SET 50
stocks = [
    'ADVANC', 'AOT', 'AWC', 'BANPU', 'BBL', 'BDMS', 'BEM', 'BGRIM', 'BH',
    'BTS', 'CBG', 'CENTEL', 'COM7', 'CPALL', 'CPF', 'CPN', 'CRC', 'DELTA',
    'EA', 'EGCO', 'GLOBAL', 'GPSC', 'GULF', 'HMPRO', 'INTUCH', 'IVL',
    'KBANK', 'KCE', 'KTB', 'KTC', 'LH', 'MINT', 'MTC', 'OR',
    'OSP', 'PTT', 'PTTEP', 'PTTGC', 'RATCH', 'SAWAD', 'SCB',
    'SCC', 'SCGP', 'TISCO',
    # 'TLI',
    'TOP', 'TRUE', 'TTB', 'TU', 'WHA',
]


class Fundamentals:
    def __init__(self, symbol: str, stocks: list = stocks):
        self.symbol = symbol
        self.data = None
        self.stocks = stocks
        self.load_data()
        print("DEBUG")

    def load_data(self):
        file_path = f"./data/fund_set/{self.symbol}.json"
        try:
            data = pd.read_json(file_path)
            data = data.loc[data['date'] == data['date'].max()].T
            data.columns = [self.symbol+"_fund"]
            self.data = data
        except FileNotFoundError:
            print(symbol+"file not founde error.")


if __name__ == "__main__":
    engine = create_engine('sqlite:///./project.db', echo=False)
    # Update to DB
    _df = pd.DataFrame()
    for symbol in stocks:
        df = Fundamentals(symbol).data
        cols = _df.columns.to_list() + df.columns.to_list()
        _df = pd.concat([_df, df], axis=1, ignore_index=True)
        _df.columns = cols
    # To SQL
    # Change Type to String
    _df = _df.reset_index().astype(str)
    _df.to_sql(name='trading_stats_compare',
               con=engine, if_exists="replace")
    print("Trading Stats Done..")
