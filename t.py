#下載資料套件
import urllib3
from bs4 import BeautifulSoup

from numpy import nan
#資料處理套件
import pandas as pd
from datetime import date
import mplfinance as mpf
from datetime import datetime

#下載每日期貨交易資訊函式
def get_tw_futures(start_year, start_month, start_day, market_code = 0):
    start_date = str(date(start_year, start_month, start_day))
    end_date = str(date(datetime.now().year, datetime.now().month,datetime.now().day))
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
                 'commodity_id':'TX' ,
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
            continue
        
        #加入日期
        df_day.insert(0, '日期', day)
        df = df.append(df_day, ignore_index = True)
    print(df)
    df['open'] = df.pop('開盤價')
    df['high'] = df.pop('最高價')
    df['low'] = df.pop('最低價')
    df['close'] = df.pop('最後成交價')
    df = {'open' : df['open'] , 'high' : df['high'], 'low' : df['low'] , 'close' : df['close'] ,'日期' : df['日期']}
    df = pd.DataFrame(df)
    df = df.drop(index = df.loc[df['open'] == '-'].index)
    df = df.drop(index = df.loc[df['high'] == '-'].index)
    df = df.drop(index = df.loc[df['low'] == '-'].index)
    df = df.drop(index = df.loc[df['close'] == '-'].index) 
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
    return df
df = get_tw_futures(start_year = 2022,
                    start_month = 8,
                    start_day = 4)   


 
mc = mpf.make_marketcolors(
        up="red",  
        down="green",  
        edge="black",  
        volume="blue", 
        wick="black")
style = mpf.make_mpf_style(base_mpl_style="ggplot", marketcolors=mc)
mpf.plot(df, type="candle", title="Candlestick",  ylabel="price($)" , style = style, mav = (5,10,20))




