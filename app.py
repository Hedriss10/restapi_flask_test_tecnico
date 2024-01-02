# --utf8-- 

"""
Script para configurar o engine do Flask 
e com isso iremos colocar a regra de negocio com a as informações de execução.
"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from config import app_active, app_config
from models.GeosCrud import GeosCrud

# Variavel de controle de desenvolvimento
config = app_config[app_active]


# criando o app
def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(app_config[config_name])
    app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql://root:1234@localhost/apirestflask'
    app.config["SQLACLHEMY_TRACK_MODIFICATIONS"] = True
    
    db = SQLAlchemy(app)
    api = Api(app)
    
    @app.before_request
    def create_database():
        db.create_all()


    def load_endpoint_uri():
        print("Executando o load_endpoint dos recursos da api")
        api.add_resource(GeosCrud, "/item")
        
        
        
    load_endpoint_uri()
    
    return app
        
if __name__ == "__main__":
    app = create_app(app_active)
    config.APP.run(host=config.IP_HOST, port=config.PORT_HOST, debug=True)