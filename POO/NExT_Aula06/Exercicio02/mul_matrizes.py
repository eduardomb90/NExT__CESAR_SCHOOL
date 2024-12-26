class Matriz:
    def __init__(self, valores):
        if len(valores) != 2 or any(len(linha) != 2 for linha in valores):
            raise ValueError('A matriz deve ser 2x2.')

        self.__matriz = valores

    def get_matriz(self):
        return self.__matriz

    def __mul__(self, outro):
        matriz_mult = [[0, 0], [0,0]]

        matriz_mult[0][0] = (self.__matriz[0][0] * outro.get_matriz()[0][0]) + (self.__matriz[0][1] * outro.get_matriz()[1][0])
        matriz_mult[0][1] =(self.__matriz[0][0] * outro.get_matriz()[0][1]) + (self.__matriz[0][1] * outro.get_matriz()[1][1])
        matriz_mult[1][0] =(self.__matriz[1][0] * outro.get_matriz()[0][0]) + (self.__matriz[1][1] * outro.get_matriz()[1][0])
        matriz_mult[1][1] =(self.__matriz[1][0] * outro.get_matriz()[0][1]) + (self.__matriz[1][1] * outro.get_matriz()[1][1])

        return Matriz(matriz_mult)

    def __str__(self):
        return f'[{self.__matriz[0][0]} {self.__matriz[0][1]}]\n[{self.__matriz[1][0]} {self.__matriz[1][1]}]'

if __name__ == '__main__':
    matriz_a = Matriz([[1, 2],[3, -1]])
    matriz_b = Matriz([[1, -2],[2, 4]])

    matriz_c = matriz_a * matriz_b

    print(matriz_c)