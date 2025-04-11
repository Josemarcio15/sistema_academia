# pages/cadastro_clientes.py

from PySide6.QtWidgets import QPushButton

class CadastroClientes:
    def __init__(self, widget_pagina):
        self.ui = widget_pagina

        # Conectando o botão que está DENTRO da página já carregada no stacked
        self.ui.findChild(QPushButton, "button_cadastrar_cliente").clicked.connect(self.executar_cadastro)

    def executar_cadastro(self):
        print("Cadastro executado com sucesso")
