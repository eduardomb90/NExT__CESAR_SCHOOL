<img src="https://www.cesar.school/wp-content/uploads/2019/09/marca_cesar_school.png" alt="drawing" width="200"/>

# NExT 2024.2 **Lógica de Programação** com Python
## Aula 02 - Bônus

### Na aula de hoje:
- pack e unpack;
- Recursos especiais do `print()`;
- Compreensão de listas.

------------------

# Pack e Unpack

Pack e Unpack são funcionalidades úteis para trabalhar com coleções de dados em Python, como listas, _tuplas_ e _dicionários_. Eles permitem agrupar ou desagrupar valores de forma eficiente.

## 📥 1.1. Pack

O packing ocorre quando vários valores são agrupados em uma única variável. Isso geralmente é feito ao atribuir múltiplos valores a uma variável em forma de _tupla_.

Exemplo:

```python
# Packing
valores = 1, 2, 3, 4
print(valores)  # Saída: (1, 2, 3, 4)
```

## 📤 1.2. Unpack

O unpacking desagrupa os valores de uma coleção para variáveis individuais. A quantidade de variáveis precisa corresponder ao número de elementos na coleção.

Exemplo:

```python
# Unpacking
valores = (1, 2, 3, 4)
a, b, c, d = valores
print(a, b, c, d)  # Saída: 1 2 3 4
```

### Unpack com números variáveis de itens

Podemos usar `*` para capturar múltiplos valores em uma única variável durante o unpacking.

Exemplo:

```python
valores = [1, 2, 3, 4, 5]
a, *b, c = valores
print(a)  # Saída: 1
print(b)  # Saída: [2, 3, 4]
print(c)  # Saída: 5
```

Ainda é possível usar o `*` para _desempacotar_ uma lista dentro de um print:

```python
valores = [1, 2, 3, 4, 5]

print(*valores)
```

# 📺 2. Recursos Especiais da Função `print()`

A função `print()` em Python tem recursos que facilitam a exibição de dados, além do básico.

## 2.1. Parâmetro `sep`

O parâmetro sep define o separador entre os argumentos da função.

Exemplo:
```python
print('Python', 'é', 'fantástico', sep='-')
# Saída: Python-é-fantástico
```

## 2.2. Parâmetro `end`

O parâmetro `end` define o que será exibido ao final da linha, substituindo o padrão de quebra de linha (`\n`).

Exemplo:

```python
print("Primeira linha", end=" | ")
print("Segunda linha")
# Saída: Primeira linha | Segunda linha
```

# 🗜️ 3. Compreensão de Listas

Compreensão de listas é uma técnica poderosa e concisa para criar ou manipular listas em Python.

## 3.1. Sintaxe Básica

```python
[nova_lista for elemento in iterável if condição]
```

Exemplo:

```python
numeros = [1, 2, 3, 4, 5]
dobrados = [n * 2 for n in numeros]
print(dobrados)
```

## 3.2. Com Condição

Você pode adicionar uma condição para filtrar elementos.

Exemplo:

```python
numeros = [1, 2, 3, 4, 5]
impares = [n for n in numeros if n % 2 != 0]
print(impares)
```

# Exercícios

## Exercício 1 (`pack`, `unpack`, `print`):

Dada a lista a seguir, usando pack/unpacking, atribua o primeiro elemento a uma variável `primeiro`, o último elemento a uma variável `ultimo`, e os demais elementos a uma lista `meio`.

Exiba todos os elementos em prints separados. No print da lista `meio`, os elementos devem ser separados por ponto e vírgula `;`.

`nomes = ["Ana", "Bruno", "Carlos", "Daniela", "Eduardo", "Fernanda", "Gustavo"]`


## Exercício 2 (`compreensão de listas`):

Crie uma lista chamada `quadrados` que contenha os quadrados dos números de 1 a 10 utilizando compreensão de listas.

## Exercício 3 (`compreensão de listas`):

Dada a lista original de nomes do exercício 1, crie uma nova lista que contenha apenas os nomes com mais de 5 caracteres.

# 🐝 Beecrowd

- [1051 - Imposto de Renda](https://judge.beecrowd.com/pt/problems/view/1051)

    ![Tabela do Imposto de Renda](https://resources.beecrowd.com/gallery/images/problems/UOJ_1051_pt.png)

- [1045 - Tipos de Triângulos](https://judge.beecrowd.com/pt/problems/view/1045)
- [1071 - Soma de Impares Consecutivos I](https://judge.beecrowd.com/pt/problems/view/1071)
