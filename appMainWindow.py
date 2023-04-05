import ctypes
from random import randint

import pyqtgraph as pg

# from include.AbstractTableModel import TableModel
from PyQt6.QtCore import QCoreApplication, QSize, Qt, QTimer
from PyQt6.QtGui import QAction, QFont, QFontMetrics, QIcon, QKeySequence, QPalette
from PyQt6.QtSql import QSqlDatabase, QSqlQuery, QSqlQueryModel
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QStatusBar,
    QTabWidget,
    QToolBar,
    QWidget,
)

from UIs.ui_ConfigurationTab import Ui_ConfigurationTab
from UIs.ui_DatabaseTab import Ui_DatabaseTab
from UIs.ui_MeasurementTab import Ui_MeasurementTab
from UIs.ui_TerminalTab import Ui_TerminalTab

# import sys
# setting path to parent folder
# sys.path.append("C:\\Users\\xstejs30\\Documents\\PythonProjects\\PyWinApp\\main\\PyQtModelViews_Databases")
# print("System paths:")
# print("\n".join(sys.path))


class ConfigurationTab(QWidget, Ui_ConfigurationTab):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)


class MeasurementTab(QWidget, Ui_MeasurementTab):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        # Set background colour - default window color background
        graphBGcolor = self.palette().color(QPalette.ColorRole.Window)
        self.graphWidget.setBackground(graphBGcolor)
        self.graphWidget.setTitle("Měření", color="k", size="18pt")
        # self.graphWidget.addLegend(offset=20)
        self.graphWidget.showGrid(x=True, y=True)

        # Timer initialization - for plot data updating
        self.timer = QTimer()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.updatePlotData)
        self.timer.start()

        self.pen = pg.mkPen(color="b", width=2, style=Qt.PenStyle.SolidLine)
        self.time = list(range(100))  # 100 time points
        self.voltage = [randint(0, 100) for _ in range(100)]  # 100 data points
        self.lineDataRef = self.graphWidget.plot(self.time, self.voltage, pen=self.pen)
        self.voltagePlot = self.graphWidget.getPlotItem()
        self.voltagePlot.setLabel("left", "napětí", "V")
        self.voltagePlot.getAxis("left").label.setFont(QFont("Times", 12))
        self.voltagePlot.setLabel("bottom", "čas", "s")
        self.voltagePlot.getAxis("bottom").label.setFont(QFont("Times", 12))
        self.voltagePlot.setTitle("ADC CH0")

    def updatePlotData(self):
        self.time = self.time[1:]  # Remove the 1st element of time vector
        self.time.append(self.time[-1] + 1)

        self.voltage = self.voltage[1:]  # Remove the 1st element of voltage vector
        self.voltage.append(randint(0, 100))  # Add a new random value

        self.lineDataRef.setData(self.time, self.voltage)  # Update the line data ref


class TerminalTab(QWidget, Ui_TerminalTab):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)


# pyuic6 UIs/DatabaseTab.ui -o UIs/ui_DatabaseTab.py
class DatabaseTab(QWidget, Ui_DatabaseTab):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        # self._data = data
        # self._headers = headers
        self._lineEditminWidth = self.lineEditUser.minimumWidth()

        self.btnLogin.clicked.connect(self.loginToDB)

        self.lineEditReadColumns.textChanged.connect(self.lineEditContentChanged)
        self.lineEditReadCondition.textChanged.connect(self.lineEditContentChanged)
        self.lineEditInsertColumns.textChanged.connect(self.lineEditContentChanged)
        self.lineEditInsertValues.textChanged.connect(self.lineEditContentChanged)
        self.lineEditUpdateColumns.textChanged.connect(self.lineEditContentChanged)
        self.lineEditUpdateValues.textChanged.connect(self.lineEditContentChanged)
        self.lineEditUpdateCondition.textChanged.connect(self.lineEditContentChanged)
        self.lineEditDeleteCondition.textChanged.connect(self.lineEditContentChanged)

        self.btnInsert.clicked.connect(self.insertIntoTable)
        self.btnRead.clicked.connect(self.selectFromTable)
        self.btnUpdate.clicked.connect(self.updateTableRecord)
        self.btnDelete.clicked.connect(self.deleteTableRecord)

        # self.tableDataModel = TableModel(self._data, self._headers)
        # self.tableViewSelected.setModel(self.tableDataModel)
        self.tableModelSQL = QSqlQueryModel()

    def loginToDB(self):
        user = self.lineEditUser.text()
        password = self.lineEditPassword.text()
        databaseName = self.comboBoxDBName.currentText()

        self.devDB = QSqlDatabase.addDatabase("QPSQL")
        self.devDB.setHostName("localhost")
        self.devDB.setPort(5432)
        self.devDB.setDatabaseName(databaseName)
        self.devDB.setUserName(user)  # postgres is the default root username
        self.devDB.setPassword(password)  # add your password here

        if not self.devDB.open():
            self.textDBStatus.setText(
                "Database Error: {}".format(self.devDB.lastError().databaseText())
            )
        else:
            self.textDBStatus.setText("Connection to the DB was successful!")

    def insertIntoTable(self):
        table = self.comboBoxTableViewed.currentText()
        columns = self.lineEditInsertColumns.text()
        values = self.lineEditInsertValues.text()
        queryInsertCmd = "INSERT INTO "

        if not columns or not values:
            self.textDBStatus.setText(
                'Při vytváření záznamu nesmí být pole "Sloupce" a "Hodnoty" prázdné!'
            )
            return
        else:
            queryInsertCmd += '"{}" ({}) VALUES ({})'.format(table, columns, values)

        queryInsert = QSqlQuery(self.devDB)
        queryInsert.prepare(queryInsertCmd)
        if not queryInsert.exec():
            self.textDBStatus.setText(
                "{}".format(queryInsert.lastError().databaseText())
            )
        else:
            self.textDBStatus.setText(
                "Vložení nového záznamu do tabulky {} proběhlo úspěšně!".format(table)
            )

    def selectFromTable(self):
        columns = self.lineEditReadColumns.text()
        table = self.comboBoxTableViewed.currentText()
        condition = self.lineEditReadCondition.text()
        limit = self.lineEditReadLimit.text()

        queryReadCmd = "SELECT "
        if not columns:
            queryReadCmd += '* FROM "{}"'.format(table)
        else:
            queryReadCmd += '{} FROM "{}"'.format(columns, table)
        if condition:
            queryReadCmd += " WHERE {}".format(condition)
        if limit:
            queryReadCmd += " LIMIT {}".format(limit)

        queryRead = QSqlQuery(self.devDB)
        queryRead.prepare(queryReadCmd)
        if not queryRead.exec():
            self.textDBStatus.setText("{}".format(queryRead.lastError().databaseText()))
        else:
            self.textDBStatus.setText(
                "Výběr záznamů z tabulky {} proběhlo úspěšně!\n".format(table)
                + "Bylo vybráno {} záznamů.".format(queryRead.size())
            )

        self.tableModelSQL.setQuery(queryRead)
        self.tableViewSelected.setModel(self.tableModelSQL)

    def updateTableRecord(self):
        queryUpdate = QSqlQuery(self.devDB)
        table = self.comboBoxTableViewed.currentText()
        columns = self.lineEditUpdateColumns.text()
        values = self.lineEditUpdateValues.text()
        condition = self.lineEditUpdateCondition.text()

        if not queryUpdate.exec(
            "UPDATE {} SET ({}) = ({}) WHERE {}".format(
                table, columns, values, condition
            )
        ):
            self.textDBStatus.setText(
                "{}".format(queryUpdate.lastError().databaseText())
            )
        else:
            self.textDBStatus.setText(
                "Aktualizace záznamů z tabulky {} proběhlo úspěšně!\n".format(table)
                + "Bylo aktualizováno {} záznamů.".format(queryUpdate.numRowsAffected())
            )

    def deleteTableRecord(self):
        queryDelete = QSqlQuery(self.devDB)
        table = self.comboBoxTableViewed.currentText()
        condition = self.lineEditDeleteCondition.text()

        if not queryDelete.exec("DELETE FROM {} WHERE {}".format(table, condition)):
            self.textDBStatus.setText(
                "{}".format(queryDelete.lastError().databaseText())
            )
        else:
            self.textDBStatus.setText(
                "Odstranění záznamů z tabulky {} proběhlo úspěšně!\n".format(table)
                + "Bylo odebráno {} záznamů.".format(queryDelete.numRowsAffected())
            )

    def lineEditContentChanged(self):
        sender = self.sender()
        font = QFont("", 0)
        fm = QFontMetrics(font)

        text = sender.text()
        newWidth = int(fm.boundingRect(text).width() * 0.8)
        if newWidth > self._lineEditminWidth:
            sender.setFixedWidth(newWidth)
        else:
            sender.setMinimumWidth(self._lineEditminWidth)


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("Application for PCB testing")
        self.setWindowIcon(QIcon("images/meter02-icon.png"))
        self.setMinimumSize(QSize(1200, 900))

        self.toolbar = QToolBar("Main Toolbar")
        self.toolbar.setIconSize(QSize(16, 16))
        self.addToolBar(self.toolbar)

        btnBugAction = QAction(QIcon("images/bug.png"), "&Bug simulation", self)
        btnBugAction.setStatusTip("Simulate a Bug.")
        btnBugAction.setCheckable(True)
        self.toolbar.addAction(btnBugAction)
        btnBugAction.setShortcut(QKeySequence("Ctrl+b"))
        self.toolbar.addSeparator()

        menuBar = self.menuBar()
        fileMenu = menuBar.addMenu("&File")
        fileSubmenu = fileMenu.addMenu("&Submenu")
        fileSubmenu.addAction(btnBugAction)
        btnExitApplication = QAction("E&xit Application", self)
        btnExitApplication.setStatusTip("Push to exit the Application.")
        btnExitApplication.triggered.connect(QCoreApplication.instance().quit)
        fileMenu.addAction(btnExitApplication)

        editMenu = menuBar.addMenu("&Edit")
        editMenu.addAction(btnBugAction)

        viewMenu = menuBar.addMenu("&View")
        self.btnShowMainToolbar = QAction("Show Main Toolbar", self)
        self.btnShowMainToolbar.setStatusTip("Push to show the Main Toolbar.")
        self.btnShowMainToolbar.triggered.connect(self.setMainToolbarVisibility)
        self.toolbar.visibilityChanged.connect(self.checkMainToolbarVisibility)
        self.btnShowMainToolbar.setCheckable(True)
        self.btnShowMainToolbar.setChecked(True)
        viewMenu.addAction(self.btnShowMainToolbar)

        tabs = QTabWidget()
        tabs.setTabPosition(QTabWidget.TabPosition.North)

        self.configTab = ConfigurationTab(self)
        cfgTabIdx = tabs.addTab(self.configTab, "Volba konfigurace DPS")

        self.measurementTab = MeasurementTab(self)
        measureTabIdx = tabs.addTab(self.measurementTab, "Měření")

        self.terminalTab = TerminalTab(self)
        terminalTabIdx = tabs.addTab(self.terminalTab, "Terminál")

        self.databaseTab = DatabaseTab(self)
        databaseTabIdx = tabs.addTab(self.databaseTab, "Databáze")

        tabs.setCurrentIndex(databaseTabIdx)  # DEBUG
        self.setCentralWidget(tabs)

        self.statusbar = QStatusBar(self)
        self.setStatusBar(self.statusbar)

    def setMainToolbarVisibility(self, visibility):
        if visibility:
            self.addToolBar(self.toolbar)
            self.toolbar.show()
        else:
            self.removeToolBar(self.toolbar)

    def checkMainToolbarVisibility(self, visibility):
        if not visibility:
            self.btnShowMainToolbar.setChecked(False)


if __name__ == "__main__":
    # https://stackoverflow.com/questions/1551605/how-to-set-applications-taskbar-icon-in-windows-7/1552105#1552105
    myappid = "mycompany.myproduct.subproduct.version"  # arbitrary string
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

    app = QApplication([])

    window = MainWindow()
    window.show()
    app.exec()

    # print(app.applicationDirPath())
    # app.addLibraryPath(
    #     "C:/Users/xstejs30/Documents/PythonProjects/PyWinApp/.venv/lib/site-packages/PyQt6/Qt6/bin"
    # )
    # print(app.libraryPaths())
