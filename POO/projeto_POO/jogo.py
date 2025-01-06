from entidade import Entidade

class Jogo(Entidade):
    def __init__(self, nome:str, sinopse:str, genero:str, plataforma:str, engine:str, status:str, ativo:bool) -> None:
        super().__init__(nome, ativo)
        self.sinopse = sinopse
        self.genero = genero
        self.plataforma = plataforma
        self.engine = engine
        self.status = status