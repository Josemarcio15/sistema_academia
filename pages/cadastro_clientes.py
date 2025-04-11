from PySide6.QtWidgets import QPushButton, QLineEdit, QComboBox

class CadastroClientes:
    def __init__(self, widget_pagina):
        self.ui = widget_pagina

        self.ui.findChild(QPushButton, "button_cadastrar_cliente").clicked.connect(self.executar_cadastro)


    def executar_cadastro(self, cpf):
        nome = self.ui.findChild(QLineEdit, "cadastro_nome_lineEdit").text()
        cpf = self.ui.findChild(QLineEdit, "cadastro_cpf_lineEdit").text()
        sexo = self.ui.findChild(QComboBox, "cadastro_sexo_comboBox").currentText()
        endereco = self.ui.findChild(QLineEdit,"cadastro_endereco_lineEdit").text() 
        numero = self.ui.findChild(QLineEdit,"cadastro_numero_lineEdit").text() 
        complemento = self.ui.findChild(QLineEdit,"cadastro_complemento_lineEdit").text() 
        bairro = self.ui.findChild(QLineEdit,"cadastro_bairro_lineEdit").text() 
        data_nascimento = self.ui.findChild(QLineEdit,"cadastro_nascimento_lineEdit").text() 
        email = self.ui.findChild(QLineEdit,"cadastro_email_lineEdit").text() 
        telefone = self.ui.findChild(QLineEdit,"cadastro_telefone_lineEdit").text() 
                                     
        print("Cadastro executado com sucesso", 
              nome,
              cpf,
              sexo,
              endereco,
              numero,
              complemento,
              bairro,
              data_nascimento,
              email,
              telefone
              )

