from binance import Client
import pandas as pd 
import ta
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

def macd(symbol,interval,lookback):
    df = gethourdata(symbol, interval, lookback)
    df['macd'] = ta.trend.macd(df.Close)
    df.dropna(inplace=True)
    return df['macd'][-1]


#EXAMPLE OF CODE: macd('BTCUSDT','1h','100')