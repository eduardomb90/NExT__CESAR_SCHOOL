while True: 
    m,n = map(int, input().split())
    
    if m <= 0 or n <= 0:
        break
    maior = m if m > n else n
    menor = m if m < n else n
    
    lista = list(range(menor, maior+1))
    
    print(*lista, f'Sum={sum(lista)}')

