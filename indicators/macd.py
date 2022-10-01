import ta
from indicators.getdata import gethourdata

def macd(df):
    df['macd'] = ta.trend.macd(df.Close)
    df.dropna(inplace=True)
    return df['macd'][-1]


#EXAMPLE OF CODE: macd(gethourdata('BTCUSDT','1h','100'))