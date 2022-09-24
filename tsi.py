import ta
from getdata import gethourdata
import pandas as pd

def tsi(symbol,interval,lookback,longlength,shortlength):
    df = gethourdata(symbol, interval, lookback)
    df['tsi'] = ta.momentum.tsi(df.Close,window_fast=longlength,window_slow=shortlength)
    df.dropna(inplace=True)
    return df['tsi'][-1]
#I reccomend lookback to be more than 100 and less than 500
#Example of calling the code:tsi('BTCUSDT','1h','500',25,13)