import os

import requests
import bs4
import datetime
import pandas as pd
import gspread
import oauth2client
from bs4 import BeautifulSoup
from oauth2client.service_account import ServiceAccountCredentials

import raspagem

#Conectando com a service account por meio da leitura do arquivo em Json

GOOGLE_SHEETS_CREDENTIALS = os.environ['GOOGLE_SHEETS_CREDENTIALS']
with open('credenciais.json', mode='w') as arquivo:
  arquivo.write(GOOGLE_SHEETS_CREDENTIALS)
conta = ServiceAccountCredentials.from_json_keyfile_name('credenciais.json')
api = gspread.authorize(conta)

#Acessando a planilha de trabalho

GOOGLE_SHEETS_KEY = os.environ['GOOGLE_SHEETS_KEY'] 
planilha = api.open_by_key(f'{GOOGLE_SHEETS_KEY}') 

#nome da planilha com os dados

sheet = planilha.worksheet('noticias')

#Verificando o que já está registrado na planilha

checagem = sheet.get_all_values()

#Cria uma lista de envio com as notícias e atualiza a planilha com as manchetes que ainda não constam

lista_envio=[]
for n in folhajus:
  if n not in checagem:
    lista_envio.append(n)
    checagem.append(n)
    sheet.append_rows([n])

#Transformando a lista em DataFrame

df_lista_envio = pd.DataFrame(lista_envio)
df_lista_envio.columns=['Manchete','Link','Data']
df_lista_envio.set_index('Manchete')
