class Coordenada:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def __add__(self, outro):
        return Coordenada(self.__x + outro.get_x(), self.__y + outro.get_y())

    def __str__(self):
        return f'({self.__x}, {self.__y})'



if __name__ == '__main__':
    c1 = Coordenada(2, 3)
    c2 = Coordenada(4, 5)

    c3 = c1 + c2

    print(c3)