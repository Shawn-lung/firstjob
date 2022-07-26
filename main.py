import twstock
import pandas as pd 
import time
wait = int(input('time'))*60
stocklist = []
realtime_dict = {}
info_dict = {}
while True:
    stockcode = (input('stockcode,  l to leave'))
    if stockcode == 'l':
        break
    stocklist.append(stockcode)
while True:
    stock = twstock.realtime.get(stocklist)
    for i in stocklist:
        all = stock.get(i)
        info = all.get('info')
        realtime = all.get('realtime')
        info_dict[i] = info
        realtime_dict[i] = realtime

    print(pd.DataFrame(realtime_dict))
    print(pd.DataFrame(info_dict))
    try:
        time.sleep(wait)
    except KeyboardInterrupt:
        break
        
