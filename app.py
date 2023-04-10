import requests
from flask import Flask, request

from raspagem import raspa, filtro, noticias_novas
from email import envia_email

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

@app.route("/coleta") #Função para raspar e filtras notícias
def coleta():
  
@app.route("/carteiro") #Função para formatar a mensagem em html e mandar por email
def carteiro():
  df = noticias_novas(filtro(raspagem()))
  envia_email(df)
  return 'E-mail enviado'

