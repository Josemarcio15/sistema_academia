from PySide6.QtCore import QStringListModel, Qt
from PySide6.QtWidgets import QLineEdit, QCompleter, QPushButton
from db.queries import obter_clientes_por_nome
from datetime import datetime

class Aluno:
    def __init__(self, widget_pagina):
        self.ui = widget_pagina

        # findChild
        self.campo_pesquisa = self.ui.findChild(QLineEdit, "lineEdit_aluno_pesquisa_nome")
        self.ui.findChild(QPushButton, "btn_aluno_pesquisa").clicked.connect(self.pesquisa_aluno)
        self.ui.findChild(QPushButton, "btn_aluno_salvar").clicked.connect(self.editar_aluno)

        self.matricula = self.ui.findChild(QLineEdit, "lineEdit_aluno_matricula")
        self.nome = self.ui.findChild(QLineEdit, "lineEdit_aluno_nome")
        self.cpf = self.ui.findChild(QLineEdit, "lineEdit_aluno_cpf")
        self.data_nascimento = self.ui.findChild(QLineEdit, "lineEdit_aluno_nascimento")
        self.email = self.ui.findChild(QLineEdit, "lineEdit_aluno_email")
        self.telefone = self.ui.findChild(QLineEdit, "lineEdit_aluno_telefone")
        self.endereco = self.ui.findChild(QLineEdit, "lineEdit_aluno_endereco")
        self.bairro = self.ui.findChild(QLineEdit, "lineEdit_aluno_bairro")
        self.numero = self.ui.findChild(QLineEdit, "lineEdit_aluno_numero")
        self.complemento = self.ui.findChild(QLineEdit, "lineEdit_aluno_complemento")
        self.sexo = self.ui.findChild(QLineEdit, "lineEdit_aluno_sexo")

        # configurando autocompleter
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

    def pesquisa_aluno(self):
        campo_pesquisa = self.campo_pesquisa.text()
        alunos = obter_clientes_por_nome(campo_pesquisa)

        if alunos:
            aluno = alunos[0]
            self.texto_perfil_aluno(
                aluno["id"],
                aluno["nome"],
                aluno["cpf"],
                aluno["data_nascimento"],
                aluno["email"],
                aluno["telefone"],
                aluno["endereco"],
                aluno["bairro"],
                aluno["numero"],
                aluno["complemento"],
                aluno["sexo"]
            )

    def texto_perfil_aluno(self, matricula, nome, cpf, data_nascimento, email, telefone, endereco,  bairro, numero, complemento, sexo):
        data_formatada = datetime.strptime(str(data_nascimento), "%Y-%m-%d").strftime("%d/%m/%Y")
        
        self.matricula.setText(str(matricula))
        self.nome.setText(nome)
        self.cpf.setText(cpf)
        self.data_nascimento.setText(data_formatada)
        self.email.setText(email)
        self.telefone.setText(telefone)
        self.endereco.setText(endereco)
        self.bairro.setText(bairro)
        self.numero.setText(str(numero))
        self.complemento.setText(complemento)
        self.sexo.setText(sexo)

    def editar_aluno(self):
        novocpf = self.cpf.text()
        print("cpf novo = ", novocpf)