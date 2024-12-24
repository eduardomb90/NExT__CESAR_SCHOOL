from abc import ABC, abstractmethod

class Instrumento(ABC):
    @abstractmethod
    def tocar(self) -> None:
        print('Tocando um instrumento...')

class Violao(Instrumento):
    def tocar(self):
        print('Tocando violão...')

class Piano(Instrumento):
    def tocar(self):
        print('Tocando piano...')

class Bateria(Instrumento):
    def tocar(self):
        print('Tocando bateria...')

if __name__ == '__main__':

    def tocar_instrumento(instrumento: Instrumento):
        instrumento.tocar()

    instrumentos = [
        Violao(),
        Piano(),
        Bateria()
    ]

    for instrumento in instrumentos:
        #instrumento.tocar()
        #ou
        tocar_instrumento(instrumento)