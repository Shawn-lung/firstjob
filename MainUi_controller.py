from PyQt6.QtWidgets import QWidget, QMessageBox
from MainUi import Ui_Form
from CrawlerClass import StockCrawler, FuturesCrawler
from stockWindowUi_controller import stockWindowUiController
from futuresWindowUi_controller import futuresWindowUiController

class MainUiController(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.stockComboBox.addItems(StockCrawler.getStocks())
        self.ui.futuresComboBox.addItem("MXF")
        self.ui.futuresComboBox.addItems(FuturesCrawler.getFutures())
        self.ui.showStockWindowPushButton.clicked.connect(self.on_stock_button_clicked)
        self.ui.showFuturesWindowPushButton.clicked.connect(self.on_futures_button_clicked)
        self.openedLst = []

    def on_stock_button_clicked(self):
        stock_code = self.ui.stockComboBox.currentText()[:self.ui.stockComboBox.currentText().find(':')]
        self.showStockWindow(stock_code)   

    def on_futures_button_clicked(self):
        futures_code = self.ui.futuresComboBox.currentText()[:self.ui.futuresComboBox.currentText().find(':')]
        try:
            self.showFuturesWindow(futures_code)
        except KeyError:
            return QMessageBox.warning(None, 'my messagebox', '查無資料')
            

    def showStockWindow(self, stock_code):
        self.openedLst.append(QWidget())
        self.stockWindowUi = stockWindowUiController(self.openedLst[-1], stock_code)
        self.openedLst[-1].show()

    def showFuturesWindow(self, futures_code):
        self.openedLst.append(QWidget())
        self.futuresWindowUi = futuresWindowUiController(self.openedLst[-1], futures_code)
        self.openedLst[-1].show()

    
