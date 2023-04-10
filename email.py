import os

import sendgrid
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail, Email, To, Content


from raspagem import noticias_novas, filtro, raspagem

SENDGRID_API_KEY = os.environ['SENDGRID_API_KEY']

carteiro = sendgrid.SendGridAPIClient(api_key=SENDGRID_API_KEY)

def envia_email(df):
  carteiro = sendgrid.SendGridAPIClient(api_key=key)
  folhajus_html = df.to_html()

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
      To('filhodeosires@gmail.com')],
      'FolhaJus: Notícias jurídicas da Folha',
      Content('text/html', folhajus_email)
      )

  resposta = carteiro.client.mail.send.post(request_body=mensagem.get())
  return resposta.status_code
