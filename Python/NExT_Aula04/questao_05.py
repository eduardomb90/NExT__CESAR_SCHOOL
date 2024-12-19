import re

texto = "Eu tenho 2 maçãs e 3 laranjas."

numeros = list(filter(lambda x: re.match(r'\d', x), texto))

print(numeros)
