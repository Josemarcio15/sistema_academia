from PySide6.QtWidgets import QLineEdit, QPushButton, QCompleter, QComboBox, QDateEdit, QLabel
from PySide6.QtCore import QStringListModel, Qt
from db.queries import obter_clientes_por_nome, obter_id_cliente
from datetime import datetime
class Financeiro:
    def __init__(self, widget_pagina):
        self.ui = widget_pagina
        
        #FindChild
        self.ui.findChild(QPushButton, "btn_financeiro_pesquisar").clicked.connect(self.pesquisa_aluno)
        self.ui.findChild(QPushButton, "btn_financeiro_efetuarPagamento").clicked.connect(self.efetuar_pagamento)

        self.campo_pesquisa_matricula = self.ui.findChild(QLineEdit, "lineEdit_pesquisa_id")
        self.campo_pesquisa = self.ui.findChild(QLineEdit, "lineEdit_pesquisa_cliente")
        self.nome = self.ui.findChild(QLineEdit, "lineEdit_financeiro_nome")
        self.cpf = self.ui.findChild(QLineEdit, "lineEdit_financeiro_cpf")
        self.valor_a_pagar = self.ui.findChild(QLineEdit, "lineEdit_financeiro_valorApagar")

        self.data_vencimento = self.ui.findChild(QComboBox, "comboBox_financeiro_diaVencimento")
        self.plano = self.ui.findChild(QComboBox, "comboBox_financeiro_plano")

        self.status = self.ui.findChild(QLabel, "label_financeiro_status")
        self.vencimento = self.ui.findChild(QDateEdit, "dateEdit_financeiro_vencimento")


        #autoComplete
        self.modelo_completer = QStringListModel()
        self.completer = QCompleter()
        self.completer.setModel(self.modelo_completer)
        self.completer.setCaseSensitivity(Qt.CaseInsensitive)
        self.completer.popup().pressed.connect(self.pesquisa_aluno)

        self.campo_pesquisa.setCompleter(self.completer)
        self.campo_pesquisa_matricula.setCompleter(self.completer)

        self.campo_pesquisa.textChanged.connect(self.atualizar_sugestoes)
        self.campo_pesquisa_matricula.textChanged.connect(self.pesquisa_id)

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
    

    def pesquisa_aluno(self):
        campo_pesquisa = self.campo_pesquisa.text()
        self.completer.popup().hide()
        alunos = obter_clientes_por_nome(campo_pesquisa)
        if alunos:
            aluno = alunos[0]
            self.mostrar_dados_aluno(

                aluno["id"],
                aluno["nome"],
                aluno["cpf"],
                aluno["ativo"]
                #aluno["data_nascimento"],
                #aluno["email"],
                #aluno["telefone"],
                #aluno["endereco"],
                #aluno["bairro"],
                #aluno["numero"],
                #aluno["complemento"],
                #aluno["sexo"]
            )
        

    def mostrar_dados_aluno(self, matricula, nome, cpf, ativo):
        

        self.campo_pesquisa_matricula.setText(str(matricula))
        self.nome.setText(nome)
        self.cpf.setText(cpf)
        if ativo == 1:
            self.status.setText("Ativo")
        else:
            self.status.setText("Inativo")

        

    
    def efetuar_pagamento(self):
        try:
            data_hoje = datetime.now().strftime("%Y-%m-%d")
            id_aluno = int(self.campo_pesquisa_matricula.text())
            campos = {
            "dia_pagamento": self.data_vencimento.currentText(),
            "plano": self.plano.currentText(),
            "data_pagamento": data_hoje
            }
            print(campos)
        except Exception as e:
            print(e)

    # def editar_aluno(self):
    #     try:
    #         id_cliente = int(self.matricula.text())
    #         campos = {
    #             "nome": self.nome.text(),
    #             "cpf": self.cpf.text(),
    #             "data_nascimento": datetime.strptime(self.data_nascimento.text(), "%d/%m/%Y").strftime("%Y-%m-%d"),
    #             "email": self.email.text(),
    #             "telefone": self.telefone.text(),
    #             "endereco": self.endereco.text(),
    #             "bairro": self.bairro.text(),
    #             "numero": self.numero.text(),
    #             "complemento": self.complemento.text(),
    #             "sexo": self.sexo.currentText()[0]
    #         }
    #         sucesso = atualizar_cliente(id_cliente, campos)
    #         print("Atualização realizada com sucesso" if sucesso else "Falha na atualização")
    #     except Exception as e:
    #         print(f"Erro ao editar aluno: {e}")
