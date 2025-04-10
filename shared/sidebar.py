from PySide6.QtWidgets import QApplication, QWidget

from class_interface.ui_principal import Ui_Home
class Sidebar(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Home()
        self.ui.setupUi(self)

        self.ui.button_bar_inicio.clicked.connect(lambda:self.navegar_indice(0))
        self.ui.button_bar_cadastrar.clicked.connect(lambda:self.navegar_indice(1))
        self.ui.button_bar_financeiro.clicked.connect(lambda:self.navegar_indice(2))
        self.ui.button_bar_configuracoes.clicked.connect(lambda: self.navegar_indice(3))

        
    def navegar_indice(self, indice):
        
        self.ui.stacked_principal.setCurrentIndex(indice)
        print("navegando para o indice: ", indice)
