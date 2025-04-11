import mysql.connector
from .db_config import DB_USER, DB_PASSWORD, DB_HOST, DB_NAME

def criar_conexao():
    try:
        conexao = mysql.connector.connect(
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            database=DB_NAME
        )
        return conexao
    except mysql.connector.Error as err:
        print(f"Erro ao conectar ao MySQL: {err}")
        return None
