from utils import *
from banco_dados import *

def menucliente():
    #lista_cliente  = []
    validador_menu = True

    while validador_menu == True:
        print("\nMenu Cliente"
        "\n1 - Cadastrar Cliente"
        "\n2 - Alterar Cliente"
        "\n3 - Buscar Cliente"
        "\n4 - Deletar Cliente"
        "\n5 - Listar Clientes"
        "\n6 - Voltar ao menu anterior")
        opcao = int(input("Digite a opção desejada: "))
        limpaterminal()
        #print ("\n" * 100)

        if opcao == 1:
            #Cadastrar cliente
            cliente_dicionario = { 
            "nome": input("Digite o nome do cliente: "),
            #"CPF": input("Digite o CPF do cliente: "),
            "cpf": valida_cpf(input("Digite o CPF do cliente: ")),
            "rg": valida_rg(input("Digite o RG do cliente: ")),
            "nascimento": valida_nascimento(),
            "cep": valida_cep(input("Digite o CEP do cliente: ")),
            "complemento" : input("Digite o complemento do endereco: "),
            "numero" : input("Digite o numero da residência do cliente: ")
            }
            #lista_cliente.append(cliente_dicionario)
            #print (lista_cliente)
            insert_banco_dados(cliente_dicionario)

        elif opcao == 2:
            #Alterar cliente
            cliente_dicionario = {
                #"cpf": input("Digite o CPF a ser procurado: "),
                "cpf": valida_padrao_cpf(input("Digite o CPF do cliente a ser alterado: ")),
                "nome": input("Digite o o novo nome: "),
                "rg": valida_rg(input("Digite o novo RG do cliente: ")),
                "nascimento": valida_nascimento(),
                "cep": valida_cep(input("Digite o novo CEP do cliente: ")),
                "complemento" : input("Digite o novo complemento do endereco: "),
                "numero" : input("Digite o novo numero da residência do cliente: ")
            }
            update_nome_banco_dados(cliente_dicionario)

        elif opcao == 3:
            #Buscar cliente
            cliente_dicionario = {
                "cpf": valida_padrao_cpf(input("Digite o CPF do cliente a ser buscado: "))
            }
            buscar_nome_banco_dados(cliente_dicionario)

        elif opcao == 4:
            #Deletar clientes
            cliente_dicionario = {
                "cpf": valida_padrao_cpf(input("Digite o CPF do cliente a ser buscado: "))
            }
            delete_banco_dados(cliente_dicionario)

        elif opcao == 5:
            #Listar clientes
            select_banco_dados()
            
        elif opcao == 6:
            validador_menu = False
    
    return
    


    #Nome, CPF, RG, Data de Nascimento, CEP, Número residência.

 #           Deletar cliente original
 #           elif opcao == 4:
 #           #Deletar clientes
 #           cliente_dicionario = {
 #           #"nome": input("Digite o nome a ser apagado: "),
 #           "cpf": input("Digite o CPF do cliente a ser apagado: ")
 #           }
 #           delete_banco_dados(cliente_dicionario)