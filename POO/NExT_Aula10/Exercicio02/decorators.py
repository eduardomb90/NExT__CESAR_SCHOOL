from functools import wraps
from datetime import datetime

def log_execucao(func):
    @wraps(func)
    def wrapper():
        resultado = func()

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        mensagem = f"[{timestamp}] A função {func.__name__} foi executada."

        with open(arquivo, "a", encoding="uft-8") as log:
            log.write(mensagem)

        return resultado
    return wrapper