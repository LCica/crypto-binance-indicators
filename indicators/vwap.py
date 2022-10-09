from getdata import gethourdata
import pandas as pd

def vwap_first(df):
    q = df.Volume.values
    p = df.Close.values
    return df.assign(vwap=(p * q).cumsum() / q.cumsum())
def vwap(df):
    df = df.groupby(df.index.date, group_keys=False).apply(vwap_first)
    return df['vwap'][-1]
#Example Of running the code: 
#df=gethourdata('BTCUSDT','1h','100')
#vwap(df)