# transcritor-revies-entrega-gemini

## Requisitos

- python 3 e pip 3 instalados
- uma API Key da Gemini: https://aistudio.google.com/apikey
- um arquivo `.env` com a propriedade `GEMINI_API_KEY`com sua API Key

## Como executar

Crie um Virtual Environment para o projeto:

```
python3 -m venv env-transcritor-reviews
```

Ative o Virtual Environment criado:

```
source env-transcritor-reviews/bin/activate
```

Instale as bibliotecas utilizadas:

```
pip3 install -r requirements.txt
```

Execute o código do transcritor de imagens:

```
python3 transcritor_image.py
```

Os resultados da transcrição serão arquivos .text criados no diretório `transcricoes-imagem`.

Execute o código do transcritor de áudio:

```
python3 transcritor_audio.py
```

Os resultados da transcrição serão arquivos .text criados no diretório `transcricoes-audio`.