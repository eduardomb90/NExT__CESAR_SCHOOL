from estoque import Estoque

try:
    celular = Estoque('celular', 10)
    #fone = Estoque('fone', -1)
    
    celular.vender(2)
    print(celular.quantidade)
    
    #celular.repor(-1)
    celular.repor(4)
    print(celular.quantidade)
except ValueError as err:
    print(f'Erro: {err}')