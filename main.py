# import time

# import sqlalchemy
from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware

# from pydantic import BaseModel, Field
from sqlalchemy import select

# from sqlalchemy import MetaData, Table, and_, create_engine,
from sqlalchemy.orm import Session

# import create_df
import models
from database import SessionLocal, engine

# SET50
from stocks_symbol import stocks

# from fastapi import HTTPException

app = FastAPI()

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

models.Base.metadata.create_all(bind=engine)


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


@app.get("/prediction_{prediction_model}_{timeframe}_{symbol}_{column}")
def prediction(db: Session = Depends(get_db),
               prediction_model: str = "ARIMA",
               timeframe: str = "15t",
               symbol: str = "ADVANC",
               column: str = "Close"):
    # Handle error
    prediction_model = prediction_model.upper()
    column = column.capitalize()
    timeframe = timeframe.upper()
    symbol = symbol.upper()
    # End Handle error
    model_price = eval(f"models.Merge{column}{timeframe}")
    tmp_price = eval(f"models.Merge{column}{timeframe}.{symbol}")
    datetime_price = eval(f"models.Merge{column}{timeframe}.datetime")
    # Price
    stmt = select(
        tmp_price,
        datetime_price
    ).select_from(model_price)
    res = db.execute(stmt)
    price_list = []
    for i in res:
        price = i._mapping
        price_list.append(price)
    # Prediction
    model_predict = eval(
        f"models.{prediction_model}{column}{timeframe}")
    tmp_predict = eval(
        f"models.{prediction_model}{column}{timeframe}.{symbol}")
    stmt = select(
        tmp_predict,
    ).select_from(model_predict)
    res = db.execute(stmt)
    for i in res:
        price = i._mapping
        price_list.append(price)

    return price_list


@app.get("/mse_error_{prediction_model}_{timeframe}_{symbol}")
def mse_error(db: Session = Depends(get_db),
              prediction_model: str = "ARIMA",
              timeframe: str = "15t",
              symbol: str = "ADVANC"):
    # Handle Error
    prediction_model = prediction_model.upper()
    timeframe = timeframe.upper()
    symbol = symbol.upper()
    # End Handle Error
    model_name = f"models.{prediction_model}MSE{timeframe}"
    model_error = eval(model_name)
    filter_model = eval(f"{model_name}.{symbol}")
    stmt = select(
        filter_model
    ).select_from(model_error)
    res = db.execute(stmt)
    return [x._mapping for x in res]


@app.get('/backtest_model_{prediction_model}_{timeframe}_{symbol}_{column}')
def backtest_model(db: Session = Depends(get_db),
                   prediction_model: str = "ARIMA",
                   timeframe: str = "15t",
                   symbol: str = "ADVANC",
                   column: str = "Close"
                   ):
    # Handle Error
    prediction_model, timeframe, symbol, column = prediction_model.upper(
    ), timeframe.upper(), symbol.upper(), column.capitalize()
    # End Handle Error
    # Model
    model_name = "models."+prediction_model+column+"Backtest"+timeframe
    model_backtest = eval(model_name)
    filter_test = eval(f"{model_name}.{symbol}_test")
    filter_predict = eval(f"{model_name}.{symbol}_predict")
    stmt = select(
        filter_test,
        filter_predict,
    ).select_from(model_backtest)
    res = db.execute(stmt)

    return [x._mapping for x in res]


@app.get('/backtest_strategy_{strategy}_{timeframe}_{symbol}_{column}')
def backtest_strategy(db: Session = Depends(get_db),
                      strategy: str = "EMACROSS",
                      timeframe: str = "15T",
                      symbol: str = "ADVANC",
                      column: str = "Close"):
    strategy, timeframe, symbol, column = strategy.upper(
    ), timeframe.upper(), symbol.upper(), column.capitalize()

    model_name = "models."+strategy+column+timeframe
    model_strategy = eval(model_name)
    filter1 = eval(model_name+f'.{symbol}_datetime')
    filter2 = eval(model_name+f'.{symbol}_close')
    filter3 = eval(model_name+f'.{symbol}_green_signal')
    filter4 = eval(model_name+f'.{symbol}_red_signal')
    filter5 = eval(model_name+f'.{symbol}_ema_short')
    filter6 = eval(model_name+f'.{symbol}_ema_long')
    stmt = select(
        filter1, filter2, filter3, filter4, filter5, filter6
    ).select_from(model_strategy)
    res = db.execute(stmt)

    return [x._mapping for x in res]


@app.get('/backtest_stats_{strategy}_{timeframe}_{symbol}_{column}')
def backtest_stats(db: Session = Depends(get_db),
                   strategy: str = "EMACROSS",
                   timeframe: str = "15T",
                   symbol: str = "ADVANC",
                   column: str = "Close"):

    strategy, timeframe, symbol, column = strategy.upper(
    ), timeframe.upper(), symbol.upper(), column.capitalize()

    model_name = "models."+strategy+"Stats"+column+timeframe
    model_stats = eval(model_name)
    filter_index = eval(model_name+".index")
    filter = eval(model_name+f".{symbol}_stats")
    print(filter_index)
    stmt = select(
        filter_index,
        filter
    ).select_from(model_stats)
    res = db.execute(stmt)

    return [x._mapping for x in res]


@app.get('/trading_stats_compare_{symbol}')
def trading_stats_compare(db: Session = Depends(get_db),
                          symbol: str = "ADVANC"):
    symbol = symbol.upper()

    model_name = "models.CompareTable"
    model_compare = eval(model_name)
    filter_index = eval(model_name+".index")
    filter_symbol = eval(model_name+f".{symbol}_fund")
    stmt = select(
        filter_index,
        filter_symbol
    ).select_from(model_compare)
    res = db.execute(stmt)

    return [x._mapping for x in res]


@app.get('/specific_info_{symbol}')
def specific_info(db: Session = Depends(get_db),
                  symbol: str = "ADVANC"):
    symbol = symbol.upper()

    model_name = "models.SpecificInfo"
    model_spec = eval(model_name)
    filter_index = eval(model_name+".index")
    filter_symbol = eval(model_name+f".{symbol}")
    stmt = select(
        filter_index,
        filter_symbol
    ).select_from(model_spec)
    res = db.execute(stmt)

    return [x._mapping for x in res]


@app.get('/stocks_symbols')
def stocks_symbol_set50():
    return {'stocks': stocks}
