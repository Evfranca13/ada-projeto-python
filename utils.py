from validate_docbr import CPF
import re
from datetime import datetime
import requests
import urllib3

def valida_padrao_cpf(cpf_input):
    while True:
        padrao_cpf = r'^\d{3}\.\d{3}\.\d{3}-\d{2}$'
        cpf_input = re.sub('[-.]','', cpf_input)
        cpf_input = f'{cpf_input[:3]}.{cpf_input[3:6]}.{cpf_input[6:9]}-{cpf_input[9:]}'
        #print (cpf_input)
        if re.match(padrao_cpf,cpf_input):
            return(cpf_input)
        else:
            cpf_input = input("\nCPF inválido. Por favor digite um CPF válido no formato XXX.XXX.XXX-XX: ")

def valida_cpf(cpf_input):
    cpf_valido = False
    cpf_original = cpf_input
    cpf_input = re.sub('[-.]', '',cpf_input)
    #resultado = cpf.validate(cpf_input)
    while cpf_valido == False:
        cpf = CPF()
        cpf_valido = cpf.validate(cpf_input)
        if cpf_valido == True:
            return (cpf_original)
        else:
            cpf_input = input("\nCPF inválido. Por favor digite um CPF válido no formato XXX.XXX.XXX-XX: ")

def valida_rg(rg_input):
    #RG - exemplo: 11.111.111.-x
    padrao_rg = r'^\d{2}\.\d{3}\.\d{3}-[0-9A-Za-z]$'
    while True:
        rg_input = re.sub('[-.]','', rg_input)
        rg_input = f'{rg_input[:2]}.{rg_input[2:5]}.{rg_input[5:8]}-{rg_input[8:]}'
        if re.match(padrao_rg,rg_input):
            return rg_input
        else:
            rg_input = input("RG Inválido. Digite novamente em formato XX.XXX.XXX-X: ")

def valida_nascimento():
    while True:
        data_nascimento_input = input("Digite a data de nascimento:  ")
        try:
            data_convertida = datetime.strptime(data_nascimento_input, '%d/%m/%Y').date()
            data_atual = datetime.now().date()
    
            # Verificacao se data pode ser aceita, inferior à data atual
            if data_convertida < data_atual:
                #return data_convertida.strftime("%d/%m/%Y")
                return data_convertida.strftime("%Y/%m/%d")
            else:
                print("Data inválida. Data deve ser anterior à data atual. ")
        except ValueError as e:
            print("Formato de data inválido. Você recebeu o erro: ", e, " Tente novamente.")

def valida_cep(cep_input):
    urllib3.disable_warnings()
    while True:
        url = f'https://viacep.com.br/ws/{cep_input}/json/'
        response = requests.get(url, verify=False)
        #print(url)
        #print(response)

        if response.status_code == 200:
            data = response.json()

            endereco = {
                "CEP": data['cep'],
                "Logradouro": data['logradouro'],
                "Bairro": data['bairro'],
                "Cidade": data['localidade'],
                "Estado": data['uf']
            }
            return endereco
        else:
            cep_input = input("Erro ao verificar CEP. Digite novamente: ")

def limpaterminal():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')


#print(response['cep'])
#print(response['bairro'])

# https://pypi.org/project/validate-docbr/
# need to find how to import and use this on code

# https://requests.readthedocs.io/en/latest/
# https://pypi.org/project/requests/

# pip install pyodbc
# https://pypi.org/project/pyodbc/