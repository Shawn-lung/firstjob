
from dataclasses import replace
from CrawlerClass import Crawler
from numpy import nan

def lineCompletion(lst):
    nan_num = 0
    for i in range(len(lst)):
        if lst[i] is nan:
            nan_num += 1
        elif nan_num != 0:
            for j in range(1, nan_num+1):
                lst[i-j] = round(lst[i] - (j*(lst[i]-lst[i-nan_num-1])/(nan_num+1)), 2)
            nan_num = 0


clr = Crawler("2330")

lst = [508.0, nan, nan, nan, nan, 507.0, nan, nan, nan, nan, nan, 509.0, 508.0, nan, nan, 509.0, nan, nan, 508.0, nan, 510.0, 509.0, nan, nan, 510.0, nan, 509.0, 510.0, 509.0, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, 511.0, 510.0, nan, nan, nan, nan, nan, 511.0, 510.0, nan, nan, nan, nan, nan, nan, nan, nan, 512.0, nan, nan, nan, 510.0, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, 512.0, nan, 511.0, nan, nan, 512.0, 511.0, nan, nan, nan, nan, nan, nan, 513.0, 512.0, nan, nan, nan, nan, nan, nan, nan, 514.0, 513.0, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, 514.0, nan, 513.0, 514.0, 513.0, nan, 514.0, nan, 513.0, nan, nan, nan, nan, 514.0, 513.0, 514.0, 513.0, nan, nan, nan, nan, nan, nan, 514.0, 513.0, nan, 514.0, nan, 513.0, 514.0, 513.0, 514.0, nan, 513.0, 514.0, 513.0, 514.0, 513.0, nan, nan, 514.0, nan, 513.0, nan, nan, 515.0, nan, 514.0, nan, 515.0, 514.0, 515.0, nan, nan, 514.0, 515.0, nan, 513.0, nan, nan, nan, nan, nan, nan, nan, nan, 515.0, nan, 514.0, nan, 515.0, 514.0, nan, 515.0, nan, nan, 514.0, 515.0, nan, 514.0, nan, 515.0, nan, nan, 514.0, 515.0, 514.0, 515.0, nan, 514.0, nan, nan, nan, nan, 515.0, 514.0, nan, 515.0, 514.0, nan, nan, 516.0, nan, 515.0, nan, nan, nan, 516.0, 515.0, nan, nan, 516.0, 515.0, 516.0, 515.0, nan, 516.0, 515.0, nan, nan, nan, 516.0, nan, 515.0, nan, nan, nan, nan, nan, nan, nan, 516.0, nan, 515.0, nan, nan, nan, nan, 516.0, 515.0, nan, nan, nan, nan, nan, nan, nan, 516.0, 515.0, 516.0, nan, 515.0, 516.0]
#lst = [2, 3, 5, None, 7, None, None, 9]
#lst = [508.0, None, None, None, None, 507.0]



lineCompletion(lst)
print(lst)