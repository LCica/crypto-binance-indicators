from binance import Client
client = Client("TYPE YOUR API KEY HERE","TYPE YOUR SECRET KEY HERE")
def check_balance(symbol):                                                                  
    info = client.get_account()
    df = info["balances"]
    i=[]
    for coin in df:
        if float(coin['free'])>1:
            if str(coin['asset'])[:2] not in 'LD':
                i.append([coin['asset'],coin['free']])
    for k in range(0,len(i)-1):
        if i[k][0]==symbol:
            return i[k][1]
