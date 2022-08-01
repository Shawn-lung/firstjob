import time
import requests

import numpy as np
import pandas as pd
import mplfinance as mpf
import matplotlib.pyplot as plt
import pandas_datareader.data as web
from talib import abstract
from datetime import datetime, timedelta

start = datetime.now()- timedelta(days =  10)
end =  datetime.now()
stock = web.DataReader('2330.TW', 'yahoo', start, end)
print(stock)
stock = mpf.plot(stock, type = "candle")
stock.show()