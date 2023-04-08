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

#As três etapas do código

import raspagem
import planilha
import email

#Variáveis de ambiente do Render
GOOGLE_SHEETS_CREDENTIALS = os.environ['GOOGLE_SHEETS_CREDENTIALS']
GOOGLE_SHEETS_KEY = os.environ['GOOGLE_SHEETS_KEY'] 
SENDGRID_API_KEY = os.environ['SENDGRID_API_KEY']

#Configurando o site

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

@app.route("/coleta") #Roda o código que está nos arquivos Raspagem e Planilha para raspar as notícias e atualizar a planilha
def coleta():
 
  
@app.route("/carteiro") #Roda o código do arquivo Email para enviar as mensagens
def carteiro():

