from PySide6.QtWidgets import QApplication, QWidget
from class_interface.ui_principal import Ui_Home
from pages.home import Home
from pages.cadastro_clientes import CadastroClientes
from pages.financeiro import Financeiro
from pages.configuracao import Configuracao

class Sidebar(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Home()
        self.ui.setupUi(self)

        self.ui.button_bar_inicio.clicked.connect(lambda: self.carregar_pagina(0, Home))
        self.ui.button_bar_cadastrar.clicked.connect(lambda: self.carregar_pagina(1,CadastroClientes))
        self.ui.button_bar_financeiro.clicked.connect(lambda: self.carregar_pagina(2, Financeiro))
        self.ui.button_bar_configuracoes.clicked.connect(lambda: self.carregar_pagina(3, Configuracao))

    def carregar_pagina(self, indice, classe):

        self.ui.stacked_principal.setCurrentIndex(indice)
        widget_pagina = self.ui.stacked_principal.widget(indice)
        self.cadastro_clientes = classe(widget_pagina)
