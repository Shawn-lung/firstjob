from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton

class MyWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("My App")
        button = QPushButton()
        button.setText("press me")
        button.clicked.connect(self.btn_clicked)
        self.setCentralWidget(button)

    def btn_clicked(self):
        print("clicked")

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())