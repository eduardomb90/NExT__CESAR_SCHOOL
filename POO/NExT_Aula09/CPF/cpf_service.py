from cpf_invalido_error import CpfInvalidoError

class CpfService:
    def __init__(self, cpf:str) -> None:
        self.__cpf: str = cpf.replace(".","").replace("-","")
        self.__primeiro_digito: int = None
        self.__segundo_digito: int = None

        if len(self.__cpf) != 11:
            raise CpfInvalidoError("CPF deve conter exatamente 11 dígitos numéricos.")

    def valida_cpf(self) -> bool:

        #Primeiro dígito
        soma_primeiro_digito:int = 0
        for i in range(9):
            multiplicador = (10 - i)
            soma_primeiro_digito += int(self.__cpf[i]) * multiplicador

        resto = (soma_primeiro_digito * 10) % 11

        if resto > 9:
            self.__primeiro_digito = 0
        else:
            self.__primeiro_digito = resto

        if self.__primeiro_digito != int(self.__cpf[9]):
            raise CpfInvalidoError(f'CPF informado é inválido! (d1)')

        # Segundo dígito
        soma_segundo_digito:int = 0
        for i in range(10):
            multiplicador = (11 - i)
            soma_segundo_digito += int(self.__cpf[i]) * multiplicador

        resto = (soma_segundo_digito * 10) % 11

        if resto > 9:
            self.__segundo_digito = 0
        else:
            self.__segundo_digito = resto

        if self.__segundo_digito != int(self.__cpf[10]):
            raise CpfInvalidoError(f'CPF informado é inválido! (d2)')

        return True

    def __str__(self) -> str:
        return f"{self.__cpf[:3]}.{self.__cpf[3:6]}.{self.__cpf[6:9]}-{self.__cpf[9:]}"

if __name__ == '__main__':
    try:
        cpf = CpfService("08969625470")
        valido = cpf.valida_cpf()

        if valido:
            print(f"{cpf} é um CPF válido!")

        cpf = CpfService("09542126492")
        valido = cpf.valida_cpf()

        if valido:
            print(f"{cpf} é um CPF válido!")

    except CpfInvalidoError as err:
        print(f'Erro ao validar CPF: {err}')