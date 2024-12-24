from entidade import Entidade

class Personagem(Entidade):
    def __init__(self, nome:str, vida:int, forca:int):
        super().__init__(nome, vida, forca)

    def usar_habilidade_especial(self):
        dano = self.atacar() * 2
        print(f'{self._nome} usou sua habilidade especial causando {dano} de dano!')
        return dano