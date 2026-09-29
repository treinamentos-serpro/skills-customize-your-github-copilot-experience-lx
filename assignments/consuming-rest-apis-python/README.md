# 📘 Assignment: Consuming REST APIs with Python

## 🎯 Objective

Aprenda a consumir uma API REST usando apenas a biblioteca padrão do Python. Ao final, você terá um programa que faz uma requisição HTTP, interpreta dados JSON, filtra resultados e informa erros de conexão de forma clara.

## 📝 Tasks

### 🛠️ Fazer uma requisição HTTP

#### Descrição

Complete a função `fetch_todos` no arquivo inicial. Ela deve acessar o endpoint público `https://jsonplaceholder.typicode.com/todos`, ler a resposta e convertê-la de JSON para uma lista de dicionários Python.

#### Requisitos

O programa concluído deve:

- Usar `urllib.request` para fazer a requisição.
- Usar `json` para interpretar o corpo da resposta.
- Retornar uma lista de tarefas contendo os campos `userId`, `id`, `title` e `completed`.
- Executar sem instalar bibliotecas externas.


### 🛠️ Exibir um resumo dos dados

#### Descrição

Complete a função `print_summary` para apresentar informações úteis sobre as tarefas recebidas pela API.

#### Requisitos

O programa concluído deve:

- Mostrar a quantidade total de tarefas.
- Mostrar quantas tarefas estão concluídas e quantas estão pendentes.
- Mostrar o título das três primeiras tarefas da resposta.
- Usar um loop para percorrer os dados retornados, em vez de repetir código manualmente.


### 🛠️ Filtrar tarefas e tratar erros

#### Descrição

Complete a função `get_pending_tasks` e o bloco principal do programa. O usuário deve poder informar um `userId` e ver apenas as tarefas pendentes desse usuário.

#### Requisitos

O programa concluído deve:

- Filtrar tarefas pelo `userId` informado e pelo valor `completed == False`.
- Exibir uma mensagem adequada quando nenhum resultado for encontrado.
- Tratar erros HTTP e erros de conexão sem exibir um traceback para o usuário.
- Exibir o título e o identificador de cada tarefa filtrada.

Exemplo de saída:

```text
Total tasks: 200
Completed: <completed count>
Pending: <pending count>

Pending tasks for user 1:
- [1] delectus aut autem
- [3] fugiat veniam minus
```