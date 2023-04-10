#Notícias jurídicas

Projeto final da disciplina Algoritmos de Automação, do curso MBA em Jornalismo de Dados, do Insper, consiste em um email automatizado com as notícias jurídicas do jornal **Folha de S.Paulo*** para produção das newsletters e atualização do índice [FolhaJus](https://www1.folha.uol.com.br/poder/folhajus/).


**A solução seguirá os seguintes passos:**


* Raspagem das últimas notícias publicadas pela **Folha** , filtradas a partir de termos jurídicos;
* Conexão com o Google Sheets para armazenar, checar as notícias inéditas e com elas fazer uma lista de envio;
* Envio de um email diário pela manhã usando o SendGrid com a lista de notícias obtida.
* As tarefas foram automatizadas por meio [deste site no Render](https://noticias-juridicas.onrender.com/), criado com o Flask. Por meio do Pipedream, a página **/carteiro** será acionada às 8h para que o e-mail seja enviado.


**O repositório contém os arquivos:**

* **requirements.txt** com as bibliotecas usadas no código;
* **raspagem.py** com as funções que realizam a raspagem das notícias e armazenagem no Sheets; 
* **carta_folhajus.py** com a função que envia o email;  
* **app.py** cria a página Site Notícias Jurícias no Render usando Flask e automatiza o envio do email.
