from PySide6.QtWidgets import QLineEdit, QPushButton, QCompleter, QComboBox, QDateEdit, QLabel, QRadioButton
from PySide6.QtCore import QStringListModel, Qt
from db.queries import obter_clientes_por_nome, obter_id_cliente, obter_valor_taxa_por_tipo, obter_cliente_por_nome_exato
from datetime import datetime
class Financeiro:
    def __init__(self, widget_pagina):
        self.ui = widget_pagina
        self.taxa_variavel_global = None

        #FindChild
        self.ui.findChild(QPushButton, "btn_financeiro_pesquisar").clicked.connect(self.pesquisa_aluno)
        self.ui.findChild(QPushButton, "btn_financeiro_efetuarPagamento").clicked.connect(self.efetuar_pagamento)

        self.dias_a_pagar = self.ui.findChild(QDateEdit, "dateEdit_financeiro_dias")

        self.campo_pesquisa_matricula = self.ui.findChild(QLineEdit, "lineEdit_pesquisa_id")
        self.campo_pesquisa = self.ui.findChild(QLineEdit, "lineEdit_pesquisa_cliente")
        self.nome = self.ui.findChild(QLineEdit, "lineEdit_financeiro_nome")
        self.cpf = self.ui.findChild(QLineEdit, "lineEdit_financeiro_cpf")
        self.valor_a_pagar = self.ui.findChild(QLineEdit, "lineEdit_financeiro_valorApagar")
        

        self.data_vencimento = self.ui.findChild(QLabel, "label_financeiro_vencimento")
        self.status = self.ui.findChild(QLabel, "label_financeiro_status")

        self.plano = self.ui.findChild(QComboBox, "comboBox_financeiro_plano")

        self.valor_normal = self.ui.findChild(QRadioButton, "radioButton_financeiro_valorNormal")
        self.valor_desconto = self.ui.findChild(QRadioButton, "radioButton_financeiro_valorDesconto")

        #ativar o dateEdit
        self.plano.currentTextChanged.connect(self.verificar_plano)

        #autoComplete
        self.modelo_completer = QStringListModel()
        self.completer = QCompleter()
        self.completer.setModel(self.modelo_completer)
        self.completer.setCaseSensitivity(Qt.CaseInsensitive)
        self.completer.popup().pressed.connect(self.pesquisa_aluno)

        self.campo_pesquisa.setCompleter(self.completer)
        self.campo_pesquisa_matricula.setCompleter(self.completer)
        
        #captura de eventos
        self.campo_pesquisa.textChanged.connect(self.atualizar_sugestoes)
        self.campo_pesquisa_matricula.textChanged.connect(self.pesquisa_id)
        
        self.valor_normal.clicked.connect(self.chamar_valor_normal)
        self.valor_desconto.clicked.connect(self.chamar_valor_desconto)

        self.dias_a_pagar.dateChanged.connect(self.calcular_diaria)

    def calcular_diaria(self):
        if self.dias_a_pagar.isEnabled() and self.valor_normal.isChecked():
            dias = self.dias_a_pagar.date().day()
            print("chamou calcular diaria")
            valor_diaria = obter_valor_taxa_por_tipo("DIARIA")
            valor_total = dias * valor_diaria
            self.valor_a_pagar.setText(str(valor_total))
        else:
            self.valor_a_pagar.setText("")

    def chamar_valor_normal(self):

        if self.valor_normal.isChecked():
            self.dias_a_pagar.setDate(self.dias_a_pagar.date().addDays(-self.dias_a_pagar.date().day() + 1))
            texto = obter_valor_taxa_por_tipo(self.taxa_variavel_global)
            self.valor_a_pagar.setText(str(texto))

    def chamar_valor_desconto(self):

        if self.valor_desconto.isChecked():
            print("valor desconto checked")

    def verificar_plano(self, combox_plano):
        if combox_plano != "":
            self.valor_a_pagar.setEnabled(True)

            if combox_plano == "Diario":
                self.dias_a_pagar.setEnabled(True)
                self.valor_normal.setEnabled(True)
                self.valor_desconto.setEnabled(True)
                self.taxa_variavel_global = "DIARIA"
                self.chamar_valor_normal()


            elif combox_plano == "Mensal":
                self.valor_normal.setEnabled(True)
                self.valor_desconto.setEnabled(True)
                self.taxa_variavel_global = "MENSAL"
                self.dias_a_pagar.setEnabled(False)
                self.chamar_valor_normal()

            elif combox_plano == "Trimestral":
                self.valor_normal.setEnabled(True)
                self.valor_desconto.setEnabled(True)
                self.taxa_variavel_global = "TRIMESTRAL"
                self.dias_a_pagar.setEnabled(False)
                self.chamar_valor_normal()

            elif combox_plano == "Semestral":
                self.valor_normal.setEnabled(True)
                self.valor_desconto.setEnabled(True)
                self.taxa_variavel_global = "SEMESTRAL"
                self.dias_a_pagar.setEnabled(False)
                self.chamar_valor_normal()

            elif combox_plano == "Anual":
                self.valor_normal.setEnabled(True)
                self.valor_desconto.setEnabled(True)
                self.taxa_variavel_global = "ANUAL"
                self.dias_a_pagar.setEnabled(False)
                self.chamar_valor_normal()

            else:
                self.dias_a_pagar.setEnabled(False)

        else:
            self.dias_a_pagar.setEnabled(False)
            self.valor_a_pagar.setEnabled(False)
        




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
        alunos = obter_cliente_por_nome_exato(campo_pesquisa)

        
        if alunos:
            aluno = alunos[0]
            self.mostrar_dados_aluno(

                aluno["id"],
                aluno["nome"],
                aluno["cpf"],
                aluno["ativo"],
                aluno["data_vencimento"]
            )
        

    def mostrar_dados_aluno(self, matricula, nome, cpf, ativo, data_vencimento):
        if data_vencimento:
            data_formatada = datetime.strptime(str(data_vencimento), "%Y-%m-%d").strftime("%d/%m/%Y")
        else:
            data_formatada = "N/A"
        self.campo_pesquisa_matricula.setText(str(matricula))
        self.nome.setText(nome)
        self.cpf.setText(cpf)
        if ativo == 1:
            self.status.setText("Ativo")
        else:
            self.status.setText("Inativo")
        self.data_vencimento.setText(str(data_formatada))

        

    
    def efetuar_pagamento(self):
        print(obter_valor_taxa_por_tipo("DIARIA"))
    #     try:
    #         data_hoje = datetime.now().strftime("%Y-%m-%d")
    #         id_aluno = int(self.campo_pesquisa_matricula.text())
    #         campos = {
    #         "plano": self.plano.currentText(),
    #         "data_pagamento": data_hoje
    #         }
    #         print(campos)
    #     except Exception as e:
    #         print(e)

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
