from PySide6.QtWidgets import QPushButton, QLineEdit, QComboBox, QMessageBox
from db.models import EnviarBanco  # Classe de inserir no banco de dados ao banco

class CadastroClientes:
    def __init__(self, widget_pagina):
        self.ui = widget_pagina
        self.ui.findChild(QPushButton, "button_cadastrar_cliente").clicked.connect(self.executar_cadastro)

    def executar_cadastro(self):

        self.nome = self.ui.findChild(QLineEdit, "cadastro_nome_lineEdit").text()
        self.cpf = self.ui.findChild(QLineEdit, "cadastro_cpf_lineEdit").text()
        self.sexo = self.ui.findChild(QComboBox, "cadastro_sexo_comboBox").currentText()
        self.endereco = self.ui.findChild(QLineEdit, "cadastro_endereco_lineEdit").text() 
        self.numero = self.ui.findChild(QLineEdit, "cadastro_numero_lineEdit").text() 
        self.bairro = self.ui.findChild(QLineEdit, "cadastro_bairro_lineEdit").text() 
        self.data_nascimento = self.ui.findChild(QLineEdit, "cadastro_nascimento_lineEdit").text() 
        self.email = self.ui.findChild(QLineEdit, "cadastro_email_lineEdit").text() 
        self.telefone = self.ui.findChild(QLineEdit, "cadastro_telefone_lineEdit").text()
        self.complemento = self.ui.findChild(QLineEdit, "cadastro_complemento_lineEdit").text() 

        if self.validar_dados() == True:
            cliente = EnviarBanco(self.nome, 
                    self.cpf, 
                    self.sexo, 
                    self.endereco,
                    self.numero, 
                    self.bairro, 
                    self.data_nascimento, 
                    self.email, 
                    self.telefone,
                    self.complemento
                    )     
            cliente.salvar_no_banco()
        else:
            print("erro depois implementar msgbox")

    def validar_dados(self):

        if self.nome is None or self.nome.strip() == "":
            self.msgbox_erro("Nome não pode ser vazio.")
            return False
        if self.cpf is None or self.cpf.strip() == "":
            self.msgbox_erro("CPF não pode ser vazio.")
            return False
        if self.sexo is None or self.sexo.strip() == "":
            self.msgbox_erro("Sexo não pode ser vazio.")
            return False
        if self.endereco is None or self.endereco.strip() == "":
            self.msgbox_erro("Endereço não pode ser vazio.")
            return False
        if self.numero is None or self.numero.strip() == "":
            self.msgbox_erro("Número não pode ser vazio.")
            return False
        if self.bairro is None or self.bairro.strip() == "":
            self.msgbox_erro("Bairro não pode ser vazio.")
            return False
        if self.data_nascimento is None or self.data_nascimento.strip() == "":
            self.msgbox_erro("Data de nascimento não pode ser vazia.")
            return False
        if self.email is None or self.email.strip() == "":
            self.msgbox_erro("E-mail não pode ser vazio.")
            return False
        if self.telefone is None or self.telefone.strip() == "":
            self.msgbox_erro("Telefone não pode ser vazio.")
            return False
        return True
    
    
    def msgbox_erro(self, msg_erro):
        QMessageBox.critical(self.ui, "Erro!", msg_erro)


