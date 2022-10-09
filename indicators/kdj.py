from indicators.getdata import gethourdata
#finding lowest 'Low' on an interval length 9. 
def low(df,i):
    lowest=df['Low'][i-1]
    for i in range(i-9,i-1):
        if df['Low'][i]<lowest:
            lowest=df['Low'][i]
    return lowest
#finding  highest 'High' on an interval length 9. 
def high(df,i):
    high=df.High[i-1]
    for i in range(i-9,i-1):
        if df.High[i]>high:
            high=df.High[i]
    return high
#calculating RSV 
def rsv(list,i):
    return 100*(list['Close'][i-1]-low(list,i))/(high(list,i)-low(list,i))
#final function calculating kdj 
def kdj(df):
    k=[]
    d=[]
    j=[]
    for i in range(0,10):
        k.append(50)
        d.append(50)
    for j in range(10,len(df.Open)+1):
        t=float(rsv(df,j))
        z=float(k[j-1])
        x=2*z/3+t/3
        p=float(d[j-1])
        k.append(x)
        d.append(2*p/3+x/3)
        j=3*k[-1]-2*d[-1]
    return (k[-1],d[-1],j)

#Example Of running the code: 
#df=gethourdata('BTCUSDT','1h','100')
#kdj(df)

