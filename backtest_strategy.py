import numpy as np
import pandas as pd
import pandas_ta as ta
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

timeframe = ["15t", "1h", "4h", "1d"]

columns = ["Close"]


class BacktestStrategy:

    def __init__(self,
                 symbol: str,
                 timeframe: str,
                 column: str):
        self.symbol = symbol
        self.timeframe = timeframe
        self.column = column
        self.length_by_tf = {'15t': 11683, '1h': 4862, '4h': 1394, '1d': 698}
        self.data = None
        self.load_data()

    def load_data(self):
        length = self.length_by_tf[self.timeframe]
        file_path = f"./data/{self.timeframe}/{self.symbol}_SET.csv"
        data = pd.read_csv(file_path)
        self.data = data[len(data)-length:].reset_index().drop(columns='index')
        return

    def ema_cross(self,
                  short: int = 50,
                  long: int = 200):
        column = self.column
        symbol = self.symbol.upper()
        df = self.data.reset_index()[['datetime', column]].copy()
        # df = self.data.set_index('datetime')[column].copy()
        new_col = symbol+"_"+column.lower()
        df = df.rename(columns={column: new_col,
                                "datetime": symbol+"_datetime"})
        ema_short = ta.ema(df[new_col], short)
        ema_long = ta.ema(df[new_col], long)
        # -------Bullish-------
        df[symbol+'_buy_signal'] = ema_short > ema_long
        # -------Bearish-------
        df[symbol+'_sell_signal'] = ema_short < ema_long
        return df


if __name__ == "__main__":
    engine = create_engine('sqlite:///./project.db', echo=False)

    # EMA_CROSS to DATABASE
    for tf in timeframe[:]:
        for col in columns[:]:
            _df = pd.DataFrame()
            for symbol in stocks[:]:
                df = BacktestStrategy(symbol, tf, col).ema_cross()
                _df = pd.concat([_df, df], axis=1)
            _df.to_sql(name=f'ema_cross_{col.lower()}_{tf.lower()}',
                       con=engine, if_exists="replace")
            print(f"Backtest EMA_CROSS {tf} Done..")