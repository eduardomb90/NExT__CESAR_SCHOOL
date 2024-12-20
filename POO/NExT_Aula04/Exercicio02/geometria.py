import math
from abc import ABC, abstractmethod

class FormaGeometrica(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def calcular_area(self) -> float:
        #precisa implementar na classe filha
        pass

    @abstractmethod
    def calcular_perimetro(self) -> float:
        #precisa implementar na classe filha
        pass

class Retangulo(FormaGeometrica):
    def __init__(self, largura: float, altura: float):
        self.__largura = largura
        self.__altura = altura

    def calcular_area(self) -> float:
        return self.__largura * self.__altura

    def calcular_perimetro(self) -> float:
        return 2 * (self.__largura + self.__altura)

    def __str__(self) -> str:
        return f"Retângulo (Largura: {self.__largura}, Altura: {self.__altura})"


class Circulo(FormaGeometrica):
    def __init__(self, raio):
        self.__raio = raio

    def calcular_area(self):
        return math.pi * (self.__raio ** 2)

    def calcular_perimetro(self):
        return 2 * math.pi * self.__raio

    def __str__(self) -> str:
        return f"Círculo (Raio: {self.__raio})"


if __name__ == "__main__":

    formas = [
        Retangulo(5, 3),
        Retangulo(10, 7),
        Circulo(4),
        Circulo(10),
    ]

    # Iteração para calcular área e perímetro
    for forma in formas:
        print(forma)  # Chama o método __str__
        print(f"Área: {forma.calcular_area():.2f}")
        print(f"Perímetro: {forma.calcular_perimetro():.2f}")
        print("-" * 30)
