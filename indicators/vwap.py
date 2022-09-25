from getdata import gethourdata
import pandas as pd

def vwap_first(df):
    q = df.Volume.values
    p = df.Close.values
    return df.assign(vwap=(p * q).cumsum() / q.cumsum())
def vwap(symbol,interval,lookback):
    df=gethourdata(symbol,interval,lookback)
    df = df.groupby(df.index.date, group_keys=False).apply(vwap_first)
    return df['vwap'][-1]
#Example of calling the code:vwap('BTCUSDT','1h','500')