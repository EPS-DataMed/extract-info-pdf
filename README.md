# Processador de Regex em PDF

[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=EPS-DataMed_extract-info-pdf&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=EPS-DataMed_extract-info-pdf)
[![Coverage](https://sonarcloud.io/api/project_badges/measure?project=EPS-DataMed_extract-info-pdf&metric=coverage)](https://sonarcloud.io/summary/new_code?id=EPS-DataMed_extract-info-pdf)
[![Lines of Code](https://sonarcloud.io/api/project_badges/measure?project=EPS-DataMed_extract-info-pdf&metric=ncloc)](https://sonarcloud.io/summary/new_code?id=EPS-DataMed_extract-info-pdf)

## Descrição do Projeto

Este projeto é uma aplicação web baseada no FastAPI que processa arquivos PDF para encontrar padrões especificados pelo usuário usando expressões regulares. Ele lê o conteúdo do PDF, aplica os padrões de regex fornecidos e retorna as correspondências encontradas no documento.


## Configuração do ambiente de desenvolvimento local

### Pré-requisitos

- Python 3.11 ou superior
- `venv` para gerenciamento de ambientes virtuais
- Dependências listadas em `requirements.txt`

Siga os passos abaixo para configurar o ambiente de desenvolvimento local:

1. **Clone o repositório**

   ```bash
   git clone <URL_DO_REPOSITORIO>
   cd terms
   ```

2. **Crie e ative um ambiente virtual**

   ```bash
   python -m venv venv
   source venv/bin/activate   # No Windows, use `venv\Scripts\activate`
   ```

3. **Instale as dependências**

   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt 
   ```

4. **Execute a aplicação**

   ```bash
   uvicorn app.main:app --host 0.0.0.0 --port 8006 --reload
   ```

   A aplicação estará disponível em `http://127.0.0.1:8006`.

### Testes

1. Para executar os testes, utilize o comando abaixo:

    ```bash
    pytest
    ```

## Configuração do ambiente de desenvolvimento com Docker

### Pré-requisitos

- Docker
- Docker Compose

1. **Construir a imagem Docker**
    ```bash
    docker-compose build
    ```

2. **Executar o container**
    ```bash
    docker-compose up
    ```

A aplicação estará disponível em `http://127.0.0.1:8006`.

## Uso

Você pode usar `curl` ou Postman para enviar uma requisição ao servidor.

### Exemplo usando `curl`

1. Crie um arquivo chamado `patterns.json` com o seguinte conteúdo:

    ```json
    {
        "patterns": {
            "hemoglobin": ["HEMOGLOBINA\s*([\d,\.]+)\s*g/dL", "g/dL"],
            "hematócrit": ["HEMATÓCRITO\s*([\d,\.]+)\s*%", "%"],
            "red_blood_cells": ["HEMÁCIAS\s*([\d,\.]+)\s*milhões/mm3", "milhões/mm3"]
        }
    }
    ```

2. Use `curl` para enviar a requisição:

    ```bash
    curl -X POST "http://127.0.0.1:8006/process/pdf/regex"     -H "accept: application/json"     -H "Content-Type: multipart/form-data"     -F "file=@/path/to/your/file.pdf"     -F 'patterns={"patterns":{"hemoglobin":["HEMOGLOBINA\s*([\d,\.]+)\s*g/dL","g/dL"],"hematócrit":["HEMATÓCRITO\s*([\d,\.]+)\s*%","%"],"red_blood_cells":["HEMÁCIAS\s*([\d,\.]+)\s*milhões/mm3","milhões/mm3"]}}'
    ```

### Exemplo usando Postman

1. Selecione o método POST.
2. Adicione o arquivo PDF na seção "Body" como `form-data` com o campo `file`.
3. Adicione os padrões na seção "Body" como `form-data` com o campo `patterns` e o conteúdo JSON diretamente na área de texto:

    ```json
    {
        "patterns": {
            "hemoglobin": ["HEMOGLOBINA\s*([\d,\.]+)\s*g/dL", "g/dL"],
            "hematócrit": ["HEMATÓCRITO\s*([\d,\.]+)\s*%", "%"],
            "red_blood_cells": ["HEMÁCIAS\s*([\d,\.]+)\s*milhões/mm3", "milhões/mm3"]
        }
    }
    ```

## Licença

Este projeto está licenciado sob a [MIT License](./LICENSE).