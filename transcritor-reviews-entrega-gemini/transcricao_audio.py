import os

import pandas as pd
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv('GEMINI_API_KEY'))

generation_config = {
  "temperature": 0,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-2.0-flash",
  generation_config=generation_config
)

reviews = pd.read_csv('reviews-entrega-MercadoAgil-audio.csv')
for index, review in reviews.iterrows():
  reviewer_id = review['reviewer_id']
  reviewer_email = review['reviewer_email']
  review_audio = review['review_audio']

  print(f'Processando áudio do review {reviewer_id} de {reviewer_email}...')

  arquivo_audio = genai.upload_file(path=f'audio/{review_audio}')

  prompt = 'Transcreva detalhadamente o arquivo de áudio em anexo.'

  response = model.generate_content([prompt, arquivo_audio])

  os.makedirs("transcricoes-audio", exist_ok=True)

  with open(f"transcricoes-audio/{reviewer_id}.txt", "w", encoding="utf-8") as arquivo:
    print(f'Salvando transcrição do áudio do review {reviewer_id} de {reviewer_email}...')
    arquivo.write(response.text)