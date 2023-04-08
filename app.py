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

@app.route("/coleta")
def coleta():
  
import raspagem
import planilha

@app.route("/carteiro")
def carteiro():
  
import email          
