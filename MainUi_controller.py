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
        self.ui.futuresComboBox.addItems(["MXF:小台指期", "FXF:金融期", "EXF:電子期", "TXF:台指期", "TSE31:金融保險類指數", "TSE27:電子類指數"])
        self.ui.showStockWindowPushButton.clicked.connect(self.on_stock_button_clicked)
        self.ui.showFuturesWindowPushButton.clicked.connect(self.on_futures_button_clicked)
        self.openedLst = []

    def on_stock_button_clicked(self):
        stock_code = self.ui.stockComboBox.currentText()[:self.ui.stockComboBox.currentText().find(':')]
        self.showStockWindow(stock_code)   

    def on_futures_button_clicked(self):
        futures_code = self.ui.futuresComboBox.currentText()[:self.ui.futuresComboBox.currentText().find(':')]
        futures_index = self.ui.futuresComboBox.currentIndex()
        try:
            self.showFuturesWindow(futures_code,futures_index)
        except KeyError:
            return QMessageBox.warning(None, 'my messagebox', '查無資料')
            

    def showStockWindow(self, stock_code):
        self.openedLst.append(QWidget())
        self.stockWindowUi = stockWindowUiController(self.openedLst[-1], stock_code)
        self.openedLst[-1].show()

    def showFuturesWindow(self, futures_code, futures_index):
        self.openedLst.append(QWidget())
        self.futuresWindowUi = futuresWindowUiController(self.openedLst[-1], futures_code, futures_index)
        self.openedLst[-1].show()

    
