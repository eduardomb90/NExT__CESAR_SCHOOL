class Livro:
    def __init__(self, titulo: str, autor: str, preco: float):
        self.__titulo = titulo
        self.__autor = autor
        self.set_preco(preco)

    def set_preco(self, valor: float):
        if valor > 0:
            self.__preco = valor

    def get_titulo(self):
        return self.__titulo

    def get_preco(self):
        return self.__preco