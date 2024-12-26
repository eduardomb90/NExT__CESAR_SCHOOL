class Produto:
    def __init__(self, nome, preco):
        self.__nome = nome
        self.__preco = preco

    def get_nome(self):
        return self.__nome

    def get_preco(self):
        return self.__preco

    def __eq__(self, outro: object) -> bool:
        if not isinstance(outro, Produto):
            return False
        return self.__nome == outro.get_nome() and self.__preco == outro.get_preco()


    def __repr__(self):
        return f'Produto(nome={self.__nome}, preco={self.__preco})'

if __name__ == '__main__':
    p1 = Produto("Camiseta", 49.90)
    p2 = Produto("Camiseta", 49.90)
    p3 = Produto("Calça", 79.90)

    print(p1)  # Produto(nome='Camiseta', preco=49.9)
    print(p2)  # Produto(nome='Camiseta', preco=49.9)
    print(p3)  # Produto(nome='Calça', preco=79.9)

    print(p1 == p2)  # True
    print(p1 == p3)  # False