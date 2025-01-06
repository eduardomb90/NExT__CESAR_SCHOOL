# NExT 2024.2 | POO

![CESAR School](/cesar_school.png)

## Aula 08 - Documentação

### Na aula de hoje

- Boas Práticas de Documentação
- API de CEP

------------------

## Por que Documentar?

Documentação é uma parte essencial do desenvolvimento de software. Um código bem documentado facilita a manutenção, colaboração e o entendimento do projeto por outros desenvolvedores (e até por você mesmo no futuro).

Vantagens de uma boa documentação:

- Facilita a colaboração em equipe;
- Reduz o tempo de manutenção;
- Acelera o aprendizado de novos membros no time;
- Evita mal-entendidos sobre o funcionamento do código.

### Tipos de Documentação

#### 1. Comentários em Código

Comentários devem ser curtos e claros, explicando trechos complexos ou justificando decisões técnicas.

```python
# Calcula o imposto sobre o valor final
valor_final = preco * 1.1  # Imposto de 10%
```

⚠️ Evite comentários óbvios como:

```python
x = x + 1  # Soma 1 a x
```

#### 2. Docstrings (Documentação de Funções, Classes e Módulos)

As docstrings são blocos de texto que explicam o propósito de uma função, classe ou módulo. Elas são inseridas logo abaixo da definição com três aspas `"""`.

Exemplo:

```python
def calcular_media(valores: list[int]) -> float:
    """Calcula a média de uma lista de números inteiros.

    Parâmetros:
        valores (list[int]): Lista de valores inteiros.

    Retorna:
        float: Média aritmética dos valores.
    """
    return sum(valores) / len(valores)
```

Boas práticas:

- Descreva o que a função faz de forma objetiva e concisa;
- Liste os parâmetros com seus tipos;
- Indique o valor de retorno e seu tipo.

#### 3. README (Documentação do Projeto)

O arquivo `README.md` serve como uma introdução ao projeto.
Ele deve conter:

- Descrição do projeto;
- Como instalar e executar;
- Exemplo de uso;
- Contribuições futuras.

💡 Geralmente usamos Markdown para escrever o `README.md`.

### Documentação em Projetos POO

Na **Programação Orientada a Objetos** (POO), a documentação desempenha um papel essencial na explicação de classes, métodos e interações entre objetos. Um código bem documentado ajuda a manter a clareza do projeto e facilita a colaboração entre desenvolvedores.

#### O que documentar

- **Módulo**: Apresentar o módulo e sua estrutura base;
- **Classe**: Explicar o propósito da classe e como instanciá-la;
- **Métodos públicos**: Documentar parâmetros, tipos de retorno e o objetivo do método.

#### Exemplo do arquivo `pessoa.py`

```python
"""Módulo Pessoa do Sistemas de Cadastro"""


class Pessoa:
    """Representa uma pessoa no sistema.

    Atributos:
        nome (str): Nome completo da pessoa.
        idade (int): Idade da pessoa.

    Métodos:
        saudacao(): Retorna uma saudação com o nome da pessoa.
    """

    def __init__(self, nome: str, idade: int) -> None:
        """Inicializa uma nova instância da classe Pessoa.

        Parâmetros:
            nome (str): O nome da pessoa.
            idade (int): A idade da pessoa.
        """
        self.nome = nome
        self.idade = idade

    def saudacao(self) -> str:
        """Retorna uma saudação personalizada com o nome da pessoa.

        Retorna:
            str: Mensagem de saudação.
        """
        return f"Olá, meu nome é {self.nome}."
```

### Ferramentas para Documentação Automática

- **[pydoc](https://docs.python.org/pt-br/3/library/pydoc.html)**: Ferramenta nativa do Python para gerar automaticamente a documentação dos módulos. A documentação pode ser apresentada no console ou salva em arquivos HTML.
    `python -m pydoc -w modulo.exemplo`
- **[Write the Docs](https://www.writethedocs.org)**: Comunidade global de desenvolvedores especializados em escrita de documentação.
- **[Sphinx](www.sphinx-doc.org)**: Gera documentação em HTML, PDF, etc. a partir de docstrings.
- **[pdoc](https://pdoc.dev)**: Simples e direto, gera documentação a partir de docstrings.
- **[MkDocs](https://www.mkdocs.org)**: Ideal para documentar APIs.

### Inspirações de Repositórios Bem Documentados

1. [Django](https://github.com/django/django)

    - Uso de docstrings extensivas;
    - Documentação robusta disponível em vários formatos.

2. [FastAPI](https://github.com/fastapi/fastapi)

    - Documentação clara, com muitos exemplos de uso;
    - README bem estruturado.

3. [Flask](https://github.com/pallets/flask)

    - Código simples e fácil de entender;
    - Documentação rica e bem segmentada.

4. [Pandas](https://github.com/pandas-dev/pandas)

    - Docstrings extensas, explicando o propósito de cada método;
    - Documentação oficial muito detalhada.

## 📮 Endereço com CEP

## Objetivo

Implementar uma classe `CEP` que utiliza a API gratuita do **ViaCEP** para buscar informações a partir de um **CEP** fornecido pelo usuário. A classe deve ser bem documentada com **docstrings** explicando cada método e atributo.

### 1. Estrutura do Projeto

```text
projeto_endereco/
│
├── cep/
│   ├── __init__.py
│   └── cep.py
│
└── README.md
```

### 2. Implementação da Classe `CEP` (_cep.py_)

O Endereço deve ser todo baseado no número do CEP. Dados como logradouro, bairro, cidade e estado devem ser preenchidos automaticamente.

Esta será uma classe genérica, detalhes como número ou complemento não vão ser implementados nela.

Usaremos a API [ViaCEP](https://viacep.com.br) para coletar os dados necessários.

### 3. Módulo `requests`

O módulo [`requests`](https://requests.readthedocs.io) é uma das ferramentas mais populares em Python para fazer requisições **HTTP**. Com ela, você pode se comunicar com APIs, baixar dados da web e enviar informações para servidores de maneira simples e intuitiva.

#### Exemplo de uso

```python
import requests

response = requests.get("https://api.github.com")

# Exibindo o conteúdo da resposta
print(response.text)
```

#### Como instalar

O módulo `requests` pode ser instalado facilmente usando o gerenciador de pacotes `pip`.

1. Certifique-se de que o Python está instalado em sua máquina.
2. No terminal ou prompt de comando, execute:

    ```bash
    pip install requests
    ```

3. Verifique a instalação executando:

    ```bash
    python -c "import requests; print(requests.__version__)"
    ```

    Se a versão for exibida corretamente, a instalação foi bem-sucedida.

#### O Que é `status_code`?

Quando você faz uma requisição HTTP com `requests`, o servidor responde com um código de status (`status_code`) que indica o resultado da operação. Esses códigos seguem os padrões da internet e possuem categorias bem definidas.

##### Categorias de Status Codes

|Categoria| Faixa de Códigos | Significado |
| ------- | ---------------- | ----------- |
|   1xx   |      100-199     | Informações |
|   2xx   |      200-299     | Sucesso (ex.: 200 = OK) |
|   3xx   |      300-399     | Redirecionamento |
|   4xx   |      400-499     | Erros do Cliente (ex.: 404 = Não Encontrado) |
|   5xx   |      500-599     | Erros do Servidor |

##### Exemplo de Uso

```python
import requests

response = requests.get("https://api.github.com")

# Verificando o código de status
print(response.status_code)

if response.status_code == 200:
    print("Requisição bem-sucedida!")
elif response.status_code == 404:
    print("Recurso não encontrado!")
else:
    print(f"Erro: {response.status_code}")
```

### 3. Implementação do `__init__.py`

No futuro, vamos verificar se o programa consegue se conectar à internet. Caso contrário, podemos interromper a execução ou informar para o usuário.

### 4. `README.md` – Documentação do Projeto

No `README.md` vamos apresentar o projeto, listar suas dependências (`request`) e explicar como usar.

## 🧱 Exercícios Fundamentais

1. Documente os módulos, classes e métodos do projeto FORJA Contatos (`Jogo`, `Pessoa`, `GameStudio`);
2. Revise outros projetos do seu portifólio e adicione a documentação adequada neles.
