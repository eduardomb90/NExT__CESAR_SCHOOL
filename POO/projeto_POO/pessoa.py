from entidade import Entidade

class Pessoa(Entidade):
    def __init__(self, nome:str, email:str, endereco:str, cargo:str, ativo:str) -> None:
        super().__init__(nome, ativo)
        self.email:str = email
        self.endereco:str = endereco
        self.cargo:str = cargo
        self.__habilidades: list[str] = []
    
    def adicionar_habilidade(self, habilidade:str) -> None:
        
        if not self.habilidade_existe(habilidade):
            self.__habilidades.append(habilidade)
    
    def habilidade_existe(self, nome:str) -> bool:
        existe: bool = False
        for hab in self.__habilidades:
            if hab == nome:
                existe = True
        return existe
    
    def listar_habilidades(self) -> list[str]:
        return self.__habilidades
    
    def __str__(self) -> str:
        return f'Nome: {self.nome} Habilidades: '