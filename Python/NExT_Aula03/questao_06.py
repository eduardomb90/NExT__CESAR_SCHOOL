# Crie um programa que tenha uma função que receba uma lista de números inteiros e exiba todos os seus valores em ordem invertida.
# Obs.: Sem usar `invert` ou o fatiador com passo `-1`.

lista = [5, 7, 1, 6, 8, 2, 9, 3, 4, 10, 21]

def inverte_lista(l):
    tam = len(l)
    tam_met = int(tam/2)

    for i in range(tam_met):
        i_r = tam - (1 + i)
        
        aux = l[i]
        l[i] = l[i_r]
        l[i_r] = aux

    print(l)
    
inverte_lista(lista)