import pandas as pd
import pandas_datareader as web

def roc(data, n_days):
    '''
    Rate of Change
    '''
    N = data['Close'].diff(n_days)
    D = data['Close'].shift(n_days)
    ROC = pd.Series(N/D,name='Rate of Change')
    data = data.join(ROC)
    return data

if __name__ == '__main__':
    # Retrieve the apple data from Yahoo finance:
    data = web.DataReader('AAPL', data_source='yahoo', start='20140101', end='20160101')
    data = pd.DataFrame(data)

    print(roc(data, 5))