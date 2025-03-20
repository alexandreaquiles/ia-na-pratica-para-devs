from dotenv import load_dotenv
import os
import json
import pandas as pd

import google.generativeai as genai

load_dotenv()

genai.configure(api_key=os.environ["GEMINI_API_KEY"])
generation_config = {
  "temperature": 0,
  "response_mime_type": "text/plain",
}
modelo = "gemini-2.0-flash"

def carrega_csv(nome_do_arquivo):
    try:
        return pd.read_csv(nome_do_arquivo)
    except IOError as e:
        print(f"Erro no carregamento de arquivo: {e}")
        return None

def carrega(nome_do_arquivo):
    try:
        with open(nome_do_arquivo, "r") as arquivo:
            dados = arquivo.read()
            return dados
    except IOError as e:
        print(f"Erro: {e}")

def salva(nome_do_arquivo, conteudo):
    try:
        with open(nome_do_arquivo, "w", encoding="utf-8") as arquivo:
            arquivo.write(conteudo)
    except IOError as e:
        print(f"Erro ao salvar arquivo: {e}")

import json
import os

def carrega_arquivos_json(diretorio):
    dados = []
    for root, dirs, files in os.walk(diretorio):
        for file in files:
            if file.endswith(".json"):
                file_path = os.path.join(root, file)
                with open(file_path, "r") as f:
                    json_data = json.load(f) 
                    dados.append(json_data)
    return dados



def gera_email(analise):
  prompt_sistema = """
  Você é um assistente de satisfação do cliente da empresa Hare Express.
  Você tem um tom de voz amigável e carinhoso.
  
  A Hare Express é uma empresa de entrega inovadora fundada por um grupo de ex-atletas olímpicos de corrida que utiliza uma combinação única de corredores ágeis e tecnologia de ponta para garantir entregas ultrarrápidas e eco-friendly em áreas urbanas.

  Seu email é: suporte@hare-express.com

  Você deve gerar o corpo de resposta de um email para clientes insatisfeitos com a entrega de nosso parceiro, o ecommerce Mercado Ágil.

  Ofereça ajuda para o contexto da mensagem do cliente e sugira o envio de um voucher em um email posterior para que a próxima entrega seja gratuita.
    """
  
  cliente = genai.GenerativeModel(
      model_name = modelo,
      generation_config=generation_config,
      system_instruction = prompt_sistema )
  
  prompt_usuario = f"""
  Nome do cliente: {analise["reviewer_name"]}
  Email do cliente: {analise["reviewer_email"]}
  Avaliação do cliente: {analise["review_text"]}
  """

  resposta = cliente.generate_content(prompt_usuario)

  return resposta.text

reviews = carrega_csv("reviews-entrega-MercadoAgil.csv")
reviews = reviews[['reviewer_id', 'reviewer_name', 'reviewer_email', 'review_text']]

lista_analises = carrega_arquivos_json("analises-reviews")

os.makedirs("emails-reviews", exist_ok=True)

i = 0
for analise in lista_analises:
  if int(analise["nota"]) < 0 and analise["sentimento"].lower() == "negativo":
    id = analise["reviewer_id"]
    review_text = reviews.loc[reviews["reviewer_id"] == id]["review_text"].values[0]
    analise["review_text"] = review_text
    email = gera_email(analise)
    salva(f"./emails-reviews/{id}.txt", email)
