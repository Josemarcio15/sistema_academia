from .db_connection import criar_conexao

def obter_clientes_por_nome(nome):
    conexao = criar_conexao()
    if conexao:
        cursor = conexao.cursor(dictionary=True)
        cursor.execute("SELECT * FROM clientes WHERE nome LIKE %s", ('%' + nome + '%',))
        clientes = cursor.fetchall()
        cursor.close()
        conexao.close()
        return clientes
    return []

def obter_id_cliente(numero):
    conexao = criar_conexao()
    if conexao:
        cursor = conexao.cursor(dictionary=True)
        cursor.execute("SELECT * FROM clientes WHERE id = %s", (numero,))
        clientes = cursor.fetchall()
        cursor.close()
        conexao.close()
        return clientes
    return []
def cpf_existe(cpf): #verifica se o cpf não é duplicado

    conexao = criar_conexao()

    if conexao:
        try:
            cursor = conexao.cursor()
            cursor.execute("SELECT COUNT(*) FROM clientes WHERE cpf = %s", (cpf,))
            result = cursor.fetchone()
            cursor.close()
            conexao.close()
            return result[0] > 0
        except Exception as e:
            print(f"Erro ao verificar CPF no banco de dados: {e}")
            return False
    return False

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

def atualizar_cliente(id_cliente, campos):
    if not campos:
        return False

    conexao = criar_conexao()
    if conexao:
        cursor = conexao.cursor()
        try:
            colunas = ", ".join([f"{col} = %s" for col in campos])
            valores = list(campos.values())
            valores.append(id_cliente)

            sql = f"UPDATE clientes SET {colunas} WHERE id = %s"
            cursor.execute(sql, valores)
            conexao.commit()
            return True
        except Exception as e:
            print(f"Erro ao atualizar cliente: {e}")
            return False
        finally:
            cursor.close()
            conexao.close()
    return False

def atualizar_taxas(taxas):
    conexao = criar_conexao()
    if conexao:
        cursor = conexao.cursor()
        try:
            for taxa in taxas:
                cursor.execute(
                    """
                    UPDATE taxas
                    SET valor = %s,
                        data_inicio = %s,
                        data_fim = %s
                    WHERE tipo = %s
                    """,
                    (taxa['valor'], taxa['data_inicio'], taxa.get('data_fim'), taxa['tipo'])
                )
            conexao.commit()
            return True
        except Exception as e:
            print(f"Erro ao atualizar taxas: {e}")
        finally:
            cursor.close()
            conexao.close()
    return False

def obter_valor_taxa_por_tipo(tipo):
    conexao = criar_conexao()
    if conexao:
        try:
            cursor = conexao.cursor(dictionary=True)
            cursor.execute("SELECT valor FROM taxas WHERE tipo = %s", (tipo.upper(),))
            resultado = cursor.fetchone()
            return resultado['valor'] if resultado else None
        except Exception as e:
            
            return print(f"Erro ao obter taxa do tipo '{tipo}': {e}")
        finally:
            cursor.close()
            conexao.close()
    return "nada encontrado"