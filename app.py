import requests
import sendgrid
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail, Email, To, Content
from flask import Flask, request

from raspagem import raspa, filtro, noticias_novas
import carta_folhajus

#Configurando o site com o Flask

app = Flask(__name__)

menu = """
<a href="/">Página inicial</a> | <a href="/sobre">Sobre</a> | <a href="/contato">Contato</a>
<br>
"""

@app.route("/")
def index():
  return menu + "Bem-vindo ao site que coleta notícias jurídicas da Folha de S.Paulo."

@app.route("/sobre")
def sobre():
  return menu + "Esse site foi criado pela jornalista Géssica Brandino para auxiliar na produção das newsletters do projeto FolhaJus, que reúne o conteúdo jurídico da Folha. Para mais informações, acesse o site do jornal."

@app.route("/contato")
def contato():
  return menu + "Sugestões, escreva para: gessica.brandino@grupofolha.com.br"

@app.route("/carteiro")
def carteiro():
  try:
    raspagem = raspa()
    filtrados = filtro(raspagem)
    novas = noticias_novas(filtrados)
    carta_folhajus.envia_email(novas)
  except:
    folhajus_email = "Não há notícias novas"
    mensagem = Mail(
      Email('gessica.brandino@grupofolha.com.br'),
      [To('ge.brandino@gmail.com'),   
      To('alvarojusten@gmail.com')],
      'FolhaJus: Notícias jurídicas da Folha',
      Content('text/html', folhajus_email)
      )
    resposta = carteiro.client.mail.send.post(request_body=mensagem.get())
  return 'ok'
