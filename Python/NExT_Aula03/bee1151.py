def fibonacci(n):
    anterior = 0
    atual = 1
    soma = 0
    resultado = []
    
    for i in range(n):
            resultado.append(str(anterior))
            soma = anterior + atual
            anterior = atual
            atual = soma
    print(" ".join(resultado))

entrada = int(input())
fibonacci(entrada)