from PySide6.QtWidgets import QPushButton, QLineEdit, QComboBox, QMessageBox, QListView, QGridLayout
from PySide6.QtCore import QStringListModel
from db.queries import obter_clientes_por_nome

class Financeiro:
    def __init__(self, widget_pagina):
        self.ui = widget_pagina

    #     self.campo_pesquisa = self.ui.findChild(QLineEdit, "lineEdit_pesquisa_cliente")
    #     self.lista_nomes = QListView(u"listView_pesquisa_cliente") #"listView_pesquisa_cliente")
    #     layout = self.ui.findChild(QGridLayout, "gridLayout_nome")
    #     layout.addWidget(self.lista_nomes)


    #     self.modelo_lista = QStringListModel()  # Modelo de dados da lista
    #     self.lista_nomes.setModel(self.modelo_lista)
    #     self.campo_pesquisa.textChanged.connect(self.imprimir_texto)
        
    # def imprimir_texto(self):
    #     texto_pesquisa = self.campo_pesquisa.text()
    #     clientes = obter_clientes_por_nome(texto_pesquisa)
    #     nomes = []
    #     for cliente in clientes:
    #         print("Nome:", cliente["nome"])
    #         print("Telefone:", cliente["telefone"])
    #         print("Email:", cliente["email"])
    #         nomes.append(cliente["nome"])
    #     self.modelo_lista.setStringList(nomes)
