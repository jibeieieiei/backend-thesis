from datetime import timedelta

import pandas as pd
import vectorbtpro as vbt

# SET 50
stocks = [
    'ADVANC', 'AOT', 'AWC', 'BANPU', 'BBL', 'BDMS', 'BEM', 'BGRIM', 'BH',
    'BTS', 'CBG', 'CENTEL', 'COM7', 'CPALL', 'CPF', 'CPN', 'CRC', 'DELTA',
    'EA', 'EGCO', 'GLOBAL', 'GPSC', 'GULF', 'HMPRO', 'INTUCH', 'IVL',
    'KBANK', 'KCE', 'KTB', 'KTC', 'LH', 'MINT', 'MTC', 'OR',
    'OSP', 'PTT', 'PTTEP', 'PTTGC', 'RATCH', 'SAWAD', 'SCB',
    'SCC', 'SCGP', 'TISCO', 'TLI', 'TOP', 'TRUE', 'TTB', 'TU', 'WHA',
]

timeframe = ["5t", "15t"]  # "1d", "1h", "4h", "1t",

end_date = "2023-12-31"
# end_date = None


def update_set50():
    for tf in timeframe:
        for symbol in stocks:
            print(f"Updating {symbol.upper()}:{tf}...")
            # df_old
            df_old = pd.read_csv(f"./data/{tf}/{symbol}_SET.csv")
            df_old.set_index("datetime", inplace=True)
            df_old.index = pd.to_datetime(df_old.index)

            last_current_date = df_old.index[-1]
            update_start_date = (last_current_date +
                                 timedelta(days=1)).strftime("%Y-%m-%d")
            if end_date:
                update_end_date = (
                    pd.to_datetime(end_date) + timedelta(days=1)
                ).strftime("%Y-%m-%d")
            else:
                update_end_date = None

            # df_new
            df_new = pd.DataFrame()
            not_fetch = True
            while not_fetch:
                try:
                    print(f"Fetching {symbol.upper()}:{tf}...")
                    data = vbt.TVData.fetch(
                        f"SET:{symbol.upper()}",
                        timeframe=tf,
                        tz="Asia/Bangkok",
                    )
                    df_new = data.get()
                    df_new = df_new.loc[update_start_date: update_end_date]
                    if df_new.empty:
                        print(f"Already Updated {symbol}:{tf}...")
                    not_fetch = False
                except AttributeError:
                    print(
                        f"Can't Fetch {symbol.upper()}:{tf}...")

            # Concat df_old and df_new
            df = pd.concat([df_old, df_new]) if not df_new.empty else df_old
            df.to_csv(f"./data/{tf}/{symbol}_SET.csv")


if __name__ == "__main__":
    update_set50()