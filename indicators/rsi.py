import pandas as pd 
import ta
from indicators.getdata import gethourdata

def rsi(df,length):
    df['rsi'] = ta.momentum.rsi(df.Close, window=length)
    df.dropna(inplace=True)
    return df['rsi'][-1]

#Example Of running the code: 
#df=gethourdata('BTCUSDT','1h','100')
#rsi(df,9)
