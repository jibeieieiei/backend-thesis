import warnings

import numpy as np
import pandas as pd
import pandas_ta as ta
import vectorbtpro as vbt
from sqlalchemy import create_engine

from stocks_symbol import stocks

warnings.filterwarnings("ignore")

# SET 50

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
        # -------Add EMA-------
        df[symbol+'_ema_short'] = ema_short
        df[symbol+'_ema_long'] = ema_long
        # -------Bullish-------
        entries = ema_short > ema_long
        df[symbol+'_buy_signal'] = entries
        # -------Bearish-------
        exits = ema_short < ema_long
        df[symbol+'_sell_signal'] = ema_short < ema_long
        df[symbol+'_sell_signal'].iloc[-1] = True
        # -------Signal-------
        pf = vbt.Portfolio.from_signals(df[f"{symbol}_close"], entries, exits)
        stats = pf.stats().to_frame()
        stats.columns = [symbol+'_stats']
        # -------Trade History for green red signal-------
        th = pf.get_trade_history()  # th: trade history
        # INIT
        green_filter = th.loc[th['Side'] == 'Buy']['Signal Index']
        df[symbol+'_green_signal'] = False
        df.loc[green_filter, symbol + '_green_signal'] = True
        df[symbol+'_green_signal'] = np.where(
            df[symbol+'_green_signal'], df[symbol+'_close']*0.85, np.nan)

        red_filter = th.loc[th['Side'] == 'Sell']['Signal Index']
        df[symbol+'_red_signal'] = False
        df.loc[red_filter, symbol + '_red_signal'] = True
        df[symbol+'_red_signal'] = np.where(
            df[symbol+'_red_signal'], df[symbol+'_close']*0.85, np.nan)
        return df, stats

    def rsi(self,
            length: int = 14,
            over_sold: int = 30,
            over_bought: int = 70):
        column = self.column
        symbol = self.symbol.upper()
        df = self.data.reset_index()[['datetime', column]].copy()
        new_col = symbol+"_"+column.lower()
        df = df.rename(columns={column: new_col,
                                "datetime": symbol+"_datetime"})
        _rsi = ta.rsi(df[new_col], length)
        # -------Add RSI-------
        df[symbol+'_rsi'] = _rsi
        # -------Bullish-------
        entries = _rsi <= over_sold
        df[symbol+'_buy_signal'] = entries
        # -------Bearish-------
        exits = _rsi >= over_bought
        df[symbol+'_sell_signal'] = exits
        df[symbol+'_sell_signal'].iloc[-1] = True
        # -------Signal-------
        pf = vbt.Portfolio.from_signals(df[f"{symbol}_close"], entries, exits)
        stats = pf.stats().to_frame()
        stats.columns = [symbol+'_stats']
        # -------Trade History for green red signal-------
        th = pf.get_trade_history()  # th: trade history

        green_filter = th.loc[th['Side'] == 'Buy']['Signal Index']
        df[symbol+'_green_signal'] = False
        df.loc[green_filter, symbol + '_green_signal'] = True
        df[symbol+'_green_signal'] = np.where(
            df[symbol+'_green_signal'], df[symbol+'_close']*0.85, np.nan)

        red_filter = th.loc[th['Side'] == 'Sell']['Signal Index']
        df[symbol+'_red_signal'] = False
        df.loc[red_filter, symbol + '_red_signal'] = True
        df[symbol+'_red_signal'] = np.where(
            df[symbol+'_red_signal'], df[symbol+'_close']*0.85, np.nan)
        return df, stats


if __name__ == "__main__":
    engine = create_engine('sqlite:///./project.db', echo=False)

    # EMA_CROSS to DATABASE
    for tf in timeframe[:]:
        for col in columns[:]:
            _df = pd.DataFrame()
            _stats = pd.DataFrame()
            for symbol in stocks[:]:
                df, stats = BacktestStrategy(symbol, tf, col).ema_cross()
                _df = pd.concat([_df, df], axis=1)
                cols = _stats.columns.to_list() + stats.columns.to_list()
                _stats = pd.concat([_stats, stats], axis=1, ignore_index=True)
                _stats.columns = cols
            _df.to_sql(name=f'ema_cross_{col.lower()}_{tf.lower()}',
                       con=engine, if_exists="replace")
            # Edit Name Index of Stats
            _index = [x.replace("[%]", "percent")
                      for x in _stats.index.str.lower()]
            _stats.index = [x.strip().replace(" ", "_") for x in _index]
            _stats = _stats.astype(float)
            _stats.reset_index(inplace=True)
            _stats.to_sql(name=f'ema_cross_stats_{col.lower()}_{tf.lower()}',
                          con=engine, if_exists="replace")
            print(f"Backtest EMA_CROSS {tf} Done..")
    # End EMA_CROSS --------------------------

    # RSI to DATABASE
    for tf in timeframe[:]:
        for col in columns[:]:
            _df = pd.DataFrame()
            _stats = pd.DataFrame()
            for symbol in stocks[:]:
                df, stats = BacktestStrategy(symbol, tf, col).rsi()
                _df = pd.concat([_df, df], axis=1)
                cols = _stats.columns.to_list() + stats.columns.to_list()
                _stats = pd.concat([_stats, stats], axis=1, ignore_index=True)
                _stats.columns = cols
            _df.to_sql(name=f'rsi_{col.lower()}_{tf.lower()}',
                       con=engine, if_exists="replace")
            # Edit Name Index of Stats
            _index = [x.replace("[%]", "percent")
                      for x in _stats.index.str.lower()]
            _stats.index = [x.strip().replace(" ", "_") for x in _index]
            _stats = _stats.astype(float)
            _stats.reset_index(inplace=True)
            _stats.to_sql(name=f'rsi_stats_{col.lower()}_{tf.lower()}',
                          con=engine, if_exists="replace")
            print(f"Backtest RSI {tf} Done..")
    # End RSI --------------------------
