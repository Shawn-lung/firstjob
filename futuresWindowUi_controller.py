from PyQt6.QtCore import QTimer
from PyQt6 import sip
from matplotlib import pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from futuresWindowUi import Ui_Form
from CrawlerClass import FuturesCrawler
from MyWidget import MyWidget
import mplfinance as mpf
import json

class futuresWindowUiController(MyWidget):
    def __init__(self, parent, futures_code, futures_index):
        super().__init__()
        self.prt = parent
        self.prt.ui = Ui_Form()
        self.prt.ui.setupUi(parent)

        self.indicatorFigure = plt.figure()
        self.indicatorCanvas = FigureCanvas(self.indicatorFigure)
        self.indicatorToolbar = NavigationToolbar(self.indicatorCanvas, self)

        self.mainFigure = mpf.figure()
        self.mainCanvas = FigureCanvas(self.mainFigure)
        self.mainToolbar = NavigationToolbar(self.mainCanvas, self)

        self.subAx = self.indicatorFigure.add_subplot(111)
        
        self.prt.ui.plotLayout.addWidget(self.indicatorCanvas)
        self.prt.ui.plotLayout.addWidget(self.indicatorToolbar)

        self.notifyFlag = True

        self.prt.ui.indicatorComboBox1.addItems(['None', 'ADX', 'ADXR', 'APO', 'AROON', 'AROONOSC', 'BOP', 'CCI', 'CMO', 'DX', 'MACD', 'MACDEXT', 'MACDFIX', 'MFI', 'MINUS_DI', 'MINUS_DM', 'MOM', 'PLUS_DI', 'PLUS_DM', 'PPO', 'ROC', 'ROCP', 'ROCR', 'ROCR100', 'RSI', 'KD', 'STOCHF', 'STOCHRSI', 'TRIX', 'ULTOSC', 'WILLR', 'BBANDS', 'DEMA', 'EMA', 'HT_TRENDLINE', 'KAMA', 'MA', 'MAMA', 'MIDPOINT', 'MIDPRICE', 'SAR', 'SAREXT', 'SMA', 'T3', 'TEMA', 'TRIMA', 'WMA', 'CDL2CROWS', 'CDL3BLACKCROWS', 'CDL3INSIDE', 'CDL3LINESTRIKE', 'CDL3OUTSIDE', 'CDL3STARSINSOUTH', 'CDL3WHITESOLDIERS', 'CDLABANDONEDBABY', 'CDLADVANCEBLOCK', 'CDLBELTHOLD', 'CDLBREAKAWAY', 'CDLCLOSINGMARUBOZU', 'CDLCONCEALBABYSWALL', 'CDLCOUNTERATTACK', 'CDLDARKCLOUDCOVER', 'CDLDOJI', 'CDLDOJISTAR', 'CDLDRAGONFLYDOJI', 'CDLENGULFING', 'CDLEVENINGDOJISTAR', 'CDLEVENINGSTAR', 'CDLGAPSIDESIDEWHITE', 'CDLGRAVESTONEDOJI', 'CDLHAMMER', 'CDLHANGINGMAN', 'CDLHARAMI', 'CDLHARAMICROSS', 'CDLHIGHWAVE', 'CDLHIKKAKE', 'CDLHIKKAKEMOD', 'CDLHOMINGPIGEON', 'CDLIDENTICAL3CROWS', 'CDLINNECK', 'CDLINVERTEDHAMMER', 'CDLKICKING', 'CDLKICKINGBYLENGTH', 'CDLLADDERBOTTOM', 'CDLLONGLEGGEDDOJI', 'CDLLONGLINE', 'CDLMARUBOZU', 'CDLMATCHINGLOW', 'CDLMATHOLD', 'CDLMORNINGDOJISTAR', 'CDLMORNINGSTAR', 'CDLONNECK', 'CDLPIERCING', 'CDLRICKSHAWMAN', 'CDLRISEFALL3METHODS', 'CDLSEPARATINGLINES', 'CDLSHOOTINGSTAR', 'CDLSHORTLINE', 'CDLSPINNINGTOP', 'CDLSTALLEDPATTERN', 'CDLSTICKSANDWICH', 'CDLTAKURI', 'CDLTASUKIGAP', 'CDLTHRUSTING', 'CDLTRISTAR', 'CDLUNIQUE3RIVER', 'CDLUPSIDEGAP2CROWS', 'CDLXSIDEGAP3METHODS', 'AVGPRICE', 'MEDPRICE', 'TYPPRICE', 'WCLPRICE', 'BETA', 'CORREL', 'LINEARREG', 'LINEARREG_ANGLE', 'LINEARREG_INTERCEPT', 'LINEARREG_SLOPE', 'STDDEV', 'TSF', 'VAR', 'ATR', 'NATR', 'TRANGE', 'AD', 'ADOSC', 'OBV'])
        self.prt.ui.indicatorComboBox2.addItems(['None', 'ADX', 'ADXR', 'APO', 'AROON', 'AROONOSC', 'BOP', 'CCI', 'CMO', 'DX', 'MACD', 'MACDEXT', 'MACDFIX', 'MFI', 'MINUS_DI', 'MINUS_DM', 'MOM', 'PLUS_DI', 'PLUS_DM', 'PPO', 'ROC', 'ROCP', 'ROCR', 'ROCR100', 'RSI', 'KD', 'STOCHF', 'STOCHRSI', 'TRIX', 'ULTOSC', 'WILLR', 'BBANDS', 'DEMA', 'EMA', 'HT_TRENDLINE', 'KAMA', 'MA', 'MAMA', 'MIDPOINT', 'MIDPRICE', 'SAR', 'SAREXT', 'SMA', 'T3', 'TEMA', 'TRIMA', 'WMA', 'CDL2CROWS', 'CDL3BLACKCROWS', 'CDL3INSIDE', 'CDL3LINESTRIKE', 'CDL3OUTSIDE', 'CDL3STARSINSOUTH', 'CDL3WHITESOLDIERS', 'CDLABANDONEDBABY', 'CDLADVANCEBLOCK', 'CDLBELTHOLD', 'CDLBREAKAWAY', 'CDLCLOSINGMARUBOZU', 'CDLCONCEALBABYSWALL', 'CDLCOUNTERATTACK', 'CDLDARKCLOUDCOVER', 'CDLDOJI', 'CDLDOJISTAR', 'CDLDRAGONFLYDOJI', 'CDLENGULFING', 'CDLEVENINGDOJISTAR', 'CDLEVENINGSTAR', 'CDLGAPSIDESIDEWHITE', 'CDLGRAVESTONEDOJI', 'CDLHAMMER', 'CDLHANGINGMAN', 'CDLHARAMI', 'CDLHARAMICROSS', 'CDLHIGHWAVE', 'CDLHIKKAKE', 'CDLHIKKAKEMOD', 'CDLHOMINGPIGEON', 'CDLIDENTICAL3CROWS', 'CDLINNECK', 'CDLINVERTEDHAMMER', 'CDLKICKING', 'CDLKICKINGBYLENGTH', 'CDLLADDERBOTTOM', 'CDLLONGLEGGEDDOJI', 'CDLLONGLINE', 'CDLMARUBOZU', 'CDLMATCHINGLOW', 'CDLMATHOLD', 'CDLMORNINGDOJISTAR', 'CDLMORNINGSTAR', 'CDLONNECK', 'CDLPIERCING', 'CDLRICKSHAWMAN', 'CDLRISEFALL3METHODS', 'CDLSEPARATINGLINES', 'CDLSHOOTINGSTAR', 'CDLSHORTLINE', 'CDLSPINNINGTOP', 'CDLSTALLEDPATTERN', 'CDLSTICKSANDWICH', 'CDLTAKURI', 'CDLTASUKIGAP', 'CDLTHRUSTING', 'CDLTRISTAR', 'CDLUNIQUE3RIVER', 'CDLUPSIDEGAP2CROWS', 'CDLXSIDEGAP3METHODS', 'AVGPRICE', 'MEDPRICE', 'TYPPRICE', 'WCLPRICE', 'BETA', 'CORREL', 'LINEARREG', 'LINEARREG_ANGLE', 'LINEARREG_INTERCEPT', 'LINEARREG_SLOPE', 'STDDEV', 'TSF', 'VAR', 'ATR', 'NATR', 'TRANGE', 'AD', 'ADOSC', 'OBV'])
        self.prt.ui.indicatorComboBox3.addItems(['None', 'ADX', 'ADXR', 'APO', 'AROON', 'AROONOSC', 'BOP', 'CCI', 'CMO', 'DX', 'MACD', 'MACDEXT', 'MACDFIX', 'MFI', 'MINUS_DI', 'MINUS_DM', 'MOM', 'PLUS_DI', 'PLUS_DM', 'PPO', 'ROC', 'ROCP', 'ROCR', 'ROCR100', 'RSI', 'KD', 'STOCHF', 'STOCHRSI', 'TRIX', 'ULTOSC', 'WILLR', 'BBANDS', 'DEMA', 'EMA', 'HT_TRENDLINE', 'KAMA', 'MA', 'MAMA', 'MIDPOINT', 'MIDPRICE', 'SAR', 'SAREXT', 'SMA', 'T3', 'TEMA', 'TRIMA', 'WMA', 'CDL2CROWS', 'CDL3BLACKCROWS', 'CDL3INSIDE', 'CDL3LINESTRIKE', 'CDL3OUTSIDE', 'CDL3STARSINSOUTH', 'CDL3WHITESOLDIERS', 'CDLABANDONEDBABY', 'CDLADVANCEBLOCK', 'CDLBELTHOLD', 'CDLBREAKAWAY', 'CDLCLOSINGMARUBOZU', 'CDLCONCEALBABYSWALL', 'CDLCOUNTERATTACK', 'CDLDARKCLOUDCOVER', 'CDLDOJI', 'CDLDOJISTAR', 'CDLDRAGONFLYDOJI', 'CDLENGULFING', 'CDLEVENINGDOJISTAR', 'CDLEVENINGSTAR', 'CDLGAPSIDESIDEWHITE', 'CDLGRAVESTONEDOJI', 'CDLHAMMER', 'CDLHANGINGMAN', 'CDLHARAMI', 'CDLHARAMICROSS', 'CDLHIGHWAVE', 'CDLHIKKAKE', 'CDLHIKKAKEMOD', 'CDLHOMINGPIGEON', 'CDLIDENTICAL3CROWS', 'CDLINNECK', 'CDLINVERTEDHAMMER', 'CDLKICKING', 'CDLKICKINGBYLENGTH', 'CDLLADDERBOTTOM', 'CDLLONGLEGGEDDOJI', 'CDLLONGLINE', 'CDLMARUBOZU', 'CDLMATCHINGLOW', 'CDLMATHOLD', 'CDLMORNINGDOJISTAR', 'CDLMORNINGSTAR', 'CDLONNECK', 'CDLPIERCING', 'CDLRICKSHAWMAN', 'CDLRISEFALL3METHODS', 'CDLSEPARATINGLINES', 'CDLSHOOTINGSTAR', 'CDLSHORTLINE', 'CDLSPINNINGTOP', 'CDLSTALLEDPATTERN', 'CDLSTICKSANDWICH', 'CDLTAKURI', 'CDLTASUKIGAP', 'CDLTHRUSTING', 'CDLTRISTAR', 'CDLUNIQUE3RIVER', 'CDLUPSIDEGAP2CROWS', 'CDLXSIDEGAP3METHODS', 'AVGPRICE', 'MEDPRICE', 'TYPPRICE', 'WCLPRICE', 'BETA', 'CORREL', 'LINEARREG', 'LINEARREG_ANGLE', 'LINEARREG_INTERCEPT', 'LINEARREG_SLOPE', 'STDDEV', 'TSF', 'VAR', 'ATR', 'NATR', 'TRANGE', 'AD', 'ADOSC', 'OBV'])
        self.prt.ui.intervalComboBox.addItems(["1m", "5m", "15m", "30m", "1d", "1w", "1mo"])
        self.prt.ui.periodComboBox.addItems(["1h", "2h", "1d"])

        with open("favorite.json", encoding="utf-8") as data:
            fav_dict = json.load(data)
            self.prt.ui.indicatorComboBox1.setCurrentText(fav_dict["indicators"][0])
            self.prt.ui.indicatorComboBox2.setCurrentText(fav_dict["indicators"][1])
            self.prt.ui.indicatorComboBox3.setCurrentText(fav_dict["indicators"][2])
        
        self.prt.ui.intervalComboBox.currentIndexChanged.connect(self.intervalComboBoxChangeEvent)
        self.prt.ui.periodComboBox.currentIndexChanged.connect(self.updateData)
        self.prt.ui.indicatorComboBox1.currentIndexChanged.connect(self.updateData)
        self.prt.ui.indicatorComboBox2.currentIndexChanged.connect(self.updateData)
        self.prt.ui.indicatorComboBox3.currentIndexChanged.connect(self.updateData)

        self.prt.ui.confirmButton.clicked.connect(self.onConfirmButtonClicked)

        self.prt.candleBars = []
        self.prt.candleBarIndex = -1

        self.notify_timer = QTimer(self)
        self.notify_timer.timeout.connect(self.notify)
        self.blinkFlag = True
        self.lastmax = 0
        self.lastmin = 0
        
        self.prt.timer = QTimer(self)
        self.prt.timer.timeout.connect(self.updateData)
        self.button_switch_on = True
        self.futures_code = futures_code
        self.futures_index = futures_index
        self.updateData()
        self.prt.ui.resetButton.clicked.connect(self.updateData)
                      
    def oneMinute(self):
        self.prt.timer.start(60000)

    def onConfirmButtonClicked(self):
        if self.prt.ui.confirmButton.text() == "通知:開":
            self.prt.ui.notifyingLabel.setStyleSheet("background-color:transparent")
            self.notifyFlag = False
            self.prt.ui.confirmButton.setText("通知:關")
            self.notify_timer.stop()
        else:
            self.prt.ui.confirmButton.setText("通知:開")
            self.button_switch_on = True

    def notify(self):
        if self.prt.ui.confirmButton.text() == "通知:開":
            self.prt.ui.notifyingLabel.setStyleSheet("background-color:red" if self.blinkFlag else "background-color:transparent")
            self.blinkFlag = not self.blinkFlag
            self.notify_timer.start(500)
    
    def intervalComboBoxChangeEvent(self):
        self.prt.ui.periodComboBox.clear()
        match self.prt.ui.intervalComboBox.currentText():
            case "1m":
                self.prt.ui.periodComboBox.addItems(["1h", "2h", "1d"])
            case "5m":
                self.prt.ui.periodComboBox.addItems(["1h", "2h", "1d"])
            case "15m":
                self.prt.ui.periodComboBox.addItems(["1h", "2h", "1d"])
            case "30m":
                self.prt.ui.periodComboBox.addItems(["1h", "2h", "1d"])            
            case "1d":
                self.prt.ui.periodComboBox.addItems(["1mo", "3mo", "6mo", "1y"])
            case "1w":
                self.prt.ui.periodComboBox.addItems(["6mo", "1y", "2y", "5y"])
            case "1mo":
                self.prt.ui.periodComboBox.addItems(["1y", "2y", "5y", "10y"])
        self.updateData()

    def updateData(self):

        self.crawlData()
        self.prt.ui.open_label.setText(str(self.prt.crawler.df['open'][-1]))
        self.prt.ui.high_price_label.setText(str(self.prt.crawler.df['high'][-1]))
        self.prt.ui.low_price_label.setText(str(self.prt.crawler.df['low'][-1]))
        self.prt.ui.close_label.setText(str(self.prt.crawler.df['close'][-1]))
        self.prt.ui.amplitude_label.setText(str(round(sorted(self.prt.crawler.df['close'])[-1]-sorted(self.prt.crawler.df['close'])[0], 2)))

        self.plotData()
        self.oneMinute()

        if self.button_switch_on:
            self.lastmax = self.prt.crawler.lastmax_y
            self.lastmin = self.prt.crawler.lastmin_y
            self.button_switch_on = False
        
        if self.lastmax != self.prt.crawler.lastmax_y :
            self.notifyFlag = True
        elif self.lastmin != self.prt.crawler.lastmin_y:
            self.notifyFlag = True
        
        if self.prt.crawler.df['close'][-1] >= self.prt.crawler.lastmax_y and self.notifyFlag == True:            
            self.lastmax = self.prt.crawler.lastmax_y
            self.lastmin = self.prt.crawler.lastmin_y
            self.notifyFlag = False
            self.notify()
        elif self.prt.crawler.df['close'][-1] <= self.prt.crawler.lastmin_y and self.notifyFlag == True:            
            self.lastmax = self.prt.crawler.lastmax_y
            self.lastmin = self.prt.crawler.lastmin_y   
            self.notify()
            self.notifyFlag = False

    def crawlData(self):
        self.prt.crawler = FuturesCrawler(self.futures_code, self.futures_index)
        self.prt.crawler.setIntervalPeriod(interval=self.prt.ui.intervalComboBox.currentText(), period=self.prt.ui.periodComboBox.currentText())
        self.prt.crawler.get_tw_futures()
        self.prt.candleBarIndex = -1
        self.prt.candleBars = [self.prt.crawler.df.index[-1], self.prt.crawler.df['open'][-1], self.prt.crawler.df['high'][-1], self.prt.crawler.df['low'][-1], self.prt.crawler.df['close'][-1]]
        self.prt.ui.tLabel.setText(str(self.prt.candleBars[0]))
        self.prt.ui.oLabel.setText(str(self.prt.candleBars[1]))
        self.prt.ui.hLabel.setText(str(self.prt.candleBars[2]))
        self.prt.ui.lLabel.setText(str(self.prt.candleBars[3]))
        self.prt.ui.cLabel.setText(str(self.prt.candleBars[4]))

    def plotData(self):
        if self.mainCanvas:
            self.prt.ui.plotLayout.removeWidget(self.mainCanvas)
            self.prt.ui.plotLayout.removeWidget(self.mainToolbar)
            sip.delete(self.mainCanvas)
            plt.cla()
            self.mainFigure.clear()
            plt.close(self.mainFigure)

        mc = mpf.make_marketcolors(
            up="red",  
            down="green",  
            edge="black",  
            volume="blue", 
            wick="black")
        
        style = mpf.make_mpf_style(base_mpl_style="ggplot", marketcolors=mc)
        ap = [mpf.make_addplot(self.prt.crawler.plus_or_minus('y'),type='line', width=0.7 )]
        self.mainFigure, mainAxlst = mpf.plot(self.prt.crawler.df, type="candle", style=style, volume = True, returnfig=True, addplot=ap)
        mainAxlst[0].set_title(self.futures_code)
        mainAxlst[0].grid(visible=True, which="both", axis="x", ms=1, markevery=1)
        mainAxlst[0].plot(self.prt.crawler.lastmax_x, self.prt.crawler.lastmax_y, 'ro' )
        mainAxlst[0].plot(self.prt.crawler.lastmin_x, self.prt.crawler.lastmin_y, 'go' )
        mainAxlst[0].plot(self.prt.crawler.maxpoint_x, self.prt.crawler.maxpoint_y, 'ro')
        mainAxlst[0].plot(self.prt.crawler.minpoint_x, self.prt.crawler.minpoint_y, 'go')
        mainAxlst[0].annotate(f"{round(self.prt.crawler.lastmax_y, 2)}", xy = (self.prt.crawler.lastmax_x, self.prt.crawler.lastmax_y))
        mainAxlst[0].annotate(f"{round(self.prt.crawler.lastmin_y, 2)}", xy = (self.prt.crawler.lastmin_x, self.prt.crawler.lastmin_y),xytext=(self.prt.crawler.lastmin_x, self.prt.crawler.lastmin_y - 0.1*self.prt.crawler.amplitude))
        mainAxlst[0].annotate(f"{round(self.prt.crawler.maxpoint_y, 2)}", xy = (self.prt.crawler.maxpoint_x,self.prt.crawler.maxpoint_y))
        mainAxlst[0].annotate(f"{round(self.prt.crawler.minpoint_y, 2)}", xy = (self.prt.crawler.minpoint_x, self.prt.crawler.minpoint_y), xytext=(self.prt.crawler.minpoint_x, self.prt.crawler.minpoint_y - 0.1*self.prt.crawler.amplitude))

        self.mainCanvas = FigureCanvas(self.mainFigure)
        self.mainToolbar = NavigationToolbar(self.mainCanvas, self)

        self.prt.ui.plotLayout.insertWidget(0, self.mainCanvas)
        self.prt.ui.plotLayout.insertWidget(0, self.mainToolbar)
        
        self.indicatorFigure.clear()
        self.subAx = self.indicatorFigure.add_subplot(111)
        self.subAx.plot(self.prt.crawler.ta_list('STOCH' if self.prt.ui.indicatorComboBox1.currentText() == 'KD' else self.prt.ui.indicatorComboBox1.currentText()))
        self.subAx.plot(self.prt.crawler.ta_list('STOCH' if self.prt.ui.indicatorComboBox1.currentText() == 'KD' else self.prt.ui.indicatorComboBox1.currentText()))
        self.subAx.plot(self.prt.crawler.ta_list('STOCH' if self.prt.ui.indicatorComboBox1.currentText() == 'KD' else self.prt.ui.indicatorComboBox1.currentText()))
        self.indicatorCanvas.draw()
