from matplotlib import pyplot as plt
import requests
import pandas
import time
import lib
i = 0
stock_list  = []
minutes = int(input('minutes'))*60
while i<5:
    stock_list.append(input('stock code'))
    i+=1
while True:
    gi = lib.Get_info(stock_list)
    gi.request_url()
    try :
        time.sleep(minutes)
    except KeyboardInterrupt:
        break