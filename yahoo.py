from matplotlib import pyplot as plt
import requests
import pandas
import time
import lib
i = 0
stock_list  = []
minutes = int(input('minutes'))*60
period = '1mo'
while i<2:
    stock_list.append(input('stock code'))
    i+=1
while True:
    gi = lib.Get_info(stock_list)
    symbol_list = gi.request_url()
    history_data = lib.get_history_data(symbol_list,period)
    #adx = lib.get_adx(history_data,symbol_list)
    #rsi = lib.get_rsi(history_data,symbol_list)
    ta_list = lib.ta_list(history_data,symbol_list,30)
    try :
        time.sleep(minutes)
    except KeyboardInterrupt:
        break