from PySide6.QtWidgets import QPushButton, QLineEdit, QComboBox, QMessageBox
from db.models import EnviarBanco
from db.queries import cpf_existe
from shared.validar_dados_cliente import Validador

class CadastroClientes:
    def __init__(self, widget_pagina):
        self.ui = widget_pagina
        self.ui.findChild(QPushButton, "button_cadastrar_cliente").clicked.connect(self.executar_cadastro)

        self.nome = self.ui.findChild(QLineEdit, "cadastro_nome_lineEdit")
        self.cpf = self.ui.findChild(QLineEdit, "cadastro_cpf_lineEdit")
        self.sexo = self.ui.findChild(QComboBox, "cadastro_sexo_comboBox")
        self.endereco = self.ui.findChild(QLineEdit, "cadastro_endereco_lineEdit") 
        self.numero = self.ui.findChild(QLineEdit, "cadastro_numero_lineEdit") 
        self.bairro = self.ui.findChild(QLineEdit, "cadastro_bairro_lineEdit") 
        self.data_nascimento = self.ui.findChild(QLineEdit, "cadastro_nascimento_lineEdit") 
        self.email = self.ui.findChild(QLineEdit, "cadastro_email_lineEdit") 
        self.telefone = self.ui.findChild(QLineEdit, "cadastro_telefone_lineEdit")
        self.complemento = self.ui.findChild(QLineEdit, "cadastro_complemento_lineEdit") 

        self.cpf.setInputMask("000.000.000-00;_")
        self.data_nascimento.setInputMask("00/00/0000;_")
        self.telefone.setInputMask("(00) 0 0000-0000;_")

        self.validador = Validador(self.ui)  # Instanciando a classe Validador

    def executar_cadastro(self):
        
        nome = self.nome.text()
        cpf = self.cpf.text()
        sexo = self.sexo.currentText()[0]
        endereco = self.endereco.text()
        numero = self.numero.text()
        bairro = self.bairro.text()
        data_nascimento = self.data_nascimento.text()
        email = self.email.text()
        telefone = self.telefone.text()
        complemento = self.complemento.text()

        if self.validador.validar_dados(nome, cpf, sexo, endereco, numero, bairro, data_nascimento, email, telefone):  # Usando o método da classe Validador
            cliente = EnviarBanco(
                    nome, 
                    cpf, 
                    sexo, 
                    endereco,
                    numero, 
                    bairro, 
                    data_nascimento, 
                    email, 
                    telefone,
                    complemento
                    )     
            cliente.salvar_no_banco()
