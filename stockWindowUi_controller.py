from PyQt6.QtWidgets import QWidget, QMessageBox
from PyQt6.QtCore import QTimer
from PyQt6 import sip
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib import pyplot as plt
from stockWindowUi import Ui_Form
from CrawlerClass import StockCrawler
import mplfinance as mpf

class stockWindowUiController(QWidget):
    def __init__(self, parent, stock_code):
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


        self.ui.indicatorComboBox1.addItems(['None', 'ADD', 'DIV', 'MAX', 'MAXINDEX', 'MIN', 'MININDEX', 'MINMAX', 'MINMAXINDEX', 'MULT', 'SUB', 'SUM', 'ACOS', 'ASIN', 'ATAN', 'CEIL', 'COS', 'COSH', 'EXP', 'FLOOR', 'LN', 'LOG10', 'SIN', 'SINH', 'SQRT', 'TAN', 'TANH', 'ADX', 'ADXR', 'APO', 'AROON', 'AROONOSC', 'BOP', 'CCI', 'CMO', 'DX', 'MACD', 'MACDEXT', 'MACDFIX', 'MFI', 'MINUS_DI', 'MINUS_DM', 'MOM', 'PLUS_DI', 'PLUS_DM', 'PPO', 'ROC', 'ROCP', 'ROCR', 'ROCR100', 'RSI', 'STOCH', 'STOCHF', 'STOCHRSI', 'TRIX', 'ULTOSC', 'WILLR', 'BBANDS', 'DEMA', 'EMA', 'HT_TRENDLINE', 'KAMA', 'MA', 'MAMA', 'MIDPOINT', 'MIDPRICE', 'SAR', 'SAREXT', 'SMA', 'T3', 'TEMA', 'TRIMA', 'WMA', 'CDL2CROWS', 'CDL3BLACKCROWS', 'CDL3INSIDE', 'CDL3LINESTRIKE', 'CDL3OUTSIDE', 'CDL3STARSINSOUTH', 'CDL3WHITESOLDIERS', 'CDLABANDONEDBABY', 'CDLADVANCEBLOCK', 'CDLBELTHOLD', 'CDLBREAKAWAY', 'CDLCLOSINGMARUBOZU', 'CDLCONCEALBABYSWALL', 'CDLCOUNTERATTACK', 'CDLDARKCLOUDCOVER', 'CDLDOJI', 'CDLDOJISTAR', 'CDLDRAGONFLYDOJI', 'CDLENGULFING', 'CDLEVENINGDOJISTAR', 'CDLEVENINGSTAR', 'CDLGAPSIDESIDEWHITE', 'CDLGRAVESTONEDOJI', 'CDLHAMMER', 'CDLHANGINGMAN', 'CDLHARAMI', 'CDLHARAMICROSS', 'CDLHIGHWAVE', 'CDLHIKKAKE', 'CDLHIKKAKEMOD', 'CDLHOMINGPIGEON', 'CDLIDENTICAL3CROWS', 'CDLINNECK', 'CDLINVERTEDHAMMER', 'CDLKICKING', 'CDLKICKINGBYLENGTH', 'CDLLADDERBOTTOM', 'CDLLONGLEGGEDDOJI', 'CDLLONGLINE', 'CDLMARUBOZU', 'CDLMATCHINGLOW', 'CDLMATHOLD', 'CDLMORNINGDOJISTAR', 'CDLMORNINGSTAR', 'CDLONNECK', 'CDLPIERCING', 'CDLRICKSHAWMAN', 'CDLRISEFALL3METHODS', 'CDLSEPARATINGLINES', 'CDLSHOOTINGSTAR', 'CDLSHORTLINE', 'CDLSPINNINGTOP', 'CDLSTALLEDPATTERN', 'CDLSTICKSANDWICH', 'CDLTAKURI', 'CDLTASUKIGAP', 'CDLTHRUSTING', 'CDLTRISTAR', 'CDLUNIQUE3RIVER', 'CDLUPSIDEGAP2CROWS', 'CDLXSIDEGAP3METHODS', 'AVGPRICE', 'MEDPRICE', 'TYPPRICE', 'WCLPRICE', 'BETA', 'CORREL', 'LINEARREG', 'LINEARREG_ANGLE', 'LINEARREG_INTERCEPT', 'LINEARREG_SLOPE', 'STDDEV', 'TSF', 'VAR', 'ATR', 'NATR', 'TRANGE', 'AD', 'ADOSC', 'OBV'])
        self.ui.indicatorComboBox2.addItems([ 'None', 'ADD', 'DIV', 'MAX', 'MAXINDEX', 'MIN', 'MININDEX', 'MINMAX', 'MINMAXINDEX', 'MULT', 'SUB', 'SUM', 'ACOS', 'ASIN', 'ATAN', 'CEIL', 'COS', 'COSH', 'EXP', 'FLOOR', 'LN', 'LOG10', 'SIN', 'SINH', 'SQRT', 'TAN', 'TANH', 'ADX', 'ADXR', 'APO', 'AROON', 'AROONOSC', 'BOP', 'CCI', 'CMO', 'DX', 'MACD', 'MACDEXT', 'MACDFIX', 'MFI', 'MINUS_DI', 'MINUS_DM', 'MOM', 'PLUS_DI', 'PLUS_DM', 'PPO', 'ROC', 'ROCP', 'ROCR', 'ROCR100', 'RSI', 'STOCH', 'STOCHF', 'STOCHRSI', 'TRIX', 'ULTOSC', 'WILLR', 'BBANDS', 'DEMA', 'EMA', 'HT_TRENDLINE', 'KAMA', 'MA', 'MAMA', 'MIDPOINT', 'MIDPRICE', 'SAR', 'SAREXT', 'SMA', 'T3', 'TEMA', 'TRIMA', 'WMA', 'CDL2CROWS', 'CDL3BLACKCROWS', 'CDL3INSIDE', 'CDL3LINESTRIKE', 'CDL3OUTSIDE', 'CDL3STARSINSOUTH', 'CDL3WHITESOLDIERS', 'CDLABANDONEDBABY', 'CDLADVANCEBLOCK', 'CDLBELTHOLD', 'CDLBREAKAWAY', 'CDLCLOSINGMARUBOZU', 'CDLCONCEALBABYSWALL', 'CDLCOUNTERATTACK', 'CDLDARKCLOUDCOVER', 'CDLDOJI', 'CDLDOJISTAR', 'CDLDRAGONFLYDOJI', 'CDLENGULFING', 'CDLEVENINGDOJISTAR', 'CDLEVENINGSTAR', 'CDLGAPSIDESIDEWHITE', 'CDLGRAVESTONEDOJI', 'CDLHAMMER', 'CDLHANGINGMAN', 'CDLHARAMI', 'CDLHARAMICROSS', 'CDLHIGHWAVE', 'CDLHIKKAKE', 'CDLHIKKAKEMOD', 'CDLHOMINGPIGEON', 'CDLIDENTICAL3CROWS', 'CDLINNECK', 'CDLINVERTEDHAMMER', 'CDLKICKING', 'CDLKICKINGBYLENGTH', 'CDLLADDERBOTTOM', 'CDLLONGLEGGEDDOJI', 'CDLLONGLINE', 'CDLMARUBOZU', 'CDLMATCHINGLOW', 'CDLMATHOLD', 'CDLMORNINGDOJISTAR', 'CDLMORNINGSTAR', 'CDLONNECK', 'CDLPIERCING', 'CDLRICKSHAWMAN', 'CDLRISEFALL3METHODS', 'CDLSEPARATINGLINES', 'CDLSHOOTINGSTAR', 'CDLSHORTLINE', 'CDLSPINNINGTOP', 'CDLSTALLEDPATTERN', 'CDLSTICKSANDWICH', 'CDLTAKURI', 'CDLTASUKIGAP', 'CDLTHRUSTING', 'CDLTRISTAR', 'CDLUNIQUE3RIVER', 'CDLUPSIDEGAP2CROWS', 'CDLXSIDEGAP3METHODS', 'AVGPRICE', 'MEDPRICE', 'TYPPRICE', 'WCLPRICE', 'BETA', 'CORREL', 'LINEARREG', 'LINEARREG_ANGLE', 'LINEARREG_INTERCEPT', 'LINEARREG_SLOPE', 'STDDEV', 'TSF', 'VAR', 'ATR', 'NATR', 'TRANGE', 'AD', 'ADOSC', 'OBV'])
        self.ui.indicatorComboBox3.addItems(['None', 'ADD', 'DIV', 'MAX', 'MAXINDEX', 'MIN', 'MININDEX', 'MINMAX', 'MINMAXINDEX', 'MULT', 'SUB', 'SUM', 'ACOS', 'ASIN', 'ATAN', 'CEIL', 'COS', 'COSH', 'EXP', 'FLOOR', 'LN', 'LOG10', 'SIN', 'SINH', 'SQRT', 'TAN', 'TANH', 'ADX', 'ADXR', 'APO', 'AROON', 'AROONOSC', 'BOP', 'CCI', 'CMO', 'DX', 'MACD', 'MACDEXT', 'MACDFIX', 'MFI', 'MINUS_DI', 'MINUS_DM', 'MOM', 'PLUS_DI', 'PLUS_DM', 'PPO', 'ROC', 'ROCP', 'ROCR', 'ROCR100', 'RSI', 'STOCH', 'STOCHF', 'STOCHRSI', 'TRIX', 'ULTOSC', 'WILLR', 'BBANDS', 'DEMA', 'EMA', 'HT_TRENDLINE', 'KAMA', 'MA', 'MAMA', 'MIDPOINT', 'MIDPRICE', 'SAR', 'SAREXT', 'SMA', 'T3', 'TEMA', 'TRIMA', 'WMA', 'CDL2CROWS', 'CDL3BLACKCROWS', 'CDL3INSIDE', 'CDL3LINESTRIKE', 'CDL3OUTSIDE', 'CDL3STARSINSOUTH', 'CDL3WHITESOLDIERS', 'CDLABANDONEDBABY', 'CDLADVANCEBLOCK', 'CDLBELTHOLD', 'CDLBREAKAWAY', 'CDLCLOSINGMARUBOZU', 'CDLCONCEALBABYSWALL', 'CDLCOUNTERATTACK', 'CDLDARKCLOUDCOVER', 'CDLDOJI', 'CDLDOJISTAR', 'CDLDRAGONFLYDOJI', 'CDLENGULFING', 'CDLEVENINGDOJISTAR', 'CDLEVENINGSTAR', 'CDLGAPSIDESIDEWHITE', 'CDLGRAVESTONEDOJI', 'CDLHAMMER', 'CDLHANGINGMAN', 'CDLHARAMI', 'CDLHARAMICROSS', 'CDLHIGHWAVE', 'CDLHIKKAKE', 'CDLHIKKAKEMOD', 'CDLHOMINGPIGEON', 'CDLIDENTICAL3CROWS', 'CDLINNECK', 'CDLINVERTEDHAMMER', 'CDLKICKING', 'CDLKICKINGBYLENGTH', 'CDLLADDERBOTTOM', 'CDLLONGLEGGEDDOJI', 'CDLLONGLINE', 'CDLMARUBOZU', 'CDLMATCHINGLOW', 'CDLMATHOLD', 'CDLMORNINGDOJISTAR', 'CDLMORNINGSTAR', 'CDLONNECK', 'CDLPIERCING', 'CDLRICKSHAWMAN', 'CDLRISEFALL3METHODS', 'CDLSEPARATINGLINES', 'CDLSHOOTINGSTAR', 'CDLSHORTLINE', 'CDLSPINNINGTOP', 'CDLSTALLEDPATTERN', 'CDLSTICKSANDWICH', 'CDLTAKURI', 'CDLTASUKIGAP', 'CDLTHRUSTING', 'CDLTRISTAR', 'CDLUNIQUE3RIVER', 'CDLUPSIDEGAP2CROWS', 'CDLXSIDEGAP3METHODS', 'AVGPRICE', 'MEDPRICE', 'TYPPRICE', 'WCLPRICE', 'BETA', 'CORREL', 'LINEARREG', 'LINEARREG_ANGLE', 'LINEARREG_INTERCEPT', 'LINEARREG_SLOPE', 'STDDEV', 'TSF', 'VAR', 'ATR', 'NATR', 'TRANGE', 'AD', 'ADOSC', 'OBV'])        
        self.ui.intervalComboBox.addItems(["1m", "5m", "15m", "30m", "1h", "1d", "1wk", "1mo"])
        self.ui.intervalComboBox.currentIndexChanged.connect(self.intervalComboBoxChangeEvent)
        self.ui.periodComboBox.currentIndexChanged.connect(self.updateData)
        self.ui.indicatorComboBox1.currentIndexChanged.connect(self.updateData)
        self.ui.indicatorComboBox2.currentIndexChanged.connect(self.updateData)
        self.ui.indicatorComboBox3.currentIndexChanged.connect(self.updateData)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.updateData)

        self.stock_code = stock_code
        self.updateData()
        self.ui.resetButton.clicked.connect(self.updateData)

    def intervalComboBoxChangeEvent(self):
        self.ui.periodComboBox.clear()
        match self.ui.intervalComboBox.currentText():
            case "1m":
                self.ui.periodComboBox.addItems(["1h", "2h", "1d", "5d"])
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

    def oneMinute(self):
        self.timer.start(60000)

    def updateData(self):
        print('data updated')
        crawler = StockCrawler(self.stock_code)
        crawler.setIntervalPeriod(interval=self.ui.intervalComboBox.currentText(), period=self.ui.periodComboBox.currentText())
        crawler.get_history_data(self.stock_code)

        try :
            self.ui.privious_close_label.setText(str(crawler.stock_data['previous_close']))
            self.ui.open_label.setText(str(round(crawler.stock_data['today_open'][1], 2)))

        except TypeError:
            QMessageBox.warning(None, 'my messagebox', '無開盤價資料')
            self.ui.open_label.setText("無資料")
        self.ui.limit_up_price_label.setText(str(crawler.stock_data['limit_up_price']))
        self.ui.limit_down_price_label.setText(str(crawler.stock_data['limit_down_price']))
        self.ui.close_label.setText(str(round(crawler.stock_data['close'][-1])))
        self.ui.up_down_percentage_label.setStyleSheet("color:red" if crawler.stock_data['percentage'] >= 0 else "color:green")
        self.ui.up_down_percentage_label.setText(f'{round(crawler.stock_data["percentage"], 2)}%')
        self.ui.amplitude_label.setText(str(round(crawler.stock_data['amplitude'], 2)))
            
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
        self.mainFigure, mainAxlst = mpf.plot(crawler.olddata, type="candle", style=style, volume = True, ylabel="price($)", returnfig=True, addplot=ap)
        mainAxlst[0].set_title(crawler.stock_symbol)
        mainAxlst[0].grid(visible=True, which="both", axis="x", ms=1, markevery=1)
        mainAxlst[0].plot(crawler.lastmax_x, crawler.lastmax_y,'ro')
        mainAxlst[0].plot(crawler.lastmin_x, crawler.lastmin_y,'ro')
        mainAxlst[0].plot(crawler.maxpoint_x, crawler.maxpoint_y,'ro')
        mainAxlst[0].plot(crawler.minpoint_x, crawler.minpoint_y,'ro')
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

