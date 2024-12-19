import math

numeros = list(range(2, 20))

eh_primo = lambda n: n > 1 and all(n % i != 0 for i in range(2, int(math.sqrt(n)) + 1))

primos = list(filter(eh_primo, numeros))

print(primos)