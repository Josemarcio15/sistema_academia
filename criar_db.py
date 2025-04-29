import mysql.connector

# Configurações do banco de dados
DB_USER = "root"
DB_PASSWORD = "Amagedom12"
DB_HOST = "localhost"
DB_NAME = "sys_mar"

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
        print("Criando o banco de dados 'sys_mar'...")
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME}")
        print(f"Banco de dados '{DB_NAME}' criado ou já existente.")

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
        print("Tabela 'migration_versions' criada ou já existente.")

        # Criação da tabela 'clientes'
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS clientes (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nome VARCHAR(255) NOT NULL,
            cpf VARCHAR(15) UNIQUE NOT NULL,
            sexo CHAR(1),
            endereco VARCHAR(255),
            numero INT,
            bairro VARCHAR(255),
            data_nascimento DATE,
            email VARCHAR(255),
            telefone VARCHAR(20),
            complemento TEXT
        )
        """)
        print("Tabela 'clientes' criada ou já existente.")

        # Verificar a versão atual do banco
        cursor.execute("SELECT MAX(version) FROM migration_versions")
        result = cursor.fetchone()
        last_version = result[0] if result[0] else 0

        # Aplique novas migrações, caso necessário (simulação de migrações)
        if last_version < 1:
            aplicar_migracao_1(cursor)
            registrar_migracao(cursor, 1)
            print("Migração 1 aplicada.")

        # Fechar a conexão
        cursor.close()
        conexao.close()
        print("Conexão com o banco de dados encerrada.")
    except Exception as e:
        print(f"Erro ao criar o banco de dados ou tabela: {e}")

def aplicar_migracao_1(cursor):
    """
    Aplica a migração 1 no banco de dados.
    Exemplo: Adicionar uma nova coluna na tabela 'clientes'.
    """
    cursor.execute("""
        ALTER TABLE clientes
        ADD COLUMN ativo BOOLEAN DEFAULT TRUE
    """)

def registrar_migracao(cursor, version):
    """
    Registra a migração aplicada na tabela 'migration_versions'.
    """
    cursor.execute("""
        INSERT INTO migration_versions (version)
        VALUES (%s)
    """, (version,))

if __name__ == "__main__":
    criar_banco_e_tabelas()
