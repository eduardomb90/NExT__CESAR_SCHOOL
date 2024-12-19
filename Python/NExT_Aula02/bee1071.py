a = int(input())
b = int(input())
menor = 0
maior = 0

menor, maior = min(a, b), max(a, b)

soma_impares = sum(n for n in range(menor+1, maior) if n % 2 != 0)

print(soma_impares)