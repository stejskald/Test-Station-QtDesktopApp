# Form implementation generated from reading ui file 'main/DP/UIs/TerminalTab.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_TerminalTab(object):
    def setupUi(self, TerminalTab):
        TerminalTab.setObjectName("TerminalTab")
        TerminalTab.resize(350, 290)
        TerminalTab.setMaximumSize(QtCore.QSize(450, 450))
        self.verticalLayout = QtWidgets.QVBoxLayout(TerminalTab)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_serialCom = QtWidgets.QLabel(parent=TerminalTab)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.label_serialCom.setFont(font)
        self.label_serialCom.setTextFormat(QtCore.Qt.TextFormat.PlainText)
        self.label_serialCom.setObjectName("label_serialCom")
        self.verticalLayout.addWidget(self.label_serialCom)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setContentsMargins(20, -1, -1, -1)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.comboBox = QtWidgets.QComboBox(parent=TerminalTab)
        self.comboBox.setMinimumSize(QtCore.QSize(70, 0))
        self.comboBox.setEditable(True)
        self.comboBox.setCurrentText("")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout_2.addWidget(self.comboBox, 0, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 0, 2, 1, 1)
        self.setSerialCom = QtWidgets.QLabel(parent=TerminalTab)
        self.setSerialCom.setObjectName("setSerialCom")
        self.gridLayout_2.addWidget(self.setSerialCom, 0, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_2)
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.verticalLayout.addItem(spacerItem1)
        self.label_serialComConfig = QtWidgets.QLabel(parent=TerminalTab)
        font = QtGui.QFont()
        font.setBold(True)
        self.label_serialComConfig.setFont(font)
        self.label_serialComConfig.setObjectName("label_serialComConfig")
        self.verticalLayout.addWidget(self.label_serialComConfig)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setContentsMargins(20, -1, -1, -1)
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit_baud = QtWidgets.QLineEdit(parent=TerminalTab)
        self.lineEdit_baud.setMinimumSize(QtCore.QSize(100, 0))
        self.lineEdit_baud.setMaximumSize(QtCore.QSize(150, 25))
        self.lineEdit_baud.setMaxLength(8)
        self.lineEdit_baud.setObjectName("lineEdit_baud")
        self.gridLayout.addWidget(self.lineEdit_baud, 0, 1, 1, 1)
        self.label_flowCtrl = QtWidgets.QLabel(parent=TerminalTab)
        self.label_flowCtrl.setObjectName("label_flowCtrl")
        self.gridLayout.addWidget(self.label_flowCtrl, 4, 0, 1, 1)
        self.label_parity = QtWidgets.QLabel(parent=TerminalTab)
        self.label_parity.setObjectName("label_parity")
        self.gridLayout.addWidget(self.label_parity, 3, 0, 1, 1)
        self.comboBox_3 = QtWidgets.QComboBox(parent=TerminalTab)
        self.comboBox_3.setMinimumSize(QtCore.QSize(100, 0))
        self.comboBox_3.setMaximumSize(QtCore.QSize(150, 16777215))
        self.comboBox_3.setCurrentText("")
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.gridLayout.addWidget(self.comboBox_3, 4, 1, 1, 1)
        self.lineEdit_stopBitCount = QtWidgets.QLineEdit(parent=TerminalTab)
        self.lineEdit_stopBitCount.setMinimumSize(QtCore.QSize(100, 0))
        self.lineEdit_stopBitCount.setMaximumSize(QtCore.QSize(150, 25))
        self.lineEdit_stopBitCount.setMaxLength(2)
        self.lineEdit_stopBitCount.setObjectName("lineEdit_stopBitCount")
        self.gridLayout.addWidget(self.lineEdit_stopBitCount, 2, 1, 1, 1)
        self.label_baud = QtWidgets.QLabel(parent=TerminalTab)
        self.label_baud.setObjectName("label_baud")
        self.gridLayout.addWidget(self.label_baud, 0, 0, 1, 1)
        self.lineEdit_dataBitCount = QtWidgets.QLineEdit(parent=TerminalTab)
        self.lineEdit_dataBitCount.setMinimumSize(QtCore.QSize(100, 0))
        self.lineEdit_dataBitCount.setMaximumSize(QtCore.QSize(150, 25))
        self.lineEdit_dataBitCount.setText("")
        self.lineEdit_dataBitCount.setMaxLength(2)
        self.lineEdit_dataBitCount.setObjectName("lineEdit_dataBitCount")
        self.gridLayout.addWidget(self.lineEdit_dataBitCount, 1, 1, 1, 1)
        self.label_dataBitCount = QtWidgets.QLabel(parent=TerminalTab)
        self.label_dataBitCount.setObjectName("label_dataBitCount")
        self.gridLayout.addWidget(self.label_dataBitCount, 1, 0, 1, 1)
        self.label_stopBitCount = QtWidgets.QLabel(parent=TerminalTab)
        self.label_stopBitCount.setObjectName("label_stopBitCount")
        self.gridLayout.addWidget(self.label_stopBitCount, 2, 0, 1, 1)
        self.comboBox_2 = QtWidgets.QComboBox(parent=TerminalTab)
        self.comboBox_2.setMinimumSize(QtCore.QSize(100, 0))
        self.comboBox_2.setMaximumSize(QtCore.QSize(150, 16777215))
        self.comboBox_2.setCurrentText("")
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.gridLayout.addWidget(self.comboBox_2, 3, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout.addItem(spacerItem2, 0, 2, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        self.setSerialCom.setBuddy(self.comboBox)
        self.label_flowCtrl.setBuddy(self.comboBox_3)
        self.label_parity.setBuddy(self.comboBox_2)
        self.label_baud.setBuddy(self.lineEdit_baud)
        self.label_dataBitCount.setBuddy(self.lineEdit_dataBitCount)
        self.label_stopBitCount.setBuddy(self.lineEdit_stopBitCount)

        self.retranslateUi(TerminalTab)
        QtCore.QMetaObject.connectSlotsByName(TerminalTab)
        TerminalTab.setTabOrder(self.lineEdit_baud, self.lineEdit_dataBitCount)
        TerminalTab.setTabOrder(self.lineEdit_dataBitCount, self.lineEdit_stopBitCount)
        TerminalTab.setTabOrder(self.lineEdit_stopBitCount, self.comboBox_2)
        TerminalTab.setTabOrder(self.comboBox_2, self.comboBox_3)

    def retranslateUi(self, TerminalTab):
        _translate = QtCore.QCoreApplication.translate
        TerminalTab.setWindowTitle(_translate("TerminalTab", "Form"))
        self.label_serialCom.setText(_translate("TerminalTab", "Možnosti ovládání sériové kounikace přes RS-485"))
        self.comboBox.setPlaceholderText(_translate("TerminalTab", "COM1"))
        self.comboBox.setItemText(0, _translate("TerminalTab", "COM1"))
        self.comboBox.setItemText(1, _translate("TerminalTab", "COM2"))
        self.comboBox.setItemText(2, _translate("TerminalTab", "COM3"))
        self.comboBox.setItemText(3, _translate("TerminalTab", "COM4"))
        self.comboBox.setItemText(4, _translate("TerminalTab", "COM5"))
        self.comboBox.setItemText(5, _translate("TerminalTab", "COM6"))
        self.comboBox.setItemText(6, _translate("TerminalTab", "COM7"))
        self.comboBox.setItemText(7, _translate("TerminalTab", "COM8"))
        self.comboBox.setItemText(8, _translate("TerminalTab", "COM9"))
        self.setSerialCom.setText(_translate("TerminalTab", "Vyberte sériovou linku k připojení"))
        self.label_serialComConfig.setText(_translate("TerminalTab", "Konfigurace sériové linky"))
        self.lineEdit_baud.setPlaceholderText(_translate("TerminalTab", "9600"))
        self.label_flowCtrl.setText(_translate("TerminalTab", "Řízení toku"))
        self.label_parity.setText(_translate("TerminalTab", "Parita"))
        self.comboBox_3.setPlaceholderText(_translate("TerminalTab", "Žádné"))
        self.comboBox_3.setItemText(0, _translate("TerminalTab", "Žádné"))
        self.comboBox_3.setItemText(1, _translate("TerminalTab", "XON/XOFF"))
        self.comboBox_3.setItemText(2, _translate("TerminalTab", "RTS/CTS"))
        self.comboBox_3.setItemText(3, _translate("TerminalTab", "DSR/DTR"))
        self.lineEdit_stopBitCount.setPlaceholderText(_translate("TerminalTab", "1"))
        self.label_baud.setText(_translate("TerminalTab", "Rychlost (baud)"))
        self.lineEdit_dataBitCount.setPlaceholderText(_translate("TerminalTab", "8"))
        self.label_dataBitCount.setText(_translate("TerminalTab", "Počet datových bitů"))
        self.label_stopBitCount.setText(_translate("TerminalTab", "Počet stop bitů"))
        self.comboBox_2.setPlaceholderText(_translate("TerminalTab", "Žádná"))
        self.comboBox_2.setItemText(0, _translate("TerminalTab", "Žádná"))
        self.comboBox_2.setItemText(1, _translate("TerminalTab", "Lichá"))
        self.comboBox_2.setItemText(2, _translate("TerminalTab", "Sudá"))
