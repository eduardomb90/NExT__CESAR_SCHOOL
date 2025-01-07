import socket

def verificar_conexao() -> bool:
    """Verifica se há conexão com a internet.

    Tenta criar uma conexão com o servidor DNS público do Google (8.8.8.8).

    Retorna:
        bool: True se houver conexão, False caso contrário.
    """
    try:
        # Testa a conexão com o servidor DNS público na porta 53
        socket.create_connection(("8.8.8.8", 53), timeout=5)
        return True
    except OSError:
        return False

if not verificar_conexao():
    raise ConnectionError("Sem conexão com a internet. Verifique sua conexão e tente novamente.")