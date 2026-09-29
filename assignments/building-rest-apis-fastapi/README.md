# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Aprenda a construir uma API REST com FastAPI, organizando endpoints, validando dados com modelos Pydantic e retornando respostas HTTP apropriadas. Ao final, você terá uma API de tarefas executada localmente e documentada automaticamente pelo framework.

## 📝 Tasks

### 🛠️ Criar o primeiro endpoint

#### Descrição

Use o arquivo inicial para executar uma aplicação FastAPI e implemente um endpoint que permita consultar todas as tarefas armazenadas em memória.

#### Requisitos

O programa concluído deve:

- Iniciar com `uvicorn starter-code:app --reload`.
- Responder a `GET /tasks` com status `200`.
- Retornar uma lista JSON contendo as tarefas iniciais.
- Exibir a documentação interativa em `/docs`.


### 🛠️ Validar dados de uma nova tarefa

#### Descrição

Crie um modelo Pydantic para representar uma tarefa e use-o no endpoint `POST /tasks`. A API deve aceitar apenas dados válidos e gerar um identificador para cada nova tarefa.

#### Requisitos

O programa concluído deve:

- Exigir um título não vazio com no máximo 100 caracteres.
- Aceitar uma descrição opcional e um campo `completed` booleano.
- Retornar status `201` ao criar uma tarefa válida.
- Retornar status `422` quando o corpo da requisição não atender ao modelo.
- Retornar a tarefa criada em formato JSON, incluindo seu identificador.

Exemplo de requisição:

```json
{
  "title": "Estudar FastAPI",
  "description": "Praticar modelos Pydantic",
  "completed": false
}
```


### 🛠️ Implementar operações CRUD

#### Descrição

Complete a API para que clientes possam buscar uma tarefa específica, atualizá-la e removê-la. Use os códigos de status HTTP adequados para indicar sucesso ou ausência de um recurso.

#### Requisitos

O programa concluído deve:

- Implementar `GET /tasks/{task_id}` e retornar `404` se o identificador não existir.
- Implementar `PUT /tasks/{task_id}` para substituir os dados de uma tarefa existente.
- Implementar `DELETE /tasks/{task_id}` e retornar `204` quando a remoção for concluída.
- Manter os dados das tarefas entre requisições enquanto o servidor estiver em execução.
- Permitir testar todos os endpoints pela interface `/docs` ou por um cliente HTTP.