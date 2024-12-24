class Entidade:
    def __init__(self, nome:str, vida:int, forca:int):
        self.__nome = nome
        self.__vida = vida
        self._forca = forca
        self._defesa = False

    def atacar(self) -> int:
        print(f'{self.__nome} ataca causando {self._forca} de dano!')
        return self._forca

    def defender(self) -> int:
        print(f'{self.__nome} está se defendendo!')
        self._defesa = True

    def receber_dano(self, dano:int) -> None:
        if(self._defesa):
            self.__vida -= dano/2
            print(f'{self.__nome} está se defendendo! Dano recebido foi diminuído pela metade.')
        else:
            self.__vida -= dano

        print(f'{self.__nome} agora tem {self.__vida} de vida.')
        self._defesa = False

    def get_vida(self) -> int:
        return self.__vida

    def get_nome(self) -> str:
        return self.__nome