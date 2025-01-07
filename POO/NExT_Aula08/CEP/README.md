# 🗺️ CepService – Serviço de Busca de Endereços

O **CepService** é um utilitário simples e eficiente para buscar endereços com base no CEP, utilizando a API gratuita do [ViaCEP](https://viacep.com.br/).

---

## 🚀 Funcionalidades

- 🏙️ **Busca de endereços**: Consulta dados como logradouro, bairro, cidade e estado, com base no CEP fornecido.
- ✅ **Validação de CEP**: Verifica automaticamente se o CEP contém apenas 8 dígitos numéricos.
- 🚨 **Tratamento de erros**: Informa o usuário caso o CEP seja inválido ou a API esteja inacessível.

---

## 📋 Estrutura do Projeto

```plaintext
projeto_endereco/
│
├── cep/
│   ├── __init__.py       # Verificação de conexão com a internet
│   └── cep_service.py    # Serviço de busca de endereços
└── README.md             # Documentação do projeto

## 📦 Dependências
Este projeto utiliza o módulo requests para fazer as requisições HTTP.

Instalação do módulo:
Certifique-se de que o Python está instalado. No terminal, execute:

```bash
pip install requests
```

Verificação da instalação:
```bash
python -c "import requests; print(requests.__version__)"
```

## 💡 Como Usar
1. Execute o script cep_service.py no terminal:

```bash
python cep_service.py
```

2. Insira um CEP válido com 8 dígitos quando solicitado.

3. O programa exibirá os dados do endereço associado ao CEP.

Exemplo de Execução:

1. CEP Válido:
```bash
🗺️ Bem-vindo ao CepService!
Digite o CEP (8 dígitos, ou 'sair' para encerrar): 01001000
Endereço encontrado: {'cep': '01001-000', 'logradouro': 'Praça da Sé', 'bairro': 'Sé', 'localidade': 'São Paulo', 'uf': 'SP'}

Digite o CEP (8 dígitos, ou 'sair' para encerrar): 87654321
CEP inválido: 87654321

Digite o CEP (8 dígitos, ou 'sair' para encerrar): sair
Encerrando o programa. Obrigado por usar o CepService!
```

2. CEP Inválido:
```bash
🗺️ Bem-vindo ao CepService!
Digite o CEP (8 dígitos, ou 'sair' para encerrar): 87654321
Erro: CEP inválido ou não encontrado: 87654321
```

3. Erro de Conexão:
```bash
🗺️ Bem-vindo ao CepService!
Digite o CEP (8 dígitos, ou 'sair' para encerrar): 01001000
Erro de conexão: Erro ao buscar o CEP 01001000: <detalhes do erro>
```

## 🛠️ Tecnologias
- Python 3.x
- Requests: Para comunicação HTTP com a API do ViaCEP.

## 📝 Observações
- Certifique-se de estar conectado à internet ao utilizar o programa.
- Apenas CEPs válidos com 8 dígitos são aceitos.
- Em caso de CEP inválido, o programa exibirá a mensagem:
```bash
CEP inválido: 87654321
```