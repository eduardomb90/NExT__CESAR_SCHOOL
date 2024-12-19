
def ler_entrada():
    lista_entrada = list(map(int, input().split()))
    print(lista_entrada)
    return lista_entrada

lista = ler_entrada()

def ordernar_reverso(lista):
    lista_invertida = lista[::-1]
    print(lista_invertida)

ordernar_reverso(lista)
    