import os

import gspread
import oauth2client
import requests
import bs4
import datetime
from bs4 import BeautifulSoup
from flask import Flask, request
from oauth2client.service_account import ServiceAccountCredentials


GOOGLE_SHEETS_KEY = os.environ["GOOGLE_SHEETS_KEY"] 

GOOGLE_SHEETS_CREDENTIALS = os.environ["GOOGLE_SHEETS_CREDENTIALS"]
with open("credenciais.json", mode="w") as arquivo:
  arquivo.write(GOOGLE_SHEETS_CREDENTIALS)
conta = ServiceAccountCredentials.from_json_keyfile_name("credenciais.json")
api = gspread.authorize(conta)
planilha = api.open_by_key(f"{GOOGLE_SHEETS_KEY}")
sheet = planilha.worksheet("Sheet1")

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
  return menu + "Esse site foi criado pela jornalista Géssica Brandino para auxiliar na produção das newsletters do projeto FolhaJus, que reúne o conteúdo jurídico da Folha. Para receber, entre no site do jornal e faça o cadastro."

@app.route("/contato")
def contato():
  return menu + "Sugestões, escreva para: gessica.brandino@grupofolha.com.br"

@app.route("/carteiro"
def carteiro():
           
