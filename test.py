import lib
from talib import abstract
import yfinance as yf

a = lib.Get_info(['0050'])
url = a.request_url()
data = lib.get_history_data(url)
ta  = lib.ta_list(data,'0050.TW')
print(ta)