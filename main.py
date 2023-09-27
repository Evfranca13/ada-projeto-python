from cliente import menucliente
from utils import limpaterminal

def menuinicial():
    print("\nSeja bem vindo(a) ao sistema de gerenciamento de carteira de ações da Nuclea. Selecione uma das opções abaixo:"
    "\n1 - Cliente"
    "\n2 - Ordem"
    "\n3 - Realizar análise da carteira"
    "\n4 - Imprimir relatório da carteira"
    "\n5 - Sair")
    opcao_menu_inicial = int(input("Digite a opção desejada: "))
    limpaterminal()
    return opcao_menu_inicial

# Início do código/execucao geral
validador_menu = True
while validador_menu == True:
    valor = menuinicial()
    if valor == 1:
        menucliente()
    elif valor == 2:
        pass
    elif valor == 3:
        pass
    elif valor == 4:
        pass
    elif valor == 5:
        print("Saindo do sistema...")
        validador_menu = False

# nome = "Daniel"
# print(nome)
# print(nome[2])

# nome = "Maria"
# sexo = "F"
# idade = 35
# altura = 1.6
# print(f"Nome:  {nome:20} Sexo: {sexo}")
# print(f"Idade: {idade!s:20} Altura: {altura:.3f}")