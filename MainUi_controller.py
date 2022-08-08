from PyQt6.QtWidgets import QWidget
from MainUi import Ui_Form
from CrawlerClass import Crawler
from stockWindowUi_controller import stockWindowUiController
from futuresWindowUi_controller import futuresWindowUiController

class MainUiController(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.stockComboBox.addItems(Crawler.getStocks())
        self.ui.futuresComboBox.addItems(Crawler.getFutres())
        self.ui.showStockWindowPushButton.clicked.connect(self.on_stock_button_clicked)
        self.ui.showFuturesWindowPushButton.clicked.connect(self.on_futures_button_clicked)
        self.openedLst = []

    def on_stock_button_clicked(self):
        stock_code = self.ui.stockComboBox.currentText()[:self.ui.comboBox.currentText().find(':')]
        self.showStockWindow(stock_code)   

    def on_futures_button_clicked(self):
        futures_code = self.ui.futuresComboBox.currentText()
        self.showFuturesWindow(futures_code)

    def showStockWindow(self, stock_code):
        self.openedLst.append(QWidget())
        self.stockWindowUi = stockWindowUiController(self.openedLst[-1], stock_code)
        self.openedLst[-1].show()

    def showFuturesWindow(self, futures_code):
        self.openedLst.append(QWidget())
        self.futuresWindowUi = futuresWindowUiController(self.openedLst[-1], futures_code)


    
