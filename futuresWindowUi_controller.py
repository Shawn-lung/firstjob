from PyQt6.QtCore import QTimer
from PyQt6.QtWidgets import QWidget
from PyQt6 import sip
from matplotlib import pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from futuresWindowUi import Ui_Form
from CrawlerClass import FuturesCrawler
import mplfinance as mpf
import json

class futuresWindowUiController(QWidget):
    def __init__(self, parent, futures_code, futures_index):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(parent)

        self.indicatorFigure = plt.figure()
        self.indicatorCanvas = FigureCanvas(self.indicatorFigure)
        self.indicatorToolbar = NavigationToolbar(self.indicatorCanvas, self)

        self.mainFigure = mpf.figure()
        self.mainCanvas = FigureCanvas(self.mainFigure)
        self.mainToolbar = NavigationToolbar(self.mainCanvas, self)

        self.subAx = self.indicatorFigure.add_subplot(111)
        
        self.ui.plotLayout.addWidget(self.indicatorCanvas)
        self.ui.plotLayout.addWidget(self.indicatorToolbar)

        self.notifyFlag = True

        self.ui.indicatorComboBox1.addItems(['None', 'ADD', 'DIV', 'MAX', 'MAXINDEX', 'MIN', 'MININDEX', 'MINMAX', 'MINMAXINDEX', 'MULT', 'SUB', 'SUM', 'ACOS', 'ASIN', 'ATAN', 'CEIL', 'COS', 'COSH', 'EXP', 'FLOOR', 'LN', 'LOG10', 'SIN', 'SINH', 'SQRT', 'TAN', 'TANH', 'ADX', 'ADXR', 'APO', 'AROON', 'AROONOSC', 'BOP', 'CCI', 'CMO', 'DX', 'MACD', 'MACDEXT', 'MACDFIX', 'MFI', 'MINUS_DI', 'MINUS_DM', 'MOM', 'PLUS_DI', 'PLUS_DM', 'PPO', 'ROC', 'ROCP', 'ROCR', 'ROCR100', 'RSI', 'STOCH', 'STOCHF', 'STOCHRSI', 'TRIX', 'ULTOSC', 'WILLR', 'BBANDS', 'DEMA', 'EMA', 'HT_TRENDLINE', 'KAMA', 'MA', 'MAMA', 'MIDPOINT', 'MIDPRICE', 'SAR', 'SAREXT', 'SMA', 'T3', 'TEMA', 'TRIMA', 'WMA', 'CDL2CROWS', 'CDL3BLACKCROWS', 'CDL3INSIDE', 'CDL3LINESTRIKE', 'CDL3OUTSIDE', 'CDL3STARSINSOUTH', 'CDL3WHITESOLDIERS', 'CDLABANDONEDBABY', 'CDLADVANCEBLOCK', 'CDLBELTHOLD', 'CDLBREAKAWAY', 'CDLCLOSINGMARUBOZU', 'CDLCONCEALBABYSWALL', 'CDLCOUNTERATTACK', 'CDLDARKCLOUDCOVER', 'CDLDOJI', 'CDLDOJISTAR', 'CDLDRAGONFLYDOJI', 'CDLENGULFING', 'CDLEVENINGDOJISTAR', 'CDLEVENINGSTAR', 'CDLGAPSIDESIDEWHITE', 'CDLGRAVESTONEDOJI', 'CDLHAMMER', 'CDLHANGINGMAN', 'CDLHARAMI', 'CDLHARAMICROSS', 'CDLHIGHWAVE', 'CDLHIKKAKE', 'CDLHIKKAKEMOD', 'CDLHOMINGPIGEON', 'CDLIDENTICAL3CROWS', 'CDLINNECK', 'CDLINVERTEDHAMMER', 'CDLKICKING', 'CDLKICKINGBYLENGTH', 'CDLLADDERBOTTOM', 'CDLLONGLEGGEDDOJI', 'CDLLONGLINE', 'CDLMARUBOZU', 'CDLMATCHINGLOW', 'CDLMATHOLD', 'CDLMORNINGDOJISTAR', 'CDLMORNINGSTAR', 'CDLONNECK', 'CDLPIERCING', 'CDLRICKSHAWMAN', 'CDLRISEFALL3METHODS', 'CDLSEPARATINGLINES', 'CDLSHOOTINGSTAR', 'CDLSHORTLINE', 'CDLSPINNINGTOP', 'CDLSTALLEDPATTERN', 'CDLSTICKSANDWICH', 'CDLTAKURI', 'CDLTASUKIGAP', 'CDLTHRUSTING', 'CDLTRISTAR', 'CDLUNIQUE3RIVER', 'CDLUPSIDEGAP2CROWS', 'CDLXSIDEGAP3METHODS', 'AVGPRICE', 'MEDPRICE', 'TYPPRICE', 'WCLPRICE', 'BETA', 'CORREL', 'LINEARREG', 'LINEARREG_ANGLE', 'LINEARREG_INTERCEPT', 'LINEARREG_SLOPE', 'STDDEV', 'TSF', 'VAR', 'ATR', 'NATR', 'TRANGE', 'AD', 'ADOSC', 'OBV'])
        self.ui.indicatorComboBox2.addItems(['None', 'ADD', 'DIV', 'MAX', 'MAXINDEX', 'MIN', 'MININDEX', 'MINMAX', 'MINMAXINDEX', 'MULT', 'SUB', 'SUM', 'ACOS', 'ASIN', 'ATAN', 'CEIL', 'COS', 'COSH', 'EXP', 'FLOOR', 'LN', 'LOG10', 'SIN', 'SINH', 'SQRT', 'TAN', 'TANH', 'ADX', 'ADXR', 'APO', 'AROON', 'AROONOSC', 'BOP', 'CCI', 'CMO', 'DX', 'MACD', 'MACDEXT', 'MACDFIX', 'MFI', 'MINUS_DI', 'MINUS_DM', 'MOM', 'PLUS_DI', 'PLUS_DM', 'PPO', 'ROC', 'ROCP', 'ROCR', 'ROCR100', 'RSI', 'STOCH', 'STOCHF', 'STOCHRSI', 'TRIX', 'ULTOSC', 'WILLR', 'BBANDS', 'DEMA', 'EMA', 'HT_TRENDLINE', 'KAMA', 'MA', 'MAMA', 'MIDPOINT', 'MIDPRICE', 'SAR', 'SAREXT', 'SMA', 'T3', 'TEMA', 'TRIMA', 'WMA', 'CDL2CROWS', 'CDL3BLACKCROWS', 'CDL3INSIDE', 'CDL3LINESTRIKE', 'CDL3OUTSIDE', 'CDL3STARSINSOUTH', 'CDL3WHITESOLDIERS', 'CDLABANDONEDBABY', 'CDLADVANCEBLOCK', 'CDLBELTHOLD', 'CDLBREAKAWAY', 'CDLCLOSINGMARUBOZU', 'CDLCONCEALBABYSWALL', 'CDLCOUNTERATTACK', 'CDLDARKCLOUDCOVER', 'CDLDOJI', 'CDLDOJISTAR', 'CDLDRAGONFLYDOJI', 'CDLENGULFING', 'CDLEVENINGDOJISTAR', 'CDLEVENINGSTAR', 'CDLGAPSIDESIDEWHITE', 'CDLGRAVESTONEDOJI', 'CDLHAMMER', 'CDLHANGINGMAN', 'CDLHARAMI', 'CDLHARAMICROSS', 'CDLHIGHWAVE', 'CDLHIKKAKE', 'CDLHIKKAKEMOD', 'CDLHOMINGPIGEON', 'CDLIDENTICAL3CROWS', 'CDLINNECK', 'CDLINVERTEDHAMMER', 'CDLKICKING', 'CDLKICKINGBYLENGTH', 'CDLLADDERBOTTOM', 'CDLLONGLEGGEDDOJI', 'CDLLONGLINE', 'CDLMARUBOZU', 'CDLMATCHINGLOW', 'CDLMATHOLD', 'CDLMORNINGDOJISTAR', 'CDLMORNINGSTAR', 'CDLONNECK', 'CDLPIERCING', 'CDLRICKSHAWMAN', 'CDLRISEFALL3METHODS', 'CDLSEPARATINGLINES', 'CDLSHOOTINGSTAR', 'CDLSHORTLINE', 'CDLSPINNINGTOP', 'CDLSTALLEDPATTERN', 'CDLSTICKSANDWICH', 'CDLTAKURI', 'CDLTASUKIGAP', 'CDLTHRUSTING', 'CDLTRISTAR', 'CDLUNIQUE3RIVER', 'CDLUPSIDEGAP2CROWS', 'CDLXSIDEGAP3METHODS', 'AVGPRICE', 'MEDPRICE', 'TYPPRICE', 'WCLPRICE', 'BETA', 'CORREL', 'LINEARREG', 'LINEARREG_ANGLE', 'LINEARREG_INTERCEPT', 'LINEARREG_SLOPE', 'STDDEV', 'TSF', 'VAR', 'ATR', 'NATR', 'TRANGE', 'AD', 'ADOSC', 'OBV'])
        self.ui.indicatorComboBox3.addItems(['None', 'ADD', 'DIV', 'MAX', 'MAXINDEX', 'MIN', 'MININDEX', 'MINMAX', 'MINMAXINDEX', 'MULT', 'SUB', 'SUM', 'ACOS', 'ASIN', 'ATAN', 'CEIL', 'COS', 'COSH', 'EXP', 'FLOOR', 'LN', 'LOG10', 'SIN', 'SINH', 'SQRT', 'TAN', 'TANH', 'ADX', 'ADXR', 'APO', 'AROON', 'AROONOSC', 'BOP', 'CCI', 'CMO', 'DX', 'MACD', 'MACDEXT', 'MACDFIX', 'MFI', 'MINUS_DI', 'MINUS_DM', 'MOM', 'PLUS_DI', 'PLUS_DM', 'PPO', 'ROC', 'ROCP', 'ROCR', 'ROCR100', 'RSI', 'STOCH', 'STOCHF', 'STOCHRSI', 'TRIX', 'ULTOSC', 'WILLR', 'BBANDS', 'DEMA', 'EMA', 'HT_TRENDLINE', 'KAMA', 'MA', 'MAMA', 'MIDPOINT', 'MIDPRICE', 'SAR', 'SAREXT', 'SMA', 'T3', 'TEMA', 'TRIMA', 'WMA', 'CDL2CROWS', 'CDL3BLACKCROWS', 'CDL3INSIDE', 'CDL3LINESTRIKE', 'CDL3OUTSIDE', 'CDL3STARSINSOUTH', 'CDL3WHITESOLDIERS', 'CDLABANDONEDBABY', 'CDLADVANCEBLOCK', 'CDLBELTHOLD', 'CDLBREAKAWAY', 'CDLCLOSINGMARUBOZU', 'CDLCONCEALBABYSWALL', 'CDLCOUNTERATTACK', 'CDLDARKCLOUDCOVER', 'CDLDOJI', 'CDLDOJISTAR', 'CDLDRAGONFLYDOJI', 'CDLENGULFING', 'CDLEVENINGDOJISTAR', 'CDLEVENINGSTAR', 'CDLGAPSIDESIDEWHITE', 'CDLGRAVESTONEDOJI', 'CDLHAMMER', 'CDLHANGINGMAN', 'CDLHARAMI', 'CDLHARAMICROSS', 'CDLHIGHWAVE', 'CDLHIKKAKE', 'CDLHIKKAKEMOD', 'CDLHOMINGPIGEON', 'CDLIDENTICAL3CROWS', 'CDLINNECK', 'CDLINVERTEDHAMMER', 'CDLKICKING', 'CDLKICKINGBYLENGTH', 'CDLLADDERBOTTOM', 'CDLLONGLEGGEDDOJI', 'CDLLONGLINE', 'CDLMARUBOZU', 'CDLMATCHINGLOW', 'CDLMATHOLD', 'CDLMORNINGDOJISTAR', 'CDLMORNINGSTAR', 'CDLONNECK', 'CDLPIERCING', 'CDLRICKSHAWMAN', 'CDLRISEFALL3METHODS', 'CDLSEPARATINGLINES', 'CDLSHOOTINGSTAR', 'CDLSHORTLINE', 'CDLSPINNINGTOP', 'CDLSTALLEDPATTERN', 'CDLSTICKSANDWICH', 'CDLTAKURI', 'CDLTASUKIGAP', 'CDLTHRUSTING', 'CDLTRISTAR', 'CDLUNIQUE3RIVER', 'CDLUPSIDEGAP2CROWS', 'CDLXSIDEGAP3METHODS', 'AVGPRICE', 'MEDPRICE', 'TYPPRICE', 'WCLPRICE', 'BETA', 'CORREL', 'LINEARREG', 'LINEARREG_ANGLE', 'LINEARREG_INTERCEPT', 'LINEARREG_SLOPE', 'STDDEV', 'TSF', 'VAR', 'ATR', 'NATR', 'TRANGE', 'AD', 'ADOSC', 'OBV'])
        self.ui.intervalComboBox.addItems(["1m", "1d", "1w", "1mo"])
        
        with open("favorite.json", encoding="utf-8") as data:
            fav_dict = json.load(data)
            self.ui.indicatorComboBox1.setCurrentText(fav_dict["indicators"][0])
            self.ui.indicatorComboBox2.setCurrentText(fav_dict["indicators"][1])
            self.ui.indicatorComboBox3.setCurrentText(fav_dict["indicators"][2])
        
        self.ui.intervalComboBox.currentIndexChanged.connect(self.intervalComboBoxChangeEvent)
        self.ui.periodComboBox.currentIndexChanged.connect(self.updateData)
        self.ui.indicatorComboBox1.currentIndexChanged.connect(self.updateData)
        self.ui.indicatorComboBox2.currentIndexChanged.connect(self.updateData)
        self.ui.indicatorComboBox3.currentIndexChanged.connect(self.updateData)

        self.ui.confirmButton.clicked.connect(self.onConfirmButtonClicked)

        self.notify_timer = QTimer(self)
        self.notify_timer.timeout.connect(self.notify)
        self.blinkFlag = True
        self.lastmax = 0
        self.lastmin = 0
        
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.updateData)
        self.button_switch_on = True
        self.futures_code = futures_code
        self.futures_index = futures_index
        self.updateData()
        self.ui.resetButton.clicked.connect(self.updateData)
                      
    def oneMinute(self):
        self.timer.start(20000)

    def onConfirmButtonClicked(self):
        if self.ui.confirmButton.text() == "通知:開":
            self.ui.notifyingLabel.setStyleSheet("background-color:transparent")
            self.notifyFlag = False
            self.ui.confirmButton.setText("通知:關")
            self.notify_timer.stop()
        else:
            self.ui.confirmButton.setText("通知:開")
            self.button_switch_on = True

    def notify(self):
        if self.ui.confirmButton.text() == "通知:開":
            self.ui.notifyingLabel.setStyleSheet("background-color:red" if self.blinkFlag else "background-color:transparent")
            self.blinkFlag = not self.blinkFlag
            self.notify_timer.start(500)
    
    def intervalComboBoxChangeEvent(self):
        self.ui.periodComboBox.clear()
        match self.ui.intervalComboBox.currentText():
            case "1m":
                self.ui.periodComboBox.addItems(["1h", "2h", "1d"])
            case "1d":
                self.ui.periodComboBox.addItems(["1mo", "3mo", "6mo", "1y"])
            case "1w":
                self.ui.periodComboBox.addItems(["6mo", "1y", "2y", "5y"])
            case "1mo":
                self.ui.periodComboBox.addItems(["1y", "2y", "5y", "10y"])
        self.updateData()

    def updateData(self):
        crawler = FuturesCrawler(self.futures_code, self.futures_index)
        crawler.setIntervalPeriod(interval=self.ui.intervalComboBox.currentText(), period=self.ui.periodComboBox.currentText())
        crawler.get_tw_futures()
        
        self.ui.open_label.setText(str(crawler.df['open'][-1]))
        self.ui.high_price_label.setText(str(crawler.df['high'][-1]))
        self.ui.low_price_label.setText(str(crawler.df['low'][-1]))
        self.ui.close_label.setText(str(crawler.df['close'][-1]))
        self.ui.amplitude_label.setText(str(round(sorted(crawler.df['close'])[-1]-sorted(crawler.df['close'])[0], 2)))


        if self.mainCanvas:
            self.ui.plotLayout.removeWidget(self.mainCanvas)
            self.ui.plotLayout.removeWidget(self.mainToolbar)
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
        ap = [mpf.make_addplot(crawler.plus_or_minus('y'),type='line', width=0.7 )]
        self.mainFigure, mainAxlst = mpf.plot(crawler.df, type="candle", style=style, volume = True, ylabel="price($)", returnfig=True, addplot=ap)
        mainAxlst[0].set_title(self.futures_code)
        mainAxlst[0].grid(visible=True, which="both", axis="x", ms=1, markevery=1)
        mainAxlst[0].plot(crawler.lastmax_x, crawler.lastmax_y, 'ro' )
        mainAxlst[0].plot(crawler.lastmin_x, crawler.lastmin_y, 'go' )
        mainAxlst[0].plot(crawler.maxpoint_x, crawler.maxpoint_y, 'ro')
        mainAxlst[0].plot(crawler.minpoint_x, crawler.minpoint_y, 'go')
        mainAxlst[0].annotate(f"{round(crawler.lastmax_y, 2)}", xy = (crawler.lastmax_x, crawler.lastmax_y))
        mainAxlst[0].annotate(f"{round(crawler.lastmin_y, 2)}", xy = (crawler.lastmin_x, crawler.lastmin_y),xytext=(crawler.lastmin_x, crawler.lastmin_y-0.05))
        mainAxlst[0].annotate(f"{round(crawler.maxpoint_y, 2)}", xy = (crawler.maxpoint_x,crawler.maxpoint_y))
        mainAxlst[0].annotate(f"{round(crawler.minpoint_y, 2)}", xy = (crawler.minpoint_x, crawler.minpoint_y), xytext=(crawler.minpoint_x, crawler.minpoint_y-0.05))

        self.mainCanvas = FigureCanvas(self.mainFigure)
        self.mainToolbar = NavigationToolbar(self.mainCanvas, self)

        self.ui.plotLayout.insertWidget(0, self.mainCanvas)
        self.ui.plotLayout.insertWidget(0, self.mainToolbar)
        
        self.indicatorFigure.clear()
        self.subAx = self.indicatorFigure.add_subplot(111)
        self.subAx.plot(crawler.ta_list(self.ui.indicatorComboBox1.currentText()))
        self.subAx.plot(crawler.ta_list(self.ui.indicatorComboBox2.currentText()))
        self.subAx.plot(crawler.ta_list(self.ui.indicatorComboBox3.currentText()))
        self.indicatorCanvas.draw()
        self.oneMinute()

        if self.button_switch_on:
            self.lastmax = crawler.lastmax_y
            self.lastmin = crawler.lastmin_y
            self.button_switch_on = False
        
        if self.lastmax != crawler.lastmax_y :
            self.notifyFlag = True
        elif self.lastmin != crawler.lastmin_y:
            self.notifyFlag = True
        
        if crawler.df['close'][-1] >= crawler.lastmax_y and self.notifyFlag == True:            
            self.lastmax = crawler.lastmax_y
            self.lastmin = crawler.lastmin_y
            self.notifyFlag = False
            self.notify()
        elif crawler.df['close'][-1] <= crawler.lastmin_y and self.notifyFlag == True:            
            self.lastmax = crawler.lastmax_y
            self.lastmin = crawler.lastmin_y   
            self.notify()
            self.notifyFlag = False
        
        with open("favorite.json", "r", encoding="utf-8") as data:
            fav_dict = json.load(data)
            fav_dict["indicators"][0] = self.ui.indicatorComboBox1.currentText()
            fav_dict["indicators"][1] = self.ui.indicatorComboBox2.currentText()
            fav_dict["indicators"][2] = self.ui.indicatorComboBox3.currentText()
        with open("favorite.json", "w", encoding="utf-8") as data:
            json.dump(fav_dict, data, ensure_ascii=False)        