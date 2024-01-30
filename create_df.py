# import os
import time
from typing import List

import pandas as pd
from sqlalchemy import create_engine


# Create Base DataFrame
def create_base_df(
    first_start: str,
    first_end: str,
    second_start: str,
    second_end: str,
    date_list: List[str],
    frequency: str,
) -> pd.DataFrame:
    empty_df = pd.DataFrame()

    for i, input_date in enumerate(date_list):
        index_range1 = pd.date_range(
            start=f"{input_date} {first_start}",
            end=f"{input_date} {first_end}",
            freq=frequency
        )
        index_range2 = pd.date_range(
            start=f"{input_date} {second_start}",
            end=f"{input_date} {second_end}",
            freq=frequency
        )

        empty_df1 = pd.DataFrame(index=index_range1)
        empty_df2 = pd.DataFrame(index=index_range2)

        empty_df = pd.concat([empty_df, empty_df1], axis=1)
        empty_df = pd.concat([empty_df, empty_df2], axis=1)

    empty_df.index = pd.to_datetime(
        empty_df.index).strftime('%Y-%m-%d %H:%M:%S')
    return empty_df


# Merge Stock w/ Symbols (except 1 Day Timeframe)
def merge_stock(
    symbols: List[str],
    params: dict,
) -> dict:

    tf = params["timeframe"]

    date_list = pd.date_range(
        start=params['start_date'],
        end=params['end_date'],
        freq="D"
    )
    base_date = params['base_date']
    partition_data = {}

    base_df = create_base_df(
        first_start=base_date['first_start'],
        first_end=base_date['first_end'],
        second_start=base_date['second_start'],
        second_end=base_date['second_end'],
        date_list=date_list,
        frequency=tf.upper()
    )
    partition_data = {}

    for _, name in enumerate(params['col_names'], start=1):
        partition_data.update({f"merge_{name.lower()}_{tf}": base_df})

    for _, name in enumerate(symbols, start=1):
        stock_name = name
        # log.info(f"Processing {stock_name}")
        df = pd.read_csv(f"./data/{tf}/{name.upper()}_SET.csv")
        df = df.set_index('datetime')
        df.index = pd.to_datetime(df.index).strftime('%Y-%m-%d %H:%M:%S')

        for _, col_name in enumerate(params['col_names'], start=1):
            temp_df = partition_data[f"merge_{col_name.lower()}_{tf}"]
            temp_df = temp_df.join(df[col_name])
            temp_df.rename(
                columns={col_name: f"{stock_name.upper()}"}, inplace=True)
            temp_df = temp_df.dropna(axis=0, how='all')
            partition_data.update(
                {f"merge_{col_name.lower()}_{tf}": temp_df})

    for name in partition_data:
        partition_data[name] = partition_data[name].reset_index()
        partition_data[name].rename(
            columns={'index': 'datetime'}, inplace=True)
        partition_data[name]['datetime'] = pd.to_datetime(
            partition_data[name]['datetime'])
    return partition_data


# Merge Stock w/ Symbols
def merge_stock_1d(
    symbols: List[str],
    params: dict,
    # input_params: dict,
) -> dict:
    index_range = pd.date_range(
        start=params['start_date'],
        end=params['end_date'],
        freq="D"
    )

    partition_data = {}

    for _, name in enumerate(params['col_names'], start=1):
        base_df = pd.DataFrame(index=index_range)
        base_df.index = pd.to_datetime(base_df.index).strftime('%Y-%m-%d')
        partition_data.update({f"merge_{name.lower()}_1d": base_df})

    for _, name in enumerate(symbols, start=1):
        stock_name = name
        df = pd.read_csv(f"./data/1d/{name.upper()}_SET.csv")
        df = df.set_index('datetime')
        df.index = pd.to_datetime(df.index).strftime('%Y-%m-%d')

        for _, col_name in enumerate(params['col_names'], start=1):
            temp_df = partition_data[f"merge_{col_name.lower()}_1d"]
            temp_df = temp_df.join(df[col_name])
            temp_df.rename(
                columns={col_name: f"{stock_name.upper()}"}, inplace=True)
            temp_df = temp_df.dropna(axis=0, how='all')
            partition_data.update(
                {f"merge_{col_name.lower()}_1d": temp_df})

    for name in partition_data:
        partition_data[name] = partition_data[name].reset_index()
        partition_data[name].rename(
            columns={'index': 'datetime'}, inplace=True)
        partition_data[name]['datetime'] = pd.to_datetime(
            partition_data[name]['datetime'])
    return partition_data


# Parameter for Merge
config = {
    "preprocess_1t": {
        "start_date": "2021-09-06",
        "end_date": "2023-10-27",
        "forward_fill": False,
        "base_date": {
            "first_start": "10:00:00",
            "first_end": "12:15:00",
            "second_start": "14:30:00",
            "second_end": "16:30:00",
        },
        "col_names": ["Close", "Volume"],
        "timeframe": "1t",
    },
    "preprocess_5t": {
        "start_date": "2021-09-06",
        "end_date": "2023-10-27",
        "forward_fill": False,
        "base_date": {
            "first_start": "10:00:00",
            "first_end": "12:15:00",
            "second_start": "14:30:00",
            "second_end": "16:30:00",
        },
        "col_names": ["Close", "Volume"],
        "timeframe": "5t",
    },
    "preprocess_15t": {
        "start_date": "2021-09-06",
        "end_date": "2023-10-27",
        "forward_fill": False,
        "base_date": {
            "first_start": "10:00:00",
            "first_end": "12:15:00",
            "second_start": "14:30:00",
            "second_end": "16:30:00",
        },
        "col_names": ["Close", "Volume"],
        "timeframe": "15t",
    },
    "preprocess_1h": {
        "start_date": "2021-09-06",
        "end_date": "2023-10-27",
        "base_date": {
            "first_start": "10:00:00",
            "first_end": "12:00:00",
            "second_start": "14:00:00",
            "second_end": "16:00:00",
        },
        "col_names": ["Close", "Volume"],
        "timeframe": "1h",
    },
    "preprocess_4h": {
        "start_date": "2021-09-06",
        "end_date": "2023-10-27",
        "base_date": {
            "first_start": "09:00:00",
            "first_end": "09:00:00",
            "second_start": "13:00:00",
            "second_end": "13:00:00",
        },
        "col_names": ["Close", "Volume"],
        "timeframe": "4h",
    },
    "preprocess_1d": {
        "start_date": "2021-09-06",
        "end_date": "2023-10-27",
        "col_names": ["Close", "Volume"],
        "timeframe": "1d",
    }
}

start = time.time()

# Fetch Symbol
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

# Create Partition Data for Price & Volume
partition_15t = merge_stock(stocks, config['preprocess_15t'])
partition_1h = merge_stock(stocks, config['preprocess_1h'])
partition_4h = merge_stock(stocks, config['preprocess_4h'])
partition_1d = merge_stock_1d(stocks, config['preprocess_1d'])

# Upload To Database
engine = create_engine('sqlite:///./project.db', echo=False)

for tf in ['15t', '1h', '4h', '1d']:
    stage = f'partition_{tf}'
    partition = eval(stage)
    for k, v in partition.items():
        partition[k].to_sql(
            name=k, con=engine, if_exists='replace')
    print(stage, "done!")

end = time.time()
print(f"Done in {end-start}")
# except ValueError:
#     pass
# partition_15t['merge_volume_15t'].to_sql(name='merge_volume_15t', con=engine)

# if __name__ == "__main__":
#     merge_stock(symbols, config['preprocess_1m'])
