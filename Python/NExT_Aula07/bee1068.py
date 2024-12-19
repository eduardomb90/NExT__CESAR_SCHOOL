def valida_parenteses(expressao):
    pilha = []

    for char in expressao:
        if char == '(':
            pilha.append(char)
        elif char == ')':
            if len(pilha) == 0:
                return False
            pilha.pop()

    # Se a pilha estiver vazia, todos os parênteses foram balanceados
    return len(pilha) == 0

while True:
    try:
        expressao = input()

        if valida_parenteses(expressao):
            print('correct')
        else:
            print('incorrect')

    except EOFError:
        break