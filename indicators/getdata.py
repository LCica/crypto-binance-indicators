from binance import Client
import pandas as pd
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def gethourdata(symbol, interval, lookback):
    client = Client("TYPE YOUR API KEY HERE","TYPE YOUR SECRET KEY HERE",{"verify": False, "timeout": 20})
    frame = pd.DataFrame(client.get_historical_klines(symbol,interval,lookback + 'hours ago UTC'))
    frame=frame.iloc[:,:6]
    frame.columns=['Time','Open','High','Low','Close','Volume']
    frame=frame.set_index('Time')
    frame.index=pd.to_datetime(frame.index, unit='ms')
    frame= frame.astype(float)
    return frame
    
def get_all_ticker(coin):
    client= Client("TYPE YOUR API KEY HERE","TYPE YOUR SECRET KEY HERE",{"verify": False, "timeout": 20})
    prices = client.get_all_tickers()
    for price in prices:
        if price['symbol']==coin:
            return price['price']