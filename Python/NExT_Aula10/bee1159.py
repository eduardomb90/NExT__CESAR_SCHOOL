while True:
    x = int(input())
    
    if x == 0:
        break
    
    lista_pares = []
    
    contador = 0
    while contador < 5:
        if x % 2 == 0:
            lista_pares.append(x)
            contador += 1
        x += 1
    
    print(sum(lista_pares))