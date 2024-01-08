import itertools
import time
import warnings

import numpy as np
import pandas as pd
from sklearn.metrics import mean_squared_error
from sqlalchemy import create_engine
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.tsa.stattools import acf, adfuller, pacf

# Plot Import
# import matplotlib.pyplot as plt
# from pandas.plotting import lag_plot
# from statsmodels.graphics.tsaplots import plot_acf, plot_pacf

warnings.filterwarnings("ignore")

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


class ARIMACalculatorParams:

    def __init__(self, symbol, timeframe, column):
        self.symbol = symbol
        self.timeframe = timeframe
        self.column = column
        self.data = None
        self.predict_length = 10
        self.load_data()
        self.d, self.p, self.q = -1, -1, -1
        self.train_test_length = (252, 108)
        self.find_d_value()
        self.find_p_value()
        self.find_q_value()
        self.check_value()

    def load_data(self):
        file_path = f"./data/{self.timeframe}/{self.symbol}_SET.csv"
        self.data = pd.read_csv(file_path)

    def find_d_value(self):
        tmp_df = self.data.copy()
        close_df = tmp_df[self.column]
        p_val = adfuller(close_df.dropna(), autolag='AIC')[1]
        self.d = 0
        while p_val >= 0.05:
            close_df = close_df.diff(1)
            adf_res = adfuller(close_df.dropna(), autolag='AIC')
            p_val = adf_res[1]
            self.d += 1
            # close_df.plot(color='green', figsize=(15, 4))
            # plt.legend([f'{self.symbol} Stock price (diff)'])
            # plt.title(f'{self.symbol} Stock values (diff)')
            # plt.show()
        return self.d

    def find_p_value(self):
        tmp_df = self.data.copy()
        close_df = tmp_df[self.column]
        # plt.rcParams.update({'figure.figsize': (10, 4)})
        # plot_pacf(close_df.dropna(), method='ols')
        df_pacf = pacf(close_df.dropna(), method='ols')

        for i in range(0, len(df_pacf)):
            if df_pacf[i] < 1.96 / np.sqrt(len(close_df)):
                self.p = i - 1
                break
        return self.p

    def find_q_value(self):
        tmp_df = self.data.copy()
        close_df = tmp_df[self.column]
        # plt.rcParams.update({'figure.figsize':(10,4)})
        # plot_acf(close_df, fft = True)
        df_acf = acf(close_df, fft=True)

        for i in range(0, len(df_acf)):
            if df_acf[i] < 1.96 / np.sqrt(len(close_df)):
                self.q = i-1
                break
        return self.q
        # When Q Cannot Find -> Using Grid Search

    def check_value(self):

        # Volume Handle
        if self.column == "Volume":
            self.p, self.d, self.q = (1, 1, 1)
            print(f"PDQ Param Done {self.symbol}:{self.timeframe}")
            return

        p = range(0, 3) if self.p == -1 else range(self.p, self.p+1)
        d = range(0, 3) if self.d == -1 else range(self.d, self.d+1)
        q = range(0, 3) if self.q == -1 else range(self.q, self.q+1)

        pdq = list(itertools.product(p, d, q))

        last_aic = 9999999
        param_pdq = ()

        tmp_df = self.data.copy()
        close_df = tmp_df[self.column]

        for param in pdq:
            model = ARIMA(close_df.dropna(), order=param)
            results = model.fit()
            if results.aic < last_aic:
                last_aic = results.aic
                param_pdq = param

        self.p, self.d, self.q = param_pdq
        print(f"PDQ Param Done {self.symbol}:{self.timeframe}")

    def mse_measure(self):
        print(f"MSE Measure... {self.symbol}:{self.timeframe}")
        tmp_df = self.data.copy()
        close_df = tmp_df[self.column]

        # Check Data has Enough Length
        max_length = self.train_test_length[0]+self.train_test_length[1]
        if len(close_df) < max_length:
            self.train_test_length = (
                int(len(close_df)*0.7), len(close_df) - int(len(close_df)*0.7))
        # Select Top 252 For Train 108 For Test (default)
        train_length, test_length = self.train_test_length

        # Split Train Test
        close_df_filter = close_df[len(
            close_df)-(train_length+test_length):len(close_df)]
        close_df_filter = close_df_filter.reset_index().drop(columns='index')

        # Train Test To List
        training_data = [x[0] for x in close_df_filter[: train_length].values]
        test_data = [x[0] for x in close_df_filter[train_length:].values]

        model_predictions = []
        # Measure Predict Test Length
        for time_point in range(len(test_data)):

            model = ARIMA(training_data, order=(
                self.p, self.d, self.q), enforce_stationarity=False)
            model_fit = model.fit()
            output = model_fit.forecast(1)
            yhat = round(output[0], 2)
            model_predictions.append(yhat)
            true_test_value = test_data[time_point]
            training_data.append(true_test_value)

        mse_error = mean_squared_error(test_data, model_predictions)
        return mse_error, test_data, model_predictions

    def forecasting(self):

        print(f"Forecasting... {self.symbol}:{self.timeframe}")
        tmp_df = self.data.copy()
        close_df = tmp_df[self.column]

        # Select Top 252 For Train 108 For Test (default)
        train_length, test_length = self.train_test_length
        # Split Train Test
        close_df_filter = close_df[len(
            close_df)-(train_length+test_length):len(close_df)]
        close_df_filter = close_df_filter.reset_index().drop(columns='index')

        training_data = [x[0] for x in close_df_filter.values]

        # Forecasting
        prediction = []
        # self.predict_length for Forecast
        for _round in range(self.predict_length):
            model = ARIMA(training_data, order=(self.p, self.d, self.q))
            model_fit = model.fit()
            output = model_fit.forecast(1)
            yhat = output[0]
            prediction.append(round(yhat, 4))

        return prediction


if __name__ == "__main__":

    start = time.time()

    engine = create_engine('sqlite:///./project.db', echo=False)

    # Train Model
    partition_data_mse = {}
    forecasting_length = 10
    columns = ["Close", "Volume"]
    for tf in timeframe[:]:
        mse_each_col = {}
        for col in columns[:]:
            mse_each_symbol = {}
            data_each_symbol = {}
            test_data = {}
            model_predictions = {}
            for symbol in stocks[:]:
                model = ARIMACalculatorParams(symbol, tf, col)
                # Add MSE to each_symbol
                model_mse = model.mse_measure()
                mse_each_symbol[symbol] = model_mse[0]
                # Backtesting
                test_data[symbol+"_test"] = model_mse[1]
                model_predictions[symbol+"_predict"] = model_mse[2]
                # Add Data to each_symbol
                data_each_symbol[symbol] = model.forecasting()
            # Add Predict Price to DB with col and tf
            price_df = pd.DataFrame(data=data_each_symbol)
            price_df.to_sql(
                name=f'arima_{col.lower()}_{tf}', con=engine,
                if_exists='replace')
            # Add Backtesting Price to DB with col and tf
            test_df = pd.DataFrame(data=test_data)
            model_predict_df = pd.DataFrame(data=model_predictions)
            backtest_df = pd.concat([test_df, model_predict_df], axis=1)
            backtest_df.to_sql(name=f'arima_{col.lower()}_backtest_{tf}',
                               con=engine,
                               if_exists='replace')
            # Add MSE to each Columns
            mse_each_col[col] = mse_each_symbol
        # Add MSE to each Timeframe
        partition_data_mse[tf] = mse_each_col

        # Add MSE Error to DB
        mse_df = pd.DataFrame(mse_each_col).T.drop(
            index="Volume").reset_index().drop(columns="index")
        mse_df.to_sql(
            name=f'arima_mse_{tf}', con=engine, if_exists='replace')
    # mse_df = pd.DataFrame(index=[0], data=partition_data_mse)

    end = time.time()

    print(f"Done in {end-start}")
    # mse_df.to_sql(name='mse_arima', con=engine, if_exists='replace')
