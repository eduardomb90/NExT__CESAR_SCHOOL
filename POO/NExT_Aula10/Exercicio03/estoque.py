class Estoque:
    def __init__(self, produto: str, qtd: int) -> None:
        self.__produto_nome: str = produto
        if qtd >= 0:
            self.__quantidade: int = qtd
        else:
            raise ValueError(f"Quantidade de {self.__produto_nome} não pode ser negativa!")

    @property
    def quantidade(self):
        return self.__quantidade

    @quantidade.setter
    def quantidade(self, valor: int):
        if valor < 0:
            self.__quantidade = valor
        else:
            raise ValueError(f"Quantidade de {self.__produto_nome} não pode ser negativa!")

    def vender(self, qtd: int):
        if 0 < qtd <= self.__quantidade:
            self.__quantidade -= qtd
        else:
            raise ValueError(f"Quantidade de {self.__produto_nome} para venda inválida!")

    def repor(self, qtd: int):
        if qtd > 0:
            self.__quantidade += qtd
        else:
            raise ValueError(f"Quantidade de {self.__produto_nome} para reposição inválida!")