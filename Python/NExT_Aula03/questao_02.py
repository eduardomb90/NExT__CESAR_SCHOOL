#Crie um programa que tenha uma função que receba uma lista de números inteiros 
# e exiba todos os valores multiplicados por um valor inserido pelo usuário.

def multiplicador(lista, multiplicador):
    resultado = [x * multiplicador for x in lista]
    print(*resultado)

lista = [7, 8, 9, 10]

numero_multiplicador = int(input())

multiplicador(lista, numero_multiplicador)