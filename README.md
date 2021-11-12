<!-- Logo do Projeto -->
<div align="center">
	<img width=100% src="docs/assets/logo-2.png" alt="Flux" class="lg">
</div>

<h1 align="center"> Flux </h1>

<!-- Descrição sobre o Projeto -->

## Sobre o Projeto

<p align="justify">&emsp; &emsp; Nossa intenção é criar um meio de aumentar a produtividade dos microempreendedores através de uma plataforma simples e intuitiva, que permite o registro de vendas e compras, e notifica o usuário sobre os clientes com dívidas pendentes.</p>

<!-- Funcionalidades -->

## Funcionalidades Principais

1. #### Cadastro de compras e vendas realizadas
1. #### Criação de perfil de clientes com suas informações
1. #### Destaque dos clientes com dívidas abertas
1. #### Histórico de transações cadastradas

## Tecnologias utilizadas

<div>
<img align="center" alt="Python" height="30" width="40" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg"> Python 3.9.6
</div> 
<p></p>
<div>
<img align="center" alt="Django" height="30" width="40" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/django/django-original.svg"> Django 3.2.6
</div>
<p></p>
<div>
<img align="center" alt="HTML" height="30" width="40" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/html5/html5-original.svg"> HTML 5
</div>
<p></p>
<div>
<img align="center" alt="JavaScript" height="30" width="40" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/javascript/javascript-original.svg"> JavaScript
</div>
<p></p>
<div>
<img align="center" alt="CSS" height="30" width="40" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/css3/css3-original.svg"> CSS 3
</div>
<p></p>
<div>
<img align="center" alt="Bootstrap" height="30" width="40" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/bootstrap/bootstrap-original.svg"> Bootstrap 4
</div>
<p></p>
<div>
<img align="center" alt="VSCode" height="30" width="40" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/vscode/vscode-original.svg"> Visual Studio Code
</div>
<p></p>
<div>
<img align="center" alt="PostgreSQL" height="30" width="40" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/postgresql/postgresql-original.svg"> PostgreSQL
</div>
<p></p>
<div>
<img align="center" alt="Heroku" height="30" width="40" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/heroku/heroku-original.svg"> Heroku
</div>
<p></p>

## Como contribuir

1. Crie um [Fork](https://docs.github.com/pt/get-started/quickstart/fork-a-repo) do repositório e clone-o
2. Baixe e instale o [Python v3.9.6](https://www.python.org/downloads/release/python-396/)
3. Crie um ambiente virtual para o projeto. Para isso, abra um terminal e digite: `python -m venv C:\ambientes\flux` <br></br>
   <img align="center" src="https://i.imgur.com/nh15r9a.png">
4. Abra a pasta _src_ do repositório no Visual Studio Code
5. Ative o ambiente virtual.

   - Para usar o terminal integrado do **VSCode** e ativar o ambiente virtual automaticamente, instale a extensão **Python** do mercado de extensões, clique na versão do python na barra inferior esquerda
     <br></br>
     <img align="center" src="https://imgur.com/qyU3WE1.png">
     <br></br>
     e selecione o seu interpretador (será necessário adicioná-lo à lista, selecionando a opção `Enter interpreter path...`)
     <br></br>
     <img align="center" src="https://imgur.com/4YhSleV.png">

6. Abra o terminal e digite `pip install -r requirements.txt` para instalar os requisitos da aplicação
7. Execute os seguintes comandos:
   ```
   py manage.py makemigrations
   py manage.py migrate
   py manage.py runserver
   ```
8. Acesse o servidor local em http://127.0.0.1:8000/
   <br></br>
   <img align="center" src="https://imgur.com/fECDxDO.png">
9. Para criar um usuário admin, execute `py manage.py createsuperuser`

## Desenvolvedores

<table>
	<tr>
		<td align="center"><a href="https://github.com/caiobsantos"><img src="docs/assets/team/caio.jpg" width="100px;" alt=""/><br /><sub><b>Caio Santos</b></sub></a><br /><a href="https://github.com/caiobsantos"></a></td>
		<td align="center"><a href="https://github.com/jusnim7"><img src="https://avatars.githubusercontent.com/u/65057466?v=4" width="100px;" alt=""/><br /><sub><b>Valderson Junior</b></sub></a><br /><a href="https://github.com/jusnim7"></a></td>
		<td align="center"><a href="https://github.com/viniciusroriz"><img src="docs/assets/team/vinicius.jpg" width="100px;" alt=""/><br /><sub><b>Vinícius Roriz</b></sub></a><br /><a href="https://github.com/fowardshift"></a></td>
	</tr>
</table>

<!-- License -->

## License

AGPLv3 © Flux. Para demais informações acesse nossa [LICENSE](./LICENSE).
