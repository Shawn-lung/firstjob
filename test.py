#!/usr/bin/python
# -*- coding: utf-8 -*-
# gui (imgui@qq.com)
# license: bsd
from pyqt4.qtcore import *
from pyqt4.qtgui import *
import sys
class w1(qwidget):
    def __init__(self, parent=none):
        super(w1, self).__init__(parent)
        self.btn = qpushbutton('click1')
        vb = qvboxlayout()
        vb.addwidget(self.btn)
        self.setlayout(vb)
        self.btn.clicked.connect(self.fireupwindows2)


    def fireupwindows2(self):
        w2 = w2()
        if w2.exec_():
            self.w3 = w3()    # 需要通過self例項化為全域性變數，不加self的話，一執行就被**，也就無法顯示。
            self.w3.show()


class w2(qdialog):
    def __init__(self, parent=none):
        super(w2, self).__init__(parent)
        self.btn = qpushbutton('click2')
        vb = qvboxlayout()
        vb.addwidget(self.btn)
        self.setlayout(vb)
        self.btn.clicked.connect(self.fireupwindows3)

    def fireupwindows3(self):
        self.accept()


class w3(qwidget):
    def __init__(self, parent=none):
        super(w3, self).__init__(parent)
        self.resize(300, 300)
        self.btn = qlabel('the last window')
        vb = qvboxlayout()
        vb.addwidget(self.btn)
        self.setlayout(vb)


if __name__ == "__main__":
    w = w1()
    w.show()
