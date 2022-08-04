import matplotlib as mpl
import mplfinance as mpf
import pandas
from CrawlerClass import Crawler
c = Crawler("0050")
mpf.plot(pandas.DataFrame({"Open": c.olddata["open"], "High": c.olddata['high'], "Low": c.olddata["low"], "Close": c.olddata["close"]}), type="candle")