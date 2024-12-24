from abc import ABC, abstractmethod

class Veiculo(ABC):
    @abstractmethod
    def deslocar(self):
        print('O veículo está se deslocando...')

class Carro(Veiculo):
    def deslocar(self):
        print('O carro está dirigindo na estrada...')

class Barco(Veiculo):
    def deslocar(self):
        print('O barco está navegando na água...')

class Aviao(Veiculo):
    def deslocar(self):
        print('O avião está voando no céu...')


if __name__ == '__main__':

    def deslocar_veiculo(veiculo: Veiculo):
        veiculo.deslocar()

    veiculos = [
        Carro(),
        Barco(),
        Aviao()
    ]

    for veiculo in veiculos:
        deslocar_veiculo(veiculo)