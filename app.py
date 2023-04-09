import os

import gspread
import oauth2client
import requests
import bs4
import datetime
import pandas as pd
import sendgrid
from bs4 import BeautifulSoup
from flask import Flask, request
from oauth2client.service_account import ServiceAccountCredentials
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail, Email, To, Content


#Fazendo a conexão com o Google Sheets

GOOGLE_SHEETS_KEY = os.environ['GOOGLE_SHEETS_KEY'] 

GOOGLE_SHEETS_CREDENTIALS = os.environ['GOOGLE_SHEETS_CREDENTIALS']
with open('credenciais.json', mode='w') as arquivo:
  arquivo.write(GOOGLE_SHEETS_CREDENTIALS)
conta = ServiceAccountCredentials.from_json_keyfile_name('credenciais.json')

api = gspread.authorize(conta)
planilha = api.open_by_key(f'{GOOGLE_SHEETS_KEY}') 
sheet = planilha.worksheet('noticias')

#Fazendo a conexão com o Sendgrid

SENDGRID_API_KEY = os.environ['SENDGRID_API_KEY']
carteiro = sendgrid.SendGridAPIClient(api_key = SENDGRID_API_KEY)


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
  

@app.route("/arquivo") #Função para guardar as notícias em uma planilha e gerar a lista de envio
def arquivo():
 

@app.route("/carteiro") #Função para formatar a mensagem em html e mandar por email
def carteiro():

