from PySide6.QtWidgets import QLineEdit, QPushButton, QCompleter
from PySide6.QtCore import QStringListModel, Qt
from db.queries import obter_clientes_por_nome

class Financeiro:
    def __init__(self, widget_pagina):
        self.ui = widget_pagina
        self.campo_pesquisa = self.ui.findChild(QLineEdit, "lineEdit_pesquisa_cliente")
        
        self.ui.findChild(QPushButton, "button_financeiro_pesquisar").clicked.connect(self.pesquisar)

        self.modelo_completer = QStringListModel()
        self.completer = QCompleter()
        self.completer.setModel(self.modelo_completer)
        self.completer.setCaseSensitivity(Qt.CaseInsensitive)

        self.campo_pesquisa.setCompleter(self.completer)

        self.campo_pesquisa.textChanged.connect(self.atualizar_sugestoes)

    def atualizar_sugestoes(self, texto):
        if texto:
            clientes = obter_clientes_por_nome(texto)
            nomes = [cliente["nome"] for cliente in clientes]
            self.modelo_completer.setStringList(nomes)
        else:
            self.modelo_completer.setStringList([])

    def pesquisar(self):
        print(self.campo_pesquisa.text())
