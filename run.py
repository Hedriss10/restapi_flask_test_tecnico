from app import create_app
from config import flask_env  # importando a variavel do Flask 

if __name__ == "__main__":
    app = create_app(config_name=flask_env)  # Passando o app do Flask como parametro 
    app.run(host=app.config['IP_HOST'], port=app.config['PORT_HOST'], debug=app.config['DEBUG'])
