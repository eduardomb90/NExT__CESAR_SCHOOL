linhas = []

with open('NExT_Aula05/questoes/arquivo.txt', 'r', encoding='utf8') as arquivo:
    linhas = arquivo.readlines()

terrestre = [linha for linha in linhas if 'terrestre' in linha]

with open('NExT_Aula05/questoes/arquivo_questao_02.txt', 'w', encoding='utf8') as arquivo:
    arquivo.writelines(terrestre)