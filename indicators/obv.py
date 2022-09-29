from getdata import gethourdata

def obv(symbol,interval,lookback):
    df=gethourdata(symbol,interval,lookback)
    k=float(df['Volume'][0])
    for i in range(1,len(df['Volume'])):
        if df['Close'][i]>df['Close'][i-1]:
            k+=float(df['Volume'][i])
        elif df['Close'][i]<df['Close'][i-1]:
            k-=float(df['Volume'][i])
    return k

#Example Of Running The Code: obv('BTCUSDT','1h','1000')