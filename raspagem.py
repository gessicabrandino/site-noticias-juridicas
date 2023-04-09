import requests
import bs4
import datetime
import pandas as pd
from bs4 import BeautifulSoup

#Acessando a página de última notícias da Folha

def raspagem_noticias():
        site_Folha = requests.get('https://www1.folha.uol.com.br/ultimas-noticias/')
        bs = BeautifulSoup(site_Folha.content,'html.parser')

        noticias = bs.find_all('div', 'c-headline__content')
        ultimas_noticias = []
        for n in noticias:
            Link = n.find('a')['href']
            Manchete = n.find('h2').text
            Data = n.find('time')['datetime']
            ultimas_noticias.append({'Manchete': Manchete, 'Link': Link, 'Data': Data})

        ultimas_folha = pd.DataFrame(ultimas_noticias)
        return ultimas_folha

#Lista de termos para procurar nos títulos

temas_juridicos = [
  'STF', 'Supremo', 'STJ', 'TSE','TRT','TRF','OAB','CNJ','Ministerio Publico','MP','PF', 'Polícia Federal','Defensoria','PGR','Procuradoria',
  'Justiça', 'juiz','advoga','promotor','procurador','julga', 'tribuna', 'deci', 'condena', 'lei ','legali',
  'Moraes','Gilmar Mendes','Barroso','Rosa Weber', 'Carmen Lucia', 'Mendonca','Fachin', 'Toffoli', 'Kassio', 'Lewandowski','Fux', 'Aras',
]

string_temas = '|'.join(temas_juridicos)

#Criação e aplicação do filtro com os termos da lista

filtro_juridico = ultimas_folha['Manchete'].str.contains(string_temas)

folhajus_noticias = ultimas_folha.loc[filtro_juridico].copy()

#Convertendo o dataframe em uma lista com os resultados obtidos para conexão com o Google Sheets

folhajus = folhajus_noticias.values.tolist()
