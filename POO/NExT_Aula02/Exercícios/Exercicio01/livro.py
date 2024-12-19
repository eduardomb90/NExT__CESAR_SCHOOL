class Livro:
    def __init__(self, titulo, autor):
        self.titulo = str(titulo)
        self.autor = str(autor)
    
    def exibir_informacoes(self):
        print(f'Título: {self.titulo} - Autor: {self.autor}')
        
        
        
o_hobbit = Livro('The Hobbit', 'Tolkien')
o_hobbit.exibir_informacoes()