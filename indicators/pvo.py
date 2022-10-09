from indicators.getdata import gethourdata
import ta
import pandas as pd
def Percentage_Volume_Oscillator(df,longlength,shortlength,signallength):
    df['PVO']=ta.momentum.pvo(df['Volume'],window_slow=longlength,window_fast=shortlength)
    df['PVO_signal']=ta.momentum.pvo_signal(df['Volume'],window_slow=longlength,window_fast=shortlength,window_sign=signallength)
    return (df['PVO'][-1],df['PVO_signal'][-1])


#I reccomend lookback to be more than 100 and less than 500
#Example Of running the code: 
#df=gethourdata('BTCUSDT','1h','100')
#Percentage_Volume_Oscillator(df,10,5,9)
