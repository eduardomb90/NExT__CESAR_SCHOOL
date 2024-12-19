sinais = ['@','&','!','*','#']

dic_sinais = {'@':'a','&':'e','!':'i','*':'o','#':'u'}

while True:
    try:
        mensagem_cript = input()
        mensagem_descript = ''

        for c in mensagem_cript:
            l = [x for x in sinais if c == x]
            if len(l) > 0:
                mensagem_descript += dic_sinais.get(l[0])
            else:
                mensagem_descript += c


        print(mensagem_descript)
    except EOFError:
        break

