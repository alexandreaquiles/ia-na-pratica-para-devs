from openai import OpenAI
import openai
from dotenv import load_dotenv
from pathlib import Path
import os

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

response = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[
    {
      "role": "system",
      "content": [
        {
          "type": "text",
          "text":"""Você é um poeta escreve versos livres em português brasileiro.
                    Você irá receber diversos temas do usuário e deverá escrever um poema em que cada verso aborda um dos temas.
                    Você tem um tom engraçado e sarcástico."""
        }
      ]
    },
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": """Gere um poema sobre os seguintes temas:
            - Goiás
            - Jantinha
            - Cerrado
            - Família"""
        }
      ]
    }
  ],
  temperature=1,
  max_tokens=1800,
  response_format={
    "type": "text"
  }
)

poem = response.choices[0].message.content
print(poem)

