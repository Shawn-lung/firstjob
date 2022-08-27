from PyQt6.QtWidgets import QWidget
from PyQt6.QtCore import Qt
from PyQt6 import QtGui
import json

class MyWidget(QWidget):
    def keyPressEvent(self, a0: QtGui.QKeyEvent) -> None:
        if a0.key() == Qt.Key.Key_Left.value:
            print("left pressed")
        if a0.key() == Qt.Key.Key_Right.value:
            print("right pressed")
    
    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
        super().closeEvent(a0)
        with open("favorite.json", "r", encoding="utf-8") as data:
            fav_dict = json.load(data)
            fav_dict["indicators"][0] = self.ui.indicatorComboBox1.currentText()
            fav_dict["indicators"][1] = self.ui.indicatorComboBox2.currentText()
            fav_dict["indicators"][2] = self.ui.indicatorComboBox3.currentText()
        with open("favorite.json", "w", encoding="utf-8") as data:
            json.dump(fav_dict, data, ensure_ascii=False)
        self.timer.stop()