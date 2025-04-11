from PySide6.QtWidgets import QApplication, QWidget
from class_interface.ui_principal import Ui_Home
from pages.cadastro_clientes import CadastroClientes

class Sidebar(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Home()
        self.ui.setupUi(self)


        # Conectando botões
        self.ui.button_bar_inicio.clicked.connect(lambda: self.carregar_pagina(0))
        self.ui.button_bar_cadastrar.clicked.connect(lambda: self.carregar_pagina(1))
        self.ui.button_bar_financeiro.clicked.connect(lambda: self.carregar_pagina(2))
        self.ui.button_bar_configuracoes.clicked.connect(lambda: self.carregar_pagina(3))

    def carregar_pagina(self, indice):
        print("Carregando Cadastro de Clientes")
        self.ui.stacked_principal.setCurrentIndex(indice)

        widget_pagina = self.ui.stacked_principal.widget(indice)
        self.cadastro_clientes = CadastroClientes(widget_pagina)
