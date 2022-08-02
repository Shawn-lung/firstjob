import time
import requests

import numpy as np
import pandas as pd
import mplfinance as mpf
import matplotlib.pyplot as plt
import pandas_datareader.data as web
from talib import abstract
from datetime import datetime, timedelta

start = datetime.now()- timedelta(days =  100)
end =  datetime.now()
stock = web.DataReader('8069.TWO', 'yahoo', start, end)
print(stock)
stock = mpf.plot(stock, type = "candle", mav = (5, 10, 20))
plt.show()