from datetime import datetime, timedelta
import requests
import pandas
def get_future_data(interval, period):
    
    futures = 'MXF'
    #UI改成像stockui一樣選interval跟period
    ftime = str(int(datetime.timestamp(datetime.now())))
    #period設定抓幾天的資料後用timedelta來減
    time = str(int(datetime.timestamp(datetime.now()-timedelta(period))))
    print(ftime)
    #interval是1min的話不能選period
    match interval:
        case '1m':
            url = "https://ws.api.cnyes.com/ws/api/v1/charting/history?symbol=TWF:"+futures+":FUTURES&resolution=1&quote=1"
        case '1d':
            url = "https://ws.api.cnyes.com/ws/api/v1/charting/history?symbol=TWF:"+futures+":FUTURES&resolution=D&quote=1&from="+ftime+"&to="+time
        case '1w':
            url ="https://ws.api.cnyes.com/ws/api/v1/charting/history?symbol=TWF:"+futures+":FUTURES&resolution=W&quote=1&from=1660502040&to=1644949980"
        case '1m':
            url ="https://ws.api.cnyes.com/ws/api/v1/charting/history?symbol=TWF:"+futures+":FUTURES&resolution=M&quote=1&from="+ftime+"&to="+time
    #其他三個都可以選period
    res = requests.get(url)
    futuredata = res.json()['data']
    time = pandas.to_datetime(futuredata['t'],unit='s')
    futuredata = pandas.DataFrame({'open' : futuredata['o'], 'high' : futuredata['h'], 'low' : futuredata['l'], 'close' : futuredata['c'], 'volume' : futuredata['v']},index=time)
    return futuredata