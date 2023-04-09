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

import raspagem
from arquivo import df_lista_envio

SENDGRID_API_KEY = os.environ['SENDGRID_API_KEY']

#Criando objeto responsável por enviar os emails

carteiro = sendgrid.SendGridAPIClient(api_key=key)

#Transformando o DataFrame em um HTML para envio por email via SendGrid

folhajus_html = df_lista_envio.to_html()
folhajus_html

#Formatando mensagem de email

titulo = 'Notícias FolhaJus'
abre = 'Olá, essas foram as últimas notícias jurídicas publicadas na Folha:'
fecha = f'Acesse <a href="https://www1.folha.uol.com.br/poder/folhajus/">Folhajus</a> e saiba como receber as newsletters FolhaJus Dia e FolhaJus+.'

folhajus_email = f"""
<html>
  <body>
    <b>{titulo}</b>
    <p>{abre}</p>
    {folhajus_html}
    <p>{fecha}</p>
  </body>
</html>
"""

mensagem = Mail(
    Email('gessica.brandino@grupofolha.com.br'),
    [To('ge.brandino@gmail.com'),
     To('alvarojusten@gmail.com')],
    'FolhaJus: Notícias jurídicas da Folha',
    Content('text/html', folhajus_email)
    )

#Acionando o envio da mensagem

resposta = carteiro.client.mail.send.post(request_body=mensagem.get())
print(resposta.status_code)
