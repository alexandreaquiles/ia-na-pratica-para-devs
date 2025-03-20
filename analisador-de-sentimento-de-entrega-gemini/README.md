# analisador-de-sentimento-de-entrega-gemini

## Requisitos

- python 3 e pip 3 instalados
- uma API Key da Gemini: https://aistudio.google.com/apikey
- um arquivo `.env` com a propriedade `GEMINI_API_KEY`com sua API Key

## Como executar

Crie um Virtual Environment para o projeto:

```
python3 -m venv env-analisador-sentimentos
```

Ative o Virtual Environment criado:

```
source env-analisador-sentimentos/bin/activate
```

Instale as bibliotecas utilizadas:

```
pip3 install -r requirements.txt
```

Execute o código do analisador de sentimentos:

```
python3 analisador_sentimentos_entregas.py
```

Os resultados da análise serão arquivos JSON criados no diretório `analises-reviews`.

Execute o código do gerador de emails:

```
python3 gerador_emails_entregas.py
```

Os emails gerados serão arquivos .txt criados no diretório `emails-reviews`.

Opcionalmente, execute o código do enviador de emails:

```
python3 python3 enviador_emails_entregas.py
```
