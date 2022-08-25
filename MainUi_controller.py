from PyQt6.QtWidgets import QWidget, QMessageBox
from MainUi import Ui_Form
from CrawlerClass import StockCrawler
from stockWindowUi_controller import stockWindowUiController
from futuresWindowUi_controller import futuresWindowUiController
from MyWidget import MyWidget
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
        self.stockn = 0
        self.futuresn = 0
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
                try:
                    fav_dict["futures"].remove(self.ui.favoriteComboBox.currentText())
                except:
                    pass
            with open("favorite.json", "w", encoding="utf-8") as data:
                json.dump(fav_dict, data, ensure_ascii=False)
        self.writeToComboBox()
    
    def on_open_favorite_button_clicked(self):
        for i in [self.ui.favoriteComboBox.itemText(x) for x in range(self.ui.favoriteComboBox.count())]:
            if i[0].isdigit():
                self.showStockWindow(i[:i.find(':')])
            elif i.startswith("TSE"):
                self.showFuturesWindow(i[:i.find(':')], 4)
            else:
                self.showFuturesWindow(i[:i.find(':')], 0)

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
        self.openedLst.append(MyWidget())
        match self.stockn:
            case 0:
                self.stockWindowUi = stockWindowUiController(self.openedLst[-1], stock_code)
            case 1:
                self.stockWindowUi1 = stockWindowUiController(self.openedLst[-1], stock_code)
            case 2:
                self.stockWindowUi2 = stockWindowUiController(self.openedLst[-1], stock_code)
            case 3:
                self.stockWindowUi3 = stockWindowUiController(self.openedLst[-1], stock_code) 
            case 4:               
                self.stockWindowUi4 = stockWindowUiController(self.openedLst[-1], stock_code)
            case 5:
                self.stockWindowUi5 = stockWindowUiController(self.openedLst[-1], stock_code)
            case 6:
                self.stockWindowUi6 = stockWindowUiController(self.openedLst[-1], stock_code)
            case 7:
                self.stockWindowUi7 = stockWindowUiController(self.openedLst[-1], stock_code)
            case 8:               
                self.stockWindowUi8 = stockWindowUiController(self.openedLst[-1], stock_code)
            case 9:
                self.stockWindowUi9 = stockWindowUiController(self.openedLst[-1], stock_code)
            case 10:
                self.stockWindowUi10 = stockWindowUiController(self.openedLst[-1], stock_code)
            case 11:
                self.stockWindowUi11 = stockWindowUiController(self.openedLst[-1], stock_code) 
            case 12:               
                self.stockWindowUi12 = stockWindowUiController(self.openedLst[-1], stock_code)
            case 13:
                self.stockWindowUi13 = stockWindowUiController(self.openedLst[-1], stock_code)
            case 14:
                self.stockWindowUi14 = stockWindowUiController(self.openedLst[-1], stock_code)
            case 15:
                self.stockWindowUi15 = stockWindowUiController(self.openedLst[-1], stock_code)                   

        self.stockn = self.stockn+1 if self.stockn <= 15 else 0
        self.openedLst[-1].show()


    def showFuturesWindow(self, futures_code, futures_index):
        self.openedLst.append(MyWidget())
        match self.futuresn:
            case 0:
                self.futuresWindowUi = futuresWindowUiController(self.openedLst[-1], futures_code, futures_index)
            case 1:
                self.futuresWindowUi1 = futuresWindowUiController(self.openedLst[-1], futures_code, futures_index) 
            case 2:
                self.futuresWindowUi2 = futuresWindowUiController(self.openedLst[-1], futures_code, futures_index)
            case 3:
                self.futuresWindowUi3 = futuresWindowUiController(self.openedLst[-1], futures_code, futures_index)
            case 4:
                self.futuresWindowUi4 = futuresWindowUiController(self.openedLst[-1], futures_code, futures_index)
            case 5:
                self.futuresWindowUi5 = futuresWindowUiController(self.openedLst[-1], futures_code, futures_index) 
            case 6:
                self.futuresWindowUi6 = futuresWindowUiController(self.openedLst[-1], futures_code, futures_index)
            case 7:
                self.futuresWindowUi7 = futuresWindowUiController(self.openedLst[-1], futures_code, futures_index)           

        self.futuresn +=1
        self.openedLst[-1].show()
                                                                                                                                                                                                                                                                                        
