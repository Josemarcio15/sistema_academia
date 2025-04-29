from PySide6.QtWidgets import QPushButton, QLineEdit, QComboBox, QMessageBox
from db.models import EnviarBanco
from db.queries import cpf_existe
import re

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

        if self.validar_dados(nome, cpf, sexo, endereco, numero, bairro, data_nascimento, email, telefone) == True:
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

    def validar_dados(self, nome, cpf, sexo, endereco, numero, bairro, data_nascimento, email, telefone):

        if nome is None or nome.strip() == "":
            self.msgbox_erro("Nome não pode ser vazio.")
            return False
        if cpf is None or not self.validar_cpf(cpf):
            if cpf_existe(cpf):
                self.msgbox_erro("CPF já existe")
                return False
            self.msgbox_erro("Formato do CPF invalido")
            return False
        if sexo is None or sexo.strip() == "" or sexo.strip() == "S":
            self.msgbox_erro("Campo sexo não pode ser vazio.")
            return False
        if endereco is None or endereco.strip() == "":
            self.msgbox_erro("Endereço não pode ser vazio.")
            return False
        if numero is None or not numero.isdigit():
            self.msgbox_erro("Número não pode ser vazio ou conter letras.")
            return False
        if bairro is None or bairro.strip() == "":
            self.msgbox_erro("Bairro não pode ser vazio.")
            return False
        if data_nascimento is None or not self.validar_data(data_nascimento):
            self.msgbox_erro("Data de nascimento inválida.")
            return False
        if email is None or not self.validar_email(email):
            self.msgbox_erro("Formato de E-mail inválido")
            return False
        if telefone is None or not self.validar_telefone(telefone):
            self.msgbox_erro("Formato de telefone invalido.")
            return False
        return True
    
    def validar_email(self, email):
        if '@' in email:
            return True
        return False

    def validar_data(self, data):
        if not re.match(r'^\d{2}/\d{2}/\d{4}$', data):
            return False
        try:
            dia, mes, ano = map(int, data.split('/'))
            if not (1 <= dia <= 31 and 1 <= mes <= 12 and 1900 <= ano <= 2100):
                return False
            return True
        except:
            return False

    def validar_cpf(self, cpf):
        if not cpf_existe(cpf):  # Verifica se o CPF não existe no banco
            return bool(re.match(r'^\d{3}\.\d{3}\.\d{3}-\d{2}$', cpf))
        return False  # Retorna False se o CPF já existir no banco

    def validar_telefone(self, telefone):
        return bool(re.match(r'^\(\d{2}\) \d \d{4}-\d{4}$', telefone))

    def msgbox_erro(self, msg_erro):
        QMessageBox.critical(self.ui, "Erro!", msg_erro)


