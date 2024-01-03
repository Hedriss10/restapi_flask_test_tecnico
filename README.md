## Desenvolvimento de API REST com Flask 



### Inicializando o projeto 🔧 🔨 ⚙️

*Para inicializar o projeto em sua máquina é de extrema importância que você siga os passos desde `readme` para que não acontece nenhum erro inesperado.*


### Configuracão do docker: 🔧 🐳


Se deseja ter controle sobre as configurações do contêiner Docker, como a ``porta``, ``usuário`` e ``senha``, é necessário acessar a documentação de desenvolvimento e configuração de ambiente do projeto. Para isso, clique <a href="docs/preview.md">aqui</a>.

Se optar pela instalação padrão do projeto é simplesmente executar no terminal, execute os seguintes comandos:

**Construa a imagem e inicie o contêiner.**

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

---

### Clonado o projeto e configurando as intalacões do Python: 🐍🔎💻

Configuracão do Python o projeto foi desenvolvido com package <a href="https://pypi.org/">pypi</a>

Mas citar e mostrar como você instalar as depedências com este instalador de pacote.

**Criando seu ambiente virtual**
```bash
python -m venv env # or venv 
```
De acordo com o comando ele irá criar um venv ou env de sua preferência dentro da pasta que deseja clonar este projeto.

**Clonando este projeto**
```bash
git clone https://github.com/Hedriss10/restapi_flask_test_tecnico.git
```
Clonando com web URL mas você pode também clona via ``ssh`` ou ``GitHub CLI` fique de acordo com sua preferência.


**Instalando as dependências**
```bash
pip install -r requirements.txt
```
De acordo com o ``requiremenets.txt`` ele é o responsável para manter os `frameworks` na nossa aplicação.

---

### Como executar o projeto 🖥️🌐

Para excutar o servidor da `api` abra o terminal no diretório que clonou o projeto digita o seguintes comandos: 


```bash
$env:FLASK_ENV = "development"
``` 

Definindo o `run.py`
```bash
$env:FLASK_APP = "run"
```

Com o Debugger ativo! (axuliar de erros)
```bash 
python run.py 
```











