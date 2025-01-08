from functools import wraps
import time

# Decorator que mede o tempo de execução de uma função
def medidor(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        inicio = time.time()

        for i in range(5):
            resultado = func(*args, **kwargs)

        fim = time.time()
        tempo_total = fim - inicio
        print(f"A função '{func.__name__}' levou {tempo_total:.4f} segundos para executar.")
        return resultado
    return wrapper

#    Se a função tem parâmetros, o decorator precisa aceitar *args e **kwargs :
# para repassar os argumentos para a função decorada

# Decorator para logar a execução de uma função
def logar_execução(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Executando a função '{func.__name__}' com os argumentos: {args} {kwargs}")
        resultado = func(*args, **kwargs)
        print(f"Função '{func.__name__}' finalizada")
        return resultado
    return wrapper


# Decorator para ajudar a entender *args e **kwargs
def meu_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Chamando a função '{func.__name__}' com os argumentos {args} e {kwargs}")
        resultado = func(*args, **kwargs)
        print("Função executada com sucesso.")
        return resultado
    return wrapper