from PyQt6.QtWidgets import QWidget
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
        self.ui.resetButton.clicked.connect(self.updateData)

        self.ui.IntervalComboBox.addItems(["1m", "5m", "15m", "30m", "1h", "1d", "1wk", "1mo"])
        self.ui.IntervalComboBox.currentIndexChanged.connect(self.intervalComboBoxChangeEvent)
        self.ui.PeriodComboBox.currentIndexChanged.connect(self.updateData)

    def intervalComboBoxChangeEvent(self):
        self.ui.PeriodComboBox.clear()
        match self.ui.IntervalComboBox.currentText():
            case "1m":
                self.ui.PeriodComboBox.addItems(["1d", "5d"])
            case "5m":
                self.ui.PeriodComboBox.addItems(["1d", "5d", "1mo"])
            case "15m":
                self.ui.PeriodComboBox.addItems(["1d", "5d", "1mo"])
            case "30m":
                self.ui.PeriodComboBox.addItems(["1d", "5d", "1mo"])
            case "1h":
                self.ui.PeriodComboBox.addItems(["1d", "5d", "1mo", "3mo", "6mo", "1y"])
            case "1d":
                self.ui.PeriodComboBox.addItems(["1mo", "3mo", "6mo", "1y", "2y"])
            case "1wk":
                self.ui.PeriodComboBox.addItems(["1mo", "3mo", "6mo", "1y", "2y"])
            case "1mo":
                self.ui.PeriodComboBox.addItems(["1y", "2y", "5y", "10y", "max"])
        self.updateData()

    def updateData(self):
        crawler = Crawler(self.stock_code)
        crawler.setIntervalPeriod(interval=self.ui.IntervalComboBox.currentText(), period=self.ui.PeriodComboBox.currentText())
        crawler.get_history_data(self.stock_code)

        self.ui.privious_close_label.setText(str(crawler.stock_data['previous_close']))
        self.ui.open_label.setText(str(round(crawler.stock_data['open'][0], 2)))
        self.ui.limit_up_price_label.setText(str(crawler.stock_data['limit_up_price']))
        self.ui.limit_down_price_label.setText(str(crawler.stock_data['limit_down_price']))
        self.ui.close_label.setText(str(round(crawler.stock_data['close'][-1])))
        self.ui.up_down_percentage_label.setStyleSheet("color:red" if crawler.stock_data['percentage'] >= 0 else "color:green")
        self.ui.up_down_percentage_label.setText(f'{round(crawler.stock_data["percentage"], 2)}%')
        self.ui.amplitude_label.setText(str(round(crawler.stock_data['amplitude'], 2)))
        
        plotItem = pg.PlotItem(title=crawler.stock_symbol)
        plotItem.plot(y=crawler.stock_data['close'], pen='green')
        plotItem.plot(y=crawler.ta_list_MA(), pen='r')
        plotItem.plot(x=crawler.plus_or_minus('x'), y=crawler.plus_or_minus('y'), symbol='star')

        self.ui.graphicsView.setCentralItem(plotItem)
        
        
        print("updateData")
        timer = QTimer()
        timer.timeout.connect(self.updateData)

