import ta
import warnings
warnings.filterwarnings("ignore")

def ADX(df):
    k=ta.trend.adx(df['High'], df['Low'], df['Close'], window=14, fillna=False)
    return k[-1]
