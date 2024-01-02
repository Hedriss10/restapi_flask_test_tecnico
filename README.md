## Desenvolvimento de API REST com Flask 



### Inicializando o projeto 🔧 🔨 ⚙️

*Para iniciar o projeto com o banco de dados postgres é necessario buildar uma imagem no docker e com isso proseguir o cosumo da `APIREST` é ncessário que seguir as regras de comando para que não aconteca algum erro inesperado:*


**Configurando o Ambiente PostgreSQL com Docker 🔧 🐳**

Crie um arquivo chamado `Dockerfile` sem extensão e passa a seguintes credenciais:

```
FROM postgres:latest

ENV POSTGRES_PASSWORD=1234

ENV POSTGRES_DB=apirestflask
ENV POSTGRES_USER=root
```

Este Dockerfile configura um contêiner ``PostgreSQL`` 


Crie um arquivo chamado ``docker-compose.yml``

```
version: '3'
services:
  postgres:
    build:
      context: .
      dockerfile: Dockerfile
    ports:
      - "5432:5432"
    volumes:
      - ./database:/var/lib/postgresql/data
    environment:
      POSTGRES_PASSWORD: 1234
      POSTGRES_DB: apirestflask
      POSTGRES_USER: root
```





















