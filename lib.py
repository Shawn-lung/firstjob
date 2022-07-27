import requests
import pandas

class Get_info(): 
    def __init__(self, stock_list):
        self.jd_dict = {}
        self.stock_list = stock_list
        self.time_list = []
        self.df = {}
        self.bn = {}
    def request_url(self):

        for stock in self.stock_list:
            time_list = []
            res = requests.get("https://tw.stock.yahoo.com/_td-stock/api/resource/FinanceChartService.ApacLibraCharts;symbols=%5B%22"+stock+".TW%22%5D;type=tick?bkt=%5B%22tw-qsp-exp-no2-1%22%2C%22test-es-module-production%22%2C%22test-portfolio-stream%22%5D&device=desktop&ecma=modern&feature=ecmaModern%2CshowPortfolioStream&intl=tw&lang=zh-Hant-TW&partner=none&prid=2h3pnulg7tklc&region=TW&site=finance&tz=Asia%2FTaipei&ver=1.2.902&returnMeta=true")
            self.jd_dict[stock] = res.json()['data']
            self.close_list = self.jd_dict[stock][0]['chart']['indicators']['quote'][0]['close']
            timestamp = self.jd_dict[stock][0]['chart']['timestamp']
            for i in timestamp:
                
                time_list.append (pandas.to_datetime(i+3600*8, unit = 's'))
                
            #print(df[stock]['timestamp'])
            #df[stock]['dt'] = pandas.to_datetime(df[stock]['timestamp'] + 3600 * 8, unit = 's')
            
            previous_close = self.jd_dict[stock][0]['chart']['meta']['previousClose']
            open = self.jd_dict[stock][0]['chart']['indicators']['quote'][0]['open'][1]
            self.close_list[0] = open
            limit_up_price = self.jd_dict[stock][0]['chart']['meta']["limitUpPrice"]
            limit_down_price = self.jd_dict[stock][0]['chart']['meta']["limitDownPrice"]
            close = self.jd_dict[stock][0]['chart']['indicators']['quote'][0]['close'][-1]
            updown = close - previous_close
            percentage = updown/previous_close * 100  
            close_list_without_none = [x for x in self.close_list if x != None]
            amplitude = max(close_list_without_none) - min(close_list_without_none)
            self.bn[stock] = {'前日收盤價': previous_close, '開盤價': open, '漲停價' : limit_up_price, '跌停價' : limit_down_price, '當下股價' : close, '漲跌幅' :updown, '漲跌比率' : percentage, '振幅' : amplitude}
        
            self.df[stock] = (pandas.DataFrame({'time' : time_list, 'price' : self.close_list }))  
        print(self.bn)
        print(self.df)
            
