import ta

def mass_index(df,window_fastt,window_sloww):
    return ta.trend.mass_index(df['High'], df['Low'],window_fast = window_fastt,window_slow = window_sloww, fillna=False)[-1]

# Example Of Code: mass_index(gethourdata('BTCUSDT','1h','100'),9,10)