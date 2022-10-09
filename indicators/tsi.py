import ta
from indicators.getdata import gethourdata
import pandas as pd

def tsi(df,longlength,shortlength):
    df['tsi'] = ta.momentum.tsi(df.Close,window_fast=longlength,window_slow=shortlength)
    df.dropna(inplace=True)
    return df['tsi'][-1]
#I reccomend lookback to be more than 100 and less than 500
#Example Of running the code: 
#df=gethourdata('BTCUSDT','1h','100')
#tsi(df,25,13)