from functools import reduce

with open('NExT_Aula05/desafio_01/dados_financeiros.txt', 'r', encoding='utf8') as arquivo:
    dados = arquivo.readlines()

dados_financeiros = list(map(lambda x: x.strip().split(','), dados[1:]))

total_meses = len(dados_financeiros)

meses = [x[0] for x in dados_financeiros]
lucro_perda = [int(x[1]) for x in dados_financeiros]

'''# a função no reduce recebe dois parâmetros, o primeiro é o acumulador, e o segunto é cada sublista da lista.
# o acumulador começa em zero.
total_lucro = reduce(lambda acumulador, x: acumulador + x[1], lucro_perda, 0)'''
#outra forma de fazer
total_lucro = sum(x for x in lucro_perda)

media = total_lucro/total_meses

mudanca = []
for i in range(1, total_meses):
    j = i-1
    variacao = lucro_perda[i] - lucro_perda[j]
    mudanca.append(variacao)


media_mudanca = float(sum(mudanca))/len(mudanca)

mes_aumento_max = ''
aumento_max = 0
for i in range(len(mudanca)):
    if aumento_max < int(mudanca[i]):
        aumento_max = int(mudanca[i])
        mes_aumento_max = meses[i+1]


mes_reducao_max = ''
reducao_max = 0
for i in range(len(mudanca)):
    if reducao_max > int(mudanca[i]):
        reducao_max = int(mudanca[i])
        mes_reducao_max = meses[i+1]

print('Analise financeira')
print('--------------------------------------')
print(f'Total de meses: {total_meses}')
print(f'Total: $ {total_lucro}')
print(f'Média: $ {media:.2f}')
print(f'Variação da média: $ {media_mudanca:.2f}')
print(f'Maior aumento nos lucros: {mes_aumento_max} ($ {aumento_max})')
print(f'Maior redução nos lucros: {mes_reducao_max} ($ {reducao_max})')