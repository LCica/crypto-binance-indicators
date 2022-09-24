from getdata import gethourdata
import ta
import pandas as pd
def Percentage_Volume_Oscillator(symbol,interval,lookback,longlength,shortlength):
    df=gethourdata(symbol,interval,lookback)
    df['PVO']=ta.momentum.pvo(df['Volume'],window_slow=longlength,window_fast=shortlength)
    return df['PVO'][-1]
#I reccomend lookback to be more than 100 and less than 500
#Example of calling the code:Percentage_Volume_Oscillator('BTCUSDT','1h','100',10,5)