import requests

class CepService:
    """
    Serviço de busca de endereços utilizando a API do ViaCEP.

    Métodos:
        - buscar_endereco: Busca os dados do endereço com base no CEP fornecido.
        - verificar_cep: Valida o formato do CEP (8 dígitos numéricos).
    """

    def buscar_endereco(self, cep:str) -> dict:
        """
        Faz a busca do endereço utilizando a API do ViaCEP.

        Parâmetros:
        - cep (str): CEP no formato de 8 dígitos numéricos.

        Retorna:
        - dict: Um dicionário com os dados do endereço, ou vazio em caso de erro.
        """

        if not self.verificar_cep(cep):
            raise ValueError("O CEP informado é inválido. Deve conter exatamente 8 dígitos numéricos.")

        api:str = f'https://viacep.com.br/ws/{cep}/json/'

        try:
            # Faz a requisição para a API do ViaCEP
            response = requests.get(api)
            #response.raise_for_status() # Verifica se houve erro na requisição
            
            # Verifica se o status_code é diferente de 200
            if response.status_code != 200:
                raise ConnectionError(f"Erro ao se conectar à API. Código de status: {response.status_code}")
            
            dados = response.json()

            # Verifica se o CEP foi encontrado na API
            if 'erro' in dados:
                raise ValueError(f"CEP inválido ou não encontrado: {cep}")

            return dados

        except requests.RequestException as e:
            # Trata possíveis erros na comunicação com a API
            raise ConnectionError(f"Erro ao buscar o CEP {cep}: {e}")

    def verificar_cep(self, cep:str) -> bool:
        """Verifica se um CEP contém apenas números e tem 8 dígitos.

        Parâmetros:
        cep (str): CEP a ser verificado.

        Retorna:
        bool: True se o CEP for válido, False caso contrário.
        """
        return len(cep) == 8 and cep.isdigit()



if __name__ == '__main__':
    """
    Bloco principal do programa para testes manuais do serviço de CEP.

    Exemplo:
        Digite um CEP válido ou inválido e veja o retorno da API.
    """
    print("🗺️ Bem-vindo ao CepService!")
    cep_service = CepService()

    while True:
        cep = input("Digite o CEP (8 dígitos, ou 'sair' para encerrar): ").strip()

        if cep.lower() == 'sair':
            print("Encerrando o programa. Obrigado por usar o CepService!")
            break

        try:
            endereco = cep_service.buscar_endereco(cep)
            print(f"Endereço encontrado: {endereco}")
        except ValueError as ve:
            print(f"Erro: {ve}")
        except ConnectionError as ce:
            print(f"Erro de conexão: {ce}")