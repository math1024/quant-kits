import pandas as pd
import pandas_datareader as web
import matplotlib.pyplot as plt

from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

def evm(data, n_days):
    '''
    Ease of Movement 价格与成交量的变化结合成一个波动指标来反映变动状况
    An indicator that compares volume and price to identify significant moves
    '''
    dm = ((data['High'] + data['Low'])/2) - ((data['High'].shift(1) + data['Low'].shift(1))/2)
    br = (data['Volume'] / 100000000) / ((data['High'] - data['Low']))
    EVM = dm / br
    EVM_MA = pd.Series(data['Close'].rolling(n_days).mean(), name = 'EVM')
    data = data.join(EVM_MA)
    return data

if __name__ == '__main__':
    # Retrieve the apple data from Yahoo finance:
    data = web.DataReader('AAPL', data_source='yahoo', start='20140101', end='20160101')
    data = pd.DataFrame(data)

    n = 14
    AAPL_EVM = evm(data, n)
    EVM = AAPL_EVM['EVM']

    # Plotting the Price Series chart and the Ease Of Movement below
    fig = plt.figure(figsize=(7, 5))
    ax = fig.add_subplot(2, 1, 1)
    ax.set_xticklabels([])
    plt.plot(data['Close'], lw=1)
    plt.title('AAPL Price Chart')
    plt.ylabel('Close Price')
    plt.grid(True)
    bx = fig.add_subplot(2, 1, 2)
    plt.plot(EVM, 'k', lw=0.75, linestyle='-', label='EVM(14)')
    plt.legend(loc=2, prop={'size': 9})
    plt.ylabel('EVM values')
    plt.grid(True)
    plt.setp(plt.gca().get_xticklabels(), rotation=30)
    plt.show()