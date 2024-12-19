x = int(input())

for _ in range(x):
    entrada = input().strip()
    palavras = entrada.split()
    codigo = "".join([palavra[0] for palavra in palavras])
    print(codigo)