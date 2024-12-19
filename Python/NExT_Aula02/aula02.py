#n1 = int(input())
#n2 = int(input())
n1, n2 = 10, 15

print(n1+n2, '🦙'*5)



numeros = [1, 2, 3, 4, 5]
# melhor forma de ler
# impares recebe n para cada n em numeros se n for par
impares = [n for n in numeros if n % 2 != 0]
print(impares)