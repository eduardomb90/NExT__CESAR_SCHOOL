class Veiculo:
    def __init__(self, marca: str, modelo: str):
        self.marca = marca
        self.modelo = modelo

    def movimentar(self):
        print('Veículo em movimento!')

class VeiculoSemMotor(Veiculo):
    def __init__(self, marca: str, modelo: str, tipo_propulsao: str):
        super().__init__(marca, modelo)
        self.tipo_propulsao = tipo_propulsao

    def movimentar(self):
        print('Queimando calorias...')
        return super().movimentar()

class VeiculoComMotor(Veiculo):
    def __init__(self, marca: str, modelo: str, combustivel: str):
        super().__init__(marca, modelo)
        self.combustivel = combustivel

    def movimentar(self):
        print('Queimando combustível...')
        return super().movimentar()

class Carro(VeiculoComMotor):
    def __init__(self, marca: str, modelo: str, combustivel: str, quantidade_portas: int):
        super().__init__(marca, modelo, combustivel)
        self.quantidade_portas = quantidade_portas

    def detalhes(self):
        print("Detalhes do Carro:")
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Combustível: {self.combustivel}")
        print(f"Quantidade de portas: {self.quantidade_portas}")

if __name__ == '__main__':
    mustang87 = Carro('Ford', 'Mustang 87', 'Gasolina', 2)
    mustang87.detalhes()
    mustang87.movimentar()


    bicicleta = VeiculoSemMotor("Caloi", "Elite Carbon", "pedal")
    bicicleta.movimentar()