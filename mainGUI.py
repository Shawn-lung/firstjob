import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel
from PyQt6.QtGui import QIcon, QFont


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.set_initUI()

    def set_initUI(self):
        self.setGeometry(50,50,320,200)
        self.setWindowTitle("PyQt6 Example")
        self.mylabel = QLabel('hello world', self)
        self.mylabel.move(40, 50)
        self.mylabel.setFont(QFont('Arial', 18))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = MyWidget()
    widget.show()
    sys.exit(app.exec())