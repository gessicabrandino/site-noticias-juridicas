# site-noticias-juridicas

Projeto final da disciplina Algoritmos de Automação, do curso MBA em Jornalismo de Dados, do Insper, tem como objetivo **automatizar o processo de checagem diária das notícias jurídicas do jornal Folha de S.Paulo** para produção das newsletters jurídicas do projeto FolhaJus por meio de um email automatizado.


**A solução seguirá os seguintes passos:**


* **Primeira etapa:** Criação de um código de raspagem das últimas notícias publicadas pela **Folha**, filtradas a partir de termos jurídicos;
* **Segunda etapa:** Conexão com o Google Sheets para armazenar, checar as notícias inéditas e com elas fazer uma lista de envio;
* **Terceira etapa:** Envio de um email pelo SendGrid para informar quais foram as últimas notícias.

As tarefas serão automatizadas por meio de um site dinâmico usando Flask e do agendador de tarefa Pipedream.
