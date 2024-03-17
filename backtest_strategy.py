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

stop_loss = [0, 2, 4, 6]


class BacktestStrategy:

    def __init__(self,
                 symbol: str,
                 timeframe: str,
                 column: str,
                 start_date: str = "2023-01-01",
                 end_date: str = "2024-01-01",
                 stop_loss: float = 0,
                 take_profit: float = 0):
        self.symbol = symbol
        self.timeframe = timeframe
        self.column = column
        self.start_date = start_date
        self.end_date = end_date
        self.stop_loss = stop_loss
        self.take_profit = take_profit
        self.length_by_tf = {'15t': 11683, '1h': 4862, '4h': 1394, '1d': 698}
        self.data = None
        self.load_data()

    def load_data(self):
        file_path = f"./data/{self.timeframe}/{self.symbol}_SET.csv"
        data = pd.read_csv(file_path)
        data = data.loc[(data['datetime'] >= self.start_date)
                        & (data['datetime'] <= self.end_date)]
        self.data = data.reset_index().drop(columns='index')
        return

    def ema_cross(self,
                  short: int = 50,
                  long: int = 200,
                  fee: float = 0.20):
        column = self.column
        symbol = self.symbol.upper()
        df = self.data.copy()
        # new_col = symbol+"_"+df.columns.str.lower()
        df = df.rename(columns={
            "Open": symbol+"_open",
            "High": symbol+"_high",
            "Low": symbol+"_low",
            "Close": symbol+"_close",
            "Volume": symbol+"_volume",
            "datetime": symbol+"_datetime"})
        ema_short = ta.ema(df[f"{symbol}_{column.lower()}"], short)
        ema_long = ta.ema(df[f"{symbol}_{column.lower()}"], long)
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
        if self.stop_loss == 0:
            pf = vbt.Portfolio.from_signals(
                df[f"{symbol}_{column.lower()}"], entries, exits, fixed_fees=fee)
        else:
            pf = vbt.Portfolio.from_signals(
                df[f"{symbol}_{column.lower()}"], entries, exits,
                sl_stop=self.stop_loss / 100,
                tp_stop=self.take_profit / 100,
                fixed_fees=fee)
        stats = pf.stats().to_frame()
        stats.columns = [symbol+'_stats']
        stats = stats.drop(['Total Time Exposure [%]', 'Benchmark Return [%]',
                            'Max Gross Exposure [%]', 'Max Drawdown Duration',
                            # 'Total Fees Paid',
                            'Total Orders',
                            'Avg Winning Trade Duration',
                            'Avg Losing Trade Duration', 'Profit Factor',
                            'Expectancy'])
        # -------Trade History for green red signal-------
        th = pf.get_trade_history()  # th: trade history
        # INIT
        green_filter = th.loc[th['Side'] == 'Buy']['Signal Index']
        df[symbol+'_green_signal'] = False
        df.loc[green_filter, symbol + '_green_signal'] = True
        df[symbol+'_green_signal'] = np.where(
            df[symbol+'_green_signal'], df[symbol+'_low'],
            np.nan)

        red_filter = th.loc[th['Side'] == 'Sell']['Signal Index']
        df[symbol+'_red_signal'] = False
        df.loc[red_filter, symbol + '_red_signal'] = True
        df[symbol+'_red_signal'] = np.where(
            df[symbol+'_red_signal'], df[symbol+'_low'],
            np.nan)
        # Trade History
        th = th.drop(columns=['Order Id', 'Column', 'Creation Index',
                              'Fill Index', 'Type', 'Size',
                              'Position Id', 'Entry Trade Id',
                              'Exit Trade Id'])
        th.columns = [symbol+"_" +
                      x.replace(" ", "_").lower() for x in th.columns]
        signal_index = th[symbol+'_signal_index'].values
        th[symbol+'_signal_index'] = df[symbol+'_datetime'][signal_index].values
        return df, stats, th

    def rsi(self,
            length: int = 14,
            over_sold: int = 30,
            over_bought: int = 70,
            fee=0.2):
        column = self.column
        symbol = self.symbol.upper()
        df = self.data.copy()
        # new_col = symbol+"_"+df.columns.str.lower()
        df = df.rename(columns={
            "Open": symbol+"_open",
            "High": symbol+"_high",
            "Low": symbol+"_low",
            "Close": symbol+"_close",
            "Volume": symbol+"_volume",
            "datetime": symbol+"_datetime"})
        _rsi = ta.rsi(df[f"{symbol}_{column.lower()}"], length)
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
        if self.stop_loss == 0:
            pf = vbt.Portfolio.from_signals(
                df[f"{symbol}_{column.lower()}"], entries, exits, fixed_fees=fee)
        else:
            pf = vbt.Portfolio.from_signals(
                df[f"{symbol}_{column.lower()}"], entries, exits,
                sl_stop=self.stop_loss / 100,
                tp_stop=self.take_profit / 100,
                fixed_fees=fee)
        stats = pf.stats().to_frame()
        stats.columns = [symbol+'_stats']
        stats = stats.drop(['Total Time Exposure [%]', 'Benchmark Return [%]',
                            'Max Gross Exposure [%]', 'Max Drawdown Duration',
                            # 'Total Fees Paid',
                            'Total Orders',
                            'Avg Winning Trade Duration',
                            'Avg Losing Trade Duration', 'Profit Factor',
                            'Expectancy'])
        # -------Trade History for green red signal-------
        th = pf.get_trade_history()  # th: trade history

        green_filter = th.loc[th['Side'] == 'Buy']['Signal Index']
        df[symbol+'_green_signal'] = False
        df.loc[green_filter, symbol + '_green_signal'] = True
        df[symbol+'_green_signal'] = np.where(
            df[symbol+'_green_signal'], df[symbol+'_low'],
            np.nan)

        red_filter = th.loc[th['Side'] == 'Sell']['Signal Index']
        df[symbol+'_red_signal'] = False
        df.loc[red_filter, symbol + '_red_signal'] = True
        df[symbol+'_red_signal'] = np.where(
            df[symbol+'_red_signal'], df[symbol+'_low'],
            np.nan)
        # Trade History
        th = th.drop(columns=['Order Id', 'Column', 'Creation Index',
                              'Fill Index', 'Type', 'Size',
                              'Position Id', 'Entry Trade Id',
                              'Exit Trade Id'])
        th.columns = [symbol+"_" +
                      x.replace(" ", "_").lower() for x in th.columns]
        signal_index = th[symbol+'_signal_index'].values
        th[symbol+'_signal_index'] = df[symbol+'_datetime'][signal_index].values
        return df, stats, th

    def macd(self,
             fast: int = 12,
             slow: int = 26,
             signal: int = 9,
             fee: float = 0.2):
        column = self.column
        symbol = self.symbol.upper()
        df = self.data.copy()
        # new_col = symbol+"_"+df.columns.str.lower()
        df = df.rename(columns={
            "Open": symbol+"_open",
            "High": symbol+"_high",
            "Low": symbol+"_low",
            "Close": symbol+"_close",
            "Volume": symbol+"_volume",
            "datetime": symbol+"_datetime"})
        _macd = ta.macd(df[f"{symbol}_{column.lower()}"], fast, slow, signal)
        # -------Add MACD-------
        df[symbol+'_macd'] = _macd[f'MACD_{fast}_{slow}_{signal}']
        df[symbol+'_macds'] = _macd[f'MACDs_{fast}_{slow}_{signal}']
        # -------Bullish-------
        entries = df[symbol+'_macd'] > df[symbol+'_macds']
        df[symbol+'_buy_signal'] = entries
        # # -------Bearish-------
        exits = df[symbol+'_macd'] < df[symbol+'_macds']
        df[symbol+'_sell_signal'] = exits
        df[symbol+'_sell_signal'].iloc[-1] = True
        # # -------Signal-------
        if self.stop_loss == 0:
            pf = vbt.Portfolio.from_signals(
                df[f"{symbol}_{column.lower()}"], entries, exits, fixed_fees=fee)
        else:
            pf = vbt.Portfolio.from_signals(
                df[f"{symbol}_{column.lower()}"], entries, exits,
                sl_stop=self.stop_loss / 100,
                tp_stop=self.take_profit / 100,
                fixed_fees=fee)
        stats = pf.stats().to_frame()
        stats.columns = [symbol+'_stats']
        stats = stats.drop(['Total Time Exposure [%]', 'Benchmark Return [%]',
                            'Max Gross Exposure [%]', 'Max Drawdown Duration',
                            # 'Total Fees Paid',
                            'Total Orders',
                            'Avg Winning Trade Duration',
                            'Avg Losing Trade Duration', 'Profit Factor',
                            'Expectancy'])
        # # -------Trade History for green red signal-------
        th = pf.get_trade_history()  # th: trade history

        green_filter = th.loc[th['Side'] == 'Buy']['Signal Index']
        df[symbol+'_green_signal'] = False
        df.loc[green_filter, symbol + '_green_signal'] = True
        df[symbol+'_green_signal'] = np.where(
            df[symbol+'_green_signal'], df[symbol+'_low'],
            np.nan)

        red_filter = th.loc[th['Side'] == 'Sell']['Signal Index']
        df[symbol+'_red_signal'] = False
        df.loc[red_filter, symbol + '_red_signal'] = True
        df[symbol+'_red_signal'] = np.where(
            df[symbol+'_red_signal'], df[symbol+'_low'],
            np.nan)
        # Trade History
        th = th.drop(columns=['Order Id', 'Column', 'Creation Index',
                              'Fill Index', 'Type', 'Size',
                              'Position Id', 'Entry Trade Id',
                              'Exit Trade Id'])
        th.columns = [symbol+"_" +
                      x.replace(" ", "_").lower() for x in th.columns]
        signal_index = th[symbol+'_signal_index'].values
        th[symbol+'_signal_index'] = df[symbol+'_datetime'][signal_index].values
        return df, stats, th

    def adx(self,
            window: int = 14,
            down_level: int = 25,
            fee: float = 0.2):
        column = self.column
        symbol = self.symbol.upper()
        df = self.data.copy()
        # new_col = symbol+"_"+df.columns.str.lower()
        df = df.rename(columns={
            "Open": symbol+"_open",
            "High": symbol+"_high",
            "Low": symbol+"_low",
            "Close": symbol+"_close",
            "Volume": symbol+"_volume",
            "datetime": symbol+"_datetime"})

        _adx = ta.adx(df[f"{symbol}_high"], df[f"{symbol}_low"],
                      df[f"{symbol}_close"], window)
        # -------Add adx-------
        df[symbol+'_adx'] = _adx[f'ADX_{window}']
        # -------Bullish-------
        entries = (_adx['DMP_14'] > _adx['DMN_14']) & (
            _adx['ADX_14'] > down_level)
        df[symbol+'_buy_signal'] = entries
        # # -------Bearish-------
        exits = (_adx['DMP_14'] < _adx['DMN_14']) & (
            _adx['ADX_14'] > down_level)
        df[symbol+'_sell_signal'] = exits
        df[symbol+'_sell_signal'].iloc[-1] = True
        # # -------Signal-------
        if self.stop_loss == 0:
            pf = vbt.Portfolio.from_signals(
                df[f"{symbol}_{column.lower()}"], entries, exits, fixed_fees=fee)
        else:
            pf = vbt.Portfolio.from_signals(
                df[f"{symbol}_{column.lower()}"], entries, exits,
                sl_stop=self.stop_loss / 100,
                tp_stop=self.take_profit / 100,
                fixed_fees=fee)
        stats = pf.stats().to_frame()
        stats.columns = [symbol+'_stats']
        stats = stats.drop(['Total Time Exposure [%]', 'Benchmark Return [%]',
                            'Max Gross Exposure [%]', 'Max Drawdown Duration',
                            # 'Total Fees Paid',
                            'Total Orders',
                            'Avg Winning Trade Duration',
                            'Avg Losing Trade Duration', 'Profit Factor',
                            'Expectancy'])
        # # -------Trade History for green red signal-------
        th = pf.get_trade_history()  # th: trade history

        green_filter = th.loc[th['Side'] == 'Buy']['Signal Index']
        df[symbol+'_green_signal'] = False
        df.loc[green_filter, symbol + '_green_signal'] = True
        df[symbol+'_green_signal'] = np.where(
            df[symbol+'_green_signal'], df[symbol+'_low'],
            np.nan)

        red_filter = th.loc[th['Side'] == 'Sell']['Signal Index']
        df[symbol+'_red_signal'] = False
        df.loc[red_filter, symbol + '_red_signal'] = True
        df[symbol+'_red_signal'] = np.where(
            df[symbol+'_red_signal'], df[symbol+'_low'],
            np.nan)
        # Trade History
        th = th.drop(columns=['Order Id', 'Column', 'Creation Index',
                              'Fill Index', 'Type', 'Size',
                              'Position Id', 'Entry Trade Id',
                              'Exit Trade Id'])
        th.columns = [symbol+"_" +
                      x.replace(" ", "_").lower() for x in th.columns]
        signal_index = th[symbol+'_signal_index'].values
        th[symbol+'_signal_index'] = df[symbol+'_datetime'][signal_index].values
        return df, stats, th


if __name__ == "__main__":
    engine = create_engine('sqlite:///./project.db', echo=False)

    # EMA_CROSS to DATABASE
    for tf in timeframe[:]:
        for col in columns[:]:
            for sl in stop_loss[:]:
                _df = pd.DataFrame()
                _stats = pd.DataFrame()
                _th = pd.DataFrame()
                for symbol in stocks[:]:
                    df, stats, th = BacktestStrategy(
                        symbol, tf, col, stop_loss=sl,
                        take_profit=2*sl).ema_cross()
                    _df = pd.concat([_df, df], axis=1)
                    cols = _stats.columns.to_list() + stats.columns.to_list()
                    _stats = pd.concat(
                        [_stats, stats], axis=1, ignore_index=True)
                    _stats.columns = cols
                    cols_th = _th.columns.to_list() + th.columns.to_list()
                    _th = pd.concat([_th, th], axis=1, ignore_index=True)
                    _th.columns = cols_th
                _df.to_sql(name=f'ema_cross_{col.lower()}_{tf.lower()}_{int(sl)}_{int(2*sl)}',
                           con=engine, if_exists="replace")
                # Edit Name Index of Stats
                _index = [x.replace("[%]", "percent")
                          for x in _stats.index.str.lower()]
                # _stats.index = [x.strip().replace(" ", "_") for x in _index]
                _stats = _stats.astype(float).applymap('{:,.2f}'.format)
                # _stats.reset_index(inplace=True)
                _stats.to_sql(name=f'ema_cross_stats_{col.lower()}_{tf.lower()}_{int(sl)}_{int(2*sl)}',
                              con=engine, if_exists="replace")
                _th.to_sql(name=f'trade_history_ema_cross_{col.lower()}_{tf.lower()}_{int(sl)}_{int(2*sl)}',
                           con=engine, if_exists="replace")
                print(f"Backtest EMA_CROSS {tf} {sl} Done..")
    # End EMA_CROSS --------------------------

    # RSI to DATABASE
    for tf in timeframe[:]:
        for col in columns[:]:
            for sl in stop_loss[:]:
                _df = pd.DataFrame()
                _stats = pd.DataFrame()
                _th = pd.DataFrame()
                for symbol in stocks[:]:
                    df, stats, th = BacktestStrategy(
                        symbol, tf, col, stop_loss=sl, take_profit=2*sl).rsi()
                    _df = pd.concat([_df, df], axis=1)
                    cols = _stats.columns.to_list() + stats.columns.to_list()
                    _stats = pd.concat(
                        [_stats, stats], axis=1, ignore_index=True)
                    _stats.columns = cols
                    cols_th = _th.columns.to_list() + th.columns.to_list()
                    _th = pd.concat([_th, th], axis=1, ignore_index=True)
                    _th.columns = cols_th
                _df.to_sql(name=f'rsi_{col.lower()}_{tf.lower()}_{int(sl)}_{int(2*sl)}',
                           con=engine, if_exists="replace")
                # Edit Name Index of Stats
                _index = [x.replace("[%]", "percent")
                          for x in _stats.index.str.lower()]
                # _stats.index = [x.strip().replace(" ", "_") for x in _index]
                _stats = _stats.astype(float).applymap('{:,.2f}'.format)
                # _stats.reset_index(inplace=True)
                _stats.to_sql(name=f'rsi_stats_{col.lower()}_{tf.lower()}_{int(sl)}_{int(2*sl)}',
                              con=engine, if_exists="replace")
                _th.to_sql(name=f'trade_history_rsi_{col.lower()}_{tf.lower()}_{int(sl)}_{int(2*sl)}',
                           con=engine, if_exists="replace")
                print(f"Backtest RSI {tf} {sl} Done..")
    # End RSI --------------------------

    # MACD to DATABASE
    for tf in timeframe[:]:
        for col in columns[:]:
            for sl in stop_loss[:]:
                _df = pd.DataFrame()
                _stats = pd.DataFrame()
                _th = pd.DataFrame()
                for symbol in stocks[:]:
                    df, stats, th = BacktestStrategy(
                        symbol, tf, col, stop_loss=sl, take_profit=2*sl).macd()
                    _df = pd.concat([_df, df], axis=1)
                    cols = _stats.columns.to_list() + stats.columns.to_list()
                    _stats = pd.concat(
                        [_stats, stats], axis=1, ignore_index=True)
                    _stats.columns = cols
                    cols_th = _th.columns.to_list() + th.columns.to_list()
                    _th = pd.concat([_th, th], axis=1, ignore_index=True)
                    _th.columns = cols_th
                _df.to_sql(name=f'macd_{col.lower()}_{tf.lower()}_{int(sl)}_{int(2*sl)}',
                           con=engine, if_exists="replace")
                # Edit Name Index of Stats
                _index = [x.replace("[%]", "percent")
                          for x in _stats.index.str.lower()]
                # _stats.index = [x.strip().replace(" ", "_") for x in _index]
                _stats = _stats.astype(float).applymap('{:,.2f}'.format)
                # _stats.reset_index(inplace=True)
                _stats.to_sql(name=f'macd_stats_{col.lower()}_{tf.lower()}_{int(sl)}_{int(2*sl)}',
                              con=engine, if_exists="replace")
                _th.to_sql(name=f'trade_history_macd_{col.lower()}_{tf.lower()}_{int(sl)}_{int(2*sl)}',
                           con=engine, if_exists="replace")
                print(f"Backtest MACD {tf} {sl} Done..")
    # End MACD

    # ADX to DATABASE
    for tf in timeframe[:]:
        for col in columns[:]:
            for sl in stop_loss[:]:
                _df = pd.DataFrame()
                _stats = pd.DataFrame()
                _th = pd.DataFrame()
                for symbol in stocks[:]:
                    df, stats, th = BacktestStrategy(
                        symbol, tf, col, stop_loss=sl, take_profit=2*sl).adx()
                    _df = pd.concat([_df, df], axis=1)
                    cols = _stats.columns.to_list() + stats.columns.to_list()
                    _stats = pd.concat(
                        [_stats, stats], axis=1, ignore_index=True)
                    _stats.columns = cols
                    cols_th = _th.columns.to_list() + th.columns.to_list()
                    _th = pd.concat([_th, th], axis=1, ignore_index=True)
                    _th.columns = cols_th
                _df.to_sql(name=f'adx_{col.lower()}_{tf.lower()}_{int(sl)}_{int(2*sl)}',
                           con=engine, if_exists="replace")
                # Edit Name Index of Stats
                _index = [x.replace("[%]", "percent")
                          for x in _stats.index.str.lower()]
                # _stats.index = [x.strip().replace(" ", "_") for x in _index]
                _stats = _stats.astype(float).applymap('{:,.2f}'.format)
                # _stats.reset_index(inplace=True)
                _stats.to_sql(name=f'adx_stats_{col.lower()}_{tf.lower()}_{int(sl)}_{int(2*sl)}',
                              con=engine, if_exists="replace")
                _th.to_sql(name=f'trade_history_adx_{col.lower()}_{tf.lower()}_{int(sl)}_{int(2*sl)}',
                           con=engine, if_exists="replace")
                print(f"Backtest ADX {tf} {sl} Done..")
    # End ADX
