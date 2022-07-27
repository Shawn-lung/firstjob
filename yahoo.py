from matplotlib import pyplot as plt
import requests
import pandas
import time
stock = input('stock name')
minutes = int(input('minutes'))*60
while True:
    res = requests.get("https://tw.stock.yahoo.com/_td-stock/api/resource/FinanceChartService.ApacLibraCharts;symbols=%5B%22"+stock+".TW%22%5D;type=tick?bkt=%5B%22tw-qsp-exp-no2-1%22%2C%22test-es-module-production%22%2C%22test-portfolio-stream%22%5D&device=desktop&ecma=modern&feature=ecmaModern%2CshowPortfolioStream&intl=tw&lang=zh-Hant-TW&partner=none&prid=2h3pnulg7tklc&region=TW&site=finance&tz=Asia%2FTaipei&ver=1.2.902&returnMeta=true")

    jd = res.json()['data']
    pandas.DataFrame(jd)
    close_list = jd[0]['chart']['indicators']['quote'][0]['close']
    timestamp = jd[0]['chart']['timestamp']
    df = pandas.DataFrame({'timestamp': timestamp, 'close':close_list})

    df.head()

    df['dt'] = pandas.to_datetime(df['timestamp'] + 3600 * 8, unit = 's')
    
    #plt.plot(df['dt'], close_list)
    #plt.show()
    previous_close = jd[0]['chart']['meta']['previousClose']
    open = jd[0]['chart']['indicators']['quote'][0]['open'][1]
    close_list[0] = open
    limit_up_price = jd[0]['chart']['meta']["limitUpPrice"]
    limit_down_price = jd[0]['chart']['meta']["limitDownPrice"]
    close = jd[0]['chart']['indicators']['quote'][0]['close'][-1]
    updown = close - previous_close
    percentage = updown/previous_close * 100  
    close_list_without_none = [x for x in close_list if x != None]
    amplitude = max(close_list_without_none) - min(close_list_without_none)
    
    df2 = pandas.DataFrame({'time' : df['dt'], 'price' : close_list })
    print(df2)
    time.sleep(minutes)
