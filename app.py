from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
  return "Olá! Bem-vindo ao site que automatiza a coleta de notícias jurídicas publicadas pelo jornal Folha de S.Paulo."

@app.route("/sobre")
def sobre():
  return "Esse site foi criado pela jornalista Géssica Brandino para produzir as newsletters do projeto FolhaJus, que reúne o conteúdo jurídico publicado pela Folha. Para receber, entre no site do jornal e faça o cadastro."

@app.route("/contato")
def contato():
  return "Sugestões, escreva para: gessica.brandino@grupofolha.com.br"
