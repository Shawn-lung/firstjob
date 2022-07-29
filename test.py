import yfinance as yf
olddata = yf.Ticker('2330.TW').history(period = '1d',interval = '1m')
print(olddata)