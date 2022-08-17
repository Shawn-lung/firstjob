from socketserver import DatagramRequestHandler
import time
from PyQt6.QtWidgets import QWidget, QMessageBox
from MainUi import Ui_Form
from CrawlerClass import StockCrawler, FuturesCrawler
from stockWindowUi_controller import stockWindowUiController
from futuresWindowUi_controller import futuresWindowUiController
import json
class MainUiController(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.stockComboBox.addItems(StockCrawler.getStocks())
        self.ui.futuresComboBox.addItems(["MXF: 小台指期", "FXF: 金融期", "EXF: 電子期", "TXF: 台指期", "TSE31: 金融保險類指數", "TSE27: 電子類指數"])
        self.ui.showStockWindowPushButton.clicked.connect(self.on_stock_button_clicked)
        self.ui.favoriteButton1.clicked.connect(self.on_favorite_button1_clicked)
        self.ui.favoriteButton2.clicked.connect(self.on_favorite_button2_clicked)
        self.ui.removeButton.clicked.connect(self.on_remove_button_clicked)
        self.ui.openFavoriteButton.clicked.connect(self.on_open_favorite_button_clicked)
        self.ui.showFuturesWindowPushButton.clicked.connect(self.on_futures_button_clicked)
        self.writeToComboBox()
        self.openedLst = []

    def on_favorite_button1_clicked(self):
        with open("favorite.json", "r", encoding="utf-8") as data:
            fav_dict = json.load(data)
            if self.ui.stockComboBox.currentText() not in fav_dict["stock"]:
                fav_dict["stock"].append(self.ui.stockComboBox.currentText())
                with open("favorite.json", "w", encoding="utf-8") as data:
                    json.dump(fav_dict, data, ensure_ascii=False)
                self.writeToComboBox()
                
    def on_favorite_button2_clicked(self):
        with open("favorite.json", "r", encoding="utf-8") as data:
            fav_dict = json.load(data)
            if self.ui.futuresComboBox.currentText() not in fav_dict["futures"]:
                fav_dict["futures"].append(self.ui.futuresComboBox.currentText())
                with open("favorite.json", "w", encoding="utf-8") as data:
                    json.dump(fav_dict, data, ensure_ascii=False)
                self.writeToComboBox()

    def on_remove_button_clicked(self):
        with open("favorite.json", encoding="utf-8") as data:
            fav_dict = json.load(data)
            try:
                fav_dict["stock"].remove(self.ui.favoriteComboBox.currentText())
            except:
                fav_dict["futures"].remove(self.ui.favoriteComboBox.currentText())
            with open("favorite.json", "w", encoding="utf-8") as data:
                json.dump(fav_dict, data, ensure_ascii=False)
        self.writeToComboBox()
    
    def on_open_favorite_button_clicked(self):
        for i in [self.ui.favoriteComboBox.itemText(x) for x in range(self.ui.favoriteComboBox.count())]:
            print(i)
            if i[0].isdigit():
                self.showStockWindow(i[:i.find(':')])
            elif i.startswith("TSE"):
                print(i[:i.find(':')])
                self.showFuturesWindow(i[:i.find(':')], 4)
            else:
                self.showFuturesWindow(i[:i.find(':')], 0)
            #time.sleep(1)

    def writeToComboBox(self):
        self.ui.favoriteComboBox.clear()
        with open("favorite.json", encoding="utf-8") as data:
            fav_dict = json.load(data)
            self.ui.favoriteComboBox.addItems(fav_dict["stock"] + fav_dict["futures"])

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
        time.sleep(0.5)

    def showFuturesWindow(self, futures_code, futures_index):
        self.openedLst.append(QWidget())
        self.futuresWindowUi = futuresWindowUiController(self.openedLst[-1], futures_code, futures_index)
        self.openedLst[-1].show()
        time.sleep(0.5)

    
