import pandas as pd
import pandas_datareader as web


# Simple Moving Average
def SMA(data, n_days):
    # SMA = pd.Series(pd.rolling_mean(data['Close'], n_days), name='SMA')
    SMA = pd.Series(data['Close'].rolling(n_days).mean(), name='SMA')
    data_new = data.join(SMA)
    return data_new


# Exponentially-weighted Moving Average
def EWMA(data, n_days):
    # EMA = pd.Series(pd.ewma(data['Close'], span=n_days, min_periods=n_days - 1),
    #                 name='EWMA_' + str(n_days))
    EMA = pd.Series(pd.DataFrame.ewm(data['Close'], span=n_days, min_periods=n_days - 1).mean(),
              name='EWMA_' + str(n_days))
    data = data.join(EMA)
    return data

if __name__ == '__main__':
    # Retrieve the apple data from Yahoo finance:
    data = web.DataReader('AAPL', data_source='yahoo', start='20140101', end='20160101')
    data = pd.DataFrame(data)
    # print(data.head(10))

    # Compute the 50-day SMA for AAPL
    n = 50
    sma_apple = SMA(data, n)
    sma_apple = sma_apple.dropna()
    # print(sma_apple)
    sma = sma_apple['SMA']
    print(sma)

    # Compute the 200-day EWMA for AAPL
    ew = 200
    ewma_apple = EWMA(data, ew)
    ewma_apple = ewma_apple.dropna()
    ewma = ewma_apple['EWMA_200']
    print(ewma)
