from PySide6.QtWidgets import QLineEdit, QPushButton, QCompleter
from PySide6.QtCore import QStringListModel, Qt
from db.queries import obter_clientes_por_nome, obter_id_cliente

class Financeiro:
    def __init__(self, widget_pagina):
        self.ui = widget_pagina
        
        #FindChild
        self.campo_pesquisa = self.ui.findChild(QLineEdit, "lineEdit_pesquisa_cliente")
        self.campo_pesquisa_id = self.ui.findChild(QLineEdit, "lineEdit_pesquisa_id")
        self.ui.findChild(QPushButton, "button_financeiro_pesquisar").clicked.connect(self.mostrar_print)
        
        #autoComplete
        self.modelo_completer = QStringListModel()
        self.completer = QCompleter()
        self.completer.setModel(self.modelo_completer)
        self.completer.setCaseSensitivity(Qt.CaseInsensitive)

        self.campo_pesquisa.setCompleter(self.completer)
        self.campo_pesquisa_id.setCompleter(self.completer)

        self.campo_pesquisa.textChanged.connect(self.atualizar_sugestoes)
        self.campo_pesquisa_id.textChanged.connect(self.pesquisa_id)

    def atualizar_sugestoes(self, texto):
        if texto:
            clientes = obter_clientes_por_nome(texto)
            nomes = [cliente["nome"] for cliente in clientes]
            self.modelo_completer.setStringList(nomes)
        else:
            self.modelo_completer.setStringList([])

    def pesquisa_id(self, numero):
        if numero.isdigit():
            ident = int(numero)
            numero_id_encontrado = obter_id_cliente(ident)
            numero_id = [str(cliente["id"]) for cliente in numero_id_encontrado]
            self.modelo_completer.setStringList(numero_id)
        else:
            self.modelo_completer.setStringList([])
    

    def mostrar_print(self):
        print(self.campo_pesquisa.text())
