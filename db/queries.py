from .db_connection import criar_conexao

def obter_clientes():
    conexao = criar_conexao()
    if conexao:
        cursor = conexao.cursor(dictionary=True)
        cursor.execute("SELECT * FROM clientes")
        clientes = cursor.fetchall()
        cursor.close()
        conexao.close()
        return clientes
    return []

def adicionar_cliente(nome, cpf):
    conexao = criar_conexao()
    if conexao:
        cursor = conexao.cursor()
        cursor.execute("INSERT INTO clientes (nome, cpf) VALUES (%s, %s)", (nome, cpf))
        conexao.commit()
        cursor.close()
        conexao.close()
