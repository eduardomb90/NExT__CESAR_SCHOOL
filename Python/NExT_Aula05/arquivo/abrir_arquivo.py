arquivo = open('NExT_Aula05/arquivo/arquivo.txt', 'r+', encoding='utf8')

for linha in arquivo:
    print(linha.strip())

# arquivo.write('adicionado pelo código\n')
# print(arquivo.read())

# arquivo.seek(9)

# print(arquivo.readline())
# print(arquivo.readline())

arquivo.close()

with open('NExT_Aula05/arquivo/arquivo.txt', 'a', encoding='utf8') as arquivo:
  while True:
      texto = input()
      if texto == 'encerrar':
          break
      arquivo.write(f'{texto}\n')

print(arquivo.read)
print('Programa Finalizado!')