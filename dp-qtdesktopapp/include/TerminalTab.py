from PyQt6.QtWidgets import QWidget
from include.UIs.TerminalTab_ui import Ui_TerminalTab


class TerminalTab(QWidget, Ui_TerminalTab):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
