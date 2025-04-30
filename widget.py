import sys
from PySide6.QtWidgets import QApplication, QWidget
from class_interface.ui_login import Ui_Widget
from class_interface.ui_principal import Ui_Home
from shared.sidebar import Sidebar

class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        
        
        self.ui.button_login.clicked.connect(self.verificar)

    def verificar(self):
        id_admin = self.ui.campo_id.text() 
        self.credencial(id_admin)

    def credencial(self, id_admin):
        self.sidebar = Sidebar()
        self.sidebar.show()
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())
