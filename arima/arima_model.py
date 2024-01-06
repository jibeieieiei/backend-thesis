import itertools
import os
import sys
import warnings

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from pandas.plotting import lag_plot
from sklearn.metrics import mean_squared_error
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.tsa.stattools import acf, adfuller, pacf

warnings.filterwarnings("ignore")

# SET 50
stocks = [
    'ADVANC', 'AOT', 'AWC', 'BANPU', 'BBL', 'BDMS', 'BEM', 'BGRIM', 'BH',
    'BTS', 'CBG', 'CENTEL', 'COM7', 'CPALL', 'CPF', 'CPN', 'CRC', 'DELTA',
    'EA', 'EGCO', 'GLOBAL', 'GPSC', 'GULF', 'HMPRO', 'INTUCH', 'IVL',
    'KBANK', 'KCE', 'KTB', 'KTC', 'LH', 'MINT', 'MTC', 'OR',
    'OSP', 'PTT', 'PTTEP', 'PTTGC', 'RATCH', 'SAWAD', 'SCB',
    'SCC', 'SCGP', 'TISCO', 'TLI', 'TOP', 'TRUE', 'TTB', 'TU', 'WHA',
]


tf = ["15t"]


class ARIMACalculatorParams:

    def __init__(self, stock_symbol, timeframe):
        self.stock_symbol = stock_symbol
        self.timeframe = timeframe
        self.data = None
        self.load_data()
        self.d, self.p, self.q = -1, -1, -1
        self.find_d_value()
        self.find_p_value()
        self.find_q_value()

    def load_data(self):
        file_path = f"../data/{self.timeframe}/{self.stock_symbol}_SET.csv"
        self.data = pd.read_csv(file_path)

    def find_d_value(self):
        tmp_df = self.data.copy()
        close_df = tmp_df['Close']
        p_val = adfuller(close_df.dropna(), autolag='AIC')[1]
        self.d = 0
        while p_val >= 0.05:
            close_df = close_df.diff(1)
            adf_res = adfuller(close_df.dropna(), autolag='AIC')
            p_val = adf_res[1]
            self.d += 1
            # close_df.plot(color='green', figsize=(15, 4))
            # plt.legend([f'{self.stock_symbol} Stock price (diff)'])
            # plt.title(f'{self.stock_symbol} Stock values (diff)')
            # plt.show()
        return self.d

    def find_p_value(self):
        tmp_df = self.data.copy()
        close_df = tmp_df['Close']
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
        close_df = tmp_df['Close']
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
        p = range(0, 3) if self.p == -1 else range(self.p, self.p+1)
        d = range(0, 3) if self.d == -1 else range(self.d, self.d+1)
        q = range(0, 3) if self.q == -1 else range(self.q, self.q+1)

        pdq = list(itertools.product(p, d, q))
        # print(pdq)

        last_aic = 999999
        param_pdq = ()

        tmp_df = self.data.copy()
        close_df = tmp_df['Close']

        for param in pdq:
            model = ARIMA(close_df.dropna(), order=param)
            results = model.fit()
            print('Order = {}'.format(param))
            print('AIC = {}'.format(results.aic))
            if results.aic < last_aic:
                last_aic = results.aic
                param_pdq = param
        return param_pdq

    def train_data(self):
        # partition_data_prediction = {}
        # partition_data_mse = {}
        # print(f"Timeframe = {tf}, SYMBOL = {symbol}..............")
        # df= pd.read_csv(f"./data/{tf}/{symbol}_SET.csv")
        # if tf == "15t":
        #     train_data = df[(df['datetime'] > '2023-03-01') & (df['datetime'] < '2023-10-01')]
        #     training_data = train_data['Close'].values
        #     test_data = df[(df['datetime'] >= '2023-10-01')]
        #     test_data = test_data['Close'].values
        # history = [x for x in training_data]
        # model_predictions = []
        # _prediction = []
        # N_test_observations = len(test_data)
        # for time_point in range(N_test_observations):
        #     # print(f'round ={time_point}')
        #     model = ARIMA(history, order=(5,2,2))
        #     model_fit = model.fit()
        #     output = model_fit.forecast(10)
        #     yhat = round(output[0],2)
        #     print("output = ", output)
        #     model_predictions.append(yhat)
        #     true_test_value = test_data[time_point]
        #     history.append(yhat)
        #     # history.append(round(output[1],2))
        # MSE_error = mean_squared_error(test_data, model_predictions)
        # print('Testing Mean Squared Error is {}'.format(MSE_error))
        # for period_predict in range(0,2):
        #     model = ARIMA(history, order=(5,2,2))
        #     model_fit = model.fit()
        #     output = model_fit.forecast()
        #     yhat = output[0]
        #     print("y_hat= ", output)
        #     _prediction.append(yhat)
        # partition_data_mse[symbol] = MSE_error
        # partition_data_prediction[symbol] = _prediction
        pass


for stock_symbol in stocks[1:2]:
    stock_analysis = ARIMACalculatorParams(stock_symbol, tf[0])
    print(stock_analysis.d, stock_analysis.p, stock_analysis.q)
    print(stock_analysis.check_value())
    # print(f"D value for {stock_symbol}: {d_value}")
