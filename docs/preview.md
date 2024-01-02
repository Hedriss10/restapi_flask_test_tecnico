## Configurações de Ambiente do projeto 

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


Para iniciar o **PostgreSQL**, execute o seguinte comando no terminal:

```
docker up -d 
```
