import requests 
import pandas as pd
import mplfinance as mpf
payload = {"MarketType":"0",
           "SymbolType":"F",
           "KindID":"1",
           "CID":"BTF",
           "ExpireMonth":"",
           "RowSize":"全部",
           "PageNo":"",
           "SortColumn":"",
           "AscDesc":"A"}
res = requests.post("https://mis.taifex.com.tw/futures/api/getQuoteList",json = payload)
data = res.json()

df = pd.DataFrame(data['RtData']['QuoteList'])
timestamp = df['CTime']
print(timestamp)
#timestamp = pd.to_datetime(timestamp)
print(timestamp)
df = df[["DispCName" , "CTotalVolume", "COpenPrice", "CHighPrice", "CLowPrice" ,"CLastPrice"]]
df['name'] = df.pop('DispCName')
df['open'] = df.pop('COpenPrice')
df['high'] = df.pop('CHighPrice')
df['low'] = df.pop('CLowPrice')
df['close'] = df.pop('CLastPrice')
df['volume'] = df.pop('CTotalVolume')
print(df)
""" mc = mpf.make_marketcolors(
        up="red",  
        down="green",  
        edge="black",  
        volume="blue", 
        wick="black")
style = mpf.make_mpf_style(base_mpl_style="ggplot", marketcolors=mc)
mpf.plot(df, type="candle", title="Candlestick", volume = True, ylabel="price($)" , style = style , returnfig = True ,mav = (5,10,20)) """