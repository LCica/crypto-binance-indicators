import ta
from indicators.getdata import gethourdata

def macd(df):
    df['macd'] = ta.trend.macd(df.Close)
    df['macd_signal']=ta.trend.macd_signal(df.Close)
    df.dropna(inplace=True)
    return (df['macd'][-1],df['macd_signal'][-1])


#Example Of running the code: 
#df=gethourdata('BTCUSDT','1h','100')
#macd(df)