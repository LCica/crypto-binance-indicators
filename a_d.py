from binance import Client
import pandas as pd 

client = Client("TYPE YOUR API KEY HERE","TYPE YOUR SECRET KEY HERE")

#function to get market data for a coin(symbol) and for interval(ex. 1h) for lookback length.
def gethourdata(symbol, interval, lookback):
    frame = pd.DataFrame(client.get_historical_klines(symbol,interval,lookback + 'hours ago UTC'))
    frame=frame.iloc[:,:6]
    frame.columns=['Time','Open','High','Low','Close','Volume']
    frame=frame.set_index('Time')
    frame.index=pd.to_datetime(frame.index, unit='ms')
    frame= frame.astype(float)
    return frame

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
