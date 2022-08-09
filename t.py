#下載資料套件
import urllib3
from bs4 import BeautifulSoup

#資料處理套件
import pandas as pd
from datetime import date

#下載每日期貨交易資訊函式
def get_tw_futures(start_year, start_month, start_day, end_year, end_month, end_day, market_code = 0):
    start_date = str(date(start_year, start_month, start_day))
    end_date = str(date(end_year, end_month, end_day))
    date_list = pd.date_range(start_date, end_date, freq='D').strftime("%Y/%m/%d").tolist()

    df = pd.DataFrame()
    http = urllib3.PoolManager()
    url = "https://www.taifex.com.tw/cht/3/futDailyMarketReport"
    for day in date_list:  
        res = http.request(
             'POST',
              url,
              fields={
                 'queryType': 2,
                 'marketCode': market_code,
                 'commodity_id': 'TX',
                 'queryDate': day,
                 'MarketCode': market_code,
                 'commodity_idt': 'TX'
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
    
    return df
df = get_tw_futures(start_year = 2022,
                    start_month = 4,
                    start_day = 6,
                    end_year = 2022, 
                    end_month = 4,
                    end_day = 13)
print(df['開盤價'])    