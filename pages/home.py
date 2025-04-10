# This Python file uses the following encoding: utf-8
#from PySide6 import QtCore
from PySide6.QtWidgets import QApplication, QWidget
from class_interface.ui_login import Ui_Widget

class Home(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Home()
        self.ui.setupUi(self)
        
