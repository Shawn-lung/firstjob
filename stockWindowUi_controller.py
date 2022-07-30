from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtCore import QTimer
from stockWindowUi import Ui_Form
from CrawlerClass import Crawler
import pyqtgraph as pg

class stockWindowUiController(QWidget):
    def __init__(self, parent, stock_code):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(parent)
        self.stock_code = stock_code
        self.updateData()
        self.ui.resetButton.clicked.connect(self.onResetButtonClicked)

    def onResetButtonClicked(self):
        self.updateData()
        
    def updateData(self):
        crawler = Crawler(self.stock_code)
        
        self.ui.privious_close_label.setText(str(crawler.stock_data['previous_close']))
        self.ui.open_label.setText(str(round(crawler.stock_data['open'][1], 2)))
        self.ui.limit_up_price_label.setText(str(crawler.stock_data['limit_up_price']))
        self.ui.limit_down_price_label.setText(str(crawler.stock_data['limit_down_price']))
        self.ui.close_label.setText(str(crawler.stock_data['close'][-1]))
        self.ui.up_down_percentage_label.setStyleSheet("color:red" if crawler.stock_data['percentage'] >= 0 else "color:green")
        self.ui.up_down_percentage_label.setText(f'{round(crawler.stock_data["percentage"], 2)}%')
        self.ui.amplitude_label.setText(str(round(crawler.stock_data['amplitude'], 2)))
        
        plotItem = pg.PlotItem(title=crawler.stock_symbol)
        plotItem.plot(y=crawler.stock_data['close'], pen='r')
        self.ui.graphicsView.setCentralItem(plotItem)
        
        print("updateData")
        timer = QTimer()
        timer.timeout.connect(self.updateData)

