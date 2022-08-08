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