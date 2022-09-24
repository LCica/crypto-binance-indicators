import pandas as pd 
from getdata import gethourdata


def sma(data, window):
    return(data.rolling(window = window).mean())

#bollinger bands calculation source is for ex.:'Close' or 'Open'(just copy and paste into function call.)

def bollinger_band(symbol, interval, lookback,source,length, nstd=2):
    df=gethourdata(symbol, interval, lookback)
    data=df[source]
    df['sma'] = sma(df[source], 20)
    std = data.rolling(window = length).std()
    upper_band = df['sma'] + std * nstd
    lower_band = df['sma'] - std * nstd
    df['upper_band'], df['lower_band'] =upper_band,lower_band   
    return (df['upper_band'][-1], df['lower_band'][-1])

#Example of calling the code: bollinger_band('BTCUSDT','1h','100','Close',20, 2)       