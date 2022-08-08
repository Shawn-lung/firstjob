import requests 
import pandas as pd
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
df = df[["DispCName" , "CTotalVolume", "COpenPrice", "CHighPrice", "CLowPrice" ,"CLastPrice"]]
print(df)
=======
import requests as request
import json
url = request.get("https://tw.screener.finance.yahoo.net/future/q?type=ta&perd=d&mkt=01&sym=WTX00&callback=jQuery1113033265881543586406_1659958858733&_=1659958858734v")
a = url.text.replace('jQuery1113033265881543586406_1659958858733(','')
a = a.replace(");",'')
>>>>>>> 168d54d702ad665c821e4828a8ae5253c7e3fd97
