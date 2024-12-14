*Projeto MVP - Back End - *Minha Estante*

Esse projeto faz parte do trabalho da Disciplina de Full Stack Básico do Curso de Engenharia de Software da PUC-Rio.

# Objetivo e Funcionalidades

O presente projeto tem por objetivo criar uma API para que o usuário possa inserir os dados dos livros que leu ou está lendo. Tem objetivo pessoal e não comercial.

# Documentos

Compõem esse projeto os arquivos abaixo:
- app.py -> Arquivo principal, onde a aplicacão é inciada. Define configuracões e rotas da API.
- Pasta schemas e arquivos -> Definem a estrutura e os tipos de dados que devem ser enviados e recebidos via requisição HTTP.
- Pasta models e arquivos -> 


# Como executar 


É necessário ter todas as bibliotecas python listadas no `requirements.txt` instaladas.

Clicar com o botão direito do mouse na pasta principal e abrir o Terminal Integrado.

Colcar o código abaixo para instalar as bibliotecas listadas em requirements.txt. 

pip install -r requirements.txt




Para executar a API  basta executar:


flask run --host 0.0.0.0 --port 5000

Após isso basta abrir o link http://localhost:5000 no navegador e executar o Swagger.


