import requests
import yfinance as yf
from talib import get_functions ,abstract, MA
import mplfinance as mpf
import matplotlib.pyplot as plt
import pandas as pd
import enum
from numpy import nan
class Crawler():
    def __init__(self, stock_code: str):
        self.stock_data = {}
        self.olddata = {}
        self.stock_code = stock_code
        self.setIntervalPeriod()
        self.get_history_data(stock_code)
        
    def get_history_data(self, stock):
        res = requests.get("https://tw.stock.yahoo.com/_td-stock/api/resource/FinanceChartService.ApacLibraCharts;symbols=%5B%22"+stock+".TW%22%5D;type=tick?bkt=%5B%22tw-qsp-exp-no2-1%22%2C%22test-es-module-production%22%2C%22test-portfolio-stream%22%5D&device=desktop&ecma=modern&feature=ecmaModern%2CshowPortfolioStream&intl=tw&lang=zh-Hant-TW&partner=none&prid=2h3pnulg7tklc&region=TW&site=finance&tz=Asia%2FTaipei&ver=1.2.902&returnMeta=true")
        self.stock_symbol = res.json()["data"][0]["chart"]["meta"]["symbol"]
        self.stock_data["previous_close"] = res.json()["data"][0]["chart"]["meta"]["previousClose"]
        self.stock_data["limit_up_price"] = res.json()["data"][0]["chart"]["meta"]["limitUpPrice"]
        self.stock_data["limit_down_price"] = res.json()["data"][0]["chart"]["meta"]["limitDownPrice"]
        self.stock_data["today_open"] = res.json()["data"][0]["chart"]["indicators"]["quote"][0]["open"]
        self.olddata = yf.Ticker(self.stock_symbol).history(interval = self.interval, period = self.period)
        self.stock_data["open"] = self.olddata["Open"]
        self.stock_data["high"] = self.olddata["High"]
        self.stock_data["low"] = self.olddata["Low"]
        self.stock_data["close"] = self.olddata["Close"]
        self.stock_data["volume"] = self.olddata["Volume"]
        #self.stock_data["Datetime"] = olddata["Datetime"]
        self.stock_data["updown"] = self.stock_data["close"][-1] - self.stock_data["previous_close"]
        self.stock_data["percentage"] = self.stock_data["updown"] / self.stock_data["previous_close"] * 100
        self.stock_data["amplitude"] = sorted(self.stock_data["close"])[-1] - sorted(self.stock_data["close"])[0]
        self.olddata['open'] = self.olddata.pop('Open')
        self.olddata['high'] = self.olddata.pop('High')
        self.olddata['low'] = self.olddata.pop('Low')
        self.olddata['close'] = self.olddata.pop('Close')
        self.olddata['volume'] = self.olddata.pop('Volume')


    def kgraph(self):
        mc = mpf.make_marketcolors(
        up="red",  
        down="green",  
        edge="black",  
        volume="blue", 
        wick="black"  )
        style = mpf.make_mpf_style(base_mpl_style="ggplot", marketcolors=mc)
        mpf.plot(self.olddata, type="candle", title="Candlestick", volume = True, ylabel="price($)" , style = style , returnfig = True ,mav = (5,10,20))
        return mpf.figure()
    
    def ta_list_MA(self):
        return MA(self.stock_data["close"])

    def ta_list(self, function):
        return(eval(f"abstract.{function}(self.olddata)"))

    def plus_or_minus(self, x):
        self.plus = []
        self.minus = []
        for i in range(1,len(self.stock_data["close"])-1):
            if self.stock_data["close"][i+1] > self.stock_data["close"][i]:
                self.plus.append(i+1)
            elif self.stock_data["close"][i+1] < self.stock_data["close"][i]:
                self.minus.append(i+1)
            else:
                pass
        return(self.deal_pom(x))

    def deal_pom(self, x):
        self.inflection_lst = [0]
        self.point = []
        timelst = []
        for i in range(len(self.stock_data["close"])):
            if i in self.plus:
                if self.inplus(i) not in self.inflection_lst:
                    self.inflection_lst.append(self.inplus(i))
            if i in self.minus:
                if self.inminus(i) not in self.inflection_lst:
                    self.inflection_lst.append(self.inminus(i))
        if x == "y":
            for x in self.inflection_lst:
                self.point.append(self.stock_data["close"][x])
                timelst.append(self.stock_data['close'].index[x])
            for i in range(len(self.stock_data['close'])):
                if i not in self.inflection_lst:
                    self.point.insert(i , nan)  
            self.lineCompletion(self.point)
            df = pd.DataFrame(self.point, columns= ['point'])
            df.index = self.stock_data['close'].index
            return df
        else:
            return(self.inflection_lst)
    
    def lineCompletion(self, lst):
        nan_num = 0
        for i in range(len(lst)):
            if lst[i] is nan:
                nan_num += 1
            elif nan_num != 0:
                for j in range(1, nan_num+1):
                    lst[i-j] = lst[i] - (j*(lst[i]-lst[i-nan_num-1])/(nan_num+1))
                nan_num = 0
                
    def line(self):
        for i in range(len(self.stock_data['close'])):
            if i not in self.inflection_lst:
                start = self.stock_data['close'][i]
                self.isnan(start , i , 1)
                
    def isnan(self,start,i,n):
        if i not in self.inflection_lst:
            return(self.isnan(start,i+1,n+1))
        else:
            newstart = start
            for x in range(n-1):
                newstart+=((self.stock_data['close'][i] - start )/n)
                self.point.insert(i-n+x+1,newstart)
                self.inflection_lst.insert(i-n+x+1 , i-n+x+1) 

    def inplus(self, i):
        if i not in self.minus and i < len(self.stock_data["close"]):
            return(self.inplus(i+1))
        else:
            return(i-1)

    def inminus(self, i):
        if i not in self.plus and i < len(self.stock_data["close"]):
            return(self.inminus(i+1))
        else:
            return(i-1)
            
    def getStocks():
        r = requests.get("https://quality.data.gov.tw/dq_download_json.php?nid=11549&md5_url=bb878d47ffbe7b83bfc1b41d0b24946e")
        json = r.json()
        id_lst = []
        for dict in json:
            id_lst.append(f"{dict['證券代號']}: {dict['證券名稱']}")
        return id_lst

    def setIntervalPeriod(self, interval="1m", period="1d"):
        self.interval = interval
        self.period = period
