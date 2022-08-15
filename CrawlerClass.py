import requests
import yfinance as yf
import json
from talib import get_functions ,abstract, MA
import mplfinance as mpf
import matplotlib.pyplot as plt
import pandas as pd
from datetime import date, datetime, timedelta
from numpy import nan
import urllib3
from bs4 import BeautifulSoup


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
        #self.stock_data["Datetime"] = olddata["Datetime"]
        self.stock_data["updown"] = self.stock_data["close"][-1] - self.stock_data["previous_close"]
        self.stock_data["percentage"] = self.stock_data["updown"] / self.stock_data["previous_close"] * 100
        self.stock_data["amplitude"] = sorted(self.stock_data["close"])[-1] - sorted(self.stock_data["close"])[0]
        self.olddata = {'open':self.stock_data["open"] , 'high' : self.stock_data["high"] ,'low' : self.stock_data["low"], 'close' : self.stock_data["close"],'volume' : self.stock_data["volume"]}
        self.olddata = pd.DataFrame(self.olddata)
        print(self.olddata)
    
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




class FuturesCrawler():
    def __init__(self, futures_code: str, days: int):
        self.futures_code = futures_code
        self.setStartDate(days)
        self.get_tw_futures(futures_code)

    def get_tw_futures(self, futures_code):
        date_list = pd.date_range(self.start_date, self.end_date, freq='D').strftime("%Y/%m/%d").tolist()

        df = pd.DataFrame()
        http = urllib3.PoolManager()
        url = "https://www.taifex.com.tw/cht/3/futDailyMarketReport"
        for day in date_list:  
            res = http.request(
                'POST',
                url,
                fields={
                    'queryType': 2,
                    'marketCode': 0,
                    'commodity_id': futures_code,
                    'queryDate': day,
                    'MarketCode': 0,
                    'commodity_idt': futures_code
                }
            )
            html_doc = res.data
            soup = BeautifulSoup(html_doc, 'html.parser')
            table = soup.findAll('table')[2]
            try:
                df_day = pd.read_html(str(table))[2]
            except:
                print(day + '並未開盤。')
                continue
            
            #加入日期
            df_day.insert(0, '日期', day)
            df = df.append(df_day, ignore_index = True)
        print(df)
        df['open'] = df.pop('開盤價')
        df['high'] = df.pop('最高價')
        df['low'] = df.pop('最低價')
        df['close'] = df.pop('最後成交價')
        df['volume'] = df.pop('*合計成交量')
        df = {'open' : df['open'] , 'high' : df['high'], 'low' : df['low'] , 'close' : df['close'],'volume' : df['volume'] ,'日期' : df['日期']}
        df = pd.DataFrame(df)
        df = df.drop(index = df.loc[df['open'] == '-'].index)
        df = df.drop(index = df.loc[df['high'] == '-'].index)
        df = df.drop(index = df.loc[df['low'] == '-'].index)
        df = df.drop(index = df.loc[df['close'] == '-'].index)
        df = df.drop(index = df.loc[df['volume'] == '-'].index)  
        index = list(range(len(df['open'])))
        df.index = index
        for i in range(len(df['open'])):           
            if pd.isnull(df['open'][i]):
                df = df.drop(index = i)
        df.index = pd.to_datetime(df['日期'])
        df.pop('日期')
        df['open'] = [float(i) for i in df['open']]
        df['high'] = [float(i) for i in df['high']]
        df['low'] = [float(i) for i in df['low']]
        df['close'] = [float(i) for i in df['close']]
        df['volume'] = [float(i) for i in df['volume']]
        self.df = df

    def setStartDate(self,days: int):
        self.start_date = datetime.now() - timedelta(days) 
        self.start_date = str(date(self.start_date.year, self.start_date.month, self.start_date.day))
        self.end_date = str(date(datetime.now().year, datetime.now().month,datetime.now().day))

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
            
    def getFutures():
        id_lst = []
        with open("future.json", mode='r', encoding="utf-8") as data:
            data = json.load(data)
        for i in range(len(data['code'])):
            id_lst.append(f"{data['code'][i]} : {data['name'][i]}")
        return id_lst

        