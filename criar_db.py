import mysql.connector

# Configurações do banco de dados
DB_USER = "root"
DB_PASSWORD = "Amagedom12"
DB_HOST = "localhost"
DB_NAME = "sys_db"

def criar_conexao():
    """
    Cria uma conexão com o MySQL.
    """
    try:
        conexao = mysql.connector.connect(
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST
        )
        return conexao
    except mysql.connector.Error as err:
        print(f"Erro ao conectar ao MySQL: {err}")
        return None

def criar_banco_e_tabelas():
    """
    Cria o banco de dados e as tabelas necessárias.
    """
    try:
        # Criar a conexão com o MySQL
        conexao = criar_conexao()
        if not conexao:
            print("Erro: Não foi possível estabelecer conexão com o MySQL.")
            return

        cursor = conexao.cursor()

        # Criação do banco de dados caso não exista
        print("Criando o banco de dados 'sys_db'...")
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME}")
        print(f"Banco de dados '{DB_NAME}' criado")

        # Selecionar o banco de dados
        cursor.execute(f"USE {DB_NAME}")
        print(f"Usando o banco de dados '{DB_NAME}'.")

        # Criação da tabela de controle de versões
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS migration_versions (
                id INT AUTO_INCREMENT PRIMARY KEY,
                version INT NOT NULL,
                applied_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        print("Tabela migration_versions criada ou já existente.")

        # Criação da tabela 'clientes'
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS clientes (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nome VARCHAR(255) NOT NULL,
            cpf VARCHAR(15) UNIQUE NOT NULL,
            sexo ENUM ('M', 'F','O'),
            endereco VARCHAR(255),
            numero INT,
            bairro VARCHAR(255),
            data_nascimento DATE,
            email VARCHAR(255),
            telefone VARCHAR(20),
            complemento TEXT,
            ativo BOOLEAN DEFAULT TRUE,
            plano ENUM('MENSAL', 'ANUAL', 'NENHUM') DEFAULT 'NENHUM',
            data_pagamento DATE,
            dia_pagamento ENUM('1','5','10', '15', '20','25' )
        )
        """)
        print("Tabela 'clientes' criada ou já existente.")

        # Fechar a conexão
        cursor.close()
        conexao.close()
        print("Conexão com o banco de dados encerrada.")
    except Exception as e:
        print(f"Erro ao criar o banco de dados ou tabela: {e}")

if __name__ == "__main__":
    criar_banco_e_tabelas()
