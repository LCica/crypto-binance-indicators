from getdata import gethourdata

def obv(df):
    k=float(df['Volume'][0])
    for i in range(1,len(df['Volume'])):
        if df['Close'][i]>df['Close'][i-1]:
            k+=float(df['Volume'][i])
        elif df['Close'][i]<df['Close'][i-1]:
            k-=float(df['Volume'][i])
    return k

#Example Of running the code: 
#df=gethourdata('BTCUSDT','1h','100')
#obv(df)