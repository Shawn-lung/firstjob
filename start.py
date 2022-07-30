from PyQt6.QtWidgets import QApplication
from MainUi_controller import MainUiController
if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    app.processEvents()
    mainWindow = MainUiController()
    mainWindow.show()
    sys.exit(app.exec())