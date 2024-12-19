from typing import List
from livro import Livro

class CarrinhoDeCompras:
    def __init__(self):
        self.__livros: List[Livro] = []

    def adicionar_livro(self, livro: Livro):
        ja_tem = False
        for item in self.__livros:
            if item.get_titulo == livro.get_titulo:
                ja_tem = True
        if ja_tem == False:
            self.__livros.append(livro)

    def remover_livro(self, livro: Livro):
        self.__livros.remove(livro)

    def calcular_total(self):
        valor_total = sum(livro.get_preco() for livro in self.__livros)
        return valor_total

    def exibir_itens(self):
        for livro in self.__livros:
            print(f'Livro: {livro.get_titulo()}')


if __name__ == '__main__':
    carrinho = CarrinhoDeCompras()
    livro1 = Livro('LOTR', 'Tolkien', 20)
    livro2 = Livro('Hobbit', 'Tolkien', 10)

    carrinho.adicionar_livro(livro1)
    carrinho.adicionar_livro(livro2)
    valor = carrinho.calcular_total()
    print(valor)

    carrinho.exibir_itens()
    carrinho.remover_livro(livro2)
    carrinho.exibir_itens()
    valor = carrinho.calcular_total()
    print(valor)
