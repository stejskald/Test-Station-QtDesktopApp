from PyQt6.QtWidgets import QWidget
from include.UIs.ConfigurationTab_ui import Ui_ConfigurationTab


class ConfigurationTab(QWidget, Ui_ConfigurationTab):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
