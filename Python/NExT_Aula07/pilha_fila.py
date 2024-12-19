pilha = []

# Adicionando elementos à pilha
pilha.append(1)
pilha.append(2)
pilha.append(3)

print("Pilha depois de adicionar elementos:", pilha)  # Saída: [1, 2, 3]

# Removendo elementos da pilha
elemento = pilha.pop()
print("Elemento removido:", elemento)  # Saída: 3
print("Pilha depois de remover um elemento:", pilha)  # Saída: [1, 2]

#-----------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------



fila = []

# Adicionando elementos à fila
fila.append(1)
fila.append(2)
fila.append(3)

print("Fila depois de adicionar elementos:", fila)  # Saída: [1, 2, 3]

# Removendo elementos da fila
elemento = fila.pop(0)
print("Elemento removido:", elemento)  # Saída: 1
print("Fila depois de remover um elemento:", fila)  # Saída: [2, 3]



#-----------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------
'''OUTRA FORMA DE USAR FILA'''

from collections import deque

fila = deque()

# Adicionando elementos à fila
fila.append(1)
fila.append(2)
fila.append(3)

print("Fila depois de adicionar elementos:", fila)  # Saída: deque([1, 2, 3])

# Removendo elementos da fila
elemento = fila.popleft()
print("Elemento removido:", elemento)  # Saída: 1
print("Fila depois de remover um elemento:", fila)  # Saída: deque([2, 3])


'''
Resumo

Pilha:
Use uma lista e os métodos append() para adicionar e pop() para remover.

Fila:
Use uma lista e os métodos append() para adicionar e pop(0) para remover (pouco eficiente).

Para maior eficiência, use deque da biblioteca collections e os métodos append() e popleft().

'''