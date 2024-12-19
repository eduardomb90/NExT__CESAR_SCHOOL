class Funcionario:
    def __init__(self, cod, nome, salario):
        self.__cod = cod
        self.__nome = nome
        self.set_salario(salario)
        self.__historico_aumento = []
    
    def set_salario(self, valor):
        if valor > 0:
            self.__salario = float(valor)
    
    def aumentar_salario(self, percentual):
        if percentual > 0:
            self.__salario = self.__salario * (1 + (percentual/100))
            self.__historico_aumento.append(f'Aumento de {percentual}% - Salário autal: {self.__salario:.2f}')
    
    def exibir_informacoes(self):
        print(f'Código do funcionário: {self.__cod}')
        print(f'Nome: {self.__nome}')
        print(f'Salário atual: {self.__salario}')
        
        print('Histório de aumentos salariais:')
        for item in self.__historico_aumento:
            print(item)


func_eduardo = Funcionario('130291', 'Eduardo Marques', 5000)
func_eduardo.aumentar_salario(20)
func_eduardo.aumentar_salario(10)
func_eduardo.exibir_informacoes()