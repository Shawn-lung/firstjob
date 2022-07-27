import requests
import pandas

class Get_info():    
    
    def request_url(stock_list):
        jd_dict = {}
        for stock in stock_list:
            res = requests.get("https://tw.stock.yahoo.com/_td-stock/api/resource/FinanceChartService.ApacLibraCharts;symbols=%5B%22"+stock+".TW%22%5D;type=tick?bkt=%5B%22tw-qsp-exp-no2-1%22%2C%22test-es-module-production%22%2C%22test-portfolio-stream%22%5D&device=desktop&ecma=modern&feature=ecmaModern%2CshowPortfolioStream&intl=tw&lang=zh-Hant-TW&partner=none&prid=2h3pnulg7tklc&region=TW&site=finance&tz=Asia%2FTaipei&ver=1.2.902&returnMeta=true")
            jd = res.json()['data']
            jd_dict[stock] = jd
        return (Get_info.get_df(jd_dict,stock_list))    
    
    def get_df(jd_dict,stock_list):
        for stock in stock_list:       
            close_list = jd_dict[stock][0]['chart']['indicators']['quote'][0]['close']
            timestamp = jd_dict[stock][0]['chart']['timestamp']
            df = pandas.DataFrame({stock :{'timestamp': timestamp, 'close':close_list}})
            df[stock]['dt'] = pandas.to_datetime(df[stock]['timestamp'] + 3600 * 8, unit = 's')
            df2 = pandas.DataFrame({stock:{'time' : df['dt'], 'price' : close_list }})
        print(df2)

