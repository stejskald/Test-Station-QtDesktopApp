import os
import sys

from include.ConfigurationTab import ConfigurationTab
from include.DatabaseTab import DatabaseTab
from include.MeasurementTab import MeasurementTab
from include.TerminalTab import TerminalTab
from PyQt6.QtCore import QCoreApplication, QSize
from PyQt6.QtGui import QAction, QIcon, QKeySequence
from PyQt6.QtWidgets import QApplication, QMainWindow, QStatusBar, QTabWidget, QToolBar

baseDir = os.path.dirname(__file__)

try:
    from ctypes import windll

    myappid = "cz.vut.testing-station.1-0"
    windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
except ImportError:
    pass


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("Application for PCB testing")
        self.setWindowIcon(QIcon(os.path.join(baseDir, "icons", "pcb.png")))
        print(os.path.join(baseDir, "icons", "pcb.png"))
        self.setMinimumSize(QSize(1200, 900))
        self.showMaximized()

        self.toolbar = QToolBar("Main Toolbar")
        self.toolbar.setIconSize(QSize(16, 16))
        self.addToolBar(self.toolbar)

        btnBugAction = QAction(
            QIcon(os.path.join(baseDir, "icons", "bug.png")), "&Bug simulation", self
        )
        btnBugAction.setStatusTip("Simulate a Bug.")
        btnBugAction.setCheckable(True)
        self.toolbar.addAction(btnBugAction)
        btnBugAction.setShortcut(QKeySequence("Ctrl+b"))
        self.toolbar.addSeparator()

        menuBar = self.menuBar()
        fileMenu = menuBar.addMenu("&File")
        fileSubmenu = fileMenu.addMenu("&Submenu")
        fileSubmenu.addAction(btnBugAction)
        btnExitApplication = QAction(
            QIcon(os.path.join(baseDir, "icons", "cross.png")),
            "E&xit Application",
            self,
        )
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
        configTabIdx = tabs.addTab(self.configTab, "Volba konfigurace DPS")

        self.measurementTab = MeasurementTab(self)
        measureTabIdx = tabs.addTab(self.measurementTab, "Měření")

        self.terminalTab = TerminalTab(self)
        terminalTabIdx = tabs.addTab(self.terminalTab, "Terminál")

        self.databaseTab = DatabaseTab(self)
        dbTabIdx = tabs.addTab(self.databaseTab, "Databáze")

        tabs.setCurrentIndex(dbTabIdx)  # DEBUG
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


def main():
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()
    app.exec()


if __name__ == "__main__":
    main()
