import pandas as pd 
import ta
from indicators.getdata import gethourdata

def rsi(symbol,interval,lookback,length):
    df = gethourdata(symbol, interval, lookback)
    df['rsi'] = ta.momentum.rsi(df.Close, window=length)
    df.dropna(inplace=True)
    return df['rsi'][-1]

#EXAMPLE OF CODE: rsi('BTCUSDT','1h','30',9)
