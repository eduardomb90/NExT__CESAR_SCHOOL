with open('NExT_Aula05/desafio_02/dados_elecao.txt', 'r', encoding='utf8') as arquivo:
    dados = arquivo.readlines()

#12864552,Marsh,Khan

total_votos = len(dados[1:])

dados_separados = [x.split(',') for x in dados[1:]]

dados_set = {x[2].strip() for x in dados_separados}

dados_dic = {key: 0 for key in dados_set}

for dado in dados_set:
    for voto in dados_separados:
        if voto[2].strip() == dado:
            dados_dic[dado] += 1

for key in dados_dic:
    dados_dic[key] = (dados_dic[key]/total_votos) * 100
    print(f'{key}: {dados_dic[key]:.1f}%')

vencedor = 0
for key in dados_dic:
    if dados_dic[key] > vencedor:
        vencedor = dados_dic[key]
        vencedor_string = key

print(vencedor_string)



# 7000 = x/100 * 100000 --> 7000 * 100 = x * 1000000 --> (7000*100)/1000000