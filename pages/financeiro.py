from PySide6.QtWidgets import QListWidget, QGridLayout, QVBoxLayout, QWidget, QLineEdit, QPushButton
from db.queries import obter_clientes_por_nome
class Financeiro:
    def __init__(self, widget_pagina):
        self.ui = widget_pagina
        self.campo_pesquisa = self.ui.findChild(QLineEdit, "lineEdit_pesquisa_cliente")
        
        self.ui.findChild(QPushButton, "button_financeiro_pesquisar").clicked.connect(self.pesquisar)

        self.quadro = self.ui.findChild(QGridLayout, "gridLayout_nome")

        self.campo_pesquisa.textChanged.connect(self.imprimir_texto)

        self.lista_widget = QListWidget(self.ui.findChild(QWidget, "page_3"))
        self.lista_widget.setObjectName("lista_de_nomes")
        self.lista_widget.setMaximumSize(400, 100)

        self.quadro.addWidget(self.lista_widget, 12, 0, 1, 1)

        self.lista_widget.itemClicked.connect(self.item_selecionado)

    def imprimir_texto(self):
        texto_pesquisa = self.campo_pesquisa.text()
        clientes = obter_clientes_por_nome(texto_pesquisa)

        self.lista_widget.clear()
        for cliente in clientes:
            self.lista_widget.addItem(cliente["nome"])

    def item_selecionado(self, item):
        cliente_nome = item.text()
        self.campo_pesquisa.setText(cliente_nome)

    def pesquisar(self):
        print(self.campo_pesquisa.text())
        self.lista_widget.hide()


