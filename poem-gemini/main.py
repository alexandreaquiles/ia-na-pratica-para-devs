from google import genai
from google.genai import types

from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

generation_config = types.GenerateContentConfig(
    max_output_tokens=1800,
    temperature=1,
    response_mime_type = "text/plain",
    system_instruction = """Você é um poeta escreve versos livres em português brasileiro.
                    Você irá receber diversos temas do usuário e deverá escrever um poema em que cada verso aborda um dos temas.
                    Você deve usar um tom engraçado e sarcástico."""
)

response = client.models.generate_content(
    model="gemini-2.0-flash",
    config=generation_config,
    contents=["""Gere um poema sobre os seguintes temas:
            - Goiás
            - Jantinha
            - Cerrado
            - Família"""]
)

print(response.text)