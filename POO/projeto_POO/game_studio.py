from typing import List
from jogo import Jogo

class GameStudio:
    def __init__(self, nome:str, link:str):
        self.nome:str = nome
        self.link:str = link
        self.__lista_jogos: List[Jogo] = []
        self.__ativo: bool = False

    def set_ativo(self, value:bool) -> None:
        self.__ativo = value

    def adicionar_jogo(self, jogo: Jogo) -> None:
        if jogo:
            self.__lista_jogos.append(jogo)

    def remover_jogo(self, jogo: Jogo) -> None:
        if jogo:
            self.__lista_jogos.remove(jogo)

    def mostrar_jogos(self) -> List[Jogo]:
        for jogo in self.__lista_jogos:
            print(f'Nome do jogo: {jogo} - Ativo: {self.__ativo}')