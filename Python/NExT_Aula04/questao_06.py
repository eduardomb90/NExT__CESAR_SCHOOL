from functools import reduce

numeros = [1, 2, 3, 4]

soma_quadrado = reduce(lambda x, y: x + y , map(lambda x: x**2, numeros))

print(soma_quadrado)