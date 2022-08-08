import requests as request
import json
url = request.get("https://tw.screener.finance.yahoo.net/future/q?type=ta&perd=d&mkt=01&sym=WTX00&callback=jQuery1113033265881543586406_1659958858733&_=1659958858734v")
a = url.text.replace('jQuery1113033265881543586406_1659958858733(','')
a = a.replace(");",'')
