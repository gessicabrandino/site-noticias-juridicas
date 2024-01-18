import os

import requests
import bs4
import datetime
import pandas as pd
import gspread
import oauth2client
from bs4 import BeautifulSoup
from oauth2client.service_account import ServiceAccountCredentials



#Conectando com a service account por meio da leitura do arquivo em Json

GOOGLE_SHEETS_CREDENTIALS = os.environ['GOOGLE_SHEETS_CREDENTIALS']
with open('credenciais.json', mode='w') as arquivo:
  arquivo.write(GOOGLE_SHEETS_CREDENTIALS)
conta = ServiceAccountCredentials.from_json_keyfile_name('credenciais.json')
api = gspread.authorize(conta)


#Acessando a página de última notícias da Folha

def raspa():
  site_Folha=requests.get('https://www1.folha.uol.com.br/ultimas-noticias/')
  bs=BeautifulSoup(site_Folha.content,'html.parser')
  noticias = bs.find_all('div', 'c-headline__content')
  ultimas_noticias = []
  for n in noticias:
    Link = n.find('a')['href']
    Manchete = n.find('h2').text
    Data = n.find('time')['datetime']
    ultimas_noticias.append({'Manchete': Manchete, 'Link': Link, 'Data': Data})
    ultimas_folha = pd.DataFrame(ultimas_noticias)
    ultimas_folha
  return ultimas_folha

def filtro(ultimas_folha):
  temas_juridicos = [
  'STF', 'Supremo', 'STJ', 'TSE','TRT','TRF','OAB','CNJ','Ministerio Publico','MPF','PF', 'Policia Federal','Defensoria','PGR','Procuradoria',
  'Justiça', 'juiz','advoga','promotor','procurador', 'desembargad', 'inelegi', 'reu','julga', 'tribuna', 'deci', 'condena', ' lei', 'leis','legali',
  'Moraes','Gilmar Mendes','Barroso','Rosa Weber', 'Carmen Lucia', 'Mendonca','Fachin', 'Toffoli', 'Kassio', 'Lewandowski','Fux', 'Aras', 'Zanin','Dino','Gonet',]
  string_temas = '|'.join(temas_juridicos)
  filtro_juridico = ultimas_folha['Manchete'].str.contains(string_temas)
  folhajus_noticias = ultimas_folha.loc[filtro_juridico].copy()
  folhajus = folhajus_noticias.values.tolist()
  return folhajus
  
#Acessando a planilha de trabalho

GOOGLE_SHEETS_KEY = os.environ['GOOGLE_SHEETS_KEY'] 
planilha = api.open_by_key(f'{GOOGLE_SHEETS_KEY}') 
sheet = planilha.worksheet('noticias')

#Verificando o que já está registrado na planilha

def noticias_novas(folhajus):
  checagem = sheet.get_all_values() 
  lista_envio=[]
  for n in folhajus:
    if n not in checagem:
      lista_envio.append(n)
      checagem.append(n)
      sheet.append_rows([n])
  df_lista_envio = pd.DataFrame(lista_envio)
  df_lista_envio.columns=['Manchete','Link','Data']
  df_lista_envio.set_index('Manchete')
  return df_lista_envio
