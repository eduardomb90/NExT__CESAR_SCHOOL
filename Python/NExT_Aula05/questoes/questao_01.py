
habitat = input()

with open('NExT_Aula05/questoes/arquivo.txt', 'r', encoding='utf8') as arquivo:
    linhas = arquivo.readlines()
    terrestres = [x for x in linhas if habitat in x]
    print(terrestres)