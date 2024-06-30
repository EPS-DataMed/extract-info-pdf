
# Processador de Regex em PDF

[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=EPS-DataMed_extract-info-pdf&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=EPS-DataMed_extract-info-pdf) [![Coverage](https://sonarcloud.io/api/project_badges/measure?project=EPS-DataMed_extract-info-pdf&metric=coverage)](https://sonarcloud.io/summary/new_code?id=EPS-DataMed_extract-info-pdf) [![Lines of Code](https://sonarcloud.io/api/project_badges/measure?project=EPS-DataMed_extract-info-pdf&metric=ncloc)](https://sonarcloud.io/summary/new_code?id=EPS-DataMed_extract-info-pdf)

Este projeto é uma aplicação web baseada no FastAPI que processa arquivos PDF para encontrar padrões especificados pelo usuário usando expressões regulares. Ele lê o conteúdo do PDF, aplica os padrões de regex fornecidos e retorna as correspondências encontradas no documento.

## Instalação

1. **Crie um ambiente virtual:**

    ```bash
    python3 -m venv myenv
    ```

2. **Ative o ambiente virtual:**

    - No Windows:
        ```bash
        myenv\Scripts\activate
        ```
    - No macOS/Linux:
        ```bash
        source myenv/bin/activate
        ```

3. **Instale as dependências:**

    ```bash
    pip3 install -r requirements.txt
    ```

## Executando o Servidor

Salve o seguinte código em um arquivo chamado `main.py`:

Inicie o servidor:

```bash
python3 main.py
```

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
    curl -X POST "http://127.0.0.1:8000/process/pdf/regex"     -H "accept: application/json"     -H "Content-Type: multipart/form-data"     -F "file=@/path/to/your/file.pdf"     -F 'patterns={"patterns":{"hemoglobin":["HEMOGLOBINA\s*([\d,\.]+)\s*g/dL","g/dL"],"hematócrit":["HEMATÓCRITO\s*([\d,\.]+)\s*%","%"],"red_blood_cells":["HEMÁCIAS\s*([\d,\.]+)\s*milhões/mm3","milhões/mm3"]}}'
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

Este projeto está licenciado sob os termos da licença MIT.
