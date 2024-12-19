# Crie um programa que receba um valor inteiro e avalie se ele é positivo ou negativo.
# Essa avaliação deve ocorrer dentro de uma função que retorna um valor booleano.

def positivo_negativo(numero):
    return "negativo" if numero < 0 else "positivo"

numero = int(input())
resultado = positivo_negativo(numero)
print(resultado)