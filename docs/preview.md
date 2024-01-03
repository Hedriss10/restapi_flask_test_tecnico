## Configurações de Ambiente do projeto 

**Configurando o Ambiente PostgreSQL com Docker 🔧 🐳**

Certamente! Vamos criar um passo a passo para criar e executar um contêiner PostgreSQL usando Docker e Docker Compose.

**Crie o arquivo `Dockerfile`.**

Abra seu editor de texto favorito e crie um arquivo chamado `Dockerfile` no diretório do seu projeto com o seguinte conteúdo:

```Dockerfile
# Dockerfile
FROM postgis/postgis:latest


ENV POSTGRES_DB=flaskrestapi
ENV POSTGRES_USER=root
ENV POSTGRES_PASSWORD=1234

```

Este `Dockerfile` usa a imagem oficial do PostgreSQL e define as variáveis de ambiente necessárias.

**Crie o arquivo `docker-compose.yml`.**

Crie um arquivo chamado `docker-compose.yml` no mesmo diretório com o seguinte conteúdo:

```yaml
# docker-compose.yml
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

Este arquivo `docker-compose.yml` define o serviço PostgreSQL, especificando a construção a partir do `Dockerfile`, a porta mapeada para o host, volumes para persistência de dados, e as variáveis de ambiente.

**Construa a imagem e inicie o contêiner.**

No terminal, execute os seguintes comandos:

```bash
docker-compose build
docker-compose up -d
```

O primeiro comando construirá a imagem do PostgreSQL com base no `Dockerfile`, e o segundo iniciará o contêiner em segundo plano.

**Verifique o status do contêiner.**

Para verificar se o contêiner está em execução, use o seguinte comando:

```bash
docker ps
```

Você deve ver uma saída que inclui o seu contêiner PostgreSQL em execução.

**Conecte-se ao PostgreSQL.**

Você pode usar uma ferramenta de administração de banco de dados, como o `psql` ou uma ferramenta gráfica como o pgAdmin, para se conectar ao PostgreSQL. Use as seguintes configurações:

- Host: `localhost`
- Porta: `5432`
- Nome do banco de dados: `apirestflask`
- Nome do usuário: `root`
- Senha: `1234`

**Pare e remova o contêiner.**

Quando você terminar de usar o contêiner, pare e remova-o com o seguinte comando:

```bash
docker-compose down
```
(Opcional)