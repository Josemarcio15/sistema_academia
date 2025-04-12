from queries import adicionar_cliente
class EnviarBanco:
    def __init__(self, nome, cpf, sexo, endereco, numero, bairro, data_nascimento, email, telefone):
        self.nome = nome
        self.cpf = cpf
        self.sexo = sexo
        self.endereco = endereco
        self.numero = numero
        self.bairro = bairro
        self.data_nascimento = data_nascimento
        self.email = email
        self.telefone = telefone

    def salvar_no_banco(self):
        adicionar_cliente(self.nome, 
                          self.cpf, 
                          self.sexo, 
                          self.endereco, 
                          self.numero, 
                          self.bairro, 
                          self.data_nascimento, 
                          self.email, 
                          self.telefone
                          )
        

