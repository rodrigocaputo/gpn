# GPN
Gerenciador de Publicidade e Notícias para painel de senha.

## Instalação

- Clone o repositório localmente: `git clone https://github.com/rodrigocaputo/gpn.git`

- Defina um arquivo `params.env` inserindo os dados de usuário, senha, banco de dados e senha do root
> Siga o formato do arquivo `params.env.sample`.

- Inicie os serviços com o comando: `docker-compose up`
> Usuários do Docker Toolbox devem utilizar o Docker Quickstart Terminal

- Através do navegador, acesse o endereço: `localhost:8000`
> Usuários do Docker Toolbox devem expor a porta 8000 da sua docker machine no VirtualBox
