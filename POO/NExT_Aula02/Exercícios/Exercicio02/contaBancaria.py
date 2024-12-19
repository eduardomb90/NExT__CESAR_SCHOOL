class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = str(titular)
        self._saldo = 0.0
        self.set_saldo(saldo)

    def set_saldo(self, valor):
        if not isinstance(valor, (int, float)):
            raise ValueError("O saldo deve ser um valor numérico.")
        if valor < 0:
            raise ValueError("O valor não pode ser negativo.")
        self._saldo = float(valor)

    def depositar(self, valor):
        if not isinstance(valor, (int, float)):
            raise ValueError("O saldo deve ser um valor numérico.")
        if valor < 0:
            raise ValueError("O valor não pode ser negativo.")
        self._saldo += valor
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")


    def sacar(self, valor):
        if not isinstance(valor, (int, float)):
            raise ValueError("O saldo deve ser um valor numérico.")
        if valor <= 0:
            raise ValueError("Valor inválido para saque.")
        if valor > self._saldo:
            print("Você não tem saldo suficiente para realizar esta ação.")
        self._saldo -= valor
        print(f"Saque de R$ {valor:.2f} realizado com sucesso!")


    def imprimir_saldo(self):
        print(f'Saldo atual: {self._saldo:.2f}')



conta_edu = ContaBancaria("Eduardo", 10000)
conta_edu.imprimir_saldo()
conta_edu.depositar(5000)
conta_edu.imprimir_saldo()
conta_edu.sacar(1000)
conta_edu.imprimir_saldo()
