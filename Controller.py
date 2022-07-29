from PyQt6.QtWidgets import QWidget
from CrawlerClass import Crawler
from UI import Ui_Form
import pyqtgraph as pg
class Controller(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.on_Button_clicked)

    def on_Button_clicked(self):
        stock_code = self.ui.lineEdit.text()
        from CrawlerClass import Crawler
        crawler = Crawler(stock_code)
        plotItem = pg.PlotItem()
        #self.ui.graphicsView.getPlotItem().removeItem(plotItem)
        self.ui.graphicsView.addItem(plotItem.plot(y=crawler.stock_data['close'], pen='r'))
        self.labelUpdate(crawler)

    def labelUpdate(self, crawler: Crawler):
        self.ui.privious_close_label.setText(str(crawler.stock_data['previous_close']))
        self.ui.open_label.setText(str(crawler.stock_data['open'][-1]))
        self.ui.limit_up_price_label.setText(str(crawler.stock_data['limit_up_price']))
        self.ui.limit_down_price_label.setText(str(crawler.stock_data['limit_down_price']))
        self.ui.close_label.setText(str(crawler.stock_data['close'][-1]))
        self.ui.up_down_percentage_label.setStyleSheet("color:green" if crawler.stock_data['percentage'] >= 0 else "color:red")
        self.ui.up_down_percentage_label.setText(f'{round(crawler.stock_data["percentage"], 2)}%')
        
