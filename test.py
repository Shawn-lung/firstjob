import mplfinance as mpf
import pandas as pd
from CrawlerClass import Crawler
import matplotlib.pyplot as plt
crawler = Crawler('2330')
df = pd.DataFrame(crawler.ta_list('MA'))
plt.plot(df)
plt.show()