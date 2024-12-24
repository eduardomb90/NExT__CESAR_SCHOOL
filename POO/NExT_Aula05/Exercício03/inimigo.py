import random
from entidade import Entidade

class Inimigo(Entidade):
    def __init__(self, nome:str, vida:int, forca:int):
        super().__init__(nome, vida, forca)

    def agir(self) -> int:
        acao = random.randint(1, 2)
        return acao
