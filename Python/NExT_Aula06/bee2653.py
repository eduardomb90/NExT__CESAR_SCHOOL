joias = set()

def verificar_joia(joia):
    for c in joia:
        if c not in {'(',')'}:
            return False
    return True

while True:
    try:
        entrada = input()
        if verificar_joia(entrada):
            joias.add(entrada)
    except EOFError:
        break

print(len(joias))