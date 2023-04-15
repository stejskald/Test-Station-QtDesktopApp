from random import randint

import pyqtgraph as pg
from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtGui import QFont, QPalette
from PyQt6.QtWidgets import QWidget
from include.UIs.MeasurementTab_ui import Ui_MeasurementTab


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
