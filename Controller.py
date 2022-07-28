from PyQt6.QtWidgets import QWidget
from UI import Ui_Form
import pyqtgraph as pg
import lib

class Controller(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setUpControl()
        self.ui.plotitem = pg.PlotWidget(self.ui.graphicsView)
        self.ui.plotitem.plot([11, 15, 26], [5, 8, 14])

    def setUpControl(self):
        self.ui.pushButton.clicked.connect(self.on_pushButton_clicked)

    def on_pushButton_clicked(self):
        code = self.ui.lineEdit.text()
        gi = lib.get_history_data([code])
        self.ui.plotitem = pg.PlotWidget(self.ui.graphicsView)
        self.ui.plotitem.plot([11, 15, 26], [5, 8, 14])

