from PyQt6.QtWidgets import QWidget
from futuresWindowUi import Ui_Form

class futuresWindowUiController(QWidget):
    def __init__(self, parent, futures_code):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(parent)
        self.futures_code = futures_code

