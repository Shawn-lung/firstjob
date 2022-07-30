from PyQt6.QtWidgets import QWidget
from MainUi import Ui_Form
from stockWindowUi_controller import stockWindowUiController

class MainUiController(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.comboBox.addItems(['0050', '2330', '8069', '8105'])
        self.ui.pushButton.clicked.connect(self.on_Button_clicked)
        self.openedLst = []

    def on_Button_clicked(self):
        stock_code = self.ui.comboBox.currentText()
        self.showStockWindow(stock_code)   


    def showStockWindow(self, stock_code):
        self.openedLst.append(QWidget())
        self.stockWindowUi = stockWindowUiController(self.openedLst[-1], stock_code)
        self.openedLst[-1].show()





    