import pandas as pd
import pandas_datareader as web

# Compute the Bollinger Bands
def bolling_bands(data, ndays):
    # pandas 0.2.3 before
    # MA = pd.Series(pd.rolling_mean(data['Close'], ndays))
    # SD = pd.Series(pd.rolling_std(data['Close'], ndays))

    # pandas since 0.23
    MA = pd.Series(data['Close'].rolling(ndays).mean())
    SD = pd.Series(data['Close'].rolling(ndays).std())

    b1 = MA + (2 * SD)
    B1 = pd.Series(b1, name='Upper Bolling Band')
    data = data.join(B1)

    b2 = MA - (2 * SD)
    B2 = pd.Series(b2, name='Lower Bolling Band')
    data = data.join(B2)

    return data

if __name__ == '__main__':
    # Retrieve the apple data from Yahoo finance:
    data = web.DataReader('AAPL', data_source='yahoo', start='20140101', end='20160101')
    data = pd.DataFrame(data)
    print(data.head(10))

    # Compute the Bollinger Bands for AAPL using the 50-day Moving average
    n = 50
    apple_bollinger_bands = bolling_bands(data, n)
    print(apple_bollinger_bands)
