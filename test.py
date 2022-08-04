import time
import requests
from CrawlerClass import Crawler
import numpy as np
import pandas as pd
import mplfinance as mpf
import matplotlib.pyplot as plt
import pandas_datareader.data as web
from talib import abstract, get_functions
from datetime import datetime, timedelta

crawler = Crawler('2330')
""" stock = 'stock'
data = {'stock': []}
data['stock'].append(crawler.olddata) """
data  = crawler.olddata


function = get_functions()[1]

print(eval(f'abstract.{function}(data)'))

