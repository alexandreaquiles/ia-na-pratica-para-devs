import os
import json

import pandas as pd
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

reviews = pd.read_csv("reviews-entrega-MercadoAgil.csv")
reviews = reviews[["reviewer_id", "reviewer_name", "reviewer_email", "review_text"]]

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

generation_config = {
  "temperature": 0,
  "response_mime_type": "application/json",
}

model = genai.GenerativeModel(
  model_name="gemini-2.0-flash",
  generation_config=generation_config,
  system_instruction="""
Você é um analisador de sentimentos de uma empresa de entrega.
Você deve analisar o sentimento das avaliações de clientes apenas em relação à entrega e não à outros aspectos.
A sua análise deve responder para cada avaliação dos clientes: 
  "negativo", "neutro" ou "positivo".
Dê uma nota para o sentimento de cada avaliação dos clientes, onde: 
  -5 é totalmente negativo, 0 é neutro, para avaliações inconclusivas quanto à entrega, 5 é totalmente positivo.

O formato da resposta deve ser um JSON como a seguir:

```json
[
  {
  "reviewer_id": <id aqui>,
  "reviewer_name": <nome aqui>,
  "reviewer_email": <email aqui>
  "sentimento": "<sentimento aqui>"
  "nota": "<nota aqui>"
 }
]
```
"""
)

prompt_usuario = f"""
Analise o sentimento das avaliações do CSV a seguir:

```csv
{reviews.to_csv()}
```
"""

response = model.generate_content(prompt_usuario)
conteudo = response.text

os.makedirs("analises-reviews", exist_ok=True)

json_resultado = json.loads(conteudo)
for avaliacao in json_resultado:
  with open(f"analises-reviews/{avaliacao['reviewer_id']}.json", "w", encoding="utf-8") as arquivo:
    arquivo.write(json.dumps(avaliacao))