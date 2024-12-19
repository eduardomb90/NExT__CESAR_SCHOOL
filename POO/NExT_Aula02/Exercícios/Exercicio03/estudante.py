class Estudante:
    def __init__(self, nome, nota1, nota2):
        self._nome = nome
        self._nota1 = float(nota1)
        self._nota2 = float(nota2)

    def media(self):
        self._media = (self._nota1 + self._nota2)/2
        print(f'Média do aluno: {self._media:.2f}')

    def situacao(self):
        self.media()
        if self._media >= 7.0:
            self._situacao = 'Aprovado'
        else:
            self._situacao = 'Reprovado'

        print(f'Aluno - {self._situacao}')


eduardo = Estudante("Eduardo", 9, 8)
raquel = Estudante("Raquel", 9.5, 9)

eduardo.situacao()
raquel.situacao()