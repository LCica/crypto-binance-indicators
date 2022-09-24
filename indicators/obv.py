from binance import Client
import pandas as pd
import numpy as np
import time
client = Client("EykUpOPocgOeUQMgRZKZQXLj4HyMVa9LkSdOlfh1qYjpv6S64endqOVs566ZQkIf", "kONVCNnP0YBfIuAo0FisFZzUjERcgXIOd2Sa2QoL6tKqPxgEzEW5fcawRJrtF5WN")

#function to get market data for a coin(symbol) and for interval(ex. 1h) for lookback length.
def gethourdata(symbol, interval, lookback):
    frame = pd.DataFrame(client.get_historical_klines(symbol,interval,lookback + 'hours ago UTC'))
    frame=frame.iloc[:,:6]
    frame.columns=['Time','Open','High','Low','Close','Volume']
    frame=frame.set_index('Time')
    frame.index=pd.to_datetime(frame.index, unit='ms')
    frame= frame.astype(float)
    return frame

def on_balance_volume(data, trend_periods=21, close_col='Close', vol_col='Volume'):
    for index, row in data.iterrows():
        if index > 0:
            last_obv = data.at[index - 1, 'obv']
            if row[close_col] > data.at[index - 1, close_col]:
                current_obv = last_obv + row[vol_col]
            elif row[close_col] < data.at[index - 1, close_col]:
                current_obv = last_obv - row[vol_col]
            else:
                current_obv = last_obv
        else:
            last_obv = 0
            current_obv = row[vol_col]

        data.set_value(index, 'obv', current_obv)

    data['obv_ema' + str(trend_periods)] = data['obv'].ewm(ignore_na=False, min_periods=0, com=trend_periods, adjust=True).mean()
    
    return data

while True:
    print(on_balance_volume(('BTCUSDT','1h','100')))
    time.sleep(1)