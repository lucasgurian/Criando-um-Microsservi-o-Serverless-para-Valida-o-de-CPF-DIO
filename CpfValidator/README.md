# Microsserviço de Validação de CPF - Azure Functions

Este é um microsserviço serverless para validação de números de CPF (Cadastro de Pessoas Físicas) do Brasil, construído para rodar na plataforma Azure Functions.

## Visão Geral

A função HTTP pode ser acionada através de requisições `GET` ou `POST`. Ela espera um CPF e retorna se ele é válido ou não.

## Como Usar

### Endpoint

`https://<seu-function-app-name>.azurewebsites.net/api/CpfValidator`

### Métodos HTTP

* GET
* POST

### Parâmetros

* **Query String (GET):**
    `?cpf=12345678909`
* **Corpo da Requisição (POST - JSON):**
    ```json
    {
      "cpf": "123.456.789-09"
    }
    ```

### Respostas

#### Sucesso (CPF Válido)

* **Código:** `200 OK`
* **Corpo:**
    ```json
    {
      "cpf": "12345678909",
      "isValid": true,
      "message": "CPF válido."
    }
    ```

#### Erro (CPF Inválido)

* **Código:** `400 Bad Request`
* **Corpo:**
    ```json
    {
      "cpf": "12345678900",
      "isValid": false,
      "message": "CPF inválido."
    }
    ```

#### Erro (CPF não fornecido)

* **Código:** `400 Bad Request`
* **Corpo:**
    ```json
    {
      "error": "Por favor, forneça um CPF no corpo da requisição (JSON) ou como um parâmetro de consulta (query string)."
    }
    ```

## Implantação

Este projeto está configurado para implantação contínua (CI/CD) utilizando GitHub Actions. Qualquer push para a branch `main` irá acionar o workflow de build e implantação para o Azure Function App configurado.

### Pré-requisitos para a Implantação

1.  Um Function App criado no Azure.
2.  O perfil de publicação do Function App configurado como um segredo (`AZURE_FUNCTIONAPP_PUBLISH_PROFILE`) no repositório do GitHub.

---
