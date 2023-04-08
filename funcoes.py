#Funções para o projeto de automação

#Funções para coletar notícias

def obter_noticias_folha():
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


def filtrar_noticias_juridicas(df, temas):
    string_temas = '|'.join(temas)
    filtro_juridico = df['Manchete'].str.contains(string_temas)
    folhajus_noticias = df.loc[filtro_juridico].copy()
    return folhajus_noticias

def converter_para_lista(df):
    lista_resultados = df.values.tolist()
    return lista_resultados

#Função etapa de planilha:

def atualizar_planilha(planilha, folhajus):
    sheet = planilha.worksheet('noticias')
    checagem = sheet.get_all_values()
    lista_envio = []
    for n in folhajus:
        if n not in checagem:
            lista_envio.append(n)
            checagem.append(n)
            sheet.append_rows([n])

    # Transformando a lista em DataFrame
    df_lista_envio = pd.DataFrame(lista_envio)
    df_lista_envio.columns = ['Manchete', 'Link', 'Data']
    df_lista_envio.set_index('Manchete')

    return df_lista_envio


#Funções para envio de email

def criar_mensagem_email(df_lista_envio):
    # Transformando o DataFrame em um HTML para envio por email via SendGrid
    folhajus_html = df_lista_envio.to_html()
    # Formatando a mensagem de email
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

    return mensagem


def enviar_email(carteiro, mensagem):
    resposta = carteiro.client.mail.send.post(request_body=mensagem.get())
    print(resposta.status_code)
