import pyodbc

def retorna_cursor_banco_de_dados():
    connection = pyodbc.connect(retorno_string_conexao_banco_dados())
    cursor = connection.cursor()
    return cursor, connection

def retorno_string_conexao_banco_dados():
    return(
        "DRIVER={SQL Server};"
        "SERVER=hoesql633.na.xom.com;"
        "DATABASE=Skillup_EVFRANC;"
        "UID=evfranc;"
        #"PWD=???;"
        "Trusted_Connection=yes"
    )

#Como chama a funcao com sucesso:
#select_banco_dados()
def select_banco_dados():
    cursor, connection = retorna_cursor_banco_de_dados()
    cursor.execute("select * from cliente;")
    clientes = cursor.fetchall()
    print(clientes)
    connection.commit()

#Como chama a funcao com sucesso:
#cliente = {"Nome": "Julio", "CPF": "29377767890"}
#insert_banco_dados(cliente)
def insert_banco_dados(cliente):
    print (cliente)
    cursor, connection = retorna_cursor_banco_de_dados()
    insert_query = """
    INSERT INTO cliente (nome, cpf, rg, data_nascimento, cep, logradouro, bairro, cidade, estado, complemento, numero_residencia)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
    """
    values = (cliente['nome'], cliente['cpf'], cliente['rg'], cliente['nascimento'], cliente['cep']['CEP'], cliente['cep']['Logradouro'], cliente['cep']['Bairro'], cliente['cep']['Cidade'], cliente['cep']['Estado'], cliente['complemento'], cliente['numero'])
    #values = ('Rodrigo Nestor6', '293.345.678-90','07.123.235-9', '01/01/2001', '80123-234', '123')
    cursor.execute(insert_query, values)
    connection.commit()
    print ("Cliente inserido na base de dados com sucesso!")
    
#Como chama a funcao com sucesso:
#delete_banco_dados(cliente["CPF"])   
def delete_banco_dados(cliente):
    cursor, connection = retorna_cursor_banco_de_dados()
    delete_query = "DELETE FROM cliente WHERE cpf = '" + cliente['cpf'] + "';"
    #print(delete_query)
    cursor.execute(delete_query)
    connection.commit()
    print ("Cliente apagado da base de dados com sucesso!")

#Como chama a funcao com sucesso:
#cliente = {"Nome": "Julio", "CPF": "29377767890"}
#update_nome_banco_dados(cliente)
def update_nome_banco_dados(cliente):
    cursor, connection = retorna_cursor_banco_de_dados()
    update_query = "UPDATE cliente SET nome = '" +cliente['nome']+ "', rg = '" +cliente['rg']+ "', data_nascimento = '" +cliente['nascimento']+ "', cep = '"+cliente['cep']['CEP']+ "', logradouro = '" +cliente['cep']['Logradouro']+ "', bairro = '" +cliente['cep']['Bairro']+ "', cidade = '" +cliente['cep']['Cidade']+ "', estado = '"+cliente['cep']['Estado']+ "', complemento = '" +cliente['complemento']+ "', numero_residencia = '"+cliente['numero']+ "' WHERE cpf = '" + cliente['cpf'] + "';"
    #print(update_query)
    cursor.execute(update_query)
    connection.commit()
    print ("Update de cliente na base de dados com sucesso!")

#Select direto na base de dados
def buscar_nome_banco_dados(cliente):
    cursor, connection = retorna_cursor_banco_de_dados()
    buscar_query = "SELECT * FROM cliente where cpf = '" + cliente['cpf'] + "';"
    #print(buscar_query)
    cursor.execute(buscar_query)
    cliente = cursor.fetchall()
    print(cliente)
    connection.commit()





#acesso_banco()

#Referencia do update em banco de dados, simples - so o Nome baseado no CPF
#def update_nome_banco_dados(cliente):
#    cursor, connection = retorna_cursor_banco_de_dados()
#    update_query = "UPDATE cliente SET nome = '" + cliente['nome'] + "' WHERE cpf = '" + cliente['cpf'] + "';"
#    #print(update_query)
#    cursor.execute(update_query)
#    connection.commit()
#    print ("Update de cliente na base de dados com sucesso!")