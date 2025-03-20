import anthropic

from dotenv import load_dotenv
import os

load_dotenv()

client = anthropic.Anthropic(api_key=os.getenv("CLAUDE_API_KEY"))

response = client.messages.create(
    model="claude-3-haiku-20240307",
    max_tokens=1800,
    temperature=1,
    system="""Você é um poeta escreve versos livres em português brasileiro.
                    Você irá receber diversos temas do usuário e deverá escrever um poema em que cada verso aborda um dos temas.
                    Você deve usar um tom engraçado e sarcástico.""",
    messages=[
        {"role": "user", 
        "content": """Gere um poema sobre os seguintes temas:
            - Goiás
            - Jantinha
            - Cerrado
            - Família"""}
    ]
)

print(response.content)
