import pandas as pd 
import ta
from getdata import gethourdata

def macd(symbol,interval,lookback):
    df = gethourdata(symbol, interval, lookback)
    df['macd'] = ta.trend.macd(df.Close)
    df.dropna(inplace=True)
    return df['macd'][-1]


#EXAMPLE OF CODE: macd('BTCUSDT','1h','100')