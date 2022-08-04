from PyQt6.QtWidgets import QWidget, QVBoxLayout 
from PyQt6.QtCore import QTimer
from PyQt6 import sip
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib import pyplot as plt
from matplotlib.figure import Figure
from stockWindowUi import Ui_Form
from CrawlerClass import Crawler
import pyqtgraph as pg
import mplfinance as mpf

class stockWindowUiController(QWidget):
    def __init__(self, parent, stock_code):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(parent)

        self.figure = mpf.figure()
        self.canvas = FigureCanvas(self.figure)
        self.ui.plotLayout.addWidget(NavigationToolbar(self.canvas, self))
        self.ui.plotLayout.addWidget(self.canvas)


        self.ui.indicatorComboBox.addItems(['HT_DCPERIOD', 'HT_DCPHASE', 'HT_PHASOR', 'HT_SINE', 'HT_TRENDMODE', 'ADD', 'DIV', 'MAX', 'MAXINDEX', 'MIN', 'MININDEX', 'MINMAX', 'MINMAXINDEX', 'MULT', 'SUB', 'SUM', 'ACOS', 'ASIN', 'ATAN', 'CEIL', 'COS', 'COSH', 'EXP', 'FLOOR', 'LN', 'LOG10', 'SIN', 'SINH', 'SQRT', 'TAN', 'TANH', 'ADX', 'ADXR', 'APO', 'AROON', 'AROONOSC', 'BOP', 'CCI', 'CMO', 'DX', 'MACD', 'MACDEXT', 'MACDFIX', 'MFI', 'MINUS_DI', 'MINUS_DM', 'MOM', 'PLUS_DI', 'PLUS_DM', 'PPO', 'ROC', 'ROCP', 'ROCR', 'ROCR100', 'RSI', 'STOCH', 'STOCHF', 'STOCHRSI', 'TRIX', 'ULTOSC', 'WILLR', 'BBANDS', 'DEMA', 'EMA', 'HT_TRENDLINE', 'KAMA', 'MA', 'MAMA', 'MIDPOINT', 'MIDPRICE', 'SAR', 'SAREXT', 'SMA', 'T3', 'TEMA', 'TRIMA', 'WMA', 'CDL2CROWS', 'CDL3BLACKCROWS', 'CDL3INSIDE', 'CDL3LINESTRIKE', 'CDL3OUTSIDE', 'CDL3STARSINSOUTH', 'CDL3WHITESOLDIERS', 'CDLABANDONEDBABY', 'CDLADVANCEBLOCK', 'CDLBELTHOLD', 'CDLBREAKAWAY', 'CDLCLOSINGMARUBOZU', 'CDLCONCEALBABYSWALL', 'CDLCOUNTERATTACK', 'CDLDARKCLOUDCOVER', 'CDLDOJI', 'CDLDOJISTAR', 'CDLDRAGONFLYDOJI', 'CDLENGULFING', 'CDLEVENINGDOJISTAR', 'CDLEVENINGSTAR', 'CDLGAPSIDESIDEWHITE', 'CDLGRAVESTONEDOJI', 'CDLHAMMER', 'CDLHANGINGMAN', 'CDLHARAMI', 'CDLHARAMICROSS', 'CDLHIGHWAVE', 'CDLHIKKAKE', 'CDLHIKKAKEMOD', 'CDLHOMINGPIGEON', 'CDLIDENTICAL3CROWS', 'CDLINNECK', 'CDLINVERTEDHAMMER', 'CDLKICKING', 'CDLKICKINGBYLENGTH', 'CDLLADDERBOTTOM', 'CDLLONGLEGGEDDOJI', 'CDLLONGLINE', 'CDLMARUBOZU', 'CDLMATCHINGLOW', 'CDLMATHOLD', 'CDLMORNINGDOJISTAR', 'CDLMORNINGSTAR', 'CDLONNECK', 'CDLPIERCING', 'CDLRICKSHAWMAN', 'CDLRISEFALL3METHODS', 'CDLSEPARATINGLINES', 'CDLSHOOTINGSTAR', 'CDLSHORTLINE', 'CDLSPINNINGTOP', 'CDLSTALLEDPATTERN', 'CDLSTICKSANDWICH', 'CDLTAKURI', 'CDLTASUKIGAP', 'CDLTHRUSTING', 'CDLTRISTAR', 'CDLUNIQUE3RIVER', 'CDLUPSIDEGAP2CROWS', 'CDLXSIDEGAP3METHODS', 'AVGPRICE', 'MEDPRICE', 'TYPPRICE', 'WCLPRICE', 'BETA', 'CORREL', 'LINEARREG', 'LINEARREG_ANGLE', 'LINEARREG_INTERCEPT', 'LINEARREG_SLOPE', 'STDDEV', 'TSF', 'VAR', 'ATR', 'NATR', 'TRANGE', 'AD', 'ADOSC', 'OBV'])
        self.ui.indicatorComboBox.setCurrentIndex(0)
        self.ui.intervalComboBox.addItems(["1m", "5m", "15m", "30m", "1h", "1d", "1wk", "1mo"])
        self.ui.intervalComboBox.currentIndexChanged.connect(self.intervalComboBoxChangeEvent)
        self.ui.periodComboBox.currentIndexChanged.connect(self.updateData)
        self.ui.indicatorComboBox.currentIndexChanged.connect(self.updateData)

        self.stock_code = stock_code
        self.updateData()
        self.ui.resetButton.clicked.connect(self.updateData)


    def intervalComboBoxChangeEvent(self):
        self.ui.periodComboBox.clear()
        match self.ui.intervalComboBox.currentText():
            case "1m":
                self.ui.periodComboBox.addItems(["1d", "5d"])
            case "5m":
                self.ui.periodComboBox.addItems(["1d", "5d", "1mo"])
            case "15m":
                self.ui.periodComboBox.addItems(["1d", "5d", "1mo"])
            case "30m":
                self.ui.periodComboBox.addItems(["1d", "5d", "1mo"])
            case "1h":
                self.ui.periodComboBox.addItems(["1d", "5d", "1mo", "3mo", "6mo", "1y"])
            case "1d":
                self.ui.periodComboBox.addItems(["1mo", "3mo", "6mo", "1y", "2y"])
            case "1wk":
                self.ui.periodComboBox.addItems(["1mo", "3mo", "6mo", "1y", "2y"])
            case "1mo":
                self.ui.periodComboBox.addItems(["1y", "2y", "5y", "10y", "max"])
        self.updateData()

    def updateData(self):
        crawler = Crawler(self.stock_code)
        crawler.setIntervalPeriod(interval=self.ui.intervalComboBox.currentText(), period=self.ui.periodComboBox.currentText())
        crawler.get_history_data(self.stock_code)

        self.ui.privious_close_label.setText(str(crawler.stock_data['previous_close']))
        self.ui.open_label.setText(str(round(crawler.stock_data['today_open'][1], 2)))
        self.ui.limit_up_price_label.setText(str(crawler.stock_data['limit_up_price']))
        self.ui.limit_down_price_label.setText(str(crawler.stock_data['limit_down_price']))
        self.ui.close_label.setText(str(round(crawler.stock_data['close'][-1])))
        self.ui.up_down_percentage_label.setStyleSheet("color:red" if crawler.stock_data['percentage'] >= 0 else "color:green")
        self.ui.up_down_percentage_label.setText(f'{round(crawler.stock_data["percentage"], 2)}%')
        self.ui.amplitude_label.setText(str(round(crawler.stock_data['amplitude'], 2)))
        

        if self.canvas:
            self.ui.plotLayout.removeWidget(self.canvas)
            sip.delete(self.canvas)
            plt.cla
            plt.clf()
            plt.close(self.figure)

        #self.line, = self.axes.plot(crawler.ta_list(self.ui.indicatorComboBox.currentText()))
        #self.line, = self.axes.plot(crawler.stock_data['close'].index, crawler.stock_data['close'], "r-")
        #self.updateCanvas(crawler)
        ap = [mpf.make_addplot(crawler.plus_or_minus('y'))]
        self.figure, axlst = mpf.plot(crawler.olddata, type="candle", title="Candlestick", volume = True, ylabel="price($)" , returnfig = True,mav = (5,10,20), addplot=ap)
        self.canvas = FigureCanvas(self.figure)
        self.ui.plotLayout.addWidget(self.canvas)

        """ plotItem = pg.PlotItem(title=crawler.stock_symbol)
        plotItem.plot(y=crawler.stock_data['close'], pen='green')
        plotItem.plot(y=crawler.ta_list_MA(), pen='r')
        plotItem.plot(x=crawler.plus_or_minus('x'), y=crawler.plus_or_minus('y'), pen = 'green', symbol='star')

        self.ui.graphicsView.setCentralItem(plotItem) """
        
        
        print("data updated")
        timer = QTimer()
        timer.timeout.connect(self.updateData)

    def updateCanvas(self, crawler: Crawler):
        self.line.set_data(crawler.olddata['close'].index, crawler.olddata['close'])

