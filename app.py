# --utf8-- 

"""
App do Flask com a regra de negócio aplicada de acordo com o test técnico
"""
from flask import Flask
from flask_restx import Api
from flask_jwt_extended import JWTManager
from models.GeosCrud import db
from resources.geospaciais import ItemResource, GeospatialSearch, UserRegistrationResource, UserAuthenticationResource

from config import config_by_name

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])
    
    db.init_app(app)  # Initialize SQLAlchemy with the Flask app
    
    api = Api(app, version="1.0", title='APIREST Itens geoespaciais', description='Desenvolvimento de APIREST para teste técnico.')
    
    jwt = JWTManager(app)
    
    @app.before_request
    def before_first_request():
        with app.app_context():
            db.create_all()

    
    def load_endpoint_uri():        
        api.add_resource(ItemResource, '/item/<string:id>') # crud da aplicação do item 
        api.add_resource(GeospatialSearch, '/geo-search') # buscar o um item por campo geométrico 
        api.add_resource(UserRegistrationResource, '/register')  # registro do usuário
        api.add_resource(UserAuthenticationResource, '/login')  # login do usuário
        
    load_endpoint_uri()
    
    return app

if __name__ == "__main__":
    app = create_app(config_name='development')
    app.run(host=app.config['IP_HOST'], port=app.config['PORT_HOST'], debug=app.config['DEBUG'])
