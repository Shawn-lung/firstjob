# Form implementation generated from reading ui file 'c:\Users\yuanc\OneDrive\文件\GitHub\firstjob\MainUi.ui'
#
# Created by: PyQt6 UI code generator 6.3.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(280, 180)
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
        self.favoriteButton1 = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.favoriteButton1.sizePolicy().hasHeightForWidth())
        self.favoriteButton1.setSizePolicy(sizePolicy)
        self.favoriteButton1.setObjectName("favoriteButton1")
        self.verticalLayout.addWidget(self.favoriteButton1)
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
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(-1, 0, -1, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setContentsMargins(-1, 20, -1, 50)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.verticalLayout_4.addWidget(self.label)
        self.favoriteComboBox = QtWidgets.QComboBox(Form)
        self.favoriteComboBox.setObjectName("favoriteComboBox")
        self.verticalLayout_4.addWidget(self.favoriteComboBox)
        self.removeButton = QtWidgets.QPushButton(Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.removeButton.setFont(font)
        self.removeButton.setObjectName("removeButton")
        self.verticalLayout_4.addWidget(self.removeButton)
        self.verticalLayout_2.addLayout(self.verticalLayout_4)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.openFavoriteButton = QtWidgets.QPushButton(Form)
        self.openFavoriteButton.setObjectName("openFavoriteButton")
        self.verticalLayout_5.addWidget(self.openFavoriteButton)
        self.verticalLayout_2.addLayout(self.verticalLayout_5)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
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
        self.favoriteButton2 = QtWidgets.QPushButton(Form)
        self.favoriteButton2.setObjectName("favoriteButton2")
        self.verticalLayout_3.addWidget(self.favoriteButton2)
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
        self.favoriteButton1.setText(_translate("Form", "新增至常用"))
        self.showStockWindowPushButton.setText(_translate("Form", "新增股票視窗"))
        self.label.setText(_translate("Form", "常用"))
        self.removeButton.setText(_translate("Form", "從常用中移除"))
        self.openFavoriteButton.setText(_translate("Form", "一鍵打開常用"))
        self.futuresComboBox.setCurrentText(_translate("Form", "選擇期貨"))
        self.favoriteButton2.setText(_translate("Form", "新增至常用"))
        self.showFuturesWindowPushButton.setText(_translate("Form", "新增期貨視窗"))
