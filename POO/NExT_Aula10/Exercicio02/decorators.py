from functools import wraps
from datetime import datetime

def log_execucao(func):
    @wraps(func)
    def wrapper():
        resultado = func()

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        mensagem = f"[{timestamp}] A função {func.__name__} foi executada."

        with open('NExT_Aula10/Exercicio02/log.txt', "a", encoding='utf-8') as log:
            log.write(mensagem)

        return resultado
    return wrapper