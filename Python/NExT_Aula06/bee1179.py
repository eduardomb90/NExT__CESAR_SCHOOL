pares = []
impares = []

def add_par(n):
    if len(pares) < 5:
        pares.append(n)
    else:
        imprimir_vetor(pares)
        pares.clear()
        pares.append(n)

def add_impar(n):
    if len(impares) < 5:
        impares.append(n)
    else:
        imprimir_vetor(impares)
        impares.clear()
        impares.append(n)

def imprimir_vetor(vetor):
    r = len(vetor)
    if vetor[0] % 2 == 0:
        for i in range(r):
            print(f'par[{i}] = {pares[i]}')
    else:
        for i in range(r):
            print(f'impar[{i}] = {impares[i]}')



for _ in range(15):
    valor = int(input())
    if valor % 2 == 0:
        add_par(valor)
    else:
        add_impar(valor)

if len(impares) > 0:
    imprimir_vetor(impares)

if len(pares) > 0:
    imprimir_vetor(pares)