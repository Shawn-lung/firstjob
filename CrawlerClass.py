import requests
import pandas
import yfinance as yf
import pandas as pd
from talib import abstract,get_functions

class Crawler():
    def __init__(self, stock_code: str):
        self.stock_data = {}
        self.stock_code = stock_code
        self.get_history_data(stock_code)
        
    def get_history_data(self,stock):       
        res = requests.get("https://tw.stock.yahoo.com/_td-stock/api/resource/FinanceChartService.ApacLibraCharts;symbols=%5B%22"+stock+".TW%22%5D;type=tick?bkt=%5B%22tw-qsp-exp-no2-1%22%2C%22test-es-module-production%22%2C%22test-portfolio-stream%22%5D&device=desktop&ecma=modern&feature=ecmaModern%2CshowPortfolioStream&intl=tw&lang=zh-Hant-TW&partner=none&prid=2h3pnulg7tklc&region=TW&site=finance&tz=Asia%2FTaipei&ver=1.2.902&returnMeta=true")
        stock_symbol = res.json()['data'][0]['symbol']
        self.stock_data['previous_close'] = res.json()['data'][0]['chart']['meta']['previousClose']
        self.stock_data['limit_up_price'] = res.json()['data'][0]['chart']['meta']["limitUpPrice"]
        self.stock_data['limit_down_price'] = res.json()['data'][0]['chart']['meta']["limitDownPrice"]
        olddata = {}
        olddata = yf.Ticker(stock_symbol).history(period = '1d',interval = '1m')
        self.stock_data['open'] = olddata['Open']
        self.stock_data['high'] = olddata['High']
        self.stock_data['low'] = olddata['Low']
        self.stock_data['close'] = olddata['Close']
        self.stock_data['volume'] = olddata['Volume']
        #self.stock_data['Datetime'] = olddata['Datetime']
        self.stock_data['updown'] = self.stock_data['close'][-1] - self.stock_data['previous_close']
        self.stock_data['percentage'] = self.stock_data['updown'] / self.stock_data['previous_close'] * 100    
    
    def ta_list(data,stock_list,periods):
        ta_list = get_functions()
        for x in ta_list:
            if x != 'MAVP' :
                #abstract.x(data[stock])
                try:
                    output = eval(f"abstract.{x}(data['2330.TW'])")
                except:
                    pass       
    def plus_or_minus(self,close, stock):
        self.plus = []
        self.minus = []
        for i in range(len(close)-1):
            if close[i+1] > close[i]:
                self.plus.append(i+1)
            elif close[i+1] < close[i]:
                self.minus.append(i+1)    
            else:
                pass
        self.deal_pom()

    def deal_pom(self):
        inflection_lst = []
        for i in range(len(self.close)):
            if i in self.plus:
                if self.inplus(i) not in inflection_lst:
                    inflection_lst.append(self.inplus(i))
            if i in self.minus:
                if self.inminus(i) not in inflection_lst:
                    inflection_lst.append(self.inminus(i))
        print(inflection_lst)
    
    def inplus(self,i):
        if i not in self.minus and i <= len(self.close):
            return(self.inplus(i+1))
        else:
            return(i-1)

    def inminus(self,i):
        if i not in self.plus:
            return(self.inminus(i+1))
        else:
            return(i-1)        
