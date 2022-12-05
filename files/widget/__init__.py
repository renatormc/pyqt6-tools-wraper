from .{{ main_window_module }} import Ui_{{ widget_name }}
from PyQt6.QtWidgets import QWidget

class {{ widget_name }}(QWidget):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.ui = Ui_{{ widget_name }}()
        self.ui.setupUi(self)
        self.connections()

    def connections(self):
        pass
