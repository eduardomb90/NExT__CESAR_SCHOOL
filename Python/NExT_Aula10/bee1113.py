while True:
    entrada = input()
    x, y = map(int, entrada.split())
    if x == y:
        break
    elif x < y:
        print("Crescente")
    else:
        print("Decrescente")