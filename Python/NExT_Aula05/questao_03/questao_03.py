'''notas = []

for i in range(4):
    print('Insira a nota: ', end="")
    nota = input()
    notas.append(f'{nota}\n')'''

# Solicita as notas, grava, lê e processa de forma mais concisa
notas = [float(input(f'Insira a nota {i+1}: ')) for i in range(4)]

with open('NExT_Aula05/questao_03/arquivo_questao_03.txt', 'w', encoding='utf8') as arquivo:
    arquivo.writelines(f'{nota}\n' for nota in notas)

with open('NExT_Aula05/questao_03/arquivo_questao_03.txt', 'r', encoding='utf8') as arquivo:
    notas = [float(linha) for linha in arquivo]


menor, maior, media = min(notas), max(notas), sum(notas) / len(notas)

print(f'Menor nota: {menor}\nMaior nota: {maior}\nMédia das notas: {media:.2f}')