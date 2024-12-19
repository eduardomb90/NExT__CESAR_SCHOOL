dic = {}

def endereco():
    cep = input('Informe o CEP: ')
    endereco = input('Informe o endereço: ')

    dic[cep] = endereco

def buscar_endereco():
    cep = input('Informe o CEP para busca: ')
    endereco = dic.get(cep, 'Endereço não encontrado')
    
    print(endereco)

endereco()
buscar_endereco()