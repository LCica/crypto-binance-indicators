from cmath import nan
from binance import Client
import pandas as pd 

client = Client("TYPE YOUR API KEY HERE","TYPE YOUR SECRET KEY HERE")

def gethourdata(symbol, interval, lookback):
    frame = pd.DataFrame(client.get_historical_klines(symbol,interval,lookback + 'hours ago UTC'))
    frame=frame.iloc[:,:6]
    frame.columns=['Time','Open','High','Low','Close','Volume']
    frame=frame.set_index('Time')
    frame.index=pd.to_datetime(frame.index, unit='ms')
    frame= frame.astype(float)
    return frame

   

def Ichimoku_Cloud(symbol, interval, lookback):
    df=gethourdata('BTCUSDT','1h','100')
    high9=df.High.rolling(9).max()
    high26=df.High.rolling(26).max()
    high52=df.High.rolling(52).max()
    low9=df.Low.rolling(9).min()
    low26=df.Low.rolling(26).min()
    low52=df.Low.rolling(52).min()
    df['tenkan_sen']=((high9+low9)/2).shift(26)
    df['kijun_sen']=((high26+low26)/2).shift(26)
    df['senkou_A']=((df.tenkan_sen+df.kijun_sen)/2)
    df['senkou_B']=((high52+low52)/2)
    df['chikou']=df.Close.shift(-26)
    df=df.iloc[26:]
    return df
print(Ichimoku_Cloud('BTCUSDT','1h','100'))   
#Example of calling the code:Ichimoku_Cloud('BTCUSDT','1h','100')

def cloud_color(symbol, interval, lookback):
    df=Ichimoku_Cloud(symbol, interval, lookback)
    k=[]
    for i in range(0,len(df['Open'])):
        if float(df['senkou_A'][i])>=float(df['senkou_B'][i]):
            k.append('green')
        if float(df['senkou_A'][i])<float(df['senkou_B'][i]):
            k.append('red')
    return k