lista = [[1, 2], [3, 1], [5, 0]]
lista_ordenada = sorted(lista, key=lambda x: x[1])
print(lista_ordenada)

def multiplicador(n):
    return lambda x, y: (x+y) * n

calculo_louco= multiplicador(2)
print(calculo_louco(5, 6))