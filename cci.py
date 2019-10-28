import pandas as pd
import pandas_datareader as web
import matplotlib.pyplot as plt
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

def cci(data, n_days):
    '''
    compute Commodity Channel Index 顺势指标, 异常检测
    Shows a stock's variation from its “typical” price

    data : original data include high,low,close price
    ndays: 数据周期
    '''
    TP = (data['High'] + data['Low'] + data['Close']) / 3
    # CCI = pd.Series((TP - pd.rolling_mean(TP, n_days)) / (0.015 * pd.rolling_std(TP, n_days)), name='CCI')
    CCI = pd.Series((TP - TP.rolling(n_days).mean()) / (0.015 * data['Close'].rolling(n_days).std()), name='CCI')
    data = data.join(CCI)
    return data

if __name__ == '__main__':
    # Retrieve the apple data from Yahoo finance:
    data = web.DataReader('AAPL', data_source='yahoo', start='20140101', end='20160101')
    data = pd.DataFrame(data)

    n = 20
    apple_CCI = cci(data, n)
    CCI = apple_CCI['CCI']

    # Plotting the Price Series chart and the Commodity Channel index below
    fig = plt.figure(figsize=(7, 5))
    ax = fig.add_subplot(2, 1, 1)
    ax.set_xticklabels([])
    plt.plot(data['Close'], lw=1)
    plt.title('NSE Price Chart')
    plt.ylabel('Close Price')
    plt.grid(True)
    bx = fig.add_subplot(2, 1, 2)
    plt.plot(CCI, 'k', lw=0.75, linestyle='-', label='CCI')
    plt.legend(loc=2, prop={'size': 9.5})
    plt.ylabel('CCI values')
    plt.grid(True)
    plt.setp(plt.gca().get_xticklabels(), rotation=30)
    plt.show()