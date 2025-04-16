from .db_connection import criar_conexao

def obter_clientes_por_nome(nome):
    conexao = criar_conexao()
    if conexao:
        cursor = conexao.cursor(dictionary=True)
        # Aqui estamos filtrando por nome usando LIKE
        cursor.execute("SELECT * FROM clientes WHERE nome LIKE %s", ('%' + nome + '%',))
        clientes = cursor.fetchall()
        cursor.close()
        conexao.close()
        return clientes
    return []


def adicionar_cliente(nome, cpf,sexo, endereco, numero, bairro, data_nascimento, email, telefone, complemento):
    conexao = criar_conexao()
    if conexao:
        cursor = conexao.cursor()
        cursor.execute(
            "INSERT INTO clientes (nome, cpf, sexo, endereco, numero, bairro, data_nascimento, email, telefone, complemento) " \
            "VALUES (%s, %s,%s,%s,%s,%s,%s,%s,%s,%s)",
            (nome, 
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
        )
        conexao.commit()
        cursor.close()
        conexao.close()
