from functools import reduce

palavras = ["sol", "montanha", "mar", "universo"]

maior_palavra = reduce(lambda x, y: x if len(x) > len(y) else y, palavras)

print(f"A palavra mais longa é: {maior_palavra}")