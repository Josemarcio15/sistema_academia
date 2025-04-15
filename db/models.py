from .queries import adicionar_cliente
from datetime import datetime

class EnviarBanco:
    def __init__(self, nome, cpf, sexo, endereco, numero, bairro, data_nascimento, email, telefone, complemento=""):
        self.nome = nome
        self.cpf = cpf
        self.sexo = sexo
        self.endereco = endereco
        self.numero = numero
        self.bairro = bairro
        self.data_nascimento = data_nascimento
        self.email = email
        self.telefone = telefone
        self.complemento = complemento

    def salvar_no_banco(self):
        data_formatada = datetime.strptime(self.data_nascimento, "%d/%m/%Y").strftime("%Y-%m-%d")

        adicionar_cliente(self.nome, 
                          self.cpf, 
                          self.sexo, 
                          self.endereco, 
                          self.numero, 
                          self.bairro, 
                          data_formatada, 
                          self.email, 
                          self.telefone,
                          self.complemento
                          )

