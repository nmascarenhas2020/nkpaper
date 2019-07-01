import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
from mpl_finance import candlestick_ohlc
import matplotlib.dates as mdates
import pandas as pd
import pandas_datareader.data as web
style.use('ggplot')
start = dt.datetime(2016,1,20) #insert your own start date here, (year, month, day)
end = dt.datetime(2016, 2, 19) #insert your own end date here, same format
df = web.DataReader('^N225', 'yahoo', start, end) #insert ticker into the first part
df.to_csv('japan2.csv') #name the end file here
df = pd.read_csv('japan2.csv', parse_dates=True, index_col=0)
df_ohlc.reset_index(inplace=True)
#print(df_ohlc.head()) ##these are if you want to see a graph of the data
#ax1 = plt.subplot2grid((6,1),(0,0), rowspan=5, colspan=1)
#ax2 = plt.subplot2grid((6,1), (5,0), rowspan=1, sharex=ax1)
#plt.show()
start = dt.datetime(2019,1,1)
end = dt.datetime(2019, 12, 31)
df = web.DataReader('^KS11', 'yahoo', start, end)
df.to_csv('southkorea2019.csv')
start = dt.datetime(2019,1,1)
end = dt.datetime(2019, 12, 31)
df = web.DataReader('^N225', 'yahoo', start, end)
df.to_csv('japan2019.csv')
print(df.head())
