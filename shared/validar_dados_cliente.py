from PySide6.QtWidgets import QMessageBox
from db.queries import cpf_existe
import re

class Validador:
    def __init__(self, ui):
        self.ui = ui

    def validar_dados(self, nome, cpf, sexo, endereco, numero, bairro, data_nascimento, email, telefone):
        if nome is None or nome.strip() == "":
            self.msgbox_erro("Nome não pode ser vazio.")
            return False

        if cpf is None or not self.validar_cpf(cpf):
            if cpf_existe(cpf):
                self.msgbox_erro("CPF já existe")
                return False
            self.msgbox_erro("Formato do CPF inválido")
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
            self.msgbox_erro("Formato de telefone inválido.")
            return False

        return True

    def validar_email(self, email):
        return '@' in email

    def validar_data(self, data):
        if not re.match(r'^\d{2}/\d{2}/\d{4}$', data):
            return False
        try:
            dia, mes, ano = map(int, data.split('/'))
            return (1 <= dia <= 31 and 1 <= mes <= 12 and 1900 <= ano <= 2100)
        except:
            return False

    def validar_cpf(self, cpf):
        if not cpf_existe(cpf):
            return bool(re.match(r'^\d{3}\.\d{3}\.\d{3}-\d{2}$', cpf))
        return False

    def validar_telefone(self, telefone):
        return bool(re.match(r'^\(\d{2}\) \d \d{4}-\d{4}$', telefone))

    def msgbox_erro(self, msg_erro):
        QMessageBox.critical(self.ui, "Erro!", msg_erro)
