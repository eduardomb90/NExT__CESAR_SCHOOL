x = int(input())

contador = 1
for _ in range(x+1):
    if contador % 2 == 0:
        print(f'{contador}^2 =', contador**2)
    contador += 1