# --utf8-- 

"""
Script para configurar o engine do Flask 
e com isso iremos colocar a regra de negocio com a as informações de execução.
"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from config import app_active, app_config


# criando o app
def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(app_config[config_name])
    app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql://root:1234@localhost/apirestflask'