# import math
import time
import warnings

# import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import MinMaxScaler
from sqlalchemy import create_engine
from tensorflow.keras.layers import LSTM, Dense
from tensorflow.keras.models import Sequential, load_model

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

columns = ["Close", "Volume"]


class LSTMPredict:

    def __init__(self, symbol, timeframe, column, load=True):
        self.symbol = symbol
        self.timeframe = timeframe
        self.column = column
        self.data = None
        self.predict_length = 10
        self.length_by_tf = {'15t': 11683, '1h': 4862, '4h': 1394, '1d': 698}
        self.load_data()
        self.train_test_length = (252, 252)
        self.scaler = MinMaxScaler()
        # Train Test Split
        self.train_data, self.test_data = self.train_test_split()
        self.X_train, self.Y_train = self.create_dataset(self.train_data, 100)
        self.X_test, self.Y_test = self.create_dataset(self.test_data, 100)
        self.rounds = 10
        if load:
            self.model = self._load_model()
        else:
            self.model = self.fitting_model()
        self.mse_error, self.data_test, self.data_predict = self.mse_measure()
        self.predict = self.forecasting()

    def load_data(self):
        file_path = f"./data/{self.timeframe}/{self.symbol}_SET.csv"
        self.data = pd.read_csv(file_path)

    def data_preprocess(self):
        df = self.data
        df2 = df.reset_index()[self.column]
        df2 = self.scaler.fit_transform(np.array(df2).reshape(-1, 1))
        return df2

    def train_test_split(self):
        length = self.length_by_tf[self.timeframe]
        df2 = self.data_preprocess()
        df2 = df2[len(df2)-length:]
        # Split Train Test
        train_size = int(len(df2)*0.65)
        train_data, test_data = df2[0:train_size,
                                    :], df2[train_size:len(df2), :1]
        return train_data, test_data

    def create_dataset(self, dataset, time_step=1):
        dataX, dataY = [], []
        for i in range(len(dataset)-time_step-1):
            a = dataset[i:(i+time_step), 0]
            dataX.append(a)
            dataY.append(dataset[i + time_step, 0])
        return np.array(dataX), np.array(dataY)

    def fitting_model(self):
        # Define train, test
        X_train, Y_train = self.X_train, self.Y_train
        X_test, Y_test = self.X_test, self.Y_test
        # Creating Model
        model = Sequential()
        model.add(LSTM(50, return_sequences=True,
                  input_shape=(X_train.shape[1], 1)))
        model.add(LSTM(50, return_sequences=True))
        model.add(LSTM(50))
        model.add(Dense(1))
        model.compile(loss='mean_squared_error', optimizer='adam')
        # Fitting Model
        model.fit(X_train, Y_train, validation_data=(
            X_test, Y_test), epochs=20, batch_size=64, verbose=1)
        model.save(
            f"lstm/models/{self.column.lower()}/{self.timeframe}/{self.symbol}_{self.timeframe}.h5")
        print(f"Save {self.symbol} done..")
        return model

    def _load_model(self):
        # Load
        model = load_model(
            f"lstm/models/{self.column.lower()}/{self.timeframe}/{self.symbol}_{self.timeframe}.h5")
        return model

    def forecasting(self):
        print(f"Forecasting(LSTM)... {self.symbol}:{self.timeframe}")
        # Loop for test self.rounds rounds
        rounds = self.rounds
        X_test = self.X_test
        tmp = X_test[len(X_test)-1:, :]
        model = self.model
        test_predict = []
        for r in range(rounds):
            next_predict = model.predict(tmp)
            test_predict.append(next_predict[0][0])
            tmp = np.append(tmp[:, r+1:tmp.shape[1]], next_predict, axis=1)
        # Inverse Transform
        test_predict = self.scaler.inverse_transform(
            np.array(test_predict).reshape(-1, 1))
        test_predict = [x.tolist()[0] for x in test_predict]
        return test_predict

    def mse_measure(self):
        X_train, Y_train = self.X_train, self.Y_train
        model = self.model
        scaler = self.scaler
        train_predict = model.predict(X_train)
        data_test = scaler.inverse_transform(Y_train.reshape(-1, 1))
        data_test = [x[0] for x in data_test.tolist()]
        data_predict = scaler.inverse_transform(train_predict)
        data_predict = [round(x[0], 2) for x in data_predict.tolist()]
        mse_error = mean_squared_error(data_test, data_predict)
        return round(mse_error, 4), data_test, data_predict


if __name__ == "__main__":
    start = time.time()

    engine = create_engine('sqlite:///./project.db', echo=False)

    for tf in timeframe[:]:
        lstm_data = {}
        lstm_backtest_test = {}
        lstm_backtest_predict = {}
        lstm_mse = {}
        for col in columns[:]:
            for symbol in stocks[:]:
                model = LSTMPredict(symbol, tf, col)
                print(f"{tf} {symbol} {col} \n\n\n\n")
                # Predict
                lstm_data[symbol] = model.predict
                # Backtest
                lstm_backtest_test[symbol+"_test"] = model.data_test
                lstm_backtest_predict[symbol+"_predict"] = model.data_predict
                # End Backtest
                # MSE
                lstm_mse[symbol] = [model.mse_error]
            # Predict df
            lstm_df = pd.DataFrame(data=lstm_data)
            lstm_df.to_sql(name=f'lstm_{col.lower()}_{tf.lower()}',
                           con=engine, if_exists="replace")
            # End Predict df
            # Now only Close
            if col == 'Close':
                # Backtest df
                backtest_test_df = pd.DataFrame(data=lstm_backtest_test)
                backtest_predict_df = pd.DataFrame(data=lstm_backtest_predict)
                backtest_df = pd.concat(
                    [backtest_test_df, backtest_predict_df], axis=1)
                name_backtest = f'lstm_{col.lower()}_backtest_{tf.lower()}'
                backtest_df.to_sql(name=name_backtest,
                                   con=engine, if_exists="replace")
                # End Backtest df
                # MSE df
                lstm_mse_df = pd.DataFrame(data=lstm_mse)
                name_mse_df = f'lstm_mse_{tf}'
                lstm_mse_df.to_sql(name=name_mse_df,
                                   con=engine, if_exists="replace")

    end = time.time()

    print(f"Done in {end-start}")
