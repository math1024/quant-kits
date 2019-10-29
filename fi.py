import pandas as pd
import pandas_datareader as web


def force_index(data, n_days):
    '''
    compute Force Index 指示上升或下降趋势大小
    A simple price-and-volume oscillator
    '''
    FI = pd.Series(data['Close'].diff(n_days) * data['Volume'], name ='ForceIndex')
    data = data.join(FI)
    return data

if __name__ == '__main__':
    data = web.DataReader('AAPL', data_source='yahoo', start='20140101', end='20160101')
    data = pd.DataFrame(data)

    n = 1
    AAPL_ForceIndex = force_index(data, n)
    print(AAPL_ForceIndex)