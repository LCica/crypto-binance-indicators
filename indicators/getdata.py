from binance import Client
import pandas as pd


def gethourdata(symbol, interval, lookback):
    client = Client("TYPE YOUR API KEY HERE","TYPE YOUR SECRET KEY HERE")
    frame = pd.DataFrame(client.get_historical_klines(symbol,interval,lookback + 'hours ago UTC'))
    frame=frame.iloc[:,:6]
    frame.columns=['Time','Open','High','Low','Close','Volume']
    frame=frame.set_index('Time')
    frame.index=pd.to_datetime(frame.index, unit='ms')
    frame= frame.astype(float)
    return frame

def get_all_ticker(coin):
    client=Client("TYPE YOUR API KEY HERE","TYPE YOUR SECRET KEY HERE")
    prices = client.get_all_tickers()
    for price in prices:
        if price['symbol']==coin:
            return price['price']