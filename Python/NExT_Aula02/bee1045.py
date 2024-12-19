#Ler 3 valores a,b,c float
#ordernar em ordem decrescente
# a > b > c


# Lendo os valores de entrada e convertendo para float
entrada = input()
valores = [float(x) for x in entrada.split()]

# valores = list(map(float, input().split()))

# Ordenando em ordem decrescente
valores.sort(reverse=True)

# Atribuindo os valores ordenados
a, b, c = valores

# Verificando as condições para determinar o tipo de triângulo
if a >= b + c:
    print("NAO FORMA TRIANGULO")
else:
    # Verificando o tipo de ângulo do triângulo
    if a**2 == b**2 + c**2:
        print("TRIANGULO RETANGULO")
    elif a**2 > b**2 + c**2:
        print("TRIANGULO OBTUSANGULO")
    elif a**2 < b**2 + c**2:
        print("TRIANGULO ACUTANGULO")

    # Verificando os lados
    if a == b == c:
        print("TRIANGULO EQUILATERO")
    elif a == b or b == c or a == c:
        print("TRIANGULO ISOSCELES")




#TESTANDO MEUS ALGORITMOS DE COMPARAÇÃO

# maior = 0
# for i in range(len(valores)-1):
#     if valores[i] >= valores[i+1]:
#         maior = valores[i]
#     else:
#         maior = valores[i+1]

# print(maior)

# maior_2 = 0
# for i in range(len(valores)):
#     for j in range(i+1, len(valores)):
#         if valores[i] >= valores[j]:
#             maior_2 = valores[i]
#         else:
#             maior_2 = valores[j]

# print(maior_2)