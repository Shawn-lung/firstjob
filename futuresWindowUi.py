# Form implementation generated from reading ui file 'futuresWindowUi.ui'
#
# Created by: PyQt6 UI code generator 6.3.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setEnabled(True)
        Form.resize(1002, 359)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setFieldGrowthPolicy(QtWidgets.QFormLayout.FieldGrowthPolicy.AllNonFixedFieldsGrow)
        self.formLayout.setFormAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.formLayout.setContentsMargins(5, 5, 5, 5)
        self.formLayout.setHorizontalSpacing(4)
        self.formLayout.setObjectName("formLayout")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setMinimumSize(QtCore.QSize(0, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_2)
        self.open_label = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.open_label.setFont(font)
        self.open_label.setText("")
        self.open_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.open_label.setObjectName("open_label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.open_label)
        self.label_3 = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setMinimumSize(QtCore.QSize(0, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_3)
        self.high_price_label = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.high_price_label.setFont(font)
        self.high_price_label.setText("")
        self.high_price_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.high_price_label.setObjectName("high_price_label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.high_price_label)
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setMinimumSize(QtCore.QSize(0, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_7)
        self.low_price_label = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.low_price_label.setFont(font)
        self.low_price_label.setText("")
        self.low_price_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.low_price_label.setObjectName("low_price_label")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.low_price_label)
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setMinimumSize(QtCore.QSize(0, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_8)
        self.close_label = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.close_label.setFont(font)
        self.close_label.setText("")
        self.close_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.close_label.setObjectName("close_label")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.ItemRole.FieldRole, self.close_label)
        self.label_10 = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        self.label_10.setMinimumSize(QtCore.QSize(0, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_10)
        self.amplitude_label = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.amplitude_label.setFont(font)
        self.amplitude_label.setText("")
        self.amplitude_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.amplitude_label.setObjectName("amplitude_label")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.ItemRole.FieldRole, self.amplitude_label)
        self.confirmButton = QtWidgets.QPushButton(Form)
        self.confirmButton.setObjectName("confirmButton")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.ItemRole.LabelRole, self.confirmButton)
        self.notifyingLabel = QtWidgets.QLabel(Form)
        self.notifyingLabel.setText("")
        self.notifyingLabel.setObjectName("notifyingLabel")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.ItemRole.FieldRole, self.notifyingLabel)
        self.verticalLayout.addLayout(self.formLayout)
        self.intervalComboBox = QtWidgets.QComboBox(Form)
        self.intervalComboBox.setEditable(False)
        self.intervalComboBox.setCurrentText("")
        self.intervalComboBox.setObjectName("intervalComboBox")
        self.verticalLayout.addWidget(self.intervalComboBox)
        self.periodComboBox = QtWidgets.QComboBox(Form)
        self.periodComboBox.setEditable(False)
        self.periodComboBox.setCurrentText("")
        self.periodComboBox.setObjectName("periodComboBox")
        self.verticalLayout.addWidget(self.periodComboBox)
        self.indicatorComboBox1 = QtWidgets.QComboBox(Form)
        self.indicatorComboBox1.setEditable(False)
        self.indicatorComboBox1.setCurrentText("")
        self.indicatorComboBox1.setObjectName("indicatorComboBox1")
        self.verticalLayout.addWidget(self.indicatorComboBox1)
        self.indicatorComboBox2 = QtWidgets.QComboBox(Form)
        self.indicatorComboBox2.setObjectName("indicatorComboBox2")
        self.verticalLayout.addWidget(self.indicatorComboBox2)
        self.indicatorComboBox3 = QtWidgets.QComboBox(Form)
        self.indicatorComboBox3.setObjectName("indicatorComboBox3")
        self.verticalLayout.addWidget(self.indicatorComboBox3)
        self.resetButton = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.resetButton.sizePolicy().hasHeightForWidth())
        self.resetButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.resetButton.setFont(font)
        self.resetButton.setCheckable(False)
        self.resetButton.setObjectName("resetButton")
        self.verticalLayout.addWidget(self.resetButton)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.plotLayout = QtWidgets.QVBoxLayout()
        self.plotLayout.setObjectName("plotLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_2.addWidget(self.label_6)
        self.tLabel = QtWidgets.QLabel(Form)
        self.tLabel.setObjectName("tLabel")
        self.horizontalLayout_2.addWidget(self.tLabel)
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.oLabel = QtWidgets.QLabel(Form)
        self.oLabel.setObjectName("oLabel")
        self.horizontalLayout_2.addWidget(self.oLabel)
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_2.addWidget(self.label_5)
        self.hLabel = QtWidgets.QLabel(Form)
        self.hLabel.setObjectName("hLabel")
        self.horizontalLayout_2.addWidget(self.hLabel)
        self.label_9 = QtWidgets.QLabel(Form)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_2.addWidget(self.label_9)
        self.lLabel = QtWidgets.QLabel(Form)
        self.lLabel.setObjectName("lLabel")
        self.horizontalLayout_2.addWidget(self.lLabel)
        self.label_12 = QtWidgets.QLabel(Form)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_2.addWidget(self.label_12)
        self.cLabel = QtWidgets.QLabel(Form)
        self.cLabel.setObjectName("cLabel")
        self.horizontalLayout_2.addWidget(self.cLabel)
        self.plotLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout.addLayout(self.plotLayout)

        self.retranslateUi(Form)
        self.indicatorComboBox1.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_2.setText(_translate("Form", "開盤價"))
        self.label_3.setText(_translate("Form", "最高"))
        self.label_7.setText(_translate("Form", "最低"))
        self.label_8.setText(_translate("Form", "最後成交價"))
        self.label_10.setText(_translate("Form", "震幅"))
        self.confirmButton.setText(_translate("Form", "通知:開"))
        self.resetButton.setText(_translate("Form", "Reset"))
        self.label_6.setText(_translate("Form", "時間"))
        self.tLabel.setText(_translate("Form", "TextLabel"))
        self.label_4.setText(_translate("Form", "開"))
        self.oLabel.setText(_translate("Form", "TextLabel"))
        self.label_5.setText(_translate("Form", "高"))
        self.hLabel.setText(_translate("Form", "TextLabel"))
        self.label_9.setText(_translate("Form", "低"))
        self.lLabel.setText(_translate("Form", "TextLabel"))
        self.label_12.setText(_translate("Form", "收"))
        self.cLabel.setText(_translate("Form", "TextLabel"))
