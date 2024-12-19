def soma_impares(vezes):
    for _ in range(vezes):
        x_y = input().split()
        intervalo = [int(n) for n in x_y]
        x = min(intervalo)
        y = max(intervalo)

        impares = [n for n in range(x+1, y) if n % 2 != 0]
        print(sum(impares))

repete = int(input())
soma_impares(repete)