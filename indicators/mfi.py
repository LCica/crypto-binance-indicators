import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
from getdata import gethourdata

def typical_price(df):
  s=[]
  for i in range(0,len(df)):
      s.append((df['Low'][i]+df['High'][i]+df['Close'][i])/3)
  return s
def raw_money_flow(df):
  k=[]
  s=typical_price(df)
  for i in range(0,len(df)):
      k.append(df['Volume'][i]*s[i])
  return k
def poz_neg_flow(df,period):
  tp=typical_price(df)
  rmf=raw_money_flow(df)
  poz=0
  neg=0
  for i in range(len(tp)-period,len(tp)):
    if tp[i-1]>tp[i]:
      neg+=float(rmf[i])
    elif tp[i-1]<tp[i]:
      poz+=float(rmf[i])
  return [poz,neg]
def money_ratio(df,period):
  k=poz_neg_flow(df,period)
  return k[0]/k[1]
def mfi(df,period):
  return 100-100/(1+money_ratio(df,period))

#Example Of running the code: 
#df=gethourdata('BTCUSDT','1h','100')
#mfi(df,14)