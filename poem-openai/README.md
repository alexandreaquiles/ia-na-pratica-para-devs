# poem-openai

## Requisitos

- python 3 e pip 3 instalados
- uma API Key da Open AI: https://platform.openai.com/settings/organization/api-keys
- um arquivo `.env` com a propriedade `OPENAI_API_KEY`com sua API Key

## Como executar

Crie um Virtual Environment para o projeto:

```
python3 -m venv env-poem-openai
```


Ative o Virtual Environment criado:

```
source env-poem-openai/bin/activate
```

Instale as bibliotecas utilizadas:

```
pip3 install -r requirements.txt
```

Execute o código:

```
python3 main.py
```

O poema deve ser impresso no Terminal e o arquivo `poem.mp3` conterá o áudio gerado.