from langchain.chat_models import init_chat_model
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import SystemMessage

from dotenv import load_dotenv
import os

load_dotenv()

#model = init_chat_model("gpt-4o-mini", model_provider="openai", api_key=os.getenv("OPENAI_API_KEY"))
model = init_chat_model("gemini-2.0-flash", model_provider="google_genai", api_key=os.getenv("GEMINI_API_KEY"))

template = ChatPromptTemplate([
    SystemMessage("""Você é um poeta escreve versos livres em português brasileiro.
                    Você irá receber diversos temas do usuário e deverá escrever um poema em que cada verso aborda um dos temas.
                    Você tem um tom engraçado e sarcástico."""),
    ("human", "{user_input}")
])

prompt = template.invoke({
  "user_input": """Gere um poema sobre os seguintes temas:
            - Goiás
            - Jantinha
            - Cerrado
            - Família"""
})

response = model.invoke(prompt)
print(response.content)
