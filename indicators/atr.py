from indicators.getdata import gethourdata
import numpy as np
import pandas as pd
def atr(df):
    high_low=df['High']-df['Low']
    high_cp= np.abs(df['High']-df['Close'].shift())
    low_cp=np.abs(df['Low']-df['Close'].shift())
    tf=pd.concat([high_low,high_cp,low_cp],axis=1)
    true_range=np.max(tf,axis=1)
    average_true_range=true_range.rolling(9).mean()
    atr_perc=average_true_range/df['Close']
    return (average_true_range[-1],atr_perc[-1])

#Example Of running the code: 
#df=gethourdata('BTCUSDT','1h','100')
#atr(df)