from abc import ABC

class Entidade(ABC):
    def __init__(self, nome:str, ativo:bool) -> None:
        self.nome:str = nome
        self._ativo:str = ativo

    def set_ativo(self, value:bool) -> None:
        self._ativo = value

    def is_ativo(self) -> bool:
        return self._ativo