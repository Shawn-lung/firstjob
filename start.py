from PyQt6.QtWidgets import QApplication
from Controller import Controller
if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window = Controller()
    window.show()
    sys.exit(app.exec())