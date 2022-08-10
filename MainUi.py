# Form implementation generated from reading ui file 'MainUi.ui'
#
# Created by: PyQt6 UI code generator 6.3.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(256, 180)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(100)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(13)
        Form.setFont(font)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(-1, 50, -1, 50)
        self.verticalLayout.setObjectName("verticalLayout")
        self.stockComboBox = QtWidgets.QComboBox(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stockComboBox.sizePolicy().hasHeightForWidth())
        self.stockComboBox.setSizePolicy(sizePolicy)
        self.stockComboBox.setEditable(True)
        self.stockComboBox.setObjectName("stockComboBox")
        self.verticalLayout.addWidget(self.stockComboBox)
        self.showStockWindowPushButton = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.showStockWindowPushButton.sizePolicy().hasHeightForWidth())
        self.showStockWindowPushButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.showStockWindowPushButton.setFont(font)
        self.showStockWindowPushButton.setObjectName("showStockWindowPushButton")
        self.verticalLayout.addWidget(self.showStockWindowPushButton)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setContentsMargins(-1, 50, -1, 50)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.futuresComboBox = QtWidgets.QComboBox(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.futuresComboBox.sizePolicy().hasHeightForWidth())
        self.futuresComboBox.setSizePolicy(sizePolicy)
        self.futuresComboBox.setEditable(True)
        self.futuresComboBox.setObjectName("futuresComboBox")
        self.verticalLayout_3.addWidget(self.futuresComboBox)
        self.showFuturesWindowPushButton = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.showFuturesWindowPushButton.sizePolicy().hasHeightForWidth())
        self.showFuturesWindowPushButton.setSizePolicy(sizePolicy)
        self.showFuturesWindowPushButton.setObjectName("showFuturesWindowPushButton")
        self.verticalLayout_3.addWidget(self.showFuturesWindowPushButton)
        self.horizontalLayout.addLayout(self.verticalLayout_3)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "看股"))
        self.stockComboBox.setCurrentText(_translate("Form", "選擇股票"))
        self.showStockWindowPushButton.setText(_translate("Form", "新增股票視窗"))
        self.futuresComboBox.setCurrentText(_translate("Form", "選擇期貨"))
        self.showFuturesWindowPushButton.setText(_translate("Form", "新增期貨視窗"))
