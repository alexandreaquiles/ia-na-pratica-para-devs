from dotenv import load_dotenv
import os
import smtplib
from email.message import EmailMessage
import pandas as pd

load_dotenv()

def carrega_csv(nome_do_arquivo):
    try:
        return pd.read_csv(nome_do_arquivo)
    except IOError as e:
        print(f"Erro no carregamento de arquivo: {e}")
        return None

def carrega_arquivos(diretorio):
    emails = {}
    for root, dirs, files in os.walk(diretorio):
        if root == diretorio:
          for file in files:
                file_path = os.path.join(root, file)
                basename, extension = os.path.splitext(file)
                with open(file_path, "r") as f:
                  emails[basename] = f.read()
    return emails

sender = "Suporte Hare Express <suporte@hare-express.com>"

reviews = carrega_csv("reviews-entrega-MercadoAgil.csv")
reviews = reviews[['reviewer_id', 'reviewer_name', 'reviewer_email', 'review_text']]

emails_reviews = carrega_arquivos("emails-reviews")

if not emails_reviews:
  print("Não há emails para enviar no momento!")
else:

  for id in emails_reviews:
    review = reviews.loc[reviews["reviewer_id"] == id]
    reviewer_name = review["reviewer_name"].values[0]
    reviewer_email = review["reviewer_email"].values[0]

    receiver = f"{reviewer_name} <{reviewer_email}>"

    msg = EmailMessage()
    msg.set_content(emails_reviews[id])
    msg['Subject'] = "Entrega Mercado Ágil"
    msg['From'] = sender
    msg['To'] = receiver

    with smtplib.SMTP("sandbox.smtp.mailtrap.io", 2525) as server:
      server.starttls()
      server.login(os.getenv("EMAIL_USER"), os.getenv("EMAIL_PASSWORD"))
      try:
        server.send_message(msg)
        print(f"Email enviado para {receiver}")
        os.rename(f"emails-reviews/{id}.txt", f"emails-reviews/enviados/{id}.txt")
      except Exception as e:
        print(f"Erro ao enviar email para {receiver}: {e}")
