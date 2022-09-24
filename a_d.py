import pandas as pd 
from getdata import gethourdata

def mfm(df):
    df['MFM']=(2*df['Close']-df['Low']-df['High'])/(df['High']-df['Low'])
    df['MFV']=df['MFM']*df['Volume']
def a_d(symbol, interval, lookback):
    df=gethourdata(symbol, interval, lookback)
    mfm(df)
    ad=[df['MFV'][0]]
    for i in range(1,len(df['Open'])):
        k=ad[i-1]+df['MFV'][i]
        ad.append(k)
    return ad[-1]
#Example of calling the code: a_d('BTCUSDT','1h','100')
