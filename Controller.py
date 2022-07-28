from cProfile import label
from PyQt6.QtWidgets import QWidget
from UI import Ui_Form
import pyqtgraph as pg
import requests

class Controller(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setUpControl()

    def setUpControl(self):
        self.ui.pushButton.clicked.connect(self.on_Button_clicked)

    def on_Button_clicked(self):
        print("btn clicked")
        stock_code = self.ui.lineEdit.text()
        requestData = requests.get(f"https://tw.stock.yahoo.com/_td-stock/api/resource/FinanceChartService.ApacLibraCharts;symbols=%5B%22{stock_code}.TW%22%5D;type=tick?bkt=%5B%22tw-qsp-exp-no2-1%22%2C%22test-es-module-production%22%2C%22test-portfolio-stream%22%5D&device=desktop&ecma=modern&feature=ecmaModern%2CshowPortfolioStream&intl=tw&lang=zh-Hant-TW&partner=none&prid=2h3pnulg7tklc&region=TW&site=finance&tz=Asia%2FTaipei&ver=1.2.902&returnMeta=true")
        close_lst = [x for x in requestData.json()['data'][0]['chart']['indicators']['quote'][0]['close'] if x != None]
        timestamp_lst = [(x - 1658883600) / 60 for x in requestData.json()['data'][0]['chart']['timestamp']]
        plotItem = pg.PlotItem()
        self.ui.graphicsView.getPlotItem().removeItem(plotItem)
        self.ui.graphicsView.addItem(plotItem.plot(x=range(len(close_lst)), y=close_lst, pen = 'r'))
        self.labelUpdate(requestData)

    def labelUpdate(self, requestData):
        previous_close = requestData.json()['data'][0]['chart']['meta']['previousClose']
        open = requestData.json()['data'][0]['chart']['indicators']['quote'][0]['open'][1]
        limit_up_price = requestData.json()['data'][0]['chart']['meta']["limitUpPrice"]
        limit_down_price = requestData.json()['data'][0]['chart']['meta']["limitDownPrice"]
        close = requestData.json()['data'][0]['chart']['indicators']['quote'][0]['close'][-1]
        updown = close - previous_close
        percentage = updown/previous_close * 100

        self.ui.privious_close_label.setText(str(previous_close))
        self.ui.open_label.setText(str(open))
        self.ui.limit_up_price_label.setText(str(limit_up_price))
        self.ui.limit_down_price_label.setText(str(limit_down_price))
        self.ui.close_label.setText(str(close))
        if percentage >= 0:
            self.ui.up_down_percentage_label.setStyleSheet("color:green")
        else:
            self.ui.up_down_percentage_label.setStyleSheet("color:red")
        self.ui.up_down_percentage_label.setText(f'{round(percentage, 2)}%')
        
