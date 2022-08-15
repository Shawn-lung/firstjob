import requests
import yfinance as yf
from talib import abstract
import pandas as pd
from datetime import datetime, timedelta
from numpy import nan

class StockCrawler():
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
        self.olddata = yf.Ticker(self.stock_symbol).history(interval = self.interval , period = self.period)
        self.stock_data["open"] = self.olddata["Open"]
        self.stock_data["high"] = self.olddata["High"]
        self.stock_data["low"] = self.olddata["Low"]
        self.stock_data["close"] = self.olddata["Close"]
        self.stock_data["volume"] = self.olddata["Volume"]
        self.stock_data["updown"] = self.stock_data["close"][-1] - self.stock_data["previous_close"]
        self.stock_data["percentage"] = self.stock_data["updown"] / self.stock_data["previous_close"] * 100
        self.stock_data["amplitude"] = sorted(self.stock_data["close"])[-1] - sorted(self.stock_data["close"])[0]
        self.olddata = {'open':self.stock_data["open"] , 'high' : self.stock_data["high"] ,'low' : self.stock_data["low"], 'close' : self.stock_data["close"],'volume' : self.stock_data["volume"]}
        self.olddata = pd.DataFrame(self.olddata)

    
    def ta_list(self, function):
        if function == "None":
            return [None]
        else:
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
                if self.stock_data["close"][-1] != self.stock_data["close"][x]:
                    if x in self.plus:
                        self.lastmax_y = self.stock_data["close"][x]
                        self.lastmax_y = self.stock_data["close"].index[x]
                    else:
                        self.lastmin_y = self.stock_data["close"][x]
                        self.lastmin_y = self.stock_data["close"].index[x]    
                timelst.append(self.stock_data['close'].index[x])
            for i in range(len(self.stock_data['close'])):
                if i not in self.inflection_lst:
                    self.point.insert(i , nan)  
            self.lineCompletion(self.point)
            self.dfpoint = pd.DataFrame(self.point, columns= ['point'])
            self.dfpoint.index = self.stock_data['close'].index
            return self.dfpoint
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

class FuturesCrawler():
    def __init__(self, futures_code: str, futures_index: int):
        self.futures_code = futures_code
        self.futures_index = futures_index
        self.setIntervalPeriod()
        self.get_tw_futures()
    
    def determine_url(self):
        match self.interval:
            case '1m':
                if self.futures_index > 3:
                    self.url = "https://ws.api.cnyes.com/ws/api/v1/charting/history?symbol=TWS:"+self.futures_code+":INDEX&resolution=1&quote=1"
                else:
                    self.url = "https://ws.api.cnyes.com/ws/api/v1/charting/history?symbol=TWF:"+self.futures_code+":FUTURES&resolution=1&quote=1"
            case '1d':
                if self.futures_index > 3:
                    self.url = "https://ws.api.cnyes.com/ws/api/v1/charting/history?symbol=TWS:"+self.futures_code+":INDEX&resolution=D&quote=1&from="+self.ftime+"&to="+self.time
                else:
                    self.url = "https://ws.api.cnyes.com/ws/api/v1/charting/history?symbol=TWF:"+self.futures_code+":FUTURES&resolution=D&quote=1&from="+self.ftime+"&to="+self.time
            case '1w':
                if self.futures_index > 3:
                    self.url = "https://ws.api.cnyes.com/ws/api/v1/charting/history?symbol=TWS:"+self.futures_code+":INDEX&resolution=W&quote=1&from="+self.ftime+"&to="+self.time
                else:
                    self.url = "https://ws.api.cnyes.com/ws/api/v1/charting/history?symbol=TWF:"+self.futures_code+":FUTURES&resolution=W&quote=1&from="+self.ftime+"&to="+self.time
            case '1mo':
                if self.futures_index > 3:
                    self.url = "https://ws.api.cnyes.com/ws/api/v1/charting/history?symbol=TWS:"+self.futures_code+":INDEX&resolution=M&quote=1&from="+self.ftime+"&to="+self.time
                else:
                    self.url = "https://ws.api.cnyes.com/ws/api/v1/charting/history?symbol=TWF:"+self.futures_code+":FUTURES&resolution=M&quote=1&from="+self.ftime+"&to="+self.time
    
    def get_tw_futures(self):
        res = requests.get(self.url)
        futuredata = res.json()['data']
        time = pd.to_datetime([i+3600*8 for i in futuredata['t']],unit='s')
        if self.flag:
            try:        
                futuredata = pd.DataFrame({'open' : list(reversed(futuredata['o'][:self.flag1])), 'high' : list(reversed(futuredata['h'][:self.flag1])), 'low' : list(reversed(futuredata['l'][:self.flag1])), 'close' : list(reversed(futuredata['c'][:self.flag1])), 'volume' : list(reversed(futuredata['v'][:self.flag1]))},index=list(reversed(time[:self.flag1])))
            except:
                futuredata = pd.DataFrame({'open' : list(reversed(futuredata['o'])), 'high' : list(reversed(futuredata['h'])), 'low' : list(reversed(futuredata['l'])), 'close' : list(reversed(futuredata['c'])), 'volume' : list(reversed(futuredata['v']))},index=list(reversed(time)))
        else:
            futuredata = pd.DataFrame({'open' : list(reversed(futuredata['o'])), 'high' : list(reversed(futuredata['h'])), 'low' : list(reversed(futuredata['l'])), 'close' : list(reversed(futuredata['c'])), 'volume' : list(reversed(futuredata['v']))},index=list(reversed(time)))
        self.df = futuredata

    def setIntervalPeriod(self, interval="1m", period="1d"):
        self.interval = interval
        self.period = period
        self.ftime = str(int(datetime.timestamp(datetime.now())))
        days = 1
        self.flag = False
        self.flag1 = 60
        #period設定抓幾天的資料後用timedelta來減
        match self.period:
            case "1h":
                days = 1
                self.flag = True
                self.flag1 = 60
            case "2h":
                days = 1
                self.flag = True
                self.flag1 = 120
            case "1d":
                days = 1
            case "1mo":
                days = 30
            case "3mo":
                days = 90
            case "6mo":
                days = 180
            case "1y":
                days = 365
            case "2y":
                days = 730
            case "5y":
                days = 1826
            case "10y":
                days = 3650
        self.time = str(int(datetime.timestamp(datetime.now()-timedelta(days))))
        self.determine_url()

    def ta_list(self, function):
        if function == "None":
            return[None]
        else:
            return(eval(f"abstract.{function}(self.df)"))


    def plus_or_minus(self, x):
        self.plus = []
        self.minus = []
        for i in range(1,len(self.df["close"])-1):
            if self.df["close"][i+1] > self.df["close"][i]:
                self.plus.append(i+1)
            elif self.df["close"][i+1] < self.df["close"][i]:
                self.minus.append(i+1)
            else:
                pass
        return(self.deal_pom(x))

    def deal_pom(self, x):
        self.inflection_lst = [0]
        self.point = []
        timelst = []
        for i in range(len(self.df["close"])):
            if i in self.plus:
                if self.inplus(i) not in self.inflection_lst:
                    self.inflection_lst.append(self.inplus(i))
            if i in self.minus:
                if self.inminus(i) not in self.inflection_lst:
                    self.inflection_lst.append(self.inminus(i))
        if x == "y":
            for x in self.inflection_lst:
                self.point.append(self.df["close"][x])
                timelst.append(self.df['close'].index[x])
            for i in range(len(self.df['close'])):
                if i not in self.inflection_lst:
                    self.point.insert(i , nan)  
            self.lineCompletion(self.point)
            df = pd.DataFrame(self.point, columns= ['point'])
            df.index = self.df['close'].index
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
        for i in range(len(self.df['close'])):
            if i not in self.inflection_lst:
                start = self.df['close'][i]
                self.isnan(start , i , 1)
                
    def isnan(self,start,i,n):
        if i not in self.inflection_lst:
            return(self.isnan(start,i+1,n+1))
        else:
            newstart = start
            for x in range(n-1):
                newstart+=((self.df['close'][i] - start )/n)
                self.point.insert(i-n+x+1,newstart)
                self.inflection_lst.insert(i-n+x+1 , i-n+x+1) 

    def inplus(self, i):
        if i not in self.minus and i < len(self.df["close"]):
            return(self.inplus(i+1))
        else:
            return(i-1)

    def inminus(self, i):
        if i not in self.plus and i < len(self.df["close"]):
            return(self.inminus(i+1))
        else:
            return(i-1)
            

        