# Crie um programa que possua uma lista de nomes. Peça que o usuário insira um nome que será buscado nesta lista.
# A busca deve ser implementada em uma função que retorna os valores lógicos verdadeiro ou falso.

lista_nomes = ["Eduardo", "Raquel", "Neide", "Fernando", "Rejane"]

def busca_nome(buscar):
    resultado = False

    for nome in lista_nomes:
        if nome == buscar:
            return True

    return resultado



nome_para_busca = input()
resultado = busca_nome(nome_para_busca)
print(resultado)