# API

A API foi desenhada para gerir usuários, imagens e apps do Grupo Gimi.

## ✔️ Tecnologias usadas
- Python
- Django
- Django Ninja
- Pydantic
- PostgreSQL
- Python Jose
- Vercel

## 📁 Acesso ao deploy

[![Deploy with Vercel](https://vercel.com/button)](https://engenhadev.com.br/)

## 🔨 Funcionalidades

- **Gestão de Usuários**: Administração de usuários que podem acessar a API.
- **Autenticação**: Sistema de tokens para acesso seguro à API.

## 📌 Uso

A API segue os princípios REST para comunicação. Os seguintes endpoints estão disponíveis:

### /users
- Gerenciar usuários e realizar operações CRUD.

## 🔐 Autenticação

A autenticação é realizada através de JWT. Utilize a rota `/auth/login` para obter um token de acesso, enviando as credenciais do usuário. Utilize este token nas requisições subsequentes para autenticar e para ter acesso aos dados do usuário e dos carros autenticado utilize a rota `/auth/me`.

## 🛠️ Abrindo e rodando o projeto

Para configurar a API em seu ambiente, siga estas etapas:

1. Clone o repositório do projeto para sua máquina local.
2. Configure o ambiente virtual para Python e ative-o.
3. Instale as dependências do projeto
```bash
pip install -r requirements.txt
```
1. Configure as variáveis de ambiente necessárias para a conexão com o banco de dados e outras configurações de sistema.
2. Execute as migrações do banco de dados
```bash
python manage.py migrate
```
1. Crie um super usuário para ter acesso a `/admin/`
```bash
python manage.py createsuperuser
```
1. Inicie o servidor de desenvolvimento
```bash
python manage.py runserver
```

## Acessando a rota cars

Esta rota permite que você visualize uma lista de carros, consulte um carro específico e adicione um novo carro.

- [Rotas](#rotas-da-api)
  - [GET /cars](#get-cars)
  - [GET /car/{id}](#get-carid)
  - [POST /cars](#post-cars)

---


### GET /cars

- **Descrição**: Retorna uma lista de todos os carros.
- **Método HTTP**: `GET`
- **URL**: `/cars`
- **Cabeçalho de Autorização**:
  ```bash
  Authorization: Bearer seu_token_de_acesso
- **Resposta de Sucesso**:
  - **Código**: `200 OK`
  - **Corpo**:
    ```bash
    [
        {
            "id": "57f3d83f-7c44-48d9-ab4f-4b21deace614",
            "name": "Celta",
            "year": 2020,
            "description": "Red Chevrolet Celta",
            "sold": false,
            "created": "2024-11-07T14:23:35.652Z"
        },
        {
            "id": "7f0f146f-abdd-4be4-9c1a-2d8ef2696d12",
            "name": "Corolla",
            "year": 2024,
            "description": "Silver Toyota Corolla",
            "sold": false,
            "created": "2024-11-08T03:09:14.346Z"
        }
    ]
    ```
- **Resposta de Erro**:
  - **Código**: `403 Forbidden`
  - **Mensagem**:
    ```bash
    {
     "erro": "Acesso não autorizado. Esta rota é protegida."
    }

    ```
---

### GET /car/{id}

- **Descrição**: Retorna os dados de um carro específico.
- **Método HTTP**: `GET`
- **URL**: `/car/{id}`
- **Cabeçalho de Autorização**:
  ```bash
  Authorization: Bearer seu_token_de_acesso
- **Parâmetros**:
  - **id**: ID do carro a ser retornado.
- **Resposta de Sucesso**:
  - **Código**: `200 OK`
  - **Corpo**:
    ```bash
    {
        "id": "57f3d83f-7c44-48d9-ab4f-4b21deace614",
        "name": "Celta",
        "year": 2020,
        "description": "Red Chevrolet Celta",
        "sold": false,
        "created": "2024-11-07T14:23:35.652Z"
    }
    ```
- **Respostas de Erro**:
  - **Código**: `404 Not Found`
  - **Mensagem**:
    ```bash
    {
      "erro": "Carro não encontrado"
    }
    ```
  - **Código**: `403 Forbidden`
  - **Mensagem**:
    ```bash
    {
     "erro": "Acesso não autorizado. Esta rota é protegida."
    }

    ```
---

### POST /cars

- **Descrição**: Cria um novo carro e retorna os dados do carro criado.
- **Método HTTP**: `POST`
- **URL**: `/cars`
- **Cabeçalho de Autorização**:
  ```bash
  Authorization: Bearer seu_token_de_acesso
- **Corpo da Requisição**:
  - **Exemplo**:
    ```bash
    {
		"name": "Celta",
		"year": 2024,
		"description": "Black Chevrolet Celta",
		"sold": false,
		"user_id": "17b4cf13-deaa-4c62-9cf8-6da0405d7ef5"
	}
    ```
- **Resposta de Sucesso**:
  - **Código**: `200 OK`
  - **Corpo**:
    ```bash
    {
        "id": "08e280bc-d1f8-4431-a9d7-0a2623fd9f05",
        "name": "Teste 2",
        "year": 2024,
        "description": "a new posted car",
        "sold": false,
        "created": "2024-11-08T21:06:03.590Z"
    }
    ```
- **Resposta de Erro**:
  - **Código**: `422 Unprocessable Content`
  - **Mensagem**:
    ```bash
    {
        "detail": [
            {
                "type": "missing",
                "loc": [
                    "body",
                    "payload",
                    "user_id" -> missing field
                ],
                "msg": "Field required"
            }
        ]
    }
    ```
  - **Código**: `403 Forbidden`
  - **Mensagem**:
    ```bash
    {
     "erro": "Acesso não autorizado. Esta rota é protegida."
    }

    ```
