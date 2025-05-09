from PySide6.QtWidgets import QLineEdit, QPushButton, QWidget
from db.queries import atualizar_taxas
from datetime import date

class Configuracao(QWidget):
    def __init__(self, widget_pagina):
        self.ui = widget_pagina
        
        #findchild
        self.campo_diario = self.ui.findChild(QLineEdit, "lineEdit_config_diaria")
        self.campo_mensal = self.ui.findChild(QLineEdit, "lineEdit_config_mensal")
        self.campo_trimestral = self.ui.findChild(QLineEdit, "lineEdit_config_trimestral")
        self.campo_semestral = self.ui.findChild(QLineEdit, "lineEdit_config_semestral")
        self.campo_anual = self.ui.findChild(QLineEdit, "lineEdit_config_anual")

        self.ui.findChild(QPushButton, "btn_config_salvar").clicked.connect(self.salvar_no_db)
    
    def salvar_no_db(self):
        try:

            # def para aceitar , e .
            def tratar_valor(valor):
                return float(valor.replace(",", ".")) if valor else 0.0

            campos = {
                "DIARIA": tratar_valor(self.campo_diario.text()),
                "MENSAL": tratar_valor(self.campo_mensal.text()),
                "TRIMESTRAL": tratar_valor(self.campo_trimestral.text()),
                "SEMESTRAL": tratar_valor(self.campo_semestral.text()),
                "ANUAL": tratar_valor(self.campo_anual.text())
            }

            data_inicio = date.today()
            data_fim = None

            taxas = [
                {"tipo": tipo, "valor": valor, "data_inicio": data_inicio, "data_fim": data_fim}
                for tipo, valor in campos.items()
            ]

            sucesso = atualizar_taxas(taxas)
            if sucesso:
                print("Atualização realizada com sucesso")
            else:
                print("Falha na atualização: Verifique a função 'atualizar_taxas'")
        except ValueError as ve:
            print(f"Erro de conversão: {ve}")
        except Exception as e:
            print(f"Erro ao salvar taxas: {e}")

